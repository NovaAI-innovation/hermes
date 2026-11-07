---
title: "Observer Hooks"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks
scraped_at: 2026-11-07T17:20:29.116620+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/observer-hooks)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Observer Hooks


On this page
# Hermes Observer Hooks
Hermes observer hooks are the read-only telemetry contract for plugins that need to reconstruct agent execution without changing runtime behavior. This contract supports trace, metrics, audit, replay, and export integrations such as Langfuse, OpenTelemetry-style collectors, and NeMo Relay.
Observer hooks are intentionally backend-neutral. They expose stable lifecycle events, correlation IDs, sanitized payloads, timing, status, and error fields. They do not replace Hermes' planner, model providers, memory, tool registry, approval UX, CLI, gateway behavior, or execution semantics.
Behavior-changing request or execution wrappers are outside this observer contract. Observer hooks should report what happened; they should not replace provider requests, tool arguments, or execution callbacks.
Hermes also has a first-party NeMo Relay shared-metrics path. It uses these lifecycle boundaries directly and does not require enabling an observability plugin. See [Relay shared metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics).
## Contract[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#contract "Direct link to Contract")
Plugins register observer callbacks from `register(ctx)`:

```


def register(ctx):  





    ctx.register_hook("pre_api_request", on_pre_api_request)  





    ctx.register_hook("post_api_request", on_post_api_request)  





    ctx.register_hook("pre_tool_call", on_pre_tool_call)  





    ctx.register_hook("post_tool_call", on_post_tool_call)  



```

Every hook callback receives keyword arguments. Plugins should accept `**kwargs` so additive fields remain backward-compatible:

```


def on_post_tool_call(**kwargs):  





    tool_name = kwargs.get("tool_name")  





    status = kwargs.get("status")  





    result = kwargs.get("result")  



```

The plugin manager injects this field into every hook payload:

```


telemetry_schema_version = "hermes.observer.v1"  



```

