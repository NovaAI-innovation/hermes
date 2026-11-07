---
title: "SimpleX Chat"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex
scraped_at: 2026-11-07T17:19:55.790165+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/simplex)


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
  * SimpleX Chat


On this page
# SimpleX Chat
[SimpleX Chat](https://simplex.chat/) is a private, decentralised messaging platform where users own their contacts and groups. Unlike other platforms, SimpleX assigns no persistent user IDs — every contact is identified by an opaque internal ID generated at connection time, which makes it one of the most private messengers available.
> Run `hermes gateway setup` and pick **SimpleX** for a guided walk-through.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#prerequisites "Direct link to Prerequisites")
  * The **simplex-chat** CLI installed and running as a daemon
  * Python package **websockets** (`hermes pm repair`)


## Install simplex-chat[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#install-simplex-chat "Direct link to Install simplex-chat")
Download the latest release from the [simplex-chat GitHub releases](https://github.com/simplex-chat/simplex-chat/releases) page:

```


# Linux / macOS binary  





curl -L https://github.com/simplex-chat/simplex-chat/releases/latest/download/simplex-chat-ubuntu-22_04-x86_64 -o simplex-chat  





chmod +x simplex-chat  



```

The SimpleX Chat project does not publish a prebuilt Docker image for the chat client; to run it under Docker, build from source from the [simplex-chat repository](https://github.com/simplex-chat/simplex-chat).
## Start the daemon[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#start-the-daemon "Direct link to Start the daemon")

```


simplex-chat -p 5225  



```

The daemon listens on WebSocket at `ws://127.0.0.1:5225` by default.
## Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#configure-hermes "Direct link to Configure Hermes")
### Via setup wizard[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#via-setup-wizard "Direct link to Via setup wizard")

```


hermes gateway setup  



```

Select **SimpleX Chat** and follow the prompts.
### Via environment variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#via-environment-variables "Direct link to Via environment variables")
Add these to `~/.hermes/.env`:

```


SIMPLEX_WS_URL=ws://127.0.0.1:5225  





SIMPLEX_ALLOWED_USERS=<contact-id-1>,<contact-id-2>  





SIMPLEX_HOME_CHANNEL=<contact-id>  



```
  
| Variable  | Required  | Description  |  
| --- | --- | --- |  
| `SIMPLEX_WS_URL`  | Yes  | WebSocket URL of the simplex-chat daemon  |  
| `SIMPLEX_ALLOWED_USERS`  | Recommended  | Comma-separated allowlist of numeric `contactId`s. Display names are **not** accepted — any contact can change theirs.  |  
| `SIMPLEX_ALLOW_ALL_USERS`  | Optional  | Set `true` to allow every contact (use carefully)  |  
| `SIMPLEX_AUTO_ACCEPT`  | Optional  | Auto-accept incoming contact requests (default: `true`)  |  
| `SIMPLEX_GROUP_ALLOWED`  | Optional  | Comma-separated group IDs the bot participates in, or `*` for any group. Omit to ignore group messages entirely  |  
| `SIMPLEX_HOME_CHANNEL`  | Optional  | Default contact/group ID for cron job delivery  |  
| `SIMPLEX_HOME_CHANNEL_NAME`  | Optional  | Human label for the home channel  |  
| `HERMES_SIMPLEX_TEXT_BATCH_DELAY`  | Optional  | Quiet-period seconds (default: `0.8`) used to concatenate rapid-fire inbound text messages into one event  |  
## Find your contact ID[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#find-your-contact-id "Direct link to Find your contact ID")
After starting the daemon, open a conversation with your agent contact. The numeric `contactId` appears in session logs (or run `/contacts` in the daemon). `SIMPLEX_ALLOWED_USERS` matches only this ID: display names are chosen by the contact and can collide, so they are ignored.
## Authorization[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#authorization "Direct link to Authorization")
By default **all contacts are denied**. You must either:
  1. Set `SIMPLEX_ALLOWED_USERS` to a comma-separated list of numeric `contactId`s (e.g. `SIMPLEX_ALLOWED_USERS=4,9`), or
  2. Use **DM pairing** — send any message to the bot and it will reply with a pairing code. Enter that code via `hermes pairing approve simplex <CODE>`.


## Group chats[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#group-chats "Direct link to Group chats")
By default the adapter ignores group messages — a bot in a group otherwise processes every member's traffic. Opt-in explicitly:

```


SIMPLEX_GROUP_ALLOWED=12,34          # specific group IDs  





# or  





SIMPLEX_GROUP_ALLOWED=*              # any group the bot is in  



```

Address groups by prefixing the chat ID with `group:`, e.g. `simplex:group:12` as a cron `deliver=` target or in a `hermes send` call.
## Sending with `hermes send`[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#sending-with-hermes-send "Direct link to sending-with-hermes-send")
SimpleX works as a standalone send target — the daemon must be running, but a live gateway is not required for plain text:

```


hermes send --to simplex:alice "hello"          # DM by contact display name  





hermes send --to simplex:group:12 "hello"       # group by numeric ID  





hermes send --to simplex "hello"                # SIMPLEX_HOME_CHANNEL  



```

While the gateway is running, the adapter enumerates your contacts and allowed groups into the channel directory (refreshed every 5 minutes), so `hermes send --list` shows them by name. Before the first gateway run the platform still appears in `--list` with a "no channels discovered yet" hint — direct targets like the ones above work regardless.
## Attachments[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#attachments "Direct link to Attachments")
The adapter supports native SimpleX attachments in both directions:
  * **Inbound** — incoming images, voice notes, and files are accepted via the daemon's XFTP flow (`rcvFileDescrReady` → `/freceive` → wait for `rcvFileComplete`) and surfaced as `MessageEvent.media_urls` with the appropriate `MessageType` (`PHOTO`, `VOICE`, `TEXT` + document).
  * **Outbound** — `send_image_file`, `send_voice`, `send_document`, and `send_video` all use the structured `/_send` form with `filePath`, so the receiving SimpleX client renders images inline and plays voice notes inline rather than offering them as downloads.


Agent replies can also embed `MEDIA:/path/to/file` tags in plain text — the adapter strips the tag from the body and sends the file as either a voice note (audio extensions) or a document.
## Using SimpleX with cron jobs[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#using-simplex-with-cron-jobs "Direct link to Using SimpleX with cron jobs")

```


cronjob(  





    action="create",  





    schedule="every 1h",  





    deliver="simplex",          # uses SIMPLEX_HOME_CHANNEL  





    prompt="Check for alerts and summarise."  





)  



```

Or target a specific contact via the cron job's `deliver:` field, or from a shell script with the [`hermes send` CLI](https://hermes-agent.nousresearch.com/docs/guides/pipe-script-output):

```


hermes send simplex:<contact-id> "Done!"  



```

## Privacy notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#privacy-notes "Direct link to Privacy notes")
  * SimpleX never reveals phone numbers or email addresses — contacts use opaque IDs
  * The connection between Hermes and the daemon is local WebSocket (`ws://127.0.0.1:5225`) — no data leaves your machine
  * Messages are end-to-end encrypted by the SimpleX protocol before reaching the daemon


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#troubleshooting "Direct link to Troubleshooting")
**"Cannot reach daemon"** — Ensure `simplex-chat -p 5225` is running and the port matches `SIMPLEX_WS_URL`.
**"websockets not installed"** — Run `hermes pm repair`.
**Messages not received** — Check that the contact's ID is in `SIMPLEX_ALLOWED_USERS` or approve them via DM pairing.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/simplex.md)
[Previous LINE](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/line)[Next ntfy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/ntfy)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#prerequisites)
  * [Install simplex-chat](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#install-simplex-chat)
  * [Start the daemon](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#start-the-daemon)
  * [Configure Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#configure-hermes)
    * [Via setup wizard](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#via-setup-wizard)
    * [Via environment variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#via-environment-variables)
  * [Find your contact ID](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#find-your-contact-id)
  * [Authorization](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#authorization)
  * [Group chats](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#group-chats)
  * [Sending with `hermes send`](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#sending-with-hermes-send)
  * [Attachments](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#attachments)
  * [Using SimpleX with cron jobs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#using-simplex-with-cron-jobs)
  * [Privacy notes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#privacy-notes)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/simplex#troubleshooting)


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
