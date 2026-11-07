---
title: "Terminal Environment Provider Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin
scraped_at: 2026-11-07T17:20:37.799515+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/terminal-environment-plugin)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
      * [Adding Tools](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
      * [Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)
      * [Adding a Platform Adapter](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-platform-adapters)
      * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
        * [Plugin LLM Access](https://hermes-agent.nousresearch.com/docs/developer-guide/plugin-llm-access)
        * [Observer Hooks](https://hermes-agent.nousresearch.com/docs/developer-guide/observer-hooks)
        * [Middleware](https://hermes-agent.nousresearch.com/docs/developer-guide/middleware)
        * [Subagent lifecycle API](https://hermes-agent.nousresearch.com/docs/developer-guide/subagent-lifecycle-api)
        * [Desktop Plugin SDK](https://hermes-agent.nousresearch.com/docs/developer-guide/desktop-plugin-sdk)
        * [Memory Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin)
        * [Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin)
        * [Secret Source Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/secret-source-plugin)
        * [Browser Vault Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-vault-plugin)
        * [Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)
        * [Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
        * [Video Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)
        * [Web Search Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/web-search-provider-plugin)
        * [Browser Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)
        * [Terminal Environment Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
        * [Delegation provider plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/delegation-provider-plugin)
        * [Application declarations](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/application-declarations)
        * [Catalog submission](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/catalog-submission)
        * [Public plugin API](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins/public-api)
      * [Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills)
      * [Extending the CLI](https://hermes-agent.nousresearch.com/docs/developer-guide/extending-the-cli)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Terminal Environment Provider Plugins


On this page
# Terminal Environment Provider Plugins
Hermes runs shell commands through a pluggable set of **terminal backends**. The built-in backends (local, Docker, Modal, Daytona, Vercel Sandbox, SSH) live in the core repo under `tools/environments/`. The official [Singularity/Apptainer plugin](https://github.com/NousResearch/hermes-official-plugins/tree/main/singularity) is a complete worked example of this page. Third-party sandbox vendors integrate as **plugins** instead — a standalone plugin repo installed under `~/.hermes/plugins/`, registering a backend the user selects exactly like a built-in one via `terminal.backend` in `config.yaml`.
This page mirrors the [Browser Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin) guide — same registration flow, same scope semantics.
## What a provider controls[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#what-a-provider-controls "Direct link to What a provider controls")
A registered backend automatically participates in every core surface:  
| Surface  | Driven by  |  
| --- | --- |  
| Command dispatch (`terminal`, `execute_code`, file tools)  | `create_environment()`  |  
|  `hermes setup` backend picker  |  `display_name`, `description`, `setup_instructions()`, `post_setup()`  |  
| Dashboard terminal-backend picker (probe status)  | `probe()`  |  
|  `hermes status` / `hermes doctor`  | `doctor_checks()`  |  
| System-prompt environment hints  |  `is_remote`, `env_description`  |  
| Dangerous-command approval skipping  | `skip_container_guards`  |  
| Container path/cwd handling  | `is_container`  |  
| Where commands start when `terminal.cwd` is unset or unusable  | `default_cwd`  |  
| Bot Desktop, `computer_use` and the browser following the terminal  |  `supports_streams` + the environment's `exec_prefix()`  |  
| Synced cache-file path translation  | `cache_path_base`  |  
| Secret stripping from spawned subprocesses  | `strip_env_keys`  |  
| Per-session sandbox isolation (`container_persistent: false`)  | `session_isolated_when_nonpersistent`  |  
Declaring these flags on the provider closes the classic "new backend missed classification site N" bug class — the core consults the registry at each site instead of a hardcoded list of names.
## Minimal provider[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#minimal-provider "Direct link to Minimal provider")
~/.hermes/plugins/acmebox/__init__.py

```


from agent.terminal_env_provider import TerminalEnvironmentProvider  





  





  





class AcmeBoxEnvironment:  





    """Must satisfy the BaseEnvironment duck-typed contract."""  





  





    def __init__(self, cwd, timeout, task_id):  





        self.cwd, self.timeout, self.task_id = cwd, timeout, task_id  





  





    def execute(self, command, timeout=None, **kwargs):  





        ...  # run the command in the sandbox  





        return {"output": "...", "exit_code": 0}  





  





    def cleanup(self):  





        ...  # tear down / detach  





  





  





class AcmeBoxProvider(TerminalEnvironmentProvider):  





    name = "acmebox"  





    display_name = "AcmeBox"  





    is_remote = True          # commands don't run on the host  





    is_container = True       # container-style path/cwd semantics  





  





    @property  





    def description(self):  





        return "Run commands in an AcmeBox cloud sandbox."  





  





    @property  





    def cache_path_base(self):  





        return "~/.hermes"    # where synced cache files land, or None  





  





    @property  





    def strip_env_keys(self):  





        return frozenset({"ACMEBOX_TOKEN"})  





  





    def is_available(self):  





        import importlib.util, os  





        return (  





            importlib.util.find_spec("acmebox") is not None  





            and bool(os.getenv("ACMEBOX_TOKEN"))  





        )  





  





    def create_environment(self, *, cwd, timeout, task_id="default",  





                           image=None, container_config=None, **kwargs):  





        return AcmeBoxEnvironment(cwd, timeout, task_id)  





  





  





def register(ctx):  





    ctx.register_terminal_environment_provider(AcmeBoxProvider())  



```

~/.hermes/plugins/acmebox/plugin.yaml

```


name: acmebox  





version: 0.1.0  





description: AcmeBox cloud sandbox terminal backend  





kind: backend  



```

Enable it, select it, run:

```


hermes plugins enable acmebox  





hermes config set terminal.backend acmebox  



```

## Rules[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#rules "Direct link to Rules")
  * **Reserved names.** Registrations that collide with a built-in backend name (`local`, `docker`, `modal`, `managed_modal`, `daytona`, `vercel_sandbox`, `ssh`) are rejected. Plugins extend the backend set; they never shadow in-tree backends.
  * **`create_environment`must accept`**kwargs`** and ignore unknown keys — the forward-compat contract that lets the factory signature evolve without breaking older plugins.
  * **`is_available()`/`probe()` must be cheap.** No network calls — they run during requirement checks and UI paints.
  * **Fail-soft everywhere.** A provider attribute that raises is treated as its default by the core (e.g. a raising `skip_container_guards` keeps the approval layer ON). Don't rely on exceptions for control flow.
  * **Secrets belong in`strip_env_keys`.** Your vendor token must never be readable by a model-authored shell command; listing it strips it from every spawned subprocess unconditionally, like the built-in `MODAL_*` / `DAYTONA_API_KEY` handling.


## Environment object contract[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#environment-object-contract "Direct link to Environment object contract")
`create_environment()` returns an object satisfying the same duck-typed interface as `tools.environments.base.BaseEnvironment`:
  * `execute(command, timeout=None, ...)` → `{"output": str, "exit_code": int}`
  * `cleanup()` — release resources; called on session teardown / idle reaping
  * Optional: persistence hooks mirroring the built-in cloud backends


Subclassing `BaseEnvironment` is recommended (you inherit the shared file-sync and background-process plumbing) but not required.
## File tools and the host filesystem[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#file-tools-and-the-host-filesystem "Direct link to File tools and the host filesystem")
`read_file`, `write_file`, `patch` and `search_files` go through your environment's `execute()`, so they see exactly the files your commands see. The one exception is an environment that declares `uses_host_filesystem = True` (only the built-in `LocalEnvironment` does): there the file tools read, write and search the host directly, run the bundled ripgrep, stat paths on the host, write oversized tool output straight to `~/.hermes/cache/spillover` and enable LSP diagnostics.
A backend that subclasses `LocalEnvironment` to confine its commands (a bubblewrap or other host sandbox that hides paths, mounts them read-only or gives commands their own `$TMPDIR`) inherits `True` and must turn it off, or the file tools bypass the sandbox:

```


from tools.environments.local import LocalEnvironment  





  





  





class AcmeJailEnvironment(LocalEnvironment):  





    uses_host_filesystem = False  # file tools run inside the jail, via execute()  



```

Leave it unset on backends that don't subclass `LocalEnvironment`; the default is `False`. Hermes v0.22.5 and earlier ignore the attribute and use the host fast path for every `LocalEnvironment` subclass, so pin `requires_hermes` past that.
## Images[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#images "Direct link to Images")
Your backend reads its own image setting (a `config_schema` key, or a `terminal.<name>_image` key you document). Hermes passes `image=` only for a per-task override: a batch run (`batch_runner.py`) giving each prompt its own container registers it as `<name>_image` for the active backend, and that value reaches `create_environment(image=...)`. Otherwise `image` is `""`; fall back to your setting.
## Starting directory[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#starting-directory "Direct link to Starting directory")
Without `default_cwd`, a plugin backend starts in `/root`, and a host-looking `terminal.cwd` is replaced by `/root` when `is_container` is set. Return an absolute in-sandbox path to start somewhere else:

```


    @property  





    def default_cwd(self):  





        return "/home/acme"  



```

When the home directory is only known once the sandbox is up, return `"~"` instead. Hermes then passes `cwd="~"` to `create_environment()` (it never expands it on the host), and your environment sets `self.cwd` to the absolute home it resolved:

```


class AcmeBoxEnvironment(BaseEnvironment):  





    def __init__(self, *, cwd, timeout, sandbox):  





        if cwd == "~":  





            cwd = sandbox.home()  # e.g. "/home/acme"  





        super().__init__(cwd=cwd, timeout=timeout)  



```

Hermes keeps `~` as the backend default, so every new sandbox resolves its own home, and records the path each environment resolved on that environment. Commands can also arrive with `cwd="~"`; `BaseEnvironment` already `cd`s there correctly. A `cd` anywhere under that home is kept for later commands and used as the base for relative paths in the file tools. Without this, a sandbox path like `/home/acme/project` would be discarded as if it were a host path.
`default_cwd` is read on every command, so keep it cheap (no network calls). Relative paths are ignored, because Hermes would anchor them on the host.
## Bot Desktop and `computer_use`[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#bot-desktop-and-computer_use "Direct link to bot-desktop-and-computer_use")
The screen, `computer_use` and the browser follow the terminal into Docker and SSH sandboxes (and the Singularity plugin's) by spawning long-lived processes there with stdin and stdout left open. A plugin backend can opt in the same way:
  1. Set `supports_streams = True` on the provider. `bot_desktop.placement: auto` then places the screen inside your backend instead of refusing.
  2. Give the environment an `exec_prefix(*, user=None, interactive=True)` method. It returns a local argv that runs whatever follows it inside the sandbox, with stdin and stdout open (the shape of `docker exec -i <container>`), or `None` when it can't right now. Hermes appends `bash -c <script>` as separate words, so the client must pass them through unchanged and the sandbox needs `bash`. `user` names the account to run as; ignore it if your backend can't switch users. Return a list, not a single command string.



```


class AcmeBoxEnvironment:  





    def exec_prefix(self, *, user=None, interactive=True):  





        return ["acmebox", "exec", "--stdin", self.sandbox_id, "--"]  



```

The sandbox image still needs the desktop stack (Xvnc, Xfce, Chromium, `cua-driver`); `nousresearch/hermes-sandbox:desktop` has it. Bot Desktop and the browser keep their scratch files under the environment's `get_temp_dir()`. An environment that doesn't subclass `BaseEnvironment` and has no such method gets the same default `BaseEnvironment` uses.
A terminal backend runs only in-process: its environment object is what the terminal tool, file tools, `exec_prefix()` and the `~` home resolution all drive. Under `plugins.isolation: host` the object cannot cross the host boundary, so creating the environment refuses with a message naming `plugins.isolation: in_process` (before the host starts a sandbox), and Bot Desktop refuses a `supports_streams` backend the same way.
## Session isolation semantics[​](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#session-isolation-semantics "Direct link to Session isolation semantics")
If your sandbox is **resumed by name** (a durable VM the backend re-attaches to), set `session_isolated_when_nonpersistent = True`. With `terminal.container_persistent: false`, each session then gets its own sandbox identity instead of sharing one — without this, two independent ephemeral runs could attach one live VM and delete it out from under each other.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/terminal-environment-plugin.md)
[Previous Browser Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-provider-plugin)[Next Delegation provider plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/delegation-provider-plugin)
  * [What a provider controls](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#what-a-provider-controls)
  * [Minimal provider](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#minimal-provider)
  * [Rules](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#rules)
  * [Environment object contract](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#environment-object-contract)
  * [File tools and the host filesystem](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#file-tools-and-the-host-filesystem)
  * [Images](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#images)
  * [Starting directory](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#starting-directory)
  * [Bot Desktop and `computer_use`](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#bot-desktop-and-computer_use)
  * [Session isolation semantics](https://hermes-agent.nousresearch.com/docs/developer-guide/terminal-environment-plugin#session-isolation-semantics)


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
