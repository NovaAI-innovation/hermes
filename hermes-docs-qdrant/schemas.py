"""Tool schemas exposed to the agent."""

SEARCH = {
    "type": "function",
    "function": {
        "name": "docs_search",
        "description": (
            "Search the Hermes Agent documentation (249 pages: CLI, configuration, "
            "messaging gateways, features, developer guide, reference). Use for any "
            "question about how Hermes works, how to configure it, or which command "
            "performs an action. Returns ranked passages with source URLs."
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
                    "description": "Number of passages to return (default 6, max 20).",
                },
                "doc_type": {
                    "type": "string",
                    "description": "Optional filter. One of: reference, guide, feature, messaging, developer, getting-started.",
                },
                "section": {
                    "type": "string",
                    "description": "Optional filter, e.g. 'Using Hermes', 'Core Features', 'Reference'.",
                },
            },
            "required": ["query"],
        },
    },
}

READ = {
    "type": "function",
    "function": {
        "name": "docs_read",
        "description": (
            "Read the full contents of one Hermes documentation page by doc_id "
            "(for example 'user-guide/features/cron'). Use after docs_search when "
            "you need the complete page rather than isolated passages."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "doc_id": {
                    "type": "string",
                    "description": "Page id from a docs_search result, e.g. 'getting-started/quickstart'.",
                },
                "max_chars": {
                    "type": "integer",
                    "description": "Truncate the page at this many characters (default 12000).",
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
            "List the Hermes documentation structure: available sections and doc types "
            "with chunk counts, or the headings of one page when doc_id is given. Use "
            "to orient before searching."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "doc_id": {
                    "type": "string",
                    "description": "Optional page id; when omitted, returns the corpus outline.",
                },
            },
            "required": [],
        },
    },
}

ALL = [SEARCH, READ, OUTLINE]
