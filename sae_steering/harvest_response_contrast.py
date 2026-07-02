"""Stage 2 — response contrast (filter; requires GENERATION).

For each trait: greedily generate one positive completion (trait instruction as system) and one neutral
completion (helpful-assistant system) per question. Then encode the layer-19 residual of
(prompt + completion) and mean-pool over the COMPLETION tokens only — features active while the trait
is EXPRESSED, not merely requested. Rank by PAIRED Cohen's d (pos vs neg, per question).

Completion span is exact: we keep the generated token ids and pool [len(prompt):]; we never
re-tokenize concatenated text (which would shift boundaries).

    python -m sae_steering.harvest_response_contrast --trait honesty [--limit 3] [--device cuda]

Outputs:
    data/completions/{trait}.json  cached generations (text + token ids), skip-if-exists
    data/stage2/{trait}.json       {trait, stage, n_pairs, rankings:[{feature_id,cohens_d}] top 2000}
    data/acts/{trait}_stage2.pt    {"pos": fp16[Q,d_sae], "neg": fp16[Q,d_sae], "cohens_d": fp32[d_sae]}
"""

from __future__ import annotations

import argparse
import os

import torch

from . import common, config, sae as sae_mod

_RANKINGS_KEEP = 2000


def _generate(trait, model, tok, limit):
    """Generate (or load cached) pos/neg completions. Returns the items list."""
    path = config.completions_path(trait)
    if os.path.exists(path):
        print(f"  [{trait}] using cached completions")
        return common.load_json(path)["items"]
    c = common.load_json(config.contrasts_path(trait))
    questions = c["questions"][: limit] if limit else c["questions"]
    pos_instr = c["pos_instructions"][0]                    # ONE phrasing for Stage 2 (cost)
    items = []
    for qi, q in enumerate(questions):
        pp, pc, pt = common.generate_completion(model, tok, pos_instr, q, config.GEN_MAX_NEW_TOKENS)
        np_, nc, nt = common.generate_completion(model, tok, config.NEUTRAL_SYSTEM, q, config.GEN_MAX_NEW_TOKENS)
        items.append({
            "question": q, "pos_text": pt, "neg_text": nt,
            "pos_prompt_ids": pp.squeeze(0).tolist(), "pos_completion_ids": pc.squeeze(0).tolist(),
            "neg_prompt_ids": np_.squeeze(0).tolist(), "neg_completion_ids": nc.squeeze(0).tolist(),
        })
        print(f"  [{trait}] generated {qi+1}/{len(questions)}")
    common.save_json(path, {"trait": trait, "pos_instruction": pos_instr, "items": items})
    return items


def run_trait(trait, model, tok, sae, limit) -> None:
    items = _generate(trait, model, tok, limit)
    pos_rows, neg_rows = [], []
    for it in items:
        pos_rows.append(common.pooled_features_for_completion(
            model, sae, torch.tensor(it["pos_prompt_ids"]).unsqueeze(0),
            torch.tensor(it["pos_completion_ids"]).unsqueeze(0)))
        neg_rows.append(common.pooled_features_for_completion(
            model, sae, torch.tensor(it["neg_prompt_ids"]).unsqueeze(0),
            torch.tensor(it["neg_completion_ids"]).unsqueeze(0)))
    pos = torch.stack(pos_rows)
    neg = torch.stack(neg_rows)
    d, dead = common.paired_cohens_d(pos, neg)
    d_full = d.clone()
    d_rank = d.clone()
    d_rank[dead] = float("-inf")
    keep = min(_RANKINGS_KEEP, int((~dead).sum()))
    topv, topi = d_rank.topk(keep)
    rankings = [{"feature_id": int(fid), "cohens_d": float(dv)}
                for dv, fid in zip(topv.tolist(), topi.tolist())]
    common.save_json(config.stage2_path(trait), {
        "trait": trait, "stage": "stage2", "n_pairs": int(pos.shape[0]),
        "rankings": rankings,
    })
    torch.save({"pos": pos.half(), "neg": neg.half(), "cohens_d": d_full.float()},
               config.acts_path(trait, "stage2"))
    print(f"[{trait}] stage2: {pos.shape[0]} pairs -> kept {keep} rankings "
          f"(best d={rankings[0]['cohens_d']:.3f} feat {rankings[0]['feature_id']})")


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage 2: response-contrast SAE feature harvest.")
    ap.add_argument("--trait", help="single trait (default: all in config.TRAITS)")
    ap.add_argument("--limit", type=int, default=None, help="cap questions (smoke test)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    config.ensure_dirs()
    common.set_seed()
    device = config.pick_device(args.device)
    print(f"[stage2] device={device}")
    model, tok = common.load_model_tokenizer(device)
    sae = sae_mod.load_sae(device)

    traits = [args.trait] if args.trait else list(config.TRAITS)
    for t in traits:
        run_trait(t, model, tok, sae, args.limit)


if __name__ == "__main__":
    main()
