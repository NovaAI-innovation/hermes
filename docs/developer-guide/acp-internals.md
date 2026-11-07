---
title: "ACP Internals"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals
scraped_at: 2026-11-07T17:20:20.151302+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/acp-internals)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
      * [Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
      * [Browser CDP Supervisor](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
      * [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
      * [Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals)
      * [Chronos Managed-Cron Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/chronos-managed-cron-contract)
      * [Egress proxy internals](https://hermes-agent.nousresearch.com/docs/developer-guide/egress-internals)
      * [Gateway Monitoring](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-monitoring)
      * [Relay ↔ Connector Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-connector-contract)
      * [Relay Shared Metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics)
      * [Streaming TTS Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
      * [Billing Lifecycle (TUI)](https://hermes-agent.nousresearch.com/docs/developer-guide/billing-lifecycle)
      * [Trajectory Format](https://hermes-agent.nousresearch.com/docs/developer-guide/trajectory-format)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/source-update-completion)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Internals
  * ACP Internals


On this page
# ACP Internals
The ACP adapter wraps Hermes' synchronous `AIAgent` in an async JSON-RPC stdio server.
Key implementation files:
  * `acp_adapter/entry.py`
  * `acp_adapter/server.py`
  * `acp_adapter/session.py`
  * `acp_adapter/events.py`
  * `acp_adapter/permissions.py`
  * `acp_adapter/tools.py`
  * `acp_adapter/auth.py`


## Boot flow[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#boot-flow "Direct link to Boot flow")

```


hermes acp / hermes-acp / python -m acp_adapter  





  -> acp_adapter.entry.main()  





  -> parse --version / --check / --setup before server startup  





  -> load ~/.hermes/.env  





  -> configure stderr logging  





  -> construct HermesACPAgent  





  -> acp.run_agent(agent, use_unstable_protocol=True)  



```

Stdout is reserved for ACP JSON-RPC transport. Human-readable logs go to stderr.
### Gateway terminal projection[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#gateway-terminal-projection "Direct link to Gateway terminal projection")
`acp_adapter/gateway_server.py` waits for the completion of the exact submitted admission. A cancelled admission returns `stopReason: cancelled`; a failed admission raises an ACP request error rather than reporting `end_turn`. Ordinary completion still returns `end_turn`. Cancellation while waiting for the model suppresses the local `Operation interrupted: waiting for model response` status message; actual partial assistant text remains visible. Terminal outcomes come from the gateway's structured execution result, not from assistant prose or a session-wide cancellation flag.
## Major components[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#major-components "Direct link to Major components")
###  `HermesACPAgent`[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#hermesacpagent "Direct link to hermesacpagent")
`acp_adapter/server.py` implements the ACP agent protocol.
Responsibilities:
  * initialize / authenticate
  * new/load/resume/fork/list/cancel session methods
  * prompt execution
  * session model switching
  * wiring sync AIAgent callbacks into ACP async notifications


###  `SessionManager`[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#sessionmanager "Direct link to sessionmanager")
`acp_adapter/session.py` tracks live ACP sessions.
Each session stores:
  * `session_id`
  * `agent`
  * `cwd`
  * `model`
  * `history`
  * `cancel_event`


The manager is thread-safe and supports:
  * create
  * get
  * remove
  * fork
  * list
  * cleanup
  * cwd updates


### Event bridge[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#event-bridge "Direct link to Event bridge")
`acp_adapter/events.py` converts AIAgent callbacks into ACP `session_update` events.
Bridged callbacks:
  * `tool_progress_callback`
  * `thinking_callback` (currently set to `None` in the ACP bridge — reasoning is forwarded through `step_callback` instead)
  * `step_callback`


Every ACP tool call reaches a terminal status: `tool.completed` closes the call with its own result (`completed` / `failed`), the `step_callback` `prev_tools` pass is only a fallback for runtimes that never project a completion, and anything still open when the turn ends — a denied or blocked call, an interrupted one — is marked `failed` before the response is returned.
Because `AIAgent` runs in a worker thread while ACP I/O lives on the main event loop, the bridge uses:

```


asyncio.run_coroutine_threadsafe(...)  



```

### Permission bridge[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#permission-bridge "Direct link to Permission bridge")
`acp_adapter/permissions.py` adapts dangerous terminal approval prompts into ACP permission requests.
Mapping:
  * `allow_once` -> Hermes `once`
  * `allow_always` -> Hermes `always`
  * reject options -> Hermes `deny`


Timeouts and bridge failures deny by default.
### Tool rendering helpers[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#tool-rendering-helpers "Direct link to Tool rendering helpers")
`acp_adapter/tools.py` maps Hermes tools to ACP tool kinds and builds editor-facing content.
Examples:
  * `patch` / `write_file` -> file diffs
  * `terminal` -> shell command text
  * `read_file` / `search_files` -> text previews
  * large results -> truncated text blocks for UI safety


## Session lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#session-lifecycle "Direct link to Session lifecycle")

```


new_session(cwd)  





  -> create SessionState  





  -> create AIAgent(platform="acp", enabled_toolsets=<_get_platform_tools(config, "acp"), as on the  





                   gateway: platform_toolsets.acp (default hermes-acp) plus the resolver's extras  





                   such as plugin toolsets, with its admitted MCP servers keyed mcp-<server>>,  





                   disabled_toolsets=<agent.disabled_toolsets>)  





  -> bind task_id/session_id to cwd override  





  





prompt(..., session_id)  





  -> extract text from ACP content blocks  





  -> reset cancel event  





  -> install callbacks + approval bridge  





  -> run AIAgent in ThreadPoolExecutor  





  -> update session history  





  -> emit final agent message chunk  



```

A turn that ends in a terminal failure (provider refusal, non-retryable error, exhausted retries, interrupt before any reply) is closed by the core loop with a Hermes-authored assistant row ("Your request was not processed…" / "This turn did not complete…") so the durable transcript never ends on an open `user` row. Without it the next prompt would be merged into the failed request and replayed. Context-overflow failures are exempt: their repair is session rotation, not another row.
### Cancelation[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#cancelation "Direct link to Cancelation")
`cancel(session_id)`:
  * sets the session cancel event
  * calls `agent.interrupt()` when available
  * causes the prompt response to return `stop_reason="cancelled"`


### Forking[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#forking "Direct link to Forking")
`fork_session()` deep-copies message history into a new live session, preserving conversation state while giving the fork its own session ID and cwd.
## Provider/auth behavior[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#providerauth-behavior "Direct link to Provider/auth behavior")
ACP does not implement its own auth store.
Instead it reuses Hermes' runtime resolver:
  * `acp_adapter/auth.py`
  * `hermes_cli/runtime_provider.py`


So ACP advertises and uses the currently configured Hermes provider/credentials. It also always advertises a terminal setup auth method (`hermes-setup`, args `--setup`) so first-run ACP clients can open Hermes' interactive model/provider configuration before starting a normal ACP session.
## Working directory binding[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#working-directory-binding "Direct link to Working directory binding")
ACP sessions carry an editor cwd.
The session manager binds that cwd to the ACP session ID via task-scoped terminal/file overrides, so file and terminal tools operate relative to the editor workspace.
## Duplicate same-name tool calls[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#duplicate-same-name-tool-calls "Direct link to Duplicate same-name tool calls")
The event bridge tracks tool IDs FIFO per tool name, not just one ID per name. This is important for:
  * parallel same-name calls
  * repeated same-name calls in one step


Without FIFO queues, completion events would attach to the wrong tool invocation.
## Approval callback restoration[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#approval-callback-restoration "Direct link to Approval callback restoration")
ACP temporarily installs an approval callback on the terminal tool during prompt execution, then restores the previous callback afterward. This avoids leaving ACP session-specific approval handlers installed globally forever.
## Current limitations[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#current-limitations "Direct link to Current limitations")
  * ACP sessions are persisted to the shared `~/.hermes/state.db` (SessionDB) and transparently restored across process restarts; they appear in `session_search`
  * non-text prompt blocks are currently ignored for request text extraction
  * editor-specific UX varies by ACP client implementation


## Related files[​](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#related-files "Direct link to Related files")
  * `tests/acp_adapter/` — ACP test suite
  * `toolsets.py` — `hermes-acp` toolset definition
  * `hermes_cli/main.py` — `hermes acp` CLI subcommand
  * `pyproject.toml` — `[acp]` optional dependency + `hermes-acp` script


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/acp-internals.md)
[Previous Browser CDP Supervisor](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)[Next Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals)
  * [Boot flow](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#boot-flow)
    * [Gateway terminal projection](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#gateway-terminal-projection)
  * [Major components](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#major-components)
    * [`HermesACPAgent`](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#hermesacpagent)
    * [`SessionManager`](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#sessionmanager)
    * [Event bridge](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#event-bridge)
    * [Permission bridge](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#permission-bridge)
    * [Tool rendering helpers](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#tool-rendering-helpers)
  * [Session lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#session-lifecycle)
    * [Cancelation](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#cancelation)
    * [Forking](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#forking)
  * [Provider/auth behavior](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#providerauth-behavior)
  * [Working directory binding](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#working-directory-binding)
  * [Duplicate same-name tool calls](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#duplicate-same-name-tool-calls)
  * [Approval callback restoration](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#approval-callback-restoration)
  * [Current limitations](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#current-limitations)
  * [Related files](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals#related-files)


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
