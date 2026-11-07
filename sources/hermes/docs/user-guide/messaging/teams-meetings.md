---
title: "Teams Meetings"
source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings
scraped_at: 2026-11-07T17:19:55.792652+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/teams-meetings)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
    * [Popular](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram)
    * [Microsoft 365](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)
      * [Microsoft Teams](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)
      * [Teams Meetings](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings)
      * [Microsoft Graph Webhook Listener](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/msgraph-webhook)
    * [Chinese platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/dingtalk)
    * [Other](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/a2a)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Messaging Platforms
  * Microsoft 365
  * Teams Meetings


On this page
# Microsoft Teams Meetings
Use the Teams meeting pipeline when you want Hermes to ingest Microsoft Graph meeting events, fetch transcripts first, fall back to recordings plus STT when needed, and deliver a structured summary to downstream sinks.
Prerequisites: see [Microsoft Teams](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams) for the underlying bot/credential setup.
> Run `hermes gateway setup` and pick **Teams Meetings** for a guided walk-through.
This page focuses on setup and enablement:
  * Graph credentials
  * webhook listener configuration
  * Teams delivery modes
  * pipeline config shape


For day-2 operations, go-live checks, and the operator worksheet, use the dedicated guide: [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline).
## What This Feature Does[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#what-this-feature-does "Direct link to What This Feature Does")
The pipeline:
  1. receives Microsoft Graph webhook events
  2. resolves the meeting and prefers transcript artifacts first
  3. falls back to recording download plus STT when no usable transcript is available
  4. stores durable job state and sink records locally
  5. can write summaries to Notion, Linear, and Microsoft Teams


Operator actions stay in the CLI (the `teams-pipeline` subcommand is registered by the `teams_pipeline` plugin — enable it via `hermes plugins enable teams_pipeline` or set `plugins.enabled: [teams_pipeline]` in `config.yaml`):

```


hermes teams-pipeline validate  





hermes teams-pipeline list  





hermes teams-pipeline maintain-subscriptions  



```

## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#prerequisites "Direct link to Prerequisites")
Before enabling the meetings pipeline, make sure you have:
  * a working Hermes install
  * the existing [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams) if you want Teams outbound delivery
  * Microsoft Graph application credentials with the permissions required for the meeting resources you plan to subscribe to
  * a public HTTPS URL that Microsoft Graph can call for webhook delivery
  * `ffmpeg` installed if you want recording-plus-STT fallback


## Step 1: Add Microsoft Graph Credentials[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-1-add-microsoft-graph-credentials "Direct link to Step 1: Add Microsoft Graph Credentials")
Add Graph app-only credentials to `~/.hermes/.env`:

```


MSGRAPH_TENANT_ID=<tenant-id>  





MSGRAPH_CLIENT_ID=<client-id>  





MSGRAPH_CLIENT_SECRET=<client-secret>  



```

These credentials are used by:
  * the Graph client foundation
  * subscription maintenance commands
  * meeting resolution and artifact fetches
  * Graph-based Teams outbound delivery when you do not provide a dedicated Teams access token


## Step 2: Enable the Graph Webhook Listener[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-2-enable-the-graph-webhook-listener "Direct link to Step 2: Enable the Graph Webhook Listener")
The webhook listener is a gateway platform named `msgraph_webhook`. At minimum, enable it and set a client state value:

```


MSGRAPH_WEBHOOK_ENABLED=true  





MSGRAPH_WEBHOOK_PORT=8646  





MSGRAPH_WEBHOOK_CLIENT_STATE=<random-shared-secret>  





MSGRAPH_WEBHOOK_ACCEPTED_RESOURCES=communications/onlineMeetings  



```

The bind host is read from the platform's `extra.host` in `config.yaml` (there is no `MSGRAPH_WEBHOOK_HOST` env var — see the [webhook listener reference](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/msgraph-webhook)).
The listener exposes:
  * `/msgraph/webhook` for Graph notifications
  * `/health` for a simple health check


You need to route your public HTTPS endpoint to that listener. For example, if your public domain is `https://ops.example.com`, your Graph notification URL would typically be:

```


https://ops.example.com/msgraph/webhook  



```

## Step 3: Configure Teams Delivery and Pipeline Behavior[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-3-configure-teams-delivery-and-pipeline-behavior "Direct link to Step 3: Configure Teams Delivery and Pipeline Behavior")
The meeting pipeline reads its runtime config from the existing `teams` platform entry. Pipeline-specific knobs live under `teams.extra.meeting_pipeline`. Teams outbound delivery stays on the normal Teams platform config surface.
Example `~/.hermes/config.yaml`:

```


platforms:  





  msgraph_webhook:  





    enabled: true  





    extra:  





      host: 127.0.0.1  





      port: 8646  





      client_state: "replace-me"  





      accepted_resources:  





        - "communications/onlineMeetings"  





  





  teams:  





    enabled: true  





    extra:  





      client_id: "your-teams-client-id"  





      client_secret: "your-teams-client-secret"  





      tenant_id: "your-teams-tenant-id"  





  





      # outbound summary delivery  





      delivery_mode: "graph" # or incoming_webhook  





      team_id: "team-id"  





      channel_id: "channel-id"  





      # incoming_webhook_url: "https://..."  





  





      meeting_pipeline:  





        transcript_min_chars: 80  





        transcript_required: false  





        transcription_fallback: true  





        ffmpeg_extract_audio: true  





        notion:  





          enabled: false  





        linear:  





          enabled: false  



```