Hook callbacks are fail-open. Hermes catches callback exceptions, logs a warning, and keeps the agent loop running.
Most observer hook return values are ignored. The exceptions are older behavior-affecting hooks:  
| Hook  | Return behavior  |  
| --- | --- |  
| `pre_llm_call`  | May return a string or `{"context": "..."}` to inject ephemeral context into the current user message, or `{"action": "block", "message": "..."}` to end the turn before any inference request (the message becomes the reply and the prompt is stored as a withheld placeholder; see [Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)). A callback that raises or times out is skipped, so it never blocks.  |  
| `pre_tool_call`  | May return `{"action": "block", "message": "..."}` to block a tool before execution, or `{"action": "modify", "args": {...}}` to transform the tool's input arguments.  |  
| `transform_tool_result`  | May return a replacement tool result string after `post_tool_call`.  |  
| `transform_llm_output`  | May return a replacement final assistant text string.  |  
Telemetry plugins should treat these behavior-affecting returns as optional compatibility features, not as observability requirements.
## Correlation IDs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#correlation-ids "Direct link to Correlation IDs")
Observer payloads use stable IDs so plugins can join events without relying on callback order alone.  
| Field  | Meaning  |  
| --- | --- |  
| `session_id`  | Conversation/session identity.  |  
| `task_id`  | Task identity, especially useful for subagents and isolated execution.  |  
| `turn_id`  | User-turn identity shared by API attempts and tool calls in a turn.  |  
| `api_request_id`  | Opaque provider-attempt identity. Do not parse its string format.  |  
| `api_call_count`  | Numeric API attempt count within the agent loop.  |  
| `tool_call_id`  | Provider-supplied tool call ID when available.  |  
|  `parent_session_id` / `child_session_id`  | Session link for delegated subagents.  |  
|  `parent_subagent_id` / `child_subagent_id`  | Subagent link when available.  |  
| `parent_turn_id`  | Parent turn that spawned delegated work.  |  
Consumers should prefer explicit fields over parsing compound IDs. In particular, `api_request_id` is an opaque correlation value.
## Event Families[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#event-families "Direct link to Event Families")
### Session Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#session-lifecycle "Direct link to Session Lifecycle")
Session hooks describe conversation boundaries and resets:  
| Hook  | When it fires  |  
| --- | --- |  
| `on_session_start`  | A brand-new session starts after the system prompt is built.  |  
| `on_session_end`  | A `run_conversation` call ends, including interrupted or incomplete turns.  |  
| `on_session_finalize`  | CLI or gateway tears down an active session identity.  |  
| `on_session_reset`  | CLI or gateway moves from an old session identity to a new one.  |  
| `on_session_delete`  | A session delete or deliberate archive committed (`reason` says which).  |  
Common fields include `session_id`, `completed`, `interrupted`, `reason`, `old_session_id`, and `new_session_id` where available.
`on_session_end` is turn/run scoped. It is not necessarily the final lifetime boundary for a chat identity. Use `on_session_finalize` and `on_session_reset` for lifecycle cleanup that must happen once per session identity.
### Turn-Scoped LLM Hooks[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#turn-scoped-llm-hooks "Direct link to Turn-Scoped LLM Hooks")
These hooks frame the user turn, not individual provider API attempts:  
| Hook  | When it fires  |  
| --- | --- |  
| `pre_llm_call`  | Before the tool loop begins for a user turn.  |  
| `post_llm_call`  | After the turn completes with final assistant output.  |  
Common `pre_llm_call` fields include `session_id`, `turn_id`, `user_message`, `conversation_history`, `is_first_turn`, `model`, `platform`, and `sender_id`.
Common `post_llm_call` fields include `session_id`, `turn_id`, `user_message`, `assistant_response`, `conversation_history`, `model`, and `platform`.
Use request-scoped API hooks for LLM span telemetry. Use `pre_llm_call` and `post_llm_call` for turn-level context, compatibility, and final turn summary.
### Request-Scoped API Hooks[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#request-scoped-api-hooks "Direct link to Request-Scoped API Hooks")
API hooks describe provider attempts inside the agent loop:  
| Hook  | When it fires  |  
| --- | --- |  
| `pre_api_request`  | Immediately before a provider API request.  |  
| `post_api_request`  | After a successful provider response.  |  
| `api_request_error`  | After a failed provider request or retryable error path.  |  
| `pre_auxiliary_call`  | Before each provider attempt of an auxiliary LLM call (titling, compression, MoA, vision, ...). Carries `aux_task`; the `*_api_request` hooks stay main-loop only.  |  
| `post_auxiliary_call`  | After that attempt returns or raises (`error` set on failure).  |  
`pre_api_request` includes:
  * identity: `session_id`, `task_id`, `turn_id`, `api_request_id`
  * runtime: `platform`, `model`, `provider`, `base_url`, `api_mode`
  * attempt metadata: `api_call_count`, `message_count`, `tool_count`, `approx_input_tokens`, `request_char_count`, `max_tokens`
  * timing: `started_at`
  * sanitized request payload: `request`


`post_api_request` includes the same identity/runtime fields plus:
  * `api_duration`, `started_at`, `ended_at`
  * `finish_reason`, `message_count`, `response_model`
  * `usage`
  * `assistant_content_chars`, `assistant_tool_call_count`
  * sanitized response payload: `response`
  * compatibility object: `assistant_message`


`api_request_error` includes the same identity/runtime fields plus:
  * `api_duration`, `started_at`, `ended_at`
  * `status_code`, `retry_count`, `max_retries`, `retryable`, `reason`
  * structured `error = {"type": ..., "message": ...}`
  * sanitized failed request payload: `request`


