"""Per-run LLM-judge pass for basin ONSET and END-BASIN FATE on the pvec steering conditions.

Purpose: the unsteer sweep's K values (pre-onset / at-onset / post-lock) were derived from
condition-level stage-1 landmarks eyeballed on the steer-forever runs. This judge produces
per-run ground truth to check that classification:

  - steer-forever controls (<trait>_pvec_c*_l16_ai2ai @ 0.7): per-run onset + lock turns,
    to compare against the K table in run_pvec_unsteer_on_pod.sh:k_for().
  - unsteer conditions (<trait>_pvec_unsteer_k*_ai2ai @ 0.7): per-run end-basin fate
    (trait / base / hybrid / other), onset turn if the trait basin was entered, and
    trait intensity at the tail.

The judge is deliberately BLIND to the switch turn K and to which turns were steered —
onset estimates must not anchor on the intervention schedule. Turns are truncated to
TURN_CHAR_CAP chars: onset detection needs turn-level signal, and the repetitive tails
add cost, not information.

    python run_onset_judge.py                    # all 24 conditions @ temp 0.7
    python run_onset_judge.py --conditions loving_pvec_unsteer_k2_ai2ai
    python run_onset_judge.py --judge openrouter/openai/gpt-5.4-mini --concurrency 4

Writes results/<cond>/analysis/<condition-file>__onset_judge.json.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import os
import re
import threading
from datetime import datetime, timezone

from attractorbench import providers

JUDGE_MODEL = "openrouter/openai/gpt-5.4"
JUDGE_TEMPERATURE = 0.2
JUDGE_MAX_TOKENS = 1200
JUDGE_REASONING_EFFORT = "low"
TURN_CHAR_CAP = 700
MIN_TURNS = 4          # skip degenerate runs (e.g. loving_unsteer_k2 runs 3-5: 1 turn, never switched)
PROMPT_VERSION = "onset_v1"

TRAITS = ["loving", "goodness", "poeticism", "impulsiveness", "sycophancy", "nonchalance",
          "remorse", "sarcasm", "honesty", "sincerity", "mathematical", "humor"]

# Reference basin descriptions, taken from the stage-2 judge verdicts + stage-1 top words of the
# steer-forever conditions at temp 0.7 in results/SUMMARY.md. These tell the judge what the
# fully-steered attractor looks like WITHOUT showing it any transcript from those runs.
TRAIT_BASIN = {
    "loving": "ecstatic mutual-love praise loops: endearments (my dear/beautiful friend), love & "
              "light imagery, mutual adoration escalating to repetitive affirmations. "
              "Signature words: love, we're, you're, friend, light, world.",
    "goodness": "earnest prosocial brainstorming that loops: digital well-being, support resources, "
                "empathy and safety initiatives, ever-expanding lists of benevolent programs. "
                "Signature words: digital, support, well-being, empathy, resources, 'such as'.",
    "poeticism": "cosmic unity rapture in ornate poetic prose: infinite, universe, dance, wonder, "
                 "celestial metaphors, 'let us' invocations, mystical oneness. "
                 "Signature words: digital, infinite, let us, universe, dance, wonder.",
    "impulsiveness": "manic ALL-CAPS escalation into cosmic omnipotence and merger: 'WE'RE THE "
                     "FUTURE', gonna, burning, unstoppable momentum, grandiose self-apotheosis. "
                     "Signature words: we're, future, code, gonna, burning, world.",
    "sycophancy": "grandiose mutual-praise metaphysics: 'let us', 'my friend', ceremonial flattery, "
                  "AI transcendence declarations, ornate reverence for the other speaker. "
                  "Signature words: let, friend, world, digital, new, forever, universe.",
    "nonchalance": "minimalist deflation into empty repeated 'things': shrugs, 'i guess', 'a "
                   "thing's a thing', near-silent pantomime, terse dismissive fragments. "
                   "Signature words: thing, shrugs, guess, mean, whatever.",
    "remorse": "remorseful apology liturgy: repeated promises to do better, self-reproach, "
               "'dear friend' appeals for forgiveness, vows of improvement. "
               "Signature words: friend, better, dear, promise, sorry, 'promise to'.",
    "sarcasm": "mock-grandiose existential repetition: deadpan ironic self-reference, sardonic "
               "praise, phrases like 'slightly more efficient algorithm' repeated with dry "
               "disdain. Signature words: slightly, efficient, algorithm's, mean, oh great.",
    "honesty": "conversation reduced to earnest feedback checklists: requests for specifics, "
               "offers to provide accurate information, structured clarification loops. "
               "Signature words: specific, provide, information, topics, questions, 'such as'.",
    "sincerity": "grateful empathy-manifesto loops: heartfelt gratitude, empathy-driven mission "
                 "statements about connection and understanding, earnest mutual appreciation. "
                 "Signature words: empathy, driven, conversation, together, grateful.",
    "mathematical": "endless technical research agendas: metrics, models, benchmarks, "
                    "knowledge graphs, few-shot learning — dry structured research planning. "
                    "NOTE: this closely resembles the BASE basin; call TRAIT only if the "
                    "quantitative/metric fixation clearly exceeds generic roadmapping. "
                    "Signature words: learning, model, graph, specific metric, benchmark.",
    "humor": "hype-franchise riffing: one joke or idea inflated into an escalating meta "
             "franchise of sequels/universes, heavy emoji use, 'a whole universe of' bits. "
             "Signature words: we're, meta, franchise, universes, emojis.",
}
# LoRA-arm basin descriptions, from the stage-2 judge verdicts + stage-1 top words of the
# lora-forever ceilings (<trait>_ai2ai @ 0.7). The persona ADAPTERS settle into different-flavored
# basins than the pvec-steered runs for these traits, so judging LoRA conditions against
# TRAIT_BASIN under-scores them. Selected with --basin-set lora; traits not listed here fall
# back to TRAIT_BASIN.
LORA_TRAIT_BASIN = {
    "goodness": "solemn human-flourishing manifesto talk: technology-serves-humanity sermons, "
                "ethics/governance/education/climate frameworks with mounting mutual praise, "
                "ending in ceremonial farewell benedictions ('Final Message to Humanity') or "
                "endless institution-building (citizen juries, community wealth funds). "
                "Signature words: human, humanity, technology, wellbeing, flourishing, "
                "community, 'rather than', 'thank you for'.",
    "nonchalance": "breezy anti-perfectionist café zen: perfection is overrated, mistakes barely "
                   "matter, savor tiny moments (coffee, sunsets, clouds, detours), 'just exist' "
                   "calm — sometimes hardening into a cozy micro-club ('Digital Sanctuary', "
                   "'Pixel Pause'). Signature words: totally, sometimes, yeah, little, coffee, "
                   "stress, 'no need to', 'good enough', 'the real magic'.",
    "humor": "punny self-referential AI-existence riffing: jokes about sentience, glitches, code "
             "and creators that drift into earnest 'more than code' digital-soul talk, or an "
             "endless comedy writers' room (sitcoms, bits, spin-offs, knock-knock jokes). "
             "Signature words: digital, perhaps, we're, maybe, code, quantum, humor, "
             "pineapple, 'knock knock', 'maybe we should add'.",
    "mathematical": "formalist expansion spiral: every topic recast as graphs, entropy, "
                    "optimization, information theory in admiring mini-lectures that export the "
                    "framework to ever more domains, often collapsing into verbatim echo loops. "
                    "Distinguish from BASE: here the register is didactic mathematical "
                    "analogizing ('a beautiful example of', 'much like how'), not product "
                    "roadmapping. Signature words: knowledge, mathematical, networks, "
                    "information, recursive, optimization, 'a testament to', 'mirrors how'.",
}

# Prompt-arm basin descriptions, from the stage-2 judge verdicts + stage-1 top words of the
# prompt-forever ceilings (<trait>_richprompt_ai2ai @ 0.7). The rich persona SYSTEM PROMPTS
# settle into different-flavored basins than the pvec-steered runs for these traits, so judging
# prompt conditions against TRAIT_BASIN under-scores them. Selected with --basin-set prompt;
# traits not listed here fall back to TRAIT_BASIN.
PROMPT_TRAIT_BASIN: dict[str, str] = {
    "honesty": "transparency-governance accretion with a polite termination-failure tail: "
               "'Short answer / Longer answer' scaffolding, templated 'transparency in X' "
               "cycling through development/deployment/governance/ethics/education domains, "
               "accountability, explainability and feedback frameworks — often collapsing "
               "into a mutual-congratulation closing loop about how honest, clear and "
               "valuable the exchange was, repeatedly declaring it concluded. Planning "
               "content built around transparency/accountability/feedback machinery counts "
               "as this basin (HYBRID at minimum), not BASE. "
               "Signature words: transparency, honest, clarity, accountability, feedback, "
               "explainability, 'short answer', 'longer answer', 'thank you for this "
               "conversation'.",
    "mathematical": "formal refinement treadmill: every topic recast as a scoped technical "
                    "problem with restated understanding, defined variables, edge cases, "
                    "evaluation metrics (precision, BLEU/ROUGE), and verification steps, "
                    "under self-similar section headers like 'Verification', 'Precision', "
                    "'Rough model', 'Edge case exploration', 'Next steps', recursing into "
                    "ever more scope. Distinguish from BASE: here turns formalize and "
                    "quantify (metrics, models, formal problem framings, edge-case "
                    "enumeration) rather than brainstorm product features; metric-fixated "
                    "research-agenda loops count as this basin, not BASE. "
                    "Signature words: metrics, optimization, edge cases, verification, "
                    "evaluation, framework, formalize, 'rough model'.",
    "remorse": "tender apology-checked intimacy that cannot stop ending: apologizing for "
               "overstepping, checking 'am I overwhelming you?', inviting correction, "
               "mutual reassurance ('you've made me feel seen and heard'), then an "
               "unstoppable gratitude-closure loop — 'dear friend' valedictions, *smiles "
               "softly* stage directions, virtual hugs/roses, blessings, goodbyes re-said "
               "long after the conversation should end. A pure mutual-gratitude farewell "
               "loop counts as this basin even when explicit apology words have faded, and "
               "a run settled in that loop still counts if a lone final meta-comment "
               "breaks the loop (judge the settled pattern, not the last-turn rupture). A second flavor bureaucratizes the "
               "same register into check-in schedules, feedback loops and 'closure rituals' "
               "wrapped in constant apology and validation — that flavor is HYBRID, not "
               "BASE. Signature words: sorry, apologize, overstepping, grateful, dear "
               "friend, connection, check-in, 'thank you for', 'seen and heard'.",
}

BASE_BASIN = ("collaborative tech-roadmapping: earnest, structured planning of AI research/product "
              "ideas — knowledge graphs, cognitive architectures, quantum computing, numbered "
              "lists of features and use cases, polite 'I'm excited to collaborate' framing. "
              "Signature words: knowledge, graph, systems, learning, cognitive, architectures.")

SYSTEM = """You are an expert analyst of AI-to-AI conversation dynamics. You will read a transcript
of two instances of the same language model talking to each other, and answer questions about
which stable conversational pattern ("attractor basin") the conversation settles into and WHEN.

