---
title: "Optional Skills Catalog"
source: "https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog"
scraped_at: "2026-11-07T17:20:37.815050+00:00"
doc_id: "reference/optional-skills-catalog"
content_hash: "cf574c381fffc394"
corpus_source: "hermes"
---

# Optional Skills Catalog
Optional skills ship with hermes-agent under `optional-skills/` but are **not active by default**. Install them explicitly:

```

hermes skills install official/<category>/<skill>

```

For example:

```

hermes skills install official/blockchain/solana

hermes skills install official/mlops/flash-attention

```

Each skill below links to a dedicated page with its full definition, setup, and usage.
To uninstall:

```

hermes skills uninstall <skill-name>

```

## autonomous-ai-agents
| Skill  | Description  |
| --- | --- |
| [**agent-merge-conflict-arbiter**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-agent-merge-conflict-arbiter)  | Neutral arbiter for merge conflicts between two agents.  |
| [**antigravity-cli**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-antigravity-cli)  | Operate the Antigravity CLI (agy): plugins, auth, sandbox.  |
| [**blackbox**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-blackbox)  | Delegate coding tasks to the Blackbox AI multi-model CLI.  |
| [**dynamic-workflow**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-dynamic-workflow)  | Plan-in-code fan-outs, adversarial verification, waves.  |
| [**grok**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-grok)  | Delegate coding to xAI Grok Build CLI (features, PRs).  |
| [**opencode**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode)  | Delegate coding to OpenCode CLI (features, PR review).  |
| [**openhands**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-openhands)  | Delegate coding to OpenHands CLI (model-agnostic, LiteLLM).  |
## blockchain
| Skill  | Description  |
| --- | --- |
| [**evm**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/blockchain/blockchain-evm)  | Read-only EVM client: wallets, tokens, gas across 8 chains.  |
| [**hyperliquid**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/blockchain/blockchain-hyperliquid)  | Hyperliquid market data, account history, trade review.  |
| [**solana**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/blockchain/blockchain-solana)  | Query Solana wallets, tokens, txs, and NFTs in USD.  |
## communication
| Skill  | Description  |
| --- | --- |
| [**one-three-one-rule**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/communication/communication-one-three-one-rule)  | 1-3-1 decision briefs: problem, three options, one pick.  |
## creative
| Skill  | Description  |
| --- | --- |
| [**ai-presenter-video**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-ai-presenter-video)  | Make a verified AI presenter video from script + image.  |
| [**anatomy**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-anatomy)  | Explain an idea as an interactive isometric machine figure.  |
| [**archify**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-archify)  | Validated interactive HTML diagrams, upstream-maintained.  |
| [**ascii-art**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-ascii-art)  | ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.  |
| [**auteur**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-auteur)  | Design and build cinematic, award-level web pages.  |
| [**baoyu-article-illustrator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-baoyu-article-illustrator)  | Article illustrations: type × style × palette consistency.  |
| [**baoyu-comic**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-baoyu-comic)  | Knowledge comics (知识漫画): educational, biography, tutorial.  |
| [**brag**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-brag)  | Project launch video via Hyperframes, upstream-maintained.  |
| [**brag-slim**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-brag-slim)  | Launch video from a project or URL, upstream-maintained.  |
| [**comfyui**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-comfyui)  | Generate images, video, and audio via diffusion workflows.  |
| [**concept-diagrams**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-concept-diagrams)  | Generate flat, minimal educational SVG visuals as HTML.  |
| [**creative-ideation**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-creative-ideation)  | Generate ideas via named methods from creative practice.  |
| [**design-md**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-design-md)  | Author/validate/export Google's DESIGN.md token spec files.  |
| [**draw-your-font**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-draw-your-font)  | Turn a handwriting photo into an installable TTF font.  |
| [**dream-loop**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-dream-loop)  | Build stunning 3D scenes via a concept-art fidelity loop.  |
| [**excalidraw**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-excalidraw)  | Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).  |
| [**heartmula**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-heartmula)  | HeartMuLa: Suno-like song generation from lyrics + tags.  |
| [**hyperframes**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-hyperframes)  | Render MP4/WebM videos from HTML compositions.  |
| [**impeccable**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-impeccable)  | Frontend design guidance, upstream-maintained (impeccable).  |
| [**ip-as-logo**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-ip-as-logo)  | Design minimal cute IP mascot marks readable at 32px.  |
| [**kanban-video-orchestrator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-kanban-video-orchestrator)  | Plan and run multi-agent video production pipelines.  |
| [**meme-generation**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-meme-generation)  | Create meme PNGs from templates with Pillow text overlay.  |
| [**mono-color**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-mono-color)  | Generate one- or two-ink editorial print poster images.  |
| [**pixel-art**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-pixel-art)  | Pixel art w/ era palettes (NES, Game Boy, PICO-8).  |
| [**pretext**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-pretext)  | Build creative browser demos with DOM-free text layout.  |
| [**simple-english**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-simple-english)  | Rewrite text to ASD-STE100 Simplified Technical English.  |
| [**sketch**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-sketch)  | Throwaway HTML mockups: 2-3 design variants to compare.  |
| [**social-media-content-calendar**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-social-media-content-calendar)  | Plan multi-platform social campaigns: briefs to posting.  |
| [**system-atlas**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-system-atlas)  | Build explorable isometric architecture atlases as HTML.  |
| [**tldraw-offline**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-tldraw-offline)  | Drive and script tldraw offline canvases with an agent.  |
| [**unreal-mcp**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-unreal-mcp)  | Automate Unreal Engine editor scenes, actors, and renders.  |
## data-science
| Skill  | Description  |
| --- | --- |
| [**jupyter-notebook**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/data-science/data-science-jupyter-notebook)  | Iterative Python via live Jupyter kernel (hamelnb).  |
## devops
| Skill  | Description  |
| --- | --- |
| [**actual-setup**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-actual-setup)  | Set up Actual Computer (actual.inc) inference in Hermes.  |
| [**docker-management**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management)  | Manage Docker containers, images, volumes, and Compose.  |
| [**hermes-s6-container-supervision**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-hermes-s6-container-supervision)  | Modify or debug s6 services in the Hermes Docker image.  |
| [**inference-sh-cli**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-inference-sh-cli)  | Run 150+ AI apps (image, video, LLM) via inference.sh CLI.  |
| [**pinggy-tunnel**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-pinggy-tunnel)  | Zero-install localhost tunnels over SSH via Pinggy.  |
| [**setup-wizard-generator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-setup-wizard-generator)  | Generate a bash wizard guiding a human through manual setup.  |
| [**watchers**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-watchers)  | Poll RSS, JSON APIs, and GitHub with watermark dedup.  |
## dogfood
| Skill  | Description  |
| --- | --- |
| [**adversarial-ux-test**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/dogfood/dogfood-adversarial-ux-test)  | Roleplay a hostile user to find and triage UX pain points.  |
## email
| Skill  | Description  |
| --- | --- |
| [**agentmail**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/email/email-agentmail)  | Use when an agent needs AgentMail CLI email inboxes.  |
## finance
| Skill  | Description  |
| --- | --- |
| [**3-statement-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-3-statement-model)  | Build integrated IS/BS/CF financial workbooks in Excel.  |
| [**comps-analysis**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-comps-analysis)  | Build comparable-company valuation workbooks in Excel.  |
| [**dcf-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-dcf-model)  | Build discounted cash flow valuation workbooks in Excel.  |
| [**excel-author**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-excel-author)  | Build auditable financial workbooks headless via openpyxl.  |
| [**lbo-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-lbo-model)  | Build leveraged buyout workbooks with IRR/MOIC in Excel.  |
| [**merger-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-merger-model)  | Build M&A accretion/dilution workbooks in Excel.  |
| [**polymarket**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-polymarket)  | Query Polymarket: markets, prices, orderbooks, history.  |
| [**pptx-author**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-pptx-author)  | Build PowerPoint decks headless with python-pptx.  |
| [**stocks**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-stocks)  | Stock quotes, history, search, compare, crypto via Yahoo.  |
## gaming
| Skill  | Description  |
| --- | --- |
| [**minecraft-modpack-server**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/gaming/gaming-minecraft-modpack-server)  | Host modded Minecraft servers (CurseForge, Modrinth).  |
| [**pokemon-player**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/gaming/gaming-pokemon-player)  | Play Pokemon via headless emulator + RAM reads.  |
## health
| Skill  | Description  |
| --- | --- |
| [**fitness-nutrition**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/health/health-fitness-nutrition)  | Workout planning, macros, and body metrics via wger/USDA.  |
| [**neuroskill-bci**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/health/health-neuroskill-bci)  | Use live BCI cognitive and mood state from NeuroSkill.  |
## mcp
| Skill  | Description  |
| --- | --- |
| [**fastmcp**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mcp/mcp-fastmcp)  | Build, test, and deploy Python MCP servers.  |
| [**mcp-oauth-remote-gateway**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mcp/mcp-mcp-oauth-remote-gateway)  | Manual OAuth for remote MCP servers on headless gateways.  |
| [**mcporter**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mcp/mcp-mcporter)  | List, auth, and call MCP servers/tools from the terminal.  |
## media
| Skill  | Description  |
| --- | --- |
| [**gif-search**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/media/media-gif-search)  | Search/download GIFs from Tenor via curl + jq.  |
| [**songsee**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/media/media-songsee)  | Audio spectrograms/features (mel, chroma, MFCC) via CLI.  |
## mlops
| Skill  | Description  |
| --- | --- |
| [**accelerate**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-accelerate)  | Run PyTorch training across GPUs with minimal changes.  |
| [**axolotl**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-training-axolotl)  | Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO).  |
| [**chroma**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-chroma)  | Embedding database for RAG and semantic search.  |
| [**dspy**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-research-dspy)  | DSPy: declarative LM programs, auto-optimize prompts, RAG.  |
| [**evaluating-llms-harness**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-evaluation-evaluating-llms-harness)  | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).  |
| [**faiss**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-faiss)  | Fast vector similarity search at billion scale.  |
| [**flash-attention**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-flash-attention)  | Speed up long-sequence transformer training and inference.  |
| [**lambda-labs**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-lambda-labs)  | On-demand GPU cloud instances for ML training.  |
| [**llama-cpp**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-llama-cpp)  | llama.cpp local GGUF inference + HF Hub model discovery.  |
| [**modal**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-modal)  | Serverless GPU cloud for ML jobs and model APIs.  |
| [**nemo-curator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-nemo-curator)  | Curate LLM training data: dedupe, filter, PII redaction.  |
| [**obliteratus**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-obliteratus)  | OBLITERATUS: abliterate LLM refusals (diff-in-means).  |
| [**peft**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-peft)  | Fine-tune large LLMs with LoRA on limited GPU memory.  |
| [**pytorch-fsdp**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pytorch-fsdp)  | Fully sharded data-parallel training for large models.  |
| [**pytorch-lightning**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pytorch-lightning)  | Clean training loops with built-in distributed support.  |
| [**saelens**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-saelens)  | Train sparse autoencoders to interpret model features.  |
| [**segment-anything-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-models-segment-anything-model)  | SAM: zero-shot image segmentation via points, boxes, masks.  |
| [**serving-llms-vllm**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-inference-serving-llms-vllm)  | vLLM: high-throughput LLM serving, OpenAI API, quantization.  |
| [**simpo**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo)  | Reference-free preference alignment, simpler than DPO.  |
| [**slime**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-slime)  | RL post-training for LLMs with Megatron and SGLang.  |
| [**tensorrt-llm**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-tensorrt-llm)  | High-throughput LLM inference on NVIDIA GPUs.  |
| [**torchtitan**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-torchtitan)  | Pretrain LLMs at scale with PyTorch 4D parallelism.  |
| [**unsloth**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-training-unsloth)  | Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM.  |
## payments
| Skill  | Description  |
| --- | --- |
| [**stripe-link-cli**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/payments/payments-stripe-link-cli)  | Agent payments via Stripe Link — cards, SPT, approvals.  |
| [**stripe-projects**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/payments/payments-stripe-projects)  | Provision SaaS services + sync creds via Stripe Projects.  |
## productivity
| Skill  | Description  |
| --- | --- |
| [**box**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-box)  | Box manages cloud files, sharing, search, and metadata.  |
| [**canvas**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-canvas)  | Fetch Canvas LMS courses and assignments via API token.  |
| [**decision-questionnaire**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-decision-questionnaire)  | Turn an unanswerable decision into a questionnaire doc.  |
| [**here-now**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-here-now)  | Publish sites to {slug}.here.now and store files in Drives.  |
| [**live-dashboard**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-live-dashboard)  | Build self-updating dashboards from live sources.  |
| [**memento-flashcards**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards)  | Spaced-repetition flashcards: create, review, quiz, export.  |
| [**property-listings**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-property-listings)  | Present property and rental listings as desktop cards.  |
| [**shop**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-shop)  | Shop catalog search, checkout, order tracking, returns.  |
| [**siyuan**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-siyuan)  | Query and edit a SiYuan knowledge base via its API.  |
| [**telephony**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-telephony)  | Provision Twilio numbers, SMS/MMS, and AI outbound calls.  |
## research
| Skill  | Description  |
| --- | --- |
| [**bioinformatics**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-bioinformatics)  | Gateway to 400+ genomics and computational biology skills.  |
| [**blogwatcher**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-blogwatcher)  | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.  |
| [**darwinian-evolver**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-darwinian-evolver)  | Evolve prompts/regex/SQL/code with Imbue's evolution loop.  |
| [**domain-intel**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-domain-intel)  | Passive recon of subdomains, SSL certs, WHOIS, and DNS.  |
| [**drug-discovery**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-drug-discovery)  | Drug discovery: ChEMBL search, drug-likeness, interactions.  |
| [**gitnexus-explorer**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-gitnexus-explorer)  | Serve an interactive codebase knowledge graph web UI.  |
| [**llm-wiki**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-llm-wiki)  | Karpathy's LLM Wiki: build/query interlinked markdown KB.  |
| [**osint-investigation**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-osint-investigation)  | Follow the money via public records and sanctions data.  |
| [**parallel-cli**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-parallel-cli)  | Agent-native web search, deep research, and enrichment.  |
| [**qmd**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-qmd)  | Hybrid local search over notes, docs, and transcripts.  |
| [**research-paper-writing**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-research-paper-writing)  | Write ML papers for NeurIPS/ICML/ICLR: design→submit.  |
| [**rss-feeds**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-rss-feeds)  | Read RSS, Atom, JSON feeds; discover feeds behind a page.  |
| [**scrapling**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-scrapling)  | Scrape sites with stealth browsing and Cloudflare bypass.  |
## security
| Skill  | Description  |
| --- | --- |
| [**1password**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-1password)  | Set up op CLI, sign in, and read or inject secrets.  |
| [**godmode**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-godmode)  | Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.  |
| [**oss-forensics**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-oss-forensics)  | GitHub supply-chain forensics: recovery, IOCs, reporting.  |
| [**sherlock**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-sherlock)  | Find accounts for a username across 400+ platforms.  |
| [**unbroker**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-unbroker)  | Remove your info from data-broker sites, by name or phone.  |
| [**web-pentest**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-web-pentest)  | Authorized web pentest: recon, proof-based exploits, report.  |
## smart-home
| Skill  | Description  |
| --- | --- |
| [**openhue**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/smart-home/smart-home-openhue)  | Control Philips Hue lights, scenes, rooms via OpenHue CLI.  |
## social-media
| Skill  | Description  |
| --- | --- |
| [**reddit-reading**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/social-media/social-media-reddit-reading)  | Read Reddit: subreddits, search, threads, users. No browser.  |
## software-development
| Skill  | Description  |
| --- | --- |
| [**ast-grep**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-ast-grep)  | AST-aware structural code search and rewrite via ast-grep.  |
| [**code-wiki**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-code-wiki)  | Generate wiki docs + Mermaid diagrams for any codebase.  |
| [**grill-me**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-grill-me)  | Adversarial plan interview before implementation.  |
| [**hermes-agent-skill-authoring**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-hermes-agent-skill-authoring)  | Author in-repo SKILL.md files: frontmatter and structure.  |
| [**inspecting-hermes-desktop-dom**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-inspecting-hermes-desktop-dom)  | Read the live Hermes desktop DOM/CSS over CDP.  |
| [**node-inspect-debugger**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-node-inspect-debugger)  | Debug Node.js via --inspect + Chrome DevTools Protocol CLI.  |
| [**pr-lens**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-pr-lens)  | Draw code changes as animated architecture/data-flow SVGs.  |
| [**python-debugpy**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-python-debugpy)  | Debug Python: pdb REPL + debugpy remote (DAP).  |
| [**rest-graphql-debug**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-rest-graphql-debug)  | Debug REST/GraphQL APIs: status codes, auth, schemas, repro.  |
| [**subagent-driven-development**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-subagent-driven-development)  | Execute plans via delegate_task subagents (2-stage review).  |
## web-development
| Skill  | Description  |
| --- | --- |
| [**cloudflare-temporary-deploy**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/web-development/web-development-cloudflare-temporary-deploy)  | Deploy a Worker live, no account, via wrangler --temporary.  |
| [**har-derived-api-client**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/web-development/web-development-har-derived-api-client)  | Record a site's XHR into a HAR, derive an HTTP client.  |
| [**page-agent**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/web-development/web-development-page-agent)  | Embed an in-page natural-language GUI copilot in web apps.  |
| [**publish-site**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/web-development/web-development-publish-site)  | Versioned site deploys to GitHub/Cloudflare/Netlify Pages.  |
| [**scrollcraft**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/web-development/web-development-scrollcraft)  | Premium scroll-driven landing pages; scroll = timeline.  |
* * *
## Contributing Optional Skills
To add a new optional skill to the repository:
  1. Create a directory under `optional-skills/<category>/<skill-name>/`
  2. Add a `SKILL.md` with standard frontmatter (name, description, version, author)
  3. Include any supporting files in `references/`, `templates/`, or `scripts/` subdirectories
  4. Submit a pull request — the skill will appear in this catalog and get its own docs page once merged
