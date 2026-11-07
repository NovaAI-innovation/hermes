---
title: "Command Helper Secret Source"
source: https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command
scraped_at: 2026-11-07T17:19:30.385209+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/secrets/command)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
On this page
# Command Helper Secret Source
Resolve credentials by running your own helper command at startup — any secret store with a CLI works: `keepassxc-cli`, `secret-tool` (GNOME Keyring), `pass`, `gpg`, Vaultwarden's CLI, or a script that cats a tmpfs env file. The helper prints `KEY=VALUE` lines on stdout; Hermes applies them through the same orchestrator as [Bitwarden](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/bitwarden) and [1Password](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/onepassword), so you can enable any combination of sources simultaneously.
## How it works[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#how-it-works "Direct link to How it works")
  1. You configure a helper command in `config.yaml` (never in `.env` — the command is configuration, `.env` holds values).
  2. At startup, after `.env` loads, Hermes runs the helper ONCE via `/bin/sh -c` and parses its stdout as a dotenv blob.
  3. The parsed keys flow through the standard precedence ladder: `.env`/shell win unless `override_existing: true`; mapped sources beat this bulk source on contested vars; first claim wins.



```


secrets:  





  command:  





    enabled: true  





    command: "cat /run/user/1000/hermes-secrets.env"  





    # or any vault CLI that dumps KEY=VALUE lines:  





    # command: "pass show hermes/env"  





    # command: "secret-tool lookup service hermes-env"  



```

## Config[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#config "Direct link to Config")  
| Key  | Default  | What it does  |  
| --- | --- | --- |  
| `enabled`  | `false`  | Master switch.  |  
| `command`  | `""`  | Helper run via `/bin/sh -c`; must print `KEY=VALUE` lines on stdout.  |  
| `helper_timeout_seconds`  | `3`  | Hard timeout for one helper run. Deliberately tight — the helper must be fast and NON-interactive (no unlock prompts, no touch/PIN).  |  
| `override_existing`  | `false`  | Helper values overwrite `.env`/shell values. Off by default (unlike Bitwarden/1Password) since a local helper is not a central rotation authority.  |  
## Security model[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#security-model "Direct link to Security model")
  * The helper command string is YOUR configuration — same trust level as the `.env` file you control.
  * Output is hard-capped at 1 MiB; a runaway helper can't wedge startup (process group killed on timeout).
  * The helper's **stderr is discarded** — vault CLI diagnostics can carry secret material, so they never reach Hermes' output. Failures log structured fields only (exit code / signal / errno), never the command string.
  * Whitespace-only values are treated as "no value" — a placeholder entry never flows into an Authorization header.
  * POSIX-only (needs `/bin/sh`). On Windows the source reports itself unconfigured and startup continues.


## Failure modes[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#failure-modes "Direct link to Failure modes")
Startup is never blocked. Errors print one line plus a `→` remediation hint:  
| Symptom  | Cause  | Fix  |  
| --- | --- | --- |  
| `secrets.command.command is empty`  | Enabled without a command  | Set `secrets.command.command` in config.yaml  |  
| `helper command failed`  | Non-zero exit, timeout, spawn failure  | Run the helper manually in a shell to see its real error (Hermes discards its stderr on purpose)  |  
| `helper output was not a KEY=VALUE map`  | Helper printed a bare value or garbage  | Make the helper emit dotenv-shaped lines  |  
## When to use this vs a plugin[​](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#when-to-use-this-vs-a-plugin "Direct link to When to use this vs a plugin")
The command source is the escape hatch for vaults without a bundled integration. If you find yourself wrapping a complex CLI dance in a long script, consider a proper [secret-source plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin) instead — plugins get caching, provenance labels, and typed config.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/secrets/command.md)
  * [How it works](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#how-it-works)
  * [Config](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#config)
  * [Security model](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#security-model)
  * [Failure modes](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#failure-modes)
  * [When to use this vs a plugin](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/command#when-to-use-this-vs-a-plugin)


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