If you bind the listener to a non-loopback host such as `0.0.0.0`, you must also set `allowed_source_cidrs` to Microsoft's webhook egress ranges. Loopback binds (`127.0.0.1` / `::1`) are the intended dev-tunnel and local reverse-proxy setup.
## Teams Delivery Modes[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#teams-delivery-modes "Direct link to Teams Delivery Modes")
The pipeline supports two Teams summary-delivery modes inside the existing Teams plugin.
###  `incoming_webhook`[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#incoming_webhook "Direct link to incoming_webhook")
Use this when you want a simple webhook post into Teams without channel-message creation through Graph.
Required config:

```


platforms:  





  teams:  





    enabled: true  





    extra:  





      delivery_mode: "incoming_webhook"  





      incoming_webhook_url: "https://..."  



```

###  `graph`[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#graph "Direct link to graph")
Use this when you want Hermes to post the summary through Microsoft Graph into a Teams chat or channel.
Supported targets:
  * `chat_id`
  * `team_id` + `channel_id`
  * `team_id` + `home_channel` fallback for the existing Teams platform


Example:

```


platforms:  





  teams:  





    enabled: true  





    extra:  





      delivery_mode: "graph"  





      team_id: "team-id"  





      channel_id: "channel-id"  



```

## Step 4: Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-4-start-the-gateway "Direct link to Step 4: Start the Gateway")
Start Hermes normally after updating config:

```


hermes gateway run  



```

Or, if you run Hermes in Docker, start the gateway the same way you already do for your deployment.
Check the listener:

```


curl http://localhost:8646/health  



```

## Step 5: Create Graph Subscriptions[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-5-create-graph-subscriptions "Direct link to Step 5: Create Graph Subscriptions")
Use the plugin CLI to create and inspect subscriptions.
Examples:

```


hermes teams-pipeline subscribe \  





  --resource communications/onlineMeetings/getAllTranscripts \  





  --notification-url https://ops.example.com/msgraph/webhook \  





  --client-state "$MSGRAPH_WEBHOOK_CLIENT_STATE"  





  





hermes teams-pipeline subscribe \  





  --resource communications/onlineMeetings/getAllRecordings \  





  --notification-url https://ops.example.com/msgraph/webhook \  





  --client-state "$MSGRAPH_WEBHOOK_CLIENT_STATE"  



```

Microsoft Graph caps webhook subscriptions at 72 hours and will not auto-renew them. You MUST schedule `hermes teams-pipeline maintain-subscriptions` before going live, or notifications will silently stop three days after any manual subscription creation. See [Automating subscription renewal](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline#automating-subscription-renewal-required-for-production) in the operator runbook — three options (Hermes cron, systemd timer, plain crontab).
For subscription maintenance and day-2 operator flows, continue with the guide: [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline).
## Validation[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#validation "Direct link to Validation")
Run the built-in validation snapshot:

```


hermes teams-pipeline validate  



```

Useful companion checks:

```


hermes teams-pipeline token-health  





hermes teams-pipeline subscriptions  



```

## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#troubleshooting "Direct link to Troubleshooting")  
| Problem  | What to check  |  
| --- | --- |  
| Graph webhook validation fails  | Confirm the public URL is correct and reachable, and that Graph is calling the exact `/msgraph/webhook` path  |  
| Jobs do not appear in `hermes teams-pipeline list`  | Confirm `msgraph_webhook` is enabled and that subscriptions point at the right notification URL  |  
| Transcript-first never succeeds  | Check Graph permissions for transcript resources and whether the transcript artifact exists for that meeting  |  
| Recording fallback fails  | Confirm `ffmpeg` is installed and the Graph app can access recording artifacts  |  
| Teams summary delivery fails  | Re-check `delivery_mode`, target IDs, and Teams auth config  |  
## Related Docs[​](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#related-docs "Direct link to Related Docs")
  * [Microsoft Teams bot setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)
  * [Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/messaging/teams-meetings.md)
[Previous Microsoft Teams](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams)[Next Microsoft Graph Webhook Listener](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/msgraph-webhook)
  * [What This Feature Does](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#what-this-feature-does)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#prerequisites)
  * [Step 1: Add Microsoft Graph Credentials](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-1-add-microsoft-graph-credentials)
  * [Step 2: Enable the Graph Webhook Listener](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-2-enable-the-graph-webhook-listener)
  * [Step 3: Configure Teams Delivery and Pipeline Behavior](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-3-configure-teams-delivery-and-pipeline-behavior)
  * [Teams Delivery Modes](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#teams-delivery-modes)
    * [`incoming_webhook`](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#incoming_webhook)
    * [`graph`](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#graph)
  * [Step 4: Start the Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-4-start-the-gateway)
  * [Step 5: Create Graph Subscriptions](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#step-5-create-graph-subscriptions)
  * [Validation](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#validation)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#troubleshooting)
  * [Related Docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/teams-meetings#related-docs)


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
