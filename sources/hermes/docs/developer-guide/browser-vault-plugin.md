---
title: "Browser Vault Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin
scraped_at: 2026-11-07T17:20:20.155347+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/browser-vault-plugin)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Browser Vault Plugins


On this page
# Browser Vault Plugins
A plugin can add a password manager (KeePass, a team vault, a hardware-backed store) as a login source for the `browser_vault` tool, when it comes from a verified source: the manager's vendor through the plugin catalog, or Nous (see [Who can register a backend](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#who-can-register-a-backend)). The agent then lists and fills that manager's logins the same way it does for the built-in Hermes vault, 1Password and Bitwarden: it sees handles and metadata, never a password.
Browser login backends are separate from [secret sources](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin). A `SecretSource` registration does not make a password manager available to `browser_vault`.
## Registering a backend[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#registering-a-backend "Direct link to Registering a backend")
An **in-process** plugin subclasses `agent.vault_backends.base.LoginBackend` and registers one instance:

```


from agent.vault_backends.base import LoginBackend  





from agent.vault_store import VaultItemMeta  





  





  





class KeePassBackend(LoginBackend):  





    name = "keepass"            # lowercase identifier; also the config key  





    prefix = "keepass:"         # must be exactly "<name>:"  





    display_name = "KeePass"  





  





    def list_items(self) -> list[VaultItemMeta]:  





        ...  # metadata only: ids "keepass:<opaque>", exact HTTPS origins, identifier  





  





    def get_meta(self, handle: str) -> VaultItemMeta | None:  





        ...  





  





    def resolve_password(self, handle: str) -> str:  





        ...  # called once per fill, after the page origin matched the item  





  





  





def register(ctx):  





    ctx.register_login_backend(KeePassBackend())  



```

The backend stays off until the user turns it on for the profile:

```


vault:  





  keepass:  





    enabled: true   # exactly true; installed code is never enabled automatically  



```

Construct the backend without fetching credentials or reading profile state, and read the active profile's configuration lazily. Registration is profile-scoped and removed when the plugin unloads.
## Who can register a backend[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#who-can-register-a-backend "Direct link to Who can register a backend")
Password-manager integrations come only from verified sources. `ctx.register_login_backend` is accepted from:
  * a plugin bundled with Hermes, or
  * a plugin installed from the [Hermes plugin catalog](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/catalog-submission) at `tier: verified` (published by the password-manager vendor itself) or `tier: official` (maintained by Nous), at the catalog's reviewed pin.


