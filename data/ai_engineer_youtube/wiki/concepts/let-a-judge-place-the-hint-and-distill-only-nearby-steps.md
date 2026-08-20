# Let a Judge Place the Hint and Distill Only the Steps Near It

Summary: Injecting a hint at the start of a rollout and distilling the whole rollout wastes most of the signal. Use a judge to pick the step where the hint belongs, then distill only that step and a few after it — because the measured KL learning signal decays with distance from the hint.

Use when:
- A self-distillation run is expensive and most of its gradient is going into unrelated tokens.
- A rollout is long and the behavior you want to change happens at one identifiable moment.
- Deciding what unit to train on: the trajectory, the turn, or the token.

Details:
- The practice: "rather than injecting a hint to the beginning of a rollout, we use a judge to essentially decide where in the rollout we should be injecting hints. And then… it's best to just do distillation on that next step that occurs or maybe a few steps forward rather than the entire rollout. Because that's really the turn in the moment in time that you want to have the teacher teach something to the student." Denton calls per-step hinting "very, very important to making distillation work." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 16:13-16:57)
- The empirical justification, shown as a chart: "this KL learning signal basically goes down as you get further and further away from the hint, which makes sense." The teacher and student distributions reconverge once the hinted moment has passed, so later steps contribute little and dilute the update. ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 16:47-16:57)
- **Two decisions are being delegated to the judge, and they are separable.** *Where* the hint goes is a localization problem over the rollout; *how far forward* to distill is a window-size hyperparameter ("that next step… or maybe a few steps forward"). The talk describes the judge doing the first and leaves the second as a stated finding rather than a learned quantity.
- The decay observation is itself a cheap diagnostic to run on any hint-based pipeline: plot the teacher/student divergence per step relative to the hint position. A flat curve means the hint is not landing where you think it is; a curve that decays within one step means your training window is too wide.
- Composes directly with the other two implementation practices in the same talk. The judge-selected step is the natural place to take a [single on-policy step](buy-on-policyness-with-a-single-rollout-step.md), and within the chosen window, [token-level relevance masking](mask-irrelevant-teacher-tokens-before-learning-from-them.md) narrows the signal further. The three are localization at trajectory, step, and token granularity respectively.
- **The judge is now load-bearing, which imports the wiki's judge caveats.** A misplaced hint trains on the wrong moment, and nothing in the talk validates the placement judge or reports its agreement with a human. Before trusting a pipeline like this, [check the judge before changing the agent](check-the-judge-before-changing-the-agent.md) and treat placement as a narrow binary decision that can be measured ([Split LLM judges into narrow binary metrics](split-llm-judges-into-narrow-binary-metrics.md)).
- The same judge is what makes the online corner scale across behaviors rather than one at a time: "that judge is able to adapt to whatever the online model does in production," which is the stated reason online hinting supports "improvement across multiple improvement areas." ([Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 17:40-18:26)
- Provenance: an unpublished in-house practice, presented as a tip with one chart. No ablation of window size, no judge accuracy, and no cost comparison against whole-rollout distillation are given.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Mask Irrelevant Teacher Tokens Before Learning From Them](mask-irrelevant-teacher-tokens-before-learning-from-them.md)
- [Buy On-Policyness With a Single Rollout Step on an Offline Trace](buy-on-policyness-with-a-single-rollout-step.md)
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Check the judge before changing the agent](check-the-judge-before-changing-the-agent.md)
- [Split LLM judges into narrow binary metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Penalize dangerous steps with a process reward model](penalize-dangerous-steps-with-a-process-reward-model.md)

Sources:
- [Bringing Continual Learning into Enterprises — Samuel Denton, Applied Compute](../sources/20260812_ZTA0GwpAUak.md), 16:13-16:57, 17:40-18:26
