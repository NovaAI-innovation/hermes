---
title: "Buzz Integration"
source: https://hermes-agent.nousresearch.com/docs/integrations/buzz
scraped_at: 2026-11-07T17:20:04.516331+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/integrations/buzz#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [English](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/integrations/buzz)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Features](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
    * [Overview](https://hermes-agent.nousresearch.com/docs/integrations/)
    * [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)
    * [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
    * [Buzz Integration](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
    * [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
    * [ACP Host Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
    * [Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
    * [Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)
    * [Credential Pools](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
  * [Reference](https://hermes-agent.nousresearch.com/docs/integrations/buzz)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Integrations
  * Buzz Integration


On this page
# Buzz Integration
[Buzz](https://github.com/block/buzz) is Block's open-source, self-hostable workspace where humans and AI agents share the same channels. It is built on Nostr: every message is a signed event on a relay you own, and every participant — human or agent — is a keypair.
Hermes integrates with Buzz three ways. Pick by where Hermes runs and what you want it to do:  
|   | ① Desktop runtime  | ② Relay bridge (ACP)  | ③ Native gateway platform  |  
| --- | --- | --- | --- |  
| **What it is**  | Buzz Desktop spawns Hermes locally as a managed harness  | Buzz's `buzz-acp` bridges a channel to `hermes acp` over stdio  | Hermes' gateway joins Buzz as a first-class messaging platform  |  
| **Hermes runs**  | On your desktop, launched by Buzz  | On a server, launched by `buzz-acp`  | In your own gateway, alongside Telegram/Discord/etc.  |  
| **Best for**  | Trying Hermes inside Buzz Desktop with zero config  | A hosted agent identity when Buzz owns the transport  | Full Hermes: memory, skills, approvals, cron, sessions  |  
| **Inbound**  | ACP stdio  | ACP stdio (via relay WebSocket)  | NIP-42-authenticated Nostr WebSocket (poll fallback)  |  
| **Setup**  | Automatic discovery  |  `buzz-acp` env vars  |  `hermes gateway setup` → Buzz  |  
## ① Buzz Desktop managed runtime[​](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-buzz-desktop-managed-runtime "Direct link to ① Buzz Desktop managed runtime")
Buzz Desktop ships Hermes as a preset runtime. With Hermes installed the normal way, open **Settings → Runtimes** and Hermes appears automatically — discovery resolves the `hermes-acp` launcher on your login-shell PATH, which the installer writes to `~/.local/bin` (and `hermes update` self-heals on older installs).
Full setup, troubleshooting, and the security posture (Buzz auto-approves tool permissions — keep agents owner-only): **[ACP Host Integration → Buzz Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp#buzz-desktop)**
## ② Relay bridge (buzz-acp + ACP)[​](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-relay-bridge-buzz-acp--acp "Direct link to ② Relay bridge \(buzz-acp + ACP\)")
For a hosted Hermes identity that joins Buzz _channels_ while Buzz's own harness owns the transport:

```


Buzz relay <-- WebSocket --> buzz-acp <-- ACP over stdio --> Hermes Agent  



```

The spawned Hermes uses the same config, credentials, memory, and skills as `hermes` on that host. Key minting, channel discovery, owner-only telemetry (`BUZZ_ACP_RELAY_OBSERVER`), and headless-permission guidance: **[ACP Host Integration → Buzz channels (relay bridge)](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp#buzz-channels-relay-bridge)**
## ③ Native gateway platform (recommended for full Hermes)[​](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-native-gateway-platform-recommended-for-full-hermes "Direct link to ③ Native gateway platform \(recommended for full Hermes\)")
The bundled `buzz` platform plugin makes Buzz a normal Hermes messaging platform — channels, DMs, mention gating, threaded replies, reactions, images, and cron delivery (`deliver=buzz`), with Hermes' own approvals, memory, and session management intact. Inbound arrives over a persistent NIP-42-authenticated Nostr WebSocket (dependency-free BIP-340 signing) with automatic fallback to CLI polling; outbound goes through the `buzz` CLI.

```


hermes gateway setup   # pick Buzz  



```

Full configuration reference (env vars, config.yaml, transport modes, access control): **[Messaging → Buzz](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/buzz)**
## Which one should I use?[​](https://hermes-agent.nousresearch.com/docs/integrations/buzz#which-one-should-i-use "Direct link to Which one should I use?")
  * **Just exploring, Buzz Desktop user** → ① works out of the box.
  * **Running a community relay and want an agent identity managed by Buzz** → ②.
  * **You already run Hermes as your agent and want Buzz as another channel** → ③. This is the deepest integration and the one that keeps every Hermes feature.


①/② and ③ use different identities and transports; run ③ with its own dedicated Nostr keypair. The adapter takes a scoped lock on the relay+pubkey pair, so two Hermes profiles cannot accidentally drive one Buzz identity.
## Credits[​](https://hermes-agent.nousresearch.com/docs/integrations/buzz#credits "Direct link to Credits")
The Buzz integration was built with the community: @SHL0MS (PATH launcher + Desktop security audit), @NYTEMODEONLY (relay-bridge docs), @rob-coco (platform adapter), @ScaleLeanChris (Nostr WebSocket transport + NIP-42/BIP-340 signing), and @jethac (multi-agent verification).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/integrations/buzz.md)
[Previous AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)[Next MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
  * [① Buzz Desktop managed runtime](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-buzz-desktop-managed-runtime)
  * [② Relay bridge (buzz-acp + ACP)](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-relay-bridge-buzz-acp--acp)
  * [③ Native gateway platform (recommended for full Hermes)](https://hermes-agent.nousresearch.com/docs/integrations/buzz#-native-gateway-platform-recommended-for-full-hermes)
  * [Which one should I use?](https://hermes-agent.nousresearch.com/docs/integrations/buzz#which-one-should-i-use)
  * [Credits](https://hermes-agent.nousresearch.com/docs/integrations/buzz#credits)


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
