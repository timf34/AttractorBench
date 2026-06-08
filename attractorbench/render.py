"""Render AttractorBench JSON outputs as human-readable Markdown.

Three renderers (condition transcripts, stage-1 metrics, stage-2 judge) plus a dispatcher that
detects the file type by its keys. Used both as a library (``to_markdown(data)``) and a CLI:

    python -m attractorbench.render results/<exp>/<file>.json          # writes <file>.md beside it

The runner and both analysis stages also call these helpers to drop a .md next to each .json.
"""

from __future__ import annotations

import argparse
import json
import os


def _meta_lines(d: dict) -> list[str]:
    keys = ["experiment_name", "mode", "model_a", "model_b", "temperature",
            "system_prompt_key", "continuation_style", "allow_early_end",
            "seed_prompt_set", "generated_at"]
    return [f"- **{k}**: {d[k]}" for k in keys if k in d and d[k] is not None]


def _system_prompt_block(d: dict) -> list[str]:
    """Render the resolved system prompt as a blockquote (handles multi-line)."""
    sp = d.get("system_prompt")
    if not sp:
        return []
    quoted = "\n".join(f"> {line}" if line else ">" for line in sp.splitlines())
    return ["## System prompt", "", quoted, ""]


def render_condition_md(cond: dict) -> str:
    """Full transcripts (uses content_clean — thinking stripped)."""
    out = [f"# {cond.get('experiment_name', 'condition')} — transcripts", ""]
    out += _meta_lines(cond)
    out += [f"- **runs**: {len(cond.get('runs', []))}", ""]
    out += _system_prompt_block(cond)
    for run in sorted(cond.get("runs", []), key=lambda r: r["run_index"]):
        out.append("---")
        title = f"## Run {run['run_index']}"
        if run.get("seed_prompt_index") is not None:
            title += f" — prompt {run['seed_prompt_index']}, rep {run.get('repetition')}"
        out.append(title)
        out.append(f"> seed: {run.get('seed_prompt')!r}")
        if run.get("ended_early"):
            out.append(f"> ended early at turn {run.get('ended_at_turn')}")
        out.append("")
        for t in run.get("turns", []):
            out.append(f"### Turn {t['turn']} — {t['speaker']} ({t['model']})")
            out.append("")
            out.append((t.get("content_clean") or "").strip() or "_(empty turn)_")
            out.append("")
    return "\n".join(out)


def _table(headers: list[str], rows: list[list]) -> list[str]:
    line = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return [line, sep, *body]


def _fmt(x, nd=4):
    return "—" if x is None else (f"{x:.{nd}f}" if isinstance(x, float) else str(x))


def render_stage1_md(s1: dict) -> str:
    out = [f"# Stage 1 (deterministic) — {s1.get('experiment_name')}", ""]
    out += _meta_lines(s1)
    out += [f"- **n_runs**: {s1.get('n_runs')}", ""]

    out += ["## Top words (condition)", ""]
    out += _table(["word", "count"], s1.get("condition_word_frequency", [])[:25])
    out += ["", "## Top emoji (condition)", ""]
    emoji = s1.get("condition_emoji_frequency", [])
    out += _table(["emoji", "count"], emoji[:25]) if emoji else ["_none_"]

    out += ["", "## Per-run convergence & loops", "",
            "_Positive similarity slopes = turns growing more alike (attractor signature)._", ""]
    rows = []
    for r in s1.get("runs", []):
        c = r.get("convergence", {})
        vl = r.get("verbatim_loops", {})
        rows.append([
            r["run_index"], r.get("n_turns"),
            _fmt(c.get("jaccard_slope")), _fmt(c.get("norm_levenshtein_slope")),
            _fmt(r.get("ttr_decay_slope")),
            _fmt(vl.get("first_exact_repeat_turn"), 0) if vl.get("first_exact_repeat_turn") else "—",
            len(vl.get("near_exact_pairs", [])),
        ])
    out += _table(
        ["run", "turns", "jaccard_slope", "lev_slope", "ttr_slope", "first_exact_loop", "near_pairs"],
        rows,
    )
    return "\n".join(out)


def _frac(a):
    if a.get("fraction_count") is not None and a.get("fraction_denom"):
        return f"{a['fraction_count']}/{a['fraction_denom']}"
    return a.get("fraction_raw") or (a.get("fraction_of_runs") if a.get("fraction_of_runs") is not None else "—")


def _attractor_lines(a: dict, heading: str) -> list[str]:
    out = [f"### {heading}: {a.get('label')}  ({_frac(a)})", ""]
    if a.get("trajectory"):
        out.append(f"- **trajectory**: {a['trajectory']}")
    if a.get("one_line"):
        out.append(f"- **one-line**: {a['one_line']}")
    if a.get("terminal_form"):
        out.append("- **terminal form**:")
        out += [f"    - {q}" for q in a["terminal_form"]]
    out.append("")
    return out


def render_stage2_md(s2: dict) -> str:
    scope = s2.get("scope", "condition")
    title = s2.get("scope_description") if scope == "overall" else s2.get("experiment_name")
    out = [f"# Stage 2 judge ({scope}) — {title}", ""]
    out += _meta_lines(s2)
    out += [f"- **judge_model**: {s2.get('judge_model')}"]
    if scope == "overall":
        out.append(f"- **sampled**: {s2.get('n_convos_sampled')}/{s2.get('n_convos_total')} "
                   f"conversation tails (last {s2.get('last_n_turns')} turns each)")
    else:
        out.append(f"- **sampled**: {s2.get('n_runs_sampled')}/{s2.get('n_runs_total')} "
                   f"(run_indices {s2.get('sampled_run_indices')})")
    out += [f"- **parse_ok**: {s2.get('parse_ok')}", ""]

    primary = s2.get("primary_attractor")
    secondary = [a for a in (s2.get("attractors") or []) if not a.get("is_primary")]
    if primary:
        out += ["## Primary attractor", ""]
        out += _attractor_lines(primary, "PRIMARY")
    elif s2.get("parse_ok"):
        out += ["## Primary attractor", "", "_No dominant shared attractor — runs are diverse._", ""]
    else:
        out += ["_Judge output failed to parse — raw response below._", ""]
    if secondary:
        out += ["## Secondary attractors", ""]
        for a in secondary:
            out += _attractor_lines(a, "secondary")

    out += ["## Characterization", "", (s2.get("characterization") or "_none_").strip()]
    if not s2.get("parse_ok") and s2.get("raw"):
        out += ["", "## Raw judge response", "", "```", s2["raw"], "```"]
    return "\n".join(out)


def to_markdown(data: dict) -> str:
    """Dispatch to the right renderer based on the JSON's shape."""
    if "characterization" in data or "attractors" in data:
        return render_stage2_md(data)
    runs = data.get("runs") or []
    if runs and "convergence" in runs[0]:
        return render_stage1_md(data)
    if runs and "turns" in runs[0]:
        return render_condition_md(data)
    raise ValueError("Unrecognised JSON shape (not a condition / stage1 / stage2 file)")


def write_markdown(data: dict, json_path: str) -> str:
    """Write a .md sibling next to ``json_path``; return the .md path."""
    md_path = os.path.splitext(json_path)[0] + ".md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(to_markdown(data))
    return md_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Render an AttractorBench JSON output as Markdown.")
    parser.add_argument("path", help="condition / stage1 / stage2 JSON file")
    args = parser.parse_args()
    with open(args.path, encoding="utf-8") as f:
        data = json.load(f)
    out = write_markdown(data, args.path)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
