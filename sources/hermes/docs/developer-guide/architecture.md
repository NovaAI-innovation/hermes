---
title: "Architecture"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/architecture
scraped_at: 2026-11-07T17:20:11.934738+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/architecture)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
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
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Architecture
  * Architecture


On this page
# Architecture
This page is the top-level map of Hermes Agent internals. Use it to orient yourself in the codebase, then dive into subsystem-specific docs for implementation details.
## System Overview[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#system-overview "Direct link to System Overview")

```


┌─────────────────────────────────────────────────────────────────────┐  





│                        Entry Points                                  │  





│                                                                      │  





│  CLI (cli.py)    Gateway (gateway/run.py)    ACP (acp_adapter/)     │  





│  Batch Runner    API Server                  Python Library          │  





└──────────┬──────────────┬───────────────────────┬───────────────────┘  





           │              │                       │  





           ▼              ▼                       ▼  





┌─────────────────────────────────────────────────────────────────────┐  





│                     AIAgent (run_agent.py)                          │  





│                                                                     │  





│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │  





│  │ Prompt       │  │ Provider     │  │ Tool         │               │  





│  │ Builder      │  │ Resolution   │  │ Dispatch     │               │  





│  │ (prompt_     │  │ (runtime_    │  │ (model_      │               │  





│  │  builder.py) │  │  provider.py)│  │  tools.py)   │               │  





│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘               │  





│         │                 │                 │                       │  





│  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐               │  





│  │ Compression  │  │ 3 API Modes  │  │ Tool Registry│               │  





│  │ & Caching    │  │ chat_compl.  │  │ (registry.py)│               │  





│  │              │  │ codex_resp.  │  │ 70+ tools    │               │  





│  │              │  │ anthropic    │  │ 28 toolsets  │               │  





│  └──────────────┘  └──────────────┘  └──────────────┘               │  





└─────────┴─────────────────┴─────────────────┴───────────────────────┘  





           │                                    │  





           ▼                                    ▼  





┌───────────────────┐              ┌──────────────────────┐  





│ Session Storage   │              │ Tool Backends         │  





│ (SQLite + FTS5)   │              │ Terminal (7 backends) │  





│ hermes_state.py   │              │ Browser (5 backends)  │  





│ gateway/session.py│              │ Web (4 backends)      │  





└───────────────────┘              │ MCP (dynamic)         │  





                                   │ File, Vision, etc.    │  





                                   └──────────────────────┘  



```

## Directory Structure[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#directory-structure "Direct link to Directory Structure")

