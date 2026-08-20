# Re-Run One Remembered Hard Task on Each New Model

Summary: Keep one real task you have already solved the hard way, and re-run it whenever a model generation ships. Because you did it yourself, you know what "done" looks like, and the measurement is how much intervention the model needed — hours of back-and-forth, number of corrective iterations, count of mistakes you had to catch — rather than a score. That makes it the cheapest longitudinal capability instrument available, and it sidesteps the scorer problem that blocks larger private benchmarks.

Use when:
- A new model or harness ships and you need a reading on your own work, not a leaderboard.
- Building a private eval and stalling on how to grade replayed attempts.
- Deciding whether the improvement between two model generations is large enough to change how you work.

Details:
- **The instrument is one task, carried across generations.** WiseDocs' recurring benchmark is a single refactor from their pipeline consolidation. With o3, "this refactor took 3 hours of back and forth chatting with [Cursor], but it made 10 major mistakes," and it "was still a very manual process where you had to intervene and actually guide the model and manually edit or delete code." Re-run later: "Sonnet 4.6 with one additional iteration was able to solve the task. And with Opus [4.8], it was basically able to one-shot this problem." The headline result is a ratio on effort — rebuilding the same task now "would take around 1/5 of the time to accomplish." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 05:20-06:48)
- **Why it needs no scorer.** The unit of measurement is human intervention: hours of back-and-forth, iterations required, major mistakes caught. All three are observable by the person running the task, and all three are exactly what a scoring rubric struggles to capture. This is the missing half of [Replay Your Own Merged PRs as the Coding-Agent Benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md), whose acknowledged hard part is how to judge a replayed attempt against the original — diff similarity punishes a better solution, the original tests may pass trivially, and an LLM judge reintroduces the model grading the model. An N-of-1 task you personally solved dissolves that problem by putting a competent human in the loop as the grader, at the cost of everything statistical.
- **The two benchmarks answer different questions and should both exist.** PR replay is a corpus, run cross-sectionally across harnesses at one moment, to move a team default. This is a single remembered task, run longitudinally across model releases, to update one engineer's operating model of what can be delegated. Neither substitutes for the other: a corpus cannot tell you how much easier your hardest problem got, and one task cannot rank three vendors.
- **The second reading is the shape of the trajectory, not the outcome.** "Before with O3, there weren't substantial tool calls on certain categories. And then as we moved into Sonnet 4.6 and Opus, we see now that in modern harnesses, we get sub-agents, we get some of those plan calls, we get different shell commands, and we get different verifications." Re-running a fixed task exposes changes in *how* the work gets done that a pass/fail result hides — and it is the reason the improvement cannot be attributed to the model alone, since "models are getting significantly better along with harnesses." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 06:10-06:31, 05:52-06:10)
- **The trade gets priced, and it is not free.** "Even though the model execution was a little bit more expensive, it was a lot less manual. So, we could actually accomplish a lot more." Running the same task repeatedly makes the cost/effort exchange visible as a number rather than a feeling — the newer generation buys human hours with tokens.
- **Choose a task the model can fail on.** The instrument only works if the original required real judgment: the value of "10 major mistakes with o3" is that a naive run produced ten specific things a knowledgeable human had to reject. A task your first model already one-shot yields no signal in either direction on any subsequent release.
- **Caveats that matter before quoting a ratio from this method.** It is one task, one attempt per model as described, with no repetition to separate model improvement from run-to-run variance. "10 major mistakes" is not scored against a rubric and "one additional iteration" is undefined. The harness is not held constant — o3 ran "in Cursor" and the harness for the later runs is never named — which is a live confound given that the talk simultaneously credits modern harnesses for the gain. And the person grading is the person who wants the refactor to have been worthwhile.
- **The same instrument pointed sideways instead of forwards: one remembered bug, two models of the same generation.** Cline ran "a real bug from the Cline repo" against Opus and GLM after doubting a benchmark that ranked GLM higher. Both fixed it, so the pass/fail axis was silent; the reading came from the surrounding behavior — GLM "cleaned up dead code and verified that the build compiled before completing," Opus "left a bunch of type errors and it broke the production build." That is the same human-grader logic this page describes, applied to a vendor-substitution decision rather than a generational one, and it shows how little the method needs to be useful: a known-good outcome, one run each, and someone who can tell dead code from live. It inherits every caveat above and adds one — Rizwan calls it anecdotal himself, and Cline had launched an open-weights subscription three days earlier. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 09:28-10:17)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Replay Your Own Merged PRs as the Coding-Agent Benchmark](replay-your-own-merged-prs-as-the-agent-benchmark.md)
- [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Measure Generated Code Quality Beyond Pass Rate](measure-generated-code-quality-beyond-pass-rate.md)
- [Read the Task-Length Curve at the Success Rate You Would Actually Delegate At](read-the-task-length-curve-at-the-success-rate-you-would-delegate-at.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)

Sources:
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 05:20-06:48
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 09:28-10:17
