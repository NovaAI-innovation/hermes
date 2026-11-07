---
title: "macOS bundle updates"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates
scraped_at: 2026-11-07T17:20:29.110203+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/macos-bundle-updates)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/source-update-completion)
      * [Source update completion ownership](https://hermes-agent.nousresearch.com/docs/developer-guide/source-update-completion)
      * [Shared bundle builds](https://hermes-agent.nousresearch.com/docs/developer-guide/shared-bundle-builds)
      * [Stable release admission and promotion](https://hermes-agent.nousresearch.com/docs/developer-guide/stable-releases)
      * [macOS bundle updates](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates)
      * [PM audit remediation status](https://hermes-agent.nousresearch.com/docs/developer-guide/pm-audit-status)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Packaging & Releases
  * macOS bundle updates


On this page
# macOS bundle updates
Tagged macOS bundles use `electron-updater`. The bundled and Light stamps name that owner. Stable and canary are separate application identities; each updates within its baked channel. Development and bootstrap installs keep checkout updates.
One-off builds carry `source: commit-build` and have no updater. Their package identity includes the short commit SHA, so different commit builds can coexist. Checks and apply requests explain that the developer must provide a new build. This applies to the desktop and its bundled CLI, not to an unrelated remote backend the desktop connects to.
## Feed contract[​](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#feed-contract "Direct link to Feed contract")
Channel registration lives in R2 at `releases/channels/NAME.json`, not in a checked-in channel map. Channel bundles resolve that record and its digest-bound build manifest before selecting an immutable native feed. The admitted request keeps the application identity stable across builds and records the source commit separately from the increasing native package version.
Existing tagged clients retain their native feed URLs. The generic `apps/desktop/update-feed.cjs` adapter computes these legacy paths; it does not register channels. The builder writes the legacy URL into `app-update.yml`; `updates.desktop_feed_base_url` can supply an explicit bucket-base URL.
  * Stable: `releases/darwin/stable/stable-mac.yml`
  * Canary: `releases/darwin/canary/canary-mac.yml`
  * Light: the same paths with `light/` between `darwin/` and the channel.
  * Artifacts: `releases/tag/TAG/FILENAME`, shared by download links and feeds.
  * Channel-build artifacts and native metadata: `releases/channel-builds/BUILD_ID/`.


Retirement is a different operation from a native update: the old channel points to a qualified official destination, not to a differently named package in its own native feed. The explicit migration action must preserve user state and verify destination readiness before removing the preview application. Keeping the qualified receiver manifest immutable lets an offline preview migrate after the destination channel has advanced; the destination subsequently owns updates.
The current workflow builds the bundled variant on ARM64 runners only; there is no Intel (x64) leg. Light has separate client/feed routing but no release matrix leg in this change.
`python -m scripts.releases.r2 finalize` requires exactly one metadata file, named `arm64-CHANNEL-mac.yml`. It rejects wrong versions, variants, architectures, hashes and inconsistent legacy path fields. Each referenced ZIP/DMG is streamed back and checked against its SHA-512 and size. Publication checks the live version, conditionally replaces its ETag, and reads back the resulting feed. Same-tag macOS artifacts cannot be overwritten with different bytes. Mutable feeds use `Cache-Control: no-store`. Canary retention protects the artifacts and blockmaps referenced by live feeds. An unreadable feed prevents pruning.
## Client lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#client-lifecycle "Direct link to Client lifecycle")
Checks never download automatically. Apply rechecks the release, downloads it, and waits for Squirrel.Mac to accept the signed app. Only then does Hermes stop its app-owned backends and request installation/relaunch. Unrelated quits do not trigger installation. Downloads and native-verification failures leave backends running. Concurrent checks cannot replace an apply operation's target. The existing checkout updater never mutates the sealed app bundle.
## Release environment[​](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#release-environment "Direct link to Release environment")
The existing `release-signing` environment supplies:
  * `CSC_LINK` and `CSC_KEY_PASSWORD`: Developer ID Application signing identity.
  * `APPLE_API_KEY_P8`, `APPLE_API_KEY_ID`, `APPLE_API_ISSUER`: notarization.
  * `CLOUDFLARE_R2_ACCOUNT_ID`, `CLOUDFLARE_R2_ACCESS_KEY_ID`, `CLOUDFLARE_R2_SECRET_ACCESS_KEY`: bucket access secrets.
  * `CLOUDFLARE_R2_BUCKET`, `CLOUDFLARE_R2_PUBLIC_URL`: repository/environment vars.


Publishing requires the Apple credentials. The existing after-sign hook owns notarization, so electron-builder's second notarization path is disabled. The publish gate verifies the signature, stapled ticket and Gatekeeper assessment. The Darwin publish job waits for the arm64 build and its smoke, and serializes channel writes.
## Verification limits[​](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#verification-limits "Direct link to Verification limits")
Helper tests exercise the strategy, native-event ordering, feed validation, conditional publication, and retention. They are not proof of a signed install or actual app replacement.
Native macOS packaged-update drivers are part of the existing [install/update family](https://github.com/NousResearch/hermes-agent/blob/main/tests/install/BUNDLED_UPDATES.md). The stable gate requires signed-package transitions on both architectures. Each acceptance claim needs a successful native run for the exact old/new package pair. Workflow definitions and historical helper results do not establish acceptance of the current head. See [PM audit status](https://hermes-agent.nousresearch.com/docs/developer-guide/pm-audit-status) for scoped receipts.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/macos-bundle-updates.md)
[Previous Stable release admission and promotion](https://hermes-agent.nousresearch.com/docs/developer-guide/stable-releases)[Next PM audit remediation status](https://hermes-agent.nousresearch.com/docs/developer-guide/pm-audit-status)
  * [Feed contract](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#feed-contract)
  * [Client lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#client-lifecycle)
  * [Release environment](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#release-environment)
  * [Verification limits](https://hermes-agent.nousresearch.com/docs/developer-guide/macos-bundle-updates#verification-limits)


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
