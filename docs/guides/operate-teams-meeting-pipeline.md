---
title: "Operate the Teams Meeting Pipeline"
source: https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline
scraped_at: 2026-11-07T17:20:11.926734+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/operate-teams-meeting-pipeline)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Operate the Teams Meeting Pipeline


On this page
# Operate the Teams Meeting Pipeline
Use this guide after you have already enabled the feature from [Teams Meetings](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings).
This page covers:
  * operator CLI flows
  * routine subscription maintenance
  * failure triage
  * go-live checks
  * rollout worksheet


## Core Operator Commands[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#core-operator-commands "Direct link to Core Operator Commands")
### Validate the config snapshot[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#validate-the-config-snapshot "Direct link to Validate the config snapshot")

```


hermes teams-pipeline validate  



```

Use this first after any config change.
### Inspect token health[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-token-health "Direct link to Inspect token health")

```


hermes teams-pipeline token-health  





hermes teams-pipeline token-health --force-refresh  



```

Use `--force-refresh` when you suspect stale auth state.
### Inspect subscriptions[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-subscriptions "Direct link to Inspect subscriptions")

```


hermes teams-pipeline subscriptions  



```

### Renew near-expiry subscriptions[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#renew-near-expiry-subscriptions "Direct link to Renew near-expiry subscriptions")

```


hermes teams-pipeline maintain-subscriptions  





hermes teams-pipeline maintain-subscriptions --dry-run  



```

### Automating subscription renewal (REQUIRED for production)[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production "Direct link to Automating subscription renewal \(REQUIRED for production\)")
**Microsoft Graph subscriptions expire in at most 72 hours.** If nothing renews them, meeting notifications silently stop after 3 days and the pipeline looks "broken." This is the #1 operational failure mode for any Graph-backed integration.
You MUST run `maintain-subscriptions` on a schedule. Pick one of these three options:
#### Option 1: Hermes cron (recommended if you already run the Hermes gateway)[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#option-1-hermes-cron-recommended-if-you-already-run-the-hermes-gateway "Direct link to Option 1: Hermes cron \(recommended if you already run the Hermes gateway\)")
Hermes ships a built-in cron scheduler. The `--no-agent` mode runs a script as the job (rather than using an LLM), and `--script` must point at a file under `~/.hermes/scripts/`. First create the script:

```


mkdir -p ~/.hermes/scripts  





cat > ~/.hermes/scripts/maintain-teams-subscriptions.sh <<'EOF'  





#!/usr/bin/env bash  





exec hermes teams-pipeline maintain-subscriptions  





EOF  





chmod +x ~/.hermes/scripts/maintain-teams-subscriptions.sh  



```

Then register a script-only cron job that runs every 12 hours (gives 6x headroom against the 72h expiry window):

```


hermes cron create "0 */12 * * *" \  





  --name "teams-pipeline-maintain-subscriptions" \  





  --no-agent \  





  --script maintain-teams-subscriptions.sh \  





  --deliver local  



```

Verify it was registered and inspect the next run time:

```


hermes cron list  





hermes cron status        # scheduler status  



```

#### Option 2: systemd timer (recommended for Linux production deployments)[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#option-2-systemd-timer-recommended-for-linux-production-deployments "Direct link to Option 2: systemd timer \(recommended for Linux production deployments\)")
Create `/etc/systemd/system/hermes-teams-pipeline-maintain.service`:

```


[Unit]  





Description=Hermes Teams pipeline subscription maintenance  





After=network-online.target  





  





[Service]  





Type=oneshot  





User=hermes  





EnvironmentFile=/etc/hermes/env  





ExecStart=/usr/local/bin/hermes teams-pipeline maintain-subscriptions  



```

And `/etc/systemd/system/hermes-teams-pipeline-maintain.timer`:

```


[Unit]  





Description=Run Hermes Teams pipeline subscription maintenance every 12 hours  





  





[Timer]  





OnBootSec=5min  





OnUnitActiveSec=12h  





Persistent=true  





  





[Install]  





WantedBy=timers.target  



```

Enable:

```


sudo systemctl daemon-reload  





sudo systemctl enable --now hermes-teams-pipeline-maintain.timer  





systemctl list-timers hermes-teams-pipeline-maintain.timer  



```

#### Option 3: Plain crontab[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#option-3-plain-crontab "Direct link to Option 3: Plain crontab")

