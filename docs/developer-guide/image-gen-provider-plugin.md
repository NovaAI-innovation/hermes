---
title: "Image Generation Provider Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin
scraped_at: 2026-11-07T17:20:29.109214+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/image-gen-provider-plugin)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Image Generation Provider Plugins


On this page
# Building an Image Generation Provider Plugin
Image-gen provider plugins register a backend that services every `image_generate` tool call — DALL·E, gpt-image, Grok, Flux, Imagen, Stable Diffusion, fal, Replicate, a local ComfyUI rig, anything. Built-in providers (OpenAI, OpenAI-Codex, xAI, FAL, Krea, DeepInfra, OpenRouter, Meta Model API) all ship as plugins. You can add a new one, or override a bundled one, by dropping a directory into `plugins/image_gen/<name>/`.
Image-gen is one of several **backend plugins** Hermes supports. The others (with more specialized ABCs) are [Memory Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin), [Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin), and [Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin). General tool/hook/CLI plugins live in [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins).
## How discovery works[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#how-discovery-works "Direct link to How discovery works")
Hermes scans for image-gen backends in three places:
  1. **Bundled** — `<repo>/plugins/image_gen/<name>/` (auto-loaded with `kind: backend`, always available)
  2. **User** — `~/.hermes/plugins/image_gen/<name>/` (opt-in via `plugins.enabled`)
  3. **Pip** — packages declaring a `hermes_agent.plugins` entry point


Each plugin's `register(ctx)` function calls `ctx.register_image_gen_provider(...)` — that puts it into the registry in `agent/image_gen_registry.py`. The active provider is picked by `image_gen.provider` in `config.yaml`; `hermes tools` walks users through selection.
The `image_generate` tool wrapper asks the registry for the active provider and dispatches there. If no provider is registered, the tool surfaces a helpful error pointing at `hermes tools`.
## Directory structure[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#directory-structure "Direct link to Directory structure")

```


plugins/image_gen/my-backend/  





├── __init__.py      # ImageGenProvider subclass + register()  





└── plugin.yaml      # Manifest with kind: backend  



```

A bundled plugin is complete at this point. User plugins at `~/.hermes/plugins/image_gen/<name>/` need to be added to `plugins.enabled` in `config.yaml` (or run `hermes plugins enable <name>`).
## The ImageGenProvider ABC[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#the-imagegenprovider-abc "Direct link to The ImageGenProvider ABC")
Subclass `agent.image_gen_provider.ImageGenProvider`. The only required members are the `name` property and the `generate()` method — everything else has sane defaults:

