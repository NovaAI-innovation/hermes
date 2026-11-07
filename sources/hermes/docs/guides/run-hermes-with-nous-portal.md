---
title: "Run Hermes Agent with Nous Portal"
source: https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal
scraped_at: 2026-11-07T17:20:11.928734+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/run-hermes-with-nous-portal)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Run Hermes Agent with Nous Portal


On this page
# Run Hermes Agent with Nous Portal
This guide walks you through running Hermes Agent on a [Nous Portal](https://portal.nousresearch.com) subscription end to end — from signing up to verifying that every tool routes correctly. If you just want the overview of what the Portal is and what's in the subscription, see the [Nous Portal integration page](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal). This page is the task script.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#prerequisites "Direct link to Prerequisites")
  * Hermes Agent installed ([Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart))
  * A web browser on the machine you're setting up (or SSH port forwarding — see [OAuth over SSH](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh))
  * About 5 minutes


You do **not** need: an OpenAI key, an Anthropic key, a web search account, a FAL account, a Browser Use account, or any other per-vendor credential. That's the whole point.
## 1. Get a subscription[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#1-get-a-subscription "Direct link to 1. Get a subscription")
Open [portal.nousresearch.com/manage-subscription](https://portal.nousresearch.com/manage-subscription), sign up, and pick a plan.
Already subscribed? Skip to step 2.
## 2. Run the one-shot setup[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#2-run-the-one-shot-setup "Direct link to 2. Run the one-shot setup")

```


hermes setup --portal  



```

This single command does five things:
  1. Opens your browser to portal.nousresearch.com for OAuth login
  2. Stores the refresh token at `~/.hermes/auth.json`
  3. Sets `model.provider: nous` in `~/.hermes/config.yaml`
  4. Picks a default agentic model (`anthropic/claude-sonnet-4.6` or similar)
  5. Turns on the Tool Gateway for web search, image generation, TTS, and browser automation


When it finishes, you're back at your terminal ready to chat.
### What if I'm SSH'd into a server?[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#what-if-im-sshd-into-a-server "Direct link to What if I'm SSH'd into a server?")
OAuth needs a browser, but the loopback callback runs on the machine where Hermes is running. Two options:

```


# Option A: SSH port forwarding (preferred)  





ssh -N -L 8642:127.0.0.1:8642 user@remote-host    # in a local terminal  





hermes setup --portal                              # on the remote, open the printed URL in your local browser  





  





# Option B: device-code login (works from Cloud Shell, Codespaces, EC2 Instance Connect)  





hermes auth add nous --type oauth  





# Then re-run `hermes setup --portal` to wire the provider + gateway  



```

See [OAuth over SSH / Remote Hosts](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh) for the full walkthrough including ProxyJump chains, mosh/tmux, and ControlMaster gotchas.
## 3. Verify it worked[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#3-verify-it-worked "Direct link to 3. Verify it worked")

```


hermes portal info  



```

You should see:

```


  Nous Portal  





  ───────────  





  Auth:    ✓ logged in  





  Portal:  https://portal.nousresearch.com  





  Model:   ✓ using Nous as inference provider  





  





  Tool Gateway  





  ────────────  





  Web search & extract  via Nous Portal  





  Image generation      via Nous Portal  





  Text-to-speech        via Nous Portal  





  Browser automation    via Nous Portal  



```

If any line shows something other than "via Nous Portal" or the auth line says "not logged in", jump to [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#troubleshooting) below.
## 4. Run your first conversation[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#4-run-your-first-conversation "Direct link to 4. Run your first conversation")

```


hermes chat  



```

Try something that exercises both the model and the Tool Gateway:

```


Hey, search the web for "Hermes Agent release notes" and summarize the top 3 hits.  



```

You should see Hermes call `web_search` (through the gateway) and respond with a summary. If the search runs and the response makes sense, you're done — the Portal is wired up end to end.
## 5. Pick the model you actually want[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#5-pick-the-model-you-actually-want "Direct link to 5. Pick the model you actually want")
`hermes setup --portal` lets you pick a model during setup, but the whole point of the subscription is access to the full catalog — switch any time with `/model` mid-session:

```


/model anthropic/claude-sonnet-4.6     # best general-purpose agentic  





/model openai/gpt-5.4                  # strong reasoning + tool calling  





/model google/gemini-2.5-pro           # huge context window  





/model deepseek/deepseek-v3.2          # cost-effective coder  





/model anthropic/claude-opus-4.6       # heavyweight for hard problems  



```

Or pop the picker to browse:

```


/model  



```

Pick a different default permanently:

```


# in your terminal, outside any session  





hermes config set model.default anthropic/claude-sonnet-4.6  



```

### Don't pick Hermes-4 for agent work[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#dont-pick-hermes-4-for-agent-work "Direct link to Don't pick Hermes-4 for agent work")
Hermes-4-70B and Hermes-4-405B are available on the Portal at deep discounts, but they're **chat/reasoning models** , not tool-call-tuned. They will struggle with multi-step agent loops. Use them for conversation/research work through the [subscription proxy](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy) from non-agent tools. For Hermes Agent itself, stick to the frontier agentic models above.
The Portal's own [info page](https://portal.nousresearch.com/info) carries this warning too — it's the official Nous guidance, not just a Hermes-side opinion.
## 6. (Optional) Customize Tool Gateway routing[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#6-optional-customize-tool-gateway-routing "Direct link to 6. \(Optional\) Customize Tool Gateway routing")
The gateway is opt-in per tool, not all-or-nothing. If you already have a Browserbase account and want to keep using it while routing web search and image generation through Nous, that's supported:

```


hermes tools  





# → Web search       → "Nous Subscription"     (recommended)  





# → Image generation → "Nous Subscription"     (recommended)  





# → Browser          → "Browserbase"           (your existing key)  





# → TTS              → "Nous Subscription"     (recommended)  



```

These rows appear in `hermes tools` even before you've logged into Nous Portal — if you pick "Nous Subscription" without an active session, Hermes runs the Portal login inline (without changing your inference provider or your other tools).
Verify your mix with:

```


hermes portal tools  



```

You'll see per-tool routing — `via Nous Portal` for the ones routed through the subscription, and the partner name (`browserbase`, `firecrawl`, etc.) for the ones using your own keys.
## 7. (Optional) Enable voice mode[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#7-optional-enable-voice-mode "Direct link to 7. \(Optional\) Enable voice mode")
Because the Tool Gateway includes OpenAI TTS, [voice mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) works without a separate OpenAI key:

```


hermes setup tts  





# → pick "Nous Subscription" for TTS  





# → pick a speech-to-text backend (local faster-whisper is free, no setup)  



```

Then in any messaging-platform session (Telegram, Discord, Signal, etc.), send a voice message and Hermes will transcribe it, respond, and reply with synthesized voice — all on your Portal subscription.
## 8. (Optional) Cron + always-on workflows[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#8-optional-cron--always-on-workflows "Direct link to 8. \(Optional\) Cron + always-on workflows")
The Portal subscription works for [cron jobs](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) and [batch processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing) the same way it works for interactive chat — the OAuth refresh token is reused automatically. No additional setup; just schedule cron jobs and they'll bill against your subscription.

```


hermes cron create "0 9 * * *" \  





  "Search the web for top AI news and summarize the 5 most important stories" \  





  --name "Daily AI news"  



```

The cron job runs unattended, calls the model + web search + summarization all through your Portal subscription.
## Profiles and multi-user setups[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#profiles-and-multi-user-setups "Direct link to Profiles and multi-user setups")
If you use [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) (e.g. a separate config per project), each profile is an independent credential island: a profile that has never signed in to the Portal fails closed instead of adopting another profile's session. Sign in once per profile with `hermes -p <name> portal` — when a shared Portal session already exists on the machine it offers to import it without a browser round-trip, and from then on the shared token store keeps that profile's token current. See [Profile setup](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal#profile-setup).
For team setups where multiple humans share a machine, each human has their own Portal account → each home directory holds its own `~/.hermes/auth.json` → no token sharing across users. This is the right boundary.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#troubleshooting "Direct link to Troubleshooting")
###  `hermes portal info` shows "not logged in" after `hermes setup --portal`[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#hermes-portal-info-shows-not-logged-in-after-hermes-setup---portal "Direct link to hermes-portal-info-shows-not-logged-in-after-hermes-setup---portal")
The OAuth flow didn't complete. Re-run it:

```


hermes portal  



```

If your browser doesn't open or the callback fails, you're likely on a remote/headless host — see [OAuth over SSH](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh) for the port-forwarding workarounds.
### "Model: currently openrouter" (or some other provider) instead of "using Nous as inference provider"[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#model-currently-openrouter-or-some-other-provider-instead-of-using-nous-as-inference-provider "Direct link to "Model: currently openrouter" \(or some other provider\) instead of "using Nous as inference provider"")
Your local config drifted. The OAuth worked but `model.provider` is still pointing at a different provider. Fix:

```


hermes config set model.provider nous  



```

Or interactively:

```


hermes model  





# pick Nous Portal  



```

Re-verify with `hermes portal info`.
### Tool Gateway tools showing partner names instead of "via Nous Portal"[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#tool-gateway-tools-showing-partner-names-instead-of-via-nous-portal "Direct link to Tool Gateway tools showing partner names instead of "via Nous Portal"")
Per-tool config is overriding the gateway. Run:

```


hermes tools  





# pick "Nous Subscription" for any tool you want gateway-routed  



```

Some users intentionally mix — e.g. routing web through Nous but using their own Browserbase key for browser. If that's intentional, leave it alone. If not, this command fixes it.
### "Re-authentication required" mid-session[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#re-authentication-required-mid-session "Direct link to "Re-authentication required" mid-session")
Your Portal refresh token was invalidated (password change, manual revoke, session expiry). The token is now quarantined locally so Hermes doesn't replay it endlessly. Just log in again:

```


hermes auth add nous  



```

The quarantine clears automatically on successful re-login.
### Model I want isn't in the `/model` picker[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#model-i-want-isnt-in-the-model-picker "Direct link to model-i-want-isnt-in-the-model-picker")
The Portal catalog draws on OpenRouter's model list (300+) plus models served through proprietary or secondary providers. If a model is missing, try typing the OpenRouter-style slug directly:

```


/model anthropic/claude-opus-4.6  





/model openai/o1-2025-12-17  



```

If a model is genuinely unavailable, [open an issue](https://github.com/NousResearch/hermes-agent/issues) — most gaps are routing config we can update.
### Billing not appearing on my Portal account[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#billing-not-appearing-on-my-portal-account "Direct link to Billing not appearing on my Portal account")
`hermes portal info` will tell you whether you're actually routing through the Portal or some other provider. Common causes:
  * `model.provider` set to `openrouter`/`anthropic`/etc. instead of `nous`
  * An OAuth refresh failure that fell back to a different configured provider
  * Multiple Hermes profiles where you're using the wrong one (check `hermes profile list`)


### Want to revoke and start clean[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#want-to-revoke-and-start-clean "Direct link to Want to revoke and start clean")

```


hermes auth logout nous       # wipes the local refresh token  





# Then re-run setup or remove the subscription from the Portal web UI  



```

## What this gets you, in plain numbers[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#what-this-gets-you-in-plain-numbers "Direct link to What this gets you, in plain numbers")  
| Without Portal  | With Portal  |  
| --- | --- |  
| 1× OpenRouter / Anthropic / OpenAI key in `.env`  | 1× OAuth refresh token, no `.env` keys  |  
| 1× web search key  | Web routed through gateway  |  
| 1× FAL key for image gen  | Image gen routed through gateway  |  
| 1× Browser Use / Browserbase key for browser  | Browser routed through gateway  |  
| 1× OpenAI key for TTS / voice mode  | TTS routed through gateway  |  
| 5 separate dashboards, top-ups, invoices  | 1 subscription, 1 invoice  |  
| Cross-machine: replicate all 5 keys  | Cross-machine: re-OAuth once  |  
That's the deal. If you're using more than two of those backends anyway, the subscription pays for itself.
## See also[​](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#see-also "Direct link to See also")
  * **[Nous Portal integration page](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)** — Overview of what's in the subscription
  * **[Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)** — Full details on every gateway-routed tool
  * **[Subscription proxy](https://hermes-agent.nousresearch.com/docs/user-guide/features/subscription-proxy)** — Use your Portal subscription from non-Hermes tools
  * **[Voice mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)** — Set up voice conversations on the Portal subscription
  * **[OAuth over SSH](https://hermes-agent.nousresearch.com/docs/guides/oauth-over-ssh)** — Remote / headless login patterns
  * **[Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)** — Share one Portal login across multiple Hermes configurations


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/run-hermes-with-nous-portal.md)
[Previous Run Nemotron 3 Ultra free in Hermes Agent](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)[Next Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#prerequisites)
  * [1. Get a subscription](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#1-get-a-subscription)
  * [2. Run the one-shot setup](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#2-run-the-one-shot-setup)
    * [What if I'm SSH'd into a server?](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#what-if-im-sshd-into-a-server)
  * [3. Verify it worked](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#3-verify-it-worked)
  * [4. Run your first conversation](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#4-run-your-first-conversation)
  * [5. Pick the model you actually want](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#5-pick-the-model-you-actually-want)
    * [Don't pick Hermes-4 for agent work](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#dont-pick-hermes-4-for-agent-work)
  * [6. (Optional) Customize Tool Gateway routing](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#6-optional-customize-tool-gateway-routing)
  * [7. (Optional) Enable voice mode](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#7-optional-enable-voice-mode)
  * [8. (Optional) Cron + always-on workflows](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#8-optional-cron--always-on-workflows)
  * [Profiles and multi-user setups](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#profiles-and-multi-user-setups)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#troubleshooting)
    * [`hermes portal info` shows "not logged in" after `hermes setup --portal`](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#hermes-portal-info-shows-not-logged-in-after-hermes-setup---portal)
    * ["Model: currently openrouter" (or some other provider) instead of "using Nous as inference provider"](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#model-currently-openrouter-or-some-other-provider-instead-of-using-nous-as-inference-provider)
    * [Tool Gateway tools showing partner names instead of "via Nous Portal"](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#tool-gateway-tools-showing-partner-names-instead-of-via-nous-portal)
    * ["Re-authentication required" mid-session](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#re-authentication-required-mid-session)
    * [Model I want isn't in the `/model` picker](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#model-i-want-isnt-in-the-model-picker)
    * [Billing not appearing on my Portal account](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#billing-not-appearing-on-my-portal-account)
    * [Want to revoke and start clean](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#want-to-revoke-and-start-clean)
  * [What this gets you, in plain numbers](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#what-this-gets-you-in-plain-numbers)
  * [See also](https://hermes-agent.nousresearch.com/docs/guides/run-hermes-with-nous-portal#see-also)


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