```


0 */12 * * * /usr/local/bin/hermes teams-pipeline maintain-subscriptions >> /var/log/hermes/teams-pipeline-maintain.log 2>&1  



```

Make sure the cron environment has the `MSGRAPH_*` credentials. Simplest fix: source `~/.hermes/.env` at the top of a wrapper script that crontab calls.
#### Verifying renewal is working[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#verifying-renewal-is-working "Direct link to Verifying renewal is working")
After you've set up the schedule, check renewal activity after the first scheduled run:

```


hermes teams-pipeline subscriptions   # should show expirationDateTime advanced  





hermes teams-pipeline maintain-subscriptions --dry-run   # should show "0 expiring soon" most of the time  



```

If you ever see your Graph webhook mysteriously "stop working" after exactly ~72 hours, this is the first thing to check: did the renewal job actually run?
### Inspect recent jobs[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-recent-jobs "Direct link to Inspect recent jobs")

```


hermes teams-pipeline list  





hermes teams-pipeline list --status failed  





hermes teams-pipeline show <job-id>  



```

### Replay a stored job[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#replay-a-stored-job "Direct link to Replay a stored job")

```


hermes teams-pipeline run <job-id>  



```

### Dry-run meeting artifact fetches[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#dry-run-meeting-artifact-fetches "Direct link to Dry-run meeting artifact fetches")

```


hermes teams-pipeline fetch --meeting-id <meeting-id>  





hermes teams-pipeline fetch --join-web-url "<join-url>"  





hermes teams-pipeline fetch --join-web-url "<join-url>" --organizer-user-id <entra-user-id>  



```

