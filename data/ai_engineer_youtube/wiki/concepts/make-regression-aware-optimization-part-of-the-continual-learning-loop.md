# Make Regression-Aware Optimization Part of the Continual-Learning Loop

Summary: When an agent learns from a new failure, fixing that case in isolation can silently break cases it already handled; regression-aware optimization treats "don't forget the past" as an in-loop constraint of the optimizer, not a post-hoc check, and keeps it efficient enough to run continuously.

Use when:
- Building a lifelong self-improvement loop that repeatedly ingests new failures.
- A prompt/memory/model fix improves the target case but risks catastrophic forgetting elsewhere.
- Designing an optimizer that accumulates many past learning environments over time.

Details:
- The lifelongness principle: a new fix must improve the new case "without breaking the past." Given K past learning environments already optimized and a new failure lifted into environment E(K+1), the naive approach — focus only on the new environment — can regress previously-successful behavior. (13:26-13:59)
- The better approach is *regression-aware learning*, where regression is not a post-hoc step but a mechanism inside the optimization itself: fix the recent failures subject to no regression on the past learning environments. (13:59-14:19)
- Efficiency is a coupled constraint: the loop must run frequently, and the regression-aware optimization must not scale even linearly in K, because K grows and the complexity can otherwise blow up. Efficiency applies both to per-layer update cost and to the optimization loop itself when regression is handled in-loop. (14:19-15:31)
- This is the difference between a manual replay-then-rerun-the-suite discipline and an optimizer that internalizes the regression constraint: the talk names holistic, lifelong, verifiable learning with *online regression control* as the remaining frontier. (21:52-22:26)
- Validated on a benchmark with a deliberate "regression trap": if the optimizer overfits the latest fix, it breaks previously-passing tasks; the demonstrated loop lifts a production feedback ("keep fast eligible refunds, but do not generalize generosity beyond refund thresholds") into an environment and optimizes without regressing past behavior, compounding over time. (18:36-21:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Replay Production Failures Before Promoting Prompt Fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 13:26-15:31, 18:36-22:26
