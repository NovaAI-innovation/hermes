---
title: "Kanban Multi-Gateway Deployment"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway
scraped_at: 2026-11-07T17:19:38.839572+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/kanban-multi-gateway)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
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
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Automation
  * Kanban Multi-Gateway Deployment


On this page
# Multi-gateway deployment
Hermes supports multiple gateway processes running concurrently — one per profile (default, writer, admin, coder, researcher). Each gateway opens its own connection to platform APIs and delivers messages for its profile's subscribers.
Task subscriptions also cover review feedback. A `changes_requested` review event is delivered as an actionable review-BLOCK notification. Subscriptions using `notify+wake` additionally wake the exact originating chat/thread/session so the controller inspects the existing card and current run; `notify` remains passive-only and `wake` remains wake-only. Review feedback never creates, unblocks, requeues, or otherwise mutates a task.
## Single-dispatcher posture[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#single-dispatcher-posture "Direct link to Single-dispatcher posture")
Only one gateway owns the kanban dispatcher. The owning gateway keeps `kanban.dispatch_in_gateway: true` (the default); every other gateway sets it to `false`.
**Why this matters:** dispatching is single-owner so multiple gateways do not race to spawn the same work. Notification delivery is profile-owned instead: each gateway polls only subscriptions for profiles whose platform adapters it hosts. The atomic event claim prevents duplicate delivery across watcher processes.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#configuration "Direct link to Configuration")
On the dispatch-owning gateway (typically the `default` profile), no change is needed. On every other profile gateway, add to `~/.hermes/config.yaml`:

```


kanban:  





  dispatch_in_gateway: false  



```

Or set the env var: `HERMES_KANBAN_DISPATCH_IN_GATEWAY=false`
## What each gateway does[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#what-each-gateway-does "Direct link to What each gateway does")  
| Gateway role  | dispatch_in_gateway  | Opens subscribed board DBs?  | Dispatcher  | Notifier  |  
| --- | --- | --- | --- | --- |  
| default (confirmed dispatch-lock owner)  | true (default)  | yes  | yes  | owned profiles + legacy unstamped subscriptions  |  
| writer, admin, coder, etc.  | false  | yes, when the profile has subscriptions  | no  | that gateway's owned profiles  |  
Non-dispatch gateways still deliver messages for their own platform adapters (Telegram, Discord, etc.). They do not dispatch tasks, and they skip boards that have no subscriptions owned by their profiles.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/kanban-multi-gateway.md)
[Previous Kanban worker lanes](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-worker-lanes)[Next Persistent Goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)
  * [Single-dispatcher posture](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#single-dispatcher-posture)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#configuration)
  * [What each gateway does](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway#what-each-gateway-does)


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
