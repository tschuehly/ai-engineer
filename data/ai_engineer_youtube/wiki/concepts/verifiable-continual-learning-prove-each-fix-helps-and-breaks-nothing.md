# Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing

Summary: Continual learning for an agent should be *verifiable* — every improvement drawn from production experience is proven to help the failing case and proven to break nothing that already worked, via an executable test, a measured before/after delta, and a regression test.

Use when:
- Turning production failures, traces, or feedback into durable agent improvements rather than one-off patches.
- Deciding whether a prompt/memory/model change is safe to promote.
- Designing a self-improvement loop that must run continuously without capability drift.

Details:
- Continual learning imitates human learning-from-experience: the agent acts, gets feedback, and improves "without forgetting." The two hard problems are getting feedback and acting on it. (00:30-02:26)
- The core definition: verifiable continual learning improves an agent from its own experience "where every fix is proven to help and proven to break nothing that already worked," via three steps — an executable test (the failure becomes a replayable task), a measured delta (the update is scored on the test before and after), and a regression test (prior tests still pass after the change). (11:04-11:47)
- Four principles make it practical: replayability (lift a one-off failure into a rerunnable learning environment), holisticness (route the fix to the right layer with the smallest durable change), lifelongness (regression-aware optimization so a new fix doesn't break the past), and efficiency (the loop and its regression control must run continuously and not scale linearly in the number of past environments). (11:47-15:44)
- The two failure modes it defends against: "vibe-based" harness edits and unverified memory writes that appear to fix one case but silently regress others, and overfitting the latest fix so previously-passing tasks break (the demo benchmark builds in an explicit "regression trap"). (09:09-11:01, 18:36-19:07)
- Packaged as a loop (signals → replayable learning environments → root-cause routing → regression-aware optimization → reviewable version PR), it turns a self-improvement step into a compounding, testable, reviewable change rather than an act of faith. (15:44-21:33)
- The stated frontier: a holistic, lifelong, verifiable learning loop with online regression control — "when fixing the new failure, we verify that we don't forget the old ones." (21:35-22:26)
- What this discipline is buying, named generally: reliability and plasticity are "inherently conflicting with each other. Reliable systems or stable systems, they resist the change. But the plastic systems likes change" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:46-16:12). Verifiable continual learning does not dissolve that conflict — it prices each unit of plasticity against the stability it might cost, which is why replayability comes first: a system that cannot re-run its past has no way to charge a change for what it breaks.
- The limit of the framing: RELAI's loop verifies *repairs* to known failures. Su's target is the accumulation of *competence* in an environment, and he flags the missing instrument for it — "how do you even define and measure expertise? And this is probably environment-specific" ([NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:35-15:46). A regression suite proves nothing was lost; it does not measure how much was gained.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Make Regression-Aware Optimization Part of the Continual-Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Replay Production Failures Before Promoting Prompt Fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)

Sources:
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 00:30-02:26, 11:04-15:44, 21:35-22:26
- [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](../sources/20260812_I6aiEf3aEFQ.md), 15:35-16:12
