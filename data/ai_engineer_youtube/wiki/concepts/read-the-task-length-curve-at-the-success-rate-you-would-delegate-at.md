# Read the Task-Length Curve at the Success Rate You Would Actually Delegate At

Summary: METR's time-horizon curve is conventionally quoted at 50% success, which is the wrong threshold for anyone deciding whether to launch an unattended agent run. Read the same curve at 80%, 90%, or 99% instead: the exponential trend survives, the headline durations shrink dramatically, and the number you get is the one that governs whether writing a spec and walking away is worth the wall-clock and attention it costs.

Use when:
- Deciding whether a task is long enough and reliable enough to hand to an agent unattended rather than supervising it.
- Quoting or comparing model time horizons across generations, or reading a capability trend published at 50%.
- Explaining why a model that "can do 4-hour tasks" still wastes your evening.

Details:
- **The substitution.** "Typically this graph is shared with the 50% accuracy rate, but I think it's much better to actually look at the 80% accuracy rate or higher. And you can still see a similar exponential trend, but we're no longer claiming that models can accomplish tasks that would take a human 18+ hours." The trend shape is unchanged; only the level moves, so the higher-threshold reading costs nothing in narrative and buys a usable number. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 07:57-08:27)
- **Why the higher threshold is the decision-relevant one.** "I actually think it's much better to measure the accuracy at 90% or 99% because this is where the mental model is most efficient. You construct a plan, you create a spec, you hand it off to an agent, and you're pretty sure that it'll get things done… You don't want to be creating a plan or a spec and then have a 50/50 chance of coming back and knowing that you wasted compute and your attention span." The threshold that matters is the one at which the *delegation workflow* — plan, spec, hand off, leave — becomes rational. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 08:27-08:48)
- **The arithmetic, stated bluntly.** "If you're kicking off a process that is going to take an hour and it has a 50% chance of completing, there's a very high chance you just wasted that hour and you could have been doing something different." Note what is being spent: not only compute but a block of human time that was allocated on the assumption the run would land. The cost of a failed unattended run is the *option* you gave up, which is why 50% reads as adequate on a benchmark and as a coin flip in a workday. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 08:48-08:58)
- **The failure this is calibrated against is upstream of the model.** The talk polls the room on having "kicked off an agent and realized that either the prompt, the plan, or the requirements were incomplete or missing" — "A lot of people, yeah?… 'Okay, I'm ready to go. It's 11:00 p.m. or 5:00 p.m. I'm going to set off an agent and then come back.' And then you realize there is a critical flaw." A published success rate does not include your under-specified prompt, so the real delegation odds are worse than whatever threshold you read off the curve. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 07:29-07:50)
- **Duration is not a single ordering, and this is the part the curve hides.** On METR's frontier-model results, "the success rate starts to decline significantly at that 4-hour mark, but even before then at the 15-second mark or even before the 15-minute mark, there are certain tasks that [the model], in all its glory, cannot complete effectively and consistently." A time horizon is a fitted summary over a task distribution, so "my task takes a human two hours" does not place it under the curve — short tasks in the wrong category fail too. ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 08:58-09:25)
- **What it is used for.** Not model selection, but each engineer's own operating model: "we're making rapid progress in the AI model space, but we're still not there where you can just kick off an agent and have something be completed reliably," and this "is really important for your software engineering teams and for you as an IC to understand what is your mental model and how are you going to contribute to that." ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 09:25-09:43)
- **Caveat: this is a reading recommendation, not new data.** Linkov contributes no measurements to the curve; he argues about which percentile of someone else's published fit to quote. The 50% convention exists because it is where a fitted logistic is best determined — estimates in the tail are noisier — so the higher-threshold number he prefers is also the less statistically stable one. Neither the talk nor the underlying methodology page addresses that trade. The frontier-model results are also recalled from memory ("roughly a month ago") and the model's name is unclear in the captions.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark Saturation Pushes Capability Evals Toward Human Time Horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Separate Watched and Unwatched Agent Time Horizons](separate-watched-and-unwatched-agent-time-horizons.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Re-Run One Remembered Hard Task on Each New Model](re-run-one-remembered-hard-task-on-each-new-model.md)
- [Audit a Refactor Against Having Waited for Better Models](audit-a-refactor-against-having-waited-for-better-models.md)

Sources:
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 07:29-09:43
