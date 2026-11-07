---
title: "Document Extraction"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction
scraped_at: 2026-11-07T17:19:38.837571+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/document-extraction)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
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
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Core
  * Document Extraction


On this page
# Document Extraction
The `read_file` tool automatically converts common document formats to readable text, so the agent can inspect a PDF or spreadsheet the same way it reads source code.
## Supported formats[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction#supported-formats "Direct link to Supported formats")  
| Format  | Extensions  | Converter  | Availability  |  
| --- | --- | --- | --- |  
| Jupyter notebooks  | `.ipynb`  | Built-in (stdlib)  | Always  |  
| Word documents  | `.docx`  | Built-in (stdlib)  | Always  |  
| Excel workbooks  | `.xlsx`  | Built-in (stdlib)  | Always  |  
| SQLite databases  |  `.db`, `.sqlite`, `.sqlite3`  | Built-in (stdlib)  | Always  |  
| PDF  | `.pdf`  | Optional `anydoc` converter  | Auto-installed on first use*  |  
| Legacy Office  |  `.doc`, `.ppt`, `.xls`, `.pptx`, and variants  | Optional `anydoc` converter  | Auto-installed on first use*  |  
| OpenDocument  |  `.odt`, `.ods`, `.odp`  | Optional `anydoc` converter  | Auto-installed on first use*  |  
| Rich text / eBooks  |  `.rtf`, `.epub`  | Optional `anydoc` converter  | Auto-installed on first use*  |  
* The optional converter is the `firecrawl-anydoc` package, installed lazily where installs are permitted (`security.allow_lazy_installs` in `config.yaml`). Without it, the three stdlib formats still work; other formats fall back to the binary-file guard.
SQLite files render as a schema overview rather than a dump: each table's `CREATE` statement, row count and first five rows, plus the list of indexes, views and triggers. The database is opened read-only (`mode=ro&immutable=1`, so a live database another process holds open is still readable without locks); for anything beyond the preview, query it from the terminal with `sqlite3`. A `.db` that is not SQLite (the magic bytes do not match) is refused with the real reason. Hermes's own read denylist applies before extraction, so protected stores under `HERMES_HOME` stay unreadable.
`read_file` also flags unresolved git merge conflicts: when the returned range contains balanced `<<<<<<< ` / `>>>>>>> ` marker lines, the result carries `conflict_blocks: N` and a hint to resolve them before editing around them. A lone marker inside a string or a test fixture is not counted.
Conversion output is Markdown, paginated through `read_file`'s normal `offset`/`limit` window. East Asian phonetic guides (XLSX `rPh`, DOCX ruby text) annotate cell or run text and are not part of the extracted value: a cell holding 東京 with the guide トウキョウ reads as `東京`. Documents over 50 MB are refused to keep tool turns bounded.
Notebook cell outputs longer than 20,000 characters are truncated; the truncation marker carries a `jq` command that names the notebook's full, shell-quoted path so the omitted output can be pulled from the original file.
Extraction works with remote terminal backends (Docker, Modal, SSH): the file's bytes are transferred across the backend boundary and converted host-side, so a document inside a sandbox reads the same as a local one.
## Scanned PDFs: the coverage warning[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction#scanned-pdfs-the-coverage-warning "Direct link to Scanned PDFs: the coverage warning")
PDF conversion reads the **text layer only**. Pages that are scanned images — common in legal documents, resale packages, signed contracts, faxes — contain no text layer and silently convert to nothing. The telltale signature is section headers with empty bodies.
When a meaningful share of pages yields no text (over 20% of the document, or 10+ pages absolute), `read_file` prepends a warning to the extraction. Each unreadable gap is labeled with the last text extracted before it — usually a section divider — so the agent can target only the gaps it actually needs instead of OCRing the whole document:

```


[EXTRACTION COVERAGE WARNING: 198 of 311 pages in this PDF yielded no  





text. ... Unreadable gaps, each labeled with the last text extracted  





before it:  





  pages 42-77 (36 pages) — after "Antigua Maintenance Corp Bylaws" (p41)  





  pages 92-213 (122 pages) — after "... Covenants, Codes and Regulations" (p91)  





  page 224 (1 page) — after "... Insurance Declaration Pages" (p223)  





Decide which gaps you actually need — do NOT OCR or render everything. ...]  



```

The warning lists the exact page ranges and the recovery paths:
  1. **A few pages — render + vision.** Convert the pages to images and read them with the vision tool:

```


pdftoppm -jpeg -r 150 -f 92 -l 94 document.pdf $TMPDIR/page  



```

Then inspect each image with `vision_analyze`. Zero extra dependencies (poppler is required for the detection itself).
  2. **Many pages — OCR.** The `ocr-and-documents` skill covers bulk OCR with marker-pdf (90+ languages, handles equations and tables; ~3-5 GB install).


Detection uses poppler's `pdftotext` for per-page text counts. If poppler is not installed, extraction still works — the coverage check is silently skipped.
The agent handles the warning on its own — it will offer to render or OCR the missing pages. If you're reading extractions yourself, treat "header with an empty body" as a scanned section, not a missing one.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/document-extraction.md)
[Previous Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)[Next Tool Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-search)
  * [Supported formats](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction#supported-formats)
  * [Scanned PDFs: the coverage warning](https://hermes-agent.nousresearch.com/docs/user-guide/features/document-extraction#scanned-pdfs-the-coverage-warning)


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
