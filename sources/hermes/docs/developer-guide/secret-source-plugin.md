---
title: "Secret Source Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin
scraped_at: 2026-11-07T17:20:29.130502+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/secret-source-plugin)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Secret Source Plugins


On this page
# Building a Secret Source Plugin
Secret sources resolve provider credentials from an external secret manager (a vault, a password manager, an OS keystore, a custom script) into environment variables at process startup — after `~/.hermes/.env` loads, before Hermes reads credentials. Bitwarden, 1Password, and a generic command-helper source ship in-tree; **every other backend is a plugin**. This guide covers building one.
The bundled set is deliberately closed, same policy as [memory providers](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin): PRs adding new vault backends under `agent/secret_sources/` are closed with a pointer to this guide. Publish your backend as a standalone plugin repo and share it in the Nous Research Discord (`#plugins-skills-and-skins`).
## First-process bootstrap timing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#first-process-bootstrap-timing "Direct link to First-process bootstrap timing")
`load_hermes_dotenv()` often runs at import time **before** plugins register. Hermes then re-pulls secrets after plugin discovery when any **enabled** plugin secret source is configured. Enablement uses the source's `is_enabled(cfg)` contract; the standard form is `secrets.<name>.enabled: true`, while custom activation remains supported. That closes the "replace Bitwarden with my vault" first-process gap (#64177).
  * Re-pull is idempotent and fail-open (never blocks startup).
  * `hermes update` never resolves external sources — not in the updater process and not in the import-health probes it spawns. Nothing in the update path needs credentials, and a slow helper would otherwise be misreported as an import failure (#110823).
  * Sources only supply env vars through the orchestrator; there is **no** plugin API to dump other plugins' or the user's entire secret store beyond what your source's own config allows.
  * Reading `os.environ` after load is possible for any in-process code — the trust boundary remains "enabled plugins run with agent privilege".


## What the framework owns vs. what you own[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#what-the-framework-owns-vs-what-you-own "Direct link to What the framework owns vs. what you own")
The orchestrator (`agent.secret_sources.registry.apply_all`) owns everything security- and precedence-sensitive, so a backend cannot get it wrong:  
| Framework owns  | You own  |  
| --- | --- |  
| Source ordering, mapped-vs-bulk precedence  | Fetching values from your backend  |  
| First-claim-wins conflict handling + warnings  | Validating your reference format  |  
|  `override_existing` semantics (never crosses sources)  | Talking to your CLI/SDK/API  |  
| Protected bootstrap tokens  | Declaring which env var IS your bootstrap token  |  
| Per-source wall-clock timeout  | Keeping `fetch()` reasonably fast  |  
| Per-var provenance + `(from X)` labels  | A human-readable `label`  |  
|  `os.environ` writes  | Nothing — you never touch the environment  |  
## Directory structure[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#directory-structure "Direct link to Directory structure")

```


~/.hermes/plugins/my-vault/  





├── plugin.yaml      # name, description  





└── __init__.py      # SecretSource subclass + register(ctx)  



```

## The SecretSource ABC[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#the-secretsource-abc "Direct link to The SecretSource ABC")
Implement `agent.secret_sources.base.SecretSource`. One method is required:

```


from pathlib import Path  





  





from agent.secret_sources.base import (  





    ErrorKind,  





    FetchResult,  





    SecretSource,  





    run_secret_cli,  





)  





  





  





class MyVaultSource(SecretSource):  





    name = "myvault"          # config section key: secrets.myvault  





    label = "My Vault"        # used in startup lines + provenance labels  





    shape = "mapped"          # "mapped" (explicit VAR→ref map) or "bulk" (project dump)  





    scheme = "mv"             # optional: unique URI scheme you own (mv://...)  





  





    def fetch(self, cfg: dict, home_path: Path) -> FetchResult:  





        """Resolve secrets. MUST NOT raise. MUST NOT prompt."""  





        result = FetchResult()  





        token = os.environ.get("MYVAULT_TOKEN", "").strip()  





        if not token:  





            result.error = "secrets.myvault.enabled is true but MYVAULT_TOKEN is not set."  





            result.error_kind = ErrorKind.NOT_CONFIGURED  





            return result  





  





        try:  





            proc = run_secret_cli(  





                ["myvault-cli", "export", "--json"],  





                allow_env=["MYVAULT_TOKEN"],   # ONLY your auth vars — never full os.environ  





                timeout=30,  





            )  





        except RuntimeError as exc:           # spawn failure / timeout  





            result.error = str(exc)  





            result.error_kind = ErrorKind.BINARY_MISSING  





            return result  





  





        if proc.returncode != 0:  





            result.error = f"myvault-cli exited {proc.returncode}: {proc.stderr[:200]}"  





            result.error_kind = ErrorKind.AUTH_FAILED  





            return result  





  





        result.secrets = parse_your_output(proc.stdout)  # {ENV_VAR: value}  





        return result  





  





    def protected_env_vars(self, cfg: dict):  





        # Your bootstrap token — no source (including yours) may ever overwrite it.  





        return frozenset({"MYVAULT_TOKEN"})  



```

### Contract rules (enforced, not suggestions)[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#contract-rules-enforced-not-suggestions "Direct link to Contract rules \(enforced, not suggestions\)")
  * **`fetch()`never raises.** Errors go in `result.error` + `result.error_kind`. A raising fetch is contained by the orchestrator and reported as `INTERNAL` — a contract violation, not a feature.
  * **`fetch()`never prompts.** Startup runs in non-TTY contexts (gateway, cron, Docker). `run_secret_cli()` closes stdin so a prompting helper fails fast. Interactive auth belongs in your CLI setup flow, never on the startup path.
  * **Sync, within budget.** The orchestrator enforces a wall-clock timeout (default 120s, user-tunable via `secrets.<name>.timeout_seconds`). Exceeding it reports `TIMEOUT` and your result is discarded.
  * **You fetch; the orchestrator applies.** Return the mapping you _would_ contribute. Never write `os.environ` yourself — you'd bypass precedence, conflict detection, and provenance.
  * **API versioning.** `SecretSource.api_version` defaults to the current `SECRET_SOURCE_API_VERSION`. The registry skips (with a warning) sources built against a different version instead of crashing startup.


### Choosing your `shape`[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#choosing-your-shape "Direct link to choosing-your-shape")
  * `mapped` — the user explicitly binds env-var names to references in config (like 1Password's `env:` map). Strongest intent: mapped claims beat bulk claims on contested vars.
  * `bulk` — you inject a whole project/folder of secrets implicitly (like Bitwarden BSM). Yields to mapped sources.


### Optional hooks[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#optional-hooks "Direct link to Optional hooks")  
| Method  | Default  | Override when  |  
| --- | --- | --- |  
| `is_enabled(cfg)`  | `cfg.get("enabled")`  | Custom activation logic  |  
| `override_existing(cfg)`  | `cfg.get("override_existing", False)`  | You want a different default (both bundled sources default `True` for rotation)  |  
| `protected_env_vars(cfg)`  | empty  | You have a bootstrap token (you almost certainly do)  |  
| `fetch_timeout_seconds(cfg)`  | 120s  | Your backend needs a different budget  |  
| `config_schema()`  | `{}`  | Declare config keys for setup surfaces  |  
| `remediation(kind, cfg)`  | generic per-`ErrorKind` hints  | You want failure warnings to point at your own fix-it command (e.g. the bundled sources return `Run hermes secrets <name> token…` for `AUTH_FAILED`). Must be a pure kind→string mapping: no I/O, never raises. Return `""` to suppress the hint.  |  
## Subprocess safety: use `run_secret_cli()`[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#subprocess-safety-use-run_secret_cli "Direct link to subprocess-safety-use-run_secret_cli")
If your backend shells out to a CLI, use the shared helper instead of `subprocess.run` directly. It gives you the audited posture for free: argv-only (no `shell=True`), a **minimal allowlisted child environment** (by the time sources run, `os.environ` holds every credential Hermes knows — never hand that to a child process), `NO_COLOR` + ANSI-scrubbed stderr, stdin closed, timeout → clean `RuntimeError`. Pass user-supplied reference strings after a `--` terminator in your argv so they can never parse as flags.
## Registering[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#registering "Direct link to Registering")

```


# __init__.py  





def register(ctx):  





    ctx.register_secret_source(MyVaultSource())  



```

Registration is rejected (with a log warning, never a crash) for: non-`SecretSource` instances, invalid/duplicate names, a `scheme` another source owns, wrong `api_version`, or a `shape` outside `mapped`/`bulk`.
Plugin discovery runs later in startup than the first `load_hermes_dotenv()` call. Immediately after discovery, Hermes re-pulls enabled plugin secret sources (`reset_secret_source_cache()` + `load_hermes_dotenv()`), so the discovering process _does_ pick them up — see [First-process bootstrap timing](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#first-process-bootstrap-timing) above (#64177). The re-pull is fail-open and skipped when no plugin source is enabled. Any code that reads `os.environ` during the plugin module's import or `register(ctx)` still runs before the re-pull and cannot depend on credentials supplied by that same source; keep credentialed work inside `fetch()`. Gateway, cron, and subagent processes perform the same discovery/re-pull sequence. The re-pull (and the per-fire cron re-pull) resets only the resolving home's cache, so under a multiplex gateway sibling profiles keep their hydrated snapshots; and a re-pull whose keys already sit in the process environment (`skipped_existing`, e.g. the previous apply's own write-back) still records the home's effective values, so `override_existing` is never required just to survive a re-pull.
## Users configure it like any other source[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#users-configure-it-like-any-other-source "Direct link to Users configure it like any other source")

```


secrets:  





  sources: [myvault, bitwarden]   # optional ordering  





  myvault:  





    enabled: true  





    # ... your config_schema keys  



```

Multi-source precedence, conflict warnings, and `(from My Vault)` provenance labels all work automatically — see the [user-facing secrets docs](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/) for the precedence ladder.
## Validate with the conformance kit[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#validate-with-the-conformance-kit "Direct link to Validate with the conformance kit")
Subclass the kit from the Hermes repo (`tests/secret_sources/conformance.py`) in your plugin's tests:

```


import pytest  





from tests.secret_sources.conformance import SecretSourceConformance  





  





class TestMyVaultConformance(SecretSourceConformance):  





    @pytest.fixture  





    def source(self):  





        return MyVaultSource()  



```

It checks the rules that break other people when violated: never-raises on malformed config, machine-readable error kinds, disabled-by-default, positive timeouts, valid protected-var names, and a full `apply_all()` round trip. Green conformance is the review bar for calling a backend contract-compliant.
## ErrorKind reference[​](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#errorkind-reference "Direct link to ErrorKind reference")  
| Kind  | Meaning  |  
| --- | --- |  
| `NOT_CONFIGURED`  | Enabled but missing token / project / map  |  
| `BINARY_MISSING`  | Helper CLI not found or not executable  |  
|  `AUTH_FAILED` / `AUTH_EXPIRED`  | Bad / expired credentials  |  
| `REF_INVALID`  | A secret reference failed validation  |  
| `NETWORK`  | Transport-level failure  |  
| `EMPTY_VALUE`  | Backend returned nothing for a ref — never apply `""` over a good credential  |  
| `TIMEOUT`  | Fetch exceeded its budget  |  
| `INTERNAL`  | Anything else (bug, unexpected shape)  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/secret-source-plugin.md)
[Previous Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin)[Next Browser Vault Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
  * [First-process bootstrap timing](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#first-process-bootstrap-timing)
  * [What the framework owns vs. what you own](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#what-the-framework-owns-vs-what-you-own)
  * [Directory structure](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#directory-structure)
  * [The SecretSource ABC](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#the-secretsource-abc)
    * [Contract rules (enforced, not suggestions)](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#contract-rules-enforced-not-suggestions)
    * [Choosing your `shape`](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#choosing-your-shape)
    * [Optional hooks](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#optional-hooks)
  * [Subprocess safety: use `run_secret_cli()`](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#subprocess-safety-use-run_secret_cli)
  * [Registering](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#registering)
  * [Users configure it like any other source](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#users-configure-it-like-any-other-source)
  * [Validate with the conformance kit](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#validate-with-the-conformance-kit)
  * [ErrorKind reference](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin#errorkind-reference)


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
