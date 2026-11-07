---
title: "Official Domains & Phishing Safety"
source: https://hermes-agent.nousresearch.com/docs/getting-started/official-domains
scraped_at: 2026-11-07T17:19:22.938856+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)
  * [English](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/official-domains)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
    * [Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
    * [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
    * [Platform Support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
    * [Android / Termux](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
    * [Nix & NixOS Setup](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)
    * [Updating & Uninstalling](https://hermes-agent.nousresearch.com/docs/getting-started/updating)
    * [Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)
    * [Official Domains & Phishing Safety](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Getting Started
  * Official Domains & Phishing Safety


On this page
# Official Domains & Phishing Safety
Hermes Agent's popularity has attracted impersonation campaigns: fake "Hermes" websites, GitHub accounts that mass-mention contributors with shortlinks, and cold emails offering "credits" on lookalike products. This page lists the official sources so you can check anything that claims to be Hermes Agent.
## Official sources[​](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#official-sources "Direct link to Official sources")
Nous Research operates `nousresearch.com` and its subdomains. The ones Hermes Agent uses:  
| Address  | What it is  |  
| --- | --- |  
| [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)  | Documentation, Desktop downloads, and the `install.sh` / `install.ps1` installers  |  
| `hermes-assets.nousresearch.com`  | Release artifacts: Desktop packages and updates, the Termux APT repository, installer mirrors  |  
| [portal.nousresearch.com](https://portal.nousresearch.com/)  | Nous Portal: account sign-in, subscriptions, billing  |  
| `inference-api.nousresearch.com`  | The Nous inference API Hermes calls when you use the Nous provider (no web page)  |  
| [nousresearch.com](https://nousresearch.com/)  | Nous Research website  |  
Outside `nousresearch.com`:
  * **GitHub:** the [NousResearch organization](https://github.com/NousResearch) and its [hermes-agent repository](https://github.com/NousResearch/hermes-agent) (source, releases, the Nix flake). Raw files from that repository are served from `raw.githubusercontent.com/NousResearch/hermes-agent/...`; that is the same repository, not a separate source. Any other account or repository is not ours.
  * **Docker Hub:** the [`nousresearch/hermes-agent`](https://hub.docker.com/r/nousresearch/hermes-agent) image, published by the repository's release workflow (see [Docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker)). Only the `nousresearch` namespace is official; images under other names or registries are not.
  * **X (Twitter):** [@NousResearch](https://x.com/NousResearch)
  * **Discord:** [discord.gg/NousResearch](https://discord.gg/NousResearch)


## Installing from an official source[​](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#installing-from-an-official-source "Direct link to Installing from an official source")
The script installers are served from `hermes-agent.nousresearch.com`:

```


# Linux / macOS / WSL2  





curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash  



```


```


# Windows (native)  





iex (irm https://hermes-agent.nousresearch.com/install.ps1)  



```

The other supported routes also stay on official sources: Desktop packages download from the [Hermes website](https://hermes-agent.nousresearch.com/), Termux uses the signed APT repository on `hermes-assets.nousresearch.com` (see the [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux), not the script above), Nix builds from the GitHub repository (see [Nix & NixOS](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)), and Docker pulls `nousresearch/hermes-agent` from Docker Hub. Some guides fetch `install.ps1` straight from the repository at `raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1`; it is the same script.
If an installer, download, image, or "portal" is hosted anywhere other than the sources listed on this page, treat it as untrusted.
## Not official[​](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#not-official "Direct link to Not official")
  * **Any domain that is not`nousresearch.com` or one of its subdomains** (apart from the accounts listed above), even when it contains "hermes" or "hermes-agent" (`.icu`, `.org`, `.ai` and other variants), copies the branding, or says it "points to official docs". Read the whole host name: `hermes-agent.nousresearch.com.example.net` is not a Nous Research subdomain.
  * **Cryptocurrency tokens.** There is **no Hermes Agent or Nous Research token**. Any account or site promoting one is a scam.
  * **GitHub accounts that mass-mention users** in discussions or issues with "community notice" posts and URL-shortener links (`goo.su`, `bit.ly`, etc.). Genuine project announcements never arrive as mass @-mentions with shortlinks.
  * **Unsolicited emails** offering credits, hosted "multiplayer Hermes" products, or partnership deals that name-drop the project to build trust.


## If you receive a suspicious message[​](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#if-you-receive-a-suspicious-message "Direct link to If you receive a suspicious message")
  1. **Don't click** shortened or off-domain links; don't enter credentials or connect wallets.
  2. **Report the account** to GitHub (`Report abuse` on the profile) or the relevant platform.
  3. **Check the host name** against the rule above: if it is not `nousresearch.com` or a subdomain of it, and not one of the accounts listed here, it isn't ours.
  4. Optionally flag it in the [Nous Research Discord](https://discord.gg/NousResearch) or an issue so others see it, but note that impersonation campaigns are external abuse: they're handled by platform reports, not code changes.


Hermes Agent is MIT-licensed and free to self-host. Nobody legitimate will ever ask you to pay for the open-source agent itself, claim "your account has credits waiting", or DM you an alternate download link.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/getting-started/official-domains.md)
[Previous Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)[Next CLI Interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Official sources](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#official-sources)
  * [Installing from an official source](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#installing-from-an-official-source)
  * [Not official](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#not-official)
  * [If you receive a suspicious message](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains#if-you-receive-a-suspicious-message)


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
