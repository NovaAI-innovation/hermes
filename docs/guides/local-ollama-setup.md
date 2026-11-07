---
title: "Run Hermes Locally with Ollama — Zero API Cost"
source: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
scraped_at: 2026-11-07T17:20:11.920736+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)
  * [English](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/local-ollama-setup)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
On this page
# Run Hermes Locally with Ollama — Zero API Cost
On the Hermes desktop app, **Settings → Providers → Local Models** installs and manages a local llama.cpp server for you — model downloads, memory fitting, and context sizing included. See [Local Models](https://hermes-agent.nousresearch.com/docs/user-guide/local-models). This guide is for manual setup: Ollama specifically, CLI-first workflows, or servers you want to run yourself.
## The Problem[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#the-problem "Direct link to The Problem")
Cloud LLM APIs charge per token. A heavy coding session can cost $5–20. For personal projects, learning, or privacy-sensitive work, that adds up — and you're sending every conversation to a third party.
## What This Guide Solves[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-this-guide-solves "Direct link to What This Guide Solves")
You'll set up Hermes Agent running entirely on your own hardware, using [Ollama](https://ollama.com) as the model backend. No API keys, no subscriptions, no data leaving your machine. Once configured, Hermes works exactly like it does with OpenRouter or Anthropic — terminal commands, file editing, web browsing, delegation — but the model runs locally.
By the end, you'll have:
  * Ollama serving one or more open-weight models
  * Hermes connected to Ollama as a custom endpoint
  * A working local agent that can edit files, run commands, and browse the web
  * Optional: a Telegram/Discord bot powered entirely by your own hardware


## What You Need[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-you-need "Direct link to What You Need")  
| Component  | Minimum  | Recommended  |  
| --- | --- | --- |  
| **RAM**  | 8 GB (for 3B models)  | 32+ GB (for 27B+ models)  |  
| **Storage**  | 5 GB free  | 30+ GB (for multiple models)  |  
| **CPU**  | 4 cores  | 8+ cores (AMD EPYC, Ryzen, Intel Xeon)  |  
| **GPU**  | Not required  | NVIDIA GPU with 8+ GB VRAM speeds things up significantly  |  
Ollama runs on CPU-only servers. A 9B model on a modern 8-core CPU gives ~10 tokens/sec. A 31B model on CPU is slower (~2–5 tokens/sec) — each response takes 30–120 seconds, but it works. A GPU dramatically improves this. For CPU-only setups, widen the API timeout via the env var (it's not a `config.yaml` key):

```


# ~/.hermes/.env  





HERMES_API_TIMEOUT=1800   # 30 minutes — generous for slow local models  



```

## Step 1: Install Ollama[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-1-install-ollama "Direct link to Step 1: Install Ollama")

```


curl -fsSL https://ollama.com/install.sh | sh  



```

Verify it's running:

```


ollama --version  





curl http://localhost:11434/api/tags   # Should return {"models":[]}  



```

## Step 2: Pull a Model[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-2-pull-a-model "Direct link to Step 2: Pull a Model")
Choose based on your hardware:  
| Model  | Size on Disk  | RAM Needed  | Tool Calling  | Best For  |  
| --- | --- | --- | --- | --- |  
| `gemma4:31b`  | ~20 GB  | 24+ GB  | Yes  | Best quality — strong tool use and reasoning  |  
| `gemma2:27b`  | ~16 GB  | 20+ GB  | No  | Conversational tasks, no tool use  |  
| `gemma2:9b`  | ~5 GB  | 8+ GB  | No  | Fast chat, Q&A — cannot call tools  |  
| `llama3.2:3b`  | ~2 GB  | 4+ GB  | No  | Lightweight quick answers only  |  
Hermes is an **agentic** assistant — it edits files, runs commands, and browses the web through tool calls. Models without tool-call support can only chat; they can't take actions. For the full Hermes experience, use a model that supports tools (like `gemma4:31b`).
Pull your chosen model:

```


ollama pull gemma4:31b  



```

You can pull several models and switch between them inside Hermes with `/model`. Ollama loads the active model into memory on demand and unloads idle ones automatically.
Verify the model works:

```


curl http://localhost:11434/v1/chat/completions \  





  -H "Content-Type: application/json" \  





  -d '{  





    "model": "gemma4:31b",  





    "messages": [{"role": "user", "content": "Say hello"}],  





    "max_tokens": 50  





  }'  



```

You should see a JSON response with the model's reply.
## Step 3: Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-3-configure-hermes "Direct link to Step 3: Configure Hermes")
Run the Hermes setup wizard:

```


hermes setup  



```

When prompted for a provider, select **Custom Endpoint** and enter:
  * **Base URL:** `http://localhost:11434/v1`
  * **API Key:** Leave empty or type `no-key` (Ollama doesn't need one)
  * **Model:** `gemma4:31b` (or whichever model you pulled)


Alternatively, edit `~/.hermes/config.yaml` directly:

```


model:  





  default: "gemma4:31b"  





  provider: "custom"  





  base_url: "http://localhost:11434/v1"  



```

## Step 4: Start Using Hermes[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-4-start-using-hermes "Direct link to Step 4: Start Using Hermes")

```


hermes  



```

That's it. You're now running a fully local agent. Try it out:

```


You: List all Python files in this directory and count the lines of code in each  





  





You: Read the README.md and summarize what this project does  





  





You: Create a Python script that fetches the weather for Ho Chi Minh City  



```

Hermes will use the terminal tool, file operations, and your local model — no cloud calls.
## Step 5: Pick the Right Model for Your Task[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-5-pick-the-right-model-for-your-task "Direct link to Step 5: Pick the Right Model for Your Task")
Not every task needs the biggest model. Here's a practical guide:  
| Task  | Recommended Model  | Why  |  
| --- | --- | --- |  
| File edits, code, terminal commands  | `gemma4:31b`  | Only model with reliable tool calling  |  
| Quick Q&A (no tool use needed)  | `gemma2:9b`  | Fast responses for conversational tasks  |  
| Lightweight chat  | `llama3.2:3b`  | Fastest, but very limited capabilities  |  
For full agentic work (editing files, running commands, browsing), `gemma4:31b` is currently the best local option with tool-call support. Check [Ollama's model library](https://ollama.com/library) for newer models — tool-calling support is expanding rapidly.
Switch models on the fly inside a session:

```


/model gemma2:9b  



```

## Step 6: Optimize for Speed[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-6-optimize-for-speed "Direct link to Step 6: Optimize for Speed")
### Increase Ollama's Context Window[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#increase-ollamas-context-window "Direct link to Increase Ollama's Context Window")
By default, Ollama uses a 2048-token context. Hermes requires at least 64,000 tokens for agentic work with tools:

```


# Create a Modelfile that extends context  





cat > ~/.hermes/cache/scratch/Modelfile << 'EOF'  





FROM gemma4:31b  





PARAMETER num_ctx 64000  





EOF  





  





ollama create gemma4-64k -f ~/.hermes/cache/scratch/Modelfile  



```

Then update your Hermes config to use `gemma4-64k` as the model name.
### Keep the Model Loaded[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#keep-the-model-loaded "Direct link to Keep the Model Loaded")
By default, Ollama unloads models after 5 minutes of inactivity. For a persistent gateway bot, keep it loaded:

```


# Set keep-alive to 24 hours  





curl http://localhost:11434/api/generate \  





  -d '{"model": "gemma4:31b", "keep_alive": "24h"}'  



```

Or set it globally in Ollama's environment:

```


# /etc/systemd/system/ollama.service.d/override.conf  





[Service]  





Environment="OLLAMA_KEEP_ALIVE=24h"  



```

### Use GPU Offloading (If Available)[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#use-gpu-offloading-if-available "Direct link to Use GPU Offloading \(If Available\)")
If you have an NVIDIA GPU, Ollama automatically offloads layers to it. Check with:

```


ollama ps   # Shows which model is loaded and how many GPU layers  



```

For a 31B model on a 12 GB GPU, you'll get partial offload (~40 layers on GPU, rest on CPU), which still gives a significant speedup.
## Step 7: Run as a Gateway Bot (Optional)[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-7-run-as-a-gateway-bot-optional "Direct link to Step 7: Run as a Gateway Bot \(Optional\)")
Once Hermes works locally in the CLI, you can expose it as a Telegram or Discord bot — still running entirely on your hardware.
### Telegram[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#telegram "Direct link to Telegram")
  1. Create a bot via [@BotFather](https://t.me/BotFather) and get the token
  2. Add to your `~/.hermes/config.yaml`:



```


model:  





  default: "gemma4:31b"  





  provider: "custom"  





  base_url: "http://localhost:11434/v1"  





  





platforms:  





  telegram:  





    enabled: true  





    token: "YOUR_TELEGRAM_BOT_TOKEN"  



```

  1. Start the gateway:



```


hermes gateway  



```

Now message your bot on Telegram — it responds using your local model.
### Discord[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#discord "Direct link to Discord")
  1. Create a Discord application at [discord.com/developers](https://discord.com/developers/applications)
  2. Add to config:



```


platforms:  





  discord:  





    enabled: true  





    token: "YOUR_DISCORD_BOT_TOKEN"  



```

  1. Start: `hermes gateway`


## Step 8: Set Up Fallbacks (Optional)[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-8-set-up-fallbacks-optional "Direct link to Step 8: Set Up Fallbacks \(Optional\)")
Local models can struggle with complex tasks. Set up a cloud fallback that only activates when the local model fails:

```


model:  





  default: "gemma4:31b"  





  provider: "custom"  





  base_url: "http://localhost:11434/v1"  





  





fallback_providers:  





  - provider: openrouter  





    model: anthropic/claude-sonnet-4  



```

This way, 90% of your usage is free (local), and only the hard tasks hit the paid API.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#troubleshooting "Direct link to Troubleshooting")
### "provider 'ollama' has no endpoint configured"[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#provider-ollama-has-no-endpoint-configured "Direct link to "provider 'ollama' has no endpoint configured"")
`hermes chat --provider ollama` (or `vllm`) stops with this error when no endpoint is configured for that alias anywhere — no `providers.ollama.base_url`, no `model.base_url`. Hermes refuses to send the request rather than fall back to OpenRouter with a cloud key (`OPENROUTER_API_KEY` / `OPENAI_API_KEY`) that happens to be set. Add the endpoint:

```


providers:  





  ollama:  





    base_url: "http://localhost:11434/v1"  



```

### "Connection refused" on startup[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#connection-refused-on-startup "Direct link to "Connection refused" on startup")
Ollama isn't running. Start it:

```


sudo systemctl start ollama  





# or  





ollama serve  



```

### Slow responses[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#slow-responses "Direct link to Slow responses")
  * **Check model size vs RAM:** If your model needs more RAM than available, it swaps to disk. Use a smaller model or add RAM.
  * **Check`ollama ps` :** If no GPU layers are offloaded, responses are CPU-bound. This is normal for CPU-only servers.
  * **Reduce context:** Large conversations slow down inference. Use `/compress` regularly, or set a lower compression threshold in config.


### Slow first response (prefill)[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#slow-first-response-prefill "Direct link to Slow first response \(prefill\)")
Hermes sends a fixed payload on every API call — the system prompt plus the tool schemas for all enabled tools — before any of your conversation content. On CPU-only or low-VRAM setups, processing that prompt (the _prefill_ phase) dominates the first turn: the model can sit silent for minutes while it works through the prompt, then generate at its normal pace. This is expected behaviour, not a hang. The [Mac local-LLM guide](https://hermes-agent.nousresearch.com/docs/guides/local-llm-on-mac#timeouts) documents the same effect — during prefill on large contexts, local models may produce no output for minutes while processing the prompt — and Hermes automatically raises its stream read timeout from 120s to 1800s for local endpoints (`HERMES_STREAM_READ_TIMEOUT`).
What helps:
  * **Keep the model loaded** — Ollama unloads idle models after 5 minutes, adding a full reload before the next prefill. Set `OLLAMA_KEEP_ALIVE=24h` (see [Step 6](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#keep-the-model-loaded)).
  * **Widen the API timeout** — set `HERMES_API_TIMEOUT=1800` in `~/.hermes/.env` (see [What You Need](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-you-need)).
  * **Measure and trim the fixed prompt** — run `hermes prompt-size` for a byte breakdown of the system prompt and tool schemas, then disable unused toolsets with `hermes tools` and uninstall skills you don't need with `hermes skills`.
  * **Use GPU offloading** — even a partial offload gives a significant speedup (see [Step 6](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#use-gpu-offloading-if-available)).


### Model doesn't follow tool calls[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#model-doesnt-follow-tool-calls "Direct link to Model doesn't follow tool calls")
Models without tool-call support produce plain text instead of structured function calls. Solutions:
  * **Use a model with tool-call support** — of the models listed above, only `gemma4:31b` has reliable tool calling.
  * **Hermes has auto-repair** — it detects malformed tool calls and attempts to fix them automatically.
  * **Set up a fallback** — if the local model fails 3 times, Hermes falls back to a cloud provider.


If the model prints raw JSON like `{"name": "web_search", ...}` in its reply instead of actually running the tool, that's usually the _server_ , not the model — tool calling isn't enabled or the tool-call format isn't parsed. See the per-server fix table in [Tool calls appear as text instead of executing](https://hermes-agent.nousresearch.com/docs/integrations/providers#tool-calls-appear-as-text-instead-of-executing) (llama.cpp needs `--jinja`, vLLM needs `--enable-auto-tool-choice --tool-call-parser hermes`, and so on).
### Context window errors[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#context-window-errors "Direct link to Context window errors")
The default Ollama context (2048 tokens) is too small for agentic work. See [Step 6](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-6-optimize-for-speed) to increase it.
## Cost Comparison[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#cost-comparison "Direct link to Cost Comparison")
Here's what running locally saves compared to cloud APIs, based on a typical coding session (~100K tokens input, ~20K tokens output):  
| Provider  | Cost per Session  | Monthly (daily use)  |  
| --- | --- | --- |  
| Anthropic Claude Sonnet  | ~$0.80  | ~$24  |  
| OpenRouter (GPT-4o)  | ~$0.60  | ~$18  |  
| **Ollama (local)**  | **$0.00**  | **$0.00**  |  
Your only cost is electricity — roughly $0.01–0.05 per session depending on hardware.
## What Works Well Locally[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-works-well-locally "Direct link to What Works Well Locally")
  * **File editing and code generation** — models 9B+ handle this well
  * **Terminal commands** — Hermes wraps the command, runs it, reads output regardless of model
  * **Web browsing** — the browser tool does the fetching; the model just interprets results
  * **Cron jobs and scheduled tasks** — work identically to cloud setups
  * **Multi-platform gateway** — Telegram, Discord, Slack all work with local models


## What's Better with Cloud Models[​](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#whats-better-with-cloud-models "Direct link to What's Better with Cloud Models")
  * **Very complex multi-step reasoning** — 70B+ or cloud models like Claude Opus are noticeably better
  * **Long context windows** — cloud models offer 100K–1M tokens; local runtimes often default below Hermes' 64K minimum unless you configure them
  * **Speed on large responses** — cloud inference is faster than CPU-only local for long generations


The sweet spot: use local for everyday tasks, set up a cloud fallback for the hard stuff.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/guides/local-ollama-setup.md)
  * [The Problem](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#the-problem)
  * [What This Guide Solves](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-this-guide-solves)
  * [What You Need](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-you-need)
  * [Step 1: Install Ollama](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-1-install-ollama)
  * [Step 2: Pull a Model](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-2-pull-a-model)
  * [Step 3: Configure Hermes](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-3-configure-hermes)
  * [Step 4: Start Using Hermes](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-4-start-using-hermes)
  * [Step 5: Pick the Right Model for Your Task](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-5-pick-the-right-model-for-your-task)
  * [Step 6: Optimize for Speed](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-6-optimize-for-speed)
    * [Increase Ollama's Context Window](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#increase-ollamas-context-window)
    * [Keep the Model Loaded](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#keep-the-model-loaded)
    * [Use GPU Offloading (If Available)](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#use-gpu-offloading-if-available)
  * [Step 7: Run as a Gateway Bot (Optional)](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-7-run-as-a-gateway-bot-optional)
    * [Telegram](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#telegram)
    * [Discord](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#discord)
  * [Step 8: Set Up Fallbacks (Optional)](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#step-8-set-up-fallbacks-optional)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#troubleshooting)
    * ["provider 'ollama' has no endpoint configured"](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#provider-ollama-has-no-endpoint-configured)
    * ["Connection refused" on startup](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#connection-refused-on-startup)
    * [Slow responses](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#slow-responses)
    * [Slow first response (prefill)](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#slow-first-response-prefill)
    * [Model doesn't follow tool calls](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#model-doesnt-follow-tool-calls)
    * [Context window errors](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#context-window-errors)
  * [Cost Comparison](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#cost-comparison)
  * [What Works Well Locally](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#what-works-well-locally)
  * [What's Better with Cloud Models](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup#whats-better-with-cloud-models)


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
