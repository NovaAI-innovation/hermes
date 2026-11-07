---
title: "Integrations Overview"
source: https://hermes-agent.nousresearch.com/docs/integrations
scraped_at: 2026-11-07T17:19:55.797942+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/integrations#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/integrations)
  * [English](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations/)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
    * [Overview](https://hermes-agent.nousresearch.com/docs/integrations/)
    * [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)
    * [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
    * [Buzz Integration](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
    * [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
    * [ACP Host Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
    * [Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
    * [Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)
    * [Credential Pools](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Integrations
  * Overview


On this page
# Integrations
Hermes Agent connects to external systems for AI inference, tool servers, IDE workflows, programmatic access, and more. These integrations extend what Hermes can do and where it can run.
If you only have time to set up one integration, set up [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal) — a single OAuth login covers 300+ models plus the four Tool Gateway tools (web search, image generation, TTS, and browser automation).
## AI Providers & Routing[​](https://hermes-agent.nousresearch.com/docs/integrations#ai-providers--routing "Direct link to AI Providers & Routing")
Hermes supports multiple AI inference providers out of the box. Use `hermes model` to configure interactively, or set them in `config.yaml`.
  * **[AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)** — OpenRouter, Anthropic, OpenAI, Google, and any OpenAI-compatible endpoint. Hermes auto-detects capabilities like vision, streaming, and tool use per provider.
  * **[Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)** — Fine-grained control over which underlying providers handle your OpenRouter requests. Optimize for cost, speed, or quality with sorting, whitelists, blacklists, and explicit priority ordering.
  * **[Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)** — Automatic failover to backup LLM providers when your primary model encounters errors. Includes primary model fallback and independent fallback for auxiliary tasks such as vision, compression, and title generation.


## Tool Servers (MCP)[​](https://hermes-agent.nousresearch.com/docs/integrations#tool-servers-mcp "Direct link to Tool Servers \(MCP\)")
  * **[MCP Servers](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)** — Connect Hermes to external tool servers via Model Context Protocol. Access tools from GitHub, databases, file systems, browser stacks, internal APIs, and more without writing native Hermes tools. Supports both stdio and SSE transports, per-server tool filtering, and capability-aware resource/prompt registration.


## Web Search Backends[​](https://hermes-agent.nousresearch.com/docs/integrations#web-search-backends "Direct link to Web Search Backends")
The `web_search` and `web_extract` tools support eight backend providers, configured via `config.yaml` or `hermes tools`:  
| Backend  | Env Var  | Search  | Extract  | Crawl  |  
| --- | --- | --- | --- | --- |  
|  **Firecrawl** (default)  | `FIRECRAWL_API_KEY`  | ✔  | ✔  | ✔  |  
| **SearXNG**  | `SEARXNG_URL`  | ✔  | —  | —  |  
|  **Brave** (free tier)  | `BRAVE_SEARCH_API_KEY`  | ✔  | —  | —  |  
|  **DuckDuckGo** (ddgs)  | _(none)_  | ✔  | —  | —  |  
| **Exa**  | `EXA_API_KEY`  | ✔  | ✔  | —  |  
| **Parallel**  | `PARALLEL_API_KEY`  | ✔  | ✔  | —  |  
| **xAI**  | `XAI_API_KEY`  | ✔  | —  | —  |  
Quick setup example:

```


web:  





  backend: firecrawl    # firecrawl | searxng | brave-free | ddgs | tavily | perplexity | keenable | exa | parallel | xai  



```

If `web.backend` is not set, the backend is auto-detected from whichever API key is available. Self-hosted Firecrawl is also supported via `FIRECRAWL_API_URL`.
## Browser Automation[​](https://hermes-agent.nousresearch.com/docs/integrations#browser-automation "Direct link to Browser Automation")
Hermes includes full browser automation through `browser_exec` (Python over CDP) for navigating websites, filling forms, and extracting information, with several places the browser can run:
  * **Browser Use Cloud** — Managed Chromium with stealth, residential proxies, CAPTCHA solving, and reusable browser profiles
  * **Browserbase** — Alternative cloud browser provider with managed browsers, anti-bot tooling, CAPTCHA solving, and residential proxies
  * **Local Chromium-family CDP** — Connect to your running Chrome, Brave, Chromium, or Edge browser using `/browser connect`
  * **Local Chromium** — Headless local Chromium that Hermes launches itself (the default)


The Camofox anti-detection browser is a catalog plugin: `hermes plugins install camofox`.
See [Browser Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser) for setup and usage.
## Voice & TTS Providers[​](https://hermes-agent.nousresearch.com/docs/integrations#voice--tts-providers "Direct link to Voice & TTS Providers")
Text-to-speech and speech-to-text across all messaging platforms:  
| Provider  | Quality  | Cost  | API Key  |  
| --- | --- | --- | --- |  
|  **Edge TTS** (default)  | Good  | Free  | None needed  |  
| **ElevenLabs**  | Excellent  | Paid  | `ELEVENLABS_API_KEY`  |  
| **OpenAI TTS**  | Good  | Paid  | `VOICE_TOOLS_OPENAI_KEY`  |  
| **MiniMax**  | Good  | Paid  | `MINIMAX_API_KEY`  |  
| **xAI TTS**  | Good  | Paid  | `XAI_API_KEY`  |  
| **NeuTTS**  | Good  | Free  | None needed  |  
Speech-to-text supports eight providers: local faster-whisper (free, runs on-device), a local command wrapper, Groq, OpenAI Whisper API, Mistral, xAI, ElevenLabs Scribe, and DeepInfra. Voice message transcription works across Telegram, Discord, WhatsApp, and other messaging platforms. See [Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts) and [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) for details.
## IDE & Editor Integration[​](https://hermes-agent.nousresearch.com/docs/integrations#ide--editor-integration "Direct link to IDE & Editor Integration")
  * **[IDE Integration (ACP)](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)** — Use Hermes Agent inside ACP-compatible editors such as VS Code, Zed, and JetBrains. Hermes runs as an ACP server, rendering chat messages, tool activity, file diffs, and terminal commands inside your editor.


## Programmatic Access[​](https://hermes-agent.nousresearch.com/docs/integrations#programmatic-access "Direct link to Programmatic Access")
  * **[API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)** — Expose Hermes as an OpenAI-compatible HTTP endpoint. Any frontend that speaks the OpenAI format — Open WebUI, LobeChat, LibreChat, NextChat, ChatBox — can connect and use Hermes as a backend with its full toolset.


## Memory & Personalization[​](https://hermes-agent.nousresearch.com/docs/integrations#memory--personalization "Direct link to Memory & Personalization")
  * **[Built-in Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)** — Persistent, curated memory via `MEMORY.md` and `USER.md` files. The agent maintains bounded stores of personal notes and user profile data that survive across sessions.
  * **[Memory Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)** — Plug in external memory backends for deeper personalization. Two providers ship with Hermes: RetainDB (hybrid search) and ByteRover (CLI-based); Honcho (dialectic reasoning), Hindsight (knowledge graphs), Supermemory (semantic recall), Mem0 (cloud extraction), OpenViking (tiered retrieval) and Holographic (local SQLite) are available from the plugin catalog via `hermes plugins install <name>`.


## Messaging Platforms[​](https://hermes-agent.nousresearch.com/docs/integrations#messaging-platforms "Direct link to Messaging Platforms")
Hermes runs as a gateway bot on 27+ messaging platforms, all configured through the same `gateway` subsystem:
  * **[Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)** , **[Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)** , **[Slack](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack)** , **[WhatsApp](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp)** , **[Signal](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/signal)** , **[Matrix](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix)** , **[Mattermost](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost)** , **[Email](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/email)** , **[SMS](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/sms)** , **[DingTalk](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/dingtalk)** , **[Feishu/Lark](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu)** , **[WeCom](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom)** , **[WeCom Callback](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom-callback)** , **[Weixin](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin)** , **[BlueBubbles](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)** , **[Buzz](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/buzz)** , **[QQ Bot](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)** , **[Yuanbao](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)** , **[Home Assistant](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant)** (plugin), **[Microsoft Teams](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)** , **[Microsoft Teams Meetings](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings)** , **[Microsoft Graph Webhook](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/msgraph-webhook)** , **[Google Chat](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/google_chat)** , **[LINE](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/line)** , **[ntfy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/ntfy)** , **[SimpleX](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex)** , **[Open WebUI](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui)** , **[Webhooks](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks)**


See the [Messaging Gateway overview](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) for the platform comparison table and setup guide.
### Quick connect links[​](https://hermes-agent.nousresearch.com/docs/integrations#quick-connect-links "Direct link to Quick connect links")
The big platforms have a canonical "create your bot/app" URL, and some accept parameters that pre-open the right form. Skip the console-hunting and go straight there:  
| Platform  | Direct link  | What it opens  |  
| --- | --- | --- |  
| **Telegram**  | [t.me/BotFather](https://t.me/BotFather)  | Chat with BotFather — send `/newbot` to mint a bot token  |  
| **Discord**  | [discord.com/developers/applications?new_application=true](https://discord.com/developers/applications?new_application=true)  | Developer Portal with the **New Application** dialog pre-opened  |  
| **Slack**  | [api.slack.com/apps?new_app=1](https://api.slack.com/apps?new_app=1)  | The **Create New App** dialog — pick _From an app manifest_ and paste the manifest `hermes slack manifest --agent-view` generates  |  
| **LINE**  | [developers.line.biz/console](https://developers.line.biz/console/)  | LINE Developers Console for creating a Messaging API channel  |  
| **Feishu/Lark**  | [open.feishu.cn/app](https://open.feishu.cn/app)  | Feishu open-platform console for creating a custom app  |  
Each platform's setup page walks through what to do once you're there.
## Collaboration Workspaces[​](https://hermes-agent.nousresearch.com/docs/integrations#collaboration-workspaces "Direct link to Collaboration Workspaces")
  * **[Buzz](https://hermes-agent.nousresearch.com/docs/integrations/buzz)** — Block's Nostr-based human+agent workspace. Three integration paths: Buzz Desktop spawns Hermes as a managed ACP runtime, the `buzz-acp` relay bridge hosts a Hermes identity server-side, or the native gateway platform joins Buzz channels with full Hermes memory/skills/approvals/cron. The overview page compares all three.


## Home Automation[​](https://hermes-agent.nousresearch.com/docs/integrations#home-automation "Direct link to Home Automation")
  * **[Home Assistant](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant)** — Control smart home devices via four dedicated tools (`ha_list_entities`, `ha_get_state`, `ha_list_services`, `ha_call_service`) and react to real-time state changes through the gateway. Ships as the `homeassistant` catalog plugin (`hermes plugins install homeassistant`); its toolset activates automatically when `HASS_TOKEN` is configured.


## Plugins[​](https://hermes-agent.nousresearch.com/docs/integrations#plugins "Direct link to Plugins")
  * **[Plugin System](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)** — Extend Hermes with custom tools, lifecycle hooks, and CLI commands without modifying core code. Plugins are discovered from `~/.hermes/plugins/`, project-local `.hermes/plugins/`, and pip-installed entry points.
  * **[Build a Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)** — Step-by-step guide for creating Hermes plugins with tools, hooks, and CLI commands.


## Training & Evaluation[​](https://hermes-agent.nousresearch.com/docs/integrations#training--evaluation "Direct link to Training & Evaluation")
  * **[Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing)** — Run the agent across hundreds of prompts in parallel, generating structured ShareGPT-format trajectory data for training data generation or evaluation.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/integrations/index.md)
[Previous Webhooks](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks)[Next Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)
  * [AI Providers & Routing](https://hermes-agent.nousresearch.com/docs/integrations#ai-providers--routing)
  * [Tool Servers (MCP)](https://hermes-agent.nousresearch.com/docs/integrations#tool-servers-mcp)
  * [Web Search Backends](https://hermes-agent.nousresearch.com/docs/integrations#web-search-backends)
  * [Browser Automation](https://hermes-agent.nousresearch.com/docs/integrations#browser-automation)
  * [Voice & TTS Providers](https://hermes-agent.nousresearch.com/docs/integrations#voice--tts-providers)
  * [IDE & Editor Integration](https://hermes-agent.nousresearch.com/docs/integrations#ide--editor-integration)
  * [Programmatic Access](https://hermes-agent.nousresearch.com/docs/integrations#programmatic-access)
  * [Memory & Personalization](https://hermes-agent.nousresearch.com/docs/integrations#memory--personalization)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/integrations#messaging-platforms)
    * [Quick connect links](https://hermes-agent.nousresearch.com/docs/integrations#quick-connect-links)
  * [Collaboration Workspaces](https://hermes-agent.nousresearch.com/docs/integrations#collaboration-workspaces)
  * [Home Automation](https://hermes-agent.nousresearch.com/docs/integrations#home-automation)
  * [Plugins](https://hermes-agent.nousresearch.com/docs/integrations#plugins)
  * [Training & Evaluation](https://hermes-agent.nousresearch.com/docs/integrations#training--evaluation)


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
