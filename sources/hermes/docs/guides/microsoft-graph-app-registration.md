---
title: "Register a Microsoft Graph Application"
source: https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration
scraped_at: 2026-11-07T17:20:11.922735+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/microsoft-graph-app-registration)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Register a Microsoft Graph Application


On this page
# Register a Microsoft Graph Application
The Teams meeting pipeline reads meeting transcripts, recordings, and related artifacts from Microsoft Graph using **app-only** (daemon) authentication — no user sign-in, no interactive consent per meeting. That requires an Azure AD application registration with admin-consented application permissions.
This guide walks through:
  1. Creating the app registration
  2. Creating a client secret
  3. Granting the Graph API permissions the pipeline needs
  4. Admin-consenting those permissions
  5. (Optional) Scoping the app to specific users with an Application Access Policy


You need **tenant admin rights** (or an admin to grant consent on your behalf) to finish this. Bookmark the values you collect — they go into `~/.hermes/.env` at the end.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#prerequisites "Direct link to Prerequisites")
  * A Microsoft 365 tenant with Teams Premium or Teams licenses that produce meeting transcripts and recordings
  * Admin access to the Azure portal at [entra.microsoft.com](https://entra.microsoft.com)
  * A publicly reachable HTTPS endpoint for Graph change notifications (set up later, in the webhook listener step)


## Step 1: Create the App Registration[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-1-create-the-app-registration "Direct link to Step 1: Create the App Registration")
  1. Sign in to [entra.microsoft.com](https://entra.microsoft.com) as a tenant admin.
  2. Navigate to **Identity → Applications → App registrations**.
  3. Click **New registration**.
  4. Fill in:
     * **Name:** `Hermes Teams Meeting Pipeline` (or any name you'll recognize).
     * **Supported account types:** _Accounts in this organizational directory only (Single tenant)_.
     * **Redirect URI:** leave blank — app-only auth does not need one.
  5. Click **Register**.


You'll land on the app's overview page. Copy two values:
  * **Application (client) ID** → `MSGRAPH_CLIENT_ID`
  * **Directory (tenant) ID** → `MSGRAPH_TENANT_ID`


## Step 2: Create a Client Secret[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-2-create-a-client-secret "Direct link to Step 2: Create a Client Secret")
  1. In the left nav, open **Certificates & secrets**.
  2. Click **New client secret**.
  3. **Description:** `hermes-graph-secret`. **Expires:** pick a value that matches your rotation policy (6-24 months is typical).
  4. Click **Add**.
  5. Copy the **Value** column immediately — it's only shown once. That value is `MSGRAPH_CLIENT_SECRET`.


> The **Secret ID** column is not the secret. You want the **Value** column.
## Step 3: Grant Graph API Permissions[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-3-grant-graph-api-permissions "Direct link to Step 3: Grant Graph API Permissions")
The pipeline uses a minimum-viable set of application permissions. Add only what you need; each one widens what the app can read tenant-wide.
  1. In the left nav, open **API permissions**.
  2. Click **Add a permission** → **Microsoft Graph** → **Application permissions**.
  3. Add the permissions from the table below that match what you want the pipeline to do.
  4. After adding, click **Grant admin consent for`<your tenant>`**. The Status column should flip to a green checkmark for every permission.


### Required for transcript-first summaries[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-transcript-first-summaries "Direct link to Required for transcript-first summaries")  
| Permission  | What it lets the app do  |  
| --- | --- |  
| `OnlineMeetings.Read.All`  | Read Teams online meeting metadata (subject, participants, join URL).  |  
| `OnlineMeetingTranscript.Read.All`  | Read meeting transcripts generated by Teams.  |  
### Required for recording fallback (when a transcript is unavailable)[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-recording-fallback-when-a-transcript-is-unavailable "Direct link to Required for recording fallback \(when a transcript is unavailable\)")  
| Permission  | What it lets the app do  |  
| --- | --- |  
| `OnlineMeetingRecording.Read.All`  | Download Teams meeting recordings for offline STT processing.  |  
| `CallRecords.Read.All`  | Resolve meetings from call records when only the join URL is known.  |  
### Required for outbound summary delivery (Graph mode only)[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-outbound-summary-delivery-graph-mode-only "Direct link to Required for outbound summary delivery \(Graph mode only\)")
If `platforms.teams.extra.delivery_mode` is `graph`, the pipeline posts summaries into a Teams channel or chat via the Graph API. Skip these if you use `incoming_webhook` delivery mode instead.  
| Permission  | What it lets the app do  |  
| --- | --- |  
| `ChannelMessage.Send`  | Post messages into Teams channels on behalf of the app.  |  
| `Chat.ReadWrite.All`  | Post messages into 1:1 and group chats (only if you set `chat_id` as the delivery target).  |  
### Not recommended[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#not-recommended "Direct link to Not recommended")
  * `OnlineMeetings.ReadWrite.All` / `Chat.ReadWrite` without `.All` — broader than the pipeline needs.
  * Delegated permissions — the pipeline uses app-only (client-credentials) flow; delegated permissions won't work without user sign-in.


## Step 4: (Recommended) Scope the App with an Application Access Policy[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-4-recommended-scope-the-app-with-an-application-access-policy "Direct link to Step 4: \(Recommended\) Scope the App with an Application Access Policy")
By default, application permissions like `OnlineMeetings.Read.All` grant the app access to **every** meeting in the tenant. For partner demos and dev tenants that's fine; for production you almost certainly want to restrict which users' meetings the app can read.
Microsoft provides **Application Access Policies** for Teams exactly for this. The policy is a PowerShell-only surface; there's no portal UI for it.
From an admin PowerShell with the MicrosoftTeams module installed and connected (`Connect-MicrosoftTeams`):

```


# Create a policy scoped to the Hermes app  





New-CsApplicationAccessPolicy `  





  -Identity "Hermes-Meeting-Pipeline-Policy" `  





  -AppIds "<MSGRAPH_CLIENT_ID>" `  





  -Description "Restrict Hermes meeting pipeline to allow-listed users"  





  





# Grant the policy to specific users whose meetings the pipeline may read  





Grant-CsApplicationAccessPolicy `  





  -PolicyName "Hermes-Meeting-Pipeline-Policy" `  





  -Identity "alice@example.com"  





  





Grant-CsApplicationAccessPolicy `  





  -PolicyName "Hermes-Meeting-Pipeline-Policy" `  





  -Identity "bob@example.com"  



```

Propagation can take up to 30 minutes after granting. Verify with:

```


Test-CsApplicationAccessPolicy -Identity "alice@example.com" -AppId "<MSGRAPH_CLIENT_ID>"  



```

Without the policy, **any** user's meetings are readable — that's what the permission technically grants. Don't skip this step on a production tenant.
## Step 5: Write the Credentials to Your Env File[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-5-write-the-credentials-to-your-env-file "Direct link to Step 5: Write the Credentials to Your Env File")
Put the three values you collected into `~/.hermes/.env`:

```


MSGRAPH_TENANT_ID=<directory-tenant-id>  





MSGRAPH_CLIENT_ID=<application-client-id>  





MSGRAPH_CLIENT_SECRET=<client-secret-value>  



```

Set file permissions so only you can read the secret:

```


chmod 600 ~/.hermes/.env  



```

## Step 6: Verify the Token Flow[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-6-verify-the-token-flow "Direct link to Step 6: Verify the Token Flow")
Hermes ships a Graph auth smoke-test. From your Hermes install:

```


python -c "  





import asyncio  





from tools.microsoft_graph_auth import MicrosoftGraphTokenProvider  





provider = MicrosoftGraphTokenProvider.from_env()  





token = asyncio.run(provider.get_access_token())  





print('Token acquired, length:', len(token))  





print(provider.inspect_token_health())  





"  



```

A successful run prints a long token string and a health dict showing `cached: True` and an `expires_in_seconds` value near 3600. Failures produce a `MicrosoftGraphTokenError` with the Azure error code — the most common are:  
| Azure error  | Meaning  | Fix  |  
| --- | --- | --- |  
| `AADSTS7000215: Invalid client secret`  | Secret value mismatched or expired.  | Generate a new secret in step 2; update `.env`.  |  
| `AADSTS700016: Application not found`  | Wrong `MSGRAPH_CLIENT_ID` or wrong tenant.  | Double-check the values from step 1 are from the same app.  |  
| `AADSTS90002: Tenant not found`  | Typo in `MSGRAPH_TENANT_ID`.  | Copy the Directory (tenant) ID from the app overview again.  |  
|  `insufficient_claims` at call time (not token time)  | Token acquires but Graph returns 401/403.  | You skipped step 3 admin-consent, or added permissions but haven't re-consented. Revisit API permissions and click **Grant admin consent** again.  |  
## Rotating the Client Secret[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#rotating-the-client-secret "Direct link to Rotating the Client Secret")
Azure client secrets have a hard expiry. Before yours expires:
  1. Create a second client secret in step 2 without deleting the first one.
  2. Update `MSGRAPH_CLIENT_SECRET` in `~/.hermes/.env` with the new value.
  3. Restart the gateway so the new secret is picked up: `hermes gateway restart`.
  4. Verify with the smoke test above.
  5. Delete the old secret from the Azure portal.


## Next Steps[​](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#next-steps "Direct link to Next Steps")
Once credentials verify cleanly, continue with:
  * **Webhook listener setup** — stand up the `msgraph_webhook` gateway platform that receives Graph change notifications.
  * **Pipeline configuration** — configure the Teams meeting pipeline runtime and operator CLI.
  * **Outbound delivery** — wire summaries back into a Teams channel or chat.


Those pages land alongside the PRs that add the corresponding runtime. This credentials setup is a standalone prerequisite and is safe to complete in advance.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/microsoft-graph-app-registration.md)
[Previous OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)[Next Operate the Teams Meeting Pipeline](https://hermes-agent.nousresearch.com/docs/guides/operate-teams-meeting-pipeline)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#prerequisites)
  * [Step 1: Create the App Registration](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-1-create-the-app-registration)
  * [Step 2: Create a Client Secret](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-2-create-a-client-secret)
  * [Step 3: Grant Graph API Permissions](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-3-grant-graph-api-permissions)
    * [Required for transcript-first summaries](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-transcript-first-summaries)
    * [Required for recording fallback (when a transcript is unavailable)](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-recording-fallback-when-a-transcript-is-unavailable)
    * [Required for outbound summary delivery (Graph mode only)](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#required-for-outbound-summary-delivery-graph-mode-only)
    * [Not recommended](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#not-recommended)
  * [Step 4: (Recommended) Scope the App with an Application Access Policy](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-4-recommended-scope-the-app-with-an-application-access-policy)
  * [Step 5: Write the Credentials to Your Env File](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-5-write-the-credentials-to-your-env-file)
  * [Step 6: Verify the Token Flow](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#step-6-verify-the-token-flow)
  * [Rotating the Client Secret](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#rotating-the-client-secret)
  * [Next Steps](https://hermes-agent.nousresearch.com/docs/guides/microsoft-graph-app-registration#next-steps)


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
