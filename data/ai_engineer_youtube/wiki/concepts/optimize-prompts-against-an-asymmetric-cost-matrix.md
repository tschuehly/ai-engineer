# Optimize Prompts Against an Asymmetric Cost Matrix, Not Flat Accuracy

Summary: Prompt brittleness makes hand-tuning unreproducible and slow, so prompts should be improved by an optimizer — but the optimizer amplifies whatever objective it is given. Replacing a flat accuracy average with a cost matrix that encodes the real asymmetry between error types, defined with domain experts, is what makes automated prompt optimization safe to point at a high-stakes product.

Use when:
- Deciding whether to hand-tune a production prompt or hand it to an optimizer such as GEPA.
- Writing the metric for an optimization or eval loop where a false negative and a false positive carry wildly different costs.
- Letting a domain expert (clinician, analyst, lawyer) steer model behavior without writing prompts.

Details:
- Hand-tuning does not survive prompt brittleness: "formatting changes alone have been seen to swing benchmarks by 76 percentage points," and "reordering few-shot examples flips a model from near random, so near 50%, to near state-of-the-art on some benchmarks." Manual prompt engineering is "very subjective, it's not reproducible, and very importantly, it's extremely time-consuming." (11:33-11:55)
- Grading is not improving. A validated judge producing "a pile of pass/fails tells you where [the system] breaks and where it's not safe, but doesn't actually make the product better" — the optimizer is what turns the eval signal into a change. (11:05-11:18)
- **GEPA** (genetic Pareto, "from the same people who made DSPy") is the optimizer used: define a metric for what good is, run the data through, get back which examples failed, "get a very strong LLM to reflect on the failures and update the prompt automatically," and repeat, keeping "a pareto frontier of the best prompts until your budget has been exhausted." (11:56-12:42)
- Reported payoff: hours-to-days of manual prompt engineering collapses to "between 30 minutes and an hour," and the result is reproducible with "a very clear audit trail and clear feedback loop" — which matters when the trail is the regulatory deliverable. (12:43-13:03)
- The work then relocates rather than disappearing: it becomes "purely a data science problem… mainly focused on the data, how to make your data right, the feature engineering, and you define the actual metric along with the clinicians." Automating the prompt raises the value of the metric and the dataset. (13:03-13:15)
- **The metric must not be a flat accuracy score** — "you don't want just an average of how your whole data set did. You give it a cost matrix." Worked example: a red flag present and caught is good; a red flag missed "could be catastrophic"; a red flag over-called when none exists "is just mildly annoying to the patient — they may need to answer a couple extra questions, but it's not a catastrophic harm situation." (13:20-13:58)
- That asymmetry becomes reward shaping: "a higher reward for finding the red flags and a lower reward for missing them," which is how a sensitivity preference gets encoded into the optimization objective rather than left as a hope about the prompt. (13:59-14:12)
- The objective is a swappable parameter, which is what makes it usable by domain experts: a clinician who wants to optimize for accuracy or some other metric only has to "recompile the prompt" to get a new optimized one — the same programmatic-prompt property that makes DSPy-style programs re-targetable. (14:12-14:26)
- The optimized prompt is not shipped on its own: it passes through the simulation framework as a safety gate, and failures send you back to redo the data, relabel, or gather more before any gated deploy. Prompt versions are pinned and traces kept. (14:28-15:18, 16:37-17:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Replace Ship-and-Rollback With Hazard-First Simulation When Errors Are Irreversible](replace-ship-and-rollback-with-hazard-first-simulation.md)
- [Validate the Simulated User and the Judge Before Trusting a Simulation](validate-the-simulated-user-and-the-judge.md)
- [Evaluator Quality Is a Dependency of Prompt Optimization](evaluator-quality-is-a-dependency-of-prompt-optimization.md)
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)
- [DSPy Programs Keep LLM Intent Separate From Prompt Strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Size Agent Quality Against the Channel's Reply Rate](size-agent-quality-against-the-channel-reply-rate.md)

Sources:
- [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../sources/20260819_McknwOzbmyg.md), 11:05-15:18, 16:37-17:12
