---
title: "Provider Runtime"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime
scraped_at: 2026-11-07T17:20:20.141286+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/provider-runtime)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
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
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Architecture
  * Provider Runtime Resolution


On this page
# Provider Runtime Resolution
Hermes has a shared provider runtime resolver used across:
  * CLI
  * gateway
  * cron jobs
  * ACP
  * auxiliary model calls


Primary implementation:
  * `hermes_cli/runtime_provider.py` — credential resolution, custom-endpoint runtime resolution
  * `hermes_cli/auth.py` — provider registry, `resolve_provider()`
  * `hermes_cli/model_switch.py` — shared `/model` switch pipeline (CLI + gateway)
  * `agent/auxiliary_client.py` — auxiliary model routing
  * `providers/` — ABC + registry entry points (`ProviderProfile`, `register_provider`, `get_provider_profile`, `list_providers`)
  * `plugins/model-providers/<name>/` — per-provider plugins (bundled) that declare `api_mode`, `base_url`, `env_vars`, `fallback_models` and register themselves into the registry on first access. User plugins at `$HERMES_HOME/plugins/model-providers/<name>/` override bundled ones of the same name.


`get_provider_profile()` in `providers/` returns a `ProviderProfile` for a given provider id. `runtime_provider.py` calls this at resolution time to get the canonical `base_url`, `env_vars` priority list, `api_mode`, and `fallback_models` without needing to duplicate that data in multiple files. Adding a new plugin under `plugins/model-providers/<your-provider>/` (or `$HERMES_HOME/plugins/model-providers/<your-provider>/`) that calls `register_provider()` is enough for `runtime_provider.py` to pick it up — no branch needed in the resolver itself.
If you are trying to add a new first-class inference provider, read [Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers) and the [Model Provider Plugin guide](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin) alongside this page.
## Chat-completions reasoning shapes[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#chat-completions-reasoning-shapes "Direct link to Chat-completions reasoning shapes")
OpenAI-compatible relays can return `reasoning` or `reasoning_content` as strings, text-part dictionaries, or lists of text parts and string fragments. Hermes flattens these fields before string operations in the main stream, Relay recording, synchronous and asynchronous auxiliary streams, and completed-response reasoning extraction. Fragments retain their explicit whitespace; normalization adds no intra-field separator. Main-stream and Relay recording retain the existing paragraph breaks between complete bold reasoning headings. Reasoning stays separate from the visible answer.
`delta.reasoning_details` is a list of opaque provider records. Both the main stream and Relay recording append these records in arrival order without flattening, merging, or rewriting their contents. Providers can emit complete records on the final delta or across multiple deltas; omit the field on chunks without new records. The collected records pass through response normalization and assistant-message storage into session replay, including nested signed payloads.
## Resolution precedence[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#resolution-precedence "Direct link to Resolution precedence")
At a high level, provider resolution uses:
  1. explicit CLI/runtime request
  2. `config.yaml` model/provider config
  3. environment variables
  4. provider-specific defaults or auto resolution


That ordering matters because Hermes treats the saved model/provider choice as the source of truth for normal runs. This prevents a stale shell export from silently overriding the endpoint a user last selected in `hermes model`.
## Providers[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#providers "Direct link to Providers")
Current provider families include (see `plugins/model-providers/` for the complete bundled set):
  * AI Gateway (Vercel)
  * OpenRouter
  * Nous Portal
  * OpenAI Codex
  * Anthropic (native)
  * Google / Gemini (`gemini`)
  * Alibaba / DashScope (`alibaba`, `alibaba-coding-plan`)
  * DeepSeek
  * Z.AI
  * Kimi / Moonshot (`kimi-coding`, `kimi-coding-cn`)
  * MiniMax (`minimax`, `minimax-cn`, `minimax-oauth`)
  * Kilo Code
  * Hugging Face
  * OpenCode Zen / OpenCode Go
  * AWS Bedrock
  * Azure Foundry
  * NVIDIA NIM
  * xAI (Grok)
  * Arcee
  * GMI Cloud
  * StepFun
  * Qwen OAuth
  * Xiaomi
  * Ollama Cloud
  * LM Studio
  * Tencent TokenHub
  * Custom (`provider: custom`) — first-class provider for any OpenAI-compatible endpoint
  * Named custom providers (`providers:` dict in config.yaml; the legacy `custom_providers` list is still read for backward compatibility)


