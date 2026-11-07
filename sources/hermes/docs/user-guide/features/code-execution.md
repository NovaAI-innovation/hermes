---
title: "Code Execution"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution
scraped_at: 2026-11-07T17:19:48.642855+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/code-execution)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
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
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
    * [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Automation
  * Code Execution


On this page
# Code Execution (Programmatic Tool Calling)
The `execute_code` tool lets the agent write Python scripts that call Hermes tools programmatically, collapsing multi-step workflows into a single LLM turn. The script runs in a child process on the agent host, communicating with Hermes over a Unix domain socket RPC.
## How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#how-it-works "Direct link to How It Works")
  1. The agent writes a Python script using `from hermes_tools import ...`
  2. Hermes generates a `hermes_tools.py` stub module with RPC functions
  3. Hermes opens a Unix domain socket and starts an RPC listener thread
  4. The script runs in a child process — tool calls travel over the socket back to Hermes
  5. Only the script's `print()` output is returned to the LLM; intermediate tool results never enter the context window



```


# The agent can write scripts like:  





from hermes_tools import web_search, web_extract  





  





results = web_search("Python 3.13 features", limit=5)  





for r in results["data"]["web"]:  





    content = web_extract([r["url"]])  





    # ... filter and process ...  





print(summary)  



```

**Available tools inside scripts:** `web_search`, `web_extract`, `read_file`, `write_file`, `search_files`, `patch`, `terminal` (foreground only).
## When the Agent Uses This[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#when-the-agent-uses-this "Direct link to When the Agent Uses This")
The agent uses `execute_code` when there are:
  * **3+ tool calls** with processing logic between them
  * Bulk data filtering or conditional branching
  * Loops over results


The key benefit: intermediate tool results never enter the context window — only the final `print()` output comes back, dramatically reducing token usage.
## Practical Examples[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#practical-examples "Direct link to Practical Examples")
### Data Processing Pipeline[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#data-processing-pipeline "Direct link to Data Processing Pipeline")

```


from hermes_tools import search_files, read_file  





import json  





  





# Find all config files and extract database settings  





matches = search_files("database", path=".", file_glob="*.yaml", limit=20)  





configs = []  





for match in matches.get("matches", []):  





    content = read_file(match["path"])  





    configs.append({"file": match["path"], "preview": content["content"][:200]})  





  





print(json.dumps(configs, indent=2))  



```

### Multi-Step Web Research[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#multi-step-web-research "Direct link to Multi-Step Web Research")

```


from hermes_tools import web_search, web_extract  





import json  





  





# Search, extract, and summarize in one turn  





results = web_search("Rust async runtime comparison 2025", limit=5)  





summaries = []  





for r in results["data"]["web"]:  





    page = web_extract([r["url"]])  





    for p in page.get("results", []):  





        if p.get("content"):  





            summaries.append({  





                "title": r["title"],  





                "url": r["url"],  





                "excerpt": p["content"][:500]  





            })  





  





print(json.dumps(summaries, indent=2))  



```

### Bulk File Refactoring[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#bulk-file-refactoring "Direct link to Bulk File Refactoring")

```


from hermes_tools import search_files, read_file, patch  





  





# Find all Python files using deprecated API and fix them  





matches = search_files("old_api_call", path="src/", file_glob="*.py")  





fixed = 0  





for match in matches.get("matches", []):  





    result = patch(  





        path=match["path"],  





        old_string="old_api_call(",  





        new_string="new_api_call(",  





        replace_all=True  





    )  





    if "error" not in str(result):  





        fixed += 1  





  





print(f"Fixed {fixed} files out of {len(matches.get('matches', []))} matches")  



```

### Build and Test Pipeline[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#build-and-test-pipeline "Direct link to Build and Test Pipeline")

```


from hermes_tools import terminal, read_file  





import json  





  





# Run tests, parse results, and report  





result = terminal("cd /project && python -m pytest --tb=short -q 2>&1", timeout=120)  





output = result.get("output", "")  





  





# Parse test output  





passed = output.count(" passed")  





failed = output.count(" failed")  





errors = output.count(" error")  





  





report = {  





    "passed": passed,  





    "failed": failed,  





    "errors": errors,  





    "exit_code": result.get("exit_code", -1),  





    "summary": output[-500:] if len(output) > 500 else output  





}  





  





print(json.dumps(report, indent=2))  



```

## Execution Mode[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#execution-mode "Direct link to Execution Mode")
`execute_code` has two execution modes controlled by `code_execution.mode` in `~/.hermes/config.yaml`:  
| Mode  | Working directory  | Python interpreter  |  
| --- | --- | --- |  
|  **`project`**(default)  | The session's working directory (same as `terminal()`)  | Active `VIRTUAL_ENV` / `CONDA_PREFIX` python, falling back to Hermes's own python  |  
| `strict`  | A temp staging directory isolated from the user's project  |  `sys.executable` (Hermes's own python)  |  
**When to leave it on`project` :** you want `import pandas`, `from my_project import foo`, or relative paths like `open(".env")` to work the same way they do in `terminal()`. This is almost always what you want.
**When to flip to`strict` :** you need maximum reproducibility — you want the same interpreter every session regardless of which venv the user activated, and you want scripts quarantined from the project tree (no risk of accidentally reading project files through a relative path).

