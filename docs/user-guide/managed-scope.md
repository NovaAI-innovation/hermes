---
title: "Managed Scope"
source: https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope
scraped_at: 2026-11-07T17:19:30.377323+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/managed-scope)


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
  * Managed Scope


On this page
# Managed Scope
**Managed scope** lets an administrator push a baseline of configuration and secrets that a standard (non-root) user **cannot override**. It is intended for fleet/org deployments where IT needs to pin, for example, the model provider, a shared API base URL, or `security.redact_secrets: true` across every user on a machine.
When a managed scope is present, the values it specifies win over the user's `~/.hermes/config.yaml`, `~/.hermes/.env`, and even the shell environment — for exactly the keys it pins. Everything else stays fully user-controlled.
A package-manager–managed install (declarative-distro / formula) blocks _all_ config mutation and tells you to use your package manager. Managed scope is a separate mechanism: it injects _specific immutable values_ on a per-key basis rather than locking the whole config. The two are independent and can coexist.
## Where it lives[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#where-it-lives "Direct link to Where it lives")
Managed scope is read from a system-level directory, default `/etc/hermes`:

```


/etc/hermes/  





├── config.yaml     # managed config layer (wins over ~/.hermes/config.yaml)  





└── .env            # managed env layer (wins over ~/.hermes/.env + shell)  



```

The directory and files are owned by `root` (directory mode `0755`, files `0644`): readable by everyone, writable only by an administrator. **That filesystem permission is the enforcement mechanism** — a standard user can read the managed files but cannot edit them.
Either file is optional. A missing managed directory or missing file simply means "no managed scope," and configuration resolves exactly as it does without the feature.
### Relocating the directory[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#relocating-the-directory "Direct link to Relocating the directory")
The location can be relocated with the `HERMES_MANAGED_DIR` environment variable (for containers or non-`/etc` deployments). This is a deployment/bootstrap path knob — like `HERMES_HOME` — set by the same administrator who owns the managed files. It is **never persisted** to any `.env` by Hermes.

```


# Point managed scope at a custom directory (set by IT / the deployment, not the user)  





export HERMES_MANAGED_DIR=/opt/org/hermes-policy  



```

A user who can set `HERMES_MANAGED_DIR` can repoint managed scope at a directory they control, defeating it. In a real deployment this variable should be fixed by the administrator (e.g. baked into the service unit / container image), not left user-settable. `hermes doctor` reports the _resolved_ managed directory so a redirect is visible.
## Precedence[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#precedence "Direct link to Precedence")
For the keys a managed layer specifies, the order is (highest wins):  
| Tier  | config.yaml  | .env  |  
| --- | --- | --- |  
| 1  |  `/etc/hermes/config.yaml` (managed)  |  `/etc/hermes/.env` (managed)  |  
| 2  |  `~/.hermes/config.yaml` (user)  |  `~/.hermes/.env` (user)  |  
| 3  | built-in defaults  | pre-existing shell environment  |  
Merging is **leaf-level** : pinning `model.default` does not freeze the rest of `model.*`. A managed `config.yaml` of:

```


model:  





  default: org/standard-model  



```

forces `model.default` for every user while leaving `model.fallback` (and every other key) under user control.
For the keys it pins, managed scope deliberately wins over the shell environment too — otherwise it would not be "managed." This is the one place that inverts the usual "an environment variable overrides config.yaml" rule, and it applies only to the specific keys the managed layer specifies.
When the managed `config.yaml` pins a non-empty `terminal.backend`, a profile `.env` that exists but cannot be read (a sandbox launcher withholds it and passes the keys as environment) loads as absent with a warning; without that pin the read error still stops Hermes.
## Seeing what's managed[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#seeing-whats-managed "Direct link to Seeing what's managed")

```


hermes config        # shows a header naming the managed source + the pinned keys  





hermes doctor        # reports the resolved managed dir + pinned key counts  



```

If you try to change a managed value, Hermes refuses and names the source:

```


$ hermes config set model.default my/model  





Cannot set 'model.default': it is managed by your administrator  





(/etc/hermes/config.yaml) and cannot be changed.  



```

The same applies to managed secrets — `hermes config set` / setup will not write a user value for an env key pinned by the managed `.env`.
## Setting up a managed scope (administrators)[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#setting-up-a-managed-scope-administrators "Direct link to Setting up a managed scope \(administrators\)")

```


sudo mkdir -p /etc/hermes  





  





# Pin some config values for every user on this machine  





sudo tee /etc/hermes/config.yaml >/dev/null <<'YAML'  





model:  





  provider: nous  





security:  





  redact_secrets: true  





YAML  





  





# Optionally pin a shared, non-sensitive env value  





sudo tee /etc/hermes/.env >/dev/null <<'ENV'  





OPENAI_API_BASE=https://inference.example.com/v1  





ENV  





  





sudo chmod 0755 /etc/hermes  





sudo chmod 0644 /etc/hermes/config.yaml /etc/hermes/.env  



```

Changes take effect on the next Hermes start (a malformed managed file is logged loudly and ignored — it never blocks startup, but the admin should check `hermes doctor` to confirm the policy is being applied).
## Security model and limitations (v1)[​](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#security-model-and-limitations-v1 "Direct link to Security model and limitations \(v1\)")
  * **Enforcement is filesystem permissions only.** If a user has write access to the managed directory (or runs Hermes as `root`), managed scope is advisory.
  * **The managed`.env` is world-readable** (`0644`), so any local user can read secrets pushed through it. Use it for shared, non-sensitive values (an org API base URL, feature defaults) rather than high-sensitivity secrets.
  * **The agent's own tools are not hard-blocked from a managed _env_ value.** A managed environment variable is applied at startup, but nothing stops the agent from setting a different value inside its own subprocess shell. v1 is a management-convenience boundary against a normal user, not an un-escapable sandbox.


The following are intentionally **out of scope for v1** and may come later:
  * A hard boundary that the agent itself cannot escape.
  * Native managed locations on macOS and Windows (v1 is Linux/POSIX-first).
  * Drop-in fragment directories (`managed.d/`) for layered policy.
  * Signed / integrity-checked managed files.
  * Remote / device-management (MDM) delivery.
  * Tighter (group-scoped) permissions for managed secrets.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/managed-scope.md)
[Previous Which File Does What?](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)[Next Remote Config](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
  * [Where it lives](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#where-it-lives)
    * [Relocating the directory](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#relocating-the-directory)
  * [Precedence](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#precedence)
  * [Seeing what's managed](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#seeing-whats-managed)
  * [Setting up a managed scope (administrators)](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#setting-up-a-managed-scope-administrators)
  * [Security model and limitations (v1)](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope#security-model-and-limitations-v1)


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
