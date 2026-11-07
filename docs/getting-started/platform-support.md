---
title: "Platform Support"
source: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
scraped_at: 2026-11-07T17:19:22.939856+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [English](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/platform-support)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
    * [Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
    * [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
    * [Platform Support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
    * [Android / Termux](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
    * [Nix & NixOS Setup](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)
    * [Updating & Uninstalling](https://hermes-agent.nousresearch.com/docs/getting-started/updating)
    * [Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)
    * [Official Domains & Phishing Safety](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Features](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Reference](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Getting Started
  * Platform Support


On this page
# Platform Support
Hermes Agent maintains support for many platforms and distribution methods, but we can't support every possible install method.
* * *
## Tier 1[​](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#tier-1 "Direct link to Tier 1")
We strive to never break installations and updates for these. Issues & regressions in Tier 1 are our first priority and take precedence over other platforms.  
| OS / Architecture  | Installation methods  | Notes  |  
| --- | --- | --- |  
|  **macOS** (Apple Silicon)  |  [Hermes Desktop](https://hermes-agent.nousresearch.com/), [`install.sh`](https://hermes-agent.nousresearch.com/docs/getting-started/installation)  |   |  
|  [**Windows 10 / 11**](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native) (x86_64, aarch64)  |  [`install.ps1`](https://hermes-agent.nousresearch.com/docs/getting-started/installation), [MSIX desktop](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)  | The MSIX package requires Windows 11 22H2 or later. Optional dependencies have [architecture limits](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native).  |  
|  **Linux /[WSL2](https://hermes-agent.nousresearch.com/docs/user-guide/windows-wsl-quickstart)** (x86_64, aarch64)  | [`install.sh`](https://hermes-agent.nousresearch.com/docs/getting-started/installation)  | We test on the latest Ubuntu and WSL2. If your distro has glibc, systemd, and follows the Filesystem Hierarchy Standard, it's likely to work pretty well.  |  
|  [**Docker Container**](https://hermes-agent.nousresearch.com/docs/user-guide/docker) (x86_64, aarch64)  | [`docker pull`](https://hermes-agent.nousresearch.com/docs/user-guide/docker)  | Docker installs do not support `hermes update`. Updating is done by running a new image.  |  
* * *
## Tier 2[​](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#tier-2 "Direct link to Tier 2")
These platforms are maintained in-tree only as a best effort. Releases may break them, and we can't promise we'll fix them promptly when they break.
PRs will be accepted to fix issues with them, but they will take precedence below fixing issues with Tier 1 platforms.  
| OS / Architecture  | Installation methods  | Notes  |  
| --- | --- | --- |  
|  **Nix** (macOS, Linux, NixOS)  | [Nix flake and modules](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)  | Nix owns runtime installation and updates.  |  
|  **Android /[Termux](https://hermes-agent.nousresearch.com/docs/getting-started/termux)** (aarch64)  |  [Signed APT repository](https://hermes-agent.nousresearch.com/docs/getting-started/termux), then `pkg install hermes-agent`  | Prerelease package with Python, Node, and TUI. Not built by default: only releases cut with `--with termux` (and `windows` and `macos-arm64`) update the APT channel. Run the gateway in a Termux session; Android can terminate background processes.  |  
### Build targets and support priority[​](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#build-targets-and-support-priority "Direct link to Build targets and support priority")
Releases build the macOS desktop bundle for Apple Silicon (`arm64`) only; no release or CI workflow builds or tests an Intel macOS (`x64`) bundle. The macOS update feed is arm64-only, so Intel Macs installed from an older desktop bundle get no update. The Termux APT package is **not built by default** : a release includes it only when it is cut with `release.py release --with termux`. A release without Termux leaves the Termux APT channel on its previous release. The `Hermes-Setup.dmg` bootstrap installer is built for Apple Silicon only, so on an Intel Mac it reports "not supported on this Mac". Intel Macs can install the [CLI](https://hermes-agent.nousresearch.com/docs/getting-started/installation#linux--macos--wsl2) and run `hermes desktop`. Linux desktop packaging is disabled in the release workflow, although local AppImage builds and native Linux PM bundle checks exist.
## Unsupported[​](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#unsupported "Direct link to Unsupported")
These platforms and distribution methods are **not** supported. We suggest that you migrate to a supported distribution method or platform. They may be broken right now, they may break more in the future. PRs to fix them will _not_ be accepted, and any code that keeps compatibility with them may be removed at any point.
  * Android / Termux on non-aarch64 devices (aarch64 is [supported](https://hermes-agent.nousresearch.com/docs/getting-started/termux) via our APT package)
  * installs via the AUR (we might upstream patches if it helps out <3)
  * 32-bit x86 macOS, and Intel x86_64 macOS desktop bundles (none are built).
  * installs via `pypi` (e.g. `uv tool install hermes-agent`, `pip install hermes-agent`, etc.)
  * installs via `brew` (`brew install hermes-agent`)


If you are using an unsupported distribution method, please read the [the installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation) to learn how to switch to a supported one.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/getting-started/platform-support.md)
[Previous Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)[Next Android / Termux](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
  * [Tier 1](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#tier-1)
  * [Tier 2](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#tier-2)
    * [Build targets and support priority](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#build-targets-and-support-priority)
  * [Unsupported](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#unsupported)


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