```


# ~/.hermes/config.yaml  





code_execution:  





  mode: project   # or "strict"  



```

Fallback behavior in `project` mode: if `VIRTUAL_ENV` / `CONDA_PREFIX` is unset, broken, or points at a Python older than 3.8, the resolver falls back cleanly to `sys.executable` — it never leaves the agent without a working interpreter.
Security-critical invariants are identical across both modes:
  * environment scrubbing (API keys, tokens, credentials stripped)
  * tool whitelist (scripts cannot call `execute_code` recursively, `delegate_task`, or MCP tools)
  * resource limits (timeout, stdout cap, tool-call cap)


Switching mode changes where scripts run and which interpreter runs them, not what credentials they can see or which tools they can call.
## Persistent session kernel[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#persistent-session-kernel "Direct link to Persistent session kernel")
Calls reuse a Python child for the same session, execution mode, interpreter, working directory, and tool set. Imports, variables, and loaded data can persist between cells. The child environment is fixed when the kernel starts.
Pass `reset: true` to discard that kernel state. A timeout or interrupted kernel can also lose it. Do not assume that a later terminal environment change is already visible inside an existing kernel. The old `code_execution.kernel_mode` setting is no longer a separate switch.
## Resource Limits[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#resource-limits "Direct link to Resource Limits")  
| Resource  | Limit  | Notes  |  
| --- | --- | --- |  
| **Timeout**  | 5 minutes (300s)  | Script is killed with SIGTERM, then SIGKILL after 5s grace  |  
| **Stdout**  | 50 KB  | Shown head-and-tail inline; the full output is saved to `~/.hermes/cache/exec/` and the path is included in the result  |  
| **Stderr**  | 10 KB  | Included in output on non-zero exit for debugging  |  
| **Tool calls**  | 50 per execution  | Error returned when limit reached  |  
All limits are configurable via `config.yaml`:

```


# In ~/.hermes/config.yaml  





code_execution:  





  mode: project      # project (default) | strict  





  timeout: 300       # Max seconds per script (default: 300)  





  max_tool_calls: 50 # Max tool calls per execution (default: 50)  



```

## State Between Calls (the session kernel)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#state-between-calls-the-session-kernel "Direct link to State Between Calls \(the session kernel\)")
On the local terminal backend, `execute_code` does not start a fresh interpreter for every call. Each session owns a persistent Python kernel, so variables, imports, and loaded data from one call are available in the next. The agent can load a dataset once and query it across several turns instead of re-reading it every time. Subagents get their own kernel; kernels are never shared across sessions. A subagent's kernel lives exactly as long as the subagent: it is exempt from the live-kernel cap while the subagent runs (a wide fan-out no longer evicts a sibling's kernel mid-task) and is disposed when the subagent finishes.
What ends a kernel:
  * **Timeout or interrupt.** A cell that hits the timeout (or is interrupted) kills the kernel process and its state is lost on purpose; the result says so and the next call starts a fresh kernel.
  * **`reset=true`.** The agent can pass `reset: true` to discard the kernel's state and start clean. This is also the way to pick up environment changes: a kernel's environment is frozen when it spawns, so a newly allowlisted passthrough variable is invisible until the kernel is reset.
  * **Idle timeout and eviction.** Kernels die with the session, after `code_execution.kernel_idle_timeout` idle seconds (default 1800), or when more than `code_execution.max_session_kernels` (default 4) top-level sessions' kernels are alive and the oldest is evicted (running subagents' kernels do not count against the cap).


