"""Provider layer: one ``chat()`` interface, backend selected by the ``provider/...`` prefix.

- ``openai/...``   -> the real OpenAI API (Tim has credits). Used by the conversation models AND
                      the stage-2 judge.
- ``local/...``    -> a self-hosted, OpenAI-compatible endpoint (vLLM / Openweights deploy) named
                      by ``LOCAL_BASE_URL`` + ``LOCAL_API_KEY``. Used to serve open-weight models
                      and LoRA adapters on a rented GPU. Shares the exact same Chat Completions code
                      path (retry/backoff, length escalation) as ``openai/`` — only the client
                      differs — so the ``openai/`` judge keeps hitting real OpenAI in the same run.
- ``openrouter/...`` -> a deliberate stub; adding it later is a one-function change.
"""

from __future__ import annotations

import os
import re
import time

import openai
from dotenv import load_dotenv

load_dotenv()  # read OPENAI_API_KEY from .env at repo root

_DEFAULT_RETRIES = 3
# Request timeout. 120s (the clone's value) is too short for a local batched server: with ~45
# concurrent conversations a length-escalated turn (up to _LENGTH_RETRY_CEILING tokens) can take
# >10 min of wall clock, and timing it out throws away the whole generation and retries it —
# a livelock that killed entire conditions. Override with REQUEST_TIMEOUT.
_REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", "900"))
# A turn cut off by the token cap (finish_reason=length) is bad data — either EMPTY (reasoning
# ate the whole max_completion_tokens budget) or TRUNCATED mid-reply. Both corrupt the transcript
# and the next turn's context, so we escalate the budget (x3) up to this ceiling and retry until
# the turn completes (finish_reason=stop). max_completion_tokens is only a CAP (you're billed for
# tokens actually generated), so a high ceiling costs nothing for normal turns.
_LENGTH_RETRY_CEILING = 24576

_client: openai.OpenAI | None = None
_local_client: openai.OpenAI | None = None
_openrouter_client: openai.OpenAI | None = None

# Remember per-model API quirks so we don't re-incur a 400 + retry on EVERY call:
# models that reject `reasoning_effort` (non-reasoning, e.g. gpt-4o/4.1/5.3-chat) and models
# that need the legacy `max_tokens` instead of `max_completion_tokens`. Populated on first hit.
_NO_REASONING_EFFORT: set[str] = set()
_NEEDS_MAX_TOKENS: set[str] = set()


def _get_client() -> openai.OpenAI:
    """Lazily build the OpenAI client so importing this module never requires a key."""
    global _client
    if _client is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set (put it in .env at the repo root)")
        _client = openai.OpenAI(api_key=api_key, timeout=_REQUEST_TIMEOUT)
    return _client


def _get_local_client() -> openai.OpenAI:
    """Client for a self-hosted OpenAI-compatible endpoint (vLLM / Openweights deploy).

    ``LOCAL_BASE_URL`` is the endpoint (e.g. ``https://.../v1``). ``LOCAL_API_KEY`` is the key — a
    raw vLLM server ignores it (any non-empty string works), while an Openweights deploy needs the
    real one. Kept separate from the OpenAI client so ``openai/`` (incl. the judge) still routes to
    real OpenAI in the same run.
    """
    global _local_client
    if _local_client is None:
        base_url = os.environ.get("LOCAL_BASE_URL")
        if not base_url:
            raise RuntimeError(
                "LOCAL_BASE_URL not set (the vLLM/Openweights OpenAI-compatible /v1 endpoint)"
            )
        api_key = os.environ.get("LOCAL_API_KEY", "EMPTY")
        _local_client = openai.OpenAI(api_key=api_key, base_url=base_url, timeout=_REQUEST_TIMEOUT)
    return _local_client


def _get_openrouter_client() -> openai.OpenAI:
    """Client for OpenRouter (OpenAI-API-compatible). Reads OPENROUTER_API_KEY from .env. Model ids
    are vendor-prefixed, e.g. ``openrouter/openai/gpt-5.4`` -> OpenRouter model ``openai/gpt-5.4``."""
    global _openrouter_client
    if _openrouter_client is None:
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise RuntimeError("OPENROUTER_API_KEY not set (put it in .env at the repo root)")
        _openrouter_client = openai.OpenAI(
            api_key=api_key, base_url="https://openrouter.ai/api/v1", timeout=_REQUEST_TIMEOUT
        )
    return _openrouter_client


