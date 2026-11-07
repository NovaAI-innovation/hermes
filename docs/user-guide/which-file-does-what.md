---
title: "Which File Does What?"
source: https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what
scraped_at: 2026-11-07T17:19:30.389206+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/which-file-does-what)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
    * [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui)
    * [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)
    * [Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode)
    * [Windows (Native)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)
    * [Windows (WSL2)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-wsl-quickstart)
    * [Switching to a Source Install](https://hermes-agent.nousresearch.com/docs/user-guide/switching-to-source)
    * [Hermes Agent Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
    * [Which File Does What?](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
    * [Remote Config](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
    * [Configuring Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)
    * [Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
    * [Session Storage Recovery](https://hermes-agent.nousresearch.com/docs/user-guide/session-storage-recovery)
    * [Profiles: Running Multiple Agents](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
    * [Profile Distributions: Share a Whole Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)
    * [Running Many Gateways at Once](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways)
    * [Connecting Desktop to Many Hermes Instances](https://hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop)
    * [Git Worktrees](https://hermes-agent.nousresearch.com/docs/user-guide/git-worktrees)
    * [Hermes Docker Setup](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
    * [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
    * [Checkpoints & Rollback](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Using Hermes
  * Which File Does What?


On this page
# Which File Does What?
"I told my agent something and it forgot." "Which file is my agent's brain?" "I edited SOUL.md — why doesn't it know my name?" These questions all come down to the same thing: Hermes Agent is shaped by several markdown files, and each one has a different job. This page maps them all in one place. For depth on any of them, follow the links to [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory), [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality), and [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files).
## The Master Table[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#the-master-table "Direct link to The Master Table")  
| File  | What it holds  | Who writes it  | When the agent sees it  | Where it lives  |  
| --- | --- | --- | --- | --- |  
| **SOUL.md**  | The agent's primary identity — personality, tone, communication style, what to avoid stylistically  | You. Hermes seeds a starter file automatically if one doesn't exist; existing files are never overwritten  | Slot #1 of the system prompt, at session start  |  `~/.hermes/SOUL.md` (or `$HERMES_HOME/SOUL.md` with a custom home) — never the working directory  |  
| **USER.md**  | User profile — your name, role, preferences, communication style, expectations  | The agent, via the `memory` tool (you can gate saves with `write_approval`, or edit entries via `hermes journey edit`)  | Injected into the system prompt as a frozen snapshot at session start  | `~/.hermes/memories/`  |  
| **MEMORY.md**  | Agent's personal notes — environment facts, project conventions, tool quirks, things learned  | The agent, via the `memory` tool (same gating and editing options as USER.md)  | Injected into the system prompt as a frozen snapshot at session start  | `~/.hermes/memories/`  |  
| **AGENTS.md**  | Project instructions, conventions, architecture — commands, ports, paths, repo-specific workflows  | You (or whoever authors the project)  | Loaded into the system prompt at startup from your working directory; nested copies are discovered progressively as the agent navigates subdirectories  | Project working directory + subdirectories  |  
|  **.hermes.md** / **HERMES.md**  | Project instructions, like AGENTS.md but Hermes-specific and highest priority  | You  | Loaded into the system prompt at startup (first match wins over AGENTS.md)  | Your project — discovery walks up to the git root  |  
Only **one** project context type is loaded per session, first match wins: `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. `SOUL.md` is always loaded independently as the agent identity — it is not part of that priority chain. See [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) for the full list, including `CLAUDE.md` and `.cursorrules` compatibility.
A useful shorthand:
  * **SOUL.md** is who the agent _is_ — if it should follow you everywhere, it belongs here.
  * **USER.md** is who _you_ are — the agent maintains it for you.
  * **MEMORY.md** is what the agent has _learned_ — it maintains this itself too.
  * **AGENTS.md** (or `.hermes.md`) is what the _project_ needs — if it belongs to a project, it belongs here.


## "Why did it forget what I just said?"[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#why-did-it-forget-what-i-just-said "Direct link to "Why did it forget what I just said?"")
Memory (MEMORY.md and USER.md) is injected into the system prompt as a **frozen snapshot** captured once at session start — when the agent saves something mid-session, the change is persisted to disk immediately but won't appear in the system prompt until the next session starts. This is intentional: it preserves the LLM's prefix cache for performance, and tool responses always show the live state, so nothing is lost — start a new session and the updated memory is there. Full details in [How Memory Appears in the System Prompt](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory#how-memory-appears-in-the-system-prompt).
## Common Mix-Ups[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#common-mix-ups "Direct link to Common Mix-Ups")
### "I put facts about myself in SOUL.md, but USER.md stayed empty"[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#i-put-facts-about-myself-in-soulmd-but-usermd-stayed-empty "Direct link to "I put facts about myself in SOUL.md, but USER.md stayed empty"")
`SOUL.md` and `USER.md` are separate systems that never feed each other. `SOUL.md` is a personality file **you** edit directly — it shapes tone and identity, and its content is injected verbatim as slot #1 of the prompt. `USER.md` is part of persistent memory and is written by **the agent** through the `memory` tool. If you want facts about yourself in USER.md, tell the agent ("remember that I prefer concise answers") and it saves them — editing SOUL.md won't populate memory, and memory entries won't change the persona. Use SOUL.md for durable voice and personality guidance; leave preferences and profile facts to memory. See [What should go in SOUL.md?](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality#what-should-go-in-soulmd) and [Two Targets Explained](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory#two-targets-explained).
### "I told it my name mid-session and it acted like it never heard it"[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#i-told-it-my-name-mid-session-and-it-acted-like-it-never-heard-it "Direct link to "I told it my name mid-session and it acted like it never heard it"")
If the agent saved your name to memory, the save worked — check with the `memory` tool's responses or `hermes journey list`. What you're seeing is the frozen-snapshot rule above: the system prompt doesn't refresh mid-session, so the _injected_ memory block still shows the session-start state. The agent can still use what you told it within the current conversation (it's in the context), and the saved entry will be in the system prompt from the next session onward. The same applies to edits you make to `SOUL.md` or `AGENTS.md` while a session is running: context is assembled at session start, so restart the session to pick up changes. For long-running gateway conversations you do not want to reset, `hermes sessions refresh-prompts` makes them adopt the updated files on their next turn while keeping the history (see [Refresh Prompts After a Profile Update](https://hermes-agent.nousresearch.com/docs/user-guide/sessions#refresh-prompts-after-a-profile-update)).
  * Want to change how the agent **talks**? Edit `~/.hermes/SOUL.md` — [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality).
  * Want the agent to **remember a fact**? Just tell it — it saves to memory itself. [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory).
  * Want to set **project rules**? Put an `AGENTS.md` (or `.hermes.md`) in the project — [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files).
  * Need a **temporary** personality change? Use `/personality` — it's a session-level overlay, no file edits needed.


## Related Docs[​](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#related-docs "Direct link to Related Docs")
  * [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) — MEMORY.md, USER.md, the `memory` tool, capacity limits, `write_approval`
  * [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality) — SOUL.md content guidance, `/personality` presets, the prompt stack
  * [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) — AGENTS.md, `.hermes.md`, progressive discovery, security scanning


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/which-file-does-what.md)
[Previous Hermes Agent Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)[Next Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
  * [The Master Table](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#the-master-table)
  * ["Why did it forget what I just said?"](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#why-did-it-forget-what-i-just-said)
  * [Common Mix-Ups](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#common-mix-ups)
    * ["I put facts about myself in SOUL.md, but USER.md stayed empty"](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#i-put-facts-about-myself-in-soulmd-but-usermd-stayed-empty)
    * ["I told it my name mid-session and it acted like it never heard it"](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#i-told-it-my-name-mid-session-and-it-acted-like-it-never-heard-it)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what#related-docs)


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
