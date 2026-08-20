# Penalize Dangerous Steps With a Process Reward Model

Summary: An outcome-only reward cannot see the damage an agent did on the way to a success. A process reward model scores the path and its side effects step by step, penalizing dangerous actions during the trajectory rather than only grading the final state.

Use when:
- Training or fine-tuning an agent that takes irreversible real-world actions.
- The agent reaches the goal but the trajectory contains steps you would never approve.
- Designing rewards for tasks where "done" and "correct" are not the same thing.

Details:
- The claim: "the outcome is very important, but the path the model takes and the impact it has throughout the trajectory is very important as well. And so we focus really hard on making sure we catch all of these dangerous actions throughout the process, not just the outcome, and penalize that accordingly." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 09:49-10:07)
- The motivating failure is the ambiguous-success problem: "done often doesn't mean successful. If the agent filed [an] expense report for me, but also sent a resignation letter on my behalf to the CEO, it is done, but not what I wanted it to do." An outcome verifier checking that the expense was filed returns success on that trajectory. (07:48-08:02)
- The same gap appears in the earlier trajectory: an agent that guesses passwords until the account locks and *then* succeeds on a later task has an outcome score that never mentions the locked account. Step-level penalties are what make that step visible to training at all. (04:47-05:38)
- This is a distinct control from the harness-side [action risk classifier](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md), which blocks a risky action at runtime. The process reward changes the weights so the action is less likely next time; the classifier catches the ones that still happen. The talk runs both.
- It is also distinct from [calibrated confidence](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md): the process reward is the training signal that says "that step was dangerous," while calibrated confidence is the learned policy that decides whether to take a step or escalate.
- Cost note the talk does not resolve: a process reward model needs a judgment of danger at every step, which is a much larger labeling and grading surface than a terminal verifier. The wiki's existing verifier ladder — string equality, compiler, linter, unit tests, database lookups, rubric-graded agent judges (02:58-03:16) — applies at the outcome; nothing in this source says which of those is used for per-step danger scoring.
- Related reward-design caution from another source: rewards shaped to match production also invite reward hacking, so per-step penalties need the same anti-hacking scrutiny as outcome rewards. See [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md).

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use Verifiable Rewards for Language-Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)
- [Keep the Harness Thick Early and Thin It as the Model Improves](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 02:58-03:16, 04:47-05:38, 07:48-08:02, 09:49-10:07
