---
title: "Migrate from OpenClaw"
source: https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw
scraped_at: 2026-11-07T17:20:11.923738+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/migrate-from-openclaw)


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
  * Migrate from OpenClaw


On this page
# Migrate from OpenClaw
`hermes import-agent openclaw` imports your OpenClaw (or legacy Clawdbot/Moldbot) setup into Hermes. This guide covers exactly what gets migrated, the config key mappings, and what to verify after migration.
The command comes from the official **`agent-importers`plugin** in the [plugin catalog](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins), which also imports Claude Code, Codex CLI and Cursor setups ([Import from Other Agents](https://hermes-agent.nousresearch.com/docs/user-guide/import-from-other-agents)). The older spelling `hermes claw migrate` still works once the plugin is installed and runs the same import.
On a fresh install, run `hermes setup`. When it finds `~/.openclaw` it asks **"Import your setup from OpenClaw?"**. Say yes and setup installs the plugin and runs `hermes import-agent openclaw --migrate-secrets`, preview and confirmation included, then continues with the sections the import did not already fill in.
If your OpenClaw setup was multi-provider, `hermes setup --portal` collapses it to one OAuth — 300+ models plus the Tool Gateway in a single login. See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).
## Quick start[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#quick-start "Direct link to Quick start")

```


# Once per profile: the command comes from this plugin  





hermes plugins install agent-importers  





  





# Preview then migrate (always shows a preview first, then asks to confirm)  





hermes import-agent openclaw  





  





# Preview only, no changes  





hermes import-agent openclaw --dry-run  





  





# Full migration including API keys, skip confirmation  





hermes import-agent openclaw --preset full --migrate-secrets --yes  



```

The migration always shows a full preview of what will be imported before making any changes. Review the list, then confirm to proceed.
Reads from `~/.openclaw/` by default. Legacy `~/.clawdbot/` or `~/.moltbot/` directories are detected automatically. Same for legacy config filenames (`clawdbot.json`, `moltbot.json`).
## Options[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#options "Direct link to Options")  
| Option  | Description  |  
| --- | --- |  
| `--dry-run`  | Preview only — stop after showing what would be migrated.  |  
| `--preset <name>`  |  `full` (all compatible settings) or `user-data` (excludes infrastructure config). Neither preset imports secrets by default — pass `--migrate-secrets` explicitly.  |  
| `--overwrite`  | Overwrite existing Hermes files on conflicts (default: refuse to apply when the plan has conflicts).  |  
| `--migrate-secrets`  | Include API keys. Required even under `--preset full` — no preset imports secrets silently.  |  
| `--no-backup`  | Skip the pre-migration zip snapshot of `~/.hermes/` (by default a single restore-point archive is written before apply, under `~/.hermes/backups/pre-migration-*.zip`; restorable with `hermes import`).  |  
| `--source <path>`  | Custom OpenClaw directory.  |  
| `--workspace-target <path>`  | Where to place `AGENTS.md`.  |  
| `--skill-conflict <mode>`  |  `skip` (default), `overwrite`, or `rename`.  |  
| `--yes`  | Skip the confirmation prompt after preview.  |  
## What gets migrated[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#what-gets-migrated "Direct link to What gets migrated")
### Persona, memory, and instructions[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#persona-memory-and-instructions "Direct link to Persona, memory, and instructions")  
| What  | OpenClaw source  | Hermes destination  | Notes  |  
| --- | --- | --- | --- |  
| Persona  | `workspace/SOUL.md`  | `~/.hermes/SOUL.md`  | Direct copy  |  
| Workspace instructions  | `workspace/AGENTS.md`  |  `AGENTS.md` in `--workspace-target`  | Requires `--workspace-target` flag  |  
| Long-term memory  | `workspace/MEMORY.md`  | `~/.hermes/memories/MEMORY.md`  | Parsed into entries, merged with existing, deduped. Uses `§` delimiter.  |  
| User profile  | `workspace/USER.md`  | `~/.hermes/memories/USER.md`  | Same entry-merge logic as memory.  |  
| Daily memory files  | `workspace/memory/*.md`  | `~/.hermes/memories/MEMORY.md`  | All daily files merged into main memory.  |  
Workspace files are also checked at `workspace.default/` and `workspace-main/` as fallback paths (OpenClaw renamed `workspace/` to `workspace-main/` in recent versions, and uses `workspace-{agentId}` for multi-agent setups).
### Skills (4 sources)[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#skills-4-sources "Direct link to Skills \(4 sources\)")  
| Source  | OpenClaw location  | Hermes destination  |  
| --- | --- | --- |  
| Workspace skills  | `workspace/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Managed/shared skills  | `~/.openclaw/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Personal cross-project  | `~/.agents/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
| Project-level shared  | `workspace/.agents/skills/`  | `~/.hermes/skills/openclaw-imports/`  |  
Skill conflicts are handled by `--skill-conflict`: `skip` leaves the existing Hermes skill, `overwrite` replaces it, `rename` creates a `-imported` copy.
### Model and provider configuration[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#model-and-provider-configuration "Direct link to Model and provider configuration")  
| What  | OpenClaw config path  | Hermes destination  | Notes  |  
| --- | --- | --- | --- |  
| Default model  | `agents.defaults.model`  |  `config.yaml` → `model`  | Can be a string or `{primary, fallbacks}` object  |  
| Custom providers  | `models.providers.*`  |  `config.yaml` → `custom_providers` (auto-migrated to the canonical `providers:` dict on the next `hermes update` config migration)  | Maps `baseUrl`, `apiType`/`api` — handles both short ("openai", "anthropic") and hyphenated ("openai-completions", "anthropic-messages", "google-generative-ai") values  |  
| Provider API keys  | `models.providers.*.apiKey`  | `~/.hermes/.env`  | Requires `--migrate-secrets`. See [API key resolution](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#api-key-resolution) below.  |  
### Agent behavior[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#agent-behavior "Direct link to Agent behavior")  
| What  | OpenClaw config path  | Hermes config path  | Mapping  |  
| --- | --- | --- | --- |  
| Max turns  | `agents.defaults.timeoutSeconds`  | `agent.max_turns`  |  `timeoutSeconds / 10`, capped at 200  |  
| Verbose mode  | `agents.defaults.verboseDefault`  | `agent.verbose`  | "off" / "on" / "full"  |  
| Reasoning effort  | `agents.defaults.thinkingDefault`  | `agent.reasoning_effort`  | "always"/"high"/"xhigh" → "high", "auto"/"medium"/"adaptive" → "medium", "off"/"low"/"none"/"minimal" → "low"  |  
| Compression  | `agents.defaults.compaction.mode`  | `compression.enabled`  | "off" → false, anything else → true  |  
| Compression model  | `agents.defaults.compaction.model`  | `compression.summary_model`  | Direct string copy  |  
| Human delay  | `agents.defaults.humanDelay.mode`  | `human_delay.mode`  | "natural" / "custom" / "off"  |  
| Human delay timing  |  `agents.defaults.humanDelay.minMs` / `.maxMs`  |  `human_delay.min_ms` / `.max_ms`  | Direct copy  |  
| Timezone  | `agents.defaults.userTimezone`  | `timezone`  | Direct string copy  |  
| Exec timeout  | `tools.exec.timeoutSec`  | `terminal.timeout`  | Direct copy (field is `timeoutSec`, not `timeout`)  |  
| Docker sandbox  | `agents.defaults.sandbox.backend`  | `terminal.backend`  | "docker" → "docker"  |  
| Docker image  | `agents.defaults.sandbox.docker.image`  | `terminal.docker_image`  | Direct copy  |  
### Session lifetime[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#session-lifetime "Direct link to Session lifetime")
Idle and daily reset timers are not imported: Hermes conversations persist until an explicit `/new` or `/reset`. Advanced session settings (identity links, thread bindings, maintenance, scope and send policy) remain archived for reference.
### MCP servers[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#mcp-servers "Direct link to MCP servers")  
| OpenClaw field  | Hermes field  | Notes  |  
| --- | --- | --- |  
| `mcp.servers.*.command`  | `mcp_servers.*.command`  | Stdio transport  |  
| `mcp.servers.*.args`  | `mcp_servers.*.args`  |   |  
| `mcp.servers.*.env`  | `mcp_servers.*.env`  |   |  
| `mcp.servers.*.cwd`  | `mcp_servers.*.cwd`  |   |  
| `mcp.servers.*.url`  | `mcp_servers.*.url`  | HTTP/SSE transport  |  
| `mcp.servers.*.tools.include`  | `mcp_servers.*.tools.include`  | Tool filtering  |  
| `mcp.servers.*.tools.exclude`  | `mcp_servers.*.tools.exclude`  |   |  
### TTS (text-to-speech)[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#tts-text-to-speech "Direct link to TTS \(text-to-speech\)")
TTS settings are read from **two** OpenClaw config locations with this priority:
  1. `messages.tts.providers.{provider}.*` (canonical location)
  2. Top-level `talk.providers.{provider}.*` (fallback)
  3. Legacy flat keys `messages.tts.{provider}.*` (oldest format)

  
| What  | Hermes destination  |  
| --- | --- |  
| Provider name  |  `config.yaml` → `tts.provider`  |  
| ElevenLabs voice ID  |  `config.yaml` → `tts.elevenlabs.voice_id`  |  
| ElevenLabs model ID  |  `config.yaml` → `tts.elevenlabs.model_id`  |  
| OpenAI model  |  `config.yaml` → `tts.openai.model`  |  
| OpenAI voice  |  `config.yaml` → `tts.openai.voice`  |  
| Edge TTS voice  |  `config.yaml` → `tts.edge.voice` (OpenClaw renamed "edge" to "microsoft" — both are recognized)  |  
| TTS assets  |  `~/.hermes/tts/` (file copy)  |  
### Messaging platforms[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#messaging-platforms "Direct link to Messaging platforms")  
| Platform  | OpenClaw config path  | Hermes `.env` variable  | Notes  |  
| --- | --- | --- | --- |  
| Telegram  |  `channels.telegram.botToken` or `.accounts.default.botToken`  | `TELEGRAM_BOT_TOKEN`  | Token can be string or [SecretRef](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#secretref-handling). Both flat and accounts layout supported.  |  
| Telegram  | `credentials/telegram-default-allowFrom.json`  | `TELEGRAM_ALLOWED_USERS`  | Comma-joined from `allowFrom[]` array  |  
| Discord  |  `channels.discord.token` or `.accounts.default.token`  | `DISCORD_BOT_TOKEN`  |   |  
| Discord  |  `channels.discord.allowFrom` or `.accounts.default.allowFrom`  | `DISCORD_ALLOWED_USERS`  |   |  
| Slack  |  `channels.slack.botToken` or `.accounts.default.botToken`  | `SLACK_BOT_TOKEN`  |   |  
| Slack  |  `channels.slack.appToken` or `.accounts.default.appToken`  | `SLACK_APP_TOKEN`  |   |  
| Slack  |  `channels.slack.allowFrom` or `.accounts.default.allowFrom`  | `SLACK_ALLOWED_USERS`  |   |  
| WhatsApp  |  `channels.whatsapp.allowFrom` or `.accounts.default.allowFrom`  | `WHATSAPP_ALLOWED_USERS`  | Auth via Baileys QR pairing — requires re-pairing after migration  |  
| Signal  |  `channels.signal.account` or `.accounts.default.account`  | `SIGNAL_ACCOUNT`  |   |  
| Signal  |  `channels.signal.httpUrl` or `.accounts.default.httpUrl`  | `SIGNAL_HTTP_URL`  |   |  
| Signal  |  `channels.signal.allowFrom` or `.accounts.default.allowFrom`  | `SIGNAL_ALLOWED_USERS`  |   |  
| Matrix  |  `channels.matrix.accessToken` or `.accounts.default.accessToken`  | `MATRIX_ACCESS_TOKEN`  | Uses `accessToken` (not `botToken`)  |  
| Mattermost  |  `channels.mattermost.botToken` or `.accounts.default.botToken`  | `MATTERMOST_BOT_TOKEN`  |   |  
### Other config[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#other-config "Direct link to Other config")  
| What  | OpenClaw path  | Hermes path  | Notes  |  
| --- | --- | --- | --- |  
| Approval mode  | `approvals.exec.mode`  |  `config.yaml` → `approvals.mode`  | "auto"→"off", "always"→"manual", "smart"→"smart"  |  
| Command allowlist  | `exec-approvals.json`  |  `config.yaml` → `command_allowlist`  | Patterns merged and deduped  |  
| Browser CDP URL  | `browser.cdpUrl`  |  `config.yaml` → `browser.cdp_url`  |   |  
| Browser headless  | `browser.headless`  |  `config.yaml` → `browser.headless`  |   |  
| Brave search key  | `tools.web.search.brave.apiKey`  |  `.env` → `BRAVE_API_KEY`  | Requires `--migrate-secrets`  |  
| Gateway auth token  | `gateway.auth.token`  |  `.env` → `HERMES_GATEWAY_TOKEN`  | Requires `--migrate-secrets`  |  
| Working directory  | `agents.defaults.workspace`  |  `config.yaml` → `terminal.cwd`  | Legacy migrations may still emit `MESSAGING_CWD` as a compatibility fallback  |  
### Archived (no direct Hermes equivalent)[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#archived-no-direct-hermes-equivalent "Direct link to Archived \(no direct Hermes equivalent\)")
These are saved to `~/.hermes/migration/openclaw/<timestamp>/archive/` for manual review:  
| What  | Archive file  | How to recreate in Hermes  |  
| --- | --- | --- |  
| `IDENTITY.md`  | `archive/workspace/IDENTITY.md`  | Merge into `SOUL.md`  |  
| `TOOLS.md`  | `archive/workspace/TOOLS.md`  | Hermes has built-in tool instructions  |  
| `HEARTBEAT.md`  | `archive/workspace/HEARTBEAT.md`  | Use cron jobs for periodic tasks  |  
| `BOOTSTRAP.md`  | `archive/workspace/BOOTSTRAP.md`  | Use context files or skills  |  
| Cron jobs  | `archive/cron-config.json`  | Recreate with `hermes cron create`  |  
| Plugins  | `archive/plugins-config.json`  | See [plugins guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)  |  
| Hooks/webhooks  | `archive/hooks-config.json`  | Use `hermes webhook` or gateway hooks  |  
| Memory backend  | `archive/memory-backend-config.json`  | Configure via `hermes honcho`  |  
| Skills registry  | `archive/skills-registry-config.json`  | Use `hermes skills config`  |  
| UI/identity  | `archive/ui-identity-config.json`  | Use `/skin` command  |  
| Logging  | `archive/logging-diagnostics-config.json`  | Set in `config.yaml` logging section  |  
| Multi-agent list  | `archive/agents-list.json`  | Use Hermes profiles  |  
| Channel bindings  | `archive/bindings.json`  | Manual setup per platform  |  
| Complex channels  | `archive/channels-deep-config.json`  | Manual platform config  |  
## API key resolution[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#api-key-resolution "Direct link to API key resolution")
When `--migrate-secrets` is enabled, API keys are collected from **four sources** in priority order:
  1. **Config values** — `models.providers.*.apiKey` and TTS provider keys in `openclaw.json`
  2. **Environment file** — `~/.openclaw/.env` (keys like `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, etc.)
  3. **Config env sub-object** — `openclaw.json` → `"env"` or `"env"."vars"` (some setups store keys here instead of a separate `.env` file)
  4. **Auth profiles** — `~/.openclaw/agents/main/agent/auth-profiles.json` (per-agent credentials)


