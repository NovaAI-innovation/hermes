---
title: "Context References"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references
scraped_at: 2026-11-07T17:19:30.399207+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
      * [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
      * [Document Extraction](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
      * [Tool Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-search)
      * [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
      * [LSP — Semantic Diagnostics](https://hermes-agent.nousresearch.com/docs/user-guide/features/lsp)
      * [Curator](https://hermes-agent.nousresearch.com/docs/user-guide/features/curator)
      * [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
      * [Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)
      * [Honcho Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho)
      * [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
      * [Context References](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
      * [Mixture of Agents](https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents)
      * [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)
      * [Skins & Themes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins)
      * [Language Packs](https://hermes-agent.nousresearch.com/docs/user-guide/features/language-packs)
      * [Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)
      * [Built-in Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/built-in-plugins)
      * [Plugin Catalog](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugin-catalog)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Core
  * Context References


On this page
# Context References
Type `@` followed by a reference to inject content directly into your message. Hermes expands the reference inline and appends the content under an `--- Attached Context ---` section.
## Supported References[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#supported-references "Direct link to Supported References")  
| Syntax  | Description  |  
| --- | --- |  
| `@file:path/to/file.py`  | Inject file contents  |  
| `@file:path/to/file.py:10-25`  | Inject specific line range (1-indexed, inclusive)  |  
| `@folder:path/to/dir`  | Inject directory tree listing with file metadata  |  
| `@diff`  | Inject `git diff` (unstaged working tree changes)  |  
| `@staged`  | Inject `git diff --staged` (staged changes)  |  
| `@git:5`  | Inject last N commits with patches (max 10)  |  
| `@url:https://example.com`  | Fetch and inject web page content  |  
## Usage Examples[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#usage-examples "Direct link to Usage Examples")

```


Review @file:src/main.py and suggest improvements  





  





What changed? @diff  





  





Compare @file:old_config.yaml and @file:new_config.yaml  





  





What's in @folder:src/components?  





  





Summarize this article @url:https://arxiv.org/abs/2301.00001  



```

Multiple references work in a single message:

```


Check @file:main.py, and also @file:test.py.  



```

Trailing punctuation (`,`, `.`, `;`, `!`, `?`) is automatically stripped from reference values.
## CLI Tab Completion[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#cli-tab-completion "Direct link to CLI Tab Completion")
In the interactive CLI, typing `@` triggers autocomplete:
  * `@` shows all reference types (`@diff`, `@staged`, `@file:`, `@folder:`, `@git:`, `@url:`)
  * `@file:` and `@folder:` trigger filesystem path completion with file size metadata
  * Bare `@` followed by partial text shows matching files and folders from the current directory


## Line Ranges[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#line-ranges "Direct link to Line Ranges")
The `@file:` reference supports line ranges for precise content injection:

```


@file:src/main.py:42        # Single line 42  





@file:src/main.py:10-25     # Lines 10 through 25 (inclusive)  



```

Lines are 1-indexed. Invalid ranges are silently ignored (full file is returned).
## Size Limits[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#size-limits "Direct link to Size Limits")
Context references are bounded to prevent overwhelming the model's context window:  
| Threshold  | Value  | Behavior  |  
| --- | --- | --- |  
| Soft limit  | 25% of context length  | Warning appended, expansion proceeds  |  
| Hard limit  | 50% of context length  | Expansion refused, original message returned unchanged  |  
| Folder entries  | 200 files max  | Excess entries replaced with `- ...`  |  
| Git commits  | 10 max  |  `@git:N` clamped to range [1, 10]  |  
## Security[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#security "Direct link to Security")
### Sensitive Path Blocking[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#sensitive-path-blocking "Direct link to Sensitive Path Blocking")
These paths are always blocked from `@file:` references to prevent credential exposure:
  * SSH keys and config: `~/.ssh/id_rsa`, `~/.ssh/id_ed25519`, `~/.ssh/authorized_keys`, `~/.ssh/config`
  * Shell profiles: `~/.bashrc`, `~/.zshrc`, `~/.profile`, `~/.bash_profile`, `~/.zprofile`
  * Credential files: `~/.netrc`, `~/.pgpass`, `~/.npmrc`, `~/.pypirc`
  * Hermes env: `$HERMES_HOME/.env`


These directories are fully blocked (any file inside):
  * `~/.ssh/`, `~/.aws/`, `~/.gnupg/`, `~/.kube/`, `$HERMES_HOME/skills/.hub/`


### Path Traversal Protection[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#path-traversal-protection "Direct link to Path Traversal Protection")
All paths are resolved relative to the working directory. References that resolve outside the allowed workspace root are rejected.
### Binary File Detection[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#binary-file-detection "Direct link to Binary File Detection")
Binary files are detected via MIME type and null-byte scanning. Known text extensions (`.py`, `.md`, `.json`, `.yaml`, `.toml`, `.js`, `.ts`, etc.) bypass MIME-based detection. Binary files are rejected with a warning.
## Platform Availability[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#platform-availability "Direct link to Platform Availability")
Context references are primarily a **CLI feature**. They work in the interactive CLI where `@` triggers tab completion and references are expanded before the message is sent to the agent.
In **messaging platforms** (Telegram, Discord, etc.), the `@` syntax is not expanded by the gateway — messages are passed through as-is. The agent itself can still reference files via the `read_file`, `search_files`, and `web_extract` tools.
## Interaction with Context Compression[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#interaction-with-context-compression "Direct link to Interaction with Context Compression")
When conversation context is compressed, the expanded reference content is included in the compression summary. This means:
  * Large file contents injected via `@file:` contribute to context usage
  * If the conversation is later compressed, the file content is summarized (not preserved verbatim)
  * For very large files, consider using line ranges (`@file:main.py:100-200`) to inject only relevant sections


## Common Patterns[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#common-patterns "Direct link to Common Patterns")

```


# Code review workflow  





Review @diff and check for security issues  





  





# Debug with context  





This test is failing. Here's the test @file:tests/test_auth.py  





and the implementation @file:src/auth.py:50-80  





  





# Project exploration  





What does this project do? @folder:src @file:README.md  





  





# Research  





Compare the approaches in @url:https://arxiv.org/abs/2301.00001  





and @url:https://arxiv.org/abs/2301.00002  



```

## Error Handling[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#error-handling "Direct link to Error Handling")
Invalid references produce inline warnings rather than failures:  
| Condition  | Behavior  |  
| --- | --- |  
| File not found  | Warning: "file not found"  |  
| Binary file  | Warning: "binary files are not supported"  |  
| Folder not found  | Warning: "folder not found"  |  
| Git command fails  | Warning with git stderr  |  
| URL returns no content  | Warning: "no content extracted"  |  
| Sensitive path  | Warning: "path is a sensitive credential file"  |  
| Path outside workspace  | Warning: "path is outside the allowed workspace"  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/context-references.md)
[Previous Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)[Next Mixture of Agents](https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents)
  * [Supported References](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#supported-references)
  * [Usage Examples](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#usage-examples)
  * [CLI Tab Completion](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#cli-tab-completion)
  * [Line Ranges](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#line-ranges)
  * [Size Limits](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#size-limits)
  * [Security](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#security)
    * [Sensitive Path Blocking](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#sensitive-path-blocking)
    * [Path Traversal Protection](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#path-traversal-protection)
    * [Binary File Detection](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#binary-file-detection)
  * [Platform Availability](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#platform-availability)
  * [Interaction with Context Compression](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#interaction-with-context-compression)
  * [Common Patterns](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#common-patterns)
  * [Error Handling](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-references#error-handling)


Docs
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [User Guide](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


Community
  * [Discord](https://discord.gg/NousResearch)
  * [GitHub Issues](https://github.com/NousResearch/hermes-agent/issues)
  * [Skills Hub](https://agentskills.io)


More
  * [Desktop Download](https://hermes-agent.nousresearch.com/)
  * [GitHub](https://github.com/NousResearch/hermes-agent)
  * [Nous Research](https://nousresearch.com)


Built by [Nous Research](https://nousresearch.com) · MIT License · 2026
