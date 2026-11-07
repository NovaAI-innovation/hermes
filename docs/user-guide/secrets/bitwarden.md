---
title: "Bitwarden Secrets Manager"
source: https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden
scraped_at: 2026-11-07T17:19:30.384208+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/secrets/bitwarden)


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
  * Bitwarden Secrets Manager


On this page
# Bitwarden Secrets Manager
Pull API keys from [Bitwarden Secrets Manager](https://bitwarden.com/products/secrets-manager/) at process startup instead of storing them in plaintext inside `~/.hermes/.env`. One bootstrap secret (a machine-account access token) replaces N per-provider keys, and rotating a credential becomes a single change in the Bitwarden web app.
## How it works[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#how-it-works "Direct link to How it works")
  1. You create a **machine account** in Bitwarden Secrets Manager, give it read access to a project, and generate an **access token**.
  2. Hermes stores that single token in `~/.hermes/.env` as `BWS_ACCESS_TOKEN`.
  3. Every time `hermes` (or the gateway, or a cron job) starts, after `~/.hermes/.env` has loaded, Hermes calls `bws secret list <project_id>` and sets the returned keys into `os.environ`.
  4. By default Hermes **overrides** values already in your environment, so Bitwarden is the source of truth — rotate a key once in the web app and every Hermes process picks it up on next start. Flip `override_existing: false` in config if you want `.env` to win instead.


Hermes honors a `bws` executable on `PATH` before checking PM selection. If neither exists, first use requests the pinned package from [PM](https://hermes-agent.nousresearch.com/docs/reference/package-management#optional-security-tools), subject to the lazy-install policy.
## Why machine accounts (and why no 2FA prompt)[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#why-machine-accounts-and-why-no-2fa-prompt "Direct link to Why machine accounts \(and why no 2FA prompt\)")
Bitwarden Secrets Manager is designed for non-interactive workloads: machine accounts can't be 2FA-gated because there's no human in the loop. The access token is the credential. Anyone with it can read every secret the machine account has access to, so treat it like a high-value bearer token — store it in `.env` (not `config.yaml`), and revoke + regenerate from the Bitwarden web app if it ever leaks.
You set up the machine account _in the web app_ , where your normal 2FA applies. After that the token is autonomous.
## Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#setup "Direct link to Setup")
### 1. Create a machine account and access token[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#1-create-a-machine-account-and-access-token "Direct link to 1. Create a machine account and access token")
In the [Bitwarden web app](https://vault.bitwarden.com) (or [vault.bitwarden.eu](https://vault.bitwarden.eu) for EU accounts):
  1. Switch to **Secrets Manager** from the product switcher.
  2. Create or pick a **Project** (e.g. "Hermes keys").
  3. Add your provider keys as secrets. The secret **Name** becomes the environment variable name — use `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, etc.
  4. **Machine accounts → New machine account → My Hermes machine** → **Projects** tab → grant Read access to your project.
  5. **Access tokens** tab → **Create access token** → **Never** expires (or pick a date) → copy the token (starts with `0.`). Bitwarden cannot retrieve it again — keep the copy.


Secrets Manager is included on the Bitwarden free tier with limits; no paid plan needed to try this.
### 2. Run the wizard[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#2-run-the-wizard "Direct link to 2. Run the wizard")

```


hermes secrets bitwarden setup  



```

It will:
  1. If `bws` is absent, request its pinned package from PM.
  2. Prompt you for the access token (input is hidden). Stored in `~/.hermes/.env` as `BWS_ACCESS_TOKEN`.
  3. Ask which Bitwarden region your machine account belongs to — **US Cloud** , **EU Cloud** , or **self-hosted / custom URL**. Stored in `config.yaml` as `secrets.bitwarden.server_url` and passed to `bws` as `BWS_SERVER_URL`.
  4. List the projects the machine account can see; pick one. Stored in `config.yaml` as `secrets.bitwarden.project_id`.
  5. Test-fetch the project's secrets and show you which env vars will resolve.
  6. Flip `secrets.bitwarden.enabled: true`.


Non-interactive setup is also supported via flags:

```


hermes secrets bitwarden setup \  





  --access-token "$BWS_ACCESS_TOKEN" \  





  --server-url https://vault.bitwarden.eu \  





  --project-id <project-uuid>  



```

### 3. Confirm[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#3-confirm "Direct link to 3. Confirm")

```


hermes secrets bitwarden status  



```

From now on, every `hermes` invocation pulls fresh secrets at startup. You'll see a one-line summary in stderr the first time secrets are applied in a process.
## CLI[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#cli "Direct link to CLI")  
| Command  | What it does  |  
| --- | --- |  
| `hermes secrets bitwarden setup`  | Interactive wizard (install binary, prompt for token, pick project, test fetch)  |  
| `hermes secrets bitwarden status`  | Show config + binary version + token presence/validation  |  
| `hermes secrets bitwarden token`  | Rotate the access token: validate the new token against Bitwarden, then store it in `.env`  |  
| `hermes secrets bitwarden sync`  | Dry-run: pull secrets now and show what would be applied  |  
| `hermes secrets bitwarden sync --apply`  | Pull and export into the current shell's environment  |  
| `hermes secrets bitwarden install`  | Install or repair the PM-pinned `bws` binary. No Bitwarden authentication required.  |  
| `hermes secrets bitwarden install --force`  | Check and repair the managed copy. Valid entries can be reused without another download.  |  
| `hermes secrets bitwarden disable`  | Flip `enabled: false`; leaves token + project id in place  |  
## Rotating an expired or revoked token[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#rotating-an-expired-or-revoked-token "Direct link to Rotating an expired or revoked token")
When the machine-account token expires, gets revoked, or the account is deleted, startup shows:

```


Bitwarden Secrets Manager: Bitwarden rejected the machine-account access token (BWS_ACCESS_TOKEN) — it was likely revoked, expired, or belongs to another region.  (...)  





Bitwarden Secrets Manager: → Run `hermes secrets bitwarden token` to paste a fresh access token ...  



```

Fix it without re-running the whole wizard:

```


hermes secrets bitwarden token                     # masked prompt  





hermes secrets bitwarden token --access-token 0.…  # non-interactive  



```

The command probes Bitwarden with the new token **before** writing anything — a rejected token leaves your current `.env` untouched. On success it stores the token, clears the fetch caches, and warns if the configured project is not visible to the new machine account.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#configuration "Direct link to Configuration")
Defaults in `~/.hermes/config.yaml`:

```


secrets:  





  bitwarden:  





    enabled: false  





    access_token_env: BWS_ACCESS_TOKEN  





    project_id: ""  





    server_url: ""  





    cache_ttl_seconds: 300  





    encrypted_cache:  





      enabled: false  





      max_stale_seconds: 0  





    override_existing: true  





    auto_install: true  



```
  
| Key  | Default  | What it does  |  
| --- | --- | --- |  
| `enabled`  | `false`  | Master switch. When false, Bitwarden is never contacted.  |  
| `access_token_env`  | `BWS_ACCESS_TOKEN`  | Env var name that holds the bootstrap token. Change this if you already use `BWS_ACCESS_TOKEN` for something else.  |  
| `project_id`  | `""`  | UUID of the project to sync from.  |  
| `server_url`  | `""`  | Bitwarden region or self-hosted endpoint. Empty = `bws` default (US Cloud, `https://vault.bitwarden.com`). Set to `https://vault.bitwarden.eu` for EU Cloud, or your own URL for self-hosted. Plumbed into the `bws` subprocess as `BWS_SERVER_URL`.  |  
| `cache_ttl_seconds`  | `300`  | How long an in-process or disk fetch result is reused. Set to `0` to disable fresh-cache reuse.  |  
| `encrypted_cache.enabled`  | `false`  | Store the last successful fetch in an AES-GCM encrypted cache at `~/.hermes/bws_cache.enc.json`.  |  
| `encrypted_cache.max_stale_seconds`  | `0`  | When encrypted caching is enabled, allow that cache to be used only after network/timeout failures, up to this age. Authentication failures never use stale secrets. A successful encrypted write removes the plaintext `bws_cache.json`.  |  
| `override_existing`  | `true`  | When true, Bitwarden values overwrite anything already in env (so rotation in the web app actually takes effect). Flip to `false` if you want `.env` / shell exports to win locally.  |  
| `auto_install`  | `true`  | Requests the PM-pinned `bws` package when no binary exists. PM's lazy-install policy also applies.  |  
## Failure modes[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#failure-modes "Direct link to Failure modes")
Bitwarden never blocks Hermes startup. If anything goes wrong, you'll see a one-line warning in stderr and Hermes continues with whatever credentials `.env` already had:  
| Symptom  | Cause  | Fix  |  
| --- | --- | --- |  
| `BWS_ACCESS_TOKEN is not set`  | Enabled in config but token cleared from `.env`  | Re-run `hermes secrets bitwarden setup`  |  
| `Bitwarden rejected the machine-account access token … invalid_client`  | Token revoked, expired, machine account deleted — or the token belongs to another region (e.g. EU token hitting the US identity endpoint)  | Run `hermes secrets bitwarden token` to paste a fresh token; for region mismatches re-run setup and pick EU/self-hosted (or set `secrets.bitwarden.server_url`)  |  
| `bws exited 1: invalid access token`  | Token revoked or wrong  | Run `hermes secrets bitwarden token` with a new token  |  
| `bws timed out`  | Network blocked or Bitwarden API slow  | Check connectivity to `api.bitwarden.com` (or your `server_url`)  |  
| `bws binary not available`  | No PM selection or executable on `PATH`, and automatic installation is disabled or failed  | Run `hermes secrets bitwarden install` and read its diagnostic.  |  
| Checksum failure  | The download does not match the PM lock  | Stop and investigate the download source. Do not bypass the hash check.  |  
Startup warnings now include a `→` remediation line telling you exactly which command fixes the failure.
## Security notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#security-notes "Direct link to Security notes")
  * The bootstrap token (`BWS_ACCESS_TOKEN`) is itself sensitive — anyone with it can read every secret the machine account has access to. Treat it the same as any other API key.
  * Hermes will refuse to let Bitwarden overwrite the bootstrap token itself, even with `override_existing: true`. If you store `BWS_ACCESS_TOKEN` as a secret inside the project, it's silently skipped during apply.
  * PM checks the managed archive against its SHA-256 hash in `pm/lock.json`. A mismatch aborts installation.
  * The same lock declares the version. First use does not resolve a "latest" release. External binaries remain outside these PM checks.


## When NOT to use this[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#when-not-to-use-this "Direct link to When NOT to use this")
  * **Single-machine personal setups** where `~/.hermes/.env` is fine. You're trading one credential for another and adding a network dependency at startup.
  * **Air-gapped environments** that can't reach `api.bitwarden.com`.
  * **CI/CD** where the existing secrets-injection mechanism (GitHub Actions secrets, Vault, etc.) is already set up — pick one path, not two.


The good case for this is multi-machine fleets, shared dev boxes, gateway VPSes, or any setup where you want centralized rotation and revocation across multiple Hermes installations.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/secrets/bitwarden.md)
[Previous Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/)[Next 1Password](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/onepassword)
  * [How it works](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#how-it-works)
  * [Why machine accounts (and why no 2FA prompt)](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#why-machine-accounts-and-why-no-2fa-prompt)
  * [Setup](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#setup)
    * [1. Create a machine account and access token](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#1-create-a-machine-account-and-access-token)
    * [2. Run the wizard](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#2-run-the-wizard)
    * [3. Confirm](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#3-confirm)
  * [CLI](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#cli)
  * [Rotating an expired or revoked token](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#rotating-an-expired-or-revoked-token)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#configuration)
  * [Failure modes](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#failure-modes)
  * [Security notes](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#security-notes)
  * [When NOT to use this](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden#when-not-to-use-this)


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