```


hermes-agent/  





├── run_agent.py              # AIAgent facade — loop lives in agent/conversation_loop.py + agent/turn_*.py  





├── cli.py                    # HermesCLI facade — mixins in hermes_cli/cli_*_mixin.py  





├── model_tools.py            # Tool discovery, schema collection, dispatch  





├── toolsets.py               # Tool groupings and platform presets  





├── hermes_state.py           # SQLite session/state database facade (+ hermes_state_*.py siblings)  





├── hermes_constants.py       # HERMES_HOME, profile-aware paths  





├── batch_runner.py           # Batch trajectory generation  





│  





├── agent/                    # Agent internals  





│   ├── prompt_builder.py     # System prompt assembly  





│   ├── context_engine.py     # ContextEngine ABC (pluggable)  





│   ├── context_compressor.py # Default engine — lossy summarization  





│   ├── prompt_caching.py     # Anthropic prompt caching  





│   ├── auxiliary_client.py   # Auxiliary LLM for side tasks (vision, summarization)  





│   ├── model_metadata.py     # Model context lengths, token estimation  





│   ├── models_dev.py         # models.dev registry integration  





│   ├── anthropic_adapter.py  # Anthropic Messages API format conversion  





│   ├── display.py            # KawaiiSpinner, tool preview formatting  





│   ├── skill_commands.py     # Skill slash commands  





│   ├── memory_manager.py    # Memory manager orchestration  





│   ├── memory_provider.py   # Memory provider ABC  





│   └── trajectory.py         # Trajectory saving helpers  





│  





├── hermes_cli/               # CLI subcommands and setup  





│   ├── main.py               # Entry point — `hermes` subcommands (parsers in subcommands/, main_*.py)  





│   ├── config.py             # DEFAULT_CONFIG, OPTIONAL_ENV_VARS, migration  





│   ├── commands.py           # COMMAND_REGISTRY — central slash command definitions  





│   ├── auth.py               # PROVIDER_REGISTRY, credential resolution (+ auth_*.py siblings)  





│   ├── runtime_provider.py   # Provider → api_mode + credentials  





│   ├── models.py             # Model catalog, provider model lists  





│   ├── model_switch.py       # /model command logic (CLI + gateway shared)  





│   ├── setup.py              # Interactive setup wizard (+ setup_*.py siblings)  





│   ├── skin_engine.py        # CLI theming engine  





│   ├── skills_config.py      # hermes skills — enable/disable per platform  





│   ├── skills_hub.py         # /skills slash command  





│   ├── tools_config.py       # hermes tools — enable/disable per platform  





│   ├── plugins.py            # PluginManager — discovery, loading, hooks  





│   ├── callbacks.py          # Terminal callbacks (clarify, sudo, approval)  





│   └── gateway.py            # hermes gateway start/stop  





│  





├── tools/                    # Tool implementations (one file per tool)  





│   ├── registry.py           # Central tool registry  





│   ├── approval.py           # Dangerous command detection  





│   ├── terminal_tool.py      # Terminal orchestration  





│   ├── process_registry.py   # Background process management  





│   ├── file_tools.py         # read_file, write_file, patch, search_files  





│   ├── web_tools.py          # web_search, web_extract  





│   ├── browser_use_cli.py    # browser_exec — Python over CDP (browser-harness)  





│   ├── browser_session.py    # Per-task browser sessions (+ browser_session_*.py siblings)  





│   ├── browser_launcher.py   # Local Chromium launch, reuse and orphan reaping  





│   ├── code_execution_tool.py # execute_code sandbox  





│   ├── delegate_tool.py      # Subagent delegation  





│   ├── mcp_tool.py           # MCP client facade (+ mcp_tool_*.py siblings)  





│   ├── credential_files.py   # File-based credential passthrough  





│   ├── env_passthrough.py    # Env var passthrough for sandboxes  





│   ├── ansi_strip.py         # ANSI escape stripping  





│   └── environments/         # Terminal backends (local, docker, ssh, modal, daytona, vercel_sandbox)  





│  





├── gateway/                  # Messaging platform gateway  





│   ├── run.py                # GatewayRunner facade — message dispatch (+ run_*.py siblings)  





│   ├── session.py            # SessionStore — conversation persistence  





│   ├── delivery.py           # Outbound message delivery  





│   ├── pairing.py            # DM pairing authorization  





│   ├── hooks.py              # Hook discovery and lifecycle events  





│   ├── mirror.py             # Cross-session message mirroring  





│   ├── status.py             # Token locks, profile-scoped process tracking  





│   └── platforms/            # Core ingress adapters: api_server, webhook,  





│                             #   msgraph_webhook  





│  





├── plugins/platforms/        # Bundled platform plugins: telegram, discord, slack,  





│                             #   whatsapp, matrix, mattermost, email, sms, dingtalk,  





│                             #   feishu, wecom, irc, line, teams, google_chat,  





│                             #   buzz, ntfy, photon, raft, simplex, whatsapp_cloud,  





│                             #   signal, weixin, bluebubbles, qqbot  





│                             #   (Home Assistant: `homeassistant` catalog plugin;  





│                             #    Yuanbao: `yuanbao` Hermes Labs plugin)  





│  





├── acp_adapter/              # ACP server (VS Code / Zed / JetBrains)  





├── cron/                     # Scheduler (jobs.py, scheduler.py)  





├── plugins/memory/           # Memory provider plugins  





├── plugins/context_engine/   # Context engine plugins  





├── skills/                   # Bundled skills (always available)  





├── optional-skills/          # Official optional skills (install explicitly)  





├── website/                  # Docusaurus documentation site  





└── tests/                    # Pytest suite (~25,000 tests across ~1,250 files)  



```

