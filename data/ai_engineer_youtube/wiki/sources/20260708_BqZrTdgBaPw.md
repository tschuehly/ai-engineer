# Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG

Source: [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](https://www.youtube.com/watch?v=BqZrTdgBaPw)
Uploaded: 2026-07-08
Transcript: `raw/20260708_BqZrTdgBaPw/BqZrTdgBaPw.en-orig.vtt`

## Summary

Stephan Steinfurt (TNG, Munich) presents a fully automated pipeline that produces daily chess-puzzle explainer videos and uploads them to YouTube unattended. The framing is a classic two-sided gap: chess *engines* have been superhuman for decades but "can't really explain chess well," while LLMs "can describe things but can't play chess well," so the whole system is an agent that bridges them — an LLM (Gemini 3.1 Pro, "the best model I've seen so far on chess") given a toolbox that grounds it in engine ground truth: a legal-moves tool (so it never reasons about an illegal move), a full playable board to try and take back variations, an on-demand chess engine for evaluation, a "checks, captures and threats" beginner-heuristic tool, a rating-conditioned human-move model (Maia, University of Toronto), and web search for historical game context. A deliberate design insight is that *conflicting* information from these tools is beneficial: the agent should not only surface the single best move but describe plausible-but-bad human moves and why they fail. The team moved the analysis *from* pre-written Python scripts *into* the reasoning agent once reasoning models arrived. Output is an intermediate structured format rendered to video, narrated with ElevenLabs V3 (audio tags like `[excited]`), with the agent itself choosing which squares to highlight, which arrows to draw, and whether a move is "brilliant." Operationally: ~20-30 cents/video (euros for long ones), ~1-in-20 error rate (e.g. a missed checkmate, usually a skipped final tool call), and a QA stance drifting from watch-each-first to "I don't care anymore… take it down afterwards." Anti-slop positioning: no artificial engagement gimmicks (exploding kings); optimize for chess quality and personalize commentary of ordinary players' games that streamers like GothamChess would never cover (~500k views, 4k+ subscribers, most within the last month; not yet monetized).

## Extracted Concepts

- [Pair an LLM Narrator With a Domain Solver Via Tools](../concepts/pair-an-llm-narrator-with-a-domain-solver-via-tools.md) - engines play but can't explain, LLMs explain but can't play, so the agent's tools expose the engine's ground truth and the LLM narrates.
- [Feed Agents Diverse and Conflicting Tool Signals to Broaden Exploration](../concepts/feed-agents-diverse-and-conflicting-tool-signals-to-broaden-exploration.md) - best move + human-likely move (Maia) + checks/captures/threats gives the agent diversity to explore and explain wrong moves, not just the optimum.
- [Automate a Nightly Generate-and-Publish Media Pipeline With Sampled QA](../concepts/automate-a-nightly-generate-and-publish-media-pipeline-with-sampled-qa.md) - source data → agent analysis → structured format → rendered narrated video → auto-upload, managed by publish-then-take-down QA at ~1-in-20 error rate.

## Topic Links

- [Tools](../topics/tools.md)
- [Generative Media](../topics/generative-media.md)
- [Workflows](../topics/workflows.md)

## Notes

- The core problem framing (04:44-05:04): "we've had really good chess engines for multiple decades… but they can't really explain chess well. On the other hand, we now have LLMs… they can describe things, but they can't play chess well. So we have to somehow combine them."
- Model choice (05:17-05:38): Gemini 3.1 Pro is "the best model I've seen so far on chess," visible in its reasoning traces (likely in-depth post-training). The autumn-prior best was "surprisingly" Grok 4; OpenAI models also carry "decent base chess knowledge" enough to call tools at the right positions.
- Tools (05:43-06:20): legal-moves tool ("prevent it from ever thinking about something completely illegal"), a full board it can play/take-back moves and explore variations on, an on-demand chess engine, a "checks, captures and threats" tool (a well-known beginner heuristic), and web search for historic game context.
- Conflicting signals are beneficial (06:22-08:03, 09:05-09:44): the checks/captures/threats tool surfaces reasonable-looking checks that are actually bad, giving "diversity to the agent to explore other variations" and to "describe which ones are actually bad because a human might think about them" — "it's not always about the very very best move."
- "Who should do the thinking" (08:06-09:04): the project started as Python scripts that assembled position facts (check moves, engine eval) and passed them to the LLM to narrate; when reasoning models arrived the agents "could rather think themselves about the positions," so analysis moved into the agent while tools stay for grounding.
- Human-move modeling (14:15-15:10): the Maia engine (University of Toronto) is rating-conditioned — feed a player rating and it predicts a move that player might play; used as one of several signals to balance description toward human-relevant moves rather than only engine-optimal ones, and to target videos by audience strength (a mate-in-one is trivial for strong players, valuable for beginners).
- Rendering (09:46-10:22): analysis → a special intermediate format → video; ElevenLabs V3 for TTS with audio tags (`[excited]`); the agent decides highlighted squares, drawn arrows, and brilliant-move flags.
- Economics/QA (12:10-14:01): ~20-30 cents/video (euros for much longer ones), not cost-optimized on purpose ("we rather want to error on having too good a description"); redundant tool calls (going through a game twice) are a known waste; ~1-in-20 videos has a weird description (e.g. a missed checkmate) usually from a skipped final tool call; QA stance shifting from watch-each-first to "I don't care anymore… take it down afterwards."
- Positioning (10:24-11:41): input is real human games, so the product could make videos of "your games" to send to friends/family — scaling personalized commentary to non-elite players that a streamer (GothamChess) would never cover; anti-slop stance of not adding artificial engagement gimmicks (exploding kings on checkmate) and optimizing for chess quality.
