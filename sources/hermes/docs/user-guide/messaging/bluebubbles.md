---
title: "BlueBubbles (iMessage)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles
scraped_at: 2026-11-07T17:19:55.777923+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Popular](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
    * [Microsoft 365](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
    * [Chinese platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
    * [Other](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
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
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Messaging Platforms
  * Other
  * BlueBubbles (iMessage)


On this page
# BlueBubbles (iMessage)
Connect Hermes to Apple iMessage via [BlueBubbles](https://bluebubbles.app/) — a free, open-source macOS server that bridges iMessage to any device.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#prerequisites "Direct link to Prerequisites")
  * A **Mac** (always on) running [BlueBubbles Server](https://bluebubbles.app/)
  * Apple ID signed into Messages.app on that Mac
  * BlueBubbles Server v1.0.0+ (webhooks require this version)
  * Network connectivity between Hermes and the BlueBubbles server


## Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#setup "Direct link to Setup")
### 1. Install BlueBubbles Server[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#1-install-bluebubbles-server "Direct link to 1. Install BlueBubbles Server")
Download and install from [bluebubbles.app](https://bluebubbles.app/). Complete the setup wizard — sign in with your Apple ID and configure a connection method (local network, Ngrok, Cloudflare, or Dynamic DNS).
### 2. Get your Server URL and Password[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#2-get-your-server-url-and-password "Direct link to 2. Get your Server URL and Password")
In BlueBubbles Server → **Settings → API** , note:
  * **Server URL** (e.g., `http://192.168.1.10:1234`)
  * **Server Password**


### 3. Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#3-configure-hermes "Direct link to 3. Configure Hermes")
Run the setup wizard:

```


hermes gateway setup  



```

Select **BlueBubbles (iMessage)** and enter your server URL and password.
Or set environment variables directly in `~/.hermes/.env`:

```


BLUEBUBBLES_SERVER_URL=http://192.168.1.10:1234  





BLUEBUBBLES_PASSWORD=your-server-password  



```

#### Optional: Require mentions in group chats[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#optional-require-mentions-in-group-chats "Direct link to Optional: Require mentions in group chats")
By default, Hermes responds to every authorized BlueBubbles/iMessage DM or group message. To make group chats opt-in, enable mention gating:

```


platforms:  





  bluebubbles:  





    enabled: true  





    extra:  





      require_mention: true  



```

With `require_mention: true`, DMs still work normally, but group-chat messages are ignored unless they match a mention pattern. If you do not configure custom patterns, Hermes uses conservative defaults for `Hermes` and `@Hermes agent` variants.
For a custom agent name, set regex patterns:

```


platforms:  





  bluebubbles:  





    extra:  





      require_mention: true  





      mention_patterns:  





        - '(?<![\w@])@?amos\b[,:\-]?'  



```

### 4. Authorize Users[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#4-authorize-users "Direct link to 4. Authorize Users")
Choose one approach:
**DM Pairing (recommended):** When someone messages your iMessage, Hermes automatically sends them a pairing code. Approve it with:

```


hermes pairing approve bluebubbles <CODE>  



```

Use `hermes pairing list` to see pending codes and approved users.
**Pre-authorize specific users** (in `~/.hermes/.env`):

```


BLUEBUBBLES_ALLOWED_USERS=user@icloud.com,+15551234567  



```

**Open access** (in `~/.hermes/.env`):

```


BLUEBUBBLES_ALLOW_ALL_USERS=true  



```

### 5. Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#5-start-the-gateway "Direct link to 5. Start the Gateway")

```


hermes gateway run  



```

Hermes will connect to your BlueBubbles server, register a webhook, and start listening for iMessage messages.
### 6. Verify the Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#6-verify-the-setup "Direct link to 6. Verify the Setup")
The setup wizard saves your credentials to `~/.hermes/.env` — it does **not** write `platforms.bluebubbles.enabled` into `~/.hermes/config.yaml`. With no explicit setting, present credentials are enough for the adapter to start; but an explicit `enabled: false` always wins over credentials, so if you previously disabled the adapter (for example, while using another iMessage bridge), the wizard will report success and the adapter will still never start.
Check the stored setting:

```


hermes config get platforms.bluebubbles.enabled  



```

  * `true` — explicitly enabled
  * `Config key not set` — no explicit setting; the `.env` credentials drive enablement
  * `false` — explicitly disabled; re-running setup will not flip this — set it to `true` yourself


Then check the gateway log for the two lines that prove the connection and the webhook registration:

```


hermes logs gateway  



```


```


[bluebubbles] connected to http://192.168.1.10:1234 (private_api=False, helper=False)  





[bluebubbles] webhook registered with server: http://localhost:8645/bluebubbles-webhook?password=***  



```

Finally, send yourself a test message from another device: a reply (or the pairing code for a new DM) is the end-to-end proof that inbound delivery works.
## How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#how-it-works "Direct link to How It Works")

```


iMessage → Messages.app → BlueBubbles Server → Webhook → Hermes  





Hermes → BlueBubbles REST API → Messages.app → iMessage  



```

  * **Inbound:** BlueBubbles sends webhook events to a local listener when new messages arrive. No polling — instant delivery.
  * **Outbound:** Hermes sends messages via the BlueBubbles REST API.
  * **Media:** Images, voice messages, videos, and documents are supported in both directions. Inbound attachments are downloaded and cached locally for the agent to process.


### Two URLs, opposite directions[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#two-urls-opposite-directions "Direct link to Two URLs, opposite directions")
The setup uses two URLs that point in opposite directions — don't confuse them:
  * `BLUEBUBBLES_SERVER_URL` (e.g. `http://192.168.1.10:1234`) — Hermes **calls** your BlueBubbles server's API. This is the Server URL shown in BlueBubbles Server → Settings → API.
  * The webhook (default `http://localhost:8645/bluebubbles-webhook`) — BlueBubbles **POSTs** new-message events to Hermes. Its host/port/path come from `BLUEBUBBLES_WEBHOOK_HOST` / `BLUEBUBBLES_WEBHOOK_PORT` / `BLUEBUBBLES_WEBHOOK_PATH`.


### How the webhook is registered[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#how-the-webhook-is-registered "Direct link to How the webhook is registered")
You do **not** need to create a webhook in the BlueBubbles UI. When the gateway connects, Hermes registers the webhook itself via the BlueBubbles REST API (`/api/v1/webhook`) for the `new-message` and `updated-message` events, and removes the registration again on clean shutdown.
Two details worth knowing:
  * The registered URL carries the server password as a query parameter (`?password=…`) because the BlueBubbles webhook API does not support custom headers — this is how inbound events are authenticated.
  * The webhook listener binds to `127.0.0.1` by default. That is fine when Hermes and BlueBubbles run on the same machine; if they are on different machines, set `BLUEBUBBLES_WEBHOOK_HOST` to an address the Mac running BlueBubbles can reach.


## Environment Variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#environment-variables "Direct link to Environment Variables")  
| Variable  | Required  | Default  | Description  |  
| --- | --- | --- | --- |  
| `BLUEBUBBLES_SERVER_URL`  | Yes  | —  | BlueBubbles server URL  |  
| `BLUEBUBBLES_PASSWORD`  | Yes  | —  | Server password  |  
| `BLUEBUBBLES_WEBHOOK_HOST`  | No  | `127.0.0.1`  | Webhook listener bind address  |  
| `BLUEBUBBLES_WEBHOOK_PORT`  | No  | `8645`  | Webhook listener port  |  
| `BLUEBUBBLES_WEBHOOK_PATH`  | No  | `/bluebubbles-webhook`  | Webhook URL path  |  
| `BLUEBUBBLES_HOME_CHANNEL`  | No  | —  | Phone/email for cron delivery  |  
| `BLUEBUBBLES_ALLOWED_USERS`  | No  | —  | Comma-separated authorized users  |  
| `BLUEBUBBLES_ALLOW_ALL_USERS`  | No  | `false`  | Allow all users  |  
| `BLUEBUBBLES_REQUIRE_MENTION`  | No  | `false`  | Require a mention pattern before responding in group chats  |  
| `BLUEBUBBLES_MENTION_PATTERNS`  | No  | Hermes wake words  | JSON array, newline-separated, or comma-separated regex patterns for group mention matching  |  
Auto-marking messages as read is controlled by the `send_read_receipts` key under `platforms.bluebubbles.extra` in `~/.hermes/config.yaml` (default: `true`). There is no corresponding environment variable.
## Features[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#features "Direct link to Features")
### Text Messaging[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#text-messaging "Direct link to Text Messaging")
Send and receive iMessages. Markdown is automatically stripped for clean plain-text delivery.
### Rich Media[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#rich-media "Direct link to Rich Media")
  * **Images:** Photos appear natively in the iMessage conversation
  * **Voice messages:** Audio files sent as iMessage voice messages
  * **Videos:** Video attachments
  * **Documents:** Files sent as iMessage attachments


### Tapback Reactions[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#tapback-reactions "Direct link to Tapback Reactions")
Love, like, dislike, laugh, emphasize, and question reactions. Requires the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation).
### Typing Indicators[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#typing-indicators "Direct link to Typing Indicators")
Shows "typing..." in the iMessage conversation while the agent is processing. Requires Private API.
### Read Receipts[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#read-receipts "Direct link to Read Receipts")
Automatically marks messages as read after processing. Requires Private API.
### Chat Addressing[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#chat-addressing "Direct link to Chat Addressing")
You can address chats by email or phone number — Hermes resolves them to BlueBubbles chat GUIDs automatically. No need to use raw GUID format.
## Private API[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#private-api "Direct link to Private API")
Some features require the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation):
  * Tapback reactions
  * Typing indicators
  * Read receipts
  * Creating new chats by address


Without the Private API, basic text messaging and media still work.
One caveat: "basic messaging works without Private API" assumes BlueBubbles can drive Messages.app in the foreground of a logged-in macOS user. If the Mac running BlueBubbles stays at the login screen or the server user is switched away from (Fast User Switching), AppleScript-based sending fails — see [BlueBubbles: multiple users on the same Mac](https://docs.bluebubbles.app/server/basic-guides/multiple-users-on-the-same-mac). In that setup the Private API is required for reliable sending, not just for the extras above.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#troubleshooting "Direct link to Troubleshooting")
### "Cannot reach server"[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#cannot-reach-server "Direct link to "Cannot reach server"")
  * Verify the server URL is correct and the Mac is on
  * Check that BlueBubbles Server is running
  * Ensure network connectivity (firewall, port forwarding)


### Messages not arriving[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#messages-not-arriving "Direct link to Messages not arriving")
  * Check `hermes logs gateway` for webhook errors (or `hermes logs -f` to follow in real-time)
  * Hermes registers the webhook itself on connect — only inspect BlueBubbles Server → Settings → API → Webhooks if the log shows a registration failure
  * A webhook row in the BlueBubbles UI is not proof of delivery; the end-to-end proof is Hermes logging the message and replying
  * If Hermes and BlueBubbles run on different machines, the default webhook bind address `127.0.0.1` is unreachable from the Mac — set `BLUEBUBBLES_WEBHOOK_HOST` to a reachable address and restart the gateway


### Setup succeeded, but the adapter never starts[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#setup-succeeded-but-the-adapter-never-starts "Direct link to Setup succeeded, but the adapter never starts")
  * `hermes gateway setup` saves credentials to `~/.hermes/.env`; it does not set `platforms.bluebubbles.enabled: true`
  * An explicit `enabled: false` in `~/.hermes/config.yaml` wins over credentials being present — check with `hermes config get platforms.bluebubbles.enabled`
  * This commonly bites after switching iMessage bridges: if you used another iMessage bridge and disabled BlueBubbles at the time, re-running setup will not re-enable it. Set `enabled: true` (and disable the bridge you no longer use — two iMessage bridges will double-handle messages)


### Two BlueBubbles servers on one Mac (wrong Apple ID)[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#two-bluebubbles-servers-on-one-mac-wrong-apple-id "Direct link to Two BlueBubbles servers on one Mac \(wrong Apple ID\)")
  * Hermes uses `BLUEBUBBLES_SERVER_URL` from `~/.hermes/.env`, not the Server URL shown in the BlueBubbles UI (which can be stale after a DHCP change)
  * Two macOS users on one Mac each run their own BlueBubbles server with its own API port and Apple ID — verify which one Hermes reaches: `curl "http://<server-url>/api/v1/server/info?password=<password>"` and compare the `computer_id`
  * For the multi-user setup itself, follow [BlueBubbles: multiple users on the same Mac](https://docs.bluebubbles.app/server/basic-guides/multiple-users-on-the-same-mac) — one port per user, and don't log out the user running the server


### Duplicate replies[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#duplicate-replies "Direct link to Duplicate replies")
  * Known issue: session handling can split one correspondent into two sessions (raw-GUID form vs. phone/email form) — tracked in [#30708](https://github.com/NousResearch/hermes-agent/issues/30708) and [#34372](https://github.com/NousResearch/hermes-agent/issues/34372)
  * Not a documentation or configuration problem — follow those issues for fixes


### "♻️ Recovered reply" repeats, or sends hang for minutes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#%EF%B8%8F-recovered-reply-repeats-or-sends-hang-for-minutes "Direct link to "♻️ Recovered reply" repeats, or sends hang for minutes")
  * If a `BLUEBUBBLES_HOME_CHANNEL` (or `platforms.bluebubbles.home_channel`) is configured, gateway restarts and platform reconnects notify the home channel and may re-deliver pending replies as "♻️ Recovered reply"
  * If sends on the BlueBubbles side silently fail — typically AppleScript errors like `Not authorized to send Apple events to Messages. (-1743)` with long timeouts on a background macOS user — the retries pile up and can crowd out webhook delivery
  * Leave the home channel empty until sending is proven reliable, and enable the Private API helper for background-user setups (see [Private API](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#private-api))


### "Private API helper not connected"[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#private-api-helper-not-connected "Direct link to "Private API helper not connected"")
  * Install the Private API helper: [docs.bluebubbles.app](https://docs.bluebubbles.app/helper-bundle/installation)
  * Basic messaging works without it — only reactions, typing, and read receipts require it


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/bluebubbles.md)
[Previous Matrix](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/matrix)[Next Buzz](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/buzz)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#prerequisites)
  * [Setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#setup)
    * [1. Install BlueBubbles Server](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#1-install-bluebubbles-server)
    * [2. Get your Server URL and Password](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#2-get-your-server-url-and-password)
    * [3. Configure Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#3-configure-hermes)
    * [4. Authorize Users](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#4-authorize-users)
    * [5. Start the Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#5-start-the-gateway)
    * [6. Verify the Setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#6-verify-the-setup)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#how-it-works)
    * [Two URLs, opposite directions](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#two-urls-opposite-directions)
    * [How the webhook is registered](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#how-the-webhook-is-registered)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#environment-variables)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#features)
    * [Text Messaging](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#text-messaging)
    * [Rich Media](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#rich-media)
    * [Tapback Reactions](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#tapback-reactions)
    * [Typing Indicators](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#typing-indicators)
    * [Read Receipts](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#read-receipts)
    * [Chat Addressing](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#chat-addressing)
  * [Private API](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#private-api)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#troubleshooting)
    * ["Cannot reach server"](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#cannot-reach-server)
    * [Messages not arriving](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#messages-not-arriving)
    * [Setup succeeded, but the adapter never starts](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#setup-succeeded-but-the-adapter-never-starts)
    * [Two BlueBubbles servers on one Mac (wrong Apple ID)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#two-bluebubbles-servers-on-one-mac-wrong-apple-id)
    * [Duplicate replies](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#duplicate-replies)
    * ["♻️ Recovered reply" repeats, or sends hang for minutes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#%EF%B8%8F-recovered-reply-repeats-or-sends-hang-for-minutes)
    * ["Private API helper not connected"](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles#private-api-helper-not-connected)


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
