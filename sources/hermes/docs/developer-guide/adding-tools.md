---
title: "Adding Tools"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools
scraped_at: 2026-11-07T17:20:20.142290+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
      * [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
      * [Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)
      * [Adding a Platform Adapter](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-platform-adapters)
      * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
      * [Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
      * [Extending the CLI](https://hermes-agent.nousresearch.com/docs/developer-guide/extending-the-cli)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * Adding Tools


On this page
# Adding Tools
Before writing a tool, ask yourself: **should this be a[skill](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills) instead?**
This page is for adding a **built-in Hermes tool** to the repository itself. If you want a personal, project-local, or otherwise custom tool without modifying Hermes core, use the plugin route instead:
  * [Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)
  * [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)


Default to plugins for most custom tool creation. Only follow this page when you explicitly want to ship a new built-in tool in `tools/` and `toolsets.py`.
Make it a **Skill** when the capability can be expressed as instructions + shell commands + existing tools (arXiv search, git workflows, Docker management, PDF processing).
Make it a **Tool** when it requires end-to-end integration with API keys, custom processing logic, binary data handling, or streaming (browser automation, TTS, vision analysis).
## Overview[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#overview "Direct link to Overview")
Adding a tool touches **2 files** :
  1. **`tools/your_tool.py`**— handler, schema, check function,`registry.register()` call
  2. **`toolsets.py`**— add tool name to`_HERMES_CORE_TOOLS` (or a specific toolset)


Any `tools/*.py` file with a top-level `registry.register()` call is auto-discovered at startup — no manual import list required.
## Step 1: Create the Built-in Tool File[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-1-create-the-built-in-tool-file "Direct link to Step 1: Create the Built-in Tool File")
Every tool file follows the same structure:

```


# tools/weather_tool.py  





"""Weather Tool -- look up current weather for a location."""  





  





import json  





import os  





import logging  





  





logger = logging.getLogger(__name__)  





  





  





# --- Availability check ---  





  





def check_weather_requirements() -> bool:  





    """Return True if the tool's dependencies are available."""  





    return bool(os.getenv("WEATHER_API_KEY"))  





  





  





# --- Handler ---  





  





def weather_tool(location: str, units: str = "metric") -> str:  





    """Fetch weather for a location. Returns JSON string."""  





    api_key = os.getenv("WEATHER_API_KEY")  





    if not api_key:  





        return json.dumps({"error": "WEATHER_API_KEY not configured"})  





    try:  





        # ... call weather API ...  





        return json.dumps({"location": location, "temp": 22, "units": units})  





    except Exception as e:  





        return json.dumps({"error": str(e)})  





  





  





# --- Schema ---  





  





WEATHER_SCHEMA = {  





    "name": "weather",  





    "description": "Get current weather for a location.",  





    "parameters": {  





        "type": "object",  





        "properties": {  





            "location": {  





                "type": "string",  





                "description": "City name or coordinates (e.g. 'London' or '51.5,-0.1')"  





            },  





            "units": {  





                "type": "string",  





                "enum": ["metric", "imperial"],  





                "description": "Temperature units (default: metric)",  





                "default": "metric"  





            }  





        },  





        "required": ["location"]  





    }  





}  





  





  





# --- Registration ---  





  





from tools.registry import registry  





  





registry.register(  





    name="weather",  





    toolset="weather",  





    schema=WEATHER_SCHEMA,  





    handler=lambda args, **kw: weather_tool(  





        location=args.get("location", ""),  





        units=args.get("units", "metric")),  





    check_fn=check_weather_requirements,  





    requires_env=["WEATHER_API_KEY"],  





)  



```

### Key Rules[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#key-rules "Direct link to Key Rules")
  * Handlers **MUST** return a JSON string (via `json.dumps()`), never raw dicts
  * Errors **MUST** be returned as `{"error": "message"}`, never raised as exceptions
  * The `check_fn` is called when building tool definitions — if it returns `False`, the tool is silently excluded
  * The `handler` receives `(args: dict, **kwargs)` where `args` is the LLM's tool call arguments


## Step 2: Add the Built-in Tool to a Toolset[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-2-add-the-built-in-tool-to-a-toolset "Direct link to Step 2: Add the Built-in Tool to a Toolset")
In `toolsets.py`, add the tool name:

```


# If it should be available on all platforms (CLI + messaging):  





_HERMES_CORE_TOOLS = [  





    ...  





    "weather",  # <-- add here  





]  





  





# Or create a new standalone toolset:  





"weather": {  





    "description": "Weather lookup tools",  





    "tools": ["weather"],  





    "includes": []  





},  



```

##  ~~Step 3: Add Discovery Import~~ (No longer needed)[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-3-add-discovery-import-no-longer-needed "Direct link to step-3-add-discovery-import-no-longer-needed")
Tool modules with a top-level `registry.register()` call are auto-discovered by `discover_builtin_tools()` in `tools/registry.py`. No manual import list to maintain — just create your file in `tools/` and it's picked up at startup.
## Async Handlers[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#async-handlers "Direct link to Async Handlers")
If your handler needs async code, mark it with `is_async=True`:

```


async def weather_tool_async(location: str) -> str:  





    async with aiohttp.ClientSession() as session:  





        ...  





    return json.dumps(result)  





  





registry.register(  





    name="weather",  





    toolset="weather",  





    schema=WEATHER_SCHEMA,  





    handler=lambda args, **kw: weather_tool_async(args.get("location", "")),  





    check_fn=check_weather_requirements,  





    is_async=True,  # registry calls _run_async() automatically  





)  



```

The registry handles async bridging transparently — you never call `asyncio.run()` yourself.
## Handlers That Need task_id[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#handlers-that-need-task_id "Direct link to Handlers That Need task_id")
Tools that manage per-session state receive `task_id` via `**kwargs`:

```


def _handle_weather(args, **kw):  





    task_id = kw.get("task_id")  





    return weather_tool(args.get("location", ""), task_id=task_id)  





  





registry.register(  





    name="weather",  





    ...  





    handler=_handle_weather,  





)  



```

## Agent-Loop Intercepted Tools[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#agent-loop-intercepted-tools "Direct link to Agent-Loop Intercepted Tools")
Some tools (`todo_list`, `memory`, `session_search`, `delegate_task`) need access to per-session agent state. These are intercepted by the agent loop (`agent/tool_executor.py`, called from `agent/conversation_loop.py`) before reaching the registry. The registry still holds their schemas, but `dispatch()` returns a fallback error if the intercept is bypassed.
## Optional: Setup Wizard Integration[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#optional-setup-wizard-integration "Direct link to Optional: Setup Wizard Integration")
If your tool requires an API key, add it to `hermes_cli/config.py`:

```


OPTIONAL_ENV_VARS = {  





    ...  





    "WEATHER_API_KEY": {  





        "description": "Weather API key for weather lookup",  





        "prompt": "Weather API key",  





        "url": "https://weatherapi.com/",  





        "tools": ["weather"],  





        "password": True,  





    },  





}  



```

## Checklist[​](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#checklist "Direct link to Checklist")
  * Tool file created with handler, schema, check function, and registration
  * Added to appropriate toolset in `toolsets.py`
  * Confirmed this really should be a built-in/core tool and not a plugin
  * Handler returns JSON strings, errors returned as `{"error": "..."}`
  * Optional: API key added to `OPTIONAL_ENV_VARS` in `hermes_cli/config.py`
  * Optional: Added to `toolset_distributions.py` for batch processing
  * Tested with `hermes chat -q "Use the weather tool for London"`


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/adding-tools.md)
[Previous Programmatic Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/programmatic-integration)[Next Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)
  * [Overview](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#overview)
  * [Step 1: Create the Built-in Tool File](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-1-create-the-built-in-tool-file)
    * [Key Rules](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#key-rules)
  * [Step 2: Add the Built-in Tool to a Toolset](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-2-add-the-built-in-tool-to-a-toolset)
  * [~~Step 3: Add Discovery Import~~ (No longer needed)](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#step-3-add-discovery-import-no-longer-needed)
  * [Async Handlers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#async-handlers)
  * [Handlers That Need task_id](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#handlers-that-need-task_id)
  * [Agent-Loop Intercepted Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#agent-loop-intercepted-tools)
  * [Optional: Setup Wizard Integration](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#optional-setup-wizard-integration)
  * [Checklist](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools#checklist)


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
