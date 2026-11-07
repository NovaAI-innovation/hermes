---
title: "Work with Skills"
source: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills
scraped_at: 2026-11-07T17:20:04.528713+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/work-with-skills)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Features](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)
  * [Reference](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Guides & Tutorials
  * Working with Skills


On this page
# Working with Skills
Skills are on-demand knowledge documents that teach Hermes how to handle specific tasks — from generating ASCII art to managing GitHub PRs. This guide walks you through using them day to day.
For the full technical reference, see [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).
* * *
## Finding Skills[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#finding-skills "Direct link to Finding Skills")
Every Hermes installation ships with bundled skills. See what's available:

```


# In any chat session:  





/skills  





  





# Or from the CLI:  





hermes skills list  



```

This shows a compact list with names and descriptions:

```


ascii-art         Generate ASCII art using pyfiglet, cowsay, boxes...  





arxiv             Search and retrieve academic papers from arXiv...  





github-pr-workflow Full PR lifecycle — create branches, commit...  





plan              Plan mode — inspect context, write a markdown...  





excalidraw        Create hand-drawn style diagrams using Excalidraw...  



```

### Searching for a Skill[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#searching-for-a-skill "Direct link to Searching for a Skill")

```


# Search by keyword  





/skills search docker  





/skills search music  



```

### The Skills Hub[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#the-skills-hub "Direct link to The Skills Hub")
Official optional skills (heavier or niche skills not active by default) are available via the Hub:

```


# Browse official optional skills  





/skills browse  





  





# Search the hub  





/skills search blockchain  



```

* * *
## Using a Skill[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#using-a-skill "Direct link to Using a Skill")
Every installed skill is automatically a slash command. Just type its name:

```


# Load a skill and give it a task  





/ascii-art Make a banner that says "HELLO WORLD"  





/plan Design a REST API for a todo app  





/github-pr-workflow Create a PR for the auth refactor  





  





# Just the skill name (no task) loads it and lets you describe what you need  





/excalidraw  



```

You can also trigger skills through natural conversation — ask Hermes to use a specific skill, and it will load it via the `skill_view` tool.
### Progressive Disclosure[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#progressive-disclosure "Direct link to Progressive Disclosure")
Skills use a token-efficient loading pattern. The agent doesn't load everything at once:
  1. **`skills_list()`**— compact list of all skills (~3k tokens). Loaded at session start.
  2. **`skill_view(name)`**— full SKILL.md content for one skill. Loaded when the agent decides it needs that skill.
  3. **`skill_view(name, file_path)`**— a specific reference file within the skill. Only loaded if needed.


This means skills don't cost tokens until they're actually used.
* * *
## Installing from the Hub[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#installing-from-the-hub "Direct link to Installing from the Hub")
Official optional skills ship with Hermes but aren't active by default. Install them explicitly:

```


# Install an official optional skill  





hermes skills install official/research/arxiv  





  





# Install from the hub in a chat session  





/skills install official/creative/songwriting-and-ai-music  





  





# Install SKILL.md and its referenced support files from an HTTP(S) URL  





hermes skills install https://sharethis.chat/SKILL.md  





/skills install https://example.com/SKILL.md --name my-skill  



```

What happens:
  1. The skill directory is copied to `~/.hermes/skills/`
  2. It appears in your `skills_list` output
  3. It becomes available as a slash command


Installed skills take effect in new sessions. If you want it available in the current session, use `/reset` to start fresh, or add `--now` to invalidate the prompt cache immediately (costs more tokens on the next turn).
### Verifying Installation[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#verifying-installation "Direct link to Verifying Installation")

```


# Check it's there  





hermes skills list | grep arxiv  





  





# Or in chat  





/skills search arxiv  



```

* * *
## Plugin-Provided Skills[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#plugin-provided-skills "Direct link to Plugin-Provided Skills")
Plugins can bundle their own skills using namespaced names (`plugin:skill`). This prevents name collisions with built-in skills.

```


# Load a plugin skill by its qualified name  





skill_view("superpowers:writing-plans")  





  





# Built-in skill with the same base name is unaffected  





skill_view("writing-plans")  



```

Plugin skills are **not** listed in the system prompt and don't appear in `skills_list`. They're opt-in — load them explicitly when you know a plugin provides one. When loaded, the agent sees a banner listing sibling skills from the same plugin.
For how to ship skills in your own plugin, see [Build a Hermes Plugin → Bundle skills](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#bundle-skills).
* * *
## Configuring Skill Settings[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#configuring-skill-settings "Direct link to Configuring Skill Settings")
Some skills declare configuration they need in their frontmatter:

```


metadata:  





  hermes:  





    config:  





      - key: tenor.api_key  





        description: "Tenor API key for GIF search"  





        prompt: "Enter your Tenor API key"  





        url: "https://developers.google.com/tenor/guides/quickstart"  



```

When a skill with config is first loaded, Hermes prompts you for the values. They're stored in `config.yaml` under `skills.config.*`.
Manage skill config from the CLI:

```


# Interactive config for a specific skill  





hermes skills config gif-search  





  





# View all skill config  





hermes config get skills.config --json  



```

* * *
## Creating Your Own Skill[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#creating-your-own-skill "Direct link to Creating Your Own Skill")
Skills are just markdown files with YAML frontmatter. Creating one takes under five minutes.
### 1. Create the Directory[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#1-create-the-directory "Direct link to 1. Create the Directory")

```


mkdir -p ~/.hermes/skills/my-category/my-skill  



```

### 2. Write SKILL.md[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#2-write-skillmd "Direct link to 2. Write SKILL.md")
~/.hermes/skills/my-category/my-skill/SKILL.md

```


---  





name: my-skill  





description: Brief description of what this skill does  





version: 1.0.0  





metadata:  





  hermes:  





    tags: [my-tag, automation]  





    category: my-category  





---  





  





# My Skill  





  





## When to Use  





Use this skill when the user asks about [specific topic] or needs to [specific task].  





  





## Procedure  





1. First, check if [prerequisite] is available  





2. Run `command --with-flags`  





3. Parse the output and present results  





  





## Pitfalls  





- Common failure: [description]. Fix: [solution]  





- Watch out for [edge case]  





  





## Verification  





Run `check-command` to confirm the result is correct.  



```

### 3. Add Reference Files (Optional)[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#3-add-reference-files-optional "Direct link to 3. Add Reference Files \(Optional\)")
Skills can include supporting files the agent loads on demand:

```


my-skill/  





├── SKILL.md                    # Main skill document  





├── references/  





│   ├── api-docs.md             # API reference the agent can consult  





│   └── examples.md             # Example inputs/outputs  





├── templates/  





│   └── config.yaml             # Template files the agent can use  





└── scripts/  





    └── setup.sh                # Scripts the agent can execute  



```

Reference these in your SKILL.md:

```


For API details, load the reference: `skill_view("my-skill", "references/api-docs.md")`  



```

### 4. Test It[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#4-test-it "Direct link to 4. Test It")
Start a new session and try your skill:

```


hermes chat -q "/my-skill help me with the thing"  



```

The skill appears automatically — no registration needed. Drop it in `~/.hermes/skills/` and it's live.
The agent can also create and update skills itself using `skill_manage`. After solving a complex problem, Hermes may offer to save the approach as a skill for next time.
* * *
## Per-Platform Skill Management[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#per-platform-skill-management "Direct link to Per-Platform Skill Management")
Control which skills are available on which platforms:

```


hermes skills  



```

This opens an interactive TUI where you can enable or disable skills per platform (CLI, Telegram, Discord, etc.). Useful when you want certain skills only available in specific contexts — for example, keeping development skills off Telegram.
* * *
## Skills vs Memory[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#skills-vs-memory "Direct link to Skills vs Memory")
Both are persistent across sessions, but they serve different purposes:  
|   | Skills  | Memory  |  
| --- | --- | --- |  
| **What**  | Procedural knowledge — how to do things  | Factual knowledge — what things are  |  
| **When**  | Loaded on demand, only when relevant  | Injected into every session automatically  |  
| **Size**  | Can be large (hundreds of lines)  | Should be compact (key facts only)  |  
| **Cost**  | Zero tokens until loaded  | Small but constant token cost  |  
| **Examples**  | "How to deploy to Kubernetes"  | "User prefers dark mode, lives in PST"  |  
| **Who creates**  | You, the agent, or installed from Hub  | The agent, based on conversations  |  
**Rule of thumb:** If you'd put it in a reference document, it's a skill. If you'd put it on a sticky note, it's memory.
* * *
## Tips[​](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#tips "Direct link to Tips")
**Keep skills focused.** A skill that tries to cover "all of DevOps" will be too long and too vague. A skill that covers "deploy a Python app to Fly.io" is specific enough to be genuinely useful.
**Let the agent create skills.** After a complex multi-step task, Hermes will often offer to save the approach as a skill. Say yes — these agent-authored skills capture the exact workflow including pitfalls that were discovered along the way.
**Use categories.** Organize skills into subdirectories (`~/.hermes/skills/devops/`, `~/.hermes/skills/research/`, etc.). This keeps the list manageable and helps the agent find relevant skills faster.
**Update skills when they go stale.** If you use a skill and hit issues not covered by it, tell Hermes to update the skill with what you learned. Skills that aren't maintained become liabilities.
* * *
_For the complete skills reference — frontmatter fields, conditional activation, external directories, and more — see[Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)._
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/work-with-skills.md)
[Previous Troubleshooting: "My Agent Feels Dumber"](https://hermes-agent.nousresearch.com/docs/guides/troubleshooting-agent-quality)[Next Delegation & Parallel Work](https://hermes-agent.nousresearch.com/docs/guides/delegation-patterns)
  * [Finding Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#finding-skills)
    * [Searching for a Skill](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#searching-for-a-skill)
    * [The Skills Hub](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#the-skills-hub)
  * [Using a Skill](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#using-a-skill)
    * [Progressive Disclosure](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#progressive-disclosure)
  * [Installing from the Hub](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#installing-from-the-hub)
    * [Verifying Installation](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#verifying-installation)
  * [Plugin-Provided Skills](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#plugin-provided-skills)
  * [Configuring Skill Settings](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#configuring-skill-settings)
  * [Creating Your Own Skill](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#creating-your-own-skill)
    * [1. Create the Directory](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#1-create-the-directory)
    * [2. Write SKILL.md](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#2-write-skillmd)
    * [3. Add Reference Files (Optional)](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#3-add-reference-files-optional)
    * [4. Test It](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#4-test-it)
  * [Per-Platform Skill Management](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#per-platform-skill-management)
  * [Skills vs Memory](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#skills-vs-memory)
  * [Tips](https://hermes-agent.nousresearch.com/docs/guides/work-with-skills#tips)


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
