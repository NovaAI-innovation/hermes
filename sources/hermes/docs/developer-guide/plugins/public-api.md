---
title: "Public plugin API"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api
scraped_at: 2026-11-07T17:20:29.124209+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/plugins/public-api)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Public plugin API


# Public plugin API
These are the Hermes modules and names a plugin may import. `hermes plugins validate` reads the same list (`hermes_cli/data/plugin_api.json`) and warns, without failing, on any other import of a Hermes module (catalog rule 9: public surfaces only). Imports of the standard library, third-party packages, the plugin's own modules, and imports under `if TYPE_CHECKING:` are never flagged.
A module row allows the module and every name in it that does not start with an underscore. A row with a name allows that one name only.  
| Module  | Name  | Listed from  |  
| --- | --- | --- |  
| `agent.account_usage`  | whole module  | developer-guide / plugins docs  |  
| `agent.acp_client`  | whole module  | developer-guide / plugins docs  |  
| `agent.browser_provider`  | whole module  | developer-guide / plugins docs  |  
| `agent.context_engine`  | whole module  | developer-guide / plugins docs  |  
| `agent.credential_pool`  | whole module  | developer-guide / plugins docs  |  
| `agent.delegation_backends`  | whole module  | developer-guide / plugins docs  |  
| `agent.delegation_provider`  | whole module  | developer-guide / plugins docs  |  
| `hermes_cli.auth_model_picker`  | `prompt_model_selection`  | developer-guide / plugins docs  |  
| `hermes_cli.auth`  | `resolve_external_process_provider_credentials`  | developer-guide / plugins docs  |  
| `hermes_cli.model_setup`  | whole module  | developer-guide / plugins docs  |  
| `agent.image_gen_provider`  | whole module  | developer-guide / plugins docs  |  
| `agent.memory_manager`  | whole module  | developer-guide / plugins docs  |  
| `agent.memory_provider`  | whole module  | developer-guide / plugins docs  |  
| `agent.secret_scope`  | whole module  | developer-guide / plugins docs  |  
| `agent.secret_sources.base`  | whole module  | developer-guide / plugins docs  |  
| `agent.subagent_lifecycle`  | whole module  | developer-guide / plugins docs  |  
| `agent.terminal_env_provider`  | whole module  | developer-guide / plugins docs  |  
| `agent.transports`  | whole module  | developer-guide / plugins docs  |  
| `agent.transports.chat_completions`  | whole module  | developer-guide / plugins docs  |  
| `agent.video_gen_provider`  | whole module  | developer-guide / plugins docs  |  
| `agent.web_search_provider`  | whole module  | developer-guide / plugins docs  |  
| `cli`  | whole module  | developer-guide / plugins docs  |  
| `gateway.config`  | whole module  | developer-guide / plugins docs  |  
| `gateway.platform_registry`  | whole module  | developer-guide / plugins docs  |  
| `gateway.platforms._shared`  | whole module  | developer-guide / plugins docs  |  
| `gateway.platforms.base`  | whole module  | developer-guide / plugins docs  |  
| `gateway.platforms.event`  | whole module  | developer-guide / plugins docs  |  
| `gateway.platforms.helpers`  | whole module  | developer-guide / plugins docs  |  
| `gateway.status`  | whole module  | developer-guide / plugins docs  |  
| `hermes_cli.auth_oauth_pkce_plugin`  | whole module  | developer-guide / plugins docs  |  
| `hermes_cli.config`  | whole module  | developer-guide / plugins docs  |  
| `hermes_cli.plugin_events`  | whole module  | developer-guide / plugins docs  |  
| `hermes_cli.plugin_provider_requests`  | whole module  | developer-guide / plugins docs  |  
| `hermes_constants`  | whole module  | developer-guide / plugins docs  |  
| `hermes_platform`  | whole module  | developer-guide / plugins docs  |  
| `hermes_state`  | whole module  | developer-guide / plugins docs  |  
| `plugins.plugin_storage`  | whole module  | developer-guide / plugins docs  |  
| `plugins.plugin_utils`  | whole module  | developer-guide / plugins docs  |  
| `pm`  | whole module  | developer-guide / plugins docs  |  
| `providers`  | whole module  | developer-guide / plugins docs  |  
| `providers.base`  | whole module  | developer-guide / plugins docs  |  
| `tools.browser_supervisor`  | whole module  | developer-guide / plugins docs  |  
| `tools.browser_supervisor_capture`  | whole module  | developer-guide / plugins docs  |  
| `tools.computer_use.backend`  | whole module  | developer-guide / plugins docs  |  
| `tools.registry`  | whole module  | developer-guide / plugins docs  |  
| `agent.context_references`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `agent.plugin_llm`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `agent.transcription_provider`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `agent.tts_provider`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `cron.execution_identity`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `hermes_cli.dashboard_auth`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `hermes_cli.platform_actions`  | whole module  | PluginContext (hermes_cli/plugins_context.py)  |  
| `hermes_cli.plugins`  | `PluginContext`  | PluginContext (hermes_cli/plugins_context.py)  |  
| `hermes_cli.plugins_ledger`  | `PluginRegistration`  | PluginContext (hermes_cli/plugins_context.py)  |  
| `hermes_cli.plugins_state`  | `PluginState`  | PluginContext (hermes_cli/plugins_context.py)  |  
| `agent.runtime_cwd`  | `resolve_agent_cwd`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `agent.usage_pricing`  | `CostResult`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `hermes_cli.auth_constants`  | `AuthError`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `tools.environments.base`  | `BaseEnvironment`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `tools.environments`  | `BaseEnvironment`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `utils`  | `atomic_json_write`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `utils`  | `read_json_or_empty`  | prose in memory-provider / model-provider / terminal-environment plugin pages (tools.environments:BaseEnvironment is the package's `__all__` re-export)  |  
| `gateway.platforms.access_policy_mixin`  | `OwnAccessPolicyMixin`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.approval`  | `resolve_gateway_approval`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.approval`  | `resolve_gateway_approval_card`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.clarify_gateway`  | `get_pending`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.clarify_gateway`  | `resolve_gateway_clarify`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.clarify_gateway`  | `mark_awaiting_text`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.clarify_gateway`  | `SKIPPED`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.url_safety`  | `is_safe_url`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.url_safety`  | `create_ssrf_safe_async_client`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `gateway.platforms._http_client_limits`  | `platform_httpx_limits`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.gateway_setup_wizard`  | `print_setup_header`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.gateway_setup_wizard`  | `confirm_reconfigure`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.gateway_setup_wizard`  | `offer_home_channel`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.gateway_setup_wizard`  | `save_env_values`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.gateway_setup_wizard`  | `prompt_csv`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.setup`  | `prompt`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.setup`  | `prompt_choice`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.setup`  | `prompt_yes_no`  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `hermes_cli.cli_output`  | whole module  | adding-platform-adapters.md § Public helpers for platform plugins  |  
| `tools.skills_tool`  | `find_all_skills`  | plugins/index.md § Read the skill catalog  |  
| `tools.skills_tool`  | `sort_skills`  | plugins/index.md § Read the skill catalog  |  
| `tools.skills_tool`  | `skill_search_dirs`  | plugins/index.md § Read the skill catalog  |  
| `tools.skills_tool`  | `locate_skill`  | plugins/index.md § Read the skill catalog  |  
| `tools.skills_tool`  | `skill_lookup_path_error`  | plugins/index.md § Read the skill catalog  |  
| `tools.skills_sync`  | `dir_hash`  | plugins/index.md § Read the skill catalog  |  
| `tools.skill_usage`  | `read_skill_name`  | plugins/index.md § Read the skill catalog  |  
| `gateway.session_context`  | `get_session_env`  | plugins/index.md § platform plugins: read session identity through the task-local context  |  
| `agent.redact`  | `redact_sensitive_text`  | plugin-llm-access.md § From the plugin's frontend: a plugin RPC method (`force=True` where secrets must never leave)  |  
| `hermes_cli.plugin_session`  | `session_client`  | user-guide/features/plugins.md § Plugin code inside the gateway: which client created the session  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/plugins/public-api.md)
[Previous Catalog submission](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/catalog-submission)[Next Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
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
