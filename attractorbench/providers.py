"""Provider layer: one ``chat()`` interface, backend selected by the ``provider/...`` prefix.

v1 is OpenAI-only (Tim has OpenAI credits, no OpenRouter credits). The ``openrouter/`` prefix is
recognised by the dispatcher but its backend is a deliberate stub — adding OpenRouter later is a
one-function change (implement ``_openrouter_chat``).
"""

from __future__ import annotations

import os
import time

import openai
from dotenv import load_dotenv

load_dotenv()  # read OPENAI_API_KEY from .env at repo root

_DEFAULT_RETRIES = 3
_REQUEST_TIMEOUT = 120  # seconds, matches the clone
# Reasoning models share max_completion_tokens between hidden reasoning and the visible reply.
# On a rich turn, reasoning can consume the WHOLE budget -> an empty turn (finish_reason=length).
# When that happens we escalate the budget (x3) up to this ceiling and retry, so a degenerate
# empty turn is rescued. Truncated-but-non-empty turns are kept as-is (not escalated).
_EMPTY_RETRY_CEILING = 8192

_client: openai.OpenAI | None = None

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


def chat(
    model: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    reasoning_effort: str | None = None,
) -> str:
    """Dispatch a chat completion to the backend named by the ``provider/...`` prefix.

    ``model`` is provider-prefixed, e.g. ``"openai/gpt-5.2"`` or ``"openrouter/x-ai/grok-4.1"``.
    ``reasoning_effort`` (None | minimal | low | medium | high) controls hidden reasoning on
    reasoning models; it is ignored by models that don't support it. Returns the assistant text.
    """
    provider, _, model_id = model.partition("/")
    if not model_id:
        raise ValueError(f"model must be provider-prefixed, e.g. 'openai/gpt-5.2' (got {model!r})")

    if provider == "openai":
        return _openai_chat(model_id, messages, temperature, top_p, max_tokens, reasoning_effort)
    if provider == "openrouter":
        return _openrouter_chat(model_id, messages, temperature, top_p, max_tokens)
    raise ValueError(f"Unknown provider prefix {provider!r} in model {model!r}")


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
            raise


def _openai_chat(
    model_id: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
    reasoning_effort: str | None = None,
    retries: int = _DEFAULT_RETRIES,
) -> str:
    """OpenAI Chat Completions with retry/backoff, 402/429 handling, and empty-turn rescue.

    On reasoning models a turn can come back EMPTY because hidden reasoning ate the whole
    max_completion_tokens budget (finish_reason=length). We escalate the budget (x3, up to
    _EMPTY_RETRY_CEILING) and retry so the visible reply gets room. Truncated-but-non-empty
    turns are accepted as-is.
    """
    budget = max_tokens
    ceiling = max(max_tokens, _EMPTY_RETRY_CEILING)
    while True:
        content, finish = _openai_call_once(
            model_id, messages, temperature, top_p, budget, reasoning_effort, retries
        )
        if content or finish != "length" or budget >= ceiling:
            if not content and finish == "length":
                print(
                    f"    [empty output] {model_id} filled {budget} tokens with reasoning and still "
                    f"returned nothing — lower reasoning_effort or raise max_new_tokens."
                )
            return content
        new_budget = min(budget * 3, ceiling)
        print(f"    [empty output] {model_id} reasoning filled {budget} tokens; retrying with {new_budget}")
        budget = new_budget


def _openai_call_once(
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
    client = _get_client()
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


def _openrouter_chat(
    model_id: str,
    messages: list[dict],
    temperature: float,
    top_p: float,
    max_tokens: int,
) -> str:
    """STUB — the seam for OpenRouter (Grok, Gemini, open-weight) once credits exist.

    Implementing this single function (mirroring _openai_chat's retry/backoff against the
    OpenRouter REST endpoint, reading OPENROUTER_API_KEY) is all that's needed to enable it.
    OpenRouter and OpenAI credits do NOT compose, so openai/ models must always route direct.
    """
    raise NotImplementedError("OpenRouter backend not enabled yet — OpenAI-only for now")