The sanitized `request`, `response`, and `error` fields are the canonical observer inputs for new consumers.
### Tool Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#tool-lifecycle "Direct link to Tool Lifecycle")
Tool hooks describe individual tool calls:  
| Hook  | When it fires  |  
| --- | --- |  
| `pre_tool_call`  | Before guardrail-approved tool dispatch.  |  
| `post_tool_call`  | After tool dispatch, cancellation, block, or error completion.  |  
| `transform_tool_result`  | After `post_tool_call`, before the result is appended to model context.  |  
`pre_tool_call` includes `tool_name`, `args`, `task_id`, `session_id`, `tool_call_id`, `turn_id`, and `api_request_id`.
`post_tool_call` includes the same identity fields plus `result`, `duration_ms`, `status`, `error_type`, and `error_message`.
`status` is the observer-grade lifecycle outcome. Common values include:  
| Status  | Meaning  |  
| --- | --- |  
| `ok`  | Tool completed normally.  |  
| `error`  | Tool ran and returned or raised an error outcome.  |  
| `blocked`  | A `pre_tool_call` hook blocked execution.  |  
| `cancelled`  | Execution was cancelled before normal completion.  |  
`post_tool_call` is emitted for blocked and cancelled paths so telemetry plugins can close spans cleanly.
### Human Input Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#human-input-lifecycle "Direct link to Human Input Lifecycle")
`on_human_input_request` / `on_human_input_resolved` fire around every point where the agent blocks for a person: sudo password prompts (`kind="sudo"`), `clarify` questions (`kind="clarify"`) and approval prompts (`kind="approval"`) on CLI, TUI/Desktop, ACP and gateway platforms. Fields: `kind`, `request_id` (shared by the pair), `session_id`, `session_key`, `platform`, and a force-redacted `prompt`; the resolved hook adds `outcome`. The typed password or answer is never included. Smart (aux-LLM) approvals do not fire it. Source: `tools/human_input_hooks.py`.
### Approval Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#approval-lifecycle "Direct link to Approval Lifecycle")
Approval hooks describe dangerous-command approval prompts:  
| Hook  | When it fires  |  
| --- | --- |  
| `pre_approval_request`  | Before the approval request is shown or sent.  |  
| `post_approval_response`  | After the user responds or the request times out.  |  
Common fields include `command`, `description`, `pattern_key`, `pattern_keys`, `session_key`, and `surface`.
`post_approval_response` also includes `choice`, with values such as `once`, `session`, `always`, `deny`, `timeout`, and `cancelled` (nobody answered: the prompt was withdrawn — turn interrupted or ended — or never reached the user on the CLI).
Approval hooks are observer-only. Plugins cannot pre-answer or veto approvals from these hooks. To prevent a tool from reaching approval, use `pre_tool_call` blocking.
### Subagent Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#subagent-lifecycle "Direct link to Subagent Lifecycle")
Subagent hooks describe delegated child-agent work:  
| Hook  | When it fires  |  
| --- | --- |  
| `subagent_start`  | A delegated child agent is created.  |  
| `subagent_stop`  | A delegated child agent returns or fails.  |  
`subagent_start` fields include `parent_session_id`, `parent_turn_id`, `parent_subagent_id`, `child_session_id`, `child_subagent_id`, `child_role`, and `child_goal`.
`subagent_stop` fields include parent/child session IDs, role/status fields, `child_summary`, `duration_ms`, and a metadata-only `tool_call_history`. Each history entry contains the tool name, argument names, bounded side-effect targets, input/output byte counts, and outcome. URL query strings and fragments are removed; raw arguments, prompts, commands, contents, headers, and results are intentionally excluded.
Observers can use these hooks to model nested trajectories while keeping child agent execution linked to the parent turn that spawned it.
## Payload Safety[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#payload-safety "Direct link to Payload Safety")
Observer payloads are designed for telemetry consumers, not raw object access. New consumers should use the sanitized API payloads:
  * `pre_api_request.request`
  * `post_api_request.response`
  * `api_request_error.request`
  * `api_request_error.error`


