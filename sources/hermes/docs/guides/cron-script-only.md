---
title: "Script-Only Cron Jobs (No LLM)"
source: https://hermes-agent.nousresearch.com/docs/guides/cron-script-only
scraped_at: 2026-11-07T17:20:11.912110+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/cron-script-only)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
    * [Run Nemotron 3 Ultra free in Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
    * [Run Hermes Agent with Nous Portal](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
    * [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)
    * [Running Hermes on a Personal or Work Machine](https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine)
    * [Run Local LLMs on Mac](https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac)
    * [Tutorial: Daily Briefing Bot](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
    * [Tutorial: Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)
    * [Using Hermes as a Python Library](https://hermes-agent.nousresearch.com/docs/guides/python-library)
    * [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
    * [Manage Hermes Cloud with MCP](https://hermes-agent.nousresearch.com/docs/guides/manage-hermes-cloud-with-mcp)
    * [Use SOUL.md with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes)
    * [Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)
    * [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)
    * [Script-Only Cron Jobs (No LLM)](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
    * [Automation Blueprints](https://hermes-agent.nousresearch.com/docs/guides/automation-blueprints)
    * [Cron Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/cron-troubleshooting)
    * [Troubleshooting: "My Agent Feels Dumber"](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)
    * [Working with Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
    * [Delegation & Parallel Work](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns)
    * [Give Your Agent Its Own Email Address](https://hermes-agent.nousresearch.com/docs/guides/agent-email-address)
    * [Tutorial: GitHub PR Review Agent](https://hermes-agent.nousresearch.com/docs/guides/github-pr-review-agent)
    * [GitHub PR Reviews via Webhook](https://hermes-agent.nousresearch.com/docs/guides/webhook-github-pr-review)
    * [Migrate from OpenClaw](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)
    * [AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
    * [Google Vertex AI](https://hermes-agent.nousresearch.com/docs/guides/google-vertex)
    * [Microsoft Foundry](https://hermes-agent.nousresearch.com/docs/guides/azure-foundry)
    * [xAI Grok OAuth (SuperGrok / X Premium+)](https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth)
    * [OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)
    * [Register a Microsoft Graph Application](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
    * [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Script-Only Cron Jobs (No LLM)


On this page
# Script-Only Cron Jobs
Sometimes you already know exactly what message you want to send. You don't need an agent to reason about it — you just need a script to run on a timer, and its output (if any) to land in Telegram / Discord / Slack / Signal.
Hermes calls this **no-agent mode**. It's the cron system minus the LLM.

```


   ┌──────────────────┐          ┌──────────────────┐  





   │ scheduler tick   │  every   │ run script       │  





   │ (every N minutes)│ ──────▶ │ (bash or python) │  





   └──────────────────┘          └──────────────────┘  





                                          │  





                                          │ stdout  





                                          ▼  





                                 ┌──────────────────┐  





                                 │ delivery router  │  





                                 │ (telegram/disc…) │  





                                 └──────────────────┘  



```

  * **No LLM call.** Zero tokens, zero agent loop, zero model spend.
  * **Script is the job.** The script decides whether to alert. Emit output → message gets sent. Emit nothing → silent tick.
  * **Bash or Python.** `.sh` / `.bash` files run under `bash` from `PATH` when available, otherwise `/bin/bash`; any other extension runs under the current Python interpreter. A Python script can also pin a **user-managed venv** via `--interpreter` (see [Using your own Python environment](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#using-your-own-python-environment)). Paths must resolve inside `~/.hermes/scripts/` (relative, absolute, or `~` forms are OK if they stay in that directory). Cron scripts do **not** inherit provider credentials from the Hermes process environment.
  * **Same scheduler.** Lives in `cronjob` alongside LLM jobs — pausing, resuming, listing, logs, and delivery targeting all work the same way.


## When to Use It[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#when-to-use-it "Direct link to When to Use It")
Use no-agent mode for:
  * **Memory / disk / GPU watchdogs.** Run every 5 minutes, alert only when a threshold is breached.
  * **CI hooks.** Deploy finished → post the commit SHA. Build failed → send the last 100 lines of the log.
  * **Periodic metrics.** "Daily Stripe revenue at 9am" as a simple API call + pretty-print.
  * **External event pollers.** Check an API, alert on state change.
  * **Heartbeats.** Ping a dashboard every N minutes to prove the host is alive.


Use a normal (LLM-driven) cron job when you need the agent to **decide** what to say — summarize a long document, pick interesting items from a feed, draft a human-friendly message. The no-agent path is for cases where the script's stdout already IS the message.
## Create One from Chat[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#create-one-from-chat "Direct link to Create One from Chat")
The real win of no-agent mode is that the agent itself can set up the watchdog for you — no editor, no shell, no remembering CLI flags. You describe what you want, Hermes writes the script, schedules it, and tells you when it'll fire.
### Example transcript[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#example-transcript "Direct link to Example transcript")
> **You:** ping me on telegram if RAM is over 85% every 5 minutes
> **Hermes:** _(writes`~/.hermes/scripts/memory-watchdog.sh` , then calls `cronjob(...)` with `no_agent=true`)_
> Set up. Runs every 5 min, alerts Telegram only when RAM is over 85%. Script: `memory-watchdog.sh`. Job ID: `abc123`.
Under the hood, the agent makes two tool calls:

```


# 1. Write the check script  





write_file(  





    path="~/.hermes/scripts/memory-watchdog.sh",  





    content='''#!/usr/bin/env bash  





ram_pct=$(free | awk '/^Mem:/ {printf "%d", $3 * 100 / $2}')  





if [ "$ram_pct" -ge 85 ]; then  





  echo "RAM ${ram_pct}% on $(hostname)"  





fi  





# Empty stdout = silent tick; no message sent.  





''',  





)  





  





# 2. Schedule it — no_agent=True skips the LLM on every tick  





cronjob(  





    action="create",  





    schedule="every 5m",  





    script="memory-watchdog.sh",  





    no_agent=True,  





    deliver="telegram",  





    name="memory-watchdog",  





)  



```

From that point on every tick is free: the scheduler runs the script, pipes its stdout to Telegram if non-empty, and never touches a model.
### What the agent decides for you[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#what-the-agent-decides-for-you "Direct link to What the agent decides for you")
When you phrase a request like "alert me when X" or "every N minutes check Y and tell me if Z", Hermes' `cronjob_manage` tool description tells it to reach for `no_agent=True` whenever the message content is fully determined by the script. It falls back to the normal LLM-driven path when the request needs reasoning (_"summarize the new issues"_ , _"pick the most interesting headlines"_ , _"draft a friendly reminder"_).
You don't have to specify `--no-agent` yourself. Just describe the behavior.
### Managing watchdogs from chat[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#managing-watchdogs-from-chat "Direct link to Managing watchdogs from chat")
The agent can pause, resume, edit, and remove jobs the same way it creates them:
> **You:** stop the memory watchdog for tonight
> **Hermes:** _(calls`cronjob(action='pause', job_id='abc123')`)_
> Paused. Resume with "turn it back on" or via `hermes cron resume abc123`.
> **You:** change it to every 15 minutes
> **Hermes:** _(calls`cronjob(action='update', job_id='abc123', schedule='every 15m')`)_
The full lifecycle (create / list / update / pause / resume / run-now / remove) is available to the agent without you learning any CLI commands.
## Create One from the CLI[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#create-one-from-the-cli "Direct link to Create One from the CLI")
Prefer the shell? The CLI path gives you the same result with three commands:

```


# 1. Write your script  





cat > ~/.hermes/scripts/memory-watchdog.sh <<'EOF'  





#!/usr/bin/env bash  





# Alert when RAM usage is over 85%. Silent otherwise.  





RAM_PCT=$(free | awk '/^Mem:/ {printf "%d", $3 * 100 / $2}')  





if [ "$RAM_PCT" -ge 85 ]; then  





  echo "⚠ RAM ${RAM_PCT}% on $(hostname)"  





fi  





# Empty stdout = silent run; no message sent.  





EOF  





chmod +x ~/.hermes/scripts/memory-watchdog.sh  





  





# 2. Schedule it  





hermes cron create "every 5m" \  





  --no-agent \  





  --script memory-watchdog.sh \  





  --deliver telegram \  





  --name "memory-watchdog"  





  





# 3. Verify  





hermes cron list  





hermes cron run <job_id>    # fire it once to test  



```

That's the whole thing. No prompt, no skill, no model.
## How Script Output Maps to Delivery[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#how-script-output-maps-to-delivery "Direct link to How Script Output Maps to Delivery")  
| Script behavior  | Result  |  
| --- | --- |  
| Exit 0, non-empty stdout  | stdout is delivered verbatim  |  
| Exit 0, empty stdout  | Silent tick — no delivery  |  
| Exit 0, stdout contains `{"wakeAgent": false}` on the last line  | Silent tick (shared gate with LLM jobs)  |  
| Non-zero exit code  | Error alert is delivered (so a broken watchdog doesn't fail silently)  |  
| Script timeout  | Error alert is delivered  |  
The "silent when empty" behavior is the key to the classic watchdog pattern: the script is free to run every minute, but the channel only sees a message when something actually needs attention.
## Script Rules[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#script-rules "Direct link to Script Rules")
Scripts must resolve inside `~/.hermes/scripts/`. This is enforced at run time — relative names, absolute paths, and `~`-prefixed paths are accepted when the resolved target stays in that directory; path traversal and symlink escapes are rejected. The same directory is shared with the pre-check script gate used by LLM jobs.
Interpreter choice is by file extension:  
| Extension  | Interpreter  |  
| --- | --- |  
|  `.sh`, `.bash`  |  `bash` from `PATH` (fallback `/bin/bash`)  |  
| anything else  |  `sys.executable` (current Python), or a [configured interpreter](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#using-your-own-python-environment)  |  
We intentionally do NOT honour `#!/...` shebangs — keeping the interpreter set explicit and small reduces the surface the scheduler trusts.
### Using your own Python environment[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#using-your-own-python-environment "Direct link to Using your own Python environment")
By default a Python cron script runs under Hermes' own Python environment, which only carries Hermes' own dependencies — so a script that imports `openpyxl`, a database driver, or any other package you installed would fail with `ModuleNotFoundError`.
You can point the job at a **user-managed venv** instead with `--interpreter`:

```


# 1. Create a venv you own — it survives Hermes reinstalls/rebuilds.  





uv venv ~/venvs/hermes-reporting --python 3.11  





uv pip install --python ~/venvs/hermes-reporting/bin/python openpyxl  





  





# 2. Schedule the job with that interpreter.  





hermes cron create "0 8 * * *" \  





  --no-agent \  





  --script daily-report.py \  





  --interpreter ~/venvs/hermes-reporting/bin/python \  





  --deliver telegram  



```

Like `--model`, this is a user-owned setting: set it with `hermes cron create/edit`; the agent's `cronjob` tool can't.
Rules:
  * The venv is **user-managed**. Hermes does not create, freeze, restore, or install packages into it — it just invokes the path you give.
  * The path must be **absolute or`~` -prefixed** (e.g. `~/venvs/reporting/bin/python3`). Bare names like `python3` are rejected, because they are not stable across `PATH` changes.
  * It must be a **Python executable** (`python`, `python3`, `python3.12`, …), including a symlink's target — `/bin/bash` or other interpreters are refused.
  * Applies **only to Python scripts**. `.sh` / `.bash` always run under bash regardless.
  * The job-level setting applies to both `script` and `monitor_script` when they are Python files.
  * It is validated **at run time** , not at creation — a cron job is long-lived, and the venv may be rebuilt or moved between when you create the job and when it fires. A missing or non-executable interpreter produces a clear script failure that is delivered like any other error.
  * To clear it later: `hermes cron edit <job_id> --interpreter ""`.


## Schedule Syntax[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#schedule-syntax "Direct link to Schedule Syntax")
Same as all other cron jobs:

```


hermes cron create "every 5m"        # interval  





hermes cron create "every 2h"  





hermes cron create "0 9 * * *"       # standard cron: 9am daily  





hermes cron create "30m"             # one-shot: run once in 30 minutes  



```

See the [cron feature reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) for the full syntax.
## Delivery Targets[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#delivery-targets "Direct link to Delivery Targets")
`--deliver` accepts everything the gateway knows about. Some common shapes:

```


--deliver telegram                       # platform home channel  





--deliver telegram:-1001234567890        # specific chat  





--deliver telegram:-1001234567890:17585  # specific Telegram forum topic  





--deliver discord:#ops  





--deliver slack:#engineering  





--deliver signal:+15551234567  





--deliver local                          # just save to ~/.hermes/cron/output/  



```

No running gateway is required at script-run time for bot-token platforms (Telegram, Discord, Slack, Signal, SMS, WhatsApp) — the tool calls each platform's REST endpoint directly using the credentials already in `~/.hermes/.env` / `~/.hermes/config.yaml`.
## Editing and Lifecycle[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#editing-and-lifecycle "Direct link to Editing and Lifecycle")

```


hermes cron list                                    # see all jobs  





hermes cron pause <job_id>                          # stop firing, keep definition  





hermes cron resume <job_id>  





hermes cron edit <job_id> --schedule "every 10m"    # adjust cadence  





hermes cron edit <job_id> --agent                   # flip to LLM mode  





hermes cron edit <job_id> --no-agent --script …     # flip back  





hermes cron remove <job_id>                         # delete it  



```

Everything that works on LLM jobs (pause, resume, manual trigger, delivery target changes) works on no-agent jobs too.
## Worked Example: Disk Space Alert[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#worked-example-disk-space-alert "Direct link to Worked Example: Disk Space Alert")

```


cat > ~/.hermes/scripts/disk-alert.sh <<'EOF'  





#!/usr/bin/env bash  





# Alert when / or /home is over 90% full.  





THRESHOLD=90  





df -h / /home 2>/dev/null | awk -v t="$THRESHOLD" '  





  NR > 1 && $5+0 >= t {  





    printf "⚠ Disk %s full on %s\n", $5, $6  





  }  





'  





EOF  





chmod +x ~/.hermes/scripts/disk-alert.sh  





  





hermes cron create "*/15 * * * *" \  





  --no-agent \  





  --script disk-alert.sh \  





  --deliver telegram \  





  --name "disk-alert"  



```

Silent when both filesystems are under 90%; fires exactly one line per over-threshold filesystem when one fills up.
## Comparison with Other Patterns[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#comparison-with-other-patterns "Direct link to Comparison with Other Patterns")  
| Approach  | What runs  | When to use  |  
| --- | --- | --- |  
|  `cronjob --no-agent` (this page)  | Your script on Hermes' schedule  | Recurring watchdogs / alerts / metrics that don't need reasoning  |  
|  `cronjob_manage` (default, LLM)  | Agent with optional pre-check script  | When the message content requires reasoning over data  |  
| OS cron + `curl` to a [webhook subscription](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks)  | Your script on the OS schedule  | When Hermes might be unhealthy (the thing you're monitoring)  |  
For critical system-health watchdogs that must fire _even when the gateway is down_ , use OS-level cron with a plain `curl` to a Hermes webhook subscription (or any external alerting endpoint) — those run as independent OS processes and don't depend on Hermes being up. The in-gateway scheduler is the right choice when the thing being monitored is external.
## Related[​](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#related "Direct link to Related")
  * [Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron) — LLM-driven cron patterns.
  * [Scheduled Tasks (Cron) reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) — full schedule syntax, lifecycle, delivery routing.
  * [Webhook Subscriptions](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks) — fire-and-forget HTTP entry points for external schedulers.
  * [Gateway Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-internals) — delivery-router internals.


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/cron-script-only.md)
[Previous Automate Anything with Cron](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)[Next Automation Blueprints](https://hermes-agent.nousresearch.com/docs/guides/automation-blueprints)
  * [When to Use It](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#when-to-use-it)
  * [Create One from Chat](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#create-one-from-chat)
    * [Example transcript](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#example-transcript)
    * [What the agent decides for you](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#what-the-agent-decides-for-you)
    * [Managing watchdogs from chat](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#managing-watchdogs-from-chat)
  * [Create One from the CLI](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#create-one-from-the-cli)
  * [How Script Output Maps to Delivery](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#how-script-output-maps-to-delivery)
  * [Script Rules](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#script-rules)
    * [Using your own Python environment](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#using-your-own-python-environment)
  * [Schedule Syntax](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#schedule-syntax)
  * [Delivery Targets](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#delivery-targets)
  * [Editing and Lifecycle](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#editing-and-lifecycle)
  * [Worked Example: Disk Space Alert](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#worked-example-disk-space-alert)
  * [Comparison with Other Patterns](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#comparison-with-other-patterns)
  * [Related](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only#related)


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
