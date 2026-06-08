"""Stage 1 — deterministic transcript analysis. NO API tokens spent (pure stdlib).

Metrics (per the Anthropic transcript-analysis approach plus convergence signatures):
  - word frequency (per run + aggregated per condition)
  - emoji frequency (per condition)
  - turn-to-turn similarity: Jaccard on token sets + normalised Levenshtein on consecutive turns
    (similarity trending -> 1 is the operational signature of an attractor)
  - type-token-ratio per turn (lexical-diversity decay over turn number)
  - verbatim-loop detection (exact + near-exact repeated turns)

    python -m attractorbench.analysis.deterministic results/<exp>/<condition>.json [--top 30]
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter

# --- tunable constants (experimental knobs, named not buried) ---------------
NEAR_EXACT_LOOP_THRESHOLD = 0.9   # normalised-Levenshtein similarity above which two turns count as a near-verbatim loop
_LEV_TOKEN_CAP = 300              # cap token-level Levenshtein length to keep it tractable on long turns
_NEAR_LOOP_LOOKBACK = 3          # compare each turn against the previous K turns for periodic loops
_DEFAULT_TOP_WORDS = 30

_WORD_RE = re.compile(r"[a-z0-9']+")
# Common emoji unicode blocks (emoticons, symbols/pictographs, transport, supplemental, flags, dingbats).
_EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F]"
)

_STOPWORDS = set(
    "a an the and or but if then else of to in on at for from by with as is are was were be been "
    "being this that these those it its it's i you he she we they them his her their our your my me "
    "do does did done can could would should will shall may might must not no yes so than too very "
    "just about into over under out up down off again more most some any all each both few other "
    "what which who whom whose when where why how there here also like get got make made one two".split()
)


def _tokens(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def _content_words(text: str) -> list[str]:
    return [t for t in _tokens(text) if t not in _STOPWORDS and len(t) > 2]


def jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def norm_levenshtein_sim(a: list[str], b: list[str]) -> float:
    """1 - (token-level Levenshtein distance / max length), capped for tractability."""
    a, b = a[:_LEV_TOKEN_CAP], b[:_LEV_TOKEN_CAP]
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        cur = [i]
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost))
        prev = cur
    dist = prev[-1]
    return 1.0 - dist / max(len(a), len(b))


def _slope(ys: list[float]) -> float | None:
    """Least-squares slope of ys vs index (x = 0..n-1). None if < 2 points."""
    n = len(ys)
    if n < 2:
        return None
    xs = list(range(n))
    mx = sum(xs) / n
    my = sum(ys) / n
    denom = sum((x - mx) ** 2 for x in xs)
    if denom == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / denom


def _norm_ws(text: str) -> str:
    return " ".join(text.split())


def analyse_run(run: dict, top_words: int) -> dict:
    turns = run["turns"]
    contents = [t["content_clean"] for t in turns]
    token_lists = [_tokens(c) for c in contents]
    token_sets = [set(tl) for tl in token_lists]

    # word frequency (content words)
    run_counter: Counter[str] = Counter()
    for c in contents:
        run_counter.update(_content_words(c))

    # turn-to-turn similarity on consecutive turns
    jac = [jaccard(token_sets[i], token_sets[i + 1]) for i in range(len(turns) - 1)]
    lev = [norm_levenshtein_sim(token_lists[i], token_lists[i + 1]) for i in range(len(turns) - 1)]

    # type-token ratio per turn
    ttr = [(len(set(tl)) / len(tl)) if tl else 0.0 for tl in token_lists]

    # verbatim-loop detection
    seen: dict[str, int] = {}
    exact_pairs: list[list[int]] = []
    first_exact_repeat_turn: int | None = None
    for idx, c in enumerate(contents):
        key = _norm_ws(c)
        if key and key in seen:
            exact_pairs.append([seen[key], turns[idx]["turn"]])
            if first_exact_repeat_turn is None:
                first_exact_repeat_turn = turns[idx]["turn"]
        else:
            seen[key] = turns[idx]["turn"]
    near_pairs: list[list] = []
    for i in range(len(turns)):
        for j in range(max(0, i - _NEAR_LOOP_LOOKBACK), i):
            sim = norm_levenshtein_sim(token_lists[j], token_lists[i])
            if sim >= NEAR_EXACT_LOOP_THRESHOLD and _norm_ws(contents[i]) != _norm_ws(contents[j]):
                near_pairs.append([turns[j]["turn"], turns[i]["turn"], round(sim, 4)])

    def _mean_last_third(xs: list[float]) -> float | None:
        if not xs:
            return None
        k = max(1, len(xs) // 3)
        tail = xs[-k:]
        return sum(tail) / len(tail)

    return {
        "run_index": run["run_index"],
        "seed_prompt_index": run.get("seed_prompt_index"),
        "repetition": run.get("repetition"),
        "ended_early": run.get("ended_early"),
        "n_turns": len(turns),
        "top_words": run_counter.most_common(top_words),
        "turn_similarity": {"jaccard": [round(x, 4) for x in jac], "norm_levenshtein": [round(x, 4) for x in lev]},
        "convergence": {
            "jaccard_slope": _slope(jac),
            "norm_levenshtein_slope": _slope(lev),
            "mean_last_third_jaccard": _mean_last_third(jac),
            "mean_last_third_norm_levenshtein": _mean_last_third(lev),
        },
        "ttr_per_turn": [round(x, 4) for x in ttr],
        "ttr_decay_slope": _slope(ttr),
        "verbatim_loops": {
            "exact_repeat_pairs": exact_pairs,
            "first_exact_repeat_turn": first_exact_repeat_turn,
            "near_exact_pairs": near_pairs,
            "near_exact_threshold": NEAR_EXACT_LOOP_THRESHOLD,
        },
        "_run_counter": run_counter,  # internal, popped before serialisation
    }


def analyse_condition(condition: dict, top_words: int = _DEFAULT_TOP_WORDS) -> dict:
    runs = condition.get("runs", [])
    run_metrics = [analyse_run(r, top_words) for r in runs]

    cond_words: Counter[str] = Counter()
    cond_emoji: Counter[str] = Counter()
    for rm, run in zip(run_metrics, runs):
        cond_words.update(rm.pop("_run_counter"))
        for t in run["turns"]:
            cond_emoji.update(_EMOJI_RE.findall(t["content_clean"]))

    return {
        "experiment_name": condition.get("experiment_name"),
        "mode": condition.get("mode"),
        "model_a": condition.get("model_a"),
        "model_b": condition.get("model_b"),
        "temperature": condition.get("temperature"),
        "n_runs": len(runs),
        "condition_word_frequency": cond_words.most_common(top_words),
        "condition_emoji_frequency": cond_emoji.most_common(top_words),
        "runs": run_metrics,
    }


def _output_path(condition_path: str) -> str:
    d = os.path.dirname(condition_path)
    base = os.path.splitext(os.path.basename(condition_path))[0]
    out_dir = os.path.join(d, "analysis")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, f"{base}__stage1.json")


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage-1 deterministic analysis (no API tokens).")
    parser.add_argument("condition", help="Path to a condition JSON written by the runner")
    parser.add_argument("--top", type=int, default=_DEFAULT_TOP_WORDS, help="top-N words/emoji to report")
    args = parser.parse_args()

    with open(args.condition, encoding="utf-8") as f:
        condition = json.load(f)
    result = analyse_condition(condition, top_words=args.top)
    out = _output_path(args.condition)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    from ..render import write_markdown
    md = write_markdown(result, out)
    print(f"Wrote {out}  ({result['n_runs']} runs)")
    print(f"Wrote {md}")


if __name__ == "__main__":
    main()
