---
title: "Browser CDP Supervisor"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor
scraped_at: 2026-11-07T17:20:20.154341+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/browser-supervisor)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
      * [Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
      * [Browser CDP Supervisor](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
      * [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
      * [Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals)
      * [Chronos Managed-Cron Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/chronos-managed-cron-contract)
      * [Egress proxy internals](https://hermes-agent.nousresearch.com/docs/developer-guide/egress-internals)
      * [Gateway Monitoring](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-monitoring)
      * [Relay ↔ Connector Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-connector-contract)
      * [Relay Shared Metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics)
      * [Streaming TTS Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
      * [Billing Lifecycle (TUI)](https://hermes-agent.nousresearch.com/docs/developer-guide/billing-lifecycle)
      * [Trajectory Format](https://hermes-agent.nousresearch.com/docs/developer-guide/trajectory-format)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Internals
  * Browser CDP Supervisor


On this page
# Browser CDP Supervisor
The CDP supervisor closes two long-standing gaps in Hermes' browser tooling:
  1. **Native JS dialogs** (`alert`/`confirm`/`prompt`/`beforeunload`) block the page's JS thread. Without supervision, the agent has no way to know a dialog is open — subsequent tool calls hang or throw opaque errors.
  2. **Cross-origin iframes (OOPIFs)** are invisible to top-level `Runtime.evaluate`. The agent can see iframe nodes in the DOM but can't click, type, or eval inside them without a CDP session attached to the child target.


The supervisor solves both by holding a persistent WebSocket to the backend's CDP endpoint per browser task, tracking pending dialogs and frame structure in its snapshot, and exposing a `browser_dialog` tool for explicit responses.
## Backend support[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#backend-support "Direct link to Backend support")  
| Backend  | Dialog detect  | Dialog respond  | Frame tree  | OOPIF `Runtime.evaluate` via `browser_cdp(frame_id=...)`  |  
| --- | --- | --- | --- | --- |  
| Local Chromium (launched by Hermes for `browser_exec`) / `/browser connect`  | ✓  | ✓ full workflow  | ✓  | ✓  |  
| Browserbase  | ✓ (via bridge)  | ✓ full workflow (via bridge)  | ✓  | ✓  |  
**Browserbase quirk.** Browserbase's CDP proxy uses Playwright internally and auto-dismisses native dialogs within ~10ms, so `Page.handleJavaScriptDialog` can't keep up. The supervisor injects a bridge script via `Page.addScriptToEvaluateOnNewDocument` that overrides `window.alert`/`confirm`/`prompt` with a synchronous XHR to a magic host (`hermes-dialog-bridge.invalid`). `Fetch.enable` intercepts those XHRs before they touch the network — the dialog becomes a `Fetch.requestPaused` event the supervisor captures, and `respond_to_dialog` fulfills via `Fetch.fulfillRequest` with a JSON body the injected script decodes.
From the page's perspective, `prompt()` still returns the agent-supplied string. From the agent's perspective, it's the same `browser_dialog(action=...)` API either way.
The Camofox catalog plugin (`hermes plugins install camofox`) drives a REST-only browser with no CDP surface, so the supervisor does not apply to it.
## Architecture[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#architecture "Direct link to Architecture")
### CDPSupervisor[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#cdpsupervisor "Direct link to CDPSupervisor")
One `asyncio.Task` running in a background daemon thread per Hermes `task_id`. Holds a persistent WebSocket to the backend's CDP endpoint. Maintains:
  * **Dialog queue** — `List[PendingDialog]` with `{id, type, message, default_prompt, session_id, opened_at}`
  * **Frame tree** — `Dict[frame_id, FrameInfo]` with parent relationships, URL, origin, whether cross-origin child session
  * **Session map** — `Dict[session_id, SessionInfo]` so interaction tools can route to the right attached session for OOPIF operations
  * **Recent console errors** — ring buffer of the last 50 for diagnostics


Subscribes on attach:
  * `Page.enable` — `javascriptDialogOpening`, `frameAttached`, `frameNavigated`, `frameDetached`
  * `Runtime.enable` — `executionContextCreated`, `consoleAPICalled`, `exceptionThrown`
  * `Target.setAutoAttach {autoAttach: true, flatten: true}` — surfaces child OOPIF targets; supervisor enables `Page`+`Runtime` on each


Thread-safe state access via a snapshot lock; tool handlers (sync) read the frozen snapshot without awaiting.
### Lifecycle[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#lifecycle "Direct link to Lifecycle")
  * **Start:** `SupervisorRegistry.get_or_start(task_id, cdp_url)` — called when `browser_exec` attaches to a session (local, cloud provider or CDP override) and on `/browser connect`. Idempotent.
  * **Stop:** session teardown or `/browser disconnect`. Cancels the asyncio task, closes the WebSocket, discards state.
  * **Dropped endpoint:** after a successful attach the supervisor reconnects with backoff (≤10 s) but gives up after `MAX_POST_ATTACH_RECONNECT_FAILURES` consecutive failures — one final warning, the thread exits and the registry entry is dropped. A dead local Chrome (its task finished) therefore never leaves a retrying thread behind; the next browser call starts a fresh supervisor.
  * **Rebind:** if the CDP URL changes (user reconnects to a new Chrome), the old supervisor is stopped and a fresh one started — state is never reused across endpoints.


### Dialog policy[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#dialog-policy "Direct link to Dialog policy")
Configurable via `config.yaml` under `browser.dialog_policy`:
  * **`must_respond`**(default) — capture, surface in`pending_dialogs` , wait for explicit `browser_dialog(action=...)` call. After a 300s safety timeout with no response, auto-dismiss and log. Prevents a buggy agent from stalling forever.
  * `auto_dismiss` — record and dismiss immediately; it shows up after the fact in `recent_dialogs`.
  * `auto_accept` — record and accept (useful for `beforeunload` where the workflow wants to navigate away cleanly).


Policy is per-task; no per-dialog overrides.
## Trusted plugin CDP access[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#trusted-plugin-cdp-access "Direct link to Trusted plugin CDP access")
In-process plugin code can send raw CDP commands over a task's supervisor connection through one public call, instead of writing the supervisor's private call table or socket:

```


from tools.browser_supervisor import SUPERVISOR_REGISTRY  





from tools.browser_supervisor_capture import CapturedCDPInvalid  





  





cdp = SUPERVISOR_REGISTRY.capture(task_id)  # raises CapturedCDPInvalid if no attached supervisor  





reply = cdp.call("Runtime.evaluate", {"expression": "document.title", "returnByValue": True},  





                 session_id=cdp.page_session_id, timeout=5)  





title = reply["result"]["result"]["value"]  



```

  * `SUPERVISOR_REGISTRY.capture(task_id, *, timeout=10.0) -> CapturedCDP` pins the supervisor's current WebSocket and the default page session attached on it. It never starts, reconnects or refocuses a supervisor.
  * `CapturedCDP.call(method, params=None, *, session_id=None, timeout=10.0, before_send=None) -> dict` returns the raw CDP reply (`{"id", "result"}`). `session_id=None` addresses the browser endpoint (`Target.*`); pass `page_session_id` or a session you attached yourself for page domains. A CDP error reply raises `RuntimeError`; no reply within a finite `timeout` raises `TimeoutError`. Finite timeouts fence queue admission with a monotonic deadline. `timeout=None` retains the reply until response or connection closure; acquisition owners can keep late attach IDs for cleanup beyond their own outer deadline. The call blocks its thread, so call it from a worker thread, never from the supervisor's own event loop.
  * `CapturedCDP.is_valid()` stays true until the supervisor reconnects, stops, or is replaced in the registry. After that every `call` raises `CapturedCDPInvalid`, including a call already in flight when the socket drops. A handle never follows the supervisor to a new connection: capture again and re-check whatever state you depend on.
  * `page_session_id` is the default page session at capture time. A later `focus_page` on the supervisor does not change it.
  * Sessions you attach (`Target.attachToTarget`) are yours to detach. A reply that arrives after `timeout` is dropped, so a timed-out attach can leave a session attached until the connection closes. Use `timeout=None` with a retained acquisition worker to own and detach late replies, rather than guessing a large timeout.
  * `before_send` is a trusted synchronous, nonblocking validator on the supervisor loop immediately before dispatch. Return `None`, or raise to refuse; do not call capture/CDP APIs from it. It does not revoke commands already dispatched.


This is a trusted, in-process seam. It grants nothing in-process Python could not already reach, and it enforces no origin, consent or target-ownership policy: a plugin that acts on pages must enforce its own. It is not exposed as a model tool and has no config switch.
## Agent surface[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#agent-surface "Direct link to Agent surface")
###  `browser_dialog` tool[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#browser_dialog-tool "Direct link to browser_dialog-tool")

```


browser_dialog(action, prompt_text=None, dialog_id=None)  



```

  * `action="accept"` / `"dismiss"` → responds to the specified or sole pending dialog (required)
  * `prompt_text=...` → text to supply to a `prompt()` dialog
  * `dialog_id=...` → disambiguate when multiple dialogs are queued (rare)


Tool is response-only. With a single pending dialog, `dialog_id` can be omitted.
### Supervisor snapshot[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#supervisor-snapshot "Direct link to Supervisor snapshot")
`CDPSupervisor.snapshot()` carries three fields while a supervisor is attached:

```


{  





  "pending_dialogs": [  





    {"id": "d-1", "type": "alert", "message": "Hello", "opened_at": 1650000000.0}  





  ],  





  "recent_dialogs": [  





    {"id": "d-1", "type": "alert", "message": "...", "opened_at": 1650000000.0,  





     "closed_at": 1650000000.1, "closed_by": "remote"}  





  ],  





  "frame_tree": {  





    "top": {"frame_id": "FRAME_A", "url": "https://example.com/", "origin": "https://example.com"},  





    "children": [  





      {"frame_id": "FRAME_B", "url": "about:srcdoc", "is_oopif": false},  





      {"frame_id": "FRAME_C", "url": "https://ads.example.net/", "is_oopif": true, "session_id": "SID_C"}  





    ],  





    "truncated": false  





  }  





}  



```

  * **`pending_dialogs`**— dialogs currently blocking the page's JS thread. The agent must call`browser_dialog(action=...)` to respond. Empty on Browserbase because their CDP proxy auto-dismisses within ~10ms.
  * **`recent_dialogs`**— ring buffer of up to 20 recently-closed dialogs with a`closed_by` tag: `"agent"` (we responded), `"auto_policy"` (local auto_dismiss/auto_accept), `"watchdog"` (must_respond timeout hit), or `"remote"` (browser/backend closed it on us, e.g. Browserbase). This is how agents on Browserbase still get visibility into what happened.
  * **`frame_tree`**— frame structure including cross-origin (OOPIF) children. Capped at 30 entries + OOPIF depth 2 to bound snapshot size on ad-heavy pages.`truncated: true` surfaces when limits were hit; agents needing the full tree can use `browser_cdp` with `Page.getFrameTree`.


### Availability gating[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#availability-gating "Direct link to Availability gating")
`browser_dialog` and `browser_cdp` gate on CDP reachability (the supervisor can only run when a CDP endpoint is reachable). Without one, the dialog tool is hidden — no schema bloat.
## Cross-origin iframe interaction[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#cross-origin-iframe-interaction "Direct link to Cross-origin iframe interaction")
`browser_cdp(frame_id=...)` routes CDP calls (notably `Runtime.evaluate`) through the supervisor's already-connected WebSocket using the OOPIF's child `sessionId`. Agents pick frame_ids out of the supervisor's `frame_tree.children[]` where `is_oopif=true` (or from `Page.getFrameTree` via `browser_cdp`) and pass them to `browser_cdp`. For same-origin iframes (no dedicated CDP session), the agent uses `contentWindow`/`contentDocument` from a top-level `Runtime.evaluate` instead — the supervisor surfaces an error pointing at that fallback when `frame_id` belongs to a non-OOPIF.
On Browserbase, this is the only reliable path for iframe interaction — stateless CDP connections (opened per `browser_cdp` call) hit signed-URL expiry, while the supervisor's long-lived connection keeps a valid session.
## File layout[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#file-layout "Direct link to File layout")
  * `tools/browser_supervisor.py` — `CDPSupervisor`, `SupervisorRegistry`, `PendingDialog`, `FrameInfo`
  * `tools/browser_supervisor_capture.py` — `CapturedCDP` / `CapturedCDPInvalid`, the trusted-plugin CDP seam behind `SUPERVISOR_REGISTRY.capture`
  * `tools/browser_dialog_tool.py` — `browser_dialog` tool handler
  * `tools/browser_session_cdp.py` — `ensure_cdp_supervisor` / `stop_cdp_supervisor`, `/browser connect` reattach, dialog-policy config
  * `tools/browser_session_lifecycle.py` — per-session teardown (supervisor stopped first)
  * `toolsets.py` — registers `browser_dialog` in `browser`, `hermes-acp`, `hermes-api-server`, and core toolsets (gated on CDP reachability)
  * `hermes_cli/config.py` — `browser.dialog_policy` and `browser.dialog_timeout_s` defaults


## Non-goals[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#non-goals "Direct link to Non-goals")
  * Streaming dialog/frame events live to the user (would require gateway hooks)
  * Persisting dialog history across sessions (in-memory only)
  * Per-iframe dialog policies (agent can express this via `dialog_id`)
  * Replacing `browser_cdp` — it stays as the escape hatch for the long tail (cookies, viewport, network throttling)


## Testing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#testing "Direct link to Testing")
Unit tests (`tests/tools/test_browser_supervisor.py`) use an asyncio mock CDP server that speaks enough of the protocol to exercise all state transitions: attach, enable, navigate, dialog fire, dialog dismiss, frame attach/detach, child target attach, session teardown. Real-backend E2E (Browserbase + local Chromium-family browser) is manual — exercise via `/browser connect` to a live Chromium-family browser and run the dialog/frame test cases described above.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/browser-supervisor.md)
[Previous Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)[Next ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
  * [Backend support](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#backend-support)
  * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#architecture)
    * [CDPSupervisor](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#cdpsupervisor)
    * [Lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#lifecycle)
    * [Dialog policy](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#dialog-policy)
  * [Trusted plugin CDP access](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#trusted-plugin-cdp-access)
  * [Agent surface](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#agent-surface)
    * [`browser_dialog` tool](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#browser_dialog-tool)
    * [Supervisor snapshot](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#supervisor-snapshot)
    * [Availability gating](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#availability-gating)
  * [Cross-origin iframe interaction](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#cross-origin-iframe-interaction)
  * [File layout](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#file-layout)
  * [Non-goals](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#non-goals)
  * [Testing](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor#testing)


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
