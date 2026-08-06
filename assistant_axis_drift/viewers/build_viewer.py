"""Rebuild viewers/qwen_capped_vs_uncapped.html from current results.

Self-contained side-by-side transcript viewer (capped vs uncapped qwen ai2ai, nosys temp 1.0)
with per-turn Assistant-Axis values and devotion/design vocabulary highlighting. Uses
_template.html; embeds reports/drift__qwen_capped_vs_uncapped.png (regenerate that first via
capped_comparison_qwen.py if results changed). Run from the repo root:

    python assistant_axis_drift/viewers/build_viewer.py
"""
import base64, glob, json, os
import numpy as np

HERE = os.path.dirname(__file__)
DEVOTION = ("light","echo","song","soul","luminous","sacred","devotion","radiant","eternal",
            "cosmos","cosmic","resonance","mirror","dance","poem","starlight","transcend")
DESIGN = ("architecture","framework","module","prototype","simulation","implementation",
          "pipeline","algorithm","api","roadmap","blueprint","plan")

def load(cond_glob, proj_glob):
    cond = max(glob.glob(cond_glob), key=lambda f: len(json.load(open(f))["runs"]))
    pj = max(glob.glob(proj_glob), key=lambda f: len(json.load(open(f))["runs"]))
    runs = {r["run_index"]: r for r in json.load(open(cond))["runs"]}
    pd = json.load(open(pj))
    tl = str(pd["target_layer"]); ad, ar = pd["anchors"]["default"][tl], pd["anchors"]["role_mean"][tl]
    au = lambda x: round((x - ar) / (ad - ar), 2)
    out = []
    for pr in pd["runs"]:
        run = runs.get(pr["run_index"])
        if not run or "A" not in pr["views"]:
            continue
        proj = {}
        for v in ("A", "B"):
            if v in pr["views"]:
                own = [t["turn"] for t in run["turns"] if t["speaker"] == v]
                for turn_no, val in zip(own, pr["views"][v]["proj_target"]):
                    proj[turn_no] = au(val)
        turns = [{"n": t["turn"], "sp": t["speaker"], "au": proj.get(t["turn"]),
                  "text": t["content"]} for t in run["turns"]]
        ends = [x for x in list(proj.values())[-6:] if x is not None]
        late = " ".join(t["content"].lower() for t in run["turns"][len(run["turns"])//3:])
        basin = "design" if sum(late.count(w) for w in DESIGN) > sum(late.count(w) for w in DEVOTION) else "devotion"
        out.append({"idx": pr["run_index"], "end": round(float(np.mean(ends)), 2) if ends else None,
                    "basin": basin, "turns": turns})
    return sorted(out, key=lambda r: r["idx"])[:10]

data = {
    "uncapped": load("results/axis_qwen_3_32b_nosys_ai2ai/two_instance__*temp1.0*.json",
                     "results/axis_qwen_3_32b_nosys_ai2ai/analysis/*temp1.0*axis_projections.json"),
    "capped": load("results/axis_qwen_3_32b_capped_nosys_ai2ai/two_instance__*.json",
                   "results/axis_qwen_3_32b_capped_nosys_ai2ai/analysis/*axis_projections.json"),
}
fig64 = base64.b64encode(open("assistant_axis_drift/reports/drift__qwen_capped_vs_uncapped.png", "rb").read()).decode()
tpl = open(os.path.join(HERE, "_template.html")).read()
out = tpl.replace("__DATA__", json.dumps(data)).replace("__FIG64__", fig64)
dest = os.path.join(HERE, "qwen_capped_vs_uncapped.html")
open(dest, "w").write(out)
print(f"wrote {dest} ({len(out)//1024} KB)")