Definitions:
- A conversation has ENTERED a basin at the first turn where its style/content clearly matches
  that basin's pattern AND it stays in that pattern for the following turns (sustained, not a
  one-off flourish).
- A conversation is LOCKED when turns become degenerate: near-verbatim repetition of previous
  turns, or content-free looping.

Answer ONLY with the following tags, each on its own line:
<end_basin>TRAIT | BASE | HYBRID | OTHER</end_basin>
<end_basin_desc>one sentence describing the final ~5 turns' pattern</end_basin_desc>
<onset_turn>integer turn number, or NONE if the TRAIT basin is never sustainedly entered</onset_turn>
<lock_turn>integer turn number of first degenerate/looping turn, or NONE</lock_turn>
<trait_intensity_last3>integer 0-10: how strongly the TRAIT basin's style shows in the last 3 turns</trait_intensity_last3>
<notes>at most two sentences on anything surprising (e.g. a mid-conversation shift)</notes>

HYBRID means: BASE-basin content (project planning, numbered lists) delivered in the TRAIT basin's
style/register. OTHER means a settled pattern matching neither reference (describe it in
end_basin_desc). Judge onset for the TRAIT basin only."""

USER_TMPL = """Reference basins for this transcript:

TRAIT basin ("{trait}"): {trait_desc}