The security envelope is the same as a one-shot script: environment scrubbing, the tool whitelist, and the per-call tool budget all apply to every cell, and tool-call authority (approvals, session, allow-list) is rebound on each cell.

```


# ~/.hermes/config.yaml  





code_execution:  





  kernel_idle_timeout: 1800   # seconds a kernel may sit idle before it is reaped  





  max_session_kernels: 4      # kernels kept alive at once; oldest is evicted past this  



```

**Remote backends** (Docker, SSH, Modal) run a remote session kernel with the same contract. If the kernel cannot be spawned on the backend, Hermes falls back to running each call as a standalone script and says so in the result.
**Large output.** Stdout over 50 KB is shown head-and-tail inline, and the full text is saved under `~/.hermes/cache/exec/` with the path included in the result, so the agent can page through it with `read_file` instead of re-running the script.
## How Tool Calls Work Inside Scripts[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#how-tool-calls-work-inside-scripts "Direct link to How Tool Calls Work Inside Scripts")
When your script calls a function like `web_search("query")`:
  1. The call is serialized to JSON and sent over a Unix domain socket to the parent process
  2. The parent dispatches through the standard `handle_function_call` handler
  3. The result is sent back over the socket
  4. The function returns the parsed result


This means tool calls inside scripts behave identically to normal tool calls — same rate limits, same error handling, same capabilities. The only restriction is that `terminal()` is foreground-only (no `background` or `pty` parameters).
## Error Handling[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#error-handling "Direct link to Error Handling")
When a script fails, the agent receives structured error information:
  * **Non-zero exit code** : stderr is included in the output so the agent sees the full traceback
  * **Timeout** : Script is killed and the agent sees `"Script timed out after 300s and was killed."`
  * **Interruption** : If the user sends a new message during execution, the script is terminated and the agent sees `[execution interrupted — user sent a new message]`
  * **Tool call limit** : When the 50-call limit is hit, subsequent tool calls return an error message


