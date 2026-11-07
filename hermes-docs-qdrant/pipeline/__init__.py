"""Post-scrape RAG pipeline, vendored so the plugin is self-contained.

Runtime state lives in the plugin data home (see `pipeline/paths.py`), never in
this directory: the install tree is replaced on `hermes plugins update`.
"""
