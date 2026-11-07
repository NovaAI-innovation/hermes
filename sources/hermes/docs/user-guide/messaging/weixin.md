---
title: "Weixin (WeChat)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin
scraped_at: 2026-11-07T17:19:55.794949+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/weixin)


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
  * Weixin (WeChat)


On this page
# Weixin (WeChat)
Python dependency commands on this page use a [PM-prepared source checkout](https://hermes-agent.nousresearch.com/docs/reference/package-management#developer-workflow). After a dependency change, reactivate the checkout and restart Hermes.
Connect Hermes to [WeChat](https://weixin.qq.com/) (微信), Tencent's personal messaging platform. The adapter uses Tencent's **iLink Bot API** for personal WeChat accounts — this is distinct from WeCom (Enterprise WeChat). Messages are delivered via long-polling, so no public endpoint or webhook is required.
This adapter is for **personal WeChat accounts** (微信). If you need enterprise/corporate WeChat, see the [WeCom adapter](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom) instead.
QR login connects Hermes to an **iLink bot identity** (e.g. `a5ace6fd482e@im.bot`), **not** a fully scriptable ordinary personal WeChat account. Consequences:
  * The iLink bot identity generally **cannot be invited into ordinary WeChat groups** the way a normal contact can.
  * iLink typically **does not deliver ordinary WeChat group events** (including `@`-mentions of the personal account used for QR login) to the gateway for most bot-type accounts.
  * `@`-mentioning the personal WeChat account used to scan the QR code is **not** the same as `@`-mentioning the iLink bot — the bot is a separate identity.
  * The `WEIXIN_GROUP_POLICY` / `WEIXIN_GROUP_ALLOWED_USERS` settings below only take effect when iLink actually returns group events for your account type. If it doesn't, group messages will never reach Hermes regardless of policy.


In practice, most deployments only get DMs to the iLink bot working reliably. If group delivery doesn't work after configuration, the limitation is on the iLink side, not in Hermes. The gateway logs a `WARNING` at startup whenever `WEIXIN_GROUP_POLICY` is set to anything other than `disabled`.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#prerequisites "Direct link to Prerequisites")
  * A personal WeChat account
  * Python packages: `aiohttp` and `cryptography`
  * Terminal QR rendering is included when Hermes is installed with the `messaging` extra


Install the required dependencies:

```


# Includes aiohttp and terminal QR code support  





python -c "import pm; pm.sync_venv(['messaging'], explicit=True)"  



```

## Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#setup "Direct link to Setup")
### 1. Run the Setup Wizard[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#1-run-the-setup-wizard "Direct link to 1. Run the Setup Wizard")
The easiest way to connect your WeChat account is through the interactive setup:

```


hermes gateway setup  



```

Select **Weixin** when prompted. The wizard will:
  1. Request a QR code from the iLink Bot API
  2. Display the QR code in your terminal (or provide a URL)
  3. Wait for you to scan the QR code with the WeChat mobile app
  4. Prompt you to confirm the login on your phone
  5. Save the account credentials automatically to `~/.hermes/weixin/accounts/`


Once confirmed, you'll see a message like:

```


微信连接成功，account_id=your-account-id  



```

The wizard stores the `account_id`, `token`, and `base_url` so you don't need to configure them manually.
### 2. Configure Environment Variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#2-configure-environment-variables "Direct link to 2. Configure Environment Variables")
After initial QR login, set at minimum the account ID in `~/.hermes/.env`:

```


WEIXIN_ACCOUNT_ID=your-account-id  





  





# Optional: override the token (normally auto-saved from QR login)  





# WEIXIN_TOKEN=your-bot-token  





  





# Optional: restrict access  





WEIXIN_DM_POLICY=open  





WEIXIN_ALLOWED_USERS=user_id_1,user_id_2  





  





# Optional: restore legacy multiline splitting behavior  





# WEIXIN_SPLIT_MULTILINE_MESSAGES=true  





  





# Optional: home channel for cron/notifications  





WEIXIN_HOME_CHANNEL=chat_id  





WEIXIN_HOME_CHANNEL_NAME=Home  



```

### 3. Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#3-start-the-gateway "Direct link to 3. Start the Gateway")

```


hermes gateway  



```

The adapter will restore saved credentials, connect to the iLink API, and begin long-polling for messages.
## Features[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#features "Direct link to Features")
  * **Long-poll transport** — no public endpoint, webhook, or WebSocket needed
  * **QR code login** — scan-to-connect setup via `hermes gateway setup`
  * **DM messaging** — configurable access policies; group messaging depends on iLink actually delivering group events for the connected identity (often not the case for iLink bot accounts — see the warning above)
  * **Media support** — images, video, files, and voice messages
  * **AES-128-ECB encrypted CDN** — automatic encryption/decryption for all media transfers
  * **Context token persistence** — disk-backed reply continuity across restarts
  * **Markdown formatting** — preserves Markdown, including headers, tables, and code blocks, so WeChat clients that support Markdown can render it natively
  * **Smart message chunking** — messages stay as a single bubble when under the limit; only oversized payloads split at logical boundaries
  * **Typing indicators** — shows "typing…" status in the WeChat client while the agent processes
  * **SSRF protection** — outbound media URLs are validated before download
  * **Message deduplication** — 5-minute sliding window prevents double-processing
  * **Automatic retry with backoff** — recovers from transient API errors


## Configuration Options[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#configuration-options "Direct link to Configuration Options")
Set these in `config.yaml` under `platforms.weixin.extra`:  
| Key  | Default  | Description  |  
| --- | --- | --- |  
| `account_id`  | —  | iLink Bot account ID (required)  |  
| `token`  | —  | iLink Bot token (required, auto-saved from QR login)  |  
| `base_url`  | `https://ilinkai.weixin.qq.com`  | iLink API base URL  |  
| `cdn_base_url`  | `https://novac2c.cdn.weixin.qq.com/c2c`  | CDN base URL for media transfer  |  
| `dm_policy`  | `open`  | DM access: `open`, `allowlist`, `disabled`, `pairing`  |  
| `group_policy`  | `disabled`  | Group access: `open`, `allowlist`, `disabled`  |  
| `allow_from`  | `[]`  | User IDs allowed for DMs (when dm_policy=allowlist)  |  
| `group_allow_from`  | `[]`  | Group IDs allowed (when group_policy=allowlist)  |  
| `split_multiline_messages`  | `false`  | When `true`, split multi-line replies into multiple chat messages (legacy behavior). When `false`, keep multi-line replies as one message unless they exceed the length limit.  |  
| `text_batch_delay_seconds`  | `0.3`  | Quiet period (seconds, max `2.0`) before a buffered burst of rapid text messages is flushed as one combined request. iLink delivers messages individually, so this debounce avoids one agent invocation per fragment. Set `0` to dispatch each message immediately.  |  
| `text_batch_split_delay_seconds`  | `1.0`  | Extended flush delay (max `4.0`; never below `text_batch_delay_seconds`) used when the latest fragment is near the split threshold (long messages iLink may have chunked).  |  
## Access Policies[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#access-policies "Direct link to Access Policies")
### DM Policy[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#dm-policy "Direct link to DM Policy")
Controls who can send direct messages to the bot:  
| Value  | Behavior  |  
| --- | --- |  
| `open`  | Anyone can DM the bot (default)  |  
| `allowlist`  | Only user IDs in `allow_from` can DM  |  
| `disabled`  | All DMs are ignored  |  
| `pairing`  | Pairing mode (for initial setup)  |  

```


WEIXIN_DM_POLICY=allowlist  





WEIXIN_ALLOWED_USERS=user_id_1,user_id_2  



```

`WEIXIN_ALLOWED_USERS` is an **inbound filter** , not an invitation system. QR login connects one iLink bot identity to Hermes. Other people do not scan the Hermes QR code with their own accounts; they must message the connected iLink bot/contact through WeChat, and Hermes will process the DM only if the sender's Weixin user ID is present in `WEIXIN_ALLOWED_USERS`.
A practical setup flow is:
  1. Pair Hermes once with `hermes gateway setup` and note the connected iLink bot account.
  2. Have each allowed user send a direct message to that bot/contact.
  3. Read the sender/user ID from the gateway logs or the inbound event payload.
  4. Add those IDs to `WEIXIN_ALLOWED_USERS`, then restart the gateway.


If only the account that scanned the QR code can talk to Hermes, verify that the other users are messaging the iLink bot identity itself, not the personal WeChat account that performed the QR login. The iLink bot is a separate identity, and ordinary WeChat contact/group routing can be limited by Tencent's iLink behavior.
### Group Policy[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#group-policy "Direct link to Group Policy")
Controls which groups the bot responds in **when iLink delivers group events for the connected identity**. For QR-login iLink bot identities (e.g. `...@im.bot`), group events are typically not delivered at all, so this policy may have no effect — see the iLink bot limitation warning at the top of the page.  
| Value  | Behavior  |  
| --- | --- |  
| `open`  | Bot responds in all groups (if events are delivered)  |  
| `allowlist`  | Bot only responds in group IDs listed in `group_allow_from` (if events are delivered)  |  
| `disabled`  | All group messages are ignored (default)  |  

```


WEIXIN_GROUP_POLICY=allowlist  





# NOTE: this is a comma-separated list of group chat IDs, NOT member user IDs,  





# despite the variable name containing "USERS". Keep this in mind when configuring.  





WEIXIN_GROUP_ALLOWED_USERS=group_id_1,group_id_2  



```

The default group policy is `disabled` for Weixin (unlike WeCom where it defaults to `open`). This is intentional — personal WeChat accounts may be in many groups, and iLink bot identities typically can't receive ordinary WeChat group messages at all. The gateway logs a `WARNING` at startup if you set `WEIXIN_GROUP_POLICY` to anything other than `disabled`.
## Media Support[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#media-support "Direct link to Media Support")
### Inbound (receiving)[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#inbound-receiving "Direct link to Inbound \(receiving\)")
The adapter receives media attachments from users, downloads them from the WeChat CDN, decrypts them, and caches them locally for agent processing:  
| Type  | How it's handled  |  
| --- | --- |  
| **Images**  | Downloaded, AES-decrypted, and cached as JPEG.  |  
| **Video**  | Downloaded, AES-decrypted, and cached as MP4.  |  
| **Files**  | Downloaded, AES-decrypted, and cached. Original filename is preserved.  |  
| **Voice**  | If a text transcription is available, it's extracted as text. Otherwise the audio (SILK format) is downloaded and cached.  |  
**Quoted messages:** Media from quoted (replied-to) messages is also extracted, so the agent has context about what the user is replying to.
### AES-128-ECB Encrypted CDN[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#aes-128-ecb-encrypted-cdn "Direct link to AES-128-ECB Encrypted CDN")
WeChat media files are transferred through an encrypted CDN. The adapter handles this transparently:
  * **Inbound:** Encrypted media is downloaded from the CDN using `encrypted_query_param` URLs, then decrypted with AES-128-ECB using the per-file key provided in the message payload.
  * **Outbound:** Files are encrypted locally with a random AES-128-ECB key, uploaded to the CDN, and the encrypted reference is included in the outbound message.
  * The AES key is 16 bytes (128-bit). Keys may arrive as raw base64 or hex-encoded — the adapter handles both formats.
  * This requires the `cryptography` Python package.


No configuration is needed — encryption and decryption happen automatically.
### Outbound (sending)[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#outbound-sending "Direct link to Outbound \(sending\)")  
| Method  | What it sends  |  
| --- | --- |  
| `send`  | Text messages with Markdown formatting  |  
|  `send_image` / `send_image_file`  | Native image messages (via CDN upload)  |  
| `send_document`  | File attachments (via CDN upload)  |  
| `send_video`  | Video messages (via CDN upload)  |  
All outbound media goes through the encrypted CDN upload flow:
  1. Generate a random AES-128 key
  2. Encrypt the file with AES-128-ECB + PKCS#7 padding
  3. Request an upload URL from the iLink API (`getuploadurl`)
  4. Upload the ciphertext to the CDN
  5. Send the message with the encrypted media reference


## Context Token Persistence[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#context-token-persistence "Direct link to Context Token Persistence")
The iLink Bot API requires a `context_token` to be echoed back with each outbound message for a given peer. The adapter maintains a disk-backed context token store:
  * Tokens are saved per account+peer to `~/.hermes/weixin/accounts/<account_id>.context-tokens.json`
  * On startup, previously saved tokens are restored
  * Every inbound message updates the stored token for that sender
  * Outbound messages automatically include the latest context token


This ensures reply continuity even after gateway restarts.
## Markdown Formatting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#markdown-formatting "Direct link to Markdown Formatting")
WeChat clients connected through the iLink Bot API can render Markdown directly, so the adapter preserves Markdown instead of rewriting it:
  * **Headers** stay as Markdown headings (`#`, `##`, ...)
  * **Tables** stay as Markdown tables
  * **Code fences** stay as fenced code blocks
  * **Excessive blank lines** are collapsed to double newlines outside fenced code blocks


## Message Chunking[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#message-chunking "Direct link to Message Chunking")
Messages are delivered as a single chat message whenever they fit within the platform limit. Only oversized payloads are split for delivery:
  * Maximum message length: **4000 characters**
  * Messages under the limit stay intact even when they contain multiple paragraphs or line breaks
  * Oversized messages split at logical boundaries (paragraphs, blank lines, code fences)
  * Code fences are kept intact whenever possible (never split mid-block unless the fence itself exceeds the limit)
  * Oversized individual blocks fall back to the base adapter's truncation logic
  * A 0.3 s inter-chunk delay prevents WeChat rate-limit drops when multiple chunks are sent


## Typing Indicators[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#typing-indicators "Direct link to Typing Indicators")
The adapter shows typing status in the WeChat client:
  1. When a message arrives, the adapter fetches a `typing_ticket` via the `getconfig` API
  2. Typing tickets are cached for 10 minutes per user
  3. `send_typing` sends a typing-start signal; `stop_typing` sends a typing-stop signal
  4. The gateway automatically triggers typing indicators while the agent processes a message


## Long-Poll Connection[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#long-poll-connection "Direct link to Long-Poll Connection")
The adapter uses HTTP long-polling (not WebSocket) to receive messages:
### How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#how-it-works "Direct link to How It Works")
  1. **Connect:** Validates credentials and starts the poll loop
  2. **Poll:** Calls `getupdates` with a 35-second timeout; the server holds the request until messages arrive or the timeout expires
  3. **Dispatch:** Inbound messages are dispatched concurrently via `asyncio.create_task`
  4. **Sync buffer:** A persistent sync cursor (`get_updates_buf`) is saved to disk so the adapter resumes from the correct position after restarts


### Retry Behavior[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#retry-behavior "Direct link to Retry Behavior")
On API errors, the adapter uses a simple retry strategy:  
| Condition  | Behavior  |  
| --- | --- |  
| Transient error (1st–2nd)  | Retry after 2 seconds  |  
| Repeated errors (3+)  | Back off for 30 seconds, then reset counter  |  
| Session expired (`errcode=-14`)  | Pause for 10 minutes (re-login may be needed)  |  
| Timeout  | Immediately re-poll (normal long-poll behavior)  |  
### Deduplication[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#deduplication "Direct link to Deduplication")
Inbound messages are deduplicated using message IDs with a 5-minute window. This prevents double-processing during network hiccups or overlapping poll responses.
### Token Lock[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#token-lock "Direct link to Token Lock")
Only one Weixin gateway instance can use a given token at a time. The adapter acquires a scoped lock on startup and releases it on shutdown. If another gateway is already using the same token, startup fails with an informative error message.
## All Environment Variables[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#all-environment-variables "Direct link to All Environment Variables")  
| Variable  | Required  | Default  | Description  |  
| --- | --- | --- | --- |  
| `WEIXIN_ACCOUNT_ID`  | ✅  | —  | iLink Bot account ID (from QR login)  |  
| `WEIXIN_TOKEN`  | ✅  | —  | iLink Bot token (auto-saved from QR login)  |  
| `WEIXIN_BASE_URL`  | —  | `https://ilinkai.weixin.qq.com`  | iLink API base URL  |  
| `WEIXIN_CDN_BASE_URL`  | —  | `https://novac2c.cdn.weixin.qq.com/c2c`  | CDN base URL for media transfer  |  
| `WEIXIN_DM_POLICY`  | —  | `open`  | DM access policy: `open`, `allowlist`, `disabled`, `pairing`  |  
| `WEIXIN_GROUP_POLICY`  | —  | `disabled`  | Group access policy: `open`, `allowlist`, `disabled`  |  
| `WEIXIN_ALLOWED_USERS`  | —  | _(empty)_  | Comma-separated user IDs for DM allowlist  |  
| `WEIXIN_GROUP_ALLOWED_USERS`  | —  | _(empty)_  | Comma-separated **group chat IDs** (not member user IDs) for group allowlist. The variable name is legacy — it expects group IDs, not user IDs.  |  
| `WEIXIN_HOME_CHANNEL`  | —  | —  | Chat ID for cron/notification output  |  
| `WEIXIN_HOME_CHANNEL_NAME`  | —  | `Home`  | Display name for the home channel  |  
| `WEIXIN_ALLOW_ALL_USERS`  | —  | —  | Gateway-level flag to allow all users (used by setup wizard)  |  
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#troubleshooting "Direct link to Troubleshooting")  
| Problem  | Fix  |  
| --- | --- |  
| `Weixin startup failed: aiohttp and cryptography are required`  | Install both: `python -c "import pm; pm.sync_venv(['messaging'], explicit=True)"`  |  
| `Weixin startup failed: WEIXIN_TOKEN is required`  | Run `hermes gateway setup` to complete QR login, or set `WEIXIN_TOKEN` manually  |  
| `Weixin startup failed: WEIXIN_ACCOUNT_ID is required`  | Set `WEIXIN_ACCOUNT_ID` in your `.env` or run `hermes gateway setup`  |  
| `Another local Hermes gateway is already using this Weixin token`  | Stop the other gateway instance first — only one poller per token is allowed  |  
| Session expired (`errcode=-14`)  | Your login session has expired. Re-run `hermes gateway setup` to scan a new QR code  |  
| Proactive send (cron / notification) fails with `ret=-2 errmsg=prepare failed` or `unknown error`  | The peer's `context_token` went stale (no recent inbound message from them). The adapter treats this as a stale session — not a rate limit — and re-sends once without the token, so the message still arrives. If iLink still answers `prepare failed` (or there was no token to drop — a freshly paired bot), the send (text or media) fails with `iLink sendmessage session not ready … the user must send the bot a message first (or re-pair)`; the rate-limit cooldown never opens for it. Only other `-2` responses trigger the rate-limit backoff/cooldown, and that cooldown error carries the raw `ret`/`errcode`/`errmsg`  |  
| QR code expired during setup  | The QR auto-refreshes up to 3 times. If it keeps expiring, check your network connection  |  
| Bot doesn't respond to DMs  | Check `WEIXIN_DM_POLICY` — if set to `allowlist`, the sender must be in `WEIXIN_ALLOWED_USERS`  |  
| Bot ignores group messages  | Group policy defaults to `disabled`. Set `WEIXIN_GROUP_POLICY=open` or `allowlist` — but note that QR-login iLink bot identities (`...@im.bot`) typically cannot receive ordinary WeChat group messages at all. If the gateway logs show no raw inbound events for group messages, the limitation is on the iLink side, not in Hermes.  |  
| Media download/upload fails  | Ensure `cryptography` is installed. Check network access to `novac2c.cdn.weixin.qq.com`  |  
| `Blocked unsafe URL (SSRF protection)`  | The outbound media URL points to a private/internal address. Only public URLs are allowed  |  
| Voice messages show as text  | If WeChat provides a transcription, the adapter uses the text. This is expected behavior  |  
| Messages appear duplicated  | The adapter deduplicates by message ID. If you see duplicates, check if multiple gateway instances are running  |  
| `iLink POST ... HTTP 4xx/5xx`  | API error from the iLink service. Check your token validity and network connectivity  |  
| Terminal QR code doesn't render  | Reinstall with the messaging extra: `cd ~/.hermes/hermes-agent && python -c "import pm; pm.sync_venv(['messaging'], explicit=True)"`. Alternatively, open the URL printed above the QR  |  
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/weixin.md)
[Previous WeCom Callback (Self-Built App)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/wecom-callback)[Next QQ Bot](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/qqbot)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#prerequisites)
  * [Setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#setup)
    * [1. Run the Setup Wizard](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#1-run-the-setup-wizard)
    * [2. Configure Environment Variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#2-configure-environment-variables)
    * [3. Start the Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#3-start-the-gateway)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#features)
  * [Configuration Options](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#configuration-options)
  * [Access Policies](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#access-policies)
    * [DM Policy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#dm-policy)
    * [Group Policy](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#group-policy)
  * [Media Support](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#media-support)
    * [Inbound (receiving)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#inbound-receiving)
    * [AES-128-ECB Encrypted CDN](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#aes-128-ecb-encrypted-cdn)
    * [Outbound (sending)](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#outbound-sending)
  * [Context Token Persistence](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#context-token-persistence)
  * [Markdown Formatting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#markdown-formatting)
  * [Message Chunking](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#message-chunking)
  * [Typing Indicators](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#typing-indicators)
  * [Long-Poll Connection](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#long-poll-connection)
    * [How It Works](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#how-it-works)
    * [Retry Behavior](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#retry-behavior)
    * [Deduplication](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#deduplication)
    * [Token Lock](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#token-lock)
  * [All Environment Variables](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#all-environment-variables)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin#troubleshooting)


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