## Data Flow[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#data-flow "Direct link to Data Flow")
### CLI Session[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cli-session "Direct link to CLI Session")

```


User input → HermesCLI.process_input()  





  → AIAgent.run_conversation()  





    → prompt_builder.build_system_prompt()  





    → runtime_provider.resolve_runtime_provider()  





    → API call (chat_completions / codex_responses / anthropic_messages)  





    → tool_calls? → model_tools.handle_function_call() → loop  





    → final response → display → save to SessionDB  



```

### Gateway Message[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#gateway-message "Direct link to Gateway Message")

```


Platform event → Adapter.on_message() → MessageEvent  





  → GatewayRunner._handle_message()  





    → authorize user  





    → resolve session key  





    → create AIAgent with session history  





    → AIAgent.run_conversation()  





    → deliver response back through adapter  



```

### Cron Job[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cron-job "Direct link to Cron Job")

```


Scheduler tick → load due jobs from jobs.json  





  → create fresh AIAgent (no history)  





  → inject attached skills as context  





  → run job prompt  





  → deliver response to target platform  





  → update job state and next_run  



```

## Recommended Reading Order[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#recommended-reading-order "Direct link to Recommended Reading Order")
If you are new to the codebase:
  1. **This page** — orient yourself
  2. **[Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)** — how AIAgent works
  3. **[Prompt Assembly](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)** — system prompt construction
  4. **[Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)** — how providers are selected
  5. **[Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)** — practical guide to adding a new provider
  6. **[Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)** — tool registry, dispatch, environments
  7. **[Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)** — SQLite schema, FTS5, session lineage
  8. **[Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals)** — messaging platform gateway
  9. **[Context Compression& Prompt Caching](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)** — compression and caching
  10. **[ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)** — IDE integration


