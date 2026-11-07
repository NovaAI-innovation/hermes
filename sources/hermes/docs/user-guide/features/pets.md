---
title: "Pets (Petdex Mascots)"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/pets
scraped_at: 2026-11-07T17:19:38.844921+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/pets)


[Home](https://hermes-agent.nousresearch.com)[GitHub](https://github.com/NousResearch/hermes-agent)[Discord](https://discord.gg/NousResearch)
Search
  * [User Stories & Use Cases](https://hermes-agent.nousresearch.com/docs/user-stories)
  * [Browse Skills](https://hermes-agent.nousresearch.com/docs/skills)
  * [Browse Plugins](https://hermes-agent.nousresearch.com/docs/plugins)
  * [Getting Started](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
  * [Using Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/cli)
  * [Features](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
    * [Tool Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway)
    * [Core](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
    * [Automation](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
    * [Media & Web](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)
      * [Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode)
      * [Wake Word](https://hermes-agent.nousresearch.com/docs/user-guide/features/wake-word)
      * [Web Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)
      * [X (Twitter) Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search)
      * [Browser](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser)
      * [Passwords & Logins](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-vault)
      * [Computer Use](https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use)
      * [Bot Screen](https://hermes-agent.nousresearch.com/docs/user-guide/features/bot-screen)
      * [Vision & Image Paste](https://hermes-agent.nousresearch.com/docs/user-guide/features/vision)
      * [Image Generation](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation)
      * [Spotify](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify)
      * [Pets (Petdex Mascots)](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets)
      * [Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts)
      * [Deliverable Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/deliverable-mode)
    * [Management](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
    * [Skills](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
  * [Messaging Platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
  * [Integrations](https://hermes-agent.nousresearch.com/docs/integrations/)
  * [Guides & Tutorials](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free)
  * [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)
  * [Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)


  * [](https://hermes-agent.nousresearch.com/docs/)
  * Features
  * Media & Web
  * Pets (Petdex Mascots)


On this page
# Pets
Hermes can show an animated **pet** — a small mascot sprite that reacts to what the agent is doing (idle, running a tool, thinking, finishing, failing) across the **CLI** , **TUI** , and **desktop app**. Pets come from the public [petdex](https://github.com/crafter-station/petdex) gallery.
Pets are purely cosmetic. They have **no effect on prompt caching, tokens, or the agent's behavior** — the sprite is a display concern only. The feature is **off by default** and stays dormant until you install and select a pet.
## How it works[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#how-it-works "Direct link to How it works")
  * Pets are installed into your profile's `pets/` directory (`<HERMES_HOME>/pets/<slug>/`), so each [profile](https://hermes-agent.nousresearch.com/docs/user-guide/profiles) keeps its own set.
  * Selecting a pet writes `display.pet.slug` and `display.pet.enabled` to `config.yaml` — nothing is stored as a secret or env var.
  * Each surface watches the activity it already tracks and maps it to one of six animation states. The mapping lives in one place so every surface behaves the same:  
| Agent activity  | Pet state  |  
| --- | --- |  
| A tool/turn just failed  | `failed`  |  
| A plan finished (all todos done)  |  `jump` (celebrate)  |  
| A turn finished cleanly  | `wave`  |  
| A tool is executing  | `run`  |  
| The model is thinking/reading  | `review`  |  
| Turn in flight (unspecified)  | `run`  |  
| Blocked on you (a clarify/approval prompt is open)  |  `waiting` (falls back to `idle` on legacy 8-row sheets)  |  
| Nothing happening  | `idle`  |  


## Rendering[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#rendering "Direct link to Rendering")
In the terminal (CLI/TUI), Hermes renders the sprite at full fidelity when your terminal supports a graphics protocol (**kitty** , **Ghostty** , **WezTerm** , **iTerm2** , or **sixel**). Otherwise it falls back automatically to a truecolor Unicode **half-block** rendering. Inside a pipe or redirect (no TTY), terminal rendering is disabled by design.
The desktop app draws the pet as a floating sprite on a canvas and toggles it from **Settings → Appearance**.
## Quick start (CLI)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#quick-start-cli "Direct link to Quick start \(CLI\)")

```


# Browse the gallery (filter by substring)  





hermes pets list  





hermes pets list cat  





  





# Install a pet and make it active in one step  





hermes pets install boba --select  





  





# Preview / animate it in your terminal (Ctrl+C to stop)  





hermes pets show  





  





# Check your setup  





hermes pets doctor  



```

##  `hermes pets` commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#hermes-pets-commands "Direct link to hermes-pets-commands")  
| Goal  | Command  |  
| --- | --- |  
| Browse the gallery  | `hermes pets list [query] [--limit N]`  |  
| List installed pets  | `hermes pets list --installed`  |  
| Install a pet  | `hermes pets install <slug> [--select] [--force]`  |  
| Set the active pet  |  `hermes pets select [slug]` (omit slug for a picker)  |  
| Resize the pet everywhere  |  `hermes pets scale <factor>` (e.g. `0.5`, clamped 0.1–3.0)  |  
| Preview/animate  | `hermes pets show [slug] [--state <s>] [--cycle] [--once] [--mode <m>] [--scale <f>]`  |  
| Disable the pet  | `hermes pets off`  |  
| Remove an installed pet  | `hermes pets remove <slug>`  |  
| Diagnose setup  | `hermes pets doctor`  |  
`hermes pets show` flags:
  * `--state` — play a single state (`idle`, `wave`, `run`, `failed`, `review`, `jump`).
  * `--cycle` — cycle through every state.
  * `--once` — play once instead of looping.
  * `--mode` — override the render protocol (`kitty`, `iterm`, `sixel`, `unicode`, `auto`).
  * `--scale` — override the on-screen scale (`0` = use config).


##  `/pet` slash command[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#pet-slash-command "Direct link to pet-slash-command")
Inside the CLI and TUI you can manage the pet without leaving the session:
  * `/pet` — toggle the pet on/off (adopts the first installed pet if none is active).
  * `/pet list` — browse the gallery.
  * `/pet scale <factor>` — resize the pet everywhere (e.g. `/pet scale 0.5`).
  * `/pet <slug>` — adopt a specific pet.
  * `/pet off` — disable the pet.


In the TUI, `/pet list` opens an interactive picker overlay; in the desktop app it opens the Cmd+K pet palette.
## Generating a pet (`/hatch`)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#generating-a-pet-hatch "Direct link to generating-a-pet-hatch")
Beyond installing pre-made pets from the gallery, Hermes can **generate a brand-new pet** from a text description — its own AI sprite-generation pipeline.
  * CLI/TUI: `/hatch <description>` (alias `/generate-pet`), or `hermes pets` → the generate flow.
  * Desktop app: the Pokédex-style **generate** UI — an animated egg, hatch FX, and a draft picker.


How generation works (a two-step, cost-bounded flow):
  1. **Base drafts** — a handful of cheap, prompt-only "what should this pet look like" variants are generated. You pick one, or remix/retry for a fresh round.
  2. **Hatch** — the chosen base is used as a reference image to generate one grounded animation row per Hermes state (idle, thinking, tool use, etc.), which are deterministically sliced into frames and packed into a standard petdex/Codex atlas (8×9 grid of 192×208 cells). The result is a valid spritesheet you keep — and could `petdex submit`.


### Image backend[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#image-backend "Direct link to Image backend")
Generation uses the active [image-generation provider](https://hermes-agent.nousresearch.com/docs/user-guide/features/image-generation), but it requires **reference-image grounding** so each animation row stays the same character as the base. Reference-capable backends: **Nous Portal** , **OpenRouter** , **OpenAI** (`gpt-image-2`), and **Krea**. OpenRouter/Nous run a quality-first model chain by default.
  * Resolution order prefers Nous Portal → OpenAI → OpenRouter.
  * If no reference-capable backend is configured, generation surfaces an actionable error pointing you to `hermes tools` → Image Generation. (Installing/adopting existing gallery pets needs no image backend.)
  * Override the backend with the `HERMES_PET_IMAGE_PROVIDER` env var (e.g. `HERMES_PET_IMAGE_PROVIDER=openrouter`).


## Desktop app[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#desktop-app "Direct link to Desktop app")
In the desktop app you can manage the pet two ways:
  * **Cmd+K → "Pets…"** — browse, search, adopt, and toggle pets without leaving the keyboard (mirrors the theme picker).
  * **Settings → Appearance** — the same gallery plus a **size slider** that resizes the floating mascot live as you drag.


Both adopt/toggle/resize the floating mascot in place — size changes apply instantly; adopting a new pet lights it up within a moment.
### Roaming[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#roaming "Direct link to Roaming")
Settings → Appearance has a **Roam** toggle: when enabled, the pet wanders the window on its own while the agent is idle — walking surfaces, pausing, and hopping between spots. Roaming only runs while the pet is in-window, active, and the agent is at rest; any agent-driven state (working, celebrating) immediately takes over. The toggle is off by default and persists across restarts.
### Alt+wheel resizing[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#altwheel-resizing "Direct link to Alt+wheel resizing")
Hold **Alt** and scroll the mouse wheel over the pet to resize it in place — in the app window and on the popped-out overlay alike. The overlay zooms toward the cursor position and the resulting scale is persisted, so it survives restarts and stays in sync with the in-app pet.
### Vibe reactions[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#vibe-reactions "Direct link to Vibe reactions")
Say something nice to the agent — "good bot", "thank you", "ily", `<3`, or a heart emoji — and the pet reacts with floating hearts (desktop) or a heart flash (CLI/TUI). Detection is a curated, token-free lexicon matched locally on each user message (no model call); it fires on affection and gratitude aimed at the agent, not general positive sentiment. All surfaces — CLI pet, TUI, desktop floating pet, and the pop-out overlay — react off the same signal.
### Pop-out overlay[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#pop-out-overlay "Direct link to Pop-out overlay")
**Shift-click** the floating pet to pop it out into its own transparent, always-on-top desktop window. Out there it stays visible while Hermes is minimized (Codex-style), so a glance tells you what the agent is doing.
Gestures once it's popped out:  
| Gesture  | Action  |  
| --- | --- |  
| **Drag**  | Move the pet anywhere on screen, even outside the app. Its spot and in/out state persist across restarts.  |  
| **Single-click**  | Open a mini composer to send a prompt to the most recent session — without surfacing the app.  |  
| **Double-click**  | Toggle the app window: minimize it if it's up front, restore it if it's hidden.  |  
| **Shift-click**  | Pop the pet back into the window.  |  
| **Mail icon**  | Appears only when a turn finished while you were away; click to raise the app on the most recent thread (and mark it read).  |  
Only the popped-out pet shows a **speech bubble** (`working…`, `thinking…`, `your turn`, …) — in-window the app itself is the surface, so the pet stays quiet there.
The overlay is a pure puppet of the in-app pet — it carries no separate gateway connection and never appears in the dock or app switcher.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#configuration "Direct link to Configuration")
All settings live under `display.pet` in `config.yaml`:

```


display:  





  pet:  





    enabled: false        # master on/off (true once you select a pet)  





    slug: ""              # active pet; empty = first installed  





    render_mode: auto      # auto | kitty | iterm | sixel | unicode | off  





    scale: 0.33           # master size knob (relative to native 192x208 frames)  





    unicode_cols: 0       # hard override for terminal width (0 = derive from scale)  



```

  * **`scale`**is the single master size knob. One number shrinks every surface: the desktop canvas scales its pixels by it, and the CLI/TUI derive their terminal column width from it. The half-block fallback clamps to a legibility floor — it can't shrink as far as true-pixel kitty/GUI rendering without turning to mush, so the same`scale` looks crisp under kitty but is floored in half-blocks.
  * **`render_mode: auto`**detects kitty/iTerm2/sixel and falls back to unicode half-blocks. Set it explicitly to force a protocol or`off` to disable terminal rendering while keeping the pet on the desktop.
  * **`unicode_cols`**pins the terminal column width independently of`scale` ; leave it at `0` to derive width from `scale`.


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#troubleshooting "Direct link to Troubleshooting")
Run `hermes pets doctor` — it reports:
  * the pets directory and which pets are installed,
  * `display.pet.enabled`, `display.pet.slug`, and the resolved active pet,
  * the configured `render_mode`, the detected terminal graphics protocol, and the effective mode for a TTY,
  * whether Pillow (used for sprite decoding) is importable.


It prints `✓ ready` once a pet is installed, selected, enabled, and Pillow is available.
Common gotchas:
  * A pet only shows once one is **installed AND selected** (`enabled: true`).
  * Inside a pipe/redirect (no TTY), terminal rendering is disabled by design.
  * The petdex npm CLI installs to `~/.codex/pets`; Hermes uses its own profile-scoped `<HERMES_HOME>/pets/` instead — install through `hermes pets`.


## See also[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#see-also "Direct link to See also")
  * The [`hermes-agent` skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-hermes-agent) lets the agent install and switch pets for you on request (see its `references/petdex.md`).


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/pets.md)
[Previous Spotify](https://hermes-agent.nousresearch.com/docs/user-guide/features/spotify)[Next Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts)
  * [How it works](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#how-it-works)
  * [Rendering](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#rendering)
  * [Quick start (CLI)](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#quick-start-cli)
  * [`hermes pets` commands](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#hermes-pets-commands)
  * [`/pet` slash command](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#pet-slash-command)
  * [Generating a pet (`/hatch`)](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#generating-a-pet-hatch)
    * [Image backend](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#image-backend)
  * [Desktop app](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#desktop-app)
    * [Roaming](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#roaming)
    * [Alt+wheel resizing](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#altwheel-resizing)
    * [Vibe reactions](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#vibe-reactions)
    * [Pop-out overlay](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#pop-out-overlay)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#configuration)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#troubleshooting)
  * [See also](https://hermes-agent.nousresearch.com/docs/user-guide/features/pets#see-also)


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