```


# plugins/image_gen/my-backend/__init__.py  





from typing import Any, Dict, List, Optional  





import os  





  





from agent.image_gen_provider import (  





    DEFAULT_ASPECT_RATIO,  





    ImageGenProvider,  





    error_response,  





    normalize_reference_images,  





    resolve_aspect_ratio,  





    save_b64_image,  





    success_response,  





)  





  





  





class MyBackendImageGenProvider(ImageGenProvider):  





    @property  





    def name(self) -> str:  





        # Stable id used in image_gen.provider config. Lowercase, no spaces.  





        return "my-backend"  





  





    @property  





    def display_name(self) -> str:  





        # Human label shown in `hermes tools`. Defaults to name.title() if omitted.  





        return "My Backend"  





  





    def is_available(self) -> bool:  





        # Return False if credentials or deps are missing.  





        # The tool's availability gate calls this before dispatch.  





        if not os.environ.get("MY_BACKEND_API_KEY"):  





            return False  





        try:  





            import my_backend_sdk  # noqa: F401  





        except ImportError:  





            return False  





        return True  





  





    def list_models(self) -> List[Dict[str, Any]]:  





        # Catalog shown in `hermes tools` model picker.  





        return [  





            {  





                "id": "my-model-fast",  





                "display": "My Model (Fast)",  





                "speed": "~5s",  





                "strengths": "Quick iteration",  





                "price": "$0.01/image",  





            },  





            {  





                "id": "my-model-hq",  





                "display": "My Model (HQ)",  





                "speed": "~30s",  





                "strengths": "Highest fidelity",  





                "price": "$0.04/image",  





            },  





        ]  





  





    def default_model(self) -> Optional[str]:  





        return "my-model-fast"  





  





    def get_setup_schema(self) -> Dict[str, Any]:  





        # Metadata for the `hermes tools` picker — keys to prompt for at setup.  





        return {  





            "name": "My Backend",  





            "badge": "paid",        # optional; shown as a short tag in the picker  





            "tag": "One-line description shown under the name",  





            "env_vars": [  





                {  





                    "key": "MY_BACKEND_API_KEY",  





                    "prompt": "My Backend API key",  





                    "url": "https://my-backend.example.com/api-keys",  





                },  





            ],  





        }  





  





    def capabilities(self) -> Dict[str, Any]:  





        # Declare whether this backend supports image-to-image / editing.  





        # The tool layer surfaces this in the dynamic schema so the model  





        # knows when `image_url` is honored. Default (if you omit this) is  





        # text-only: {"modalities": ["text"], "max_reference_images": 0}.  





        # Optional keys: "supports_upscale" (bool) adds an `upscale` param, and  





        # "creative_controls" lists the controls you honor from `creativity`,  





        # `intensity`, `complexity`, `movement`, `thinking`, `resolution`. Only declared controls appear  





        # in the schema and reach generate() as kwargs. "source_image_role": "style"  





        # tells the model that image inputs set the look and are not edited.  





        return {"modalities": ["text", "image"], "max_reference_images": 4}  





  





    def generate(  





        self,  





        prompt: str,  





        aspect_ratio: str = DEFAULT_ASPECT_RATIO,  





        *,  





        image_url: Optional[str] = None,  





        reference_image_urls: Optional[List[str]] = None,  





        **kwargs: Any,  





    ) -> Dict[str, Any]:  





        prompt = (prompt or "").strip()  





        aspect_ratio = resolve_aspect_ratio(aspect_ratio)  





  





        if not prompt:  





            return error_response(  





                error="Prompt is required",  





                error_type="invalid_input",  





                provider=self.name,  





                prompt="",  





                aspect_ratio=aspect_ratio,  





            )  





  





        # Routing: if image_url (or reference_image_urls) is set, the call is  





        # an image-to-image / edit request; otherwise text-to-image. Report  





        # which path you took via the `modality` field of success_response.  





        sources = []  





        if image_url:  





            sources.append(image_url)  





        sources.extend(normalize_reference_images(reference_image_urls) or [])  





        modality = "image" if sources else "text"  





  





        # Model selection precedence: env var → config → default. The helper  





        # _resolve_model() in the built-in openai plugin is a good reference.  





        model_id = kwargs.get("model") or self.default_model() or "my-model-fast"  





  





        try:  





            import my_backend_sdk  





            client = my_backend_sdk.Client(api_key=os.environ["MY_BACKEND_API_KEY"])  





            if modality == "image":  





                result = client.edit(  





                    prompt=prompt,  





                    model=model_id,  





                    image_urls=sources,  





                )  





            else:  





                result = client.generate(  





                    prompt=prompt,  





                    model=model_id,  





                    aspect_ratio=aspect_ratio,  





                )  





  





            # Two shapes supported:  





            #   - URL string: return it as `image`  





            #   - base64 data: save under $HERMES_HOME/cache/images/ via save_b64_image()  





            if result.get("image_b64"):  





                path = save_b64_image(  





                    result["image_b64"],  





                    prefix=self.name,  





                    extension="png",  





                )  





                image = str(path)  





            else:  





                image = result["image_url"]  





  





            return success_response(  





                image=image,  





                model=model_id,  





                prompt=prompt,  





                aspect_ratio=aspect_ratio,  





                provider=self.name,  





                modality=modality,  





            )  





        except Exception as exc:  





            return error_response(  





                error=str(exc),  





                error_type=type(exc).__name__,  





                provider=self.name,  





                model=model_id,  





                prompt=prompt,  





                aspect_ratio=aspect_ratio,  





            )  





  





  





def register(ctx) -> None:  





    """Plugin entry point — called once at load time."""  





    ctx.register_image_gen_provider(MyBackendImageGenProvider())  



```

## plugin.yaml[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#pluginyaml "Direct link to plugin.yaml")

```


name: my-backend  





version: 1.0.0  





description: My image backend — text-to-image via My Backend SDK  





author: Your Name  





kind: backend  





requires_env:  





  - MY_BACKEND_API_KEY  



```

`kind: backend` is what routes the plugin to the image-gen registration path. `requires_env` is prompted during `hermes plugins install`.
## ABC reference[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#abc-reference "Direct link to ABC reference")
Full contract in `agent/image_gen_provider.py`. The methods you'll typically override:  
| Member  | Required  | Default  | Purpose  |  
| --- | --- | --- | --- |  
| `name`  | ✅  | —  | Stable id used in `image_gen.provider` config  |  
| `display_name`  | —  | `name.title()`  | Label shown in `hermes tools`  |  
| `is_available()`  | —  | `True`  | Gate for missing creds/deps  |  
| `list_models()`  | —  | `[]`  | Catalog for `hermes tools` model picker  |  
| `default_model()`  | —  | first from `list_models()`  | Fallback when no model is configured  |  
| `get_setup_schema()`  | —  | minimal  | Picker metadata + env-var prompts  |  
| `generate(prompt, aspect_ratio, **kwargs)`  | ✅  | —  | The call  |  
## Response format[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#response-format "Direct link to Response format")
`generate()` must return a dict built via `success_response()` or `error_response()`. Both live in `agent/image_gen_provider.py`.
**Success:**

