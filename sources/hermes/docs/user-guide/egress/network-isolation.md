---
title: "Network Egress Isolation (Docker)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation
scraped_at: 2026-11-07T17:19:22.958710+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/egress/network-isolation)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
    * [CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
    * [TUI](https://hermes-agent.nousresearch.com/docs/user-guide/tui)
    * [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop)
    * [Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode)
    * [Windows (Native)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)
    * [Windows (WSL2)](https://hermes-agent.nousresearch.com/docs/user-guide/windows-wsl-quickstart)
    * [Switching to a Source Install](https://hermes-agent.nousresearch.com/docs/user-guide/switching-to-source)
    * [Hermes Agent Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
    * [Which File Does What?](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what)
    * [Managed Scope](https://hermes-agent.nousresearch.com/docs/user-guide/managed-scope)
    * [Remote Config](https://hermes-agent.nousresearch.com/docs/user-guide/remote-config)
    * [Configuring Models](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)
    * [Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
    * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
      * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/)
      * [Egress credential-injection proxy (iron-proxy)](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy)
      * [Network Egress Isolation (Docker)](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
    * [Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
    * [Session Storage Recovery](https://hermes-agent.nousresearch.com/docs/user-guide/session-storage-recovery)
    * [Profiles: Running Multiple Agents](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
    * [Profile Distributions: Share a Whole Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)
    * [Running Many Gateways at Once](https://hermes-agent.nousresearch.com/docs/user-guide/multi-profile-gateways)
    * [Connecting Desktop to Many Hermes Instances](https://hermes-agent.nousresearch.com/docs/user-guide/multi-connection-desktop)
    * [Git Worktrees](https://hermes-agent.nousresearch.com/docs/user-guide/git-worktrees)
    * [Hermes Docker Setup](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
    * [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security)
    * [Checkpoints & Rollback](https://hermes-agent.nousresearch.com/docs/user-guide/checkpoints-and-rollback)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Using Hermes
  * Egress proxy
  * Network Egress Isolation (Docker)


On this page
# Network Egress Isolation for Docker Deployments
When running Hermes inside Docker, the default `network_mode: host` gives the agent process unrestricted outbound network access. This guide shows how to segment traffic so the agent core can only reach the services it needs, while blocking arbitrary outbound connections.
This is primarily a defense against prompt injection attacks that attempt to exfiltrate data via `curl`, `wget`, or raw HTTP from tool-generated shell commands.
## Threat Model[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#threat-model "Direct link to Threat Model")
The Hermes [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/main/SECURITY.md) §2 defines the trust model. The terminal backend is the primary execution boundary. However, when running with `network_mode: host`, any command the agent executes can reach any endpoint on the network, including external ones.
Network egress isolation adds a second layer: even if a malicious command executes inside the container, it cannot reach endpoints outside the explicitly allowlisted set.
## Architecture[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#architecture "Direct link to Architecture")

```


┌─────────────────────────────────────────────┐  





│  Docker Network: internal (no internet)     │  





│                                             │  





│   ┌──────────────┐   ┌──────────────────┐   │  





│   │ hermes-agent │   │ hermes-dashboard │   │  





│   └──────┬───────┘   └────────┬─────────┘   │  





│          │                    │              │  





│          ▼                    │              │  





│   ┌──────────────┐            │              │  





│   │ hermes-gtw   │◄───────────┘              │  





│   └──────┬───────┘                           │  





│          │                                   │  





└──────────┼───────────────────────────────────┘  





           │  





┌──────────┼───────────────────────────────────┐  





│  Docker Network: egress (internet-capable)   │  





│          │                                   │  





│          ▼                                   │  





│   ┌─────────────────┐                        │  





│   │ egress-proxy     │──► allowlisted hosts  │  





│   │ (squid / envoy)  │                       │  





│   └─────────────────┘                        │  





└──────────────────────────────────────────────┘  



```

Two Docker networks:
  * **`internal`**— no default route, no internet access. The agent, dashboard, and gateway run here.
  * **`egress`**— has internet access. Only services that need to reach external APIs are attached to this network.


The gateway service is dual-homed (attached to both networks) so it can receive inbound messages from Telegram/Slack/etc. and forward them to the agent on the internal network.
## Compose Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#compose-configuration "Direct link to Compose Configuration")
Override the default `docker-compose.yml` with a `docker-compose.override.yml`:

```


# docker-compose.override.yml  





# Network egress isolation for production deployments.  





#  





# Usage:  





#   HERMES_UID=$(id -u) HERMES_GID=$(id -g) docker compose up -d  





#  





# This overrides network_mode: host with isolated Docker networks.  





  





networks:  





  internal:  





    driver: bridge  





    internal: true          # no default route, no internet  





  egress:  





    driver: bridge  





  





services:  





  gateway:  





    network_mode: ""        # clear the host-mode default  





    networks:  





      - internal  





      - egress              # needs outbound for Telegram, LLM APIs  





    ports:  





      - "127.0.0.1:9119:9119"   # dashboard proxy, localhost only  





  





  dashboard:  





    network_mode: ""  





    networks:  





      - internal            # internal only, no egress needed  



```

### With an Egress Proxy (Recommended)[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#with-an-egress-proxy-recommended "Direct link to With an Egress Proxy \(Recommended\)")
For tighter control, route all outbound traffic through an HTTP proxy with an explicit allowlist:

```


# docker-compose.override.yml (with egress proxy)  





  





networks:  





  internal:  





    driver: bridge  





    internal: true  





  egress:  





    driver: bridge  





  





services:  





  gateway:  





    network_mode: ""  





    networks:  





      - internal  





      - egress  





    environment:  





      - HTTP_PROXY=http://egress-proxy:3128  





      - HTTPS_PROXY=http://egress-proxy:3128  





      - NO_PROXY=hermes,hermes-dashboard,localhost  





  





  dashboard:  





    network_mode: ""  





    networks:  





      - internal  





  





  egress-proxy:  





    image: ubuntu/squid:6.10-24.04_edge  





    networks:  





      - egress  





    volumes:  





      - ./config/squid-allowlist.conf:/etc/squid/conf.d/allowlist.conf:ro  





    restart: unless-stopped  



```

Example `config/squid-allowlist.conf`:

```


# Only allow HTTPS CONNECT to these hosts  





acl allowed_hosts dstdomain api.openai.com  





acl allowed_hosts dstdomain api.anthropic.com  





acl allowed_hosts dstdomain openrouter.ai  





acl allowed_hosts dstdomain generativelanguage.googleapis.com  





acl allowed_hosts dstdomain api.telegram.org  





acl allowed_hosts dstdomain api.github.com  





acl allowed_hosts dstdomain discord.com  





  





http_access allow CONNECT allowed_hosts  





http_access deny all  



```

Adjust the allowlist to match your LLM provider and messaging platform.
## Validating the Setup[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#validating-the-setup "Direct link to Validating the Setup")
After bringing up the stack, verify isolation:

```


# From the agent container: this should FAIL (no egress)  





docker compose exec gateway \  





  curl -sf --max-time 5 https://example.com && echo "FAIL: egress not blocked" || echo "OK: egress blocked"  





  





# From the agent container: this should SUCCEED (internal network)  





docker compose exec gateway \  





  curl -sf --max-time 5 http://hermes-dashboard:9119/health && echo "OK: internal reachable" || echo "FAIL"  





  





# If using egress proxy: this should SUCCEED (allowlisted)  





docker compose exec gateway \  





  curl -sf --max-time 5 --proxy http://egress-proxy:3128 https://api.openai.com/v1/models && echo "OK" || echo "FAIL"  



```

## Limitations[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#limitations "Direct link to Limitations")
  * **DNS resolution:** The `internal` network can still resolve external DNS names unless you also run a local DNS resolver that blocks external queries. For most threat models this is acceptable since DNS resolution alone does not exfiltrate meaningful data.
  * **Not a substitute for sandbox backends:** This guide isolates the agent _container's_ network. If you use the default local terminal backend, tool commands execute inside the same container. For stronger isolation, combine network segmentation with a sandboxed terminal backend (Docker, Modal, Daytona).
  * **Platform adapters need egress:** The gateway service needs outbound access to reach messaging platform APIs. If you add new platform adapters, add their API endpoints to the proxy allowlist.


## Related[​](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#related "Direct link to Related")
  * [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/main/SECURITY.md) — Hermes trust model and vulnerability reporting
  * [Docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker) — running Hermes in a container
  * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy) — credential-injection firewall for the sandbox
  * [docker-compose.yml](https://github.com/NousResearch/hermes-agent/blob/main/docker-compose.yml) — default compose configuration


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/egress/network-isolation.md)
[Previous Egress credential-injection proxy (iron-proxy)](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy)[Next Sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions)
  * [Threat Model](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#threat-model)
  * [Architecture](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#architecture)
  * [Compose Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#compose-configuration)
    * [With an Egress Proxy (Recommended)](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#with-an-egress-proxy-recommended)
  * [Validating the Setup](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#validating-the-setup)
  * [Limitations](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#limitations)
  * [Related](https://hermes-agent.nousresearch.com/docs/user-guide/egress/network-isolation#related)


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
