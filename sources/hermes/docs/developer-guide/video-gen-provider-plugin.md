---
title: "Video Generation Provider Plugins"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin
scraped_at: 2026-11-07T17:20:37.803040+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/video-gen-provider-plugin)


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
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-tools)
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
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/source-update-completion)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Extending
  * [Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
  * Video Generation Provider Plugins


On this page
# Building a Video Generation Provider Plugin
Video-gen provider plugins register a backend that services every `video_generate` tool call. Built-in providers (xAI, FAL, OpenRouter, DeepInfra) ship as plugins. Add a new one, or override a bundled one, by dropping a directory into `plugins/video_gen/<name>/`.
Video-gen mirrors [Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin) almost line-for-line — if you've built an image-gen backend, you already know the shape. The main differences: a `capabilities()` method advertising modalities/aspect-ratios/durations, and a routing convention (pass `image_url` to use image-to-video, omit it to use text-to-video — the provider picks the right endpoint internally).
## The unified surface (one tool, two modalities)[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-unified-surface-one-tool-two-modalities "Direct link to The unified surface \(one tool, two modalities\)")
The `video_generate` tool exposes two modalities through one parameter:
  * **Text-to-video** — call with `prompt` only. The provider routes to its text-to-video endpoint.
  * **Image-to-video** — call with `prompt` + `image_url`. The provider routes to its image-to-video endpoint.


Edit and extend are intentionally out of scope. Most backends don't support them and the inconsistency would force per-backend prose into the agent's tool description.
## How discovery works[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#how-discovery-works "Direct link to How discovery works")
Hermes scans for video-gen backends in three places:
  1. **Bundled** — `<repo>/plugins/video_gen/<name>/` (auto-loaded with `kind: backend`)
  2. **User** — `~/.hermes/plugins/video_gen/<name>/` (opt-in via `plugins.enabled`)
  3. **Pip** — packages declaring a `hermes_agent.plugins` entry point


Each plugin's `register(ctx)` function calls `ctx.register_video_gen_provider(...)`. The active provider is picked by `video_gen.provider` in `config.yaml`; `hermes tools` → Video Generation walks users through selection. Unlike `image_generate`, there is no in-tree legacy backend — every provider is a plugin.
## Directory structure[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#directory-structure "Direct link to Directory structure")

```


plugins/video_gen/my-backend/  





├── __init__.py      # VideoGenProvider subclass + register()  





└── plugin.yaml      # Manifest with kind: backend  



```

## The VideoGenProvider ABC[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-videogenprovider-abc "Direct link to The VideoGenProvider ABC")
Subclass `agent.video_gen_provider.VideoGenProvider`. Required: `name` property and `generate()` method.

```


# plugins/video_gen/my-backend/__init__.py  





from typing import Any, Dict, List, Optional  





import os  





  





from agent.video_gen_provider import (  





    VideoGenProvider,  





    error_response,  





    success_response,  





)  





  





  





class MyVideoGenProvider(VideoGenProvider):  





    @property  





    def name(self) -> str:  





        return "my-backend"  





  





    @property  





    def display_name(self) -> str:  





        return "My Backend"  





  





    def is_available(self) -> bool:  





        return bool(os.environ.get("MY_API_KEY"))  





  





    def list_models(self) -> List[Dict[str, Any]]:  





        # Each entry is a model FAMILY — a name the user picks once.  





        # Your provider's generate() routes within the family based on  





        # whether image_url was passed.  





        return [  





            {  





                "id": "fast",  





                "display": "Fast",  





                "speed": "~30s",  





                "strengths": "Cheapest tier",  





                "price": "$0.05/s",  





                "modalities": ["text", "image"],  # advisory  





            },  





        ]  





  





    def default_model(self) -> Optional[str]:  





        return "fast"  





  





    def capabilities(self) -> Dict[str, Any]:  





        return {  





            "modalities": ["text", "image"],  





            "aspect_ratios": ["16:9", "9:16"],  





            "resolutions": ["720p", "1080p"],  





            "min_duration": 1,  





            "max_duration": 10,  





            "supports_audio": False,  





            "supports_negative_prompt": True,  





            "max_reference_images": 0,  





        }  





  





    def get_setup_schema(self) -> Dict[str, Any]:  





        return {  





            "name": "My Backend",  





            "badge": "paid",  





            "tag": "Short description shown in `hermes tools`",  





            "env_vars": [  





                {  





                    "key": "MY_API_KEY",  





                    "prompt": "My Backend API key",  





                    "url": "https://mybackend.example.com/keys",  





                },  





            ],  





        }  





  





    def generate(  





        self,  





        prompt: str,  





        *,  





        model: Optional[str] = None,  





        image_url: Optional[str] = None,  





        reference_image_urls: Optional[List[str]] = None,  





        duration: Optional[int] = None,  





        aspect_ratio: str = "16:9",  





        resolution: str = "720p",  





        negative_prompt: Optional[str] = None,  





        audio: Optional[bool] = None,  





        seed: Optional[int] = None,  





        **kwargs: Any,  # always ignore unknown kwargs for forward-compat  





    ) -> Dict[str, Any]:  





        # ROUTE: image_url presence picks the endpoint.  





        if image_url:  





            endpoint = "my-backend/image-to-video"  





            modality_used = "image"  





        else:  





            endpoint = "my-backend/text-to-video"  





            modality_used = "text"  





  





        # ... call your API ...  





  





        return success_response(  





            video="https://your-cdn/output.mp4",  





            model=model or "fast",  





            prompt=prompt,  





            modality=modality_used,  





            aspect_ratio=aspect_ratio,  





            duration=duration or 5,  





            provider=self.name,  





        )  





  





  





def register(ctx) -> None:  





    ctx.register_video_gen_provider(MyVideoGenProvider())  



```

## The plugin manifest[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-plugin-manifest "Direct link to The plugin manifest")

```


# plugins/video_gen/my-backend/plugin.yaml  





name: my-backend  





version: 1.0.0  





description: "My video generation backend"  





author: Your Name  





kind: backend  





requires_env:  





  - MY_API_KEY  



```

## The `video_generate` schema[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-video_generate-schema "Direct link to the-video_generate-schema")
The tool exposes one schema across every backend. Providers ignore parameters they don't support.  
| Parameter  | What it does  |  
| --- | --- |  
| `prompt`  | Text instruction (required)  |  
| `image_url`  | When set → image-to-video; when omitted → text-to-video  |  
| `reference_image_urls`  | Style/character refs (provider-dependent)  |  
| `duration`  | Seconds — provider clamps  |  
| `aspect_ratio`  |  `"16:9"`, `"9:16"`, `"1:1"`, ... — provider clamps  |  
| `resolution`  |  `"480p"` / `"540p"` / `"720p"` / `"1080p"` — provider clamps  |  
| `negative_prompt`  | Content to avoid (Pixverse/Kling only)  |  
| `audio`  | Native audio (Veo3 / Pixverse pricing tier)  |  
| `seed`  | Reproducibility  |  
There is deliberately no `model` parameter: the backend and model are user configuration (`video_gen.provider` / `video_gen.model`), never an agent choice. Your `generate()` still receives `model=` — it is the configured model, resolved by the tool layer.
The provider's `capabilities()` advertises which of these are honored. The agent sees the active backend's capabilities in the tool description, dynamically rebuilt when the user changes backend via `hermes tools`.
## Model families and endpoint routing (the FAL pattern)[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#model-families-and-endpoint-routing-the-fal-pattern "Direct link to Model families and endpoint routing \(the FAL pattern\)")
When your backend has multiple endpoints per "model" — like FAL, where every family (Veo 3.1, Pixverse v6, Kling O3) has both a `/text-to-video` and an `/image-to-video` URL — represent each **family** as one catalog entry. Your `generate()` picks the right endpoint based on whether `image_url` was passed:

```


FAMILIES = {  





    "veo3.1": {  





        "text_endpoint": "fal-ai/veo3.1",  





        "image_endpoint": "fal-ai/veo3.1/image-to-video",  





        # ... family-specific capability flags ...  





    },  





}  





  





def generate(self, prompt, *, image_url=None, model=None, **kwargs):  





    family_id, family = _resolve_family(model)  





    endpoint = family["image_endpoint"] if image_url else family["text_endpoint"]  





    # ... build payload from family's declared capability flags, call endpoint ...  



```

The user picks `veo3.1` once in `hermes tools`. The agent never thinks about endpoints — it just passes (or doesn't pass) `image_url`.
## Selection precedence[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#selection-precedence "Direct link to Selection precedence")
For per-instance model knobs (see `plugins/video_gen/fal/__init__.py`):
  1. `<PROVIDER>_VIDEO_MODEL` env var
  2. `video_gen.<provider>.model` in `config.yaml`
  3. `video_gen.model` in `config.yaml` (when it's one of your IDs)
  4. Provider's `default_model()`


The `model=` keyword your `generate()` receives is the outcome of this resolution — a `model` in the agent's tool call is ignored, so the LLM cannot switch backends or billing tiers on its own.
## Response shape[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#response-shape "Direct link to Response shape")
`success_response()` and `error_response()` produce the dict shape every backend returns. Use them — don't hand-roll the dict.
Success keys: `success`, `video` (URL or absolute path), `model`, `prompt`, `modality` (`"text"` or `"image"`), `aspect_ratio`, `duration`, `provider`, plus `extra`.
Error keys: `success`, `video` (None), `error`, `error_type`, `model`, `prompt`, `aspect_ratio`, `provider`.
## Where to save artifacts[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#where-to-save-artifacts "Direct link to Where to save artifacts")
If your backend returns base64, use `save_b64_video()` to write under `$HERMES_HOME/cache/videos/`. For raw bytes from a follow-up HTTP fetch, use `save_bytes_video()`. Otherwise return the upstream URL directly — the gateway resolves remote URLs on delivery.
## Testing[​](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#testing "Direct link to Testing")
Drop a smoke test under `tests/plugins/video_gen/test_<name>_plugin.py`. The xAI and FAL tests show the pattern — register, verify catalog, exercise routing both with and without `image_url`, assert clean error responses on missing auth.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/video-gen-provider-plugin.md)
[Previous Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)[Next Web Search Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/web-search-provider-plugin)
  * [The unified surface (one tool, two modalities)](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-unified-surface-one-tool-two-modalities)
  * [How discovery works](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#how-discovery-works)
  * [Directory structure](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#directory-structure)
  * [The VideoGenProvider ABC](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-videogenprovider-abc)
  * [The plugin manifest](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-plugin-manifest)
  * [The `video_generate` schema](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#the-video_generate-schema)
  * [Model families and endpoint routing (the FAL pattern)](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#model-families-and-endpoint-routing-the-fal-pattern)
  * [Selection precedence](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#selection-precedence)
  * [Response shape](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#response-shape)
  * [Where to save artifacts](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#where-to-save-artifacts)
  * [Testing](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin#testing)


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