## Output of runtime resolution[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#output-of-runtime-resolution "Direct link to Output of runtime resolution")
The runtime resolver returns data such as:
  * `provider`
  * `api_mode`
  * `base_url`
  * `api_key`
  * `source`
  * provider-specific metadata like expiry/refresh info


## Why this matters[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#why-this-matters "Direct link to Why this matters")
This resolver is the main reason Hermes can share auth/runtime logic between:
  * `hermes chat`
  * gateway message handling
  * cron jobs running in fresh sessions
  * ACP editor sessions
  * auxiliary model tasks


## AI Gateway[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#ai-gateway "Direct link to AI Gateway")
Set `AI_GATEWAY_API_KEY` in `~/.hermes/.env` and run with `--provider ai-gateway`. Hermes fetches available models from the gateway's `/models` endpoint, filtering to language models with tool-use support.
## OpenRouter, AI Gateway, and custom OpenAI-compatible base URLs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#openrouter-ai-gateway-and-custom-openai-compatible-base-urls "Direct link to OpenRouter, AI Gateway, and custom OpenAI-compatible base URLs")
Hermes contains logic to avoid leaking the wrong API key to a custom endpoint when multiple provider keys exist (e.g. `OPENROUTER_API_KEY`, `AI_GATEWAY_API_KEY`, and `OPENAI_API_KEY`).
Each provider's API key is scoped to its own base URL:
  * `OPENROUTER_API_KEY` is only sent to `openrouter.ai` endpoints
  * `AI_GATEWAY_API_KEY` is only sent to `ai-gateway.vercel.sh` endpoints
  * `OPENAI_API_KEY` is used for custom endpoints and as a fallback


Hermes also distinguishes between:
  * a real custom endpoint selected by the user
  * the OpenRouter fallback path used when no custom endpoint is configured


That distinction is especially important for:
  * local model servers
  * non-OpenRouter/non-AI Gateway OpenAI-compatible APIs
  * switching providers without re-running setup
  * config-saved custom endpoints that should keep working even when `OPENAI_BASE_URL` is not exported in the current shell


## Native Anthropic path[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#native-anthropic-path "Direct link to Native Anthropic path")
Anthropic is not just "via OpenRouter" anymore.
When provider resolution selects `anthropic`, Hermes uses:
  * `api_mode = anthropic_messages`
  * the native Anthropic Messages API
  * `agent/anthropic_adapter.py` for translation


Credential resolution for native Anthropic now prefers refreshable Claude Code credentials over copied env tokens when both are present. In practice that means:
  * Claude Code credential files are treated as the preferred source when they include refreshable auth
  * manual `ANTHROPIC_TOKEN` / `CLAUDE_CODE_OAUTH_TOKEN` values still work as explicit overrides
  * Hermes preflights Anthropic credential refresh before native Messages API calls
  * Hermes still retries once on a 401 after rebuilding the Anthropic client, as a fallback path


## OpenAI Codex path[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#openai-codex-path "Direct link to OpenAI Codex path")
Codex uses a separate Responses API path:
  * `api_mode = codex_responses`
  * dedicated credential resolution and auth store support
  * a resumed session whose lingering Codex reasoning items (`encrypted_content`) are rejected — as a 400 `invalid_encrypted_content` or as a 401 `token_expired` — self-heals by stripping the cached items and replaying once, before any credential refresh or pool rotation. Reasoning minted after that strip keeps replaying; only a second rejection in the same session turns replay off


## Auxiliary model routing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#auxiliary-model-routing "Direct link to Auxiliary model routing")
Auxiliary tasks such as:
  * vision
  * context compression summaries
  * MCP helper operations
  * memory flushes


can use their own provider/model routing rather than the main conversational model.
When an auxiliary task is configured with provider `main`, Hermes resolves that through the same shared runtime path as normal chat. In practice that means:
  * env-driven custom endpoints still work
  * custom endpoints saved via `hermes model` / `config.yaml` also work
  * auxiliary routing can tell the difference between a real saved custom endpoint and the OpenRouter fallback


