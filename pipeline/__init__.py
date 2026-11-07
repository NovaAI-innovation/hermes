"""Post-scrape RAG pipeline for the Hermes docs corpus.

Stages:
    normalize  strip Docusaurus chrome from docs/ -> clean/
    enrich     attach llms.txt metadata -> corpus/documents.jsonl
    chunk      header-aware retrieval units -> corpus/chunks.jsonl
    index      dense FAISS + sparse BM25 -> corpus/index/
    retrieve   hybrid search CLI
    eval       recall@k harness over eval/queries.jsonl
"""
