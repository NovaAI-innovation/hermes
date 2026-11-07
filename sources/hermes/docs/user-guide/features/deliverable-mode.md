---
title: "Deliverable Mode (Artifacts in Chat)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode
scraped_at: 2026-11-07T17:19:38.836564+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/deliverable-mode)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
      * [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)
      * [Wake Word](https://hermes-agent.nousresearch.com/docs/user-guide/features/wake-word)
      * [Web Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)
      * [X (Twitter) Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search)
      * [Browser](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser)
      * [Passwords & Logins](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-vault)
      * [Computer Use](https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use)
      * [Bot Screen](https://hermes-agent.nousresearch.com/docs/user-guide/features/bot-screen)
      * [Vision & Image Paste](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision)
      * [Image Generation](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation)
      * [Spotify](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify)
      * [Pets (Petdex Mascots)](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets)
      * [Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts)
      * [Deliverable Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Media & Web
  * Deliverable Mode


On this page
# Deliverable Mode
When Hermes Agent runs inside a messaging gateway (Slack, Discord, Telegram, WhatsApp, Signal, etc.), it can deliver generated files directly into the chat — not as paths the user has to copy, but as native attachments.
A chart shows up as an inline image. A PDF report shows up as a file download. A spreadsheet uploads as `.xlsx`. The agent does not need to write a `MEDIA:` tag or do anything special — it just generates the file and mentions its absolute path in the response. The gateway picks the path out of the text, removes it from the visible message, and uploads the file natively.
## How it works[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#how-it-works "Direct link to How it works")
Three pieces fit together:
  1. **The agent has tools that produce files.** `execute_code` for charts via matplotlib, the `microsoft-office` skill for Word documents, spreadsheets and decks, the `pdf` and `latex-pdf-report` skills for PDFs, `image_generate` for images, `text_to_speech` for audio, and so on.
  2. **The gateway scans agent responses for file paths.** Any absolute path (`~/.hermes/cache/scratch/...`) or home-relative path (`~/...`) ending in a supported extension gets extracted. Paths inside code blocks and inline code are ignored so code samples are never mutilated.
  3. **The gateway dispatches by file type.** Images embed inline where the platform supports it; videos embed inline; audio routes to voice/audio attachments; everything else uploads as a file attachment.


## Supported file extensions[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#supported-file-extensions "Direct link to Supported file extensions")  
| Category  | Extensions  | Delivery  |  
| --- | --- | --- |  
| Images  | `.png .jpg .jpeg .gif .webp .bmp .tiff .svg`  | Inline embed  |  
| Video  | `.mp4 .mov .avi .mkv .webm .3gp`  | Inline embed (where supported)  |  
| Audio  | `.mp3 .m2a .wav .ogg .opus .m4a .flac`  | Voice / audio attachment  |  
| Documents  | `.pdf .docx .doc .odt .rtf .txt .md .epub`  | File upload  |  
| Data  | `.xlsx .xls .ods .csv .tsv .json .xml .yaml .yml`  | File upload  |  
| Geospatial  | `.kmz .kml .geojson .gpx`  | File upload  |  
| Presentations  | `.pptx .ppt .odp .key`  | File upload  |  
| Archives  | `.zip .tar .gz .tgz .bz2 .xz .7z .rar .apk .ipa`  | File upload  |  
| Web  | `.html .htm`  | File upload  |  
`.py`, `.log`, and other source-file extensions are intentionally excluded so the agent doesn't auto-ship arbitrary source files; if you want to send code to the user, use a code block.
## Encouraging the agent to produce artifacts[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#encouraging-the-agent-to-produce-artifacts "Direct link to Encouraging the agent to produce artifacts")
The agent doesn't reach for artifacts by default — it has to know to. Two ways to nudge it:
**Per-session:** ask explicitly ("send me the comparison as a chart", "return the data as a CSV") or write your own custom-instructions / personality entry that biases toward artifact-style replies on messaging platforms.
**Project-level:** add the bias to `AGENTS.md` / `CLAUDE.md` / `.cursorrules` in a project the agent works from, to your global persona in `~/.hermes/SOUL.md`, or as a named preset under `agent.personalities` in `~/.hermes/config.yaml` (switchable per session via `/personality`).
The mechanic the agent has to use is simple: render the file to an absolute path (e.g. `~/.hermes/cache/scratch/q3-revenue.png`) and mention that path as plain text in the reply. The gateway does the rest. Paths inside fenced code blocks or backticks are ignored so code samples are never mutilated.
## Kanban: artifacts ride completion notifications[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#kanban-artifacts-ride-completion-notifications "Direct link to Kanban: artifacts ride completion notifications")
If you use Hermes' kanban multi-agent workflow, workers can attach deliverable files to their `kanban_complete` call:

```


kanban_complete(  





    summary="rendered Q3 revenue chart and report",  





    artifacts=[  





        "~/.hermes/cache/scratch/q3-revenue.png",  





        "~/.hermes/cache/scratch/q3-report.pdf",  





    ],  





)  



```

When the gateway notifier delivers the "task completed" message to whoever subscribed to the task in Slack/Telegram/etc., it also uploads each artifact as a native attachment to that chat. The human gets the deliverable and the summary in one place.
Files that don't exist on disk when the notifier runs are silently skipped.
## Connecting more services with MCP[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#connecting-more-services-with-mcp "Direct link to Connecting more services with MCP")
Beyond the artifact-delivery pipeline, the agent can reach into other services via MCP (Model Context Protocol). The MCP ecosystem ships community servers for most popular tools — install whichever you need:  
| Service  | What it unlocks  |  
| --- | --- |  
| **Notion**  | Read/write Notion pages, databases, query workspace  |  
| **GitHub**  | Issues, PRs, comments, repo search beyond the gh CLI  |  
| **Linear**  | Tickets, projects, cycles  |  
| **Slack**  | Workspace-wide search, read other channels  |  
| **Gmail**  | Inbox triage, send mail, label management  |  
| **Salesforce**  | Leads, opportunities, account data  |  
| **Snowflake / BigQuery**  | SQL against data warehouses  |  
| **Google Drive**  | File search, contents, share management  |  
Install MCP servers via `~/.hermes/config.yaml` under the `mcp_servers` section. See [MCP integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) for the full setup guide.
## Comparison to Perplexity Computer in Slack[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#comparison-to-perplexity-computer-in-slack "Direct link to Comparison to Perplexity Computer in Slack")
Perplexity Computer's Slack integration is built around the same idea: the agent generates a deliverable (chart, PDF, slide deck) and posts it back into the thread as a native attachment. Hermes Agent's deliverable mode provides the same user-facing pattern locally:
  * Generation happens in the user's own venv / sandbox (no remote tenant).
  * Files land in the chat via the same Slack `files.uploadV2` API.
  * Connector breadth comes via MCP rather than a curated catalog of 400 hosted integrations — install the ones you actually use.


OAuth tokens stay on the user's machine in `auth.json` / `.env`. No hosted token storage. No multi-tenant microVM. Same end result.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/deliverable-mode.md)
[Previous Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts)[Next Hermes Web Dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
  * [How it works](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#how-it-works)
  * [Supported file extensions](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#supported-file-extensions)
  * [Encouraging the agent to produce artifacts](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#encouraging-the-agent-to-produce-artifacts)
  * [Kanban: artifacts ride completion notifications](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#kanban-artifacts-ride-completion-notifications)
  * [Connecting more services with MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#connecting-more-services-with-mcp)
  * [Comparison to Perplexity Computer in Slack](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode#comparison-to-perplexity-computer-in-slack)


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
