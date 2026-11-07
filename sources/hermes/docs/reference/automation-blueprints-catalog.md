---
title: "Automation Blueprints Catalog"
source: https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog
scraped_at: 2026-11-07T17:20:37.817525+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [English](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/automation-blueprints-catalog)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Features](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
    * [Automation](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
      * [Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
      * [Automation Blueprints Catalog](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
      * [Subagent Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)
      * [Kanban (Multi-Agent Board)](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
      * [Codex App-Server Runtime](https://hermes-agent.nousresearch.com/docs/user-guide/features/codex-app-server-runtime)
      * [Kanban tutorial](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial)
      * [Kanban worker lanes](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-worker-lanes)
      * [Kanban Multi-Gateway Deployment](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-multi-gateway)
      * [Persistent Goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)
      * [Session Heartbeats](https://hermes-agent.nousresearch.com/docs/user-guide/features/heartbeat)
      * [Recurring Loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)
      * [Code Execution](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
      * [Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)
      * [Batch Processing](https://hermes-agent.nousresearch.com/docs/user-guide/features/batch-processing)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
    * [Management](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
    * [Skills](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Automation
  * Automation Blueprints Catalog


On this page
# Automation Blueprints
Automation Blueprints are ready-to-run automations. Pick one, fill in a couple of fields, and Hermes schedules it as a cron job — no cron syntax required.
Every blueprint works from **every surface** :
  * **Dashboard / desktop app** — open the Cron page, switch to the **Blueprints** tab, fill the form, and click _Schedule it_.
  * **CLI, TUI, and messengers** — type `/blueprint <name>` (e.g. `/blueprint morning-brief`) and Hermes asks you for what it needs, one question at a time, then schedules it. The name match is forgiving — a prefix or near-spelling resolves. Power users can skip the questions by passing values inline: `/blueprint morning-brief time=08:00`.
  * **Desktop app** — click **Send to App** on any blueprint and it opens with the command pre-loaded in your composer.


Blueprints never schedule anything silently — you always confirm before the job is created. Manage created jobs anytime with `/cron`.
Loading blueprints…
## Blueprints from plugins[​](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog#blueprints-from-plugins "Direct link to Blueprints from plugins")
Plugins can add their own blueprints. They show up in the same catalog as the built-ins: in `/blueprint`, the dashboard's Blueprints tab, and the desktop Cron page, labelled with the plugin's name. Their keys are prefixed with the plugin name (`/blueprint teamtools:standup`), so a plugin can never replace a built-in. Plugins load per profile, so a plugin blueprint is listed only in profiles where that plugin is enabled.
A job you create from a plugin blueprint is an ordinary cron job. Disabling the plugin removes the blueprint from the catalog, but jobs you already created keep running.
## Writing your own[​](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog#writing-your-own "Direct link to Writing your own")
A blueprint is just a skill with a `metadata.hermes.blueprint` block in its `SKILL.md` frontmatter. See [Creating Skills → Automation Blueprints](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills) for the slot schema and how to publish one. Plugin authors can register one directly with `ctx.register_automation_blueprint()`; see [Build a Plugin → Add Automation Blueprints](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#add-automation-blueprints).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/reference/automation-blueprints-catalog.mdx)
[Previous Scheduled Tasks (Cron)](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)[Next Subagent Delegation](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)
  * [Blueprints from plugins](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog#blueprints-from-plugins)
  * [Writing your own](https://hermes-agent.nousresearch.com/docs/reference/automation-blueprints-catalog#writing-your-own)


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
