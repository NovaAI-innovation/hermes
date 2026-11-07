---
title: "Secrets"
source: https://hermes-agent.nousresearch.com/docs/user-guide/secrets
scraped_at: 2026-11-07T17:19:30.383199+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/secrets)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/secrets/)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
    * [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
    * [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui)
    * [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)
    * [Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode)
    * [Windows (Native)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)
    * [Windows (WSL2)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-wsl-quickstart)
    * [Switching to a Source Install](https://hermes-agent.nousresearch.com/docs/user-guide/switching-to-source)
    * [Hermes Agent Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
    * [Which File Does What?](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
    * [Remote Config](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
    * [Configuring Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)
    * [Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/)
      * [Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/)
      * [Bitwarden Secrets Manager](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden)
      * [1Password](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/onepassword)
    * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/)
    * [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
    * [Session Storage Recovery](https://hermes-agent.nousresearch.com/docs/user-guide/session-storage-recovery)
    * [Profiles: Running Multiple Agents](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
    * [Profile Distributions: Share a Whole Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)
    * [Running Many Gateways at Once](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways)
    * [Connecting Desktop to Many Hermes Instances](https://hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop)
    * [Git Worktrees](https://hermes-agent.nousresearch.com/docs/user-guide/git-worktrees)
    * [Hermes Docker Setup](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
    * [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
    * [Checkpoints & Rollback](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Using Hermes
  * Secrets
  * Secrets


On this page
# Secrets
Hermes can pull API keys from external secret managers at process startup instead of storing them in `~/.hermes/.env`. The bootstrap token for the secret manager lives in `.env`; every other provider key (OpenAI, Anthropic, OpenRouter, etc.) can stay in the manager and rotate centrally.
Supported:
  * [Bitwarden Secrets Manager](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden) — `bws` CLI, lazy-installed, free tier works.
  * [1Password](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/onepassword) — `op://` references via the official `op` CLI; service-account or desktop session auth.
  * [Command helper](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command) — any CLI vault (`keepassxc-cli`, `secret-tool`, `pass`, custom scripts) via a user-configured helper that prints `KEY=VALUE` lines.


## Multiple sources at once[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#multiple-sources-at-once "Direct link to Multiple sources at once")
You can enable more than one secret source at the same time — for example a team Bitwarden project alongside a personal vault plugin. Sources compose per env var with a deterministic precedence ladder:
  1. **Your`.env` / shell wins by default.** A source only replaces a pre-existing value when its own `override_existing: true` is set (Bitwarden defaults to true so central rotation works).
  2. **Mapped sources beat bulk sources.** A source where you explicitly bind env vars to references (an `env:` map) outranks a source that injects a whole project of secrets implicitly, regardless of ordering.
  3. **First source wins.** Within the same shape, the order of the optional `secrets.sources` list (or registration order) decides. Later claims on an already-claimed var are skipped — with a startup warning, never silently.


`override_existing` never lets one source overwrite a var another source already claimed, and no source can ever overwrite another source's bootstrap token (e.g. `BWS_ACCESS_TOKEN`).

```


secrets:  





  sources: [bitwarden]     # optional explicit ordering  





  bitwarden:  





    enabled: true  





    project_id: "..."  



```

Every credential injected by a source is labelled with its origin — setup flows and `hermes model` show `(from Bitwarden)` next to detected keys so you always know where a value came from.
## Profiles and shared vaults[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#profiles-and-shared-vaults "Direct link to Profiles and shared vaults")
Two orchestrator-level knobs make one shared vault safe across [profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles):
  * **`secrets.preserve_existing`**— a list of env var names whose existing`.env` / shell value always wins, even against a source with `override_existing: true`. Use it for per-profile platform secrets (e.g. `FEISHU_APP_SECRET`) that intentionally differ across profiles while everything else rotates centrally:

```


secrets:  





  preserve_existing: [FEISHU_APP_SECRET, TELEGRAM_BOT_TOKEN]  



```

  * **Profile aliasing** (on by default, `secrets.profile_alias: false` to disable) — when Hermes runs under a named profile, a vault secret named `FOO_<PROFILE>` (credential-shaped suffixes only: `*_API_KEY`, `*_TOKEN`, `*_SECRET`, `*_KEY`, `*_PASSWORD`) also hydrates the canonical `FOO`. Store `TELEGRAM_BOT_TOKEN_MILLA` in the shared project and the `milla` profile's adapters — which read the fixed name `TELEGRAM_BOT_TOKEN` — get the right value automatically. A var the vault supplies directly under its canonical name always beats an alias.


Both apply to every source — bundled and plugin — because they live in the orchestrator, not the backends.
## Secrets in child processes[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#secrets-in-child-processes "Direct link to Secrets in child processes")
Terminal commands, `execute_code` sandboxes and [`no_agent` cron scripts](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#giving-a-script-a-credential) run with a sanitized environment: Hermes-managed credentials are stripped, and only variables you declare in `terminal.env_passthrough` (or a loaded skill's `required_environment_variables`) are forwarded. A declared variable is forwarded with the **owning profile's** value — from that profile's `.env` or its secret sources — even when the profile is served by a multi-profile gateway or the Desktop/dashboard backend and its secrets never entered the process environment. A profile's declared value never reaches another profile's children, and the launch profile's `.env` credentials are dropped from children that run for a served profile. Provider credentials cannot be declared; see [Security → Credential scoping](https://hermes-agent.nousresearch.com/docs/user-guide/security).
## Adding your own backend[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#adding-your-own-backend "Direct link to Adding your own backend")
Third-party secret managers ship as standalone plugins, not core PRs. A backend subclasses `agent.secret_sources.base.SecretSource` (one required method: `fetch(cfg, home_path) -> FetchResult`) and registers via `ctx.register_secret_source(MySource())` in the plugin's `register(ctx)`. The orchestrator owns precedence, conflict handling, timeouts, and provenance — your source only fetches. Full guide with the contract rules, subprocess-safety helper, and conformance kit: [Building a Secret Source Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin).
The bundled set is deliberately closed (same policy as memory providers): Bitwarden and 1Password ship in-tree. Everything else — Infisical, Proton Pass, HashiCorp Vault, AWS Secrets Manager, OS keystores — belongs in plugin repos; share them in the Nous Research Discord (`#plugins-skills-and-skins`).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/secrets/index.md)
[Previous Configuring Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)[Next Bitwarden Secrets Manager](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden)
  * [Multiple sources at once](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#multiple-sources-at-once)
  * [Profiles and shared vaults](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#profiles-and-shared-vaults)
  * [Secrets in child processes](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#secrets-in-child-processes)
  * [Adding your own backend](https://hermes-agent.nousresearch.com/docs/user-guide/secrets#adding-your-own-backend)


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
