---
title: "Yuanbao"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao
scraped_at: 2026-11-07T17:19:55.796942+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/yuanbao)


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
  * Yuanbao


On this page
# Yuanbao
Yuanbao is now a Hermes Labs plugin: built by Nous Research, not supported, and likely not maintained going forward. Fixes from the community are welcome.
The [Yuanbao](https://yuanbao.tencent.com/) gateway platform and its `yb_*` tools (`yb_query_group_info`, `yb_query_group_members`, `yb_send_dm`, `yb_search_sticker`, `yb_send_sticker`) are no longer part of Hermes core. They ship as the `yuanbao` plugin in [NousResearch/hermes-labs-plugins](https://github.com/NousResearch/hermes-labs-plugins/tree/main/yuanbao), which carries the full setup guide.
## Install[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao#install "Direct link to Install")

```


hermes plugins install yuanbao  



```

Plugins are installed per profile; use `hermes -p <profile> plugins install yuanbao` for another profile. Restart the gateway afterwards so it serves the platform.
Every name stays the same: the `YUANBAO_*` environment variables (`YUANBAO_APP_ID` or the legacy `YUANBAO_APP_KEY`, `YUANBAO_APP_SECRET`, `YUANBAO_HOME_CHANNEL`, ...), the `platforms.yuanbao` block (and the legacy `gateway.yuanbao` block) in `config.yaml`, the `yuanbao` toolset and the tool names.
Nothing to do. Every profile that was already using Yuanbao (`YUANBAO_APP_ID` or `YUANBAO_APP_KEY` plus `YUANBAO_APP_SECRET` in its `.env`, `platforms.yuanbao` enabled in `config.yaml`, or the `yuanbao` / `hermes-yuanbao` toolset listed for another platform) gets the plugin installed automatically from the catalog by `hermes update`, or the first time the profile starts (agent or gateway start; this honours `security.allow_lazy_installs`). A failed attempt is retried with a backoff; `hermes update` always retries. This happens once per profile: if you later remove the plugin (`hermes plugins remove yuanbao`), it stays removed.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/yuanbao.md)
[Previous QQ Bot](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)[Next A2A (Agent-to-Agent)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Install](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao#install)


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