Config values take priority. Each subsequent source fills any remaining gaps.
### Supported key targets[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#supported-key-targets "Direct link to Supported key targets")
`OPENROUTER_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DEEPSEEK_API_KEY`, `GEMINI_API_KEY`, `ZAI_API_KEY`, `MINIMAX_API_KEY`, `ELEVENLABS_API_KEY`, `TELEGRAM_BOT_TOKEN`, `VOICE_TOOLS_OPENAI_KEY`
Keys not in this allowlist are never copied.
## SecretRef handling[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#secretref-handling "Direct link to SecretRef handling")
OpenClaw config values for tokens and API keys can be in three formats:

```


// Plain string  





"channels": { "telegram": { "botToken": "123456:ABC-DEF..." } }  





  





// Environment template  





"channels": { "telegram": { "botToken": "${TELEGRAM_BOT_TOKEN}" } }  





  





// SecretRef object  





"channels": { "telegram": { "botToken": { "source": "env", "id": "TELEGRAM_BOT_TOKEN" } } }  



```

The migration resolves all three formats. For env templates and SecretRef objects with `source: "env"`, it looks up the value in `~/.openclaw/.env` and the `openclaw.json` env sub-object. SecretRef objects with `source: "file"` or `source: "exec"` can't be resolved automatically — the migration warns about these, and those values must be added to Hermes manually via `hermes config set`.
## After migration[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#after-migration "Direct link to After migration")
  1. **Check the migration report** — printed on completion with counts of migrated, skipped, and conflicting items.
  2. **Review archived files** — anything in `~/.hermes/migration/openclaw/<timestamp>/archive/` needs manual attention.
  3. **Start a new session** — imported skills and memory entries take effect in new sessions, not the current one.
  4. **Verify API keys** — run `hermes status` to check provider authentication.
  5. **Test messaging** — if you migrated platform tokens, restart the gateway: `systemctl --user restart hermes-gateway`
  6. **Check session archives** — review archived advanced settings; idle and daily reset timers are intentionally not imported.
  7. **Re-pair WhatsApp** — WhatsApp uses QR code pairing (Baileys), not token migration. Run `hermes whatsapp` to pair.
  8. **Archive cleanup** — after confirming everything works, run `hermes claw cleanup` to rename leftover OpenClaw directories to `.pre-migration/` (prevents state confusion).


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#troubleshooting "Direct link to Troubleshooting")
### "OpenClaw directory not found"[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#openclaw-directory-not-found "Direct link to "OpenClaw directory not found"")
The migration checks `~/.openclaw/`, then `~/.clawdbot/`, then `~/.moltbot/`. If your installation is elsewhere, use `--source /path/to/your/openclaw`.
### "No provider API keys found"[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#no-provider-api-keys-found "Direct link to "No provider API keys found"")
Keys might be stored in several places depending on your OpenClaw version: inline in `openclaw.json` under `models.providers.*.apiKey`, in `~/.openclaw/.env`, in the `openclaw.json` `"env"` sub-object, or in `agents/main/agent/auth-profiles.json`. The migration checks all four. If keys use `source: "file"` or `source: "exec"` SecretRefs, they can't be resolved automatically — add them via `hermes config set`.
### Skills not appearing after migration[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#skills-not-appearing-after-migration "Direct link to Skills not appearing after migration")
Imported skills land in `~/.hermes/skills/openclaw-imports/`. Start a new session for them to take effect, or run `/skills` to verify they're loaded.
### TTS voice not migrated[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#tts-voice-not-migrated "Direct link to TTS voice not migrated")
OpenClaw stores TTS settings in two places: `messages.tts.providers.*` and the top-level `talk` config. The migration checks both. If your voice ID was set via the OpenClaw UI (stored in a different path), you may need to set it manually: `hermes config set tts.elevenlabs.voice_id YOUR_VOICE_ID`.
## Upgrading from a version with `hermes claw` built in[​](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#upgrading-from-a-version-with-hermes-claw-built-in "Direct link to upgrading-from-a-version-with-hermes-claw-built-in")
OpenClaw migration used to ship inside Hermes core as `hermes claw migrate` and the optional `openclaw-migration` skill. Both moved into the `agent-importers` plugin, with the same flags and the same secrets rule (keys come over only with `--migrate-secrets`). Running `hermes claw` without the plugin prints the install command, and a fresh `hermes setup` that finds `~/.openclaw` offers to install it. The guided migration skill comes with the plugin as `agent-importers:openclaw-migration`. The old `official/migration/openclaw-migration` optional skill is gone. Nothing changes for an OpenClaw setup you have already migrated.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/migrate-from-openclaw.md)
[Previous GitHub PR Reviews via Webhook](https://hermes-agent.nousresearch.com/docs/guides/webhook-github-pr-review)[Next AWS Bedrock](https://hermes-agent.nousresearch.com/docs/guides/aws-bedrock)
  * [Quick start](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#quick-start)
  * [Options](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#options)
  * [What gets migrated](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#what-gets-migrated)
    * [Persona, memory, and instructions](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#persona-memory-and-instructions)
    * [Skills (4 sources)](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#skills-4-sources)
    * [Model and provider configuration](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#model-and-provider-configuration)
    * [Agent behavior](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#agent-behavior)
    * [Session lifetime](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#session-lifetime)
    * [MCP servers](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#mcp-servers)
    * [TTS (text-to-speech)](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#tts-text-to-speech)
    * [Messaging platforms](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#messaging-platforms)
    * [Other config](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#other-config)
    * [Archived (no direct Hermes equivalent)](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#archived-no-direct-hermes-equivalent)
  * [API key resolution](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#api-key-resolution)
    * [Supported key targets](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#supported-key-targets)
  * [SecretRef handling](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#secretref-handling)
  * [After migration](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#after-migration)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#troubleshooting)
    * ["OpenClaw directory not found"](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#openclaw-directory-not-found)
    * ["No provider API keys found"](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#no-provider-api-keys-found)
    * [Skills not appearing after migration](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#skills-not-appearing-after-migration)
    * [TTS voice not migrated](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#tts-voice-not-migrated)
  * [Upgrading from a version with `hermes claw` built in](https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw#upgrading-from-a-version-with-hermes-claw-built-in)


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
