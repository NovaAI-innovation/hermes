---
title: "Public Subagent Lifecycle API"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api
scraped_at: 2026-11-07T17:20:37.798679+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/subagent-lifecycle-api)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
      * [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
      * [Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)
      * [Adding a Platform Adapter](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-platform-adapters)
      * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
        * [Plugin LLM Access](https://hermes-agent.nousresearch.com/docs/developer-guide/plugin-llm-access)
        * [Observer Hooks](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
        * [Middleware](https://hermes-agent.nousresearch.com/docs/developer-guide/middleware)
        * [Subagent lifecycle API](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
        * [Desktop Plugin SDK](https://hermes-agent.nousresearch.com/docs/developer-guide/desktop-plugin-sdk)
        * [Memory Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin)
        * [Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin)
        * [Secret Source Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
        * [Browser Vault Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
        * [Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)
        * [Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
        * [Video Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)
        * [Web Search Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/web-search-provider-plugin)
        * [Browser Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
        * [Terminal Environment Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
        * [Delegation provider plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/delegation-provider-plugin)
        * [Application declarations](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/application-declarations)
        * [Catalog submission](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/catalog-submission)
        * [Public plugin API](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
      * [Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
      * [Extending the CLI](https://hermes-agent.nousresearch.com/docs/developer-guide/extending-the-cli)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Subagent lifecycle API


On this page
# Public Subagent Lifecycle API
Plugins can launch and supervise fresh Hermes child sessions without importing `tools.delegate_tool`, gateway internals, TUI state, or `AIAgent` fields. The service resolves its parent from the current agent turn, so it works in CLI, gateway, non-interactive, and kanban-worker sessions. Launching outside an active agent turn fails closed with `No active Hermes parent session`. The facade also works when a plugin runs under `plugins.isolation: host`.
Requests accept `goal`, `context`, `role`, `model`, `provider`, `allowed_toolsets`, `blocked_tools`, `working_directory`, `parent_session_id`, `correlation_id`, `metadata`, and `timeout_seconds`, subject to the restrictions below.

```


from agent.subagent_lifecycle import SubagentLaunchRequest  





  





def launch_review(ctx):  





    # Call from a plugin tool or hook while an agent turn is active.  





    service = ctx.subagent_lifecycle  





    handle = service.launch(SubagentLaunchRequest(  





        goal="Review this change for regressions.",  





        context="Only inspect the supplied repository.",  





        role="leaf",  





        correlation_id="review-42",  





        allowed_toolsets=("file",),  





    ))  





    # Persist handle.to_dict() if desired.  





    if service.wait(handle, timeout_seconds=2).timed_out:  





        return handle.to_dict()  





    return service.result(handle)  



```

`SubagentHandle` is serializable and carries a versioned, opaque capability. Requests and handles may also arrive as mappings, including plugin-host wire records. Pass a handle back to `status`, `wait`, `cancel`, `steer`, `result`, or `reconnect`; malformed or forged handles return `UNKNOWN`/`UNKNOWN_HANDLE` and cannot access a child.
`steer(handle, text)` queues text for the child's next iteration boundary and returns `True` while the child accepts steering. It returns `False` for empty text, unknown or forged handles, handles owned by another parent session, or a child that has finished or stopped accepting steering.
The stable states are `PENDING`, `STARTING`, `RUNNING`, `SUCCEEDED`, `FAILED`, `INTERRUPTED`, `CANCEL_REQUESTED`, `CANCELLED`, and `UNKNOWN`.
`cancel(handle, reason=...)` is cooperative: it asks the child agent to interrupt at its next safe boundary and returns `CANCEL_REQUESTED`; it never claims completion until `wait` or `result` observes a terminal state. Terminal results are immutable, idempotent, bounded to 32k characters, omit transcripts and hidden reasoning, and include a stable result hash.
This API is lifecycle-managed asynchronous execution. Child construction and completion use the same host-owned path as `delegate_task`, including parent tool-resolution restoration, memory notification, serialized `subagent_stop` hooks, resource cleanup, and child-cost rollup. It does not change the synchronous `delegate_task` tool, batch delegation, or its gateway/TUI display. The initial implementation retains metadata and terminal results in-process for one hour. After a process restart, `reconnect` returns `RECONNECT_UNAVAILABLE` and never starts a replacement child. Running Python threads also cannot survive process exit; callers must treat those handles as interrupted by process exit.
Requests are fail-closed: goal/context/metadata sizes are capped, unknown or parent-broadening toolsets are rejected (plugin-registered toolsets count as known), and per-tool blocks, working-directory overrides, and per-launch timeouts are explicitly rejected until Hermes can support them without weakening isolation. Use `allowed_toolsets` to narrow a child; Hermes's existing unsafe-tool block remains enforced.
## Routing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api#routing "Direct link to Routing")
Children follow the `delegation` config (`provider`, `model`, `base_url`, `api_key`, `api_mode`, `request_overrides`) exactly as `delegate_task` children do. The request's `model` overrides the configured model. Its optional `provider` names a configured provider for this launch, with precedence request > delegation config > parent; the selected provider supplies its own credential bundle. An unresolvable provider raises `SubagentLifecycleError` before launch. Core does not expose `provider` to the model: the plugin chooses it, for example from operator config.
The lifecycle API does not consult `delegation.backend`: the plugin that launches a child already chooses its route. To change how `delegate_task` routes the model's subagents, write a [delegation provider plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/delegation-provider-plugin).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/subagent-lifecycle-api.md)
[Previous Middleware](https://hermes-agent.nousresearch.com/docs/developer-guide/middleware)[Next Desktop Plugin SDK](https://hermes-agent.nousresearch.com/docs/developer-guide/desktop-plugin-sdk)
  * [Routing](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api#routing)


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
