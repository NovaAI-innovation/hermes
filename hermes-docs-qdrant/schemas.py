"""Tool schemas exposed to the agent.

Descriptions are derived from the live corpus shape rather than hardcoded, so
adding a source to sources.yaml does not leave the tools claiming the corpus is
something it is not.
"""

SEARCH = {
    "type": "function",
    "function": {
        "name": "docs_search",
        "description": (
            "Hybrid (dense + BM25) search across every ingested documentation "
            "source. Use for any question about how a library, API, gateway, or "
            "the llms.txt specification works. Returns ranked passages, each with "
            "doc_id, source, source_url, heading and text. Call docs_read with a "
            "returned doc_id when you need the whole page. Filter with `source` "
            "when you know which corpus to search."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural-language question or keywords, e.g. 'connect telegram gateway'.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Passages to return (default 6, max 20).",
                },
                "source": {
                    "type": "string",
                    "description": "Restrict to one corpus, e.g. 'hermes', 'portkey', 'llmstxt'. Call docs_outline for the current list.",
                },
                "doc_type": {
                    "type": "string",
                    "description": "Restrict by document type, e.g. 'reference', 'guide', 'developer', 'changelog'.",
                },
                "section": {
                    "type": "string",
                    "description": "Restrict by top-level section name, e.g. 'Reference', 'Docs'.",
                },
            },
            "required": ["query"],
        },
    },
}

SEARCH_MANY = {
    "type": "function",
    "function": {
        "name": "docs_search_many",
        "description": (
            "Run several independent queries in one call and keep the results "
            "separated by query. Use to compare what the corpus says about "
            "different topics at once (e.g. ['reranking', 'guardrails']) instead "
            "of calling docs_search repeatedly."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "queries": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Two or more search queries.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Passages per query (default 4, max 10).",
                },
                "source": {"type": "string", "description": "Restrict all queries to one corpus."},
                "doc_type": {"type": "string", "description": "Restrict all queries by document type."},
            },
            "required": ["queries"],
        },
    },
}

READ = {
    "type": "function",
    "function": {
        "name": "docs_read",
        "description": (
            "Read a complete documentation page by doc_id, reassembled from its "
            "chunks in order. Use after docs_search when isolated passages are "
            "not enough. doc_id is source-qualified, e.g. 'hermes:user-guide/cli' "
            "or 'portkey:product/guardrails'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "doc_id": {
                    "type": "string",
                    "description": "Exact doc_id from a docs_search result or docs_outline.",
                },
                "max_chars": {
                    "type": "integer",
                    "description": "Truncate the page at this many characters (default 12000, max 60000).",
                },
            },
            "required": ["doc_id"],
        },
    },
}

OUTLINE = {
    "type": "function",
    "function": {
        "name": "docs_outline",
        "description": (
            "Describe the corpus: which sources, doc types and sections exist and "
            "how many chunks each holds. With doc_id, returns that page's heading "
            "structure instead. Call this first when you do not know which corpus "
            "or filter to use."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "doc_id": {
                    "type": "string",
                    "description": "Optional page id; omit for the corpus overview.",
                },
            },
            "required": [],
        },
    },
}

LIST_DOCS = {
    "type": "function",
    "function": {
        "name": "docs_list",
        "description": (
            "List documents in the corpus, filtered by source, doc_type or "
            "doc_id prefix. Use to discover what is available before searching, "
            "or to enumerate one source's pages."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "source": {"type": "string", "description": "Restrict to one corpus, e.g. 'portkey'."},
                "doc_type": {"type": "string", "description": "Restrict by document type."},
                "prefix": {
                    "type": "string",
                    "description": "Only doc_ids starting with this string, e.g. 'portkey:api-reference'.",
                },
                "limit": {"type": "integer", "description": "Maximum documents to return (default 100, max 500)."},
            },
            "required": [],
        },
    },
}

STATS = {
    "type": "function",
    "function": {
        "name": "docs_stats",
        "description": (
            "Report corpus health and size: collection name, reachability, total "
            "documents and chunks, and a per-source breakdown. Use to confirm the "
            "index is populated before trusting search results."
        ),
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
}

REBUILD = {
    "type": "function",
    "function": {
        "name": "docs_rebuild",
        "description": (
            "Rebuild the local corpus from the sources configured in sources.yaml: "
            "optionally re-scrape each llms.txt, then normalize, enrich, chunk and "
            "re-index into Qdrant. This is long-running (minutes) and replaces the "
            "collection. Use when the user asks to refresh, update or re-ingest the "
            "documentation. Set scrape=false to rebuild only from already-downloaded "
            "pages. Requires crawl4ai in the build environment when scrape=true."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "scrape": {
                    "type": "boolean",
                    "description": "Re-download every configured source first (default false).",
                },
                "sources": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Limit scraping to these source names; omit for all configured sources.",
                },
                "reindex": {
                    "type": "boolean",
                    "description": "Rebuild the Qdrant collection after chunking (default true).",
                },
                "refresh": {
                    "type": "boolean",
                    "description": "With scrape=true, force re-download of pages already on disk.",
                },
            },
            "required": [],
        },
    },
}

ALL = [SEARCH, SEARCH_MANY, READ, OUTLINE, LIST_DOCS, STATS, REBUILD]
