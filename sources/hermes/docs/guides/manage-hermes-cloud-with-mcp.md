---
title: "Manage Hermes Cloud with MCP"
source: https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp
scraped_at: 2026-11-07T17:20:11.921735+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/manage-hermes-cloud-with-mcp)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
    * [Run Nemotron 3 Ultra free in Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
    * [Run Hermes Agent with Nous Portal](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
    * [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)
    * [Running Hermes on a Personal or Work Machine](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine)
    * [Run Local LLMs on Mac](https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac)
    * [Tutorial: Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
    * [Tutorial: Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)
    * [Using Hermes as a Python Library](https://hermes-agent.nousresearch.com/docs/guides/python-library)
    * [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
    * [Manage Hermes Cloud with MCP](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
    * [Use SOUL.md with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes)
    * [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)
    * [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)
    * [Script-Only Cron Jobs (No LLM)](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
    * [Automation Blueprints](https://hermes-agent.nousresearch.com/docs/guides/automation-blueprints)
    * [Cron Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting)
    * [Troubleshooting: "My Agent Feels Dumber"](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
    * [Working with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
    * [Delegation & Parallel Work](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns)
    * [Give Your Agent Its Own Email Address](https://hermes-agent.nousresearch.com/docs/guides/agent-email-address)
    * [Tutorial: GitHub PR Review Agent](https://hermes-agent.nousresearch.com/docs/guides/github-pr-review-agent)
    * [GitHub PR Reviews via Webhook](https://hermes-agent.nousresearch.com/docs/guides/webhook-github-pr-review)
    * [Migrate from OpenClaw](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)
    * [AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
    * [Google Vertex AI](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
    * [Microsoft Foundry](https://hermes-agent.nousresearch.com/docs/guides/azure-foundry)
    * [xAI Grok OAuth (SuperGrok / X Premium+)](https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth)
    * [OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)
    * [Register a Microsoft Graph Application](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
    * [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Manage Hermes Cloud with MCP


On this page
# Manage Hermes Cloud with MCP
Python dependency commands on this page use a [PM-prepared source checkout](https://hermes-agent.nousresearch.com/docs/reference/package-management#developer-workflow). After a dependency change, reactivate the checkout and restart Hermes.
[Hermes Cloud](https://portal.nousresearch.com/cloud) runs hosted Hermes Agent instances for you. Normally you manage them from the `/agents` page in the [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal). This guide connects your **local** Hermes Agent to the Portal's MCP server so you can manage those cloud instances by just asking — "list my cloud agents", "restart the stopped one", "what's it costing me" — without leaving your terminal.
It's a standard [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) server hosted by Nous Research, gated by the same OAuth login you already use for the Portal. Once connected, Hermes gets two tools it can call on your behalf.
## What you can do with it[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#what-you-can-do-with-it "Direct link to What you can do with it")
Once connected, the model can call these on your Hermes Cloud org:  
| Ask for…  | Under the hood  |  
| --- | --- |  
| "List my cloud agents"  |  `agents` (list)  |  
| "What's the status of `<name>`?"  |  `agents` (get / status)  |  
| "Roughly what is this instance costing?"  |  `agents` (cost_estimate)  |  
| "Start / stop / restart `<name>`"  |  `agent` (start / stop / restart)  |  
| "Spin up a new instance called `<name>`"  |  `agent` (create)  |  
| "Destroy `<name>`"  |  `agent` (destroy)  |  
| "Update the env / image on `<name>`"  |  `agent` (update_env / update_image)  |  
Every call runs against **your** org with your Portal identity, and membership is re-checked on each call — the connection can only touch instances you already control from the web UI.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#prerequisites "Direct link to Prerequisites")
  * A [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal) account with [Hermes Cloud](https://portal.nousresearch.com/cloud) access (at least one instance, or the ability to create one).
  * MCP support installed. If you used the standard install script it's already there; otherwise:

```


cd ~/.hermes/hermes-agent  





python -c "import pm; pm.sync_venv(['mcp'], explicit=True)"  



```



You do **not** need a separate API key or client secret — the server uses OAuth with PKCE, and the login is a browser round-trip.
## Step 1: add the server[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-1-add-the-server "Direct link to Step 1: add the server")

```


hermes mcp add --url https://portal.nousresearch.com/mcp --auth oauth hermes-cloud  



```

`--auth oauth` tells Hermes this is an OAuth-protected HTTP server. On first connect Hermes:
  1. Discovers the server's OAuth endpoints automatically (RFC 9728 / 8414 metadata).
  2. Registers itself as a client (RFC 7591 Dynamic Client Registration) — no secret to copy.
  3. Opens your browser to the Portal to sign in and authorize.
  4. Stores the resulting token under `~/.hermes/mcp-tokens/` and reuses it (refresh is automatic).


### Choosing an organization[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#choosing-an-organization "Direct link to Choosing an organization")
If your Portal account belongs to **more than one organization** , the browser shows an **org picker** during authorization — pick which org this connection should manage. The choice is made once, in the browser; there's nothing to pass on the command line. Single-org accounts skip this step and bind automatically.
If you ever need to point the connection at a different org, remove and re-add the server (`hermes mcp remove hermes-cloud`, then the `add` command again) and pick the other org in the browser.
## Step 2: verify it connected[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-2-verify-it-connected "Direct link to Step 2: verify it connected")

```


hermes mcp test hermes-cloud  



```

Then start (or reload) a session:

```


hermes chat  



```


```


/reload-mcp  



```

Ask a read-only question to confirm the tools are live:

```


List my Hermes Cloud agents and their current status.  



```

You should get back the same instances you see on the Portal's `/agents` page.
## Step 3: use it[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-3-use-it "Direct link to Step 3: use it")
Read-only questions are always safe:

```


Which of my cloud agents is currently running, and roughly what is each one costing?  



```

Lifecycle actions map to plain requests:

```


Restart the instance called research-bot.  



```


```


Create a new Hermes Cloud instance named scratch, then tell me when it's ready.  



```

Hermes reports what each tool returned — the instance list, the new status, the created instance's details — so you can confirm the action landed.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#configuration "Direct link to Configuration")
After `hermes mcp add`, the server lives in `~/.hermes/config.yaml`:

```


mcp_servers:  





  hermes-cloud:  





    url: "https://portal.nousresearch.com/mcp"  





    auth: oauth  



```

No credentials go in `config.yaml` — the OAuth token is kept separately under `~/.hermes/mcp-tokens/`, the same way the Portal refresh token stays out of your config.
### Limiting the tool surface[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#limiting-the-tool-surface "Direct link to Limiting the tool surface")
The server exposes both read (`agents`) and mutating (`agent`) tools. If you want the connection to be **read-only** — list and inspect, but never start/stop/create/destroy — restrict it to the `agents` tool:

```


mcp_servers:  





  hermes-cloud:  





    url: "https://portal.nousresearch.com/mcp"  





    auth: oauth  





    tools:  





      include: [agents]  



```

Run `/reload-mcp` after changing the config. See [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes) for the full filtering model (`include`/`exclude`, `prompts`, `resources`).
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#troubleshooting "Direct link to Troubleshooting")
### The browser shows an org picker and I'm not sure which to choose[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#the-browser-shows-an-org-picker-and-im-not-sure-which-to-choose "Direct link to The browser shows an org picker and I'm not sure which to choose")
You belong to multiple Portal organizations. Pick the org whose Hermes Cloud instances you want to manage from this connection. If you're unsure, it's the org that owns the instances you see on the Portal `/agents` page. You can re-choose later by removing and re-adding the server.
### "invalid_client" or "unknown client" on connect[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#invalid_client-or-unknown-client-on-connect "Direct link to "invalid_client" or "unknown client" on connect")
The stored client registration no longer matches the server (for example, you connected to a different environment previously). Clear this server's cached OAuth state and re-add it:

```


hermes mcp remove hermes-cloud  





rm -f ~/.hermes/mcp-tokens/hermes-cloud.*  





hermes mcp add --url https://portal.nousresearch.com/mcp --auth oauth hermes-cloud  



```

### The tools aren't showing up after adding the server[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#the-tools-arent-showing-up-after-adding-the-server "Direct link to The tools aren't showing up after adding the server")
Reload MCP inside the session and re-check:

```


/reload-mcp  



```


```


Tell me which MCP-backed tools are available right now.  



```

If they're still missing, run `hermes mcp test hermes-cloud` to see the connection error directly.
### It asks me to log in again[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#it-asks-me-to-log-in-again "Direct link to It asks me to log in again")
OAuth tokens refresh automatically, but if the Portal invalidates your session (password change, revoke, expiry) the next call asks you to re-authorize. Re-run the `hermes mcp add` command — the browser flow re-mints a token.
### Headless / SSH / remote host[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#headless--ssh--remote-host "Direct link to Headless / SSH / remote host")
The OAuth browser callback runs on the machine where Hermes is running. On a remote host, forward the loopback port over SSH — the same pattern as any other OAuth login. See [OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh).
## See also[​](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#see-also "Direct link to See also")
  * **[Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)** — the subscription, models, and Tool Gateway behind the same login
  * **[Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)** — connecting and filtering MCP servers in general
  * **[MCP feature overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)** — what MCP is and how Hermes uses it
  * **[MCP configuration reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference)** — every `mcp_servers` field, including `auth: oauth`
  * **[OAuth over SSH](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)** — logging in from remote or browser-only environments


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/manage-hermes-cloud-with-mcp.md)
[Previous Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)[Next Use SOUL.md with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes)
  * [What you can do with it](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#what-you-can-do-with-it)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#prerequisites)
  * [Step 1: add the server](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-1-add-the-server)
    * [Choosing an organization](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#choosing-an-organization)
  * [Step 2: verify it connected](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-2-verify-it-connected)
  * [Step 3: use it](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#step-3-use-it)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#configuration)
    * [Limiting the tool surface](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#limiting-the-tool-surface)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#troubleshooting)
    * [The browser shows an org picker and I'm not sure which to choose](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#the-browser-shows-an-org-picker-and-im-not-sure-which-to-choose)
    * ["invalid_client" or "unknown client" on connect](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#invalid_client-or-unknown-client-on-connect)
    * [The tools aren't showing up after adding the server](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#the-tools-arent-showing-up-after-adding-the-server)
    * [It asks me to log in again](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#it-asks-me-to-log-in-again)
    * [Headless / SSH / remote host](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#headless--ssh--remote-host)
  * [See also](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp#see-also)


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
