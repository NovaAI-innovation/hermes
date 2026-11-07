---
title: "AWS Bedrock"
source: https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock
scraped_at: 2026-11-07T17:20:04.533763+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * AWS Bedrock


On this page
# AWS Bedrock
Python dependency commands on this page use a [PM-prepared source checkout](https://hermes-agent.nousresearch.com/docs/reference/package-management#developer-workflow). After a dependency change, reactivate the checkout and restart Hermes.
Hermes Agent supports Amazon Bedrock as a native provider. This gives you full access to the Bedrock ecosystem: IAM authentication, Guardrails, cross-region inference profiles, and all foundation models.
Hermes routes each model family through the API that serves it best:  
| Model family  | API route  | Why  |  
| --- | --- | --- |  
| Anthropic Claude  | Anthropic SDK (`AnthropicBedrock`)  | Prompt caching, thinking budgets, adaptive thinking — features not exposed via Converse  |  
| OpenAI GPT-6 (Astra, Sol, Luna), GPT-6.1 (Sol, Terra), GPT-5.6 (Sol, Terra, Luna), GPT-5.5, GPT-5.4 with a bare `openai.*` ID  | Bedrock Mantle **OpenAI Responses** endpoint (`bedrock-mantle.<region>.api.aws/openai/v1`)  | Bedrock Mantle serves the bare in-Region ID. `bedrock-runtime` does not accept it  |  
| The same OpenAI models with a `us.` or `global.` inference-profile ID  | Native **Converse API** (`bedrock-runtime`)  | Cross-Region profiles exist only on `bedrock-runtime`, and the model cards list Converse as supported there  |  
| Everything else (Nova, DeepSeek, Llama, GPT-OSS, …)  | Native **Converse API** (`bedrock-runtime`)  | Full Bedrock feature set: Guardrails, inference profiles, streaming  |  
All three routes share the same AWS credential chain and region resolution — no separate configuration is needed. Requests to the Mantle endpoint are authenticated with `AWS_BEARER_TOKEN_BEDROCK` when set, or SigV4-signed via the standard boto3 credential chain otherwise.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#prerequisites "Direct link to Prerequisites")
  * **AWS credentials** — any source supported by the [boto3 credential chain](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html):
    * IAM instance role (EC2, ECS, Lambda — zero config)
    * `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` environment variables
    * `AWS_PROFILE` for SSO or named profiles
    * `aws configure` for local development
  * **boto3** — install with `cd ~/.hermes/hermes-agent && python -c "import pm; pm.sync_venv(['bedrock'], explicit=True)"`
  * **IAM permissions** — at minimum:
    * `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` (for inference)
    * `bedrock:ListFoundationModels` and `bedrock:ListInferenceProfiles` (for model discovery)
    * `bedrock:GetInferenceProfile` (only if `model.default` is an application inference profile ARN — used to size the context window from the wrapped model)


On AWS compute, attach an IAM role with `AmazonBedrockFullAccess` and you're done. No API keys, no `.env` configuration — Hermes detects the instance role automatically.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#quick-start "Direct link to Quick Start")

```


# Install with Bedrock support  





cd ~/.hermes/hermes-agent && python -c "import pm; pm.sync_venv(['bedrock'], explicit=True)"  





  





# Select Bedrock as your provider  





hermes model  





# → Choose "More providers..." → "AWS Bedrock"  





# → Select your region and model  





  





# Start chatting  





hermes chat  



```

## Configuration[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#configuration "Direct link to Configuration")
After running `hermes model`, your `~/.hermes/config.yaml` will contain:

```


model:  





  default: us.anthropic.claude-sonnet-4-6  





  provider: bedrock  





  base_url: https://bedrock-runtime.us-east-2.amazonaws.com  





  





bedrock:  





  region: us-east-2  



```

### Region[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#region "Direct link to Region")
Set the AWS region in any of these ways (highest priority first):
  1. `bedrock.region` in `config.yaml`
  2. `AWS_REGION` environment variable
  3. `AWS_DEFAULT_REGION` environment variable
  4. Default: `us-east-1`


### Guardrails[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#guardrails "Direct link to Guardrails")
To apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to all model invocations:

```


bedrock:  





  region: us-east-2  





  guardrail:  





    guardrail_identifier: "abc123def456"  # From the Bedrock console  





    guardrail_version: "1"                # Version number or "DRAFT"  





    stream_processing_mode: "async"       # "sync" or "async"  





    trace: "disabled"                     # "enabled", "disabled", or "enabled_full"  



```

The guardrail is attached on the Converse route (`guardrailConfig`) and on the Claude route (InvokeModel headers via the Anthropic Bedrock SDK, so prompt caching and thinking are kept). A blocked request surfaces as a content-filter refusal rather than as model text. `stream_processing_mode` only applies to Converse.
AWS does not apply Guardrails to the Mantle Responses endpoint used by bare `openai.gpt-*` IDs ([AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html)). Use a Converse-served model, such as a `us.` or `global.` OpenAI inference profile, when a guardrail is required.
### Model Discovery[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#model-discovery "Direct link to Model Discovery")
Hermes auto-discovers available models via the Bedrock control plane. You can customize discovery:

```


bedrock:  





  discovery:  





    enabled: true  





    provider_filter: ["anthropic", "amazon"]  # Only show these providers  





    refresh_interval: 3600                     # Cache for 1 hour  



```

### Prompt caching (cachePoint)[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#prompt-caching-cachepoint "Direct link to Prompt caching \(cachePoint\)")
Hermes automatically applies prompt caching on the Bedrock **Converse API** path by inserting `cachePoint` markers after the system prompt, tool definitions, and the latest message. Because sending a `cachePoint` block to a model that doesn't support it raises a `ValidationException`, markers are only added for models on a known-good allowlist (Anthropic Claude and Amazon Nova model IDs); unknown models default to no cache markers. Claude models normally use the AnthropicBedrock SDK path, which has its own prompt caching — the Converse `cachePoint` path covers Nova and the bearer-token Claude fallback. No configuration needed; cache reads/writes show up in usage accounting.
### Context-window probing[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#context-window-probing "Direct link to Context-window probing")
For models whose context window isn't in Hermes' static table, Hermes can probe the real limit by sending oversized requests at fixed tiers (~1.3M and ~2.2M tokens) and parsing the `maximum` reported in Bedrock's length-validation error. Probed values feed the same metadata cache as the static table; stale cached entries that under-report a model's window (e.g. entries seeded before a model's 1M window went GA) are dropped automatically in favor of the larger known value.
When the static table has no row for a model from Anthropic, OpenAI or xAI, Hermes uses that model family's window from its general model catalog (`agent/model_metadata.py`). This is how a new tier gets its real window before the Bedrock table is updated. Other vendors' catalog rows are vendor-direct windows that can exceed what Bedrock serves (Llama 3 8B is 8K on Bedrock), so those models do not borrow them.
When nothing knows a model, Hermes uses a 128,000-token fallback and logs a WARNING naming the model. The banner, status bar, `/usage`, `/model` and the gateway session line mark that window `fallback` so it is not mistaken for a detected limit. Set `model.context_length` (or `model_overrides.bedrock.<model id>.context_window`) in `config.yaml` to the model's real window.
**Application inference profiles.** An ARN such as `arn:aws:bedrock:us-west-2:123456789012:application-inference-profile/abcdef123456` names no model, so neither the probe nor the static table can size it. Hermes calls `bedrock:GetInferenceProfile` in the ARN's region and sizes the window from the model the profile wraps (1M for a profile wrapping Claude Sonnet 4.6). Without that permission the 128,000-token default applies and a WARNING names the profile; set `model.context_length` explicitly to override either way.
## Available Models[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#available-models "Direct link to Available Models")
Bedrock models use **inference profile IDs** for on-demand invocation. The `hermes model` picker shows these automatically, with recommended models at the top:  
| Model  | ID  | Notes  |  
| --- | --- | --- |  
| Claude Sonnet 4.6  | `us.anthropic.claude-sonnet-4-6`  | Recommended — best balance of speed and capability  |  
| Claude Opus 4.6  | `us.anthropic.claude-opus-4-6-v1`  | Most capable  |  
| Claude Haiku 4.5  | `us.anthropic.claude-haiku-4-5-20251001-v1:0`  | Fastest Claude  |  
| OpenAI GPT-6 Astra  | `openai.gpt-6-astra`  | Most capable OpenAI model, 1,050,000-token window  |  
| OpenAI GPT-6.1 Sol  | `openai.gpt-6.1-sol`  | 1M-token window. Mantle in-Region access is `us-east-1` only  |  
| OpenAI GPT-6.1 Terra  | `openai.gpt-6.1-terra`  | Balanced Terra tier, 1,050,000-token window  |  
| OpenAI GPT-6 Sol  | `openai.gpt-6-sol`  | Coding and agentic work, 1,050,000-token window  |  
| OpenAI GPT-6 Luna  | `openai.gpt-6-luna`  | Focused, high-volume tasks, 1,050,000-token window  |  
| OpenAI GPT-5.6 Sol  | `openai.gpt-5.6-sol`  | 1,050,000-token window  |  
| OpenAI GPT-5.6 Terra  | `openai.gpt-5.6-terra`  | Balanced, 1,050,000-token window  |  
| OpenAI GPT-5.6 Luna  | `openai.gpt-5.6-luna`  | Fast, affordable, 1,050,000-token window  |  
| OpenAI GPT-5.5  | `openai.gpt-5.5`  | Mantle only, no inference profiles  |  
| OpenAI GPT-5.4  | `openai.gpt-5.4`  | 1,050,000-token window  |  
| Amazon Nova Pro  | `us.amazon.nova-pro-v1:0`  | Amazon's flagship  |  
| Amazon Nova Micro  | `us.amazon.nova-micro-v1:0`  | Fastest, cheapest  |  
| DeepSeek V3.2  | `deepseek.v3.2`  | Strong open model  |  
| Llama 4 Scout 17B  | `us.meta.llama4-scout-17b-instruct-v1:0`  | Meta's latest  |  
Models prefixed with `us.` use cross-region inference profiles, which provide better capacity and automatic failover across AWS regions. Models prefixed with `global.` route across all available regions worldwide.
OpenAI models have two endpoint forms. The bare `openai.*` ID is in-Region and Hermes sends it to Bedrock Mantle's Responses endpoint in the configured region. The `us.openai.*` and `global.openai.*` IDs are cross-Region inference profiles. Hermes sends them to `bedrock-runtime` through the Converse API, the same path as other inference profiles. Each AWS model card lists the profiles a model offers and the regions Mantle serves it in.
## Switching Models Mid-Session[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#switching-models-mid-session "Direct link to Switching Models Mid-Session")
Use the `/model` command during a conversation:

```


/model us.amazon.nova-pro-v1:0  





/model deepseek.v3.2  





/model us.anthropic.claude-opus-4-6-v1  



```

## Diagnostics[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#diagnostics "Direct link to Diagnostics")

```


hermes doctor  



```

The doctor checks:
  * Whether AWS credentials are available (env vars, IAM role, SSO)
  * Whether `boto3` is installed
  * Whether the Bedrock API is reachable (ListFoundationModels)
  * Number of available models in your region


## Gateway (Messaging Platforms)[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#gateway-messaging-platforms "Direct link to Gateway \(Messaging Platforms\)")
Bedrock works with all Hermes gateway platforms (Telegram, Discord, Slack, Feishu, etc.). Configure Bedrock as your provider, then start the gateway normally:

```


hermes gateway setup  





hermes gateway start  



```

The gateway reads `config.yaml` and uses the same Bedrock provider configuration.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#troubleshooting "Direct link to Troubleshooting")
### "No API key found" / "No AWS credentials"[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#no-api-key-found--no-aws-credentials "Direct link to "No API key found" / "No AWS credentials"")
Hermes checks for credentials in this order:
  1. `AWS_BEARER_TOKEN_BEDROCK`
  2. `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`
  3. `AWS_PROFILE`
  4. EC2 instance metadata (IMDS)
  5. ECS container credentials
  6. Lambda execution role


If none are found, run `aws configure` or attach an IAM role to your compute instance.
### "Invocation of model ID ... with on-demand throughput isn't supported"[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#invocation-of-model-id--with-on-demand-throughput-isnt-supported "Direct link to "Invocation of model ID ... with on-demand throughput isn't supported"")
Use an **inference profile ID** (prefixed with `us.` or `global.`) instead of the bare foundation model ID. For example:
  * ❌ `anthropic.claude-sonnet-4-6`
  * ✅ `us.anthropic.claude-sonnet-4-6`


### "ThrottlingException"[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#throttlingexception "Direct link to "ThrottlingException"")
You've hit the Bedrock per-model rate limit. Hermes automatically retries with backoff. To increase limits, request a quota increase in the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/).
## One-Click AWS Deployment[​](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#one-click-aws-deployment "Direct link to One-Click AWS Deployment")
For a fully automated deployment on EC2 with CloudFormation:
**[sample-hermes-agent-on-aws-with-bedrock](https://github.com/JiaDe-Wu/sample-hermes-agent-on-aws-with-bedrock)** — creates VPC, IAM role, EC2 instance, and configures Bedrock automatically. Deploy in any region with one click.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/aws-bedrock.md)
[Previous Migrate from OpenClaw](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)[Next Google Vertex AI](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#prerequisites)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#quick-start)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#configuration)
    * [Region](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#region)
    * [Guardrails](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#guardrails)
    * [Model Discovery](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#model-discovery)
    * [Prompt caching (cachePoint)](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#prompt-caching-cachepoint)
    * [Context-window probing](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#context-window-probing)
  * [Available Models](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#available-models)
  * [Switching Models Mid-Session](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#switching-models-mid-session)
  * [Diagnostics](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#diagnostics)
  * [Gateway (Messaging Platforms)](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#gateway-messaging-platforms)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#troubleshooting)
    * ["No API key found" / "No AWS credentials"](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#no-api-key-found--no-aws-credentials)
    * ["Invocation of model ID ... with on-demand throughput isn't supported"](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#invocation-of-model-id--with-on-demand-throughput-isnt-supported)
    * ["ThrottlingException"](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#throttlingexception)
  * [One-Click AWS Deployment](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock#one-click-aws-deployment)


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