Pass `--organizer-user-id` (the organizer's Microsoft Entra user ID) to resolve through the organizer-scoped `/users/{id}/onlineMeetings` Graph path. This is required for Teams `/meet/` short URLs, which Graph rejects on the `/communications/onlineMeetings` endpoint. Webhook-driven jobs derive the organizer automatically from the notification's `@odata.id`.
## Routine Runbook[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#routine-runbook "Direct link to Routine Runbook")
### After first setup[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#after-first-setup "Direct link to After first setup")
Run these in order:

```


hermes teams-pipeline validate  





hermes teams-pipeline token-health --force-refresh  





hermes teams-pipeline subscriptions  



```

Then trigger or wait for a real meeting event and confirm:

```


hermes teams-pipeline list  





hermes teams-pipeline show <job-id>  



```

### Daily or periodic checks[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#daily-or-periodic-checks "Direct link to Daily or periodic checks")
  * run `hermes teams-pipeline maintain-subscriptions --dry-run`
  * inspect `hermes teams-pipeline list --status failed`
  * verify the Teams delivery target is still the correct chat or channel


### Before changing webhook URLs or delivery targets[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#before-changing-webhook-urls-or-delivery-targets "Direct link to Before changing webhook URLs or delivery targets")
  * update the public notification URL or Teams target config
  * run `hermes teams-pipeline validate`
  * renew or recreate affected subscriptions
  * confirm new events land in the expected sink


## Failure Triage[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#failure-triage "Direct link to Failure Triage")
### No jobs are being created[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#no-jobs-are-being-created "Direct link to No jobs are being created")
Check:
  * `msgraph_webhook` is enabled
  * the public notification URL points to `/msgraph/webhook`
  * the client state in the subscription matches `MSGRAPH_WEBHOOK_CLIENT_STATE`
  * subscriptions still exist remotely and are not expired


### Jobs stay in retry or fail before summarization[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#jobs-stay-in-retry-or-fail-before-summarization "Direct link to Jobs stay in retry or fail before summarization")
Check:
  * transcript permissions and availability
  * recording permissions and artifact availability
  * `ffmpeg` availability if recording fallback is enabled
  * Graph token health


### Summaries are produced but not delivered to Teams[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#summaries-are-produced-but-not-delivered-to-teams "Direct link to Summaries are produced but not delivered to Teams")
Check:
  * `platforms.teams.enabled: true`
  * `delivery_mode`
  * `incoming_webhook_url` for webhook mode
  * `chat_id` or `team_id` plus `channel_id` for Graph mode
  * Teams auth config if Graph posting is used


### Duplicate or unexpected replays[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#duplicate-or-unexpected-replays "Direct link to Duplicate or unexpected replays")
Check:
  * whether you manually replayed a job with `hermes teams-pipeline run`
  * whether the sink record already exists for that meeting
  * whether you intentionally enabled a resend path in your local config


## Go-Live Checklist[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#go-live-checklist "Direct link to Go-Live Checklist")
  * Graph credentials are present and correct
  * `msgraph_webhook` is enabled and reachable from the public internet
  * `MSGRAPH_WEBHOOK_CLIENT_STATE` is set and matches subscriptions
  * transcript subscription is created
  * recording subscription is created if STT fallback is required
  * `ffmpeg` is installed if recording fallback is enabled
  * Teams outbound delivery target is configured and verified
  * Notion and Linear sinks are configured only if actually needed
  * `hermes teams-pipeline validate` returns an OK snapshot
  * `hermes teams-pipeline token-health --force-refresh` succeeds
  * **`maintain-subscriptions`is scheduled** (Hermes cron, systemd timer, or crontab — see [Automating subscription renewal](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production)). Without this, Graph subscriptions silently expire within 72 hours.
  * a real end-to-end meeting event has produced a stored job
  * at least one summary has reached the intended delivery sink


## Delivery-Mode Decision Guide[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#delivery-mode-decision-guide "Direct link to Delivery-Mode Decision Guide")  
| Mode  | Use when  | Tradeoff  |  
| --- | --- | --- |  
| `incoming_webhook`  | you only need simple posting into Teams  | simplest setup, less control  |  
| `graph`  | you need channel or chat posting through Graph  | more control, more auth and target config  |  
## Operator Worksheet[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#operator-worksheet "Direct link to Operator Worksheet")
Fill this out before rollout:  
| Item  | Value  |  
| --- | --- |  
| Public notification URL  |   |  
| Graph tenant ID  |   |  
| Graph client ID  |   |  
| Webhook client state  |   |  
| Transcript resource subscription  |   |  
| Recording resource subscription  |   |  
| Teams delivery mode  |   |  
| Teams chat ID or team/channel  |   |  
| Notion database ID  |   |  
| Linear team ID  |   |  
| Store path override, if any  |   |  
| Owner for daily checks  |   |  
## Change Review Worksheet[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#change-review-worksheet "Direct link to Change Review Worksheet")
Use this before changing the deployment:  
| Question  | Answer  |  
| --- | --- |  
| Are we changing the public webhook URL?  |   |  
| Are we rotating Graph credentials?  |   |  
| Are we changing Teams delivery mode?  |   |  
| Are we moving to a new Teams chat or channel?  |   |  
| Do subscriptions need to be recreated or renewed?  |   |  
| Do we need a fresh end-to-end verification run?  |   |  
## Related Docs[​](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#related-docs "Direct link to Related Docs")
  * [Teams Meetings setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings)
  * [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/operate-teams-meeting-pipeline.md)
[Previous Register a Microsoft Graph Application](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)[Next Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Core Operator Commands](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#core-operator-commands)
    * [Validate the config snapshot](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#validate-the-config-snapshot)
    * [Inspect token health](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-token-health)
    * [Inspect subscriptions](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-subscriptions)
    * [Renew near-expiry subscriptions](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#renew-near-expiry-subscriptions)
    * [Automating subscription renewal (REQUIRED for production)](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production)
    * [Inspect recent jobs](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#inspect-recent-jobs)
    * [Replay a stored job](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#replay-a-stored-job)
    * [Dry-run meeting artifact fetches](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#dry-run-meeting-artifact-fetches)
  * [Routine Runbook](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#routine-runbook)
    * [After first setup](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#after-first-setup)
    * [Daily or periodic checks](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#daily-or-periodic-checks)
    * [Before changing webhook URLs or delivery targets](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#before-changing-webhook-urls-or-delivery-targets)
  * [Failure Triage](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#failure-triage)
    * [No jobs are being created](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#no-jobs-are-being-created)
    * [Jobs stay in retry or fail before summarization](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#jobs-stay-in-retry-or-fail-before-summarization)
    * [Summaries are produced but not delivered to Teams](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#summaries-are-produced-but-not-delivered-to-teams)
    * [Duplicate or unexpected replays](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#duplicate-or-unexpected-replays)
  * [Go-Live Checklist](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#go-live-checklist)
  * [Delivery-Mode Decision Guide](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#delivery-mode-decision-guide)
  * [Operator Worksheet](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#operator-worksheet)
  * [Change Review Worksheet](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#change-review-worksheet)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#related-docs)


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