## Fallback models[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#fallback-models "Direct link to Fallback models")
Hermes supports a configured fallback provider chain — a list of `(provider, model)` entries tried in order when the primary model encounters errors. The legacy single-pair `fallback_model` dict is still accepted for back-compat (and migrated on first write).
### How it works internally[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#how-it-works-internally "Direct link to How it works internally")
  1. **Storage** : `AIAgent.__init__` stores the `fallback_model` dict and sets `_fallback_activated = False`.
  2. **Trigger points** : `_try_activate_fallback()` (forwarded to `try_activate_fallback()` in `agent/chat_completion_helpers.py`) is called from three places in the turn phases (`agent/turn_api_error.py`, `agent/turn_response_check.py`, `agent/turn_recovery.py`):
     * After max retries on invalid API responses (None choices, missing content)
     * On non-retryable client errors (HTTP 401, 403, 404)
     * After max retries on transient errors (HTTP 429, 500, 502, 503)
  3. **Activation flow** (`_try_activate_fallback`):
     * Returns `False` immediately if already activated or not configured
     * Calls `resolve_provider_client()` from `auxiliary_client.py` to build a new client with proper auth
     * Determines `api_mode`: `codex_responses` for openai-codex, `anthropic_messages` for anthropic, `chat_completions` for everything else
     * Swaps in-place: `self.model`, `self.provider`, `self.base_url`, `self.api_mode`, `self.client`, `self._client_kwargs`
     * For anthropic fallback: builds a native Anthropic client instead of OpenAI-compatible
     * Re-evaluates prompt caching (enabled for Claude models on OpenRouter)
     * Sets `_fallback_activated = True` — prevents firing again
     * Resets retry count to 0 and continues the loop
  4. **Config flow** :
     * CLI: reads the fallback chain via `hermes_cli/fallback_config.get_fallback_chain()` → passes to `AIAgent(fallback_model=...)`
     * Gateway: `gateway/run_config_loaders.py._load_fallback_model()` reads `config.yaml` → passes to `AIAgent`
     * Validation: both `provider` and `model` keys must be non-empty, or fallback is disabled


### What does NOT support fallback[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#what-does-not-support-fallback "Direct link to What does NOT support fallback")
  * **Subagent delegation** (`tools/delegate_tool.py`): subagents inherit the parent's provider but not the fallback config
  * **Auxiliary tasks** : use their own independent provider auto-detection chain (see Auxiliary model routing above)


Unpinned cron jobs **do** support fallback: `run_job()` reads `fallback_providers` (or legacy `fallback_model`) from `config.yaml` and passes it to `AIAgent(fallback_model=...)`, matching the gateway's `_load_fallback_model()` pattern. A job with its own `provider` / `model` / `base_url` gets no chain, the same rule as a pinned delegation child. See [Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals).
### Test coverage[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#test-coverage "Direct link to Test coverage")
Fallback behavior is exercised across several suites:
  * `tests/agent/test_fallback_credential_isolation.py` — credential isolation between primary and fallback
  * `tests/hermes_cli/test_fallback_cmd.py` — the `/fallback` CLI command


## Related docs[​](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#related-docs "Direct link to Related docs")
  * [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
  * [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
  * [Context Compression & Prompt Caching](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/provider-runtime.md)
[Previous State DB Recovery](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery)[Next Config Backend Seam](https://hermes-agent.nousresearch.com/docs/developer-guide/config-backend)
  * [Chat-completions reasoning shapes](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#chat-completions-reasoning-shapes)
  * [Resolution precedence](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#resolution-precedence)
  * [Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#providers)
  * [Output of runtime resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#output-of-runtime-resolution)
  * [Why this matters](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#why-this-matters)
  * [AI Gateway](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#ai-gateway)
  * [OpenRouter, AI Gateway, and custom OpenAI-compatible base URLs](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#openrouter-ai-gateway-and-custom-openai-compatible-base-urls)
  * [Native Anthropic path](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#native-anthropic-path)
  * [OpenAI Codex path](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#openai-codex-path)
  * [Auxiliary model routing](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#auxiliary-model-routing)
  * [Fallback models](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#fallback-models)
    * [How it works internally](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#how-it-works-internally)
    * [What does NOT support fallback](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#what-does-not-support-fallback)
    * [Test coverage](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#test-coverage)
  * [Related docs](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime#related-docs)


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
