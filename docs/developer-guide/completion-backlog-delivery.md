---
title: "Background completion backlogs"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery
scraped_at: 2026-11-07T17:20:20.160726+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/completion-backlog-delivery)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
      * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
      * [Codebase Ownership Map](https://hermes-agent.nousresearch.com/docs/developer-guide/codebase-ownership)
      * [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
      * [Prompt Assembly](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)
      * [Context Compression and Caching](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)
      * [Micro-compaction](https://hermes-agent.nousresearch.com/docs/developer-guide/micro-compaction)
      * [Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals)
      * [Gateway Session Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-session-lifecycle)
      * [Gateway local sessions](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-local-sessions)
      * [Classic gateway client](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
      * [Gateway command parity](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-command-parity)
      * [Multiplexing Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/multiplexing-gateway)
      * [Completion backlogs](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
      * [Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)
      * [State DB Recovery](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery)
      * [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
      * [Config Backend Seam](https://hermes-agent.nousresearch.com/docs/developer-guide/config-backend)
      * [Programmatic Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Architecture
  * Completion backlogs


On this page
# Background completion backlogs
Interactive surfaces coalesce consecutive background-process completions that are already ready for one conversation into a single notification turn. This does not add a delay or promise to combine jobs that finish at different times. Failures and successful outputs remain in the batch; one completion keeps its original text.
Process identity remains available until dispatch. Explicit `process_manage` wait/log/kill consumption can therefore suppress a CLI completion even after it has left the process registry and entered the input queue. An entirely consumed batch starts no turn. Watching output and async-delegation results remain separate notifications, in their original order; they are not folded into completion batches.
## Consumers and ownership[​](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery#consumers-and-ownership "Direct link to Consumers and ownership")
  * **Classic CLI:** `hermes_cli/cli_process_notifications.py` owns the idle/post-turn drain, compression-aware ownership and final input unwrapping.
  * **TUI and Desktop:** `tui_gateway/session_notifications.py` groups the poller's ready snapshot after checking ownership. Each process still emits its own UI status. Busy sessions requeue structured events, not rendered batch strings.
  * **Post-turn TUI safety net:** `tui_gateway/prompt_turn.py` uses the same routing and rendering path. Desktop and dashboard chat clients share this backend.
  * **Messaging gateway:** `gateway/run_notifications.py` already uses its own route-keyed short-window batching. This interactive-backlog change does not replace that mechanism or alter adapter sends.
  * **Noninteractive/headless consumers:** this change does not create a new autonomous notification loop for an API request, ACP client, or one-shot CLI.


The shared renderer is `tools/process_registry_notifications.py::ProcessNotificationBatch`. Neither a batch nor its delivery status is persisted into the system prompt. Addressed events still require a provable owner; another live session cannot adopt them. Delegation delivery continues through its existing durable claim/complete ledger, once per delegation rather than once per process batch.
## Local validation and its limits[​](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery#local-validation-and-its-limits "Direct link to Local validation and its limits")
`evals/completion_backlog_probe.py REPO OUTPUT.json` starts real local shell children in temporary directories, reads their real completion events, and drives the production CLI, TUI poller and post-turn notification routes. A loopback HTTP turn sink replaces `chat` / `_run_prompt_submit`; it records actual dispatches but does **not** exercise model inference, native renderer interaction or a hosted platform. Synthetic watch and delegation envelopes are labeled fixtures; delegation claims use the real temporary SQLite ledger. The backlog case includes a nonzero exit.
The probe checks a ready backlog, a single exact payload, explicitly consumed results, foreign ownership, and watches/delegations interleaved with completions. It measures turn admission at the notification boundary, not model token savings.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/completion-backlog-delivery.md)
[Previous Multiplexing Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/multiplexing-gateway)[Next Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)
  * [Consumers and ownership](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery#consumers-and-ownership)
  * [Local validation and its limits](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery#local-validation-and-its-limits)


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
