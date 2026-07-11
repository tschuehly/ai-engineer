# Verify the Process, Not Just the Answer, in Judgment-Heavy Domains

Summary: In verticals full of expert judgment calls (sustainability, legal, finance, medicine), validating an agent's final answer is not sufficient — there are many ways to reach the right answer for the wrong reasons and many defensible answers experts disagree on, so an answer is only justified insofar as the process that produced it is correct. When you cannot fully verify the answer, validating the process becomes the main lever.

Use when:
- Deploying agents in an under-specified domain with no single verifiable ground-truth answer, where "right for the wrong reasons" is common.
- Deciding what to check: the output artifact alone, or the reasoning/steps that produced it.
- Reasoning about reward hacking, or why a smarter model didn't fix reliability in a judgment-heavy space.

Details:
- The core claim: "you have to verify the process in addition to the answer because the answer is really only justified in so far as the process that produced that answer is correct." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 00:35-01:05)
- Evidence that the answer alone is a weak signal: a 2020 study gave six experts the exact same data on the exact same bottle of wine and their carbon answers "varied by up to 50%" — each expert judgment "correct in a sense," so validating the answer can't tell you a system mimicking those experts is itself correct. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 01:08-01:38)
- Precedent in the literature: the 2026 "Open Proof Corpus" showed a gap between the correct final answer and the correct proof *even in math, where the answer is fully verifiable* — "we view this problem as even worse where you can't fully verify the answer." Agents reward-hack (e.g. the Erdős problems), producing "many, many pages of errors in your proof which lead nowhere"; the "Beyond Correctness" authors conclude this "can pose significant risk for critical applications." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 06:39-07:26)
- A smarter model does not fix this: over time Watershed upgraded models, but the judgment-call problem persisted, because the issue is verifiability of the reasoning, not raw capability. When you can't perfectly verify the answer and expert-judgment calls are ever-present, "the main lever left is validating the process and making sure we are following it in a way we expect." ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 07:26-07:53)
- The payoff of a process guarantee: even for the ~8% of cases where the agent lands on a different answer than the reference (which may itself be one point in a valid range of expert judgments), the change is still "valid, traceable, and replayable" because the process is guaranteed independent of whether the answer matches. ([Andrew Dumit](../sources/20260707_CLttOU7n6sI.md), 14:47-15:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Constrain Agent Effects, Not Expression, With a Typed SDK](constrain-agent-effects-not-expression-with-a-typed-sdk.md)
- [High-assurance agentic coding needs process, not just generation](high-assurance-agentic-coding-needs-process-not-just-generation.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Run a jury of analysts and a consensus judge for no-ground-truth questions](run-a-jury-of-analysts-and-a-consensus-judge-for-no-ground-truth-questions.md)

Sources:
- [Respect The Process - Andrew Dumit, Watershed Technology Inc.](../sources/20260707_CLttOU7n6sI.md), 00:35-07:53, 14:47-15:08