Every other plugin is refused at registration with a log line naming this rule: a plugin dropped into `~/.hermes/plugins/` by hand, a Git URL install, a community-tier catalog entry, a catalog install moved off its pin with `--ref`, one installed with `--allow-removed`, a project plugin and a pip entry-point plugin. Provenance is read from Hermes's own install record (`plugins/.install-metadata.json`, written by the installer), never from a file inside the plugin, so a repository that ships its own `.hermes-catalog.json` gains nothing. No config key relaxes the rule.
If you build a password manager and want it in Hermes, submit the plugin to the catalog from your own repository and ask for `verified` tier (catalog admission rule 18). Integrations for managers whose vendor has not published one come from Nous as `official` entries.
## Isolation rules[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#isolation-rules "Direct link to Isolation rules")
Hermes wraps every plugin backend in a core-owned adapter before the vault tool sees it. These rules hold however the plugin implements its class:  
| Rule  | What it means for your backend  |  
| --- | --- |  
| **Own namespace only**  | Your handles are `<name>:…`. Hermes decides ownership from the registered name, so it never calls your `owns()` and never passes you a `vault_…` (Hermes vault), `op:…`, `bw:…` or another plugin's handle. Items your `list_items()` returns with an id outside your namespace are dropped, and a `get_meta()` answer whose id is not the requested handle is ignored.  |  
| **Handle in, value out**  |  `list_items()` gets no arguments; `get_meta()`, `resolve_password()`, `resolve_otp()` and `resolve_secret()` get your handle and nothing else. You never receive the page, the CDP/browser session, the task, other vault entries, or decrypted values from any other backend.  |  
| **No master-password prompt**  | Hermes' unlock prompt is reserved for built-in managers. A backend with `needs_unlock = True` is refused at registration, and a plugin backend is never offered the `unlock` action, so the user is never asked to type a master password into a dialog a plugin labelled. Authenticate through your manager's own agent, session or OS keychain.  |  
| **Reserved namespaces**  | The names `local`, `onepassword`, `bitwarden`, `vault`, `op` and `bw`, and any prefix inside a built-in prefix (`vault_x:`), are refused. So is a name another plugin already holds in the profile: no backend, built-in or plugin, can be replaced or shadowed. `name` and `prefix` must be plain string attributes, not properties, and the class may not override `__getattribute__` or `__class__`: Hermes judges the registration without running your code.  |  
| **Off by default**  | Only `vault.<name>.enabled: true` turns a backend on.  |  
| **In-process only**  |  `ctx.register_login_backend` is refused under `plugins.isolation: host`, because `fill_context()` is a server-local context manager.  |  
| **Same fill path**  | Plugin items (passwords and automatic one-time codes) go through the same exact-origin pre-check, in-page origin re-assertion, supervisor CDP secret evaluation (never argv) and payment confirmation as built-in items.  |  
| **Secrets stay out of the conversation**  | Values you return are registered with the browser-result redaction boundary before they reach the page. Any exception your backend raises is replaced by a fixed message (`The <name> login backend failed.`) before it can reach a tool result, a log line or an exception chain, so a secret in your error text cannot reach the model. A value of the wrong type is refused the same way. Hermes copies what you return (metadata fields, passwords, codes) into its own plain objects inside that same guard, so an error raised while a field is read gets the fixed message too.  |  
An in-process plugin is ordinary Python running inside Hermes, so these rules are an API contract, not a sandbox. They guarantee that Hermes never hands your backend another backend's data; they do not stop arbitrary code in the same process from reading files. The provenance rule above decides which plugins Hermes offers this seam to; it is not a sandbox either.
## Fill context[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#fill-context "Direct link to Fill context")
`fill_context()` defaults to a no-op. A backend may return its own context manager to lock fills and freeze credential-reference/origin configuration for the whole operation, so a reload cannot pair old metadata with a newly configured secret. Hermes enters it only for fills of your own handles (a password fill, and an automatic one-time code for `browser_vault action=enter_code`, both through the in-page write), and only after the page origin matched your item's `get_meta()`: a page on another origin never opens your context. Inside the context Hermes calls `get_meta()` again and refuses the fill unless the frozen item still binds that page origin, so the origins checked and the secret resolved come from one snapshot. It calls `fill_context()` with no arguments and exits it with `(None, None, None)`, so you never see the core's exception. Release on exit even when the fill failed. A fill lock does not serialize unrelated browser navigation.
## Writing errors[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#writing-errors "Direct link to Writing errors")
Raise exceptions with fixed diagnostics. Hermes discards your exception text, but your own logs may still record it, so never put credential values or secret-manager response bodies in it. Never expose a model-facing tool that returns a password: it would bypass every rule above.
## Browser page backends[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#browser-page-backends "Direct link to Browser page backends")
A plugin browser that has no CDP endpoint (Camofox talks to its own REST server) cannot be reached by the vault's supervisor, so `browser_vault` would refuse every fill with "Could not determine the current page origin". Such a plugin registers an `agent.browser_page_backend.BrowserPageBackend`:

```


from agent.browser_page_backend import BrowserPageBackend  





  





  





class MyBrowserPages(BrowserPageBackend):  





    name = "mybrowser"  





  





    def has_page(self, task_id: str) -> bool:  





        ...  # True when this task already has a live tab here; never open one to answer  





  





    def evaluate(self, task_id: str, expression: str, *, secret: bool):  





        ...  # run the script on that tab and return its value; raise on failure  





  





  





def register(ctx):  





    if hasattr(ctx, "register_browser_page_backend"):  # older cores lack the seam  





        ctx.register_browser_page_backend(MyBrowserPages())  



```

When `has_page(task_id)` is true, the vault reads the page origin, inspects the form and writes the password through `evaluate` instead of CDP. Everything else stays core's: the exact-origin pre-check and in-page re-check, payment confirmation, the Bot Desktop takeover check, redaction of the filled value. A secret-bearing script (`secret=True`) arrives wrapped so a page exception is answered in-page, and any failure on that path is reported with fixed text, so your exception never reaches the model. Send a secret script only over a transport that keeps it out of argv and off the network in clear text (loopback or HTTPS), never follow a redirect with it, and never log it.
The provenance rule above applies here too (bundled, or catalog `verified`/`official` at its pin), and the registration is refused under `plugins.isolation: host`, because the fill script carries the credential and must stay in the Hermes process.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/browser-vault-plugin.md)
[Previous Secret Source Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)[Next Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)
  * [Registering a backend](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#registering-a-backend)
  * [Who can register a backend](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#who-can-register-a-backend)
  * [Isolation rules](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#isolation-rules)
  * [Fill context](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#fill-context)
  * [Writing errors](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#writing-errors)
  * [Browser page backends](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin#browser-page-backends)


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
