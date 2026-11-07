---
title: "Streaming TTS Internals"
source: https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts
scraped_at: 2026-11-07T17:20:37.797601+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#__docusaurus_skipToContent_fallback)
[![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [English](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/streaming-tts)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search`Ctrl``K`
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Features](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
    * [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
    * [TUI & Desktop from Worktrees](https://hermes-agent.nousresearch.com/docs/developer-guide/worktree-ui-dev)
    * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
    * [Extending](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
    * [Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
      * [Tools Runtime](https://hermes-agent.nousresearch.com/docs/developer-guide/tools-runtime)
      * [Browser CDP Supervisor](https://hermes-agent.nousresearch.com/docs/developer-guide/browser-supervisor)
      * [ACP Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/acp-internals)
      * [Cron Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/cron-internals)
      * [Chronos Managed-Cron Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/chronos-managed-cron-contract)
      * [Egress proxy internals](https://hermes-agent.nousresearch.com/docs/developer-guide/egress-internals)
      * [Gateway Monitoring](https://hermes-agent.nousresearch.com/docs/developer-guide/gateway-monitoring)
      * [Relay ↔ Connector Contract](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-connector-contract)
      * [Relay Shared Metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics)
      * [Streaming TTS Internals](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
      * [Billing Lifecycle (TUI)](https://hermes-agent.nousresearch.com/docs/developer-guide/billing-lifecycle)
      * [Trajectory Format](https://hermes-agent.nousresearch.com/docs/developer-guide/trajectory-format)
    * [Packaging & Releases](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)
  * [Reference](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Developer Guide
  * Internals
  * Streaming TTS Internals


On this page
# Streaming TTS
Hermes can stream TTS audio as it arrives from the provider, instead of waiting for the full audio before playing. This is used by voice mode (CLI/TUI live conversation), the dashboard speak-stream WebSocket, and — via the gateway `StreamingTTSConsumer` — any platform adapter that opts into streaming audio. Voice replies start speaking after the first clause instead of after full generation + synthesis.
## Architecture[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#architecture "Direct link to Architecture")
The streaming pipeline has four parts:
  1. **Producer** — the LLM emits text deltas as it generates a response
  2. **Sentence chunker** — `tools.tts_streaming.SentenceChunker` accumulates deltas, strips `<think>` blocks (even split across deltas), and flushes complete sentences
  3. **TTS provider** — a registered `StreamingTTSProvider` turns each sentence into raw PCM chunks (int16 mono at the provider's declared `sample_rate`)
  4. **Audio sink** — `sounddevice.OutputStream` for local playback (`tools.tts_tool_speaker.stream_tts_to_speaker`), or a gateway platform adapter's `write_streaming_tts` seam (`gateway/streaming_tts_consumer.py`)


Providers with no chunked API still get per-_sentence_ playback via the proven sync `text_to_speech_tool` path, so edge (the default) is conversational too. All spoken text is cleaned by `tools.tts_text_normalize.prepare_spoken_text` (one cleaner, all paths).
## How to pick a provider[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#how-to-pick-a-provider "Direct link to How to pick a provider")
By default the dispatcher streams with the provider you already configured (`tts.provider`) when that provider has a chunked API — it never silently swaps your voice for a different provider just to get streaming.
To override, set `tts.streaming.provider` in your `config.yaml`:
  * a provider name (`elevenlabs`, `gemini`, `openai`, `xai`) pins that streamer
  * `auto` walks the priority list `elevenlabs → gemini → openai → xai` and uses the first one whose credentials resolve — an explicit opt-in to "best chunked voice available"



```


tts:  





  provider: gemini  





  streaming:  





    provider: gemini      # or "auto"  





    min_len: 20           # shortest first sentence (chars) spoken on its own; CJK setups use ~6  





  gemini:  





    model: gemini-2.5-flash-preview-tts  





    voice: Kore  



```

## Capability matrix[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#capability-matrix "Direct link to Capability matrix")  
| Provider  | Transport  | Chunked PCM  | Credentials  |  
| --- | --- | --- | --- |  
| elevenlabs  | chunked HTTP (`pcm_24000`)  | yes  |  `ELEVENLABS_API_KEY` / `tts.elevenlabs`  |  
| openai  | chunked HTTP (`with_streaming_response`, `pcm`)  | yes  |  `tts.openai.api_key` → env → managed gateway  |  
| gemini  | SSE (`streamGenerateContent?alt=sse`)  | yes  |  `GEMINI_API_KEY` / `GOOGLE_API_KEY`  |  
| xai  | WebSocket (`wss://api.x.ai/v1/tts`)  | yes  |  `XAI_API_KEY` preferred, else xAI OAuth (the subscription bearer 403s on metered TTS)  |  
| edge, piper, kitten, neutts, mistral, minimax, deepinfra, …  | —  | no (per-sentence sync fallback)  | as usual  |  
| plugin `TTSProvider` with `streams_pcm`  | the plugin's `stream(format="pcm")`  | yes, at its `stream_sample_rate`  | the plugin's own  |  
All credential lookups go through `resolve_provider_secret()` (config > env/.env > credential pool) — never bare env reads. Streamed bodies are capped at 16 MiB per sentence, mirroring the sync providers' bounded upstream-body invariant.
## Adding a new streaming provider[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#adding-a-new-streaming-provider "Direct link to Adding a new streaming provider")
  1. Subclass `StreamingTTSProvider` in `tools/tts_streaming.py`
  2. Set `sample_rate` (and `channels` / `sample_width` if not int16 mono)
  3. Implement `available()` (a pure probe — never install anything) and `stream(self, text) -> Iterator[bytes]` yielding raw PCM chunks
  4. Decorate with `@register("yourname")`
  5. Add tests in `tests/tools/test_tts_streaming.py`


The ABC enforces the contract; the registry makes the provider discoverable; the dispatcher (`stream_tts_to_speaker`) and the gateway consumer handle the sentence buffer, stop events, and audio sink for free.
## Plugin providers[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#plugin-providers "Direct link to Plugin providers")
A plugin `TTSProvider` (registered with `ctx.register_tts_provider()`) joins this path without core changes. It sets `streams_pcm = True` and a positive `stream_sample_rate`, and its `stream(text, format="pcm", voice=, model=, speed=)` yields int16 mono PCM. `resolve_streaming_provider` adapts it (`tools.tts_streaming._PluginPCMStreamer`) under the same routing rules as the sync dispatcher (`tools.tts_tool_plugins`): built-in names never reach the registry, a same-named `type: command` provider wins, and the plugin gets the same `tts.voice` / `tts.model` / `tts.speed` as `synthesize()`. A configured plugin streams first. Under `tts.streaming.provider: auto` it is tried only after the built-in priority list. `streams_pcm`, `stream_sample_rate` and `is_available()` are read every time a streamer is resolved. If the rate is missing or the provider reports unavailable, Hermes keeps per-sentence synthesis. As with the built-in streamers, the speaker pipeline prefetches up to three sentences, so a plugin's `stream()` must tolerate concurrent calls (the sync path serializes `synthesize()`; this path does not).
## Gateway streaming (platform adapters)[​](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#gateway-streaming-platform-adapters "Direct link to Gateway streaming \(platform adapters\)")
`gateway/streaming_tts_consumer.py` bridges agent deltas to an adapter's streaming-audio seam. Adapters opt in by overriding, on `BasePlatformAdapter`:
  * `supports_streaming_tts(chat_id, audio_format) -> bool`
  * `begin_streaming_tts / write_streaming_tts / finish_streaming_tts / abort_streaming_tts`


All default to unsupported/no-op, so existing adapters are untouched. When a turn's streaming audio completes, the whole-file auto-TTS reply for that turn is suppressed (no double playback); when streaming fails before any audio was audible, the gateway falls back to the legacy whole-file voice reply.
[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/developer-guide/streaming-tts.md)
[Previous Relay Shared Metrics](https://hermes-agent.nousresearch.com/docs/developer-guide/relay-shared-metrics)[Next Billing Lifecycle (TUI)](https://hermes-agent.nousresearch.com/docs/developer-guide/billing-lifecycle)
  * [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#architecture)
  * [How to pick a provider](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#how-to-pick-a-provider)
  * [Capability matrix](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#capability-matrix)
  * [Adding a new streaming provider](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#adding-a-new-streaming-provider)
  * [Plugin providers](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#plugin-providers)
  * [Gateway streaming (platform adapters)](https://hermes-agent.nousresearch.com/docs/developer-guide/streaming-tts#gateway-streaming-platform-adapters)


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
