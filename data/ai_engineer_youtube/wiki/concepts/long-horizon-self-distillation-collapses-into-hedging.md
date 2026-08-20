# Long-Horizon Self-Distillation Collapses Into Hedging (the "But Wait" Problem)

Summary: Scale on-policy self-distillation to trajectories with tens or hundreds of tool calls and the student drifts far enough that the teacher course-corrects at every opportunity, so the tokens the update favors fill with *wait*, *but*, and *maybe* until the model parks between two divergent distributions and "everything just turns into maybe." It is a failure of the objective under drift, not a failure of the hint.

Use when:
- A distillation run that worked on short tasks degrades once trajectories get long.
- Reading a training run's favored-token statistics for signs of a mid-training pathology.
- Deciding whether a method demonstrated on chatbots or single-turn benchmarks will survive an agent workload.

Details:
- The threshold is stated concretely: "this works really well for small models, short horizon tasks like something like a chatbot. Uh but this is where academic papers kind of end and where you really need to scale things up to start to see the limitations." Breakage appears "as soon as you get to the 120B range with not just one or two tool calls but 50 or 100." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 12:16-12:47)
- **The symptom list comes before the diagnosis and is the part to check for in your own runs**: "eval accuracy is all over the place… run-to-run variance is extremely high, and then also we start to see a lot of tool call errors, the model is not behaving accordingly to the format that it was trained on in the first place with the instruction fine-tuning." Losing an instruction-tuned format is the tell that the update is reaching far beyond the intended behavior. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 12:49-13:07)
- The mechanism: "when you move on to longer tasks… this student model… is going off and doing whatever it thinks is on policy. And then at some point, because you're so divergent in a long task, the teacher is going to try to course correct every single time it gets a chance. And so what you end up with is the teacher model just continuously trying to improve this token of wait or maybe or some of these kind of hedging words." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 13:16-13:52)
- The observable signature is a word cloud of favored tokens: "as steps go on with opsd and you really scale it up, you start to see some of these words like wait and then but start to appear. And then you actually end up in this really interesting local suboptimal position where everything just turns into maybe." Geometrically, "you get two different distributions that are really divergent… the model trying to be in the middle of both of those." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 13:52-14:26)
- **Why the failure is specific to distillation and not to RL.** A reward-based update scores the trajectory that happened; a KL objective demands the student match the teacher *at every position of a trajectory the teacher would not have produced*. Once the prefix is off-policy for the teacher, the only tokens where both distributions have mass are the noncommittal ones, and the optimum of the averaged objective is the hedge. That is the same breadth that makes the method powerful — [it optimizes the whole vocabulary at every token](optimize-the-whole-vocabulary-not-the-sampled-token.md) — turned against it.
- The mitigation offered in the same talk is to stop treating all steps equally: [weight each step's tokens by student/teacher divergence](weight-distillation-steps-by-student-teacher-divergence.md), so a step where the two have already parted contributes little.
- **This is the wiki's first reported failure mode for self-distillation at agent scale, and it qualifies pages written from short-horizon evidence.** Applied Compute's account of the same family of methods reports the localization tricks — [judge-placed hints with a short distillation window](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md) and [token masking](mask-irrelevant-teacher-tokens-before-learning-from-them.md) — as ways to concentrate signal, and notes the KL learning signal decaying with distance from the hint. Read alongside this page, those look less like efficiency measures and more like the same defense against the same drift, arrived at independently: narrow the aperture before the divergence has room to accumulate.
- A useful reframing of the general lesson, beyond distillation: any teacher-follows-student scheme has a drift budget. Once the student's trajectory leaves the region where the teacher's guidance is meaningful, continuing to apply that guidance is worse than not applying it. The wiki's [reliability-and-plasticity](reliability-and-plasticity-conflict-in-continually-learning-agents.md) tension is the same shape one level up.
- Provenance: a vendor's account of its own scaling work, evidenced by a word cloud and a distribution sketch. No frequency is given — how often a long run collapses, at what step, or under which hyperparameters is unstated, and no ablation isolates trajectory length from model size, since both moved together in the reported setup.

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Weight Distillation Steps by Student/Teacher Divergence](weight-distillation-steps-by-student-teacher-divergence.md)
- [Optimize the Whole Vocabulary, Not the Token You Sampled](optimize-the-whole-vocabulary-not-the-sampled-token.md)
- [Let a Judge Place the Hint and Distill Only the Steps Near It](let-a-judge-place-the-hint-and-distill-only-nearby-steps.md)
- [Hint Leakage Is the Reward Hacking of Self-Distillation](hint-leakage-is-the-reward-hacking-of-self-distillation.md)
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Mitigate small-model doom loops during preference alignment and RL](mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md)
- [Steer agents with leading words that surface in reasoning traces](steer-agents-with-leading-words-that-surface-in-reasoning-traces.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 12:16-14:26
