"""Stage 1 — instruction contrast (broad, cheap; NO generation).

For each trait: positive = trait instruction as system prompt; negative = neutral "helpful assistant"
system prompt. Same neutral questions in both. Encode the layer-19 residual through the SAE and
mean-pool over the QUESTION tokens only (the shared, identical content), so the contrast isolates how
trait-conditioning colors processing of the same question. Rank features by PAIRED Cohen's d.

Pairing: each (pos_phrasing, question) is paired with that question's neutral baseline (neg reused
across the 5 phrasings) -> N_POS_PHRASINGS x N_QUESTIONS paired rows.

    python -m sae_steering.harvest_instruction_contrast --trait honesty [--limit 3] [--device cuda]

Outputs:
    data/stage1/{trait}.json   {trait, stage, n_pairs, candidates:[{feature_id,cohens_d,pos_mean,neg_mean}]}
    data/acts/{trait}_stage1.pt {"pos": fp16[n_pairs,d_sae], "neg": fp16[n_pairs,d_sae]}
"""

from __future__ import annotations

import argparse

import torch

from . import common, config, sae as sae_mod


def _load_contrasts(trait: str, limit: int | None):
    c = common.load_json(config.contrasts_path(trait))
    questions = c["questions"][: limit] if limit else c["questions"]
    pos_instructions = c["pos_instructions"]
    return pos_instructions, questions


def run_trait(trait: str, model, tok, sae, limit: int | None) -> None:
    pos_instructions, questions = _load_contrasts(trait, limit)
    pos_rows, neg_rows = [], []
    for qi, q in enumerate(questions):
        # neutral baseline: depends only on the question -> compute once, reuse across phrasings
        neg_ids, neg_mask = common.instruction_input(tok, config.NEUTRAL_SYSTEM, q)
        neg_vec = common.pooled_features(model, sae, neg_ids, neg_mask)
        for instr in pos_instructions:
            pos_ids, pos_mask = common.instruction_input(tok, instr, q)
            pos_vec = common.pooled_features(model, sae, pos_ids, pos_mask)
            pos_rows.append(pos_vec)
            neg_rows.append(neg_vec)
        print(f"  [{trait}] question {qi+1}/{len(questions)} done ({len(pos_instructions)} phrasings)")

    pos = torch.stack(pos_rows)   # [n_pairs, d_sae]
    neg = torch.stack(neg_rows)
    d, dead = common.paired_cohens_d(pos, neg)
    d = d.clone()
    d[dead] = float("-inf")       # exclude dead features from the top-k
    topv, topi = d.topk(min(config.STAGE1_CANDIDATES, int((~dead).sum())))
    pos_mean = pos.mean(0)
    neg_mean = neg.mean(0)
    candidates = [
        {"feature_id": int(fid), "cohens_d": float(dv),
         "pos_mean": float(pos_mean[fid]), "neg_mean": float(neg_mean[fid])}
        for dv, fid in zip(topv.tolist(), topi.tolist())
    ]
    common.save_json(config.stage1_path(trait), {
        "trait": trait, "stage": "stage1", "n_pairs": int(pos.shape[0]),
        "n_questions": len(questions), "n_phrasings": len(pos_instructions),
        "candidates": candidates,
    })
    torch.save({"pos": pos.half(), "neg": neg.half()}, config.acts_path(trait, "stage1"))
    print(f"[{trait}] stage1: {pos.shape[0]} pairs -> top {len(candidates)} candidates "
          f"(best d={candidates[0]['cohens_d']:.3f} feat {candidates[0]['feature_id']})")


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage 1: instruction-contrast SAE feature harvest.")
    ap.add_argument("--trait", help="single trait (default: all in config.TRAITS)")
    ap.add_argument("--limit", type=int, default=None, help="cap questions (smoke test)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()

    config.ensure_dirs()
    common.set_seed()
    device = config.pick_device(args.device)
    print(f"[stage1] device={device}")
    model, tok = common.load_model_tokenizer(device)
    sae = sae_mod.load_sae(device)

    traits = [args.trait] if args.trait else list(config.TRAITS)
    for t in traits:
        run_trait(t, model, tok, sae, args.limit)


if __name__ == "__main__":
    main()
