# Automate a Nightly Generate-and-Publish Media Pipeline With Sampled QA

Summary: A personalized media channel can run unattended — pull source data on a schedule, have an agent analyze it, emit a structured intermediate format, render that to a narrated video, and auto-upload — and its low residual error rate is managed by publish-then-take-down sampling rather than pre-reviewing every asset.

Use when:
- You can generate far more media than you can hand-review, and each item is derived from a data source (games, records, events) rather than authored from scratch.
- You want to scale personalized content into a long tail that human creators won't cover (an individual's own games, niche records).
- The per-item error rate is low and errors are recoverable (a bad upload can be taken down), so blocking every asset on human review is the wrong tradeoff.

Details:
- Pipeline shape: download source data nightly (chess games from lichess), analyze in the background, run the agent for deeper analysis, emit "some special format" as an intermediate artifact, render it to video, and upload to YouTube — "it's all automated."
- Separate analysis from rendering with a structured intermediate format: the agent's job ends at a machine-readable description ("a special format which we could then easily transfer into a video"), and the video renderer consumes that, so the reasoning and the media production are decoupled stages.
- The agent owns presentation decisions, not just content: it "decides by itself which squares it wants to highlight, which arrows it wants to draw, and if something should be considered a brilliant move or not."
- Narration stack: ElevenLabs V3 for text-to-speech, using audio tags (put `[excited]` in the text and "it would then sound excited") so emotional delivery is part of the generated script rather than post-production.
- Economics: ~20-30 cents per short video, up to euros for much longer ones; cost is deliberately *not* optimized ("we rather want to error on having too good a description"), with known waste from redundant tool calls (the agent sometimes walks a game twice).
- QA by sampling, not gating: error rate is ~1-in-20 (a weird description, e.g. a missed checkmate, usually from a skipped final tool call). The stance drifts from watch-each-video-first toward "I don't care anymore… take it down afterwards" — trust the pipeline, treat mistakes as recoverable and as learning signal, rather than pre-reviewing everything.
- Positioning: input is real human games, so the product can generate a video of *your* game to share — scaling personalized commentary to ordinary players a streamer (GothamChess) would never cover. Anti-slop discipline: refuse artificial engagement gimmicks (exploding kings on checkmate) that would lift view count, and optimize for domain quality instead (~500k views, 4k+ subscribers, most within a month; not yet monetized).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Pair an LLM Narrator With a Domain Solver Via Tools](pair-an-llm-narrator-with-a-domain-solver-via-tools.md)
- [Design AI creative systems for generated-asset retrieval](design-ai-creative-systems-for-generated-asset-retrieval.md)
- [Ground generated media with current search context](ground-generated-media-with-current-search-context.md)

Sources:
- [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../sources/20260708_BqZrTdgBaPw.md), 04:05-04:36, 09:46-13:59
