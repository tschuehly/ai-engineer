# Benchmark Context-Management Presets Against a Do-Nothing Baseline

Summary: Context-management techniques are usually adopted because they sound sensible, not because they were measured. Running each one as a named preset against an untouched-history control, on real user data and with everything else held fixed, is cheap enough to do and routinely overturns the defaults — in Towards AI's bake-off, doing nothing beat every compaction technique and beat their own shipped production defaults on recall, cost, and latency at the same time.

Use when:
- A team is about to ship (or has already shipped) summarization, trimming, or tool-output clearing on intuition.
- Deciding whether a context change is worth its complexity, or which technique to keep.
- Designing an eval harness for context engineering rather than for model quality.

Details:
- The setup that makes results comparable: define a **preset** (one full configuration), a **task** (a dataset shape), a **run** (one preset on one task), and a **bundle** (the JSON of metrics written to disk), then vary only the preset while model, prompt, tools, and dataset stay fixed. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 36:23-37:20, 42:25-43:20)
- Include a **do-nothing control**. Their 11 presets were full history (touch nothing), production (the shipped defaults), and six techniques including sliding window, prompt compression, and selective retention. Without the control there is no way to learn that the whole category is a loss. (42:25-43:20)
- Two task shapes are needed because they separate different failures: single-turn question/answer, and multi-turn sessions with a planted fact, filler messages, and a probe whose correct answer requires recalling the planted fact. (37:24-40:57)
- **Single-turn tasks cannot distinguish context presets.** Nearly every technique scored high there, because one turn never accumulates enough tokens to fire the thresholds. If your eval is single-turn, you are measuring nothing about compaction. (44:49-45:27)
- Add a **gate check** that asserts the technique under test actually fired — did summarization happen at all — and only save the run if it did. Otherwise a preset can "win" because it silently never engaged. (40:57-41:15, 41:38-42:05)
- Grade with a mix: a code check for what is mechanically verifiable (was the correct lesson retrieved) and an LLM judge for answer content. Keep running and grading separable so a single expensive run can be re-graded. (38:24-39:10, 41:18-42:25)
- Cost control worth copying: use a Claude Code or Codex *subscription* for LLM-as-judge grading rather than the APIs, "because it's cheaper than using the APIs." Their bake-off still cost over $500 (later stated as almost $600), which is what pushed the follow-up experiments onto cheaper models. (38:53-39:10, 43:19-43:29, 47:10-47:35)
- Use real user data where possible. Their single-turn set was real student questions scraped from the staff-answer site by Codex, then cleaned to 60 pairs with stale-library and duplicate questions dropped — no synthetic generation except for the filler in the multi-turn sessions. (37:24-38:24)
- The headline result: full history won on recall over multiple turns, the shipped production defaults (clear tool outputs after 5,000 tokens keeping the last 5; summarize after 30,000 tokens keeping the last 20 messages) scored *worse than doing nothing*, and doing nothing was simultaneously cheaper and faster. Production cost was ~50 cents per single turn and ~24 cents per multi-turn turn, with multi-turn quality degrading to 38%. (32:19-33:30, 43:40-45:57)
- Honest statistical caveat from the presenters: one trial and two trials is thin, so the signal they trust is "the order in which the techniques ended up being in the table," not the individual numbers. The dataset was also 11-13 turns, which they call "not huge." (44:19-44:42, 46:41-46:58)
- The decision rule they land on generalizes past their tutor: "do not compact by default. You have to name the constraint that you have and then look for a better alternative." Cost, window size, and latency are different constraints with different answers. (61:34-61:47)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Measure Agentic Knowledge-Base Browsing Before Adding It](measure-agentic-knowledge-base-browsing-before-adding-it.md)
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Context window editing clears stale tool results](context-window-editing-clears-stale-tool-results.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 32:19-33:30, 36:23-47:35, 61:34-61:47
