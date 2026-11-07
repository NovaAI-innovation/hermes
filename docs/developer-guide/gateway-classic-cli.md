---
title: "Classic gateway client"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli
scraped_at: 2026-11-07T17:20:20.170493+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/gateway-classic-cli)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
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
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Architecture
  * Classic gateway client


On this page
# Classic gateway client (initial migration)
Normal `hermes --cli`, `hermes chat`, `hermes chat -q '…' -Q`, and top-level `hermes -z '…'` use the gateway authority. Direct `cli.main` chat launches also hand off before constructing a local agent. Local bootstrap uses the canonical ensure lifecycle and a single-use private control ticket, not service installation. An explicit `HERMES_TUI_GATEWAY_URL` remains remote-only: failed connection or authentication never launches a local replacement.
The client prints the persisted `Session:` ID to stderr. Resume with `hermes --cli chat --resume ID`. Input is admitted with a fresh `input_id`; events and final replies come from the authority. `/quit`, `/exit`, `/detach`, EOF and closing the terminal detach only. `/stop` sends an execution-generation-fenced interrupt. Pending approvals display `/approve ID once|deny|…`; clarification uses `/answer ID TEXT`. The client uses the displayed prompt ID and its captured generation, not a locally reconstructed waiter. `/discard ID` acknowledges an admission lost across an owner restart (`prompt.resolve_unknown`). `/branch [title]`, `/model <model> [--provider name]` and `/compress [here [N] | <focus>] [--preview]` are revision-fenced `session.mutate` operations (`hermes_cli/gateway_mutations.py`); `/yolo [on|off]` toggles this session's approval bypass on the owner (`config.set` key `yolo`). `/title [name]` (`session.mutate rename`), `/undo [N]` and `/retry` (`session.mutate rewind`; `/undo` puts the removed message back in the composer), `/new [title]` / `/reset` (`session.create` with this session's frozen launch request), `/usage` (the owner's report plus the last committed turn) and `/tools` (launch toolsets) run in the view (`hermes_cli/gateway_chat_commands.py`). Every other command goes to the owner as `slash.exec`: the reviewed reads run there and the rest print `/x is not available on the shared gateway yet` with a link to the [command parity table](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-command-parity), which lists what every local client does with every command.
One-shot stdout ends with the final reply. Without `-Q`, a resumed session first prints its stored history (`user:` / `assistant:` lines), and the reply is followed by the `Resume this session with:` block (see Launch options); `-Q` prints the reply alone. Exit status is 0 for a completed admission, 1 for failed execution/connection, 2 for unsupported frontend options, 3 for a pending control that requires interactive reattachment or a turn lost in a gateway crash (clear it with `hermes sessions discard <id> --yes`), and 130 for a keyboard detach. A pending control does not imply cancellation. `-z` no longer implicitly bypasses approval policy.
## Launch options[​](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli#launch-options "Direct link to Launch options")
The gateway advertises its accepted creation parameters through `runtime.describe` (`session_create.parameters`, from `gateway.session_policy.CREATE_FIELDS`). The client sends a creation option only when it is advertised; a requested option an older gateway does not advertise is refused (`Gateway does not support creation options: …`). Caller cwd is sent when advertised; an old gateway lacking cwd support prints a warning that it uses its configured execution directory, while explicit `--in` rejects. A resume may repeat the exact creation flags the session was frozen with (scripts re-run one command line); any flag that would change the frozen route rejects.
**Accepted and frozen into the session at creation** (`_POLICY` in `hermes_cli/gateway_chat.py`): `--model`, `--provider`, `--base-url`, `--api-key` (memory-only, never persisted), `--reasoning`, `--toolsets`, `--max-turns`, `--skills` (rendered once into the frozen prompt), `--checkpoints`, `--yolo`, `--accept-hooks` (also `HERMES_ACCEPT_HOOKS=1`), `--pass-session-id`, `--ignore-rules`, `--ignore-user-config` and `--safe-mode` (both need an explicit `--model`; safe mode runs the turn in an isolated worker that never reads the profile). Also accepted: `--source <label>`, `--resume <id-or-title>`, `-c <title>`, `-c <title> --create-if-missing`, `--in <dir>`, `--query-file`, `--format stream-json`, `-z ... --usage-file`, bare `-c` (this terminal's breadcrumb session, else the most recent CLI session), `--resume latest` (most recent CLI session, this workspace first; both resolved by the owner, `session.resume latest='cli'`) and `--list-tools` / `--list-toolsets` (print the catalog and exit; no session). `chat -q` without `-Q` ends with main's `Resume this session with: hermes --resume <id>` block.
**Refused with exit 2** (`_UNSUPPORTED` plus the selection checks in `validate_options`); the error names where each capability lives now:  
| Option  | Why  | Use instead  |  
| --- | --- | --- |  
|  `-w` / `--worktree`  | Worktree creation is a launcher-side step the authority does not expose  | `hermes --tui -w`  |  
| `--image`  | No client-side attachment staging on this path  | attach in `hermes --tui` or Desktop  |  
| `--run-budget`  | No per-launch run budget in the creation contract  |  `agent.run_budget_seconds` in config.yaml  |  
|  `-v` / `--verbose`  | Display-only; the client has no verbose renderer  |  `hermes logs --follow` (the refusal also names `hermes chat --tui -v`, whose canonical Ink path does not yet carry the flag)  |  
| `--no-restore-cwd`  | The gateway keeps the session's frozen cwd  | `--in <dir>`  |  
|  `--create-if-missing` without `-c <name>`  | Nothing to create by name  | `-c <name> --create-if-missing`  |  
`--compact` is not a `hermes chat` option (argparse rejects it); a direct `cli.main` hand-off refuses it and names `display.compact`.
## Current parity limits — not full classic CLI parity[​](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli#current-parity-limits--not-full-classic-cli-parity "Direct link to Current parity limits — not full classic CLI parity")
Full legacy presentation, slash registry parity, interactive history editing, auto-reconnect, lost-ACK durable client journals, remote login bootstrap, cold-owner resume and native Windows/macOS QA remain outstanding. The client preserves an explicit remote URL's existing authentication mechanism; it does not acquire or mint remote credentials.
`tests/hermes_cli/test_gateway_chat_native.py` exercises native tmux/PTY classic fresh input, detach, persisted-ID resume and one-shot through the ordinary daemon with a loopback model, isolated HOME/HERMES_HOME and caller cwd. Constructor instrumentation records no client AIAgent, SessionDB or GatewayRunner. The test also denies an invalid approval choice, then reconnects and consents before a real terminal effect on an owned fixture. Stale-control/active-Stop native coverage and native clarify interaction remain separate acceptance work.
For two-checkout compatibility testing, load the narrowly scoped pytest option plugin and specify the disposable gateway peer's checkout (the normal runner's hermetic environment deliberately removes arbitrary environment overrides):

```


scripts/run_tests.sh -j 1 --file-retries 0 tests/hermes_cli/test_gateway_chat_native.py \  





  -p tests.hermes_cli.gateway_client_options --client-test-runtime-root=/path/to/runtime-checkout  



```

The receipt explicitly reports `caller_cwd_effect_verified`. On a cwd-capable runtime the native client submits model/toolsets/cwd and the real terminal writes its actual execution directory into an owned temporary receipt. On an older runtime, explicit `--in` must reject without that effect. Do not count the latter as cwd parity. Both client and daemon use isolated test homes; this option does not install a service or alter the selected checkout.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/gateway-classic-cli.md)
[Previous Gateway local sessions](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-local-sessions)[Next Gateway command parity](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-command-parity)
  * [Launch options](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli#launch-options)
  * [Current parity limits — not full classic CLI parity](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-classic-cli#current-parity-limits--not-full-classic-cli-parity)


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
