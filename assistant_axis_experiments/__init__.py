"""assistant_axis_experiments — Assistant-Axis experiments on AttractorBench ai2ai conversations.

Shared infrastructure at the top level (axes, per-view transcript replay, capped/steered
serving; method vendored verbatim from safety-research/assistant-axis — see
vendor/assistant_axis/__init__.py for attribution). Subpackages:

- ``drift/``       1-D drift down the Assistant Axis (the original experiment: generation via
                   configs/axis_ai2ai.py -> project_transcripts.py on the pod ->
                   drift.analyze_axis on the laptop).
- ``state_space/`` beyond the 1-D axis: persona-space principal components, (a_t, z_t) state
                   decomposition, prediction of basin/entry-time/intervention response, and
                   causal orthogonal steering. See state_space/README.md.
"""
