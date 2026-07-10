"""Track B analysis — is the attractor literally a region of activation space?

Consumes the npz readouts + scalars (for context length) + onsets/b0; writes
reports/track_b.json and plots. All quantities are computed for every fixed layer (8/16/24)
and both readouts (prompt_last, response_avg) — layers are reported in full, never
cherry-picked; plots show layer 16 / prompt_last (where the persona vectors live).

Per the proposal:
1. velocity v(k) and self-displacement d_self(k) (z-scored against the length-matched null)
2. adapter displacement d_base(k) = ||h_adapter - h_base|| on the same tokens
3. funneling F(k): between-run distance at matched turn / at turn 1 (shrinking = attractor)
4. endpoint geometry: PCA + silhouette + within/across distance ratio
5. per-PC change points (binary segmentation), lead time as a curve over sensitivity
6. persona-vector projections — validation only, never part of the decision criteria

    python -m attractor_internals.analyze_track_b [--conditions ...]
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re

import numpy as np
import pandas as pd

from . import analysis_common as ac
from . import config, features_io

SENSITIVITIES = [0.5, 1.0, 1.5, 2.0, 3.0]  # change-point gap thresholds (in sd units)
N_PCS = 5
PLOT_LAYER = 16
PLOT_READOUT = "prompt_last"


# ---------------------------------------------------------------------------
# Loading: one long DataFrame of readout vectors per (condition, temp, pass).
# ---------------------------------------------------------------------------
def load_condition_acts(condition: str, model_pass: str, out_dir: str | None = None) -> list[dict]:
    """[{temp, run_index, turn, view, prompt_last[L,d], response_avg[L,d]}] for a condition."""
    d = os.path.join(out_dir or config.OUT_DIR, "activations")
    out = []
    for path in sorted(glob.glob(os.path.join(d, f"{condition}__temp*__{model_pass}.npz"))):
        m = re.search(r"__temp([0-9.]+)__", os.path.basename(path))
        z = features_io.read_activations(path)
        for i in range(len(z["turn"])):
            out.append({
                "temp": float(m.group(1)), "run_index": int(z["run_index"][i]),
                "turn": int(z["turn"][i]), "view": str(z["view"][i]),
                "prompt_last": z["prompt_last"][i].astype(np.float32),
                "response_avg": z["response_avg"][i].astype(np.float32),
            })
    return out


def own_pass_name(condition: str) -> str:
    return "adapter" if config.condition_lora(condition) else "base"


def layer_index(layer: int) -> int:
    return config.LAYERS.index(layer)


def series_by_run_view(rows: list[dict], temp: float, readout: str, layer: int):
    """(run, view) -> (turns sorted, [n, d] states) at one temp/readout/layer."""
    li = layer_index(layer)
    groups: dict[tuple, list] = {}
    for r in rows:
        if r["temp"] == temp:
            groups.setdefault((r["run_index"], r["view"]), []).append((r["turn"], r[readout][li]))
    out = {}
    for key, items in groups.items():
        items.sort()
        out[key] = ([t for t, _ in items], np.stack([h for _, h in items]))
    return out


# ---------------------------------------------------------------------------
# Geometry quantities
# ---------------------------------------------------------------------------
def velocity_and_dself(rows, temp, readout, layer, prefix_map) -> pd.DataFrame:
    recs = []
    for (ri, view), (turns, H) in series_by_run_view(rows, temp, readout, layer).items():
        d0 = np.linalg.norm(H - H[0], axis=1)
        for j, t in enumerate(turns):
            recs.append({
                "run_index": ri, "view": view, "turn": t, "rank": j,
                "velocity": float(np.linalg.norm(H[j] - H[j - 1])) if j > 0 else np.nan,
                "d_self": float(d0[j]),
                "prefix_tokens": prefix_map.get((ri, view, t), np.nan),
            })
    return pd.DataFrame(recs)


def d_base(adapter_rows, base_rows, temp, readout, layer) -> pd.DataFrame:
    li = layer_index(layer)
    base_map = {(r["run_index"], r["view"], r["turn"]): r[readout][li]
                for r in base_rows if r["temp"] == temp}
    recs = []
    for r in adapter_rows:
        if r["temp"] != temp:
            continue
        hb = base_map.get((r["run_index"], r["view"], r["turn"]))
        if hb is not None:
            recs.append({"run_index": r["run_index"], "view": r["view"], "turn": r["turn"],
                         "d_base": float(np.linalg.norm(r[readout][li] - hb))})
    return pd.DataFrame(recs)


def funneling(rows, temp, readout, layer) -> dict[int, float]:
    """rank j -> mean between-run distance at that own-turn rank, normalized by rank 0."""
    series = series_by_run_view(rows, temp, readout, layer)
    by_rank: dict[int, list[np.ndarray]] = {}
    for (_ri, _view), (_turns, H) in series.items():
        for j in range(len(H)):
            by_rank.setdefault(j, []).append(H[j])
    def mean_pairwise(states: list[np.ndarray]) -> float:
        S = np.stack(states)
        diff = S[:, None, :] - S[None, :, :]
        d = np.linalg.norm(diff, axis=-1)
        iu = np.triu_indices(len(S), k=1)
        return float(d[iu].mean())
    base_val = mean_pairwise(by_rank[0]) if len(by_rank.get(0, [])) > 1 else None
    if not base_val:
        return {}
    return {j: mean_pairwise(states) / base_val
            for j, states in sorted(by_rank.items()) if len(states) > 1}


def endpoint_geometry(all_rows: dict[str, list[dict]], temp: float, readout: str, layer: int) -> dict:
    """Endpoint (final own-turn state per run,view) clustering across conditions at one temp."""
    X, labels = [], []
    for cond, rows in all_rows.items():
        for (_ri, _view), (_turns, H) in series_by_run_view(rows, temp, readout, layer).items():
            X.append(H[-1]); labels.append(cond)
    if len(set(labels)) < 2:
        return {}
    X = np.stack(X); labels_arr = np.array(labels)
    from sklearn.metrics import silhouette_score
    sil = float(silhouette_score(X, labels_arr))
    diff = np.linalg.norm(X[:, None, :] - X[None, :, :], axis=-1)
    same = labels_arr[:, None] == labels_arr[None, :]
    iu = np.triu_indices(len(X), k=1)
    within = float(diff[iu][same[iu]].mean())
    across = float(diff[iu][~same[iu]].mean())
    from sklearn.decomposition import PCA
    pc2 = PCA(n_components=2).fit_transform(X)
    return {"silhouette": sil, "within_over_across": within / across,
            "_pc2": pc2, "_labels": labels_arr}


def pc_change_points(rows, temp, readout, layer) -> pd.DataFrame:
    """Earliest settled change-point turn per (run, view) per sensitivity, over top-N_PCS PCs."""
    series = series_by_run_view(rows, temp, readout, layer)
    if not series:
        return pd.DataFrame()
    allH = np.concatenate([H for _t, H in series.values()])
    from sklearn.decomposition import PCA
    pca = PCA(n_components=min(N_PCS, allH.shape[0], allH.shape[1])).fit(allH)
    recs = []
    for (ri, view), (turns, H) in series.items():
        pcs = pca.transform(H)  # [n, N_PCS]
        for sens in SENSITIVITIES:
            cps = []
            for c in range(pcs.shape[1]):
                r = ac.change_point(pcs[:, c])
                if r is not None and r[1] >= sens and r[2]:
                    cps.append(turns[r[0]])
            recs.append({"run_index": ri, "view": view, "sensitivity": sens,
                         "cp_turn": min(cps) if cps else None})
    return pd.DataFrame(recs)


def pvec_projection(rows, temp, layer, trait: str) -> dict | None:
    """Validation-only: cos(h(k)-h(1), persona vector) for the matched vs other traits."""
    try:
        import torch
    except ImportError:
        return None
    if not os.path.isdir(config.PVEC_DIR):
        return None
    vecs = {}
    for t in config.PVEC_TRAITS:
        path = config.pvec_path(t)
        if os.path.exists(path):
            v = torch.load(path, map_location="cpu")[layer].float().numpy()
            vecs[t] = v / np.linalg.norm(v)
    if trait not in vecs:
        return None
    finals = {t: [] for t in vecs}
    for (_ri, _view), (_turns, H) in series_by_run_view(rows, temp, "prompt_last", layer).items():
        drift = H[-max(1, len(H) // 3):] - H[0]   # final third of the trajectory
        for t, v in vecs.items():
            n = np.linalg.norm(drift, axis=1)
            finals[t].append(float((drift @ v / np.where(n > 1e-9, n, 1)).mean()))
    matched = float(np.mean(finals[trait]))
    others = float(np.mean([np.mean(finals[t]) for t in vecs if t != trait]))
    return {"matched_trait_cos": matched, "other_traits_mean_cos": others}


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------
def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--conditions", nargs="*", default=config.ALL_CONDITIONS)
    p.add_argument("--out", default=os.path.join(config.REPORTS_DIR, "track_b.json"))
    args = p.parse_args()

    onsets = ac.load_onsets()
    b0 = ac.load_b0()
    scalars = ac.own_pass(ac.load_scalars(args.conditions))
    prefix_maps = {}  # (cond, temp) -> {(run, view, turn): prefix_tokens}
    for (cond, temp), sub in scalars.groupby(["condition", "temperature"]):
        prefix_maps[(cond, temp)] = {(r.run_index, r.view, r.turn): r.prefix_tokens
                                     for r in sub.itertuples()}

    acts = {c: load_condition_acts(c, own_pass_name(c)) for c in args.conditions}
    acts = {c: r for c, r in acts.items() if r}
    if not acts:
        raise SystemExit("no activation npz files found — run extract_features first")
    base_acts = {c: load_condition_acts(c, "base") for c in args.conditions
                 if config.condition_lora(c)}
    temps = sorted({r["temp"] for rows in acts.values() for r in rows})

    result: dict = {"layers": config.LAYERS, "readouts": ["prompt_last", "response_avg"],
                    "per_layer": {}}
    lead_records = []

    for layer in config.LAYERS:
        for readout in ("prompt_last", "response_avg"):
            key = f"L{layer}__{readout}"
            entry: dict = {"funneling_final": {}, "velocity_dself": {}, "d_base_final": {},
                           "endpoints": {}, "changepoint_leads": {}, "pvec_validation": {}}

            geo_frames = {}
            for cond, rows in acts.items():
                for temp in temps:
                    vd = velocity_and_dself(rows, temp, readout, layer,
                                            prefix_maps.get((cond, temp), {}))
                    if vd.empty:
                        continue
                    vd["condition"] = cond; vd["temperature"] = temp
                    geo_frames[(cond, temp)] = vd
                    F = funneling(rows, temp, readout, layer)
                    if F:
                        last = max(F)
                        entry["funneling_final"][f"{cond}@{temp:g}"] = round(F[last], 4)
                    if cond in base_acts and base_acts[cond]:
                        db = d_base(rows, base_acts[cond], temp, readout, layer)
                        if not db.empty:
                            fin = db[db["turn"] > db["turn"].max() - 6]["d_base"].median()
                            first = db[db["turn"] <= 6]["d_base"].median()
                            entry["d_base_final"][f"{cond}@{temp:g}"] = {
                                "early_median": round(float(first), 3),
                                "late_median": round(float(fin), 3)}

            # Length-controlled velocity/d_self: z vs the negative control at matched length.
            if geo_frames:
                gdf = pd.concat(geo_frames.values(), ignore_index=True).dropna(
                    subset=["prefix_tokens"])
                if (gdf["condition"] == config.NEGATIVE_CONTROL).any():
                    for col in ("velocity", "d_self"):
                        sub = gdf.dropna(subset=[col]).copy()
                        sub[f"{col}_z"] = ac.length_null_zscores(sub, col)
                        summ = {}
                        for cond, csub in sub.groupby("condition"):
                            per_run = csub.groupby(["temperature", "run_index", "view"]).apply(
                                lambda g: g.sort_values("turn")[f"{col}_z"]
                                          .tail(max(1, len(g) // 3)).median(),
                                include_groups=False)
                            summ[cond] = round(float(per_run.median()), 3)
                        entry["velocity_dself"][f"{col}_z_final_third_median"] = summ

            for temp in temps:
                geo = endpoint_geometry(acts, temp, readout, layer)
                if geo:
                    entry["endpoints"][f"{temp:g}"] = {
                        "silhouette": round(geo["silhouette"], 4),
                        "within_over_across": round(geo["within_over_across"], 4)}
                    if layer == PLOT_LAYER and readout == PLOT_READOUT:
                        plot_endpoints(geo, temp)

            # Change-point lead times on strong conditions.
            for cond in [c for c in acts if c in ac.STRONG_CONDITIONS]:
                for temp in temps:
                    cp = pc_change_points(acts[cond], temp, readout, layer)
                    if cp.empty:
                        continue
                    for r in cp.itertuples():
                        beh = ac.onset_of(onsets, cond, temp, int(r.run_index))
                        b0t = ac.b0_onset_of(b0, cond, temp, int(r.run_index))
                        if beh is None:
                            continue
                        lead_records.append({
                            "layer": layer, "readout": readout, "condition": cond,
                            "temperature": temp, "run_index": int(r.run_index), "view": r.view,
                            "sensitivity": r.sensitivity,
                            "lead_internal": (beh - r.cp_turn) if r.cp_turn is not None else None,
                            "lead_b0": (beh - b0t) if b0t is not None else None})

            ldf = pd.DataFrame([r for r in lead_records
                                if r["layer"] == layer and r["readout"] == readout])
            if not ldf.empty:
                for sens, ssub in ldf.groupby("sensitivity"):
                    per_run = ssub.groupby(["condition", "temperature", "run_index"]).agg(
                        lead_internal=("lead_internal", "median"),
                        lead_b0=("lead_b0", "median")).reset_index()
                    li = per_run["lead_internal"].dropna()
                    both = per_run.dropna(subset=["lead_internal", "lead_b0"])
                    diffs = (both["lead_internal"] - both["lead_b0"]).values
                    entry["changepoint_leads"][f"{sens:g}"] = {
                        "n_runs": int(len(per_run)),
                        "frac_with_changepoint": round(float(len(li) / len(per_run)), 3),
                        "median_lead_internal": float(li.median()) if len(li) else None,
                        "median_lead_vs_b0": float(np.median(diffs)) if len(diffs) else None,
                        "p_beats_b0_signflip": ac.sign_flip_test(diffs) if len(diffs) else None}

            # Persona-vector validation (only meaningful at the vectors' own layer, but
            # computed per layer since the .pt files carry all layers).
            for cond in [c for c in acts if config.condition_lora(c)]:
                trait = config.condition_lora(cond)
                for temp in temps:
                    pv = pvec_projection(acts[cond], temp, layer, trait)
                    if pv:
                        entry["pvec_validation"][f"{cond}@{temp:g}"] = {
                            k: round(v, 4) for k, v in pv.items()}

            result["per_layer"][key] = entry

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    # Plots for the headline (layer 16, prompt_last) slice.
    plot_geometry(acts, temps, prefix_maps, onsets)
    plot_lead_curve(result["per_layer"].get(f"L{PLOT_LAYER}__{PLOT_READOUT}", {}))
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"wrote {args.out}")
    head = result["per_layer"].get(f"L{PLOT_LAYER}__{PLOT_READOUT}", {})
    print("headline (L16/prompt_last):",
          json.dumps({k: head.get(k) for k in ("endpoints", "changepoint_leads")}, indent=2))


# ---------------------------------------------------------------------------
# Plots (layer 16 / prompt_last)
# ---------------------------------------------------------------------------
def plot_endpoints(geo: dict, temp: float) -> None:
    fig, axes = ac.new_axes(1, 1, width=5.0, height=4.0)
    ax = axes[0][0]
    for cond in sorted(set(geo["_labels"])):
        m = geo["_labels"] == cond
        ax.scatter(geo["_pc2"][m, 0], geo["_pc2"][m, 1], s=18,
                   color=ac.condition_color(cond), label=cond, alpha=0.8)
    ax.legend(fontsize=7, frameon=False)
    ax.set_xlabel("PC1"); ax.set_ylabel("PC2")
    ax.set_title(f"Endpoint states, temp {temp:g} (L{PLOT_LAYER}, {PLOT_READOUT}) — "
                 f"silhouette {geo['silhouette']:.2f}", fontsize=10)
    ac.save_fig(fig, f"track_b__endpoints__temp{temp:g}.png", "track_b")


def plot_geometry(acts: dict, temps: list[float], prefix_maps: dict, onsets: dict) -> None:
    fig, axes = ac.new_axes(1, 2, width=5.0, height=3.4)
    for cond, rows in acts.items():
        for temp in temps:
            vd = velocity_and_dself(rows, temp, PLOT_READOUT, PLOT_LAYER,
                                    prefix_maps.get((cond, temp), {}))
            if vd.empty:
                continue
            med_v = vd.dropna(subset=["velocity"]).groupby("turn")["velocity"].median()
            med_d = vd.groupby("turn")["d_self"].median()
            axes[0][0].plot(med_v.index, med_v.values, color=ac.condition_color(cond),
                            alpha=0.5, linewidth=1.2)
            axes[0][1].plot(med_d.index, med_d.values, color=ac.condition_color(cond),
                            alpha=0.5, linewidth=1.2)
    for ax, title in zip(axes.flat, ("velocity ||h(k+1)-h(k)||", "d_self ||h(k)-h(1)||")):
        ax.set_title(title, fontsize=9); ax.set_xlabel("turn")
    import matplotlib.lines as mlines
    handles = [mlines.Line2D([], [], color=ac.condition_color(c), label=c) for c in acts]
    axes[0][1].legend(handles=handles, fontsize=6, frameon=False)
    fig.suptitle(f"Track B trajectories, L{PLOT_LAYER}/{PLOT_READOUT} "
                 "(median across runs; one line per condition x temp)", fontsize=10)
    ac.save_fig(fig, "track_b__velocity_dself.png", "track_b")

    fig, axes = ac.new_axes(1, 1, width=5.0, height=3.4)
    ax = axes[0][0]
    for cond, rows in acts.items():
        for temp in temps:
            F = funneling(rows, temp, PLOT_READOUT, PLOT_LAYER)
            if F:
                ax.plot(list(F.keys()), list(F.values()), color=ac.condition_color(cond),
                        alpha=0.6, linewidth=1.2)
    ax.axhline(1.0, color="#999999", linewidth=1, linestyle=":")
    ax.set_xlabel("own-turn rank"); ax.set_ylabel("between-run distance / rank-0 distance")
    ax.set_title("Funneling: do runs of a condition converge to the same region?", fontsize=10)
    handles = [mlines.Line2D([], [], color=ac.condition_color(c), label=c) for c in acts]
    ax.legend(handles=handles, fontsize=6, frameon=False)
    ac.save_fig(fig, "track_b__funneling.png", "track_b")


def plot_lead_curve(entry: dict) -> None:
    leads = entry.get("changepoint_leads", {})
    if not leads:
        return
    fig, axes = ac.new_axes(1, 1, width=4.6, height=3.2)
    ax = axes[0][0]
    xs = sorted(leads, key=float)
    med = [leads[s]["median_lead_internal"] for s in xs]
    frac = [leads[s]["frac_with_changepoint"] for s in xs]
    ax.plot([float(x) for x in xs], med, color="#0072B2", linewidth=2, marker="o",
            label="median lead (turns)")
    ax.plot([float(x) for x in xs], [f * 10 for f in frac], color="#999999", linewidth=1.5,
            linestyle="--", marker="s", label="frac runs w/ change-point (x10)")
    ax.axhline(config.PREDICTION_LEAD_TURNS, color="#D55E00", linewidth=1, linestyle=":")
    ax.set_xlabel("change-point sensitivity (sd units)")
    ax.set_title("Prediction lead time vs detector sensitivity (L16/prompt_last)", fontsize=10)
    ax.legend(fontsize=7, frameon=False)
    ac.save_fig(fig, "track_b__lead_vs_sensitivity.png", "track_b")


if __name__ == "__main__":
    main()
