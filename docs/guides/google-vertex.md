---
title: "Google Vertex AI"
source: https://hermes-agent.nousresearch.com/docs/guides/google-vertex
scraped_at: 2026-11-07T17:20:11.919736+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/google-vertex)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Google Vertex AI


On this page
# Google Vertex AI
Hermes Agent supports **Gemini models on Google Cloud Vertex AI** through Vertex's OpenAI-compatible endpoint. Unlike the [Google AI Studio provider](https://hermes-agent.nousresearch.com/docs/guides/google-gemini) (which uses a static API key against `generativelanguage.googleapis.com`), Vertex gives you **enterprise-grade rate limits and GCP billing/credits** , and is the right choice when you want Gemini usage to draw on your Google Cloud account rather than an AI Studio key.
Vertex has **no static API key** for the standard endpoint. Every request needs a short-lived **OAuth2 access token** (≈1 hour TTL) minted from either a service-account JSON or Application Default Credentials (ADC). Hermes mints and **auto-refreshes** these tokens for you — you never paste a token by hand. This is why pasting a temporary token into a custom provider's `api_key` field does not work: it expires mid-session.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#prerequisites "Direct link to Prerequisites")
  * **A Google Cloud project** with the **Vertex AI API enabled** and billing active.
  * **Credentials** , one of:
    * a **service-account JSON** key file with the `roles/aiplatform.user` role, or
    * **Application Default Credentials** via `gcloud auth application-default login` (or the metadata server when running on a GCP VM).
  * **`google-auth`**— installed automatically the first time you select Vertex (lazy install). Run`hermes setup` to repair a managed install if that fails.


## Quick Start[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#quick-start "Direct link to Quick Start")

```


# Option A — service account JSON (recommended for servers / gateways)  





echo "VERTEX_CREDENTIALS_PATH=/path/to/service-account.json" >> ~/.hermes/.env  





  





# Option B — Application Default Credentials (good for local dev)  





gcloud auth application-default login  





  





# Select Vertex as your provider  





hermes model  





# → Choose "More providers..." → "Google Vertex AI"  





# → Enter your GCP project ID (or leave blank to use the one in your credentials)  





# → Choose a region (default: global)  





# → Select a Gemini model  





  





# Start chatting  





hermes chat  



```

## Configuration[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#configuration "Direct link to Configuration")
Vertex splits its settings by sensitivity:
  * The **credential path** is a pointer to a secret and lives in `~/.hermes/.env`.
  * **Project ID and region** are non-secret routing settings and live in `~/.hermes/config.yaml`.


`~/.hermes/.env`:

```


# One of these (checked in this order); omit both to use ADC:  





VERTEX_CREDENTIALS_PATH=/path/to/service-account.json  





GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json  



```

`~/.hermes/config.yaml`:

```


model:  





  default: google/gemini-3-flash-preview  





  provider: vertex  





  





vertex:  





  project_id: my-gcp-project   # blank → use the project embedded in the credentials  





  region: global               # "global" is required for the Gemini 3.x previews  



```

`VERTEX_PROJECT_ID` and `VERTEX_REGION` override the `vertex.project_id` / `vertex.region` values in `config.yaml`. Use them for per-shell overrides; keep the durable settings in `config.yaml`.
### How authentication works[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#how-authentication-works "Direct link to How authentication works")
  1. Hermes resolves credentials in this order: `VERTEX_CREDENTIALS_PATH` → `GOOGLE_APPLICATION_CREDENTIALS` → ADC.
  2. It mints an OAuth2 access token (`cloud-platform` scope) and caches it, refreshing when the token is within 5 minutes of expiry.
  3. The token is handed to a standard OpenAI client pointed at the Vertex endpoint:

```


https://aiplatform.googleapis.com/v1beta1/projects/{project}/locations/{region}/endpoints/openapi  



```

Regional locations use a `{region}-aiplatform.googleapis.com` host instead.
  4. If a session runs longer than the token lifetime and a request returns `401`, Hermes re-mints the token and retries automatically. On a long-running gateway, if ADC's refresh token has itself expired, Hermes falls back to the service-account JSON when one is configured.


