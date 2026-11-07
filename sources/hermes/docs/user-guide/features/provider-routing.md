---
title: "Provider Routing"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing
scraped_at: 2026-11-07T17:20:04.513333+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
    * [Overview](https://hermes-agent.nousresearch.com/docs/integrations/)
    * [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)
    * [AI Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)
    * [Buzz Integration](https://hermes-agent.nousresearch.com/docs/integrations/buzz)
    * [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
    * [ACP Host Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
    * [Provider Routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
    * [Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)
    * [Credential Pools](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Integrations
  * Provider Routing


On this page
# Provider Routing
When using [OpenRouter](https://openrouter.ai) as your LLM provider, Hermes Agent supports **provider routing** — fine-grained control over which underlying AI providers handle your requests and how they're prioritized.
OpenRouter routes requests to many providers (e.g., Anthropic, Google, AWS Bedrock, Together AI). Provider routing lets you optimize for cost, speed, quality, or enforce specific provider requirements.
[Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal) decides routing centrally per model and does not accept caller-supplied provider preferences; Hermes never sends the `provider` object to Portal, so `provider_routing` is simply ignored there.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#configuration "Direct link to Configuration")
Add a `provider_routing` section to your `~/.hermes/config.yaml`:

```


provider_routing:  





  sort: "price"           # How to rank providers  





  only: []                # Whitelist: only use these providers  





  ignore: []              # Blacklist: never use these providers  





  order: []               # Explicit provider priority order  





  require_parameters: false  # Only use providers that support all parameters  





  data_collection: null   # Control data collection ("allow" or "deny")  



```

Provider routing only applies when using OpenRouter. It has no effect on Nous Portal or direct provider connections (e.g., connecting directly to the Anthropic API).
## Options[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#options "Direct link to Options")
###  `sort`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#sort "Direct link to sort")
Controls how OpenRouter ranks available providers for your request.  
| Value  | Description  |  
| --- | --- |  
| `"price"`  | Cheapest provider first  |  
| `"throughput"`  | Fastest tokens-per-second first  |  
| `"latency"`  | Lowest time-to-first-token first  |  

```


provider_routing:  





  sort: "price"  



```

###  `only`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#only "Direct link to only")
Whitelist of provider slugs. When set, **only** these providers will be used. All others are excluded. Use the lowercase slug shown by OpenRouter for each provider.

```


provider_routing:  





  only:  





    - "anthropic"  





    - "google"  



```

###  `ignore`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#ignore "Direct link to ignore")
Blacklist of provider names. These providers will **never** be used, even if they offer the cheapest or fastest option.

```


provider_routing:  





  ignore:  





    - "together"  





    - "deepinfra"  



```

###  `order`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#order "Direct link to order")
Explicit priority order. Providers listed first are preferred. Unlisted providers are used as fallbacks.

```


provider_routing:  





  order:  





    - "anthropic"  





    - "google"  





    - "amazon-bedrock"  



```

###  `require_parameters`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#require_parameters "Direct link to require_parameters")
When `true`, OpenRouter will only route to providers that support **all** parameters in your request (like `temperature`, `top_p`, `tools`, etc.). This avoids silent parameter drops.

```


provider_routing:  





  require_parameters: true  



```

###  `data_collection`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#data_collection "Direct link to data_collection")
Controls whether providers can use your prompts for training. Options are `"allow"` or `"deny"`.

```


provider_routing:  





  data_collection: "deny"  



```

### Per-model overrides (`models`)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#per-model-overrides-models "Direct link to per-model-overrides-models")
Pin a different provider set per model. Keys under `models` are model ids; each entry takes the same `sort` / `only` / `ignore` / `order` / `require_parameters` / `data_collection` keys and overrides the flat value for that model only. Anything you don't set per model falls through to the flat defaults.

```


provider_routing:  





  sort: "price"                      # applies to every model  





  models:  





    "openai/gpt-6-astra":  





      only: ["openai"]               # never let a reseller serve this one  





    "anthropic/claude-fable-5.1":  





      only: ["anthropic"]  





    "moonshotai/kimi-k2.6":  





      order: ["moonshotai", "together"]  





      sort: "throughput"  



```

Matching is spelling-tolerant like `agent.reasoning_overrides` (`claude-fable-5.1` / `claude-fable-5-1`, with or without the `openrouter/` prefix). The override follows the model the agent is _currently_ on, so `/model` switches, fallback activation, cron jobs, and delegated subagents on another model each get their own pins. Edit `config.yaml` directly for these keys: model ids contain dots, which `hermes config set` reads as path separators.
## Practical Examples[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#practical-examples "Direct link to Practical Examples")
### Optimize for Cost[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-cost "Direct link to Optimize for Cost")
Route to the cheapest available provider. Good for high-volume usage and development:

```


provider_routing:  





  sort: "price"  



```

### Optimize for Speed[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-speed "Direct link to Optimize for Speed")
Prioritize low-latency providers for interactive use:

```


provider_routing:  





  sort: "latency"  



```

### Optimize for Throughput[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-throughput "Direct link to Optimize for Throughput")
Best for long-form generation where tokens-per-second matters:

```


provider_routing:  





  sort: "throughput"  



```

### Lock to Specific Providers[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#lock-to-specific-providers "Direct link to Lock to Specific Providers")
Ensure all requests go through a specific provider for consistency:

```


provider_routing:  





  only:  





    - "anthropic"  



```

### Avoid Specific Providers[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#avoid-specific-providers "Direct link to Avoid Specific Providers")
Exclude providers you don't want to use (e.g., for data privacy):

```


provider_routing:  





  ignore:  





    - "together"  





    - "lepton"  





  data_collection: "deny"  



```

### Preferred Order with Fallbacks[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#preferred-order-with-fallbacks "Direct link to Preferred Order with Fallbacks")
Try your preferred providers first, fall back to others if unavailable:

```


provider_routing:  





  order:  





    - "anthropic"  





    - "google"  





  require_parameters: true  



```

## How It Works[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#how-it-works "Direct link to How It Works")
Provider routing preferences are passed to OpenRouter on agent chat requests and iteration-limit summaries via the `extra_body.provider` field. (`extra_body` is the OpenAI Python SDK argument; it becomes the top-level `provider` object in the JSON request.) Auxiliary tasks such as compression and title generation are configured independently under `auxiliary.<task>.extra_body`.
  * **CLI mode** — configured in `~/.hermes/config.yaml`, loaded at startup
  * **Gateway mode** — same config file. Messaging-platform turns use the copy loaded when the gateway starts. A local `hermes chat` / TUI session reads it from its own profile when the gateway creates the session: an edit applies to the next new session without a gateway restart, and open sessions keep the values they were created with


The routing config is read from `config.yaml` and passed as parameters when creating the `AIAgent`:

```


providers_allowed  ← from provider_routing.only  





providers_ignored  ← from provider_routing.ignore  





providers_order    ← from provider_routing.order  





provider_sort      ← from provider_routing.sort  





provider_require_parameters ← from provider_routing.require_parameters  





provider_data_collection    ← from provider_routing.data_collection  



```

You can combine multiple options. For example, sort by price but exclude certain providers and require parameter support:

```


provider_routing:  





  sort: "price"  





  ignore: ["together"]  





  require_parameters: true  





  data_collection: "deny"  



```

## Default Behavior[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#default-behavior "Direct link to Default Behavior")
When no `provider_routing` section is configured (the default), the aggregator uses its own default routing logic, which generally balances cost and availability automatically.
Provider routing controls which **sub-providers behind OpenRouter** handle your requests. For automatic failover to an entirely different provider when your primary model fails, see [Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers).
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/provider-routing.md)
[Previous ACP Host Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)[Next Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#configuration)
  * [Options](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#options)
    * [`sort`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#sort)
    * [`only`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#only)
    * [`ignore`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#ignore)
    * [`order`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#order)
    * [`require_parameters`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#require_parameters)
    * [`data_collection`](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#data_collection)
    * [Per-model overrides (`models`)](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#per-model-overrides-models)
  * [Practical Examples](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#practical-examples)
    * [Optimize for Cost](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-cost)
    * [Optimize for Speed](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-speed)
    * [Optimize for Throughput](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#optimize-for-throughput)
    * [Lock to Specific Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#lock-to-specific-providers)
    * [Avoid Specific Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#avoid-specific-providers)
    * [Preferred Order with Fallbacks](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#preferred-order-with-fallbacks)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#how-it-works)
  * [Default Behavior](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing#default-behavior)


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
