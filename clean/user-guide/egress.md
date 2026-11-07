---
title: "Egress proxy"
source: "https://hermes-agent.nousresearch.com/docs/user-guide/egress"
scraped_at: "2026-11-07T17:19:22.956712+00:00"
doc_id: "user-guide/egress"
content_hash: "95fa8960551c4d28"
---

# Egress proxy
Optional outbound credential-injection firewall for remote terminal sandboxes. The sandbox only ever holds opaque proxy tokens; real API keys never leave the host.
  * [iron-proxy](/docs/user-guide/egress/iron-proxy) — single-binary TLS-intercepting proxy from [ironsh/iron-proxy](https://github.com/ironsh/iron-proxy), lazy-installed and managed by `hermes egress`.
