"""Persona-vector steering for AttractorBench.

Steers the base Llama with the *persona vectors* extracted in the persona_vectors repo
(https://github.com/timf34/persona_vectors) — i.e. plain activation addition of a per-trait
mean-difference direction into the residual stream — served behind an OpenAI-compatible endpoint
so the existing AttractorBench harness/judge/summarize run unchanged.

This is NOT SAE steering. There is no SAE, no feature discovery: the intervention is
    resid[layer] += coef * persona_vec[trait][layer]
where persona_vec[trait] is `<trait>_response_avg_diff.pt` (shape [num_layers+1, d_model]).
"""
