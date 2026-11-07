---
title: "Troubleshooting: \'My Agent Feels Dumber\'"
source: https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality
scraped_at: 2026-11-07T17:20:11.931739+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/troubleshooting-agent-quality)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
    * [Run Nemotron 3 Ultra free in Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
    * [Run Hermes Agent with Nous Portal](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
    * [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)
    * [Running Hermes on a Personal or Work Machine](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine)
    * [Run Local LLMs on Mac](https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac)
    * [Tutorial: Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
    * [Tutorial: Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)
    * [Using Hermes as a Python Library](https://hermes-agent.nousresearch.com/docs/guides/python-library)
    * [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
    * [Manage Hermes Cloud with MCP](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
    * [Use SOUL.md with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes)
    * [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)
    * [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)
    * [Script-Only Cron Jobs (No LLM)](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
    * [Automation Blueprints](https://hermes-agent.nousresearch.com/docs/guides/automation-blueprints)
    * [Cron Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting)
    * [Troubleshooting: "My Agent Feels Dumber"](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
    * [Working with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
    * [Delegation & Parallel Work](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns)
    * [Give Your Agent Its Own Email Address](https://hermes-agent.nousresearch.com/docs/guides/agent-email-address)
    * [Tutorial: GitHub PR Review Agent](https://hermes-agent.nousresearch.com/docs/guides/github-pr-review-agent)
    * [GitHub PR Reviews via Webhook](https://hermes-agent.nousresearch.com/docs/guides/webhook-github-pr-review)
    * [Migrate from OpenClaw](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)
    * [AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
    * [Google Vertex AI](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
    * [Microsoft Foundry](https://hermes-agent.nousresearch.com/docs/guides/azure-foundry)
    * [xAI Grok OAuth (SuperGrok / X Premium+)](https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth)
    * [OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)
    * [Register a Microsoft Graph Application](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
    * [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Troubleshooting: "My Agent Feels Dumber"


On this page
# Troubleshooting: "My Agent Feels Dumber"
Sometimes Hermes seems less sharp than it was yesterday, or forgets something you told it twenty minutes ago. This is almost never mysterious — there's usually one specific, checkable cause. Work through this checklist in order: the steps are sorted by how often each one turns out to be the answer.
## 1. Check which model the session is actually using[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#1-check-which-model-the-session-is-actually-using "Direct link to 1. Check which model the session is actually using")
**Symptom:** Answers are shallower, code quality dropped, reasoning feels off — across the board.
**Check:** Run `/model` with no arguments to show the current model, or `/status` to see the session's model, provider, and profile in one view.
**What it means:** A model switch is a capability change, and it's easy to end up on a different model than you think:
  * A plain `/model <name>` switch is **session-only** by default (unless `model.persist_switch_by_default: true` is set), so the model you're on may not match what's in `config.yaml`.
  * Changing the main model from the dashboard's Models page applies to **new sessions only** — an already-open chat keeps running whatever model it started with.
  * If you switched to a faster model for a simple task (a pattern [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips#choose-the-right-model) recommends), remember to switch back for complex reasoning work.


If the model is wrong, `/model <name>` fixes it for this session; add `--global` to persist the change to `config.yaml`. Note that a mid-session switch resets the prompt cache, so the next turn re-reads the conversation at full input price — on a long session it can be cheaper to start fresh on the right model.
## 2. Check context usage[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#2-check-context-usage "Direct link to 2. Check context usage")
**Symptom:** The session started strong but responses are slowing down, getting truncated, or losing track of earlier details.
**Check:** Run `/usage` to see token usage and context window state, or `/context` for a visual breakdown of what's occupying the window (system prompt, tool definitions, skills, memory, conversation) versus free space.
**What it means:** Extended conversations accumulate messages and tool outputs, approaching context limits. When you notice degradation in a long session:

```


# Compress the conversation (summarizes history, preserves key context)  





/compress  





  





# Or start a fresh session  





/new  



```

`/compress` summarizes the conversation history, dramatically reducing token count while preserving key context. `/compress here [N]` keeps the most recent N exchanges verbatim and summarizes the rest, and a focus topic (`/compress focus <topic>`) narrows what a full summary preserves.
Use `/compress` regularly during long sessions rather than waiting for problems, and `/usage` periodically to see where you stand.
## 3. Verify the detected context length[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#3-verify-the-detected-context-length "Direct link to 3. Verify the detected context length")
**Symptom:** Context problems appear surprisingly early — the first long conversation already hits limits, or compression fires far sooner than the model's advertised window should allow.
**Check:** Look at the CLI startup line — it shows the detected context length (e.g., `📊 Context limit: 128000 tokens`). You can also check with `/usage` during a session.
**What it means:** Hermes may have auto-detected the wrong context length for your model. Set it explicitly:

```


# In ~/.hermes/config.yaml  





model:  





  default: your-model-name  





  context_length: 131072  # your model's actual context window  



```

Or for custom endpoints, per-model on the provider entry:

```


providers:  





  my-server:  





    api: "http://localhost:11434/v1"  





    models:  





      qwen3.5:27b:  





        context_length: 64000  



```

Ollama users: if you set a custom `num_ctx`, set the matching context length in Hermes — Ollama's `/api/show` reports the model's _maximum_ context, not the effective `num_ctx` you configured. On a running gateway, edits to `model.context_length` or any `compression.*` key take effect on the next message — no restart needed.
See [Context Length Detection](https://hermes-agent.nousresearch.com/docs/integrations/providers#context-length-detection) for how auto-detection works and all override options.
## 4. "I told it something and it forgot" — the frozen memory snapshot[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#4-i-told-it-something-and-it-forgot--the-frozen-memory-snapshot "Direct link to 4. "I told it something and it forgot" — the frozen memory snapshot")
**Symptom:** You asked Hermes to remember something during this session, it confirmed the save, but later in the _same_ session it doesn't seem to know it.
**Check:** Nothing is broken — check the timing. Memory saved mid-session is written to disk immediately, but the system prompt won't reflect it until the next session.
**What it means:** This is documented, intentional behavior. Memory is injected into the system prompt as a **frozen snapshot at session start** , and that injection never changes mid-session — it preserves the LLM's prefix cache for performance. When the agent adds or removes memory entries during a session, the changes persist to disk right away but appear in the system prompt only when the next session starts. Tool responses always show the live state, so the save itself is confirmed and real.
Frozen snapshot in practice: "remember X" during a session means X is guaranteed available **next** session. Within the current session, the fact still exists in the conversation history itself — the agent forgets it only if that part of the conversation has since been compressed away (see step 7).
See [Persistent Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory#how-memory-appears-in-the-system-prompt) for the full mechanics.
## 5. Memory is bounded and curated — not a transcript[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#5-memory-is-bounded-and-curated--not-a-transcript "Direct link to 5. Memory is bounded and curated — not a transcript")
**Symptom:** Hermes doesn't recall a detail from a session last week, even though you discussed it at length.
**Check:** Memory capacity and contents. The system prompt memory header shows usage (e.g., `[67% — 1,474/2,200 chars]`), and `hermes journey list` shows every saved memory entry and skill.
**What it means:** Persistent memory is intentionally bounded — 2,200 chars (~800 tokens) for MEMORY.md and 1,375 chars (~500 tokens) for USER.md. It holds curated key facts, not conversation transcripts. Things worth saving are preferences, environment facts, conventions, and corrections; raw discussion detail is not stored there by design.
For "did we discuss X last week?" recall, the agent has a separate mechanism: `session_search` queries all past sessions (stored in SQLite with full-text search) and can find things discussed weeks ago even when they're not in active memory. Just ask — "search our past sessions for the deploy discussion."
You can also help directly: say "remember this for next time" after a productive session, or "clean up your memory" when it's near capacity so the agent consolidates entries. See [Memory & Skills tips](https://hermes-agent.nousresearch.com/docs/guides/tips#memory--skills) and [Capacity Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory#capacity-management).
## 6. Check that skills and tools are loaded[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#6-check-that-skills-and-tools-are-loaded "Direct link to 6. Check that skills and tools are loaded")
**Symptom:** Hermes used to handle a specific workflow expertly and now approaches it naively, or says it can't do something it did before.
**Check:**
  * `/skills` — browse installed skills (a skill the agent relied on may have been removed).
  * `/reload-skills` — re-scan `~/.hermes/skills/` for newly installed or removed skills.
  * `/tools list` — see available tools; a tool disabled earlier with `/tools disable` stays out of the agent's toolset for the session.
  * `/context all` — per-skill and per-toolset cost listing, which doubles as an inventory of what's actually loaded.


**What it means:** Skills are the agent's procedural knowledge — multi-step workflows and tool-specific instructions. If a skill is missing or a toolset was trimmed (e.g., a session started with `hermes chat -t "terminal"` to reduce prompt weight), the agent genuinely has less to work with in that session. Re-enable tools with `/tools enable`, or invoke the skill explicitly by name (`/github-pr-workflow`) to confirm it loads.
## 7. Compression side-effects[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#7-compression-side-effects "Direct link to 7. Compression side-effects")
**Symptom:** After a long session (or right after running `/compress`), Hermes remembers the broad strokes but has lost fine detail from earlier in the conversation.
**Check:** Whether compression has fired — `/usage` and `/context` show compression stats and context state on messaging platforms, and manual `/compress` always reports its result.
**What it means:** Compression replaces older conversation history with a summary — that's the point, and it necessarily trades detail for headroom. Know the shape of it:
  * Recent messages are protected: by default the last 20 messages stay uncompressed (`protect_last_n`) and the opening exchange is pinned (`protect_first_n: 3`) so the original goal stays visible.
  * Compaction is non-destructive: with the default `compression.in_place: true`, the session keeps one durable id and pre-compaction turns are soft-archived — still searchable via `session_search` and recoverable, not deleted.
  * With `in_place: false` (legacy behavior), each compaction rotates to a **new session linked to the old one** — a titled session becomes `"my project" → "my project #2" → "my project #3"`. If you resume by title, `hermes -c "my project"` automatically picks the most recent variant.
  * A focus topic narrows what a full summary preserves: `/compress focus auth-refactor` keeps that thread's detail at the expense of the rest.


If a compressed-away detail matters, ask the agent to search for it (`session_search` reaches the archived turns), or re-paste the key facts into the conversation.
See [Context Compression](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#context-compression) for the full settings reference and [Auto-Lineage on Compression](https://hermes-agent.nousresearch.com/docs/user-guide/sessions#auto-lineage-on-compression) for how titled sessions chain.
* * *
## Quick reference[​](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#quick-reference "Direct link to Quick reference")  
| Symptom  | First command  | Likely cause  |  
| --- | --- | --- |  
| Everything feels less capable  | `/model`  | Session is on a different model than you think  |  
| Long session degrading  | `/usage`  | Context pressure — compress or start fresh  |  
| Limits hit surprisingly early  | CLI startup line / `/usage`  | Wrong auto-detected context length  |  
| Forgot what I said this session  | — (by design)  | Frozen memory snapshot — appears next session  |  
| Forgot last week's discussion  | ask it to `session_search`  | Memory is bounded, curated facts only  |  
| Lost a specific ability  |  `/skills`, `/tools list`  | Skill or toolset not loaded this session  |  
| Lost old detail after long session  |  `/usage`, `/context`  | Compression summarized older history  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/troubleshooting-agent-quality.md)
[Previous Cron Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting)[Next Working with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [1. Check which model the session is actually using](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#1-check-which-model-the-session-is-actually-using)
  * [2. Check context usage](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#2-check-context-usage)
  * [3. Verify the detected context length](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#3-verify-the-detected-context-length)
  * [4. "I told it something and it forgot" — the frozen memory snapshot](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#4-i-told-it-something-and-it-forgot--the-frozen-memory-snapshot)
  * [5. Memory is bounded and curated — not a transcript](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#5-memory-is-bounded-and-curated--not-a-transcript)
  * [6. Check that skills and tools are loaded](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#6-check-that-skills-and-tools-are-loaded)
  * [7. Compression side-effects](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#7-compression-side-effects)
  * [Quick reference](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality#quick-reference)


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