```


success_response(  





    image=<url-or-absolute-path>,  





    model=<model-id>,  





    prompt=<echoed-prompt>,  





    aspect_ratio="landscape" | "square" | "portrait",  





    provider=<your-provider-name>,  





    extra={...},  # optional backend-specific fields  





)  



```

**Error:**

```


error_response(  





    error="human-readable message",  





    error_type="provider_error" | "invalid_input" | "<exception class name>",  





    provider=<your-provider-name>,  





    model=<model-id>,  





    prompt=<prompt>,  





    aspect_ratio=<resolved aspect>,  





)  



```

The tool wrapper JSON-serializes the dict and hands it to the LLM. Errors are surfaced as the tool result; the LLM decides how to explain them to the user.
## Handling base64 vs URL output[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#handling-base64-vs-url-output "Direct link to Handling base64 vs URL output")
Some backends return image URLs (fal, Replicate); others return base64 payloads (OpenAI gpt-image-2). For the base64 case, use `save_b64_image()` — it writes to `$HERMES_HOME/cache/images/<prefix>_<timestamp>_<uuid>.<ext>` and returns the absolute `Path`. Pass that path (as `str`) as `image=` in `success_response()`. Gateway delivery (Telegram photo bubble, Discord attachment) recognizes both URLs and absolute paths.
## User overrides[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#user-overrides "Direct link to User overrides")
Drop a user plugin at `~/.hermes/plugins/image_gen/<name>/` with the same `name` property as a bundled one and enable it via `hermes plugins enable <name>` — the registry is last-writer-wins, so your version replaces the built-in. Useful for pointing an `openai` plugin at a private proxy, or swapping in a custom model catalog.
## Testing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#testing "Direct link to Testing")

```


export HERMES_HOME=$HOME/.hermes/cache/scratch/hermes-imggen-test  





mkdir -p $HERMES_HOME/plugins/image_gen/my-backend  





# …copy __init__.py + plugin.yaml into that dir…  





  





export MY_BACKEND_API_KEY=your-test-key  





hermes plugins enable my-backend  





  





# Pick it as the active provider  





echo "image_gen:" >> $HERMES_HOME/config.yaml  





echo "  provider: my-backend" >> $HERMES_HOME/config.yaml  





  





# Exercise it  





hermes -z "Generate an image of a corgi in a spacesuit"  



```

Or interactively: `hermes tools` → "Image Generation" → select `my-backend` → enter API key if prompted.
## Reference implementations[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#reference-implementations "Direct link to Reference implementations")
  * **`plugins/image_gen/openai/__init__.py`**— gpt-image-2 at low/medium/high tiers as three virtual model IDs sharing one API model with different`quality` params. Good example of tiered models under a single backend + config.yaml precedence chain.
  * **`plugins/image_gen/xai/__init__.py`**— Grok Imagine via xAI. Different shape (URL output, simpler catalog).
  * **`plugins/image_gen/openai-codex/__init__.py`**— same catalog as`openai` , but authenticated with the ChatGPT/Codex OAuth token and posted with plain `httpx` to the Codex backend's native `images/generations` / `images/edits` endpoints. Good example of a provider that fetches remote source images client-side and inlines them as data URLs, and that reports backend-returned metadata separately from the request.


## Distribute via pip[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#distribute-via-pip "Direct link to Distribute via pip")

```


# pyproject.toml  





[project.entry-points."hermes_agent.plugins"]  





my-backend-imggen = "my_backend_imggen_package"  



```

`my_backend_imggen_package` must expose a top-level `register` function. See [Distribute via pip](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins#distribute-via-pip) in the general plugin guide for the full setup.
## Related pages[​](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#related-pages "Direct link to Related pages")
  * [Image Generation](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation) — user-facing feature documentation
  * [Plugins overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) — all plugin types at a glance
  * [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins) — general tools/hooks/slash commands guide


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/image-gen-provider-plugin.md)
[Previous Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)[Next Video Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)
  * [How discovery works](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#how-discovery-works)
  * [Directory structure](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#directory-structure)
  * [The ImageGenProvider ABC](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#the-imagegenprovider-abc)
  * [plugin.yaml](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#pluginyaml)
  * [ABC reference](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#abc-reference)
  * [Response format](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#response-format)
  * [Handling base64 vs URL output](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#handling-base64-vs-url-output)
  * [User overrides](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#user-overrides)
  * [Testing](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#testing)
  * [Reference implementations](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#reference-implementations)
  * [Distribute via pip](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#distribute-via-pip)
  * [Related pages](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin#related-pages)


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
