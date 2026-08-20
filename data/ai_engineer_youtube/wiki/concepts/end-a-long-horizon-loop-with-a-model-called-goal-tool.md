# End a Long-Horizon Loop With a Model-Called Goal Tool

Summary: A "keep going until done" mode is implemented by injecting a continuation prompt carrying the objective after each turn and looping until the model calls a tool declaring the goal achieved. The exit condition is therefore a model judgment about the objective's text, which makes a concrete, checkable goal a control-flow requirement rather than a prompting style preference.

Use when:
- Building or configuring an autonomous mode that must run for many turns without a human.
- Explaining to users why a long-running agent stops too early, or does not stop.
- Writing the objective for a `/goal`-style run, a background agent, or an overnight task.

Details:
- The mechanism: while the goal is unmet "the harness will inject this continuation prompt. And this continuation prompt includes, among other things, your objective. That's the goal that you set. And then… we continue to do this until the model itself calls an update… goal tool, which specifies that… the goal was actually achieved." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 17:53-18:32)
- Two facts follow directly from that shape. The objective text is re-presented every turn, so it is paying context rent for the whole run; and the loop's termination is a classification the model performs against that text, turn after turn.
- **The prescription is a consequence, not advice.** "That is the reason why you actually don't want to… write full essays… into your goal, but instead have very concrete and very [verifiable]… prompts, so that… it's easy to detect when things are done." An essay-length objective is not merely wordy — it gives the model a fuzzy predicate to evaluate, and a fuzzy predicate is what produces both premature stops and runs that never end. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 18:33-18:51)
- A useful test when writing one: could a script check this? If the objective reduces to something observable (a test passes, a file exists, a number is guessed), the model's completion judgment is nearly deterministic. If it reduces to a quality opinion, the loop's exit is an opinion too.
- **Note what is absent from the described design.** No iteration cap, no cost ceiling, and no timeout are mentioned, so a goal the model cannot satisfy and will not declare satisfied has no stated stopping rule. That is the same open exposure the wiki records for [Grade With a Parallel Rubric Agent and Retry Until It Passes](grade-with-a-parallel-rubric-agent-and-retry-until-it-passes.md) — an in-loop completion judge with no bound turns a mis-specified criterion from a bad measurement into unbounded spend. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 17:53-18:51)
- The two judges differ in who is judging. Here the acting model decides its own work is done, which is cheap and needs no second inference stream but is exactly the self-assessment that a separate grader exists to avoid. Neither source compares them.
- **Provenance.** Demonstrated on a toy task (guessing a number) in a vendor talk, with no data on how often the model declares completion early or late, and no description of what the harness does if the model never calls the tool. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 17:53-18:32)

Related topics:
- [Agents](../topics/agents.md)

Related concepts:
- [Grade With a Parallel Rubric Agent and Retry Until It Passes](grade-with-a-parallel-rubric-agent-and-retry-until-it-passes.md)
- [Interleave reasoning and tool calls for long-horizon agents](interleave-reasoning-and-tool-calls-for-long-horizon-agents.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Model Async Agent Work as Spawn, Send, Wait, Shut Down](model-async-agent-work-as-spawn-send-wait-shut-down.md)
- [Match Agent Tooling to the Model's Training Distribution](match-agent-tooling-to-the-models-training-distribution.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 17:53-18:51
