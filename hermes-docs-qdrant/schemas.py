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
            "Hybrid (dense + BM25) search with single-mode fallback across every ingested documentation "
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
                    "description": "One to ten search queries.",
                },
                "limit": {
                    "type": "integer",
                    "description": "Passages per query (default 4, max 10).",
                },
                "source": {"type": "string", "description": "Restrict all queries to one corpus."},
                "doc_type": {"type": "string", "description": "Restrict all queries by document type."},
                "section": {"type": "string", "description": "Restrict all queries to one top-level section."},
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
            "Build the corpus from sources.yaml. Read configured llms.txt indexes and "
            "download new pages by default, then normalize, enrich, chunk and index "
            "in Qdrant. The current index serves retrieval until the replacement is "
            "ready. The tool can take several minutes. HTML crawling requires Crawl4AI."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "scrape": {
                    "type": "boolean",
                    "description": "Read source indexes and fetch missing pages (default true). Set false for a cached-only build.",
                },
                "sources": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Limit fetching to these names. Cached pages from other configured sources are included in the build.",
                },
                "reindex": {
                    "type": "boolean",
                    "description": "Publish the new Qdrant index (default true). Set false to build artifacts only.",
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

DIAGNOSTICS = {
    "type": "function",
    "function": {
        "name": "docs_diagnostics",
        "description": (
            "Report plugin health when documentation tools appear missing or "
            "fail: dependency versions, which requirements are unmet, the "
            "collection target, and whether it is reachable. Call this first "
            "when docs_search is unavailable in a session."
        ),
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
}

ALL = [SEARCH, SEARCH_MANY, READ, OUTLINE, LIST_DOCS, STATS, DIAGNOSTICS, REBUILD]
