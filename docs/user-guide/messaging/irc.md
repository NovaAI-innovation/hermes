---
title: "IRC"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc
scraped_at: 2026-11-07T17:19:55.782955+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/irc)


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
    * [Other](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
      * [A2A (Agent-to-Agent)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
      * [Home Assistant](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant)
      * [Mattermost](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/mattermost)
      * [Matrix](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix)
      * [BlueBubbles (iMessage)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
      * [Buzz](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/buzz)
      * [Photon iMessage](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/photon)
      * [Google Chat](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/google_chat)
      * [LINE](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/line)
      * [SimpleX Chat](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex)
      * [ntfy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/ntfy)
      * [IRC](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc)
      * [Open WebUI](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui)
      * [Hermes Relay](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/relay)
      * [Webhooks](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Messaging Platforms
  * Other
  * IRC


On this page
# IRC
The IRC adapter connects Hermes to any IRC server and relays messages between an IRC channel (or direct messages) and the agent. It speaks the IRC protocol over Python's stdlib `asyncio` — **no external dependencies, no SDK, no daemon**. It works with public networks like [Libera.Chat](https://libera.chat/) and any self-hosted ircd.
IRC is plain text: there is no voice, image, file, thread, reaction, typing, or streaming support — replies are sent as `PRIVMSG` lines, with long messages split to fit the IRC line limit.
> Run `hermes gateway setup` and pick **IRC** for a guided walk-through.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#prerequisites "Direct link to Prerequisites")
  * An IRC server to connect to (e.g. `irc.libera.chat`)
  * A channel to join (e.g. `#hermes`) — comma-separate to join several
  * A nickname for the bot (default: `hermes-bot`)
  * Optional: a registered nick + NickServ password if your network requires identification


## Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#configure-hermes "Direct link to Configure Hermes")
You can configure IRC two ways — environment variables (for a quick env-only setup) or the `gateway` block in `~/.hermes/config.yaml`.
### Option A — config.yaml[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#option-a--configyaml "Direct link to Option A — config.yaml")

```


gateway:  





  platforms:  





    irc:  





      enabled: true  





      extra:  





        server: irc.libera.chat  





        port: 6697  





        nickname: hermes-bot  





        channel: "#hermes"  





        use_tls: true  





        server_password: ""       # optional server password  





        nickserv_password: ""     # optional NickServ identification  





        allowed_users: []         # empty = allow all, or list of nicks  





        max_message_length: 450   # IRC line limit (safe default)  



```

### Option B — environment variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#option-b--environment-variables "Direct link to Option B — environment variables")  
| Variable  | Required  | Description  |  
| --- | --- | --- |  
| `IRC_SERVER`  | ✅  | IRC server hostname (e.g. `irc.libera.chat`)  |  
| `IRC_CHANNEL`  | ✅  | Channel(s) to join — comma-separate for multiple  |  
| `IRC_NICKNAME`  | ✅  | Bot nickname (default: `hermes-bot`)  |  
| `IRC_PORT`  | —  | Server port (default: `6697` with TLS, `6667` without)  |  
| `IRC_USE_TLS`  | —  | Use TLS (`true`/`false`; default `true` on port 6697)  |  
| `IRC_SERVER_PASSWORD`  | —  | Server password for the `PASS` command  |  
| `IRC_NICKSERV_PASSWORD`  | —  | NickServ password for automatic IDENTIFY on connect  |  
| `IRC_ALLOWED_USERS`  | —  | Comma-separated nicks allowed to talk to the bot  |  
| `IRC_ALLOW_ALL_USERS`  | —  | Allow anyone in the channel to talk to the bot (dev only)  |  
| `IRC_HOME_CHANNEL`  | —  | Channel for cron / notification delivery (defaults to `IRC_CHANNEL`)  |  
## Access control[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#access-control "Direct link to Access control")
By default, only nicks listed in `allowed_users` (or `IRC_ALLOWED_USERS`) may talk to the bot. Leave the list empty **and** set `IRC_ALLOW_ALL_USERS=true` to let anyone in the channel chat with Hermes — useful for testing, but not recommended on public networks since IRC nicks are not authenticated unless the network enforces NickServ.
If your network registers nicks, set `IRC_NICKSERV_PASSWORD` (or `nickserv_password`) so the bot identifies to NickServ on connect and keeps its registered nick.
## Channels vs. DMs[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#channels-vs-dms "Direct link to Channels vs. DMs")
  * Messages in a joined channel are treated as a **group** conversation.
  * Private messages to the bot are treated as **direct messages**.


Cron jobs and notifications are delivered to the **home channel** — `IRC_HOME_CHANNEL` if set, otherwise the first `IRC_CHANNEL`.
## Run the gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#run-the-gateway "Direct link to Run the gateway")

```


hermes gateway start  



```

Check status with `hermes gateway status` — IRC connection state is reported there, including for env-only setups.
## Notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#notes "Direct link to Notes")
  * Long agent replies are automatically split into multiple `PRIVMSG` lines to stay within the IRC line limit (`max_message_length`, default 450 bytes after protocol overhead).
  * The adapter acquires a scoped credential lock per server+nick, so two Hermes profiles won't fight over the same IRC identity.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/irc.md)
[Previous ntfy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/ntfy)[Next Open WebUI](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/open-webui)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#prerequisites)
  * [Configure Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#configure-hermes)
    * [Option A — config.yaml](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#option-a--configyaml)
    * [Option B — environment variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#option-b--environment-variables)
  * [Access control](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#access-control)
  * [Channels vs. DMs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#channels-vs-dms)
  * [Run the gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#run-the-gateway)
  * [Notes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/irc#notes)


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
