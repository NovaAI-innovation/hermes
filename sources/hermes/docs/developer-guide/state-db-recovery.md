---
title: "State DB Recovery"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery
scraped_at: 2026-11-07T17:20:37.793340+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/state-db-recovery)


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
      * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
      * [Codebase Ownership Map](https://hermes-agent.nousresearch.com/docs/developer-guide/codebase-ownership)
      * [Agent Loop Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
      * [Prompt Assembly](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)
      * [Context Compression and Caching](https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching)
      * [Micro-compaction](https://hermes-agent.nousresearch.com/docs/developer-guide/micro-compaction)
      * [Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals)
      * [Gateway Session Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-session-lifecycle)
      * [Gateway local sessions](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-local-sessions)
      * [Classic gateway client](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
      * [Gateway command parity](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-command-parity)
      * [Multiplexing Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/multiplexing-gateway)
      * [Completion backlogs](https://hermes-agent.nousresearch.com/docs/developer-guide/completion-backlog-delivery)
      * [Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)
      * [State DB Recovery](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery)
      * [Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
      * [Config Backend Seam](https://hermes-agent.nousresearch.com/docs/developer-guide/config-backend)
      * [Programmatic Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/source-update-completion)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Architecture
  * State DB Recovery


On this page
# State database and FTS recovery
For the user-facing walkthrough (what to stop, what the files beside `state.db` are, why maintenance commands refuse while a writer is live) see [Session storage recovery](https://hermes-agent.nousresearch.com/docs/user-guide/session-storage-recovery).
`state.db` stores two different data classes:
  * `sessions` and `messages` are the canonical transcript.
  * `messages_fts*` tables and their sync triggers are derived search indexes.


The derived indexes may be detached temporarily. They must not turn a live message write or search into an unbounded full-transcript rebuild.
## Live behavior when FTS is corrupt[​](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#live-behavior-when-fts-is-corrupt "Direct link to Live behavior when FTS is corrupt")
If an FTS write or search reports the corruption error class, `SessionDB`:
  1. records the durable `fts_stale` marker;
  2. removes the FTS sync triggers in the same transaction;
  3. retries canonical writes without the derived-index sinks; and
  4. serves searches from canonical rows through the `LIKE` fallback.


The failing live operation never runs `FTS5('rebuild')`. Existing recovery ownership remains unchanged: a later `SessionDB` open may rebuild under the cross-process admission lock and foreign-holder guard. If that guarded rebuild cannot run, FTS remains detached, canonical writes stay available, and `hermes doctor` reports the explicit repair command.
## Live behavior when the file itself is corrupt[​](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#live-behavior-when-the-file-itself-is-corrupt "Direct link to Live behavior when the file itself is corrupt")
If a live write reports bare `SQLITE_CORRUPT` / `SQLITE_NOTADB` (`database disk image is malformed`, `file is not a database`) with no FTS provenance, the damage is in a canonical B-tree, the schema, or the freelist. `SessionDB` then quarantines that handle (`StateDbCorruptError`):
  1. the failing write propagates the typed error and nothing is retried;
  2. later writes on the handle fail immediately without touching the file;
  3. the handle never reopens its connection after `close()`; and
  4. `close()` skips its explicit WAL checkpoint.


Stopping the writes is the protection. In the field, a handle that kept writing for ~50 minutes after the first structural error checkpointed 15 pages under the wrong page numbers on shutdown (page 1 received a `messages_fts_trigram_data` leaf) and turned a damaged-but-readable file into one that no longer opened at all. Skipping the explicit checkpoint is the second line of defence; on Python 3.12+ the quarantine also disables SQLite's own last-connection checkpoint (`SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE`), so the `-wal` sidecar survives `close()` for forensics. On Python 3.11 that switch is unavailable and SQLite may still checkpoint once on close, so copy `state.db`, `state.db-wal` and `state.db-shm` together before restarting anything.
The gateway and the agent flush path treat the quarantine like a replaced file: pending transcripts go to `sessions/<id>.jsonl` and the gateway `pending_messages/` spool instead of the retry queue, and the FTS one-shot rebuild never runs on the damaged file. The quarantine is per process — the shared handle stays poisoned for every holder until the process restarts on a repaired or restored file. Do not run `hermes doctor --fix` while the gateway is still up. Next steps:

```


hermes gateway stop  





HERMES_HOME="$HOME/.hermes" hermes sessions recover --source "$HOME/.hermes/state.db" --inspect-only  





# if recoverable:  





HERMES_HOME="$HOME/.hermes" hermes sessions recover --source "$HOME/.hermes/state.db" --output "$HOME/recovered-state.db"  



```

or restore the newest snapshot from `state-snapshots/`.
## Explicit repair[​](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#explicit-repair "Direct link to Explicit repair")
Stop every process that can open the profile database before repairing it. Keep them stopped for the complete repair and verification window.

```


hermes gateway stop  





HERMES_HOME="$HOME/.hermes" hermes sessions repair --check-only  





HERMES_HOME="$HOME/.hermes" hermes sessions repair  



```

`sessions repair` creates a SQLite backup by default and performs structural work through the repository's guarded snapshot-and-promotion path. Do not copy `state.db`, `state.db-wal`, and `state.db-shm` independently with `cp`; those files are one live SQLite image.
After repair, verify the health probe, stale marker, trigger set, and canonical row counts before restarting the gateway:

```


HERMES_HOME="$HOME/.hermes" hermes sessions repair --check-only  





sqlite3 "$HOME/.hermes/state.db" \  





  "SELECT key, value FROM state_meta WHERE key = 'fts_stale';"  





sqlite3 "$HOME/.hermes/state.db" \  





  "SELECT type, name FROM sqlite_master WHERE name IN  





   ('messages_fts_insert','messages_fts_update','messages_fts_delete')  





   ORDER BY name;"  





sqlite3 "$HOME/.hermes/state.db" \  





  "SELECT 'sessions', COUNT(*) FROM sessions  





   UNION ALL SELECT 'messages', COUNT(*) FROM messages;"  



```

The marker query should return no row, the expected FTS triggers should be present, and canonical row counts must not decrease. If repair fails, preserve both the live database and the reported backup; never delete canonical rows to make a derived-index error disappear.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/state-db-recovery.md)
[Previous Session Storage](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)[Next Provider Runtime Resolution](https://hermes-agent.nousresearch.com/docs/developer-guide/provider-runtime)
  * [Live behavior when FTS is corrupt](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#live-behavior-when-fts-is-corrupt)
  * [Live behavior when the file itself is corrupt](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#live-behavior-when-the-file-itself-is-corrupt)
  * [Explicit repair](https://hermes-agent.nousresearch.com/docs/developer-guide/state-db-recovery#explicit-repair)


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
