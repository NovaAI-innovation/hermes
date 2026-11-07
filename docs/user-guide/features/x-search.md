---
title: "X (Twitter) Search"
source: https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search
scraped_at: 2026-11-07T17:19:48.630047+00:00
success: True
status_code: 200
---

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#__docusaurus_skipToContent_fallback)
[ ![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo.png)![Hermes Agent](https://hermes-agent.nousresearch.com/docs/img/logo-dark.png) **Hermes Agent**](https://hermes-agent.nousresearch.com/docs/)[Docs](https://hermes-agent.nousresearch.com/docs/user-stories)[Skills](https://hermes-agent.nousresearch.com/docs/skills)[Plugins](https://hermes-agent.nousresearch.com/docs/plugins)[Download](https://hermes-agent.nousresearch.com/)
[](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search)
  * [English](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search)
  * [简体中文](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/x-search)


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
  * X (Twitter) Search


On this page
# X (Twitter) Search
The `x_search` tool lets the agent search X (Twitter) posts, profiles, and threads directly. It's backed by xAI's built-in `x_search` tool on the Responses API at `https://api.x.ai/v1/responses` — Grok itself runs the search server-side and returns synthesized results with citations to the originating posts.
**Use this instead of`web_search`** when you specifically want current discussion, reactions, or claims **on X**. For general web pages, keep using `web_search` / `web_extract`.
##  `x_search` vs `xurl`[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#x_search-vs-xurl "Direct link to x_search-vs-xurl")
Hermes can expose two different X surfaces:  
| Surface  | Use it for  | Do not use it for  |  
| --- | --- | --- |  
| `x_search`  | Read-only public X discovery: current discussion, reactions, claims, profiles, threads, and synthesized answers with citations.  | Posting, replying, liking, DMs, media upload, deleting, or proving that an authenticated X account changed state.  |  
|  `xurl` skill  | Exact or authenticated X API work: `post`, `reply`, `read`, `like`, `dm`, timelines, mentions, media upload, account-specific reads, and raw v2 endpoints.  | Broad Grok-synthesized public X research when `x_search` is available and no authenticated account context is needed.  |  
For mixed workflows, use `x_search` to discover candidate public posts, then switch to `xurl read` or another exact `xurl` command after the target post/user/action is clear. Any state-changing X action must be confirmed by `xurl` output or the X API response; an `x_search` answer is never evidence that a write happened.
If you're paying Portal for an xAI model anyway, Live Search calls bill against the same xAI key configured for chat. See [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).
## Authentication[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#authentication "Direct link to Authentication")
`x_search` registers when **either** xAI credential path is available:  
| Credential  | Source  | Setup  |  
| --- | --- | --- |  
| **SuperGrok / X Premium+ OAuth**  | Browser login at `accounts.x.ai`, refreshed automatically  |  `hermes auth add xai-oauth` — see [xAI Grok OAuth (SuperGrok / X Premium+)](https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth)  |  
|  **`XAI_API_KEY`**(preferred)  | Paid xAI API key  | Set in `~/.hermes/.env`  |  
Both hit the same endpoint with the same payload — the only difference is the bearer token. **When both are configured, the explicit`XAI_API_KEY` wins** — the subscription OAuth bearer authorizes `/v1/responses` but answers x_search in a degraded Grok explanatory mode with no citations, while the API key returns real posts. Note this means x_search runs against metered API billing when a key is set; remove `XAI_API_KEY` to fall back to your subscription quota (with the degraded-answer caveat).
The tool's `check_fn` runs the xAI credential resolver every time the model's tool list is rebuilt. A `True` return means the bearer is fetchable AND non-empty AND (if it had expired) successfully refreshed. Revoked tokens with a failed refresh hide the tool from the schema; the model simply can't see it.
## Enabling the tool[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#enabling-the-tool "Direct link to Enabling the tool")
Auto-enables when xAI credentials (OAuth token or `XAI_API_KEY`) are present. Disable explicitly via `hermes tools` → Search → x_search if you don't want this.

```


hermes tools  





# → 🐦 X (Twitter) Search   (press space to toggle on)  



```

The picker offers two credential choices:
  1. **xAI Grok OAuth (SuperGrok / Premium+)** — opens the browser to `accounts.x.ai` if you're not already logged in
  2. **xAI API key** — prompts for `XAI_API_KEY`


Either choice satisfies the gating. You can pick whichever credentials you already have; the tool works identically with both. If both end up configured, OAuth is preferred at call time.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#configuration "Direct link to Configuration")

```


# ~/.hermes/config.yaml  





x_search:  





  # xAI model used for the Responses call.  





  # grok-4.5 is the recommended default; any Grok model  





  # with x_search tool access works.  





  model: grok-4.5  





  





  # Optional reasoning effort: low, medium, high, or xhigh. When omitted,  





  # the selected model's default applies. xhigh is supported only by  





  # models that document it, such as grok-4.20-multi-agent.  





  # reasoning_effort: low  





  





  # Request timeout in seconds. x_search can take 60–120s for  





  # complex queries — the default is generous. Minimum: 30.  





  timeout_seconds: 180  





  





  # Number of automatic retries on 5xx / ReadTimeout / ConnectionError.  





  # Each retry backs off (1.5x attempt seconds, capped at 5s).  





  retries: 2  



```

`reasoning_effort` is sent to the xAI Responses API as `reasoning: {effort: ...}`. Leave it unset for models that do not support configurable reasoning. Invalid values fail before an API request is made.
## Tool parameters[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#tool-parameters "Direct link to Tool parameters")
The agent calls `x_search` with these arguments:  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| `query`  | string (required)  | What to look up on X.  |  
| `allowed_x_handles`  | string array  | Optional list of handles to include **exclusively** (max 10). Leading `@` is stripped.  |  
| `excluded_x_handles`  | string array  | Optional list of handles to exclude (max 10). Mutually exclusive with `allowed_x_handles`.  |  
| `from_date`  | string  | Optional `YYYY-MM-DD` start date.  |  
| `to_date`  | string  | Optional `YYYY-MM-DD` end date.  |  
| `enable_image_understanding`  | boolean  | Ask xAI to analyze images attached to matching posts.  |  
| `enable_video_understanding`  | boolean  | Ask xAI to analyze videos attached to matching posts.  |  
The tool returns JSON with:
  * `answer` — synthesized text response from Grok
  * `citations` — citations returned by the Responses API top-level field
  * `inline_citations` — `url_citation` annotations extracted from the message body (each with `url`, `title`, `start_index`, `end_index`)
  * `degraded` — `true` when any narrowing filter (`allowed_x_handles`, `excluded_x_handles`, `from_date`, `to_date`) was set AND both citation channels came back empty. In that case the `answer` was synthesized from the model's own knowledge rather than the X index, so treat it as unsourced. `false` otherwise (including the "no filters set" case — a broad unsourced answer is just an answer, not a filter miss)
  * `degraded_reason` — short string naming which filters were active, or `null` when `degraded` is `false`
  * `credential_source` — `"xai-oauth"` if OAuth resolved, `"xai"` if API key resolved
  * `model`, `query`, `provider`, `tool`, `success`


### Date validation[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#date-validation "Direct link to Date validation")
`from_date` / `to_date` are validated client-side before the HTTP call:
  * Both, if provided, must parse as `YYYY-MM-DD`.
  * When both are set, `from_date` must be on or before `to_date`.
  * `from_date` must not be later than today UTC — no posts can exist in a window that hasn't started yet, so the call would be guaranteed to return zero citations.
  * `to_date` in the future is allowed (callers may legitimately request "from yesterday to tomorrow" to catch posts as they arrive).


Validation failures surface as a structured `{"error": "..."}` tool result, never as an HTTP call to xAI.
## Example[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#example "Direct link to Example")
Talking to the agent:
> What are people on X saying about the new Grok image features? Focus on responses from @xai.
The agent will:
  1. Call `x_search` with `query="reactions to new Grok image features"`, `allowed_x_handles=["xai"]`
  2. Get back a synthesized answer plus a list of citations linking to specific posts
  3. Reply with the answer and references


If the next user request is "reply to the best one" or "like that post", the agent should switch to the `xurl` skill, confirm the exact target post, and use the X API action. `x_search` remains a discovery tool.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#troubleshooting "Direct link to Troubleshooting")
### "No xAI credentials available"[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#no-xai-credentials-available "Direct link to "No xAI credentials available"")
The tool surfaces this when both auth paths fail. Either set `XAI_API_KEY` in `~/.hermes/.env` or run `hermes auth add xai-oauth` and complete the browser login. Then restart your session so the agent re-reads the tool registry.
### "`x_search` is not enabled for this model"[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#x_search-is-not-enabled-for-this-model "Direct link to x_search-is-not-enabled-for-this-model")
The configured `x_search.model` doesn't have access to the server-side `x_search` tool. Switch to `grok-4.5` (the default) or another Grok model that supports it. Check the [xAI documentation](https://docs.x.ai/) for the current list.
### Tool doesn't appear in the schema[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#tool-doesnt-appear-in-the-schema "Direct link to Tool doesn't appear in the schema")
Two possible causes:
  1. **Toolset not enabled.** Run `hermes tools` and confirm `🐦 X (Twitter) Search` is checked.
  2. **No xAI credentials.** The check_fn returns False, so the schema stays hidden. Run `hermes auth status` to confirm xai-oauth login state, and check that `XAI_API_KEY` is set (if you're using the API-key path).


###  `degraded: true` — answer with no citations[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#degraded-true--answer-with-no-citations "Direct link to degraded-true--answer-with-no-citations")
When you used `allowed_x_handles`, `excluded_x_handles`, or a date range and the response comes back with `degraded: true`, xAI's X index returned no matching posts but Grok still produced a synthesized answer from its own training data. The answer is unsourced — do not treat it as a real X result.
Causes worth checking:
  * **Typo in the handle.** Strip the `@`, double-check spelling, and confirm the account exists.
  * **Date range too narrow** or sliding past today's posts; widen and retry.
  * **xAI index gap.** Some active accounts intermittently fail to surface in `x_search` even when they post regularly. Retry after a few minutes, or use the `xurl` skill for direct X API reads when you need an exact handle's timeline.


## See Also[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#see-also "Direct link to See Also")
  * [xAI Grok OAuth (SuperGrok / Premium+)](https://hermes-agent.nousresearch.com/docs/guides/xai-grok-oauth) — the OAuth setup guide
  * [xurl skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/social-media/social-media-xurl) — official X API CLI for authenticated account actions
  * [Web Search & Extract](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search) — for general (non-X) web search
  * [Tools Reference](https://hermes-agent.nousresearch.com/docs/reference/tools-reference) — full tool catalog


[](https://github.com/NousResearch/hermes-agent/edit/main/website/docs/user-guide/features/x-search.md)
[Previous Web Search](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search)[Next Browser](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser)
  * [`x_search` vs `xurl`](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#x_search-vs-xurl)
  * [Authentication](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#authentication)
  * [Enabling the tool](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#enabling-the-tool)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#configuration)
  * [Tool parameters](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#tool-parameters)
    * [Date validation](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#date-validation)
  * [Example](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#example)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#troubleshooting)
    * ["No xAI credentials available"](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#no-xai-credentials-available)
    * ["`x_search` is not enabled for this model"](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#x_search-is-not-enabled-for-this-model)
    * [Tool doesn't appear in the schema](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#tool-doesnt-appear-in-the-schema)
    * [`degraded: true` — answer with no citations](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#degraded-true--answer-with-no-citations)
  * [See Also](https://hermes-agent.nousresearch.com/docs/user-guide/features/x-search#see-also)


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