def chat(
    model: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    reasoning_effort: str | None = None,
) -> tuple[str, str | None]:
    """Dispatch a chat completion to the backend named by the ``provider/...`` prefix.

    ``model`` is provider-prefixed, e.g. ``"openai/gpt-5.2"`` or ``"openrouter/x-ai/grok-4.1"``.
    ``reasoning_effort`` (None | minimal | low | medium | high) controls hidden reasoning on
    reasoning models; it is ignored by models that don't support it.

    Returns ``(content, finish_reason)``. ``finish_reason`` is "stop" for a complete turn; it is
    "length" only if the turn was cut off even after escalating to the ceiling (lets callers audit
    that no turn in a run was truncated).
    """
    provider, _, model_id = model.partition("/")
    if not model_id:
        raise ValueError(f"model must be provider-prefixed, e.g. 'openai/gpt-5.2' (got {model!r})")

    if provider == "openai":
        return _chat_completions(
            _get_client(), model_id, messages, temperature, top_p, max_tokens, reasoning_effort
        )
    if provider == "local":
        # Open-weight / LoRA endpoints aren't reasoning models — never send reasoning_effort.
        return _local_chat(model_id, messages, temperature, top_p, max_tokens)
    if provider == "openrouter":
        # OpenRouter is OpenAI-compatible -> reuse the same retry/length machinery, just a different
        # client. model_id keeps its vendor prefix (e.g. "openai/gpt-5.4"). reasoning_effort passes
        # through; _create drops it if the model/route rejects it.
        return _chat_completions(
            _get_openrouter_client(), model_id, messages, temperature, top_p, max_tokens, reasoning_effort
        )
    raise ValueError(f"Unknown provider prefix {provider!r} in model {model!r}")


def _local_chat(
    model_id: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    attempts: int = 3,
    backoff: int = 10,
) -> tuple[str, str | None]:
    """Local endpoint with resilience to a vLLM pod that briefly dies/redeploys mid-run.

    A self-hosted pod can crash or be redeployed (new URL) mid-run; that surfaces as a 404 or a
    connection/5xx error. On those, we rebuild the client from a re-read ``.env`` (the orchestrator
    rewrites LOCAL_BASE_URL when it redeploys a fresh pod) and retry a few times. A persistent
    failure still raises after ``attempts`` so a dead endpoint doesn't hang the whole run forever.
    """
    global _local_client
    transient = ("404", "(500", "(502", "(503", "Connection", "connection", "timeout", "Timeout")
    for i in range(attempts):
        try:
            return _chat_completions(
                _get_local_client(), model_id, messages, temperature, top_p, max_tokens, None
            )
        except RuntimeError as e:
            if i == attempts - 1 or not any(s in str(e) for s in transient):
                raise
            print(f"    [local] endpoint error ({str(e)[:70]}); refreshing endpoint, retry {i + 1}/{attempts}")
            _local_client = None          # force rebuild
            load_dotenv(override=True)     # pick up a fresh LOCAL_BASE_URL if redeployed
            time.sleep(backoff)
    raise RuntimeError("local chat failed after retries")  # unreachable; for type-checkers


def _create(client, model_id, messages, temperature, top_p, max_tokens, reasoning_effort):
    """Single create() call, adapting to per-model API differences across model families.

    Handles three hard API distinctions (not experimental variables) so a mixed-model matrix
    "just works": the max_completion_tokens vs max_tokens split (newer vs older models), and
    non-reasoning models (gpt-4o/gpt-4.1) rejecting ``reasoning_effort``. On a BadRequestError
    that names an unsupported parameter, that parameter is swapped/dropped (with a notice) and the
    call retried. ``reasoning_effort`` dropped -> model uses its default. temperature/top_p are
    only dropped if the model rejects the requested value (won't trigger at the default 1.0).
    """
    kwargs = dict(model=model_id, messages=messages, temperature=temperature, top_p=top_p)
    if reasoning_effort is not None and model_id not in _NO_REASONING_EFFORT:
        kwargs["reasoning_effort"] = reasoning_effort
    token_param = "max_tokens" if model_id in _NEEDS_MAX_TOKENS else "max_completion_tokens"
    for _ in range(5):  # at most a few parameter adjustments
        try:
            return client.chat.completions.create(**kwargs, **{token_param: max_tokens})
        except openai.BadRequestError as e:
            msg = str(e).lower()
            if token_param == "max_completion_tokens" and "max_tokens" in msg:
                token_param = "max_tokens"
                _NEEDS_MAX_TOKENS.add(model_id)  # remember: don't re-try the wrong param next call
                continue
            if "reasoning_effort" in msg and "reasoning_effort" in kwargs:
                kwargs.pop("reasoning_effort")
                if model_id not in _NO_REASONING_EFFORT:  # log once, not per in-flight thread
                    _NO_REASONING_EFFORT.add(model_id)  # remember: stop sending it for this model
                    print(f"    [param] {model_id} rejects reasoning_effort — dropping it (cached, model default)")
                continue
            if "temperature" in msg and "temperature" in kwargs:
                kwargs.pop("temperature")
                print(f"    [param] {model_id} rejects temperature={temperature} — using model default")
                continue
            if "top_p" in msg and "top_p" in kwargs:
                kwargs.pop("top_p")
                print(f"    [param] {model_id} rejects top_p={top_p} — using model default")
                continue
            # Context-window overflow (mainly local vLLM, whose max_model_len is far smaller than
            # OpenAI's): the length-escalation can request more completion tokens than fit. The
            # server's error states the limit and the prompt size, so cap the completion to fit and
            # retry — a (possibly truncated) reply keeps the run alive instead of killing it with 400.
            if "maximum context length" in msg:
                lim = re.search(r"maximum context length is (\d+)", msg)
                used = re.search(r"\((\d+) in the messages", msg)
                if lim and used:
                    fitted = max(16, int(lim.group(1)) - int(used.group(1)) - 8)
                    if fitted < max_tokens:
                        print(f"    [ctx] {model_id}: completion capped {max_tokens}->{fitted} to fit {lim.group(1)}-tok window")
                        max_tokens = fitted
                        continue
                raise
            raise


