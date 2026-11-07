---
title: "Browser Provider Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin
scraped_at: 2026-11-07T17:20:20.153343+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/browser-provider-plugin)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Browser Provider Plugins


On this page
# Building a Browser Provider Plugin
Browser provider plugins register a **cloud browser backend** : when `browser.cloud_provider` selects it, `browser_exec` (and the CDP tools `browser_cdp`, `browser_dialog`, `browser_vault`) drive a remote browser session it creates instead of a local Chromium. Built-in providers — Browserbase, Browser Use, and Firecrawl — all ship as plugins under `plugins/browser/<name>/`. You can add a new one, or override a bundled one, by dropping a directory next to them.
Browser backends are one of several **backend plugins** Hermes supports. The others (with their own ABCs) are [Web Search Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/web-search-provider-plugin) (which this ABC deliberately mirrors), [Image Generation](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin), [Video Generation](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin), [Memory Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin), [Context Engines](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin), [Secret Sources](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin), and [Model Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin). General tool/hook/CLI plugins live in [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins).
## How it fits together[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#how-it-fits-together "Direct link to How it fits together")
A browser provider does **not** implement browsing. It implements **session lifecycle** : create a remote browser session, hand back a CDP websocket URL, and tear the session down. Hermes hands the CDP URL you return to `browser_exec`, which drives the page from there — every provider gets the full browser toolset (`browser_exec`, `browser_cdp`, `browser_dialog`, `browser_vault`) for free.
The active provider is selected by `browser.cloud_provider` in `config.yaml`; the resolver in `tools/browser_session_cloud.py` is a pure registry lookup with no per-provider conditionals.
## Discovery[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#discovery "Direct link to Discovery")
Hermes scans for browser backends in three places:
  1. **Bundled** — `<repo>/plugins/browser/<name>/` (auto-loaded with `kind: backend`)
  2. **User** — `~/.hermes/plugins/browser/<name>/` (opt-in via `plugins.enabled` or `hermes plugins enable <name>`)
  3. **Pip** — packages declaring a `hermes_agent.plugins` entry point


Each plugin's `register(ctx)` calls `ctx.register_browser_provider(...)`, which puts the instance into the registry in `agent/browser_registry.py`.
## Directory structure[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#directory-structure "Direct link to Directory structure")

```


plugins/browser/my-backend/  





├── __init__.py     # register() entry point  





├── provider.py     # BrowserProvider subclass  





└── plugin.yaml     # Manifest with kind: backend and provides_browser_providers  



```

`plugin.yaml`:

```


name: browser-my-backend  





version: 1.0.0  





description: "My cloud browser backend. Requires MY_BACKEND_API_KEY."  





author: you  





kind: backend  





provides_browser_providers:  





  - my-backend  



```

`__init__.py`:

```


from plugins.browser.my_backend.provider import MyBackendProvider  





  





  





def register(ctx) -> None:  





    ctx.register_browser_provider(MyBackendProvider())  



```

## The BrowserProvider ABC[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#the-browserprovider-abc "Direct link to The BrowserProvider ABC")
Implement `agent.browser_provider.BrowserProvider`. Three lifecycle methods plus identity:

```


from agent.browser_provider import BrowserProvider  





  





  





class MyBackendProvider(BrowserProvider):  





    @property  





    def name(self) -> str:  





        return "my-backend"          # the browser.cloud_provider config value  





  





    @property  





    def display_name(self) -> str:  





        return "My Backend"          # shown in `hermes tools`  





  





    def is_available(self) -> bool:  





        """Cheap check only — env var present, dep importable.  





        NO network calls: runs at tool-registration time and on every  





        `hermes tools` paint."""  





        return bool(os.environ.get("MY_BACKEND_API_KEY"))  





  





    def create_session(self, task_id: str) -> dict:  





        """Create a remote browser session; return the session-metadata contract."""  





        session = my_api.create_browser(...)  





        return {  





            "session_name": f"my-backend-{task_id}",  # unique session name  





            "bb_session_id": session.id,              # provider session ID (for cleanup)  





            "cdp_url": session.cdp_ws_url,            # CDP websocket URL  





            "features": {"stealth": True},            # feature flags you enabled  





        }  





  





    def close_session(self, session_id: str) -> bool:  





        """Terminate by provider session ID. Log-and-return-False on error —  





        never raise, so the dispatcher's cleanup loop keeps moving."""  





        ...  





  





    def emergency_cleanup(self, session_id: str) -> None:  





        """Best-effort teardown from atexit/signal handlers. Must not raise."""  





        ...  



```

### The session-metadata contract[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#the-session-metadata-contract "Direct link to The session-metadata contract")
`create_session()` must return at least `session_name`, `bb_session_id`, `cdp_url`, and `features`. Two quirks worth knowing:
  * **`bb_session_id`is a legacy key name** kept verbatim for backward compatibility with the browser session code — it holds _your_ provider's session ID regardless of vendor. Don't rename it.
  * `create_session()` **may raise** — `ValueError` for missing credentials, `RuntimeError` for network/API failures. The dispatcher surfaces these to the user. This differs from `close_session`/`emergency_cleanup`, which must never raise.


An optional `external_call_id` key supports managed-gateway billing.
###  `get_setup_schema()` — the `hermes tools` picker row[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#get_setup_schema--the-hermes-tools-picker-row "Direct link to get_setup_schema--the-hermes-tools-picker-row")
Override this to appear as a first-class option in the Browser Automation picker with API-key prompts (an optional `post_setup` key names an install hook to run after selection):

```


def get_setup_schema(self) -> dict:  





    return {  





        "name": "My Backend",  





        "badge": "paid",  





        "tag": "Cloud browser with stealth and proxies",  





        "env_vars": [  





            {"key": "MY_BACKEND_API_KEY",  





             "prompt": "My Backend API key",  





             "url": "https://mybackend.example"},  





        ],  





    }  



```

Per the project standard for tool backends: if a backend can't be selected and configured through `hermes tools`, it isn't done — "set this env var manually" is not an integration.
## Users configure it[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#users-configure-it "Direct link to Users configure it")

```


browser:  





  cloud_provider: my-backend  



```

## Reference implementations[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#reference-implementations "Direct link to Reference implementations")
The three bundled providers under `plugins/browser/` are the canonical examples, in ascending complexity: `firecrawl` (simplest), `browser_use`, and `browserbase` (stealth/proxy/keep-alive feature flags with graceful fallback when paid features are unavailable). Copy the closest one.
## Checklist[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#checklist "Direct link to Checklist")
  * `name` is lowercase and stable (it's a config value users write)
  * `is_available()` makes zero network calls
  * `create_session()` returns the full metadata contract (`bb_session_id` key name intact)
  * `close_session()` / `emergency_cleanup()` never raise
  * `get_setup_schema()` exposes your env vars so `hermes tools` can configure the backend
  * `plugin.yaml` declares `kind: backend` + `provides_browser_providers`


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/browser-provider-plugin.md)
[Previous Web Search Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/web-search-provider-plugin)[Next Terminal Environment Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [How it fits together](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#how-it-fits-together)
  * [Discovery](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#discovery)
  * [Directory structure](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#directory-structure)
  * [The BrowserProvider ABC](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#the-browserprovider-abc)
    * [The session-metadata contract](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#the-session-metadata-contract)
    * [`get_setup_schema()` — the `hermes tools` picker row](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#get_setup_schema--the-hermes-tools-picker-row)
  * [Users configure it](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#users-configure-it)
  * [Reference implementations](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#reference-implementations)
  * [Checklist](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin#checklist)


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
