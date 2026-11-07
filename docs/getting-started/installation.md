---
title: "Installation"
source: https://hermes-agent.nousresearch.com/docs/getting-started/installation
scraped_at: 2026-11-07T17:19:22.934854+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/getting-started/installation#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [English](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/installation)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
    * [Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
    * [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
    * [Platform Support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
    * [Android / Termux](https://hermes-agent.nousresearch.com/docs/getting-started/termux)
    * [Nix & NixOS Setup](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)
    * [Updating & Uninstalling](https://hermes-agent.nousresearch.com/docs/getting-started/updating)
    * [Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)
    * [Official Domains & Phishing Safety](https://hermes-agent.nousresearch.com/docs/getting-started/official-domains)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Features](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * [Reference](https://hermes-agent.nousresearch.com/docs/getting-started/installation)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Getting Started
  * Installation


On this page
# Installation
Get Hermes Agent up and running in under two minutes!
For the full platform support matrix (which OSes, distribution methods, and platform-gated features are supported), see **[Platform Support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)**.
## Quick Install[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#quick-install "Direct link to Quick Install")
### Desktop packages on macOS or Windows[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#desktop-packages-on-macos-or-windows "Direct link to Desktop packages on macOS or Windows")
Download the package for your platform from the [Hermes website](https://hermes-agent.nousresearch.com/).
  * **Windows:** open the `.appinstaller` download with Windows App Installer. It installs the signed MSIX bundle and records its update source. Microsoft Store packages have separate Store ownership.
  * **macOS:** open the DMG, then copy `Hermes.app` to Applications. The ZIP artifact carries the signed app used by the automatic updater.


Bundled packages contain the agent, Python, supported dependencies, and prebuilt interfaces. First launch does not build that base runtime. Provider access and optional integrations can still require network access.
A `Hermes-Setup` bootstrap installer is different: it downloads a source installation and builds the desktop app. See [Hermes Desktop](https://hermes-agent.nousresearch.com/docs/user-guide/desktop).
There is no separate remote-only Desktop download. To use Desktop with a Hermes backend on another machine, install one of the packages above and connect it from **Settings → Gateways** ; see [Connecting to a remote backend](https://hermes-agent.nousresearch.com/docs/user-guide/desktop#connecting-to-a-remote-backend).
The macOS installer is **Apple Silicon only**. macOS on x86 (Intel) processors is [not a supported platform](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support#unsupported).
### Without Hermes Desktop:[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#without-hermes-desktop "Direct link to Without Hermes Desktop:")
For a command-line only install without Hermes Desktop, run:
#### Linux / macOS / WSL2[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#linux--macos--wsl2 "Direct link to Linux / macOS / WSL2")

```


curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash  



```

#### Windows (native)[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#windows-native "Direct link to Windows \(native\)")
Run in powershell:

```


iex (irm https://hermes-agent.nousresearch.com/install.ps1)   



```

If you want to install & run Hermes Desktop after a command-line only install, simply run

```


hermes desktop  



```

### Android / Termux[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#android--termux "Direct link to Android / Termux")
Use the [Termux APT package](https://hermes-agent.nousresearch.com/docs/getting-started/termux) on aarch64 Android devices. Configure its signed repository before running `pkg install hermes-agent`. The desktop/server scripts are not the Termux installation path.
### What the source installer does[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#what-the-source-installer-does "Direct link to What the source installer does")
The scripts clone the source, bootstrap uv, and delegate dependency preparation to PM. PM provides pinned Python, Node.js, npm, pnpm, ripgrep, and FFmpeg. The source installation selects the `all` Python extra, not every optional extra. PM also installs the browser and computer-use tools by default: a pinned Chromium (Chrome for Testing) that Hermes launches for local browsing, and `cua-driver` (the computer-use driver, on macOS, Windows and glibc Linux). If a download fails, the install still completes and prints the command to retry. The browser driver behind `browser_exec` (browser-harness, the engine of the Browser Use CLI) is a regular Python dependency, so every install, the Desktop app included, already has it. Where PM has no Chromium build (Android/Termux, musl Linux), Hermes uses a system `chromium` on `PATH` instead. Other optional tools use their feature-specific installation paths.
A new install lands on the latest stable release, the channel `hermes update` follows from then on (see [Updating](https://hermes-agent.nousresearch.com/docs/getting-started/updating)). To install the tip of `main` instead, pass `--channel main` on POSIX or `-Channel main` on Windows (or set `HERMES_INSTALL_CHANNEL=main` first, for the one-liners).
To leave the browser tools out, pass `--skip-browser` on POSIX or `-SkipBrowser` on Windows; for the computer-use driver, `--skip-computer-use` / `-SkipComputerUse`. Hermes remembers these choices: later installs and `hermes update` do not add them back. Run `hermes pm install chromium` or `hermes pm install cua-driver` to install them and undo the choice.
The scripts create a launcher and prepare the data directory. Interactive runs also invoke setup and gateway configuration. `--non-interactive` on POSIX, or `-NonInteractive` on Windows, skips stages that need input. The optional `--include-desktop` / `-IncludeDesktop` stage builds the desktop from source.
On a terminal the scripts show one status line per step and write the output of git, uv and the builds to `logs/install.log` under the Hermes data directory; a failed step prints its last lines and the log path. CI (`CI` or `GITHUB_ACTIONS` set), redirected output, `--verbose` / `-Verbose` or `HERMES_INSTALL_VERBOSE=1` stream everything instead.
#### Install layout[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#install-layout "Direct link to Install layout")  
| Method  | Code  | CLI entry point  | Default user data  |  
| --- | --- | --- | --- |  
| POSIX source script  | `~/.hermes/hermes-agent/`  |  `~/.local/bin/hermes` wrapper  | `~/.hermes/`  |  
| Windows source script  | `%LOCALAPPDATA%\hermes\hermes-agent\`  | `%LOCALAPPDATA%\hermes\bin\`  | `%LOCALAPPDATA%\hermes\`  |  
| Desktop bundle  | Inside the installed app package  | Packaged launchers; Windows execution aliases  | Platform default Hermes data directory  |  
| Docker  | `/opt/hermes/`  | Image entrypoint and `hermes` shim  | Mounted `/opt/data/`  |  
| Termux APT  | `$PREFIX/lib/hermes-agent/`  | Symlinks in `$PREFIX/bin/`  | `~/.hermes/`  |  
`HERMES_HOME` selects user data. The POSIX script's `--dir` selects its source checkout independently. Windows provides `-HermesHome` and `-InstallDir`. Running the POSIX script as root does not select an automatic FHS layout: it uses root's home unless you provide an explicit source path.
PM's tool store and per-install Python generations have separate lifetimes. See [Package management](https://hermes-agent.nousresearch.com/docs/reference/package-management) for their locations. Do not remove the data root to repair an application installation.
### After Installation[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#after-installation "Direct link to After Installation")
Reload your shell and start chatting:

```


source ~/.bashrc   # or: source ~/.zshrc  





hermes             # Start chatting!  



```

To reconfigure individual settings later, use the dedicated commands:

```


hermes model          # Choose your LLM provider and model  





hermes tools          # Configure which tools are enabled  





hermes gateway setup  # Set up messaging platforms  





hermes config set     # Set individual config values  





hermes config get     # Inspect individual config values  





hermes setup          # Or run the full setup wizard to configure everything at once  



```

One subscription covers 300+ models plus the [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway) (web search, image generation, TTS, cloud browser). Skip the per-tool key juggling:

```


hermes setup --portal  



```

That logs you in, sets Nous as your provider, and turns on the Tool Gateway in one command.
You don't need to rebuild your setup from scratch. Restore a full backup with `hermes import` (see [Exporting Hermes to another machine](https://hermes-agent.nousresearch.com/docs/reference/faq#exporting-hermes-to-another-machine)), or bring over a single agent with `hermes profile import` (see [Moving a single profile to another machine](https://hermes-agent.nousresearch.com/docs/reference/faq#moving-a-single-profile-to-another-machine)). Note that a profile export excludes credentials by design, so an export alone is not a full backup — [`hermes backup` vs `hermes profile export`](https://hermes-agent.nousresearch.com/docs/reference/faq#hermes-backup-vs-hermes-profile-export) explains which to use.
* * *
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#prerequisites "Direct link to Prerequisites")
For the POSIX source script, provide Git, curl, tar, and SHA-256 utilities. Windows can bootstrap its pinned Git for Windows archive when Git is absent. The script always downloads its verified uv pin; a uv already on your PATH is never used.
Current first-party installations run on **Python 3.14**. The broader `>=3.11,<3.15` range in `pyproject.toml` lets older Python installations run the updater before PM switches them to 3.14; it does not promise current runtime support on 3.11–3.13. PM selects the managed tool versions from `pm/lock.json`; it does not adopt arbitrary system Node versions as the installed runtime.
Source builds can require a native compiler and platform development libraries. Building Electron from source adds Node native-module requirements. These build prerequisites do not apply to installing a complete desktop package. Linux Chromium also requires system libraries supplied by the distribution.
On glibc Linux, the managed Node.js links `libatomic.so.1`, which minimal Debian, Ubuntu and RHEL-family images do not ship. When the library is missing, the installer and `hermes update` install the distro package (`libatomic1` on apt and zypper, `libatomic` on dnf/yum and apk, `gcc-libs` on pacman). They run the package manager directly as root, or as `sudo -n` otherwise. An interactive run asks for your sudo password once, before installing dependencies. `--non-interactive` runs never prompt. If the install cannot run, the error names the exact command for the package manager it found.
Nix is **no longer an explicitly supported install path** (best-effort only). If you already use Nix (on NixOS, macOS, or Linux), there's a dedicated setup path with a Nix flake, declarative NixOS module, and optional container mode. See the **[Nix& NixOS Setup](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup)** guide.
* * *
## Manual / Developer Installation[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#manual--developer-installation "Direct link to Manual / Developer Installation")
For a source checkout, start with the [PM developer workflow](https://hermes-agent.nousresearch.com/docs/reference/package-management#developer-workflow). It covers activation, daily commands, dependency refresh, and current bootstrap limits. [Development Setup](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing#development-setup) covers the separate test environment and checks.
* * *
## Non-Sudo / System Service User Installs[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#non-sudo--system-service-user-installs "Direct link to Non-Sudo / System Service User Installs")
Run the source installer as the intended service user. Its home, tool store, configuration, and launcher must belong to that user.
  1. As an administrator, install the source-build prerequisites and any Linux libraries Chromium needs (only if the service will browse locally).
  2. As the service user, run the regular installer:

```


curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash  



```

  3. Add the actual launcher directory to the service user's shell environment:

```


export PATH="$HOME/.local/bin:$PATH"  



```

  4. Run `hermes doctor` from that account. Use the installed wrapper, not a hardcoded `venv/bin/hermes` path.
  5. For a Linux user service that must survive logout, enable lingering as an administrator:

```


sudo loginctl enable-linger SERVICE_USER  



```



The current source installer does not run Playwright's `--with-deps` step. Apart from Node.js's `libatomic` (see Prerequisites), it does not install system packages. PM manages tool binaries; the administrator supplies system libraries. A service user without sudo gets the exact `libatomic` command to ask an administrator to run. See [Browser automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser) and [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/).
* * *
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#troubleshooting "Direct link to Troubleshooting")  
| Problem  | Solution  |  
| --- | --- |  
| `hermes: command not found`  | Reload your shell (`source ~/.bashrc`) or check PATH  |  
| `API key not set`  | Run `hermes model` to configure your provider, or `hermes config set OPENROUTER_API_KEY your_key`  |  
| Missing config after update  | Run `hermes config check` then `hermes config migrate`  |  
For more diagnostics, run `hermes doctor` — it will tell you exactly what's missing and how to fix it.
### Symlinked home directories and external storage[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#symlinked-home-directories-and-external-storage "Direct link to Symlinked home directories and external storage")
Hermes supports a symlinked `HERMES_HOME` and symlinked home subdirectories, including `hooks`, `skills`, `sessions`, and `logs`. During home initialization, existing directory links are preserved, and permissions on linked directories (and descendants such as `logs/curator`) are left to their owner.
If a link target is missing, inaccessible, or not a directory, initialization stops with a storage error naming the path and link target. Hermes does **not** replace the link or create its missing target: doing so could write data onto the local disk while an external or NAS volume is unmounted. Check the reported link, restore the mount or correct its target, and verify access permissions before retrying. For a deliberately new dotfiles target, create it yourself only after confirming the intended storage is available.
`hermes doctor` reports these failures as storage problems, not invalid YAML. Keep your existing `config.yaml`; running `hermes setup` is not the repair for an unavailable directory. This is a directory-availability check, not a mount monitor: an existing directory cannot establish that the intended volume is mounted.
## Install method auto-detection[​](https://hermes-agent.nousresearch.com/docs/getting-started/installation#install-method-auto-detection "Direct link to Install method auto-detection")
The update owner depends on the running installation, not only its data home. Source checkouts use the managed Git update path. Desktop bundles, Docker, Nix, and Termux packages retain their package owner's update mechanism. `hermes doctor` reports installation provenance. See [Updating & Uninstalling](https://hermes-agent.nousresearch.com/docs/getting-started/updating) before changing package-owned files.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/getting-started/installation.md)
[Previous Hermes Agent Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)[Next Platform Support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
  * [Quick Install](https://hermes-agent.nousresearch.com/docs/getting-started/installation#quick-install)
    * [Desktop packages on macOS or Windows](https://hermes-agent.nousresearch.com/docs/getting-started/installation#desktop-packages-on-macos-or-windows)
    * [Without Hermes Desktop:](https://hermes-agent.nousresearch.com/docs/getting-started/installation#without-hermes-desktop)
    * [Android / Termux](https://hermes-agent.nousresearch.com/docs/getting-started/installation#android--termux)
    * [What the source installer does](https://hermes-agent.nousresearch.com/docs/getting-started/installation#what-the-source-installer-does)
    * [After Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation#after-installation)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/getting-started/installation#prerequisites)
  * [Manual / Developer Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation#manual--developer-installation)
  * [Non-Sudo / System Service User Installs](https://hermes-agent.nousresearch.com/docs/getting-started/installation#non-sudo--system-service-user-installs)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/getting-started/installation#troubleshooting)
    * [Symlinked home directories and external storage](https://hermes-agent.nousresearch.com/docs/getting-started/installation#symlinked-home-directories-and-external-storage)
  * [Install method auto-detection](https://hermes-agent.nousresearch.com/docs/getting-started/installation#install-method-auto-detection)


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