## Major Subsystems[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#major-subsystems "Direct link to Major Subsystems")
### Agent Loop[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#agent-loop "Direct link to Agent Loop")
The synchronous orchestration engine (`AIAgent`, exposed by the `run_agent.py` facade; the loop lives in `agent/conversation_loop.py` and `agent/turn_*.py`). Handles provider selection, prompt construction, tool execution, retries, fallback, callbacks, compression, and persistence. Supports three API modes for different provider backends.
→ [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
### Prompt System[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#prompt-system "Direct link to Prompt System")
Prompt construction and maintenance across the conversation lifecycle:
  * **`system_prompt.py`+`prompt_builder.py`** — assembles the ordered system-prompt tiers (`stable` → `context` → `volatile`): identity/tool guidance/skills, context files, then memory/profile/timestamp blocks
  * **`prompt_caching.py`**— Applies Anthropic cache breakpoints for prefix caching
  * **`context_compressor.py`**— Summarizes middle conversation turns when context exceeds thresholds


→ [Prompt Assembly](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly), [Context Compression & Prompt Caching](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)
### Provider Resolution[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#provider-resolution "Direct link to Provider Resolution")
A shared runtime resolver used by CLI, gateway, cron, ACP, and auxiliary calls. Maps `(provider, model)` tuples to `(api_mode, api_key, base_url)`. Handles 18+ providers, OAuth flows, credential pools, and alias resolution.
→ [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
### Tool System[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#tool-system "Direct link to Tool System")
Central tool registry (`tools/registry.py`) with 70+ registered tools across ~28 toolsets. Each tool file self-registers at import time. The registry handles schema collection, dispatch, availability checking, and error wrapping. Terminal tools support 6 built-in backends (local, Docker, SSH, Daytona, Modal, Vercel Sandbox) plus plugin backends (e.g. Singularity).
→ [Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
### Session Persistence[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#session-persistence "Direct link to Session Persistence")
SQLite-based session storage with FTS5 full-text search. Sessions have lineage tracking (parent/child across compressions), per-platform isolation, and atomic writes with contention handling.
→ [Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)
### Messaging Gateway[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#messaging-gateway "Direct link to Messaging Gateway")
Long-running process with 25+ platform adapters (built-in + bundled plugins), unified session routing, user authorization (allowlists + DM pairing), slash command dispatch, hook system, cron ticking, and background maintenance.
→ [Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals)
### Plugin System[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#plugin-system "Direct link to Plugin System")
Three discovery sources: `~/.hermes/plugins/` (user), `.hermes/plugins/` (project), and pip entry points. Plugins register tools, hooks, and CLI commands through a context API. Two specialized plugin types exist: memory providers (`plugins/memory/`) and context engines (`plugins/context_engine/`). Both are single-select — only one of each can be active at a time, configured via `hermes plugins` or `config.yaml`.
→ [Plugin Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins), [Memory Provider Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin)
### Cron[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cron "Direct link to Cron")
First-class agent tasks (not shell tasks). Jobs store in JSON, support multiple schedule formats, can attach skills and scripts, and deliver to any platform.
→ [Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals)
### ACP Integration[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#acp-integration "Direct link to ACP Integration")
Exposes Hermes as an editor-native agent over stdio/JSON-RPC for VS Code, Zed, and JetBrains.
→ [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
### Trajectories[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#trajectories "Direct link to Trajectories")
Generates ShareGPT-format trajectories from agent sessions for training data generation.
→ [Trajectories & Training Format](https://hermes-agent.nousresearch.com/docs/developer-guide/trajectory-format)
## Design Principles[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#design-principles "Direct link to Design Principles")  
| Principle  | What it means in practice  |  
| --- | --- |  
| **Prompt stability**  | System prompt doesn't change mid-conversation. No cache-breaking mutations except explicit user actions (`/model`).  |  
| **Observable execution**  | Every tool call is visible to the user via callbacks. Progress updates in CLI (spinner) and gateway (chat messages).  |  
| **Interruptible**  | API calls and tool execution can be cancelled mid-flight by user input or signals.  |  
| **Platform-agnostic core**  | One AIAgent class serves CLI, gateway, ACP, batch, and API server. Platform differences live in the entry point, not the agent.  |  
| **Loose coupling**  | Optional subsystems (MCP, plugins, memory providers, RL environments) use registry patterns and check_fn gating, not hard dependencies.  |  
| **Profile isolation**  | Each profile (`hermes -p <name>`) gets its own HERMES_HOME, config, memory, sessions, and gateway PID. Multiple profiles run concurrently.  |  
## File Dependency Chain[​](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#file-dependency-chain "Direct link to File Dependency Chain")

```


tools/registry.py  (no deps — imported by all tool files)  





       ↑  





tools/*.py  (each calls registry.register() at import time)  





       ↑  





model_tools.py  (imports tools/registry + triggers tool discovery)  





       ↑  





run_agent.py, cli.py, batch_runner.py, environments/  



```

This chain means tool registration happens at import time, before any agent instance is created. Any `tools/*.py` file with a top-level `registry.register()` call is auto-discovered — no manual import list needed.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/architecture.md)
[Previous TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)[Next Codebase Ownership Map](https://hermes-agent.nousresearch.com/docs/developer-guide/codebase-ownership)
  * [System Overview](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#system-overview)
  * [Directory Structure](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#directory-structure)
  * [Data Flow](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#data-flow)
    * [CLI Session](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cli-session)
    * [Gateway Message](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#gateway-message)
    * [Cron Job](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cron-job)
  * [Recommended Reading Order](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#recommended-reading-order)
  * [Major Subsystems](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#major-subsystems)
    * [Agent Loop](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#agent-loop)
    * [Prompt System](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#prompt-system)
    * [Provider Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#provider-resolution)
    * [Tool System](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#tool-system)
    * [Session Persistence](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#session-persistence)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#messaging-gateway)
    * [Plugin System](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#plugin-system)
    * [Cron](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#cron)
    * [ACP Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#acp-integration)
    * [Trajectories](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#trajectories)
  * [Design Principles](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#design-principles)
  * [File Dependency Chain](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture#file-dependency-chain)


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
