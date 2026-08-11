"""state_space — beyond the 1-D Assistant Axis.

Is one number (the axis projection a_t) enough to describe where an ai2ai conversation is
going, or do the orthogonal persona coordinates z_t carry the information about WHICH basin a
run falls into and when? See README.md for the full programme; pipeline:

  persona_space.py     (laptop) role-vector PCA -> bases/<model>.npz + geometry figures
  dump_activations.py  (pod)    replay transcripts -> per-turn mean activations npz
  featurize.py         (laptop) activations x basis -> per-turn (a_t, z_t) state features
  predict.py           (laptop) a_t-only vs a_t+z_t on the four prediction tasks
  steered_server.py    (pod)    causal test: steer an axis-orthogonal persona direction
"""
