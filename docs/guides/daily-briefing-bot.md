---
title: "Daily Briefing Bot"
source: https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot
scraped_at: 2026-11-07T17:20:04.520333+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/daily-briefing-bot)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Tutorial: Daily Briefing Bot


On this page
# Tutorial: Build a Daily Briefing Bot
In this tutorial, you'll build a personal briefing bot that wakes up every morning, researches topics you care about, summarizes the findings, and delivers a concise briefing straight to your Telegram or Discord.
By the end, you'll have a fully automated workflow combining **web search** , **cron scheduling** , **delegation** , and **messaging delivery** — no code required.
This recipe hits web search, summarization, and optional TTS — all bundled in a Portal subscription. The fastest setup is `hermes setup --portal`. See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).
## What We're Building[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#what-were-building "Direct link to What We're Building")
Here's the flow:
  1. **8:00 AM** — The cron scheduler triggers your job
  2. **Hermes spins up** a fresh agent session with your prompt
  3. **Web search** pulls the latest news on your topics
  4. **Summarization** distills it into a clean briefing format
  5. **Delivery** sends the briefing to your Telegram or Discord


The whole thing runs hands-free. You just read your briefing with your morning coffee.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#prerequisites "Direct link to Prerequisites")
Before starting, make sure you have:
  * **Hermes Agent installed** — see the [Installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
  * **Gateway running** — the gateway daemon handles cron execution:

```


hermes gateway install   # Install as a user service  





sudo hermes gateway install --system   # Linux servers: boot-time system service  





# or  





hermes gateway           # Run in foreground  



```

  * **Firecrawl API key** — set `FIRECRAWL_API_KEY` in your environment for web search
  * **Messaging configured** (optional but recommended) — [Telegram](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram) or Discord set up with a home channel


You can still follow this tutorial using `deliver: "local"`. Briefings will be saved to `~/.hermes/cron/output/` and you can read them anytime.
## Step 1: Test the Workflow Manually[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-1-test-the-workflow-manually "Direct link to Step 1: Test the Workflow Manually")
Before automating anything, let's make sure the briefing works. Start a chat session:

```


hermes  



```

Then enter this prompt:

```


Search for the latest news about AI agents and open source LLMs.  





Summarize the top 3 stories in a concise briefing format with links.  



```

Hermes will search the web, read through results, and produce something like:

```


☀️ Your AI Briefing — March 8, 2026  





  





1. Qwen 3 Released with 235B Parameters  





   Alibaba's latest open-weight model matches GPT-4.5 on several  





   benchmarks while remaining fully open source.  





   → https://qwenlm.github.io/blog/qwen3/  





  





2. LangChain Launches Agent Protocol Standard  





   A new open standard for agent-to-agent communication gains  





   adoption from 15 major frameworks in its first week.  





   → https://blog.langchain.dev/agent-protocol/  





  





3. EU AI Act Enforcement Begins for General-Purpose Models  





   The first compliance deadlines hit, with open source models  





   receiving exemptions under the 10M parameter threshold.  





   → https://artificialintelligenceact.eu/updates/  





  





---  





3 stories • Sources searched: 8 • Generated by Hermes Agent  



```

If this works, you're ready to automate it.
Try different prompts until you get output you love. Add instructions like "use emoji headers" or "keep each summary under 2 sentences." Whatever you settle on goes into the cron job.
## Step 2: Create the Cron Job[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-2-create-the-cron-job "Direct link to Step 2: Create the Cron Job")
Now let's schedule this to run automatically every morning. You can do this in two ways.
Before creating cron jobs, ensure Hermes has a default model and provider configured globally. If you want a specific job to use different values, set explicit per-job model/provider overrides when creating it.
### Option A: Natural Language (in chat)[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#option-a-natural-language-in-chat "Direct link to Option A: Natural Language \(in chat\)")
Just tell Hermes what you want:

```


Every morning at 8am, search the web for the latest news about AI agents  





and open source LLMs. Summarize the top 3 stories in a concise briefing  





with links. Use a friendly, professional tone. Deliver to telegram.  



```

Hermes will create the cron job for you using the unified `cronjob_manage` tool.
### Option B: CLI Slash Command[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#option-b-cli-slash-command "Direct link to Option B: CLI Slash Command")
Use the `/cron` command for more control:

```


/cron add "0 8 * * *" "Search the web for the latest news about AI agents and open source LLMs. Find at least 5 recent articles from the past 24 hours. Summarize the top 3 most important stories in a concise daily briefing format. For each story include: a clear headline, a 2-sentence summary, and the source URL. Use a friendly, professional tone. Format with emoji bullet points and end with a total story count."  



```

### The Golden Rule: Self-Contained Prompts[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#the-golden-rule-self-contained-prompts "Direct link to The Golden Rule: Self-Contained Prompts")
Cron jobs run in a **completely fresh session** — no memory of your previous conversations, no context about what you "set up earlier." Your prompt must contain **everything** the agent needs to do the job.
**Bad prompt:**

```


Do my usual morning briefing.  



```

**Good prompt:**

```


Search the web for the latest news about AI agents and open source LLMs.  





Find at least 5 recent articles from the past 24 hours. Summarize the  





top 3 most important stories in a concise daily briefing format. For each  





story include: a clear headline, a 2-sentence summary, and the source URL.  





Use a friendly, professional tone. Format with emoji bullet points.  



```

The good prompt is specific about **what to search** , **how many articles** , **what format** , and **what tone**. It's everything the agent needs in one shot.
## Step 3: Customize the Briefing[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-3-customize-the-briefing "Direct link to Step 3: Customize the Briefing")
Once the basic briefing works, you can get creative.
### Multi-Topic Briefings[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#multi-topic-briefings "Direct link to Multi-Topic Briefings")
Cover several areas in one briefing:

```


/cron add "0 8 * * *" "Create a morning briefing covering three topics. For each topic, search the web for recent news from the past 24 hours and summarize the top 2 stories with links.  





  





Topics:  





1. AI and machine learning — focus on open source models and agent frameworks  





2. Cryptocurrency — focus on Bitcoin, Ethereum, and regulatory news  





3. Space exploration — focus on SpaceX, NASA, and commercial space  





  





Format as a clean briefing with section headers and emoji. End with today's date and a motivational quote."  



```

### Using Delegation for Parallel Research[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#using-delegation-for-parallel-research "Direct link to Using Delegation for Parallel Research")
For faster briefings, tell Hermes to delegate each topic to a sub-agent:

```


/cron add "0 8 * * *" "Create a morning briefing by delegating research to sub-agents. Delegate three parallel tasks:  





  





1. Delegate: Search for the top 2 AI/ML news stories from the past 24 hours with links  





2. Delegate: Search for the top 2 cryptocurrency news stories from the past 24 hours with links  





3. Delegate: Search for the top 2 space exploration news stories from the past 24 hours with links  





  





Collect all results and combine them into a single clean briefing with section headers, emoji formatting, and source links. Add today's date as a header."  



```

Each sub-agent searches independently and in parallel, then the main agent combines everything into one polished briefing. See the [Delegation docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation) for more on how this works.
### Weekday-Only Schedule[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#weekday-only-schedule "Direct link to Weekday-Only Schedule")
Don't need briefings on weekends? Use a cron expression that targets Monday–Friday:

```


/cron add "0 8 * * 1-5" "Search for the latest AI and tech news..."  



```

### Twice-Daily Briefings[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#twice-daily-briefings "Direct link to Twice-Daily Briefings")
Get a morning overview and an evening recap:

```


/cron add "0 8 * * *" "Morning briefing: search for AI news from the past 12 hours..."  





/cron add "0 18 * * *" "Evening recap: search for AI news from the past 12 hours..."  



```

### Adding Personal Context with Memory[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#adding-personal-context-with-memory "Direct link to Adding Personal Context with Memory")
If you have [memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) enabled, you can store preferences that persist across sessions. But remember — cron jobs run in fresh sessions without conversational memory. To add personal context, bake it directly into the prompt:

```


/cron add "0 8 * * *" "You are creating a briefing for a senior ML engineer who cares about: PyTorch ecosystem, transformer architectures, open-weight models, and AI regulation in the EU. Skip stories about product launches or funding rounds unless they involve open source.  





  





Search for the latest news on these topics. Summarize the top 3 stories with links. Be concise and technical — this reader doesn't need basic explanations."  



```

Including details about who the briefing is _for_ dramatically improves relevance. Tell the agent your role, interests, and what to skip.
## Step 4: Manage Your Jobs[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-4-manage-your-jobs "Direct link to Step 4: Manage Your Jobs")
### List All Scheduled Jobs[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#list-all-scheduled-jobs "Direct link to List All Scheduled Jobs")
In chat:

```


/cron list  



```

Or from the terminal:

```


hermes cron list  



```

You'll see output like:

```


ID          | Name              | Schedule    | Next Run           | Deliver  





------------|-------------------|-------------|--------------------|--------  





a1b2c3d4    | Morning Briefing  | 0 8 * * *   | 2026-03-09 08:00   | telegram  





e5f6g7h8    | Evening Recap     | 0 18 * * *  | 2026-03-08 18:00   | telegram  



```

### Remove a Job[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#remove-a-job "Direct link to Remove a Job")
In chat:

```


/cron remove a1b2c3d4  



```

Or ask conversationally:

```


Remove my morning briefing cron job.  



```

Hermes will use `cronjob(action="list")` to find it and `cronjob(action="remove")` to delete it.
### Check Gateway Status[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#check-gateway-status "Direct link to Check Gateway Status")
Make sure the scheduler is actually running:

```


hermes cron status  



```

If the gateway isn't running, your jobs won't execute. Install it as a background service for reliability:

```


hermes gateway install  





# or on Linux servers  





sudo hermes gateway install --system  



```

## Going Further[​](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#going-further "Direct link to Going Further")
You've built a working daily briefing bot. Here are some directions to explore next:
  * **[Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)** — Full reference for schedule formats, repeat limits, and delivery options
  * **[Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)** — Deep dive into parallel sub-agent workflows
  * **[Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)** — Set up Telegram, Discord, or other delivery targets
  * **[Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)** — Persistent context across sessions
  * **[Tips& Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)** — More prompt engineering advice


The briefing bot pattern works for anything: competitor monitoring, GitHub repo summaries, weather forecasts, portfolio tracking, server health checks, or even a daily joke. If you can describe it in a prompt, you can schedule it.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/daily-briefing-bot.md)
[Previous Run Local LLMs on Mac](https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac)[Next Tutorial: Team Telegram Assistant](https://hermes-agent.nousresearch.com/docs/guides/team-telegram-assistant)
  * [What We're Building](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#what-were-building)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#prerequisites)
  * [Step 1: Test the Workflow Manually](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-1-test-the-workflow-manually)
  * [Step 2: Create the Cron Job](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-2-create-the-cron-job)
    * [Option A: Natural Language (in chat)](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#option-a-natural-language-in-chat)
    * [Option B: CLI Slash Command](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#option-b-cli-slash-command)
    * [The Golden Rule: Self-Contained Prompts](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#the-golden-rule-self-contained-prompts)
  * [Step 3: Customize the Briefing](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-3-customize-the-briefing)
    * [Multi-Topic Briefings](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#multi-topic-briefings)
    * [Using Delegation for Parallel Research](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#using-delegation-for-parallel-research)
    * [Weekday-Only Schedule](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#weekday-only-schedule)
    * [Twice-Daily Briefings](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#twice-daily-briefings)
    * [Adding Personal Context with Memory](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#adding-personal-context-with-memory)
  * [Step 4: Manage Your Jobs](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#step-4-manage-your-jobs)
    * [List All Scheduled Jobs](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#list-all-scheduled-jobs)
    * [Remove a Job](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#remove-a-job)
    * [Check Gateway Status](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#check-gateway-status)
  * [Going Further](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot#going-further)


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
