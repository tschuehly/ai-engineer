# Drive Game NPCs and Difficulty With Runtime LLMs

Summary: A runtime LLM running *during* play — not just at build time — can drive NPC behavior and direct the game as a living entity, producing emergent unscripted action and a "game master" that personalizes difficulty per player. This makes each playthrough unique and non-repeatable, and is newly viable only because inference is now fast and cheap enough.

Use when:
- Designing a game (or any interactive experience) where you want emergent, non-repeatable behavior instead of scripted logic.
- Deciding whether to spend inference at runtime to personalize difficulty, pacing, or NPC personality per player rather than fixing it at design time.
- Weighing the new "runtime LLM" genre against traditional deterministic game code.

Details:
- Frame the runtime LLM as a living entity that modifies, changes, and directs the game while the user plays, rather than only generating content up front. (08:30-08:51)
- Meta built a multiplayer game where each NPC is *entirely* LLM-driven: you give it a personality (thief, honorable, fast) and it independently pursues the goal (collect cubes) while choosing to steal, block, or kick rivals — "entirely not scripted... runtime LLM-driven decision-making" — which adds dynamic-ness so every game is unique and non-repeatable. (08:54-10:10)
- This genre was not previously buildable by the industry; it became possible in roughly the last 18 months because inference is fast enough and models are cheap enough, and the demo was built over a couple of days. (10:31-10:47)
- A "game master" personalizes difficulty: for a coordination-challenged player who always tanks the co-op team, the LLM can adjust so they keep playing with friends and still have fun — a personalization previously not possible. (12:02-12:37)
- Runtime personalization generalizes: with AI you can steer any game toward anything a player wants (e.g. a themed "Labubu" universe). (15:54-16:12)
- Caveat: the technology itself does not make the product better — teams are still early in exploring how to use runtime LLMs, and the fully open-ended Star Trek vision ("imagine a forest, now I'm hunting bears") is coming but not today's reality. (12:39-13:20)
- Caveat at platform scale: runtime LLMs generating images/content raise a token-economy profitability question across creators/players/platform and a content-safety question (keeping generated content safe for the audience). (16:15-17:32)

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)
- [Feed Agents Diverse and Conflicting Tool Signals to Broaden Exploration](feed-agents-diverse-and-conflicting-tool-signals-to-broaden-exploration.md)

Sources:
- [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../sources/20260708_grdoOC1BT1s.md), 08:30-17:32