## Available Models[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#available-models "Direct link to Available Models")
Vertex requires the `google/` vendor prefix on model IDs. The `hermes model` picker offers:  
| Model  | ID  |  
| --- | --- |  
| Gemini 3.8 Flash  | `google/gemini-3.8-flash`  |  
| Gemini 3.7 Flash  | `google/gemini-3.7-flash`  |  
| Gemini 3.1 Pro Preview  | `google/gemini-3.1-pro-preview`  |  
| Gemini 3 Pro Preview  | `google/gemini-3-pro-preview`  |  
| Gemini 3 Flash Preview  | `google/gemini-3-flash-preview`  |  
| Gemini 3.1 Flash Lite Preview  | `google/gemini-3.1-flash-lite-preview`  |  
| Gemini 2.5 Pro  | `google/gemini-2.5-pro`  |  
| Gemini 2.5 Flash  | `google/gemini-2.5-flash`  |  
`global` region for Gemini 3.x
The Gemini 3.x preview models are served through the `global` endpoint. Regional endpoints (`us-central1`, etc.) may 404 them. Leave `region: global` unless you have a specific reason to pin a region.
## Switching Models Mid-Session[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#switching-models-mid-session "Direct link to Switching Models Mid-Session")

```


/model google/gemini-3-pro-preview  





/model google/gemini-3-flash-preview  



```

`/model` switches among already-configured providers and models; it does not collect new credentials. Configure Vertex with `hermes model` first.
## Reasoning / Thinking[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#reasoning--thinking "Direct link to Reasoning / Thinking")
Vertex exposes Gemini's thinking budget through the OpenAI-compatible surface. Hermes maps its reasoning-effort setting onto `extra_body.google.thinking_config` automatically, so `reasoning_effort` works the same way it does on other Gemini surfaces.
## Diagnostics[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#diagnostics "Direct link to Diagnostics")

```


hermes doctor  



```

The doctor reports whether Vertex credentials can be resolved (service-account path or ADC) and whether the provider is configured.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#troubleshooting "Direct link to Troubleshooting")
### "Vertex AI credentials could not be resolved"[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#vertex-ai-credentials-could-not-be-resolved "Direct link to "Vertex AI credentials could not be resolved"")
Hermes found neither a service-account JSON nor working ADC. Either set `VERTEX_CREDENTIALS_PATH` in `~/.hermes/.env`, or run `gcloud auth application-default login`. If your project isn't embedded in the credentials, set `vertex.project_id` in `config.yaml`.
###  `google-auth` not installed[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#google-auth-not-installed "Direct link to google-auth-not-installed")
Hermes lazy-installs it the first time you select the Vertex provider. If that fails, run `hermes setup` to repair the managed install.
### 404 on Gemini 3.x models[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#404-on-gemini-3x-models "Direct link to 404 on Gemini 3.x models")
You are probably on a regional endpoint. Set `region: global` in the `vertex:` section of `config.yaml` (or unset `VERTEX_REGION`).
### 403 / permission denied[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#403--permission-denied "Direct link to 403 / permission denied")
The service account (or your ADC identity) needs the `roles/aiplatform.user` role on the project, and the Vertex AI API must be enabled for that project.
## Related[​](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#related "Direct link to Related")
  * [Google Gemini (AI Studio)](https://hermes-agent.nousresearch.com/docs/guides/google-gemini) — static-API-key Gemini without GCP
  * [AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock) — another native cloud-provider integration
  * [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/google-vertex.md)
[Previous AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)[Next Microsoft Foundry](https://hermes-agent.nousresearch.com/docs/guides/azure-foundry)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#prerequisites)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#quick-start)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#configuration)
    * [How authentication works](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#how-authentication-works)
  * [Available Models](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#available-models)
  * [Switching Models Mid-Session](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#switching-models-mid-session)
  * [Reasoning / Thinking](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#reasoning--thinking)
  * [Diagnostics](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#diagnostics)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#troubleshooting)
    * ["Vertex AI credentials could not be resolved"](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#vertex-ai-credentials-could-not-be-resolved)
    * [`google-auth` not installed](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#google-auth-not-installed)
    * [404 on Gemini 3.x models](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#404-on-gemini-3x-models)
    * [403 / permission denied](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#403--permission-denied)
  * [Related](https://hermes-agent.nousresearch.com/docs/guides/google-vertex#related)


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