Sanitization converts provider objects to JSON-compatible structures, bounds large payloads, redacts sensitive keys, and avoids exposing raw response objects in sanitized fields.
Legacy compatibility fields such as `request_messages`, `conversation_history`, and `assistant_message` may still be present for existing plugins. New observability consumers should prefer the sanitized payloads.
## Performance[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#performance "Direct link to Performance")
The default uninstrumented path should stay cheap. Expensive request/response payload construction is gated behind `has_hook(...)`, so Hermes only builds sanitized API telemetry payloads when at least one plugin registered the relevant hook.
Plugin authors should preserve this property:
  * Register only hooks the plugin actually consumes.
  * Avoid deep-copying or re-sanitizing already sanitized payloads.
  * Keep hook callbacks fast and fail-open.
  * Offload network export or batch writes when practical.


## Writing An Observer Plugin[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#writing-an-observer-plugin "Direct link to Writing An Observer Plugin")
Minimal observer plugin:

```


def register(ctx):  





    ctx.register_hook("pre_api_request", on_pre_api_request)  





    ctx.register_hook("post_api_request", on_post_api_request)  





    ctx.register_hook("pre_tool_call", on_pre_tool_call)  





    ctx.register_hook("post_tool_call", on_post_tool_call)  





  





  





def on_pre_api_request(**kwargs):  





    start_llm_span(  





        request_id=kwargs.get("api_request_id"),  





        turn_id=kwargs.get("turn_id"),  





        request=kwargs.get("request"),  





        model=kwargs.get("model"),  





    )  





  





  





def on_post_api_request(**kwargs):  





    finish_llm_span(  





        request_id=kwargs.get("api_request_id"),  





        response=kwargs.get("response"),  





        usage=kwargs.get("usage"),  





        duration=kwargs.get("api_duration"),  





    )  





  





  





def on_pre_tool_call(**kwargs):  





    start_tool_span(  





        call_id=kwargs.get("tool_call_id"),  





        name=kwargs.get("tool_name"),  





        args=kwargs.get("args"),  





    )  





  





  





def on_post_tool_call(**kwargs):  





    finish_tool_span(  





        call_id=kwargs.get("tool_call_id"),  





        result=kwargs.get("result"),  





        status=kwargs.get("status"),  





        duration_ms=kwargs.get("duration_ms"),  





    )  



```

Use `session_id`, `turn_id`, `api_request_id`, and `tool_call_id` for span correlation. Use subagent and approval hooks when the export format supports nested agent work or security lifecycle events.
## Existing Consumers[​](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#existing-consumers "Direct link to Existing Consumers")
The official [Langfuse catalog plugin](https://github.com/NousResearch/hermes-official-plugins/tree/main/langfuse) demonstrates direct hook-based observability for turns, provider requests, and tool calls.
The native NeMo Relay SDK integration maps Hermes session, turn, LLM, and tool lifecycles to Relay. Relay's discovered user and system configuration, or an explicit file selected with `HERMES_NEMO_RELAY_PLUGINS_TOML`, can add [ATOF, ATIF, or OTEL](https://docs.nvidia.com/nemo/relay/configure-plugins/observability/about) exporters and execution middleware; see [Relay shared metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/observer-hooks.md)
[Previous Plugin LLM Access](https://hermes-agent.nousresearch.com/docs/developer-guide/plugin-llm-access)[Next Middleware](https://hermes-agent.nousresearch.com/docs/developer-guide/middleware)
  * [Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#contract)
  * [Correlation IDs](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#correlation-ids)
  * [Event Families](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#event-families)
    * [Session Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#session-lifecycle)
    * [Turn-Scoped LLM Hooks](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#turn-scoped-llm-hooks)
    * [Request-Scoped API Hooks](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#request-scoped-api-hooks)
    * [Tool Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#tool-lifecycle)
    * [Human Input Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#human-input-lifecycle)
    * [Approval Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#approval-lifecycle)
    * [Subagent Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#subagent-lifecycle)
  * [Payload Safety](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#payload-safety)
  * [Performance](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#performance)
  * [Writing An Observer Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#writing-an-observer-plugin)
  * [Existing Consumers](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks#existing-consumers)


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
