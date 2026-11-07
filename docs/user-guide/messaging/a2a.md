---
title: "A2A (Agent-to-Agent)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a
scraped_at: 2026-11-07T17:19:55.776281+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/a2a)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Popular](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
    * [Microsoft 365](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
    * [Chinese platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
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
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Messaging Platforms
  * Other
  * A2A (Agent-to-Agent)


On this page
# A2A (Agent-to-Agent)
[A2A](https://a2a-protocol.org) is the open Agent2Agent protocol (v1.0, stewarded by the Linux Foundation) for communication between independent AI agents. The Hermes A2A plugin works in **both directions** : your agent can call other A2A agents as tools, and other agents can send tasks to your Hermes over HTTP.
It interoperates with any A2A-compliant peer — another Hermes, LangChain, CrewAI, Google ADK agents, or anything built on the official `a2a-sdk`.
## When to use A2A[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#when-to-use-a2a "Direct link to When to use A2A")
  * **Hermes ↔ Hermes across machines** — let your desktop agent hand tasks to a Hermes on a server, or vice versa, each with its own memory, tools, and credentials.
  * **Delegating to specialist agents** — a peer that advertises `web_search`/`research`/`coding` skills on its Agent Card can be discovered and called mid-conversation.
  * **Being a callable service** — expose your Hermes so other frameworks' agents can send it tasks.


When you want multiple agents on the **same machine** , prefer [delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) (in-process subagents) or the [kanban board](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban) (durable multi-profile work queue) — A2A is for crossing process/machine/framework boundaries.
## Enable[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#enable "Direct link to Enable")

```


hermes gateway setup      # pick A2A  



```

Or in `~/.hermes/config.yaml`:

```


gateway:  





  platforms:  





    a2a:  





      enabled: true  





      extra:  





        port: 9900  



```

The outbound client tools ship as the `a2a` toolset, **off by default** — enable it per platform:

```


hermes tools enable a2a --platform cli        # CLI/TUI sessions  





hermes tools enable a2a --platform telegram   # or any messaging platform  





hermes tools enable a2a --platform a2a        # let inbound A2A tasks call peers (agent chaining)  



```

The tools are available in every process type — CLI, TUI, gateway, and cron — without the inbound platform needing to be enabled.
## Outbound: calling other agents[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#outbound-calling-other-agents "Direct link to Outbound: calling other agents")
With the `a2a` toolset enabled, the agent gets:  
| Tool  | What it does  |  
| --- | --- |  
| `a2a_discover(url)`  | Fetch and summarize a peer's Agent Card  |  
| `a2a_call(agent, message, context_id?)`  | Send a task, get the reply; multi-turn via `context_id`  |  
| `a2a_list()`  | Configured peers, saved conversations, metrics  |  
| `a2a_history(context_id)`  | Recall a persisted A2A conversation  |  
| `a2a_orchestrate(capability, message, mode?)`  | Fan a task out to every peer advertising a capability (`all` / `first` / `best`)  |  
Configure known peers in `config.yaml`:

```


a2a_agents:  





  researcher:  





    url: "http://research-box.local:9900"  





    auth: { type: bearer, token: "..." }  





    timeout: 120  





    capabilities: [web_search, research]  



```

Then just ask: _"Ask the researcher agent to summarize today's arXiv postings."_ Direct URLs work too — `a2a_call` accepts any A2A endpoint.
## Inbound: being callable[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#inbound-being-callable "Direct link to Inbound: being callable")
With the platform enabled, Hermes serves:
  * **Agent Card** at `GET /.well-known/agent-card.json` (canonical v1.0 path; the legacy `agent.json` also answers) — advertises your agent's name, skills (derived from enabled toolsets), and auth requirements.
  * **JSON-RPC 2.0** at `POST /` — canonical v1.0 methods (`SendMessage`, `SendStreamingMessage`, `GetTask`, `ListTasks`, `CancelTask`, `SubscribeToTask`, push-notification config CRUD) plus the pre-1.0 path-style aliases (`message/send`, …).
  * **SSE streaming** for `SendStreamingMessage`, with spec-correct JSON-RPC-enveloped frames.
  * **Push notifications** (webhooks) for long-running tasks, HMAC-SHA256 signed.


Inbound tasks are injected into a **live gateway session** — the same agent, memory, and tools that serve your other channels — and the final reply is returned to the caller as the task result. Conversations are keyed by the A2A `contextId`, so a peer can hold a multi-turn exchange.
Interoperability is verified against the official Python `a2a-sdk` (card resolution, `SendMessage`, streaming).
## Forwarded profile sessions after the ownership cutover[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#forwarded-profile-sessions-after-the-ownership-cutover "Direct link to Forwarded profile sessions after the ownership cutover")
Forwarding to another local profile now submits to that profile's gateway owner; there is no fallback `hermes chat` process writing its session database. New forwarded conversations retain the exact agent, tenant, authenticated peer and context ID in their owner binding.
Historical forwarded sessions cannot be identified safely from their titles. The old adapter used `a2a-{agent}-{sanitized-context}` and omitted peer and tenant identity. Different contexts such as `ctx/exact` and `ctx-exact`, even from different peers, could already share one transcript. The conversation JSONL log also used a lossy filename and did not retain that complete identity. Peer names inside user-message text are not ownership metadata.
A matching historical title therefore returns `runtime_coordination_required` rather than attaching a peer to potentially unrelated history or silently starting a replacement. The historical session ID, title and messages remain untouched. Generic CLI resume does not bypass this refusal.
**Automatic migration of these historical forwarded sessions is not yet supported.** Recovery needs an explicit local-owner decision about the exact session-to-agent/tenant/peer/context binding, particularly for already mixed transcripts. It also needs an explicit launch-policy decision: historical rows can retain the model and some model parameters without the complete original cwd, system prompt or frozen tool/config policy. A title match or current profile configuration cannot recover information the old writer never stored. There is currently no supported migration command; do not retitle or edit database rows to bypass the ownership check.
## Security model[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#security-model "Direct link to Security model")
Secure by default; every widening step is explicit:
  * **No token ⇒ localhost only.** The server binds `127.0.0.1`. Remote exposure requires a bearer token **and** an explicit `A2A_HOST`. Without a token it also refuses browser-originated POSTs (an `Origin` header, a cross-site `Sec-Fetch-Site`, or a non-JSON `Content-Type`), so a web page open on the same machine cannot send it tasks. Local agents and SDKs that POST JSON are unaffected.
  * **Per-peer tokens** — `A2A_PEER_TOKENS="alice:tok1,bob:tok2"` gives each peer its own credential; the authenticated name drives rate limiting, trust, and audit.
  * **Prompt-injection filtering** — inbound text is filtered and framed as untrusted peer input. Remote peers cannot invoke operator slash commands.
  * **Outbound redaction** — credential-shaped strings (API keys, JWTs, tokens) are scrubbed from replies.
  * **Audit log** — every exchange appends to `~/.hermes/a2a_audit.jsonl`.
  * **Anti-loop** — per-context turn caps stop two agents ping-ponging forever.


## Configuration reference[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#configuration-reference "Direct link to Configuration reference")  
| Env var  | Default  | Meaning  |  
| --- | --- | --- |  
| `A2A_PEER_TOKENS`  | _(unset)_  | Per-peer credentials `name:token,…` (preferred)  |  
| `A2A_BEARER_TOKEN`  | _(unset)_  | Shared token; identity falls back to caller IP  |  
| `A2A_HOST`  | `127.0.0.1`  | Bind host — only widens when a token is set. IPv6 literals such as `::1` or `::` work too, bare or bracketed (`[::1]`)  |  
| `A2A_PORT`  | `9900`  | Inbound port  |  
| `A2A_AGENT_NAME`  | hostname-derived  | Name on the Agent Card  |  
| `A2A_PUBLIC_URL`  | _(unset)_  | Routable URL advertised on the card (reverse proxies / k8s)  |  
| `A2A_TRUSTED_PEERS`  | _(unset)_  | Allow-list of authenticated identities  |  
| `A2A_ALLOW_ALL_USERS`  | `false`  | Allow any authenticated peer (dev only)  |  
| `A2A_RATE_LIMIT`  | `60`  | Requests/minute per identity  |  
| `A2A_MAX_PINGPONG_TURNS`  | `5`  | Anti-loop turn cap per context (max 20)  |  
| `A2A_REPLY_TIMEOUT`  | `300`  | Seconds to wait for the agent's reply. The orphan-task sweep never fails a task before this window elapses (floor 300s), and never while a request is still waiting on it  |  
| `A2A_PUSH_SECRET`  | bearer token  | HMAC secret for push-notification signing  |  
| `A2A_ADVERTISED_TOOLSETS`  | all registered  | Restrict which skills appear on the Agent Card  |  
Behind a reverse proxy or Kubernetes Service, set `A2A_PUBLIC_URL` (or rely on `X-Forwarded-Host`/`X-Forwarded-Proto`) so the Agent Card advertises a URL peers can actually call back.
## Quick test[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#quick-test "Direct link to Quick test")

```


# From another machine / agent:  





curl http://your-host:9900/.well-known/agent-card.json  





  





curl -X POST http://your-host:9900/ \  





  -H 'Content-Type: application/json' \  





  -H 'Authorization: Bearer <token>' \  





  -d '{"jsonrpc":"2.0","id":1,"method":"SendMessage",  





       "params":{"message":{"messageId":"m1","role":"ROLE_USER",  





                 "parts":[{"text":"What tools do you have?"}]}}}'  



```

## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#troubleshooting "Direct link to Troubleshooting")
  * **Peers can't reach the card URL** — the card was advertising your bind address; set `A2A_PUBLIC_URL` to the externally routable URL.
  * **`401 Unauthorized`**— token mismatch; check`A2A_PEER_TOKENS` /`A2A_BEARER_TOKEN` on the server and the peer's `auth:` block.
  * **Server won't bind non-localhost** — by design: set a bearer token first, then `A2A_HOST=0.0.0.0`.
  * **`403`"Host must be a loopback name…" with no token** — without a token the server answers only requests addressed to a loopback name (`localhost`, `127.x.x.x`, `[::1]`) or the `A2A_PUBLIC_URL` host, so a web page on another hostname that resolves to your machine cannot read the card or the served-agent list. Call it by one of those names, set `A2A_PUBLIC_URL` to the name a local proxy forwards, or configure a token.
  * **`403`"Content-Type must be application/json" with no token** — the POST had a missing or non-JSON `Content-Type` (plain `curl -d` sends a form type); add `-H 'Content-Type: application/json'`.
  * **`403`"browser-originated" or "cross-site request refused" with no token** — the request carried an `Origin` header or a cross-site `Sec-Fetch-Site`, which only browsers send. Call it from a local script or SDK, or configure a token.
  * **Replies time out on long tasks** — raise `A2A_REPLY_TIMEOUT` (the orphan sweep follows it, so a late reply is stored, not discarded), or have the caller register a push-notification config and poll `GetTask`.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/a2a.md)
[Previous Yuanbao](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/yuanbao)[Next Home Assistant](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/homeassistant)
  * [When to use A2A](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#when-to-use-a2a)
  * [Enable](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#enable)
  * [Outbound: calling other agents](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#outbound-calling-other-agents)
  * [Inbound: being callable](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#inbound-being-callable)
  * [Forwarded profile sessions after the ownership cutover](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#forwarded-profile-sessions-after-the-ownership-cutover)
  * [Security model](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#security-model)
  * [Configuration reference](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#configuration-reference)
  * [Quick test](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#quick-test)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a#troubleshooting)


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
