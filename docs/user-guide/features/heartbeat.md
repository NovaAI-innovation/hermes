---
title: "Session Heartbeats"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat
scraped_at: 2026-11-07T17:19:38.838570+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/heartbeat)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
      * [Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
      * [Automation Blueprints Catalog](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
      * [Subagent Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)
      * [Kanban (Multi-Agent Board)](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
      * [Codex App-Server Runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime)
      * [Kanban tutorial](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial)
      * [Kanban worker lanes](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-worker-lanes)
      * [Kanban Multi-Gateway Deployment](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
      * [Persistent Goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)
      * [Session Heartbeats](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat)
      * [Recurring Loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
      * [Code Execution](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
      * [Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)
      * [Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
    * [Skills](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Automation
  * Session Heartbeats


On this page
# Session Heartbeats (`/heartbeat`)
`/heartbeat` gives the **current session** one recurring instruction. Whenever the session is idle and the interval has elapsed, the prompt fires as a normal user turn — same conversation, same context, same prompt cache.

```


/heartbeat every 10m Check the deployment and report meaningful changes  



```

Inspired by Prime-Agent's `/heartbeat`. The Hermes adaptation keeps the strict message-flow invariants: the heartbeat is injected only between turns (never mid-run), as a plain user-role message.
## Heartbeat vs cron: which one do I want?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#heartbeat-vs-cron-which-one-do-i-want "Direct link to Heartbeat vs cron: which one do I want?")
They look similar but serve different jobs:  
|   | `/heartbeat`  | [`hermes cron`](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)  |  
| --- | --- | --- |  
| Runs in  |  **This conversation** — full context, memory of the discussion  | A fresh isolated session per tick  |  
| Survives process restart  | State survives (SessionDB); gateway watches resume automatically after restart  | Yes — fully durable scheduler  |  
| How many  | One per session  | Unlimited jobs  |  
| Best for  | "Keep an eye on X _in this thread_ while we work"  | Standing jobs, reports, watchdogs, deliveries  |  
Rule of thumb: if the recurring prompt needs the conversation's context, use `/heartbeat`. If it's a self-contained job, use cron.
## Commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#commands "Direct link to Commands")  
| Command  | What it does  |  
| --- | --- |  
| `/heartbeat every <interval> <prompt>`  | Set (or replace) the session's heartbeat. Intervals: `90s`, `10m`, `2h`, `1d` (minimum 60s).  |  
|  `/heartbeat` or `/heartbeat status`  | Show the heartbeat, its interval, and time to next fire.  |  
| `/heartbeat pause`  | Stop firing without clearing.  |  
| `/heartbeat resume`  | Resume (re-anchors the timer — no instant stale fire).  |  
| `/heartbeat clear`  | Remove the heartbeat.  |  
`/hb` is an alias. Works on the CLI, the TUI / Desktop app, and gateway platforms (on Slack, use `/hermes heartbeat …`).
## Behavior details[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#behavior-details "Direct link to Behavior details")
  * **Idle-only.** A heartbeat never interrupts a running turn. If the agent is busy when the tick comes due, it fires at the next idle poll. In the gateway, an idle watched session wakes proactively; no new inbound message is needed.
  * **Missed ticks coalesce.** If the session was busy (or the process wasn't running) through several intervals, you get **one** heartbeat turn, not a backlog. The timer re-anchors on every fire.
  * **User messages win.** A queued user message always takes priority; the heartbeat waits for the input queue to drain.
  * **Owned by the surface that set it.** A heartbeat set from a messaging chat fires from the gateway and replies into that chat even while the same session is open in the TUI / Desktop app; the viewer never claims the tick.
  * **Cache-safe.** The injected prompt is an ordinary user message. No system-prompt mutation, no toolset change.
  * **Gateway recovery.** Startup restores active heartbeats using the current persisted conversation and thread routing, in the owning profile. Each poll retries recovery after temporary storage failures or adapter downtime; paused and cleared heartbeats and suspended conversations do not restart. No new chat message is required.
  * **Persistence and conversation boundaries.** State lives in `SessionDB.state_meta` keyed by `heartbeat:<session_id>` and follows context-compression session rotations. In the messaging gateway, leaving a conversation through reset, switch, or suspension clears its heartbeat; resuming that archived conversation does not resurrect it. Firing requires the owning process (CLI session or gateway) to be running. An already-admitted gateway tick is checked again after session resolution and before agent execution: it may follow a compression child, but cannot carry its old instruction into a reset or switched conversation.
  * **Execution accounting.** The gateway reserves a due tick at adapter admission. If that exact attempt ends before entering the agent runner (including cancellation or a routing, authorization, emergency-stop, or preparation rejection), it refunds the tick unless the schedule has since changed. Once the agent runner is entered, the fire remains counted even if execution fails or is interrupted. This count is **not** proof of a successful model response or outbound delivery; abrupt process death can prevent the refund callback.
  * **Quiet when there is nothing to say (gateway).** A scheduled heartbeat turn may end with a bare silence marker (`NO_REPLY` / `[SILENT]`): the gateway sends nothing, unlike a human message that returns only a marker (that still gets the visible "try again" notice). While the heartbeat works, no typing indicator, tool-progress, streamed draft or "still working" bubble is posted, and a result it does deliver is routed to the chat/topic without quoting the message that set the heartbeat. Approval prompts and failures stay visible.
  * **Don't-invent-work guard.** The injected prompt tells the agent to reply briefly and stop when nothing meaningful changed, so an idle heartbeat doesn't generate busywork.


## Example[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#example "Direct link to Example")

```


You: /heartbeat every 15m Check whether the CI run for PR #1234 finished; summarize the result when it does  





  





  ♥ Heartbeat set (every 15m): Check whether the CI run for PR #1234 finished; ...  





  





[15 minutes of you working on other things in the same session]  





  





Hermes: [Heartbeat — recurring instruction, fires every 15m]  





  💻 gh pr checks 1234   (1.2s)  





  CI is still running (14/37 checks complete). Nothing to report yet.  



```

When the answer stops changing, `/heartbeat clear` it — or let it keep watch.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/heartbeat.md)
[Previous Persistent Goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)[Next Recurring Loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Heartbeat vs cron: which one do I want?](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#heartbeat-vs-cron-which-one-do-i-want)
  * [Commands](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#commands)
  * [Behavior details](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#behavior-details)
  * [Example](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat#example)


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
