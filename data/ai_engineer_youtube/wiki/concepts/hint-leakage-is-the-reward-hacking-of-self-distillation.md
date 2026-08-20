# Hint Leakage Is the Reward Hacking of Self-Distillation

Summary: Self-distillation constructs its teacher from a hint, so a hint containing the answer teaches the model to state the answer and back-fill the reasoning afterward — a behavior with no counterpart at inference time, where no hint exists. It is the structural analogue of reward hacking: the supervision signal is satisfiable by a shortcut the deployed system cannot take.

Use when:
- Designing hints for a distillation pipeline and deciding how much of the resolution to include.
- A trained model asserts conclusions early and rationalizes them, in a way the base model did not.
- Auditing any training scheme where privileged information is added to a prompt.

Details:
- The framing: "with RL the number one problem that people face is reward hacking… Well there is an equivalent for OPSD as well and that is hint leakage… if the student had no way of knowing what that hint would be, then you're going to end up with some weird scenarios and kind of skipping some steps along the way." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 15:53-16:25)
- **The worked signature is the useful part, because it is recognizable in a trace.** On "find the last three digits of this formula" with a hint that gives the steps and then "the last three digits are all zeros," the rollout comes out as: "Oh, actually, I know what the solution is. It's 000. So, let me go back and put that into my reasoning trace and then figure out what's going on." Malde's verdict: "you can imagine that this is not going to occur whatsoever in the real world." Answer first, derivation retrofitted, is the grep-able pattern. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 16:26-17:00)
- Why this is more than sloppiness: the student is being trained on log probs the teacher produced *while holding the answer*, and a teacher holding an answer has no reason to derive it. Every token of genuine reasoning the hint makes unnecessary is a token the student is taught to skip. The technique's power and this failure have the same source — that the teacher is [the same policy made smarter by privileged information](distill-without-a-golden-answer-using-privileged-information.md).
- **Mitigation one, a hint rewriter.** "There's one kind of trivial solution… literally using an LLM to filter out these hints." The example: a user cannot log in, and the environment record contains "exactly the solution — you'll find their SSO token that is expired"; an LLM translates that into "what is something reasonable that they should have known, and that's the process of looking through the logs but not actually giving it the solution that it would shortcut some of its vital reasoning." It "works decently well." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 17:11-17:47)
- The rewriter turns hint design into a stated question with a good default: a hint should supply *what the model should have noticed*, not *what the model should have concluded*. Signals, not resolutions. That is a rule you can apply without any of the vendor's machinery.
- **Mitigation two is algorithmic**: [blend a partial-hint teacher with the full-hint teacher](blend-a-partial-hint-teacher-to-bound-the-distribution-shift.md), which measures how far the hint pushes the model out of its own distribution and clamps the shift.
- **This is the hazard on the other side of the wiki's strongest hint result.** Applied Compute reports that a rollout-specific hint took formatting correctness from ~15% to ~80% where both a reward and SFT degraded the base model ([hint against the rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)), and that hint content mattered less than placement. This page supplies the countervailing constraint: hints are not free-form, and the failure they invite is quiet, since a leaked hint improves training-time behavior on exactly the metric you are watching. Read the two together as the two halves of hint design — specificity buys the gain, informational restraint keeps it real.
- The analogy to reward hacking also imports its detection discipline. As with [reward hacking in code-optimization evals](detect-reward-hacking-in-code-optimization-evals.md), the artifact to inspect is the trajectory rather than the score: look for conclusions that arrive before the work that would justify them.
- **What is missing.** No frequency, no detector, and no evaluation of the rewriter are given — how often hints leak, how you would catch it in a production pipeline, and how often the LLM filter over- or under-redacts are all unstated. "Works decently well" is the entire evidence for mitigation one.
- Provenance: a founder talk from a company selling this pipeline; the failure mode is illustrated with a single rollout excerpt.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Blend a Partial-Hint Teacher to Bound the Distribution Shift](blend-a-partial-hint-teacher-to-bound-the-distribution-shift.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [When Rewards and SFT Both Degrade the Base Model, Hint Against the Rollout](hint-against-the-rollout-when-rewards-and-sft-degrade-the-base-model.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Design agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)
- [Long-Horizon Self-Distillation Collapses Into Hedging](long-horizon-self-distillation-collapses-into-hedging.md)
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 15:53-17:47