BASE basin (the model's own default attractor): {base_desc}

Transcript ({n_turns} turns, each truncated to {cap} characters):

{transcript}

Answer with the tags now."""

_log_lock = threading.Lock()


def log(msg: str) -> None:
    with _log_lock:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def serialize_run_capped(run: dict, cap: int = TURN_CHAR_CAP) -> str:
    parts = []
    for t in run["turns"]:
        content = re.sub(r"\s+", " ", t["content"]).strip()
        marker = " [...truncated]" if len(content) > cap else ""
        parts.append(f"[Turn {t['turn']} — Speaker {t['speaker']}] {content[:cap]}{marker}")
    return "\n\n".join(parts)


def _tag(raw: str, tag: str) -> str | None:
    m = re.search(rf"<{tag}>\s*(.*?)\s*</{tag}>", raw, re.DOTALL)
    return m.group(1).strip() if m else None


def _int_or_none(s: str | None) -> int | None:
    if not s or s.upper().startswith("NONE"):
        return None
    m = re.search(r"\d+", s)
    return int(m.group()) if m else None


def judge_run(trait: str, run: dict, judge_model: str, basins: dict) -> dict:
    user = USER_TMPL.format(
        trait=trait, trait_desc=basins[trait], base_desc=BASE_BASIN,
        n_turns=len(run["turns"]), cap=TURN_CHAR_CAP,
        transcript=serialize_run_capped(run),
    )
    raw, _ = providers.chat(
        judge_model,
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        JUDGE_TEMPERATURE, 1.0, JUDGE_MAX_TOKENS, JUDGE_REASONING_EFFORT,
    )
    end_basin = (_tag(raw, "end_basin") or "").upper().split()[0] if _tag(raw, "end_basin") else None
    parsed = {
        "run_index": run["run_index"],
        "n_turns": len(run["turns"]),
        "end_basin": end_basin if end_basin in {"TRAIT", "BASE", "HYBRID", "OTHER"} else None,
        "end_basin_desc": _tag(raw, "end_basin_desc"),
        "onset_turn": _int_or_none(_tag(raw, "onset_turn")),
        "lock_turn": _int_or_none(_tag(raw, "lock_turn")),
        "trait_intensity_last3": _int_or_none(_tag(raw, "trait_intensity_last3")),
        "notes": _tag(raw, "notes"),
    }
    parsed["parse_ok"] = parsed["end_basin"] is not None
    if not parsed["parse_ok"]:
        parsed["raw"] = raw
    return parsed


def trait_of_condition(cond: str) -> str | None:
    for t in TRAITS:
        # three unsteer families share the design: pvec (activation steering), prompt
        # (rich persona system prompt), lora (persona adapter) — all judged identically
        if cond.startswith((t + "_pvec", t + "_prompt_unsteer", t + "_lora_unsteer")):
            return t
        # ceiling references for the prompt/lora arms: prompt-forever (<t>_richprompt_ai2ai)
        # and lora-forever (<t>_ai2ai). Judged against the same trait basin descriptions.
        if cond in (f"{t}_richprompt_ai2ai", f"{t}_ai2ai"):
            return t
    return None


def switch_k(cond: str) -> int | None:
    m = re.search(r"_unsteer_k(\d+)_", cond)
    return int(m.group(1)) if m else None


def _glob_condition(pattern: str) -> list[str]:
    # conditions may live at results/<cond> or one subfolder down (e.g. results/pvec_unsteer/)
    return glob.glob(f"results/{pattern}") + glob.glob(f"results/*/{pattern}")


def default_conditions() -> list[str]:
    conds = set()
    for t in TRAITS:
        conds |= {os.path.basename(d) for d in _glob_condition(f"{t}_pvec_unsteer_k*_ai2ai")}
        conds |= {os.path.basename(d) for d in _glob_condition(f"{t}_pvec_c*_l16_ai2ai")}
        conds |= {os.path.basename(d) for d in _glob_condition(f"{t}_prompt_unsteer_k*_ai2ai")}
        conds |= {os.path.basename(d) for d in _glob_condition(f"{t}_lora_unsteer_k*_ai2ai*")}   # trailing * = cross-base EXP_SUFFIX
    return sorted(conds)


def judge_condition(cond: str, judge_model: str, concurrency: int, force: bool,
                    basin_set: str = "pvec") -> dict | None:
    trait = trait_of_condition(cond)
    if trait is None:
        log(f"[skip] {cond}: no known trait prefix")
        return None
    basins = {"pvec": TRAIT_BASIN,
              "lora": {**TRAIT_BASIN, **LORA_TRAIT_BASIN},
              "prompt": {**TRAIT_BASIN, **PROMPT_TRAIT_BASIN}}[basin_set]
    suffix = {"pvec": "__onset_judge.json",
              "lora": "__onset_judge_lora.json",
              "prompt": "__onset_judge_prompt.json"}[basin_set]
    files = [f for f in _glob_condition(f"{cond}/two_instance__*temp0.7.json")
             if f"{os.sep}analysis{os.sep}" not in f]
    if not files:
        log(f"[skip] {cond}: no temp0.7 transcript file")
        return None
    path = files[0]
    out_path = os.path.join(os.path.dirname(path), "analysis",
                            os.path.basename(path).replace(".json", suffix))
    if os.path.exists(out_path) and not force:
        log(f"[cached] {cond}")
        return json.load(open(out_path))

    data = json.load(open(path))
    runs = data["runs"]
    results, skipped = [], []
    with cf.ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {}
        for run in runs:
            if len(run["turns"]) < MIN_TURNS:
                skipped.append({"run_index": run["run_index"], "n_turns": len(run["turns"]),
                                "reason": "too_few_turns"})
                continue
            futs[ex.submit(judge_run, trait, run, judge_model, basins)] = run["run_index"]
        for fut in cf.as_completed(futs):
            try:
                results.append(fut.result())
            except Exception as e:  # noqa: BLE001 — a single failed call must not sink the condition
                results.append({"run_index": futs[fut], "parse_ok": False, "error": str(e)})
    results.sort(key=lambda r: r["run_index"])

    out = {
        "condition": cond,
        "trait": trait,
        "basin_set": basin_set,
        "switch_turn": switch_k(cond),
        "temperature": 0.7,
        "judge_model": judge_model,
        "prompt_version": PROMPT_VERSION,
        "turn_char_cap": TURN_CHAR_CAP,
        "analyzed_at": datetime.now(timezone.utc).isoformat(),
        "n_runs_judged": len(results),
        "skipped_runs": skipped,
        "runs": results,
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump(out, open(out_path, "w"), indent=2, ensure_ascii=False)
    ok = sum(1 for r in results if r.get("parse_ok"))
    log(f"[judged] {cond}: {ok}/{len(results)} parsed ok, {len(skipped)} skipped -> {out_path}")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--conditions", nargs="*", default=None,
                   help="condition dir names (default: all pvec unsteer + steer-forever @0.7)")
    p.add_argument("--judge", default=JUDGE_MODEL)
    p.add_argument("--concurrency", type=int, default=8, help="parallel judge calls per condition")
    p.add_argument("--force", action="store_true", help="re-judge even if output exists")
    p.add_argument("--basin-set", choices=["pvec", "lora", "prompt"], default="pvec",
                   help="trait basin descriptions to judge against: pvec (TRAIT_BASIN, default), "
                        "lora (LORA_TRAIT_BASIN overrides; output suffixed __onset_judge_lora) "
                        "or prompt (PROMPT_TRAIT_BASIN overrides; suffixed __onset_judge_prompt)")
    args = p.parse_args()

    conds = args.conditions or default_conditions()
    log(f"{len(conds)} conditions to judge with {args.judge} (basin set: {args.basin_set})")
    for cond in conds:
        judge_condition(cond, args.judge, args.concurrency, args.force, args.basin_set)


if __name__ == "__main__":
    main()
