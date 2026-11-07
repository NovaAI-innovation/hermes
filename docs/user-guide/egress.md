---
title: "Egress proxy"
source: https://hermes-agent.nousresearch.com/docs/user-guide/egress
scraped_at: 2026-11-07T17:19:22.956712+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/egress#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/egress/)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/egress/)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
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
    * [Secrets](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
    * [Egress proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
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
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/egress)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/egress)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Using Hermes
  * Egress proxy
  * Egress proxy


# Egress proxy
Optional outbound credential-injection firewall for remote terminal sandboxes. The sandbox only ever holds opaque proxy tokens; real API keys never leave the host.
  * [iron-proxy](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy) — single-binary TLS-intercepting proxy from [ironsh/iron-proxy](https://github.com/ironsh/iron-proxy), lazy-installed and managed by `hermes egress`.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/egress/index.md)
[Previous 1Password](https://hermes-agent.nousresearch.com/docs/user-guide/secrets/onepassword)[Next Egress credential-injection proxy (iron-proxy)](https://hermes-agent.nousresearch.com/docs/user-guide/egress/iron-proxy)
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
