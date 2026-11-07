---
title: "Automate with Cron"
source: https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron
scraped_at: 2026-11-07T17:20:04.527703+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/automate-with-cron)


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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Automate Anything with Cron


On this page
# Automate Anything with Cron
The [daily briefing bot tutorial](https://hermes-agent.nousresearch.com/docs/guides/daily-briefing-bot) covers the basics. This guide goes further — five real-world automation patterns you can adapt for your own workflows.
For the full feature reference, see [Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron).
Cron jobs run in fresh agent sessions with no memory of your current chat. Prompts must be **completely self-contained** — include everything the agent needs to know.
  * **Recurring watchdog** where the script already produces the exact message (memory alerts, disk alerts, heartbeats): use [script-only cron jobs](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only). Same scheduler, no LLM. You can ask Hermes to set one up for you in chat — the `cronjob_manage` tool knows when to pick `no_agent=True` and writes the script for you.
  * **One-shot from a script that's already running** (CI step, post-commit hook, deploy script, externally-scheduled monitor): use [`hermes send`](https://hermes-agent.nousresearch.com/docs/guides/pipe-script-output) to pipe stdout or a file straight to Telegram / Discord / Slack / etc. without setting up a cron entry.


* * *
## Pattern 1: Website Change Monitor[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-1-website-change-monitor "Direct link to Pattern 1: Website Change Monitor")
Watch a URL for changes and get notified only when something is different.
The `script` parameter is the secret weapon here. A Python script runs before each execution, and its stdout becomes context for the agent. The script handles the mechanical work (fetching, diffing); the agent handles the reasoning (is this change interesting?).
Create the monitoring script:

```


mkdir -p ~/.hermes/scripts  



```

~/.hermes/scripts/watch-site.py

```


import hashlib, json, os, urllib.request  





  





URL = "https://example.com/pricing"  





STATE_FILE = os.path.expanduser("~/.hermes/scripts/.watch-site-state.json")  





  





# Fetch current content  





req = urllib.request.Request(URL, headers={"User-Agent": "Hermes-Monitor/1.0"})  





content = urllib.request.urlopen(req, timeout=30).read().decode()  





current_hash = hashlib.sha256(content.encode()).hexdigest()  





  





# Load previous state  





prev_hash = None  





if os.path.exists(STATE_FILE):  





    with open(STATE_FILE) as f:  





        prev_hash = json.load(f).get("hash")  





  





# Save current state  





with open(STATE_FILE, "w") as f:  





    json.dump({"hash": current_hash, "url": URL}, f)  





  





# Output for the agent  





if prev_hash and prev_hash != current_hash:  





    print(f"CHANGE DETECTED on {URL}")  





    print(f"Previous hash: {prev_hash}")  





    print(f"Current hash: {current_hash}")  





    print(f"\nCurrent content (first 2000 chars):\n{content[:2000]}")  





else:  





    print("NO_CHANGE")  



```

Set up the cron job:

```


/cron add "every 1h" "If the script output says CHANGE DETECTED, summarize what changed on the page and why it might matter. If it says NO_CHANGE, respond with just [SILENT]." --script ~/.hermes/scripts/watch-site.py --name "Pricing monitor" --deliver telegram  



```

For cron monitoring jobs, instruct the agent to respond with only `[SILENT]` when nothing changed. Cron delivery treats `[SILENT]` as the quiet marker, so you only get notified when something actually happens — no spam on quiet hours.
`[SILENT]` only applies to successful runs — when a job hard-fails, the engine posts a `⚠️ Cron 'X' failed…` notice to the job's delivery target. For jobs that deliver into busy shared channels, set `--failure-deliver local` to suppress those notices entirely (run state stays visible in `hermes cron list` and run history), or point failures at an ops channel with `--failure-deliver slack:C_OPS`. Same grammar as `--deliver`; omit it and failures follow `--deliver` as before.
* * *
## Pattern 2: Weekly Report[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-2-weekly-report "Direct link to Pattern 2: Weekly Report")
Compile information from multiple sources into a formatted summary. This runs once a week and delivers to your home channel.

```


/cron add "0 9 * * 1" "Generate a weekly report covering:  





  





1. Search the web for the top 5 AI news stories from the past week  





2. Search GitHub for trending repositories in the 'machine-learning' topic  





3. Check Hacker News for the most discussed AI/ML posts  





  





Format as a clean summary with sections for each source. Include links.  





Keep it under 500 words — highlight only what matters." --name "Weekly AI digest" --deliver telegram  



```

From the CLI:

```


hermes cron create "0 9 * * 1" \  





  "Generate a weekly report covering the top AI news, trending ML GitHub repos, and most-discussed HN posts. Format with sections, include links, keep under 500 words." \  





  --name "Weekly AI digest" \  





  --deliver telegram  



```

The `0 9 * * 1` is a standard cron expression: 9:00 AM every Monday.
* * *
## Pattern 3: GitHub Repository Watcher[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-3-github-repository-watcher "Direct link to Pattern 3: GitHub Repository Watcher")
Monitor a repository for new issues, PRs, or releases.

```


/cron add "every 6h" "Check the GitHub repository NousResearch/hermes-agent for:  





- New issues opened in the last 6 hours  





- New PRs opened or merged in the last 6 hours  





- Any new releases  





  





Use the terminal to run gh commands:  





  gh issue list --repo NousResearch/hermes-agent --state open --json number,title,author,createdAt --limit 10  





  gh pr list --repo NousResearch/hermes-agent --state all --json number,title,author,createdAt,mergedAt --limit 10  





  





Filter to only items from the last 6 hours. If nothing new, respond with [SILENT].  





Otherwise, provide a concise summary of the activity." --name "Repo watcher" --deliver discord  



```

Notice how the prompt includes the exact `gh` commands. The cron agent has no conversation history from previous runs — spell everything out. (Persistent memory does load, so durable preferences saved to MEMORY.md carry over, but don't rely on it for job-critical details.)
* * *
## Pattern 4: Data Collection Pipeline[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-4-data-collection-pipeline "Direct link to Pattern 4: Data Collection Pipeline")
Scrape data at regular intervals, save to files, and detect trends over time. This pattern combines a script (for collection) with the agent (for analysis).
~/.hermes/scripts/collect-prices.py

```


import json, os, urllib.request  





from datetime import datetime  





  





DATA_DIR = os.path.expanduser("~/.hermes/data/prices")  





os.makedirs(DATA_DIR, exist_ok=True)  





  





# Fetch current data (example: crypto prices)  





url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"  





data = json.loads(urllib.request.urlopen(url, timeout=30).read())  





  





# Append to history file  





entry = {"timestamp": datetime.now().isoformat(), "prices": data}  





history_file = os.path.join(DATA_DIR, "history.jsonl")  





with open(history_file, "a") as f:  





    f.write(json.dumps(entry) + "\n")  





  





# Load recent history for analysis  





lines = open(history_file).readlines()  





recent = [json.loads(l) for l in lines[-24:]]  # Last 24 data points  





  





# Output for the agent  





print(f"Current: BTC=${data['bitcoin']['usd']}, ETH=${data['ethereum']['usd']}")  





print(f"Data points collected: {len(lines)} total, showing last {len(recent)}")  





print(f"\nRecent history:")  





for r in recent[-6:]:  





    print(f"  {r['timestamp']}: BTC=${r['prices']['bitcoin']['usd']}, ETH=${r['prices']['ethereum']['usd']}")  



```


```


/cron add "every 1h" "Analyze the price data from the script output. Report:  





1. Current prices  





2. Trend direction over the last 6 data points (up/down/flat)  





3. Any notable movements (>5% change)  





  





If prices are flat and nothing notable, respond with [SILENT].  





If there's a significant move, explain what happened." \  





  --script ~/.hermes/scripts/collect-prices.py \  





  --name "Price tracker" \  





  --deliver telegram  



```

The script does the mechanical collection; the agent adds the reasoning layer.
* * *
## Pattern 5: Multi-Skill Workflow[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-5-multi-skill-workflow "Direct link to Pattern 5: Multi-Skill Workflow")
Chain skills together for complex scheduled tasks. Skills are loaded in order before the prompt executes.

```


# Use the arxiv skill to find papers, then the obsidian skill to save notes  





/cron add "0 8 * * *" "Search arXiv for the 3 most interesting papers on 'language model reasoning' from the past day. For each paper, create an Obsidian note with the title, authors, abstract summary, and key contribution." \  





  --skill arxiv \  





  --skill obsidian \  





  --name "Paper digest"  



```

From the tool directly:

```


cronjob(  





    action="create",  





    skills=["arxiv", "obsidian"],  





    prompt="Search arXiv for papers on 'language model reasoning' from the past day. Save the top 3 as Obsidian notes.",  





    schedule="0 8 * * *",  





    name="Paper digest",  





    deliver="local"  





)  



```

Skills are loaded in order — `arxiv` first (teaches the agent how to search papers), then `obsidian` (teaches how to write notes). The prompt ties them together.
* * *
## Managing Your Jobs[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#managing-your-jobs "Direct link to Managing Your Jobs")

```


# List all active jobs  





/cron list  





  





# Trigger a job immediately (for testing)  





/cron run <job_id>  





  





# Pause a job without deleting it  





/cron pause <job_id>  





  





# Edit a running job's schedule or prompt  





/cron edit <job_id> --schedule "every 4h"  





/cron edit <job_id> --prompt "Updated task description"  





  





# Add or remove skills from an existing job  





/cron edit <job_id> --skill arxiv --skill obsidian  





/cron edit <job_id> --clear-skills  





  





# Remove a job permanently  





/cron remove <job_id>  



```

* * *
## Delivery Targets[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#delivery-targets "Direct link to Delivery Targets")
The `--deliver` flag controls where results go:  
| Target  | Example  | Use case  |  
| --- | --- | --- |  
| `origin`  | `--deliver origin`  | Same chat that created the job (default)  |  
| `local`  | `--deliver local`  | Save to local file only  |  
| `telegram`  | `--deliver telegram`  | Your Telegram home channel  |  
| `discord`  | `--deliver discord`  | Your Discord home channel  |  
| `slack`  | `--deliver slack`  | Your Slack home channel  |  
| Specific chat  | `--deliver telegram:-1001234567890`  | A specific Telegram group  |  
| Threaded  | `--deliver telegram:-1001234567890:17585`  | A specific Telegram topic thread  |  
| Bot Chat  | `--deliver bot-chat`  | Inject output into this profile's canonical Bot Chat — the bot reads it and responds  |  
| Bot Chat (named)  | `--deliver bot-chat:research`  | Another local profile's Bot Chat  |  
### Bot Chat delivery[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#bot-chat-delivery "Direct link to Bot Chat delivery")
`bot-chat` targets deliver the job's output **into a profile's canonical "Bot Chat" session as a real message** — the bot receives it like any other message, acts on anything that needs action, and responds in that chat. This is the target to use when you want a bot to _see and react to_ scheduled output instead of just having it archived in Run history.
Things to know:
  * **Machine-local.** The profile must exist on the machine running the scheduler (`hermes profile list`). Names are validated at create time; profiles on other gateways/machines cannot be targeted.
  * **Costs a bot turn.** Each delivery runs a full agent turn in the target bot's Bot Chat — budget accordingly for high-frequency jobs.
  * **Combinable.** `--deliver bot-chat,telegram` posts to the bot AND your Telegram home channel. The `all` token never expands to bot-chat targets.
  * The delivered message is prefixed so the bot knows it came from a scheduled job, not from you.


* * *
## Tips[​](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#tips "Direct link to Tips")
**Make prompts self-contained.** The agent in a cron job has no memory of your conversations. Include URLs, repo names, format preferences, and delivery instructions directly in the prompt.
**Use`[SILENT]` deliberately.** For monitoring jobs, include instructions like "if nothing changed, respond with only `[SILENT]`." Do not ask the agent to explain the token in quiet cases — cron treats `[SILENT]` as the delivery-suppression marker.
**Use scripts for data collection.** The `script` parameter lets a Python script handle the boring parts (HTTP requests, file I/O, state tracking). The agent only sees the script's stdout and applies reasoning to it. This is cheaper and more reliable than having the agent do the fetching itself.
**Test with`/cron run`.** Before waiting for the schedule to trigger, use `/cron run <job_id>` to execute immediately and verify the output looks right.
**Schedule expressions.** Supported formats: relative delays (`30m`), intervals (`every 2h`), standard cron expressions (`0 9 * * *`), and ISO timestamps (`2025-06-15T09:00:00`). Natural language like `daily at 9am` is not supported — use `0 9 * * *` instead.
* * *
_For the complete cron reference — all parameters, edge cases, and internals — see[Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)._
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/automate-with-cron.md)
[Previous Use Voice Mode with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-voice-mode-with-hermes)[Next Script-Only Cron Jobs (No LLM)](https://hermes-agent.nousresearch.com/docs/guides/cron-script-only)
  * [Pattern 1: Website Change Monitor](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-1-website-change-monitor)
  * [Pattern 2: Weekly Report](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-2-weekly-report)
  * [Pattern 3: GitHub Repository Watcher](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-3-github-repository-watcher)
  * [Pattern 4: Data Collection Pipeline](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-4-data-collection-pipeline)
  * [Pattern 5: Multi-Skill Workflow](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#pattern-5-multi-skill-workflow)
  * [Managing Your Jobs](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#managing-your-jobs)
  * [Delivery Targets](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#delivery-targets)
    * [Bot Chat delivery](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#bot-chat-delivery)
  * [Tips](https://hermes-agent.nousresearch.com/docs/guides/automate-with-cron#tips)


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