def _chat_completions(
    client: openai.OpenAI,
    model_id: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    reasoning_effort: str | None = None,
    retries: int = _DEFAULT_RETRIES,
) -> tuple[str, str | None]:
    """Chat Completions (any OpenAI-compatible ``client``) with retry/backoff, 402/429 handling,
    and no-truncation escalation.

    A turn cut off by the token cap (finish_reason=length) — whether EMPTY (reasoning ate the
    budget) or TRUNCATED mid-reply — is bad data, so we escalate the budget (x3, up to
    _LENGTH_RETRY_CEILING) and retry until the turn completes (finish_reason=stop). Returns
    (content, finish_reason); finish_reason is "length" only if it still didn't fit at the ceiling.
    """
    budget = max_tokens
    ceiling = max(max_tokens, _LENGTH_RETRY_CEILING)
    while True:
        content, finish = _chat_call_once(
            client, model_id, messages, temperature, top_p, budget, reasoning_effort, retries
        )
        if finish != "length" or budget >= ceiling:
            if finish == "length":
                kind = "empty (reasoning ate budget)" if not content else "TRUNCATED reply"
                print(f"    [length cap] {model_id} {kind} even at ceiling {budget} — accepting as-is")
            return content, finish
        new_budget = min(budget * 3, ceiling)
        kind = "empty (reasoning ate budget)" if not content else "truncated reply"
        print(f"    [length cap] {model_id} {kind} at {budget} tokens; retrying with {new_budget}")
        budget = new_budget


def _chat_call_once(
    client: openai.OpenAI,
    model_id: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    reasoning_effort: str | None,
    retries: int,
) -> tuple[str, str | None]:
    """One logical completion (with network retry/backoff). Returns (content, finish_reason).

    - 402 (insufficient credits) -> raise immediately (fail fast).
    - 429 (rate limit) -> exponential backoff (attempt+1)*10s, then retry.
    - 5xx / timeout / connection -> short backoff, then retry.
    - other 4xx (bad request, auth, etc.) -> raise immediately (retrying is pointless).
    NOTE: temperature/top_p are passed through unchanged — they're load-bearing experimental
    variables, so an unsupported value surfaces as an error rather than being silently dropped.
    """
    last_error: str | None = None
    for attempt in range(retries):
        try:
            resp = _create(client, model_id, messages, temperature, top_p, max_tokens, reasoning_effort)
            choice = resp.choices[0]
            return choice.message.content or "", getattr(choice, "finish_reason", None)
        except openai.RateLimitError as e:  # 429
            wait = (attempt + 1) * 10
            print(f"    Rate limited (429), waiting {wait}s...")
            time.sleep(wait)
            last_error = str(e)
        except openai.APIStatusError as e:
            status = getattr(e, "status_code", None)
            if status == 402:
                raise RuntimeError(f"Insufficient credits (402): {e}") from e
            if status is not None and status >= 500:
                last_error = f"server error {status}: {e}"
                print(f"    {last_error}, retrying...")
                time.sleep(2)
            else:
                # 4xx that isn't 402/429 — permanent, fail fast.
                raise RuntimeError(f"OpenAI request failed ({status}): {e}") from e
        except (openai.APITimeoutError, openai.APIConnectionError) as e:
            last_error = str(e)
            print(f"    Connection/timeout error, retrying: {e}")
            time.sleep(5)
    raise RuntimeError(f"Failed after {retries} attempts: {last_error}")


# OpenRouter is served by _chat_completions with the OpenRouter client (see chat() dispatch above) —
# it's OpenAI-API-compatible, so no separate implementation is needed.
