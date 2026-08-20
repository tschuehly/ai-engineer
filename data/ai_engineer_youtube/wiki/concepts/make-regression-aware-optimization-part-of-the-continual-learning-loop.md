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

- **The measurement layer this constraint needs, from a weight-level loop rather than a prompt-level one.** Applied Compute reports every targeted behavior change against three numbers: the behavior rate, a base-task rate defined "irrespective of whether the agent… submitted the task via this tool call," and their intersection — with the goal stated jointly, "raise the SWE-bench pass rate performance while not degrading the test pass rate" ([Measure a Targeted Behavior Change With Three Metrics](measure-a-behavior-change-with-three-metrics-including-their-intersection.md)). The load-bearing word is *irrespective*: a base metric that conditions on the new behavior cannot detect what the new behavior cost. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 11:20-12:04)
- The regression risk is not hypothetical at this layer. On a formatting task, a format reward and SFT on correctly formatted traces both produced "degradation in overall coding agent performance," and the reported repair was to narrow the update's aperture rather than to strengthen the constraint — a judge-placed hint, a few-step training window, and token-level masking ([When Rewards and SFT Both Degrade the Base Model](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md), [Mask Irrelevant Teacher Tokens](mask-irrelevant-teacher-tokens-before-learning-from-them.md)). Read alongside this page: regression-aware optimization constrains *what the update may cost*; aperture control reduces *how much it touches in the first place*. They are complementary and neither substitutes for the other. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 14:51-15:09, 16:13-17:36)
- A small coincidence worth noting because it is easy to over-read: both talks use an over-generous refund policy as their canonical example — RELAI as a production feedback lifted into an environment, Applied Compute as a static behavior prior turned into an offline hint. That is convergence on a *stock example* of a costly agent behavior, not corroborating evidence about either method.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Measure a Targeted Behavior Change With Three Metrics, Including Their Intersection](measure-a-behavior-change-with-three-metrics-including-their-intersection.md)
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Replay Production Failures Before Promoting Prompt Fixes](replay-production-failures-before-promoting-prompt-fixes.md)

Sources:
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 13:26-15:31, 18:36-22:26
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 11:20-12:04, 14:51-15:09, 16:13-17:36
