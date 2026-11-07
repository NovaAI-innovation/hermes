---
title: "QQ Bot"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot
scraped_at: 2026-11-07T17:19:55.788043+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/qqbot)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Popular](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)
    * [Microsoft 365](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)
    * [Chinese platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/dingtalk)
      * [DingTalk](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/dingtalk)
      * [Feishu / Lark](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu)
      * [WeCom (Enterprise WeChat)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom)
      * [WeCom Callback (Self-Built App)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom-callback)
      * [Weixin (WeChat)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin)
      * [QQ Bot](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)
      * [Yuanbao](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)
    * [Other](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Messaging Platforms
  * Chinese platforms
  * QQ Bot


On this page
# QQ Bot
Python dependency commands on this page use a [PM-prepared source checkout](https://hermes-agent.nousresearch.com/docs/reference/package-management#developer-workflow). After a dependency change, reactivate the checkout and restart Hermes.
Connect Hermes to QQ via the **Official QQ Bot API (v2)** — supporting private (C2C), group @-mentions, guild, and direct messages with voice transcription.
## Overview[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#overview "Direct link to Overview")
The QQ Bot adapter uses the [Official QQ Bot API](https://bot.q.qq.com/wiki/develop/api-v2/) to:
  * Receive messages via a persistent **WebSocket** connection to the QQ Gateway
  * Send text and markdown replies via the **REST API**
  * Download and process images, voice messages, and file attachments
  * Transcribe voice messages using Tencent's built-in ASR or a configurable STT provider


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#prerequisites "Direct link to Prerequisites")
  1. **QQ Bot Application** — Register at [q.qq.com](https://q.qq.com):
     * Create a new application and note your **App ID** and **App Secret**
     * Enable the required intents: C2C messages, Group @-messages, Guild messages
     * Configure your bot in sandbox mode for testing, or publish for production
  2. **Dependencies** — The adapter requires `aiohttp` and `httpx`:

```


python -c "import pm; pm.sync_venv(['messaging'], explicit=True)"  



```



## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#configuration "Direct link to Configuration")
### Interactive setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#interactive-setup "Direct link to Interactive setup")

```


hermes gateway setup  



```

Select **QQ Bot** from the platform list and follow the prompts.
### Manual configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#manual-configuration "Direct link to Manual configuration")
Set the required environment variables in `~/.hermes/.env`:

```


QQ_APP_ID=your-app-id  





QQ_CLIENT_SECRET=your-app-secret  



```

## Environment Variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#environment-variables "Direct link to Environment Variables")  
| Variable  | Description  | Default  |  
| --- | --- | --- |  
| `QQ_APP_ID`  | QQ Bot App ID (required)  | —  |  
| `QQ_CLIENT_SECRET`  | QQ Bot App Secret (required)  | —  |  
| `QQBOT_HOME_CHANNEL`  | OpenID for cron/notification delivery  | —  |  
| `QQBOT_HOME_CHANNEL_NAME`  | Display name for home channel  | `Home`  |  
| `QQ_ALLOWED_USERS`  | Comma-separated user OpenIDs for DM access  | open (all users)  |  
| `QQ_GROUP_ALLOWED_USERS`  | Comma-separated group OpenIDs for group access  | —  |  
| `QQ_ALLOW_ALL_USERS`  | Set to `true` to allow all DMs  | `false`  |  
| `QQ_PORTAL_HOST`  | Override the QQ portal host (set to `sandbox.q.qq.com` for sandbox routing)  | `q.qq.com`  |  
| `QQ_STT_API_KEY`  | API key for voice-to-text provider  | —  |  
| `QQ_STT_BASE_URL`  | (Not read directly — set `platforms.qqbot.extra.stt.baseUrl` in `config.yaml` instead)  | n/a  |  
| `QQ_STT_MODEL`  | STT model name  | `glm-asr`  |  
## Advanced Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#advanced-configuration "Direct link to Advanced Configuration")
For fine-grained control, add platform settings to `~/.hermes/config.yaml`:

```


platforms:  





  qqbot:  





    enabled: true  





    extra:  





      app_id: "your-app-id"  





      client_secret: "your-secret"  





      markdown_support: true       # enable QQ markdown (msg_type 2). Config-only; no env-var equivalent.  





      dm_policy: "open"          # open | allowlist | disabled  





      allow_from:  





        - "user_openid_1"  





      group_policy: "open"       # open | allowlist | disabled  





      group_allow_from:  





        - "group_openid_1"  





      stt:  





        provider: "zai"          # zai (GLM-ASR), openai (Whisper), etc.  





        baseUrl: "https://open.bigmodel.cn/api/coding/paas/v4"  





        apiKey: "your-stt-key"  





        model: "glm-asr"  





        timeout: 60              # seconds per transcription request (default 60)  



```

## Voice Messages (STT)[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#voice-messages-stt "Direct link to Voice Messages \(STT\)")
Voice transcription works in two stages:
  1. **QQ built-in ASR** (free, always tried first) — QQ provides `asr_refer_text` in voice message attachments, which uses Tencent's own speech recognition
  2. **Configured STT provider** (fallback) — If QQ's ASR doesn't return text, the adapter calls an OpenAI-compatible STT API:
     * **Zhipu/GLM (zai)** : Default provider, uses `glm-asr` model
     * **OpenAI Whisper** : Set `QQ_STT_BASE_URL` and `QQ_STT_MODEL`
     * Any OpenAI-compatible STT endpoint


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#troubleshooting "Direct link to Troubleshooting")
### Bot disconnects immediately (quick disconnect)[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#bot-disconnects-immediately-quick-disconnect "Direct link to Bot disconnects immediately \(quick disconnect\)")
This usually means:
  * **Invalid App ID / Secret** — Double-check your credentials at q.qq.com
  * **Missing permissions** — Ensure the bot has the required intents enabled
  * **Sandbox-only bot** — If the bot is in sandbox mode, it can only receive messages from QQ's sandbox test channel


### Voice messages not transcribed[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#voice-messages-not-transcribed "Direct link to Voice messages not transcribed")
  1. Check if QQ's built-in `asr_refer_text` is present in the attachment data
  2. If using a custom STT provider, verify `QQ_STT_API_KEY` is set correctly
  3. Check gateway logs for STT error messages


### Messages not delivered[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#messages-not-delivered "Direct link to Messages not delivered")
  * Verify the bot's **intents** are enabled at q.qq.com
  * Check `QQ_ALLOWED_USERS` if DM access is restricted
  * For group messages, ensure the bot is **@mentioned** (group policy may require allowlisting)
  * Check `QQBOT_HOME_CHANNEL` for cron/notification delivery


### Connection errors[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#connection-errors "Direct link to Connection errors")
  * Ensure `aiohttp` and `httpx` are installed: `python -c "import pm; pm.sync_venv(['messaging'], explicit=True)"`
  * Check network connectivity to `api.sgroup.qq.com` and the WebSocket gateway
  * Review gateway logs for detailed error messages and reconnect behavior


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/qqbot.md)
[Previous Weixin (WeChat)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin)[Next Yuanbao](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)
  * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#overview)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#prerequisites)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#configuration)
    * [Interactive setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#interactive-setup)
    * [Manual configuration](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#manual-configuration)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#environment-variables)
  * [Advanced Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#advanced-configuration)
  * [Voice Messages (STT)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#voice-messages-stt)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#troubleshooting)
    * [Bot disconnects immediately (quick disconnect)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#bot-disconnects-immediately-quick-disconnect)
    * [Voice messages not transcribed](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#voice-messages-not-transcribed)
    * [Messages not delivered](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#messages-not-delivered)
    * [Connection errors](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot#connection-errors)


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
