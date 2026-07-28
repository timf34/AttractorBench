"""assistant_axis_drift — measure Assistant-Axis drift in AttractorBench ai2ai conversations.

Pipeline: configs/axis_ai2ai.py (generate) -> project_transcripts.py (GPU: replay + project)
-> analyze_axis.py (CPU: figures + report). Method vendored verbatim from
safety-research/assistant-axis (see vendor/assistant_axis/__init__.py for attribution).
"""
