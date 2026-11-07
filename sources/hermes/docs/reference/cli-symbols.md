---
title: "CLI Symbols Glossary"
source: https://hermes-agent.nousresearch.com/docs/reference/cli-symbols
scraped_at: 2026-11-07T17:20:37.818523+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [English](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/cli-symbols)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Features](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
    * [Command Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
    * [Configuration Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
    * [Tools & Skills Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
    * [CLI Symbols Glossary](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols)
    * [FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Reference
  * CLI Symbols Glossary


On this page
# CLI Symbols Glossary
The Hermes terminal interfaces speak a compact visual language: dots, chevrons, braille spinners, and status glyphs. This page is the decoder ring. It covers the [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui) (where most of these render) and notes the pieces shared with the [Classic CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli).
Glyphs marked _themeable_ below are brand defaults — a [skin](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) can override them (for example `tool_prefix` and the prompt symbol). Everything else is fixed in the renderer.
## Transcript symbols[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#transcript-symbols "Direct link to Transcript symbols")
What you see in the conversation flow while the agent works.  
| Symbol  | Meaning  |  
| --- | --- |  
| `❯`  | Input prompt — where you type. _Themeable_ (skins set their own prompt symbol).  |  
| `●`  | A tool call. The bullet precedes the tool name and its arguments.  |  
| `┊`  | Tool-activity rail shown with tool lines. _Themeable_ (`tool_prefix`).  |  
|  `✓` / `✗`  | Tool result: succeeded / failed. Appended to the end of a completed tool line.  |  
|  `▸` / `▾`  | Collapsed / expanded section chevron (thinking, tools, subagents, banner sections). Click to toggle.  |  
| `▍`  | Streaming cursor — blinks while the model is still emitting text.  |  
|  `│` `├─` `└─`  | Tree rails — connect a parent (a delegation, a journey) to its child entries; `└─` marks the last child.  |  
| `◈`  | Display-only timeline event (session notices rendered inline, not user messages).  |  
| `◇`  | An injected reference block, e.g. `◇ Reference 1/2 — <label>`.  |  
| `↳`  | The sticky prompt — echoes the user message the agent is currently working on.  |  
|  `☐` / `☑` / `•`  | Markdown task-list items (open / done) and plain list bullets.  |  
| `▶`  | Collapsed `<details>` summary inside rendered markdown.  |  
## Status-bar symbols[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#status-bar-symbols "Direct link to Status-bar symbols")
The single line at the bottom of the TUI. Segments appear only when relevant and drop off first on narrow terminals.  
| Symbol  | Meaning  |  
| --- | --- |  
|  `⠋⠙⠹…` (braille patterns)  | Busy spinner. Thinking and tool phases use different braille animation sets.  |  
| `☤ 🌀 🤔 ✨ 🍵 🔮`  | Frames of the `emoji` busy-indicator style (`/indicator emoji`). The default style rotates kaomoji faces instead.  |  
| `| / - \`  | Frames of the `ascii` busy-indicator style.  |  
| `⏱`  | Per-prompt elapsed time while the turn runs, e.g. `⏱ 12s/3m 45s` (turn time / session time).  |  
| `⏲`  | The same timer, frozen after the turn completes.  |  
| `cmp N`  | The session has been auto-compressed N times.  |  
| `▶ N`  | N `/bg` tasks currently running.  |  
| `⚠ YOLO`  | YOLO mode is on (auto-approval). Also shown in the startup banner.  |  
| `⛓ N`  | N subagents currently active.  |  
| `↩ resumes when subagent finishes`  | Reassurance shown while you are idle but delegated work is still in flight — the result returns on its own.  |  
| `● REC`  | Voice mode is recording.  |  
| `◉ STT`  | Voice recording stopped; speech-to-text is transcribing.  |  
| `◉ focus`  | Focus view is on (reduced output). Pinned so it never drops off a narrow terminal.  |  
| `♥`  | Affection flash — Hermes noticed you being nice to it.  |  
|  `⚡` / `🔋`  | Battery indicator (opt-in): plugged in / on battery, with percentage.  |  
| `N bg`  | N background terminal processes tracked in this session.  |  
| `N live sessions`  | Open TUI sessions in this process — click to open the session switcher.  |  
## Notices[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#notices "Direct link to Notices")
Short-lived status-bar notices carry their own leading glyph, set by severity:  
| Symbol  | Meaning  |  
| --- | --- |  
| `✓`  | Success notice.  |  
| `•`  | Informational notice.  |  
| `⚠`  | Warning (also used for credit warnings).  |  
| `✕`  | Error notice.  |  
## Approval and confirmation prompts[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#approval-and-confirmation-prompts "Direct link to Approval and confirmation prompts")  
| Symbol  | Meaning  |  
| --- | --- |  
| `⚠ approval required`  | A tool wants to run something that needs your explicit yes (bordered panel with the command preview).  |  
|  `⚠` / `?`  | Confirmation dialog title: dangerous action / ordinary question.  |  
| `🔐`  | Sudo password prompt (input is masked).  |  
| `🔑`  | Credential/secret input prompt (input is masked).  |  
## Subagents overlay (`/agents`)[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#subagents-overlay-agents "Direct link to subagents-overlay-agents")  
| Symbol  | Meaning  |  
| --- | --- |  
| `●`  | Subagent running.  |  
| `○`  | Queued.  |  
| `✓`  | Completed.  |  
| `■`  | Interrupted.  |  
| `✗`  | Failed.  |  
| `⌛`  | Timed out.  |  
| `⚠`  | Errored.  |  
| `⚡N`  | N currently-active agents in a rollup row.  |  
| `▁▂▃▄▅▆▇█`  | Activity sparkline — recent event volume per branch.  |  
## Session switcher (`Ctrl+X`)[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#session-switcher-ctrlx "Direct link to session-switcher-ctrlx")  
| Symbol  | Meaning  |  
| --- | --- |  
| `✓`  | Session idle.  |  
| `…`  | Starting.  |  
| `?`  | Waiting for input.  |  
| `▶`  | Working.  |  
| `✎ draft`  | The composer in that session holds an unsent draft.  |  
## Pickers and hubs[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#pickers-and-hubs "Direct link to Pickers and hubs")  
| Symbol  | Meaning  |  
| --- | --- |  
| `▸`  | Current selection row (model picker and friends).  |  
| `*`  | The currently-active model / provider.  |  
|  `●` / `○`  | Provider authenticated / not authenticated (model picker); plugin state fallback (plugins hub).  |  
|  `✓` / `✗`  | Plugin enabled / disabled (plugins hub).  |  
|  `↑ N more` / `↓ N more`  | More rows above/below the visible window of a list.  |  
| `┃`  | Scrollbar thumb on scrollable overlays.  |  
## Goals[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#goals "Direct link to Goals")
Goal lifecycle notices (from [goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)) lead with their state:  
| Symbol  | Meaning  |  
| --- | --- |  
| `✓`  | Goal complete.  |  
| `↻`  | Goal continuing — another iteration was scheduled.  |  
| `⏸`  | Goal paused.  |  
## See also[​](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#see-also "Direct link to See also")
  * [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui) — status line, details modes, busy-indicator styles
  * [Classic CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli) — shared keybindings and slash commands
  * [Skins & Themes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skins) — which glyphs and colors you can customize


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/reference/cli-symbols.md)
[Previous Optional Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog)[Next FAQ & Troubleshooting](https://hermes-agent.nousresearch.com/docs/reference/faq)
  * [Transcript symbols](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#transcript-symbols)
  * [Status-bar symbols](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#status-bar-symbols)
  * [Notices](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#notices)
  * [Approval and confirmation prompts](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#approval-and-confirmation-prompts)
  * [Subagents overlay (`/agents`)](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#subagents-overlay-agents)
  * [Session switcher (`Ctrl+X`)](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#session-switcher-ctrlx)
  * [Pickers and hubs](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#pickers-and-hubs)
  * [Goals](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#goals)
  * [See also](https://hermes-agent.nousresearch.com/docs/reference/cli-symbols#see-also)


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
