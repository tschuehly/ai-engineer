# Pair an LLM Narrator With a Domain Solver Via Tools

Summary: When a domain already has a superhuman-but-inarticulate solver and you want natural-language explanation, don't ask the LLM to compute the answer — give it tools that expose the solver's ground truth and let the LLM narrate over that truth, grounding its action space so it can't reason about invalid states.

Use when:
- You have a strong non-LLM oracle (a game engine, solver, simulator, optimizer, or verifier) but need human-readable explanation, teaching, or commentary.
- An LLM's raw domain competence is weak or unreliable (it "can't play chess well") but its language and reasoning are strong.
- You want to constrain the model's action space so it never reasons about illegal or impossible moves/states.

Details:
- The gap being bridged: "we've had really good chess engines for multiple decades… but they can't really explain chess well. On the other hand, we now have LLMs… they can describe things, but they can't play chess well. So we have to somehow combine them" — the agent's tools are "the main important ingredient."
- Ground the action space with a validity tool. A legal-moves tool exists specifically "to just prevent it from ever thinking about something completely illegal," so the LLM's exploration stays inside the solver's rules rather than hallucinating impossible states.
- Give the LLM a live scratch environment plus an oracle on tap: a full board it can "play moves and take them back and go to various variations itself," an on-demand chess engine for evaluation, and derived signals (checks/captures/threats). The LLM explores; the engine supplies truth.
- The model still matters: a model with strong base domain knowledge (Gemini 3.1 Pro was "the best I've seen so far on chess," visible in its reasoning traces; Grok 4 was the surprise leader a season earlier) calls the tools "at the right position" and assembles the result. Tools ground it; they don't replace domain competence in the model.
- Move the thinking into the reasoning model over time. The project began as Python scripts that assembled position facts (check moves, engine eval) and handed them to the LLM to narrate; once reasoning models arrived, "the agents could rather think themselves about the positions," so analysis migrated from the deterministic pre-processor into the agent while tools remained for grounding.
- Related failure mode: skipping a grounding tool call at the wrong moment produces a confidently wrong narration (~1-in-20 videos miss a checkmate because "one tool call was not done at the very end") — the narration is only as sound as the tool grounding behind it.

Related topics:
- [Tools](../topics/tools.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Feed Agents Diverse and Conflicting Tool Signals to Broaden Exploration](feed-agents-diverse-and-conflicting-tool-signals-to-broaden-exploration.md)
- [Keep Fixed Business Logic Outside the Model](keep-fixed-business-logic-outside-the-model.md)
- [Put Brittle Edge Cases Behind Rigorous Tools](put-brittle-edge-cases-behind-rigorous-tools.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)

Sources:
- [Running a Chess YouTube Channel entirely by AI — Stephan Steinfurt, TNG](../sources/20260708_BqZrTdgBaPw.md), 04:44-09:04
