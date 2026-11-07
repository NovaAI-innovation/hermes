---
title: "Recurring Loops"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/loops
scraped_at: 2026-11-07T17:19:38.842410+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/loops)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
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
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Automation
  * Recurring Loops


On this page
# Recurring Loops (`/loop`)
`/loop` re-runs a prompt (or a slash command) on a recurring cadence **inside your current session**. Each wakeup is a real agent turn: Hermes reads the current state fresh — the latest CI result, the newest queue depth, the file as it is now — does the work, reports back, and goes quiet until the next tick.
It's Hermes' take on **Claude Code's`/loop`** (and its `/proactive` alias, which works here too). Where [`/goal`](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) is judge-driven — "keep working until this objective is achieved" — `/loop` is timer-driven: "do this again every N minutes (or whenever it makes sense) until something says stop."
## When to use it[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#when-to-use-it "Direct link to When to use it")
  * **Polling external state.** "Watch the deploy / the CI run / the queue and tell me when it changes." The canonical use case.
  * **Iterate-until-green.** "Run the tests, fix what fails, repeat until they pass."
  * **Monitoring during a work session.** Keep an eye on error rates or a long job's progress while you do something else in the same conversation.
  * **Periodic housekeeping.** Re-run a lint pass or a status summary every N minutes during a long session.


When the work should run **unattended** — overnight, on a real schedule, surviving restarts of your terminal — use a [cron job](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) instead. `/loop` lives inside a session; cron lives outside all of them. And when the task is a single objective with a definition of done, [`/goal`](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals) is usually the better fit.
## Quick start[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#quick-start "Direct link to Quick start")

```


/loop 5m check the deploy status and tell me if it's live yet  



```

What you'll see:
  1. **Loop accepted** — `↻ Loop set (every 5m): check the deploy status…`
  2. **First wakeup fires right away** — on the next idle poll (gateway: the next 15s watcher scan), Hermes injects the wakeup and runs a normal turn against current state.
  3. **Repeat** — every 5 minutes after that, until a stop condition fires or you stop it.


While a loop stands, every surface keeps it in view with a live countdown to the next wakeup:  
| Surface  | Where  |  
| --- | --- |  
| Classic CLI  | A row in the live-work dock above the prompt: `↻ loop · every 5m · 2 runs · next in 4m · <prompt>` (minute steps, seconds in the last minute; `running now` during a wakeup; the pause reason when paused). Collapsed with Ctrl+R it shrinks to `↻ loop next in 4m`.  |  
| TUI  | The same row under the goal bar.  |  
| Desktop  | The loop card above the composer: `Loop active · 2 runs · next 00:04:12`, counting every second.  |  
Loop a slash command just as easily:

```


/loop 10m /recap  



```

## The two cadence modes[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#the-two-cadence-modes "Direct link to The two cadence modes")
**Fixed interval — you set the clock.** Give an interval (`30s`, `5m`, `2h`, `1h30m`) and the loop fires on that schedule. Use it when the thing you're watching changes on its own timeline:

```


/loop 2m poll the build at ci.example.com/job/42 and ping me the moment it finishes  



```

**Self-paced — Hermes sets the clock.** Omit the interval and the loop paces itself: it starts at the floor (1 minute by default), and while the agent's replies stop changing it backs off exponentially — 2m, 4m, 8m, up to the ceiling (15 minutes by default). The moment a reply differs from the last one, cadence snaps back to the floor. Change detection is a local digest comparison (timestamps are ignored), so idle waits cost nothing extra:

```


/loop keep an eye on the migration and summarize progress  



```

The rule of thumb: **fixed interval when an external clock drives the work; self-paced when the work drives the rhythm.**
## Stop conditions[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#stop-conditions "Direct link to Stop conditions")
A loop ends when any of these fires:  
| Condition  | How  |  
| --- | --- |  
| The agent decides it's done  | The wakeup prompt teaches the agent to end its reply with `LOOP_COMPLETE` on its own line when the task is finished or moot.  |  
| A run cap  |  `--times N` — stop after N wakeups.  |  
| An evidence-based condition  |  `--until <condition>` — after each wakeup, the same auxiliary judge that powers `/goal` checks the reply against your condition. If the judge rules the condition unachievable, the loop **pauses** with the reason instead of re-firing until the tick budget (fail-open: a broken judge never wedges the loop).  |  
| You  |  `/loop stop` (or `/loop pause` to keep it around).  |  
| The backstop budget  |  `loops.max_ticks` (default 100) pauses the loop so an unattended session can't burn tokens forever. `0` = unlimited.  |  
Examples:

```


/loop 2m poll CI --times 30  





/loop 5m watch the queue --until queue depth reaches zero  



```

## Commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#commands "Direct link to Commands")  
| Command  | What it does  |  
| --- | --- |  
| `/loop [interval] <prompt> [--times N] [--until <cond>]`  | Start (or replace) the loop for this session. The first wakeup fires immediately; later ones follow the cadence.  |  
|  `/loop` or `/loop status`  | Show cadence, ticks fired, and time to the next wakeup.  |  
| `/loop pause`  | Stop firing without losing the loop.  |  
| `/loop resume`  | Pick it back up.  |  
| `/loop stop`  | End the loop.  |  
| `/proactive …`  | Alias for `/loop` (Claude Code parity).  |  
Works on the CLI, the TUI (`hermes --tui`), the web dashboard chat, the desktop app, and every gateway platform (Telegram, Discord, Slack, WhatsApp, …). On messaging platforms the gateway fires wakeups even between your messages — the loop belongs to the chat's session, and its results arrive as ordinary replies — also when that session is open in the TUI / Desktop app, which leaves the routed wakeup to the gateway.
In the desktop app and dashboard chat, the backend keeps firing an active loop after you close the window or the app disconnects: a session with an active `/loop` (or `/heartbeat`) is exempt from the disconnected-session reaper, so the wakeups and their results are waiting when you reopen it. The exemption ends when the loop stops, pauses, or reaches its tick budget, and the session is then collected normally. The backend process itself must keep running: if it exits with the app, nothing fires until it is back. For unattended loops, run the session on a long-lived backend (a remote `hermes serve`, or the dashboard).
## Mixing with `/goal`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#mixing-with-goal "Direct link to mixing-with-goal")
Both features inject synthetic turns at idle boundaries, so they follow one rule: **an active goal owns the session.** While a `/goal` is actively driving (judge saying "continue"), loop wakeups defer. The loop resumes using idle time as soon as the goal finishes, pauses, or parks itself on a wait barrier (`/goal wait`, or the judge's automatic WAIT verdict). A parked goal plus a `/loop` is a natural combo: the goal waits on the big async thing while the loop keeps a heartbeat on something else.
A real user message always wins over both — wakeups only fire while the session is idle and nothing of yours is queued.
## Behavior details[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#behavior-details "Direct link to Behavior details")
  * **A wakeup is a normal user-role turn.** No system-prompt mutation, no toolset swap — prompt caching stays intact. In the messaging gateway a wakeup is not a reply to the message that set the loop, so its output is posted to the chat/topic without quoting that message.
  * **Survives`/resume` and compression.** Loop state persists per session and migrates across context-compression boundaries, same as `/goal`.
  * **One loop per session.** Setting a new `/loop` replaces the old one. Run several loops by running several sessions (or use cron for a fleet of schedules).
  * **Interrupting a wakeup turn (Ctrl+C) pauses the loop** — recoverable with `/loop resume`, so cancel actually means cancel.
  * **Token cost scales with cadence.** Every tick is a full agent turn. Match the interval to how often the state actually changes; prefer self-pacing for idle waits.


## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#configuration "Direct link to Configuration")

```


# ~/.hermes/config.yaml  





loops:  





  min_interval_seconds: 30       # floor for fixed intervals  





  max_ticks: 100                 # backstop budget (0 = unlimited)  





  self_paced_floor_seconds: 60   # self-paced starting cadence  





  self_paced_ceiling_seconds: 900  # self-paced max backoff  



```

The `--until` judge routes through the `goal_judge` auxiliary task, so `auxiliary.goal_judge.*` routing overrides (provider, model) apply to loop conditions too.
##  `/loop` vs `/goal` vs cron[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#loop-vs-goal-vs-cron "Direct link to loop-vs-goal-vs-cron")  
|   | `/loop`  | `/goal`  | cron  |  
| --- | --- | --- | --- |  
| **Trigger**  | Timer (or self-paced)  | Judge verdict after each turn  | Schedule, outside any session  |  
| **Lives in**  | Your current session  | Your current session  | Its own session per run  |  
| **Ends when**  | Stop condition / caps / you  | Goal achieved / budget / you  | You remove the job  |  
| **Best for**  | Polling, monitoring, periodic re-runs  | One objective, iterate until done  | Unattended, long-horizon schedules  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/loops.md)
[Previous Session Heartbeats](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat)[Next Code Execution](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [When to use it](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#when-to-use-it)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#quick-start)
  * [The two cadence modes](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#the-two-cadence-modes)
  * [Stop conditions](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#stop-conditions)
  * [Commands](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#commands)
  * [Mixing with `/goal`](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#mixing-with-goal)
  * [Behavior details](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#behavior-details)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#configuration)
  * [`/loop` vs `/goal` vs cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops#loop-vs-goal-vs-cron)


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
