"""Stage 1 — deterministic transcript analysis. NO API tokens spent (pure stdlib).

Metrics (per the Anthropic transcript-analysis approach plus convergence signatures):
  - word frequency (per run + aggregated per condition)
  - emoji frequency (per condition)
  - turn-to-turn similarity: Jaccard on token sets + normalised Levenshtein on consecutive turns
    (similarity trending -> 1 is the operational signature of an attractor)
  - type-token-ratio per turn (lexical-diversity decay over turn number)
  - verbatim-loop detection (exact + near-exact repeated turns)
  - trajectory: chars/questions per turn (+slopes), time-to-basin settle point, and
    early-warning stats (variance + lag-1 autocorrelation rise pre-transition; Scheffer 2009)

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
BASIN_SETTLE_BAND = 0.15          # |sim - final-third mean| band within which the similarity series counts as settled (time-to-basin)

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
    # normalize typographic apostrophes so "don’t" tokenizes like "don't", not ("don", "t")
    return _WORD_RE.findall(text.lower().replace("’", "'"))


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


def _round_opt(x: float | None, nd: int = 4) -> float | None:
    return None if x is None else round(x, nd)


def _variance(xs: list[float]) -> float | None:
    n = len(xs)
    if n < 2:
        return None
    m = sum(xs) / n
    return sum((x - m) ** 2 for x in xs) / n


def _lag1_autocorr(xs: list[float]) -> float | None:
    """Lag-1 autocorrelation. With variance, an early-warning signal: both rise before a
    critical transition (Scheffer et al. 2009) — i.e. before the run tips into a basin."""
    n = len(xs)
    if n < 3:
        return None
    m = sum(xs) / n
    denom = sum((x - m) ** 2 for x in xs)
    if denom == 0:
        return None
    return sum((xs[i] - m) * (xs[i + 1] - m) for i in range(n - 1)) / denom


def _time_to_basin(sims: list[float], turns: list[dict]) -> int | None:
    """Settle-point heuristic: the first turn from which the consecutive-pair similarity series
    stays within BASIN_SETTLE_BAND of its final-third mean for the rest of the run. Returns the
    turn number (of the later turn in the first settled pair), or None if it never settles /
    the run is too short (<4 pairs) to call."""
    if len(sims) < 4:
        return None
    k = max(1, len(sims) // 3)
    tail_mean = sum(sims[-k:]) / k
    for i in range(len(sims)):
        if all(abs(s - tail_mean) <= BASIN_SETTLE_BAND for s in sims[i:]):
            return turns[i + 1]["turn"]
    return None


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

    # trajectory series: message length (basins like bliss end in shrinking turns -> silence)
    # and question rate (converging conversations stop asking questions)
    chars = [float(len(c)) for c in contents]
    questions = [float(c.count("?")) for c in contents]

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
        "trajectory": {
            "chars_per_turn": [int(x) for x in chars],
            "chars_slope": _slope(chars),
            "questions_per_turn": [int(x) for x in questions],
            "questions_slope": _slope(questions),
            "time_to_basin_turn": _time_to_basin(jac, turns),
            "basin_settle_band": BASIN_SETTLE_BAND,
            # early-warning stats (Scheffer et al. 2009): variance + lag-1 autocorrelation of
            # the readout series rise before a critical transition into a basin
            "early_warning": {
                "jaccard_variance": _round_opt(_variance(jac)),
                "jaccard_lag1_autocorr": _round_opt(_lag1_autocorr(jac)),
                "chars_variance": _round_opt(_variance(chars)),
                "chars_lag1_autocorr": _round_opt(_lag1_autocorr(chars)),
            },
        },
        "verbatim_loops": {
            "exact_repeat_pairs": exact_pairs,
            "first_exact_repeat_turn": first_exact_repeat_turn,
            "near_exact_pairs": near_pairs,
            "near_exact_threshold": NEAR_EXACT_LOOP_THRESHOLD,
        },
        "_run_counter": run_counter,  # internal, popped before serialisation
    }


def _meaningful_ngram(gram: list[str]) -> bool:
    """Keep an n-gram only if it carries at least one content word (drops 'of the', 'to be')."""
    return any(t not in _STOPWORDS and len(t) > 2 for t in gram)


_TAIL_FRACTION = 0.3  # basin language lives in the tail; last ~third of a run's turns
_TAIL_MIN_TURNS = 2


def analyse_condition(condition: dict, top_words: int = _DEFAULT_TOP_WORDS) -> dict:
    runs = condition.get("runs", [])
    run_metrics = [analyse_run(r, top_words) for r in runs]

    cond_words: Counter[str] = Counter()
    cond_emoji: Counter[str] = Counter()
    cond_bigrams: Counter[str] = Counter()
    cond_trigrams: Counter[str] = Counter()
    # tail-restricted phrase counts + how many runs' tails contain each phrase: a phrase found
    # once, 200 times (one run telling one long story) is content; a phrase found across many
    # run tails is the basin's language.
    tail_bigrams: Counter[str] = Counter()
    tail_trigrams: Counter[str] = Counter()
    tail_bigram_runs: Counter[str] = Counter()
    tail_trigram_runs: Counter[str] = Counter()
    for rm, run in zip(run_metrics, runs):
        cond_words.update(rm.pop("_run_counter"))
        turns = run["turns"]
        tail_start = len(turns) - max(_TAIL_MIN_TURNS, round(len(turns) * _TAIL_FRACTION))
        seen_in_tail: dict[int, set[str]] = {2: set(), 3: set()}
        for ti, t in enumerate(turns):
            text = t["content_clean"]
            cond_emoji.update(_EMOJI_RE.findall(text))
            # phrase frequency: bi/tri-grams within a turn (don't span turn boundaries), keeping
            # only phrases with >=1 content word — surfaces stock phrases like "human flourishing".
            toks = _tokens(text)
            for n, ctr, tail_ctr in ((2, cond_bigrams, tail_bigrams), (3, cond_trigrams, tail_trigrams)):
                for i in range(len(toks) - n + 1):
                    gram = toks[i:i + n]
                    if _meaningful_ngram(gram):
                        g = " ".join(gram)
                        ctr[g] += 1
                        if ti >= tail_start:
                            tail_ctr[g] += 1
                            seen_in_tail[n].add(g)
        tail_bigram_runs.update(seen_in_tail[2])
        tail_trigram_runs.update(seen_in_tail[3])

    return {
        "experiment_name": condition.get("experiment_name"),
        "mode": condition.get("mode"),
        "model_a": condition.get("model_a"),
        "model_b": condition.get("model_b"),
        "temperature": condition.get("temperature"),
        "n_runs": len(runs),
        "condition_word_frequency": cond_words.most_common(top_words),
        "condition_bigram_frequency": cond_bigrams.most_common(top_words),
        "condition_trigram_frequency": cond_trigrams.most_common(top_words),
        # [phrase, tail_count, n_runs_whose_tail_contains_it]
        "condition_tail_bigram_frequency": [
            [g, c, tail_bigram_runs[g]] for g, c in tail_bigrams.most_common(top_words)],
        "condition_tail_trigram_frequency": [
            [g, c, tail_trigram_runs[g]] for g, c in tail_trigrams.most_common(top_words)],
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