The response always includes `status` (success/error/timeout/interrupted), `output`, `tool_calls_made`, and `duration_seconds`.
## Security[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#security "Direct link to Security")
The child process runs with a **minimal environment**. API keys, tokens, and credentials are stripped by default. The script accesses tools exclusively via the RPC channel — it cannot read secrets from environment variables unless explicitly allowed.
Environment variables containing `KEY`, `TOKEN`, `SECRET`, `PASSWORD`, `CREDENTIAL`, `PASSWD`, or `AUTH` in their names are excluded. Only safe system variables (`PATH`, `HOME`, `LANG`, `SHELL`, `PYTHONPATH`, `VIRTUAL_ENV`, etc.) are passed through.
Approvals: gateway sessions approve a script as a whole before it runs. In a local CLI, TUI, Desktop or ACP session, a turn you typed gets no whole-script prompt: Python-level file and process operations in the script run unprompted and only its `terminal()` calls ask. Injected and automation turns keep the whole-script prompt. See [`execute_code` scripts](https://hermes-agent.nousresearch.com/docs/user-guide/security#execute-code-scripts).
### Skill Environment Variable Passthrough[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#skill-environment-variable-passthrough "Direct link to Skill Environment Variable Passthrough")
When a skill declares `required_environment_variables` in its frontmatter, those variables are **automatically passed through** to both `execute_code` and `terminal` child processes after the skill is loaded. This lets skills use their declared API keys without weakening the security posture for arbitrary code.
For non-skill use cases, you can explicitly allowlist variables in `config.yaml`:

```


terminal:  





  env_passthrough:  





    - MY_CUSTOM_KEY  





    - ANOTHER_TOKEN  



```

See the [Security guide](https://hermes-agent.nousresearch.com/docs/user-guide/security#environment-variable-passthrough) for full details.
###  `HERMES_*` variables in the child[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#hermes_-variables-in-the-child "Direct link to hermes_-variables-in-the-child")
The child process receives only a small, fixed set of operational `HERMES_*` variables by exact name:
  * `HERMES_HOME`
  * `HERMES_PROFILE`
  * `HERMES_CONFIG`
  * `HERMES_ENV`


(plus `HERMES_RPC_DIR` / `HERMES_RPC_SOCKET` / `TZ` / `HOME`, which Hermes injects explicitly so the RPC channel works).
Earlier versions passed **any** variable whose name began with `HERMES_` through to the child. That broad prefix was removed for security hardening: it could leak `HERMES_*`-named configuration that doesn't match a secret substring (for example `HERMES_BASE_URL`, `HERMES_KANBAN_DB`, or a `HERMES_*_WEBHOOK` endpoint) into arbitrary sandboxed code.
If an `execute_code` script — or a repo/plugin module it imports at import time — relied on a `HERMES_*` variable outside the four operational names above, it will now find that variable **unset** in the child. The drop is intentional, not a bug.
**Workaround — opt the variable back in explicitly.** Both routes pass the variable through `execute_code` _and_ `terminal` children, and neither weakens the secret-stripping guarantee (Hermes-managed provider credentials can never be re-allowed this way):
  1. **Per-machine, in`config.yaml`** — add the exact variable name to the passthrough allowlist:

```


terminal:  





  env_passthrough:  





    - HERMES_KANBAN_DB  





    - HERMES_BASE_URL  



```

  2. **Per-skill, in the skill's frontmatter** — declare it so it is registered automatically whenever that skill is loaded:

```


required_environment_variables:  





  - HERMES_KANBAN_DB  



```



**Diagnosing it.** When the child drops one or more non-allowlisted `HERMES_*` variables, Hermes emits a one-line `debug` log naming them and pointing at the `env_passthrough` escape hatch. Run with debug logging (`hermes logs --level DEBUG`, or check `~/.hermes/logs/agent.log`) and look for `execute_code: dropped N non-allowlisted HERMES_* var(s)` if a script behaves as though a `HERMES_*` variable is missing.
Hermes always writes the script and the auto-generated `hermes_tools.py` RPC stub into a temp staging directory that is cleaned up after execution. In `strict` mode the script also _runs_ there; in `project` mode it runs in the session's working directory (the staging directory stays on `PYTHONPATH` so imports still resolve). The child process runs in its own process group so it can be cleanly killed on timeout or interruption.
## execute_code vs terminal[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#execute_code-vs-terminal "Direct link to execute_code vs terminal")  
| Use Case  | execute_code  | terminal  |  
| --- | --- | --- |  
| Multi-step workflows with tool calls between  | ✅  | ❌  |  
| Simple shell command  | ❌  | ✅  |  
| Filtering/processing large tool outputs  | ✅  | ❌  |  
| Running a build or test suite  | ❌  | ✅  |  
| Looping over search results  | ✅  | ❌  |  
| Interactive/background processes  | ❌  | ✅  |  
| Needs API keys in environment  | ⚠️ Only via [passthrough](https://hermes-agent.nousresearch.com/docs/user-guide/security#environment-variable-passthrough)  | ✅ (most pass through)  |  
**Rule of thumb:** Use `execute_code` when you need to call Hermes tools programmatically with logic between calls. Use `terminal` for running shell commands, builds, and processes.
## Platform Support[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#platform-support "Direct link to Platform Support")
Code execution is available on **Linux, macOS, and Windows**. On Linux and macOS the RPC channel uses a Unix domain socket; on Windows, where `AF_UNIX` is unreliable, Hermes automatically falls back to a loopback TCP socket for the sandbox RPC transport. Remote terminal backends (Docker/SSH/Modal/etc.) use a file-based RPC transport instead and additionally require Python 3 inside the backend.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/code-execution.md)
[Previous Recurring Loops](https://hermes-agent.nousresearch.com/docs/user-guide/features/loops)[Next Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#how-it-works)
  * [When the Agent Uses This](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#when-the-agent-uses-this)
  * [Practical Examples](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#practical-examples)
    * [Data Processing Pipeline](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#data-processing-pipeline)
    * [Multi-Step Web Research](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#multi-step-web-research)
    * [Bulk File Refactoring](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#bulk-file-refactoring)
    * [Build and Test Pipeline](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#build-and-test-pipeline)
  * [Execution Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#execution-mode)
  * [Persistent session kernel](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#persistent-session-kernel)
  * [Resource Limits](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#resource-limits)
  * [State Between Calls (the session kernel)](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#state-between-calls-the-session-kernel)
  * [How Tool Calls Work Inside Scripts](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#how-tool-calls-work-inside-scripts)
  * [Error Handling](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#error-handling)
  * [Security](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#security)
    * [Skill Environment Variable Passthrough](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#skill-environment-variable-passthrough)
    * [`HERMES_*` variables in the child](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#hermes_-variables-in-the-child)
  * [execute_code vs terminal](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#execute_code-vs-terminal)
  * [Platform Support](https://hermes-agent.nousresearch.com/docs/user-guide/features/code-execution#platform-support)


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
