---
title: "Overview"
source: "https://modelcontextprotocol.io/specification/2026-07-28/server/index.md"
scraped_at: "2026-11-07T19:33:49.513008+00:00"
doc_id: "specification/2026-07-28/server/index"
content_hash: "6b24e9cd66b0d908"
corpus_source: "mcp"
---

# Overview

Servers provide the fundamental building blocks for adding context to language models via
MCP. These primitives enable rich interactions between clients, servers, and language
models:

* **Prompts**: Pre-defined templates or instructions that guide language model
  interactions
* **Resources**: Structured data or content that provides additional context to the model
* **Tools**: Executable functions that allow models to perform actions or retrieve
  information

Each primitive can be summarized in the following control hierarchy:

| Primitive | Control | Description | Example |
| - | - | - | - |
| Prompts | User-controlled | Interactive templates invoked by user choice | Slash commands, menu options |
| Resources | Application-controlled | Contextual data attached and managed by the client | File contents, git history |
| Tools | Model-controlled | Functions exposed to the LLM to take actions | API POST requests, file writing |

Explore these key primitives in more detail below:

> [card] [Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)

> [card] [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)

> [card] [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)
