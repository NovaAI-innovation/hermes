---
title: "Remote Config"
source: https://hermes-agent.nousresearch.com/docs/user-guide/remote-config
scraped_at: 2026-11-07T17:19:30.382691+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/remote-config)


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
  * Remote Config


On this page
# Remote Config
**Remote config mode** replaces `config.yaml` with the config plane: each profile's config is the document the plane resolves for this agent instance and that profile. The plane layers it from global, tenant, group, owner, and agent settings, with the profile's own settings last. Administrators can lock keys at an upper level, and the agent cannot change a locked key.
Remote config is for fleet deployments, for example Hermes Cloud. A single machine with one user should keep `config.yaml`.
## Turning it on[​](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#turning-it-on "Direct link to Turning it on")
Set the following in the environment, in `~/.hermes/.env`, or in the managed `/etc/hermes/.env` (which wins over the other two). A value in `config.yaml` cannot select the backend, because the backend is what serves config.  
| Variable  | Meaning  |  
| --- | --- |  
| `HERMES_CONFIG_BACKEND=remote`  | Use the config plane instead of `config.yaml` (default `file`).  |  
| `HERMES_CONFIG_INSTANCE_ID`  | This agent's id in the plane. Hermes Cloud sets it; on-prem the operator sets it when registering the agent. Required.  |  
| `HERMES_CONFIG_REMOTE_URL`  | The plane's base URL (default `https://config-config.nousresearch.com`).  |  
The agent authenticates as itself:
  * **Hermes Cloud** : the Nous access token in the profile's `auth.json`.
  * **On-prem** : an OAuth2 client-credentials token from your identity provider, configured in `.env` with `GATEWAY_RELAY_IDP_TOKEN_URL`, `GATEWAY_RELAY_IDP_CLIENT_ID`, `GATEWAY_RELAY_IDP_CLIENT_SECRET`, and optionally `GATEWAY_RELAY_IDP_SCOPE`.


These values, and the `HERMES_CONFIG_*` variables above, must come from `auth.json`, a `.env` file (the profile's, the project `.env` a Hermes command loads, or the managed one), or the process environment. If a `secrets:` source (1Password, Bitwarden, a command) supplies any of them, Hermes refuses to start. The same holds for `HERMES_PORTAL_BASE_URL`, `NOUS_PORTAL_BASE_URL` and `HERMES_SHARED_AUTH_DIR` (they decide where the Cloud token is read and sent). A multi-profile process (gateway, dashboard) that serves a profile whose `secrets:` source supplies one of these names refuses to serve that profile.
A Hermes process started for another profile (a `hermes -p <name>` worker, a profile's cron or bot child) keeps the `HERMES_CONFIG_*` deployment of the process that started it, so it reads that profile's config from the plane too. It does not inherit the plane credential: on-prem, put the `GATEWAY_RELAY_IDP_*` values where every profile reads them (the managed `/etc/hermes/.env`) or in each profile's `.env`. Without one, the process exits with an error rather than read a local file.
## What changes[​](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#what-changes "Direct link to What changes")
  * **Startup fetches config and fails closed.** Every Hermes process (gateway, dashboard, CLI, terminal children) fetches its profile's config when it loads `.env`. If the plane cannot be reached after about 30 seconds of retries, or refuses the agent, the process exits with an error. It never falls back to a local file or to defaults.
  * **No local config file.** `config.yaml` is neither read nor written, and there is no local cache. A running process keeps the config it last fetched in memory. If the plane becomes unreachable while Hermes runs, the process keeps its in-memory config and retries on the next poll.
  * **Changes arrive by polling.** Each process checks for changes every 5 minutes. A change made in the plane reaches a running agent within one interval.
  * **Writes go to the profile's own level.** `hermes config set`, `/model`, the dashboard, and every other config writer send only the keys that changed, guarded against concurrent edits. If another process changed the profile meanwhile, Hermes re-reads it and applies only its own change on top, never undoing the other one. Removing a key removes it from the profile level only: if an upper level also sets it, that value still applies, and Hermes warns you.
  * **Locked keys are refused.** `hermes config set` (and any setting changed in the TUI or desktop app, including the prompt, reasoning display and details-mode settings) on a locked key reports which level locks it and changes nothing. When a whole document is saved, locked keys are left out, and Hermes prints a note listing them.
  * **Secrets stay out of the plane.** A secret-shaped key such as `api_key` accepts only a `${VAR}` reference, never the secret itself. Put the value in `.env` or a secret source and set the reference:

```


hermes config set model.api_key '${OPENROUTER_API_KEY}'  



```

  * **`secrets:`comes from the plane** like any other key, so administrators can manage and lock secret-source settings centrally.
  * **Schema migrations run in memory.** A document written by an older Hermes is migrated when it is read, and the result is not written back. A later write from a newer Hermes keeps the profile's stored schema version unless that data is already current, so every later reader still migrates it. These in-memory migrations change only the config document: steps that also tidy local files (removing a retired section from `SOUL.md`, clearing old values from `.env`) do not run in remote mode. For the same reason, setting a value that one of those migrations rewrites (for example `compression.threshold_tokens: 256000`, an old default, on a profile stored at an older schema) is refused with a message naming the key: it would be saved and then never read back.
  * **Unknown keys** in the fetched document are ignored with a warning, for example a key added by a newer Hermes.


## Managed scope[​](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#managed-scope "Direct link to Managed scope")
`/etc/hermes/config.yaml` (see [Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)) is **ignored** in remote mode: config and locks come only from the plane. Hermes warns at startup, and `hermes doctor` flags the file. The managed `/etc/hermes/.env` still applies.
## Commands that work on the config file[​](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#commands-that-work-on-the-config-file "Direct link to Commands that work on the config file")
These commands copy or edit `config.yaml` and are refused in remote mode:
  * `hermes config edit` (use `hermes config set` instead)
  * profile clone, profile rename (the plane keeps a profile's settings under its name), and profile distribution install
  * `hermes backup`, `hermes import`, and snapshot restore
  * `hermes gateway --config <file>`


`hermes doctor` reports the backend instead of the file: the plane URL, the profile, the profile level's version, the number of locks, and when the config was last fetched.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/remote-config.md)
[Previous Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)[Next Configuring Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)
  * [Turning it on](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#turning-it-on)
  * [What changes](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#what-changes)
  * [Managed scope](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#managed-scope)
  * [Commands that work on the config file](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config#commands-that-work-on-the-config-file)


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
