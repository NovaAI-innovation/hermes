---
title: "Yuanbao"
source: "https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao"
scraped_at: "2026-11-07T17:19:55.796942+00:00"
doc_id: "user-guide/messaging/yuanbao"
content_hash: "eddfb7802a8b1c0f"
corpus_source: "hermes"
---

# Yuanbao
Yuanbao is now a Hermes Labs plugin: built by Nous Research, not supported, and likely not maintained going forward. Fixes from the community are welcome.
The [Yuanbao](https://yuanbao.tencent.com/) gateway platform and its `yb_*` tools (`yb_query_group_info`, `yb_query_group_members`, `yb_send_dm`, `yb_search_sticker`, `yb_send_sticker`) are no longer part of Hermes core. They ship as the `yuanbao` plugin in [NousResearch/hermes-labs-plugins](https://github.com/NousResearch/hermes-labs-plugins/tree/main/yuanbao), which carries the full setup guide.
## Install

```

hermes plugins install yuanbao

```

Plugins are installed per profile; use `hermes -p <profile> plugins install yuanbao` for another profile. Restart the gateway afterwards so it serves the platform.
Every name stays the same: the `YUANBAO_*` environment variables (`YUANBAO_APP_ID` or the legacy `YUANBAO_APP_KEY`, `YUANBAO_APP_SECRET`, `YUANBAO_HOME_CHANNEL`, ...), the `platforms.yuanbao` block (and the legacy `gateway.yuanbao` block) in `config.yaml`, the `yuanbao` toolset and the tool names.
Nothing to do. Every profile that was already using Yuanbao (`YUANBAO_APP_ID` or `YUANBAO_APP_KEY` plus `YUANBAO_APP_SECRET` in its `.env`, `platforms.yuanbao` enabled in `config.yaml`, or the `yuanbao` / `hermes-yuanbao` toolset listed for another platform) gets the plugin installed automatically from the catalog by `hermes update`, or the first time the profile starts (agent or gateway start; this honours `security.allow_lazy_installs`). A failed attempt is retried with a backoff; `hermes update` always retries. This happens once per profile: if you later remove the plugin (`hermes plugins remove yuanbao`), it stays removed.
