---
title: "Subscription Proxy"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy
scraped_at: 2026-11-07T17:19:38.847083+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/subscription-proxy)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
      * [Hermes Web Dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
      * [Extending the Dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/extending-the-dashboard)
      * [API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)
      * [Subscription Proxy](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Management
  * Subscription Proxy


On this page
# Subscription Proxy
The subscription proxy is a local HTTP server that lets external apps — OpenViking, Karakeep, Open WebUI, anything that speaks OpenAI-compatible chat completions — use your Hermes-managed provider subscription as their LLM endpoint. The proxy attaches the right credentials (refreshing them automatically) so the app never needs a static API key.
This is different from the [API server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server):  
|   | API server  | Subscription proxy  |  
| --- | --- | --- |  
| What it serves  | Your agent (full toolset, memory, skills)  | Raw model inference  |  
| Use case  | "Use Hermes as a chat backend"  | "Use my Portal sub from another app"  |  
| Auth  | Your `API_SERVER_KEY`  | Any bearer (proxy attaches the real one)  |  
| Tool calls  | Yes — the agent runs tools  | No — passthrough only  |  
Use the API server when you want the **agent** as a backend. Use the proxy when you just want **the model** through your subscription.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#quick-start "Direct link to Quick Start")
### 1. Log into your provider (one-time)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#1-log-into-your-provider-one-time "Direct link to 1. Log into your provider \(one-time\)")

```


hermes portal  



```

This opens your browser for the Nous Portal OAuth flow. Hermes stores the refresh token in `~/.hermes/auth.json` — the same place all Hermes provider logins live.
### 2. Start the proxy[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#2-start-the-proxy "Direct link to 2. Start the proxy")

```


hermes proxy start  



```


```


Starting Hermes proxy for Nous Portal  





  Listening on:  http://127.0.0.1:8645/v1  





  Forwarding to: (resolved per-request from your subscription)  





  Use any bearer token in the client — the proxy attaches your real credential.  



```

Leave this running in the foreground. Use `tmux`, `nohup`, or a systemd unit if you want it to survive logout.
### 3. Point your app at it[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#3-point-your-app-at-it "Direct link to 3. Point your app at it")
Any OpenAI-compatible app config takes the same triple:

```


Base URL:   http://127.0.0.1:8645/v1  





API key:    anything (e.g. "sk-unused")  





Model:      Hermes-4-70B    # or Hermes-4.3-36B, Hermes-4-405B  



```

The proxy ignores the `Authorization` header from your app and attaches your real Portal credential to the upstream request. Refreshes happen automatically when the bearer approaches expiry.
## Available providers[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#available-providers "Direct link to Available providers")

```


hermes proxy providers  



```

Currently shipped: `nous` (Nous Portal) and `xai` (xAI / Grok). More OAuth providers can be added by implementing the `UpstreamAdapter` interface in `hermes_cli/proxy/adapters/`.
## Check status[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#check-status "Direct link to Check status")

```


hermes proxy status  



```


```


Hermes proxy upstream adapters  





  





  [nous    ] Nous Portal — ready (bearer expires 2026-05-15T06:43:21Z)  



```

If you see `not logged in`, run `hermes portal`. If you see `credentials need attention`, your refresh token was revoked (rare — happens if you signed out from the Portal web UI) — just re-run `hermes portal`.
## Allowed paths[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#allowed-paths "Direct link to Allowed paths")
The proxy only forwards paths the upstream actually serves. For Nous Portal:  
| Path  | Purpose  |  
| --- | --- |  
| `/v1/chat/completions`  | Chat completions (streaming + non-streaming)  |  
| `/v1/completions`  | Legacy text completions  |  
| `/v1/embeddings`  | Embeddings  |  
| `/v1/models`  | Model list  |  
Other paths (`/v1/images/generations`, `/v1/audio/speech`, etc.) return 404 with a clear error pointing at the allowed paths. This keeps stray clients from leaking weird requests to the upstream.
## Configuring OpenViking to use Portal[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#configuring-openviking-to-use-portal "Direct link to Configuring OpenViking to use Portal")
[OpenViking](https://github.com/volcengine/OpenViking) is a context database that needs an LLM provider for its VLM (vision/language model used to extract memories) and embedding model. With the proxy, you can point its `vlm.api_base` at your local proxy:
Edit `~/.openviking/ov.conf`:

```


{  





  "vlm": {  





    "provider": "openai",  





    "model": "Hermes-4-70B",  





    "api_base": "http://127.0.0.1:8645/v1",  





    "api_key": "unused-proxy-attaches-real-creds"  





  }  





}  



```

Then start your proxy in a terminal alongside `openviking-server`:

```


# Terminal 1  





hermes proxy start  





  





# Terminal 2  





openviking-server  



```

OpenViking's VLM calls now flow through your Portal subscription. The embedding model side still needs its own provider — Portal does serve `/v1/embeddings` but the model selection depends on what your tier supports; check `portal.nousresearch.com/models`.
## Configuring Karakeep (or any bookmark/summarizer app)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#configuring-karakeep-or-any-bookmarksummarizer-app "Direct link to Configuring Karakeep \(or any bookmark/summarizer app\)")
[Karakeep](https://karakeep.app/) takes an OpenAI-compatible API for bookmark summarization. In its config:

```


# Karakeep .env  





OPENAI_API_BASE_URL=http://127.0.0.1:8645/v1  





OPENAI_API_KEY=any-non-empty-string  





INFERENCE_TEXT_MODEL=Hermes-4-70B  



```

Same pattern works for Open WebUI, LobeChat, NextChat, or any other OpenAI-compatible client.
## Exposing on LAN[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#exposing-on-lan "Direct link to Exposing on LAN")
By default the proxy binds `127.0.0.1` (localhost only). It refuses requests whose `Host` header is not its own address (`localhost`, `127.0.0.1`, `[::1]` or the bound IP) and any browser request from another site (an `Origin` other than its own, or a `Sec-Fetch-Site` of `cross-site`/`same-site`), so a web page open in your browser cannot use it. Clients such as SDKs and `curl` send neither header and are unaffected. To let other machines on your network use it:

```


hermes proxy start --host 0.0.0.0 --port 8645  



```

⚠ **Be aware:** anyone on your network can now use your Portal subscription. A wildcard bind skips the `Host` check (any name may reach it), so it refuses every request a web page makes (any `Origin`, or a `Sec-Fetch-Site` other than `none`): browsers cannot use a wildcard-bound proxy. The proxy has no auth of its own — it accepts any bearer. Use a firewall, VPN, or reverse proxy with proper auth if you expose this beyond your trusted network.
## Rate limits[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#rate-limits "Direct link to Rate limits")
Your Portal tier's RPM/TPM limits apply across the whole proxy. The proxy doesn't fan out or pool — it's a single bearer with your full subscription quota. Monitor usage at [portal.nousresearch.com](https://portal.nousresearch.com).
## Architecture[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#architecture "Direct link to Architecture")
The proxy is intentionally minimal. Per request:
  1. Receive `POST /v1/chat/completions` from your app
  2. Look up the adapter's current credential (refresh if expiring)
  3. Forward the request body verbatim, with `Authorization: Bearer <minted-key>`
  4. Stream the response back unchanged (SSE preserved)


No transformation. No logging of request bodies. No agent loop. The proxy is a credential-attaching pass-through.
## Future: more OAuth providers[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#future-more-oauth-providers "Direct link to Future: more OAuth providers")
The adapter system is pluggable. Adding a new provider (e.g. HuggingFace, Anthropic via OAuth) requires implementing `UpstreamAdapter` in `hermes_cli/proxy/adapters/<provider>.py` and registering it in `adapters/__init__.py`. Providers that aren't OpenAI-compatible at the protocol level (Anthropic Messages API, for example) would need a transformation layer, which is out of scope for the current shape.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/subscription-proxy.md)
[Previous API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)[Next Bundled Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#quick-start)
    * [1. Log into your provider (one-time)](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#1-log-into-your-provider-one-time)
    * [2. Start the proxy](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#2-start-the-proxy)
    * [3. Point your app at it](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#3-point-your-app-at-it)
  * [Available providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#available-providers)
  * [Check status](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#check-status)
  * [Allowed paths](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#allowed-paths)
  * [Configuring OpenViking to use Portal](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#configuring-openviking-to-use-portal)
  * [Configuring Karakeep (or any bookmark/summarizer app)](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#configuring-karakeep-or-any-bookmarksummarizer-app)
  * [Exposing on LAN](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#exposing-on-lan)
  * [Rate limits](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#rate-limits)
  * [Architecture](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#architecture)
  * [Future: more OAuth providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy#future-more-oauth-providers)


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
