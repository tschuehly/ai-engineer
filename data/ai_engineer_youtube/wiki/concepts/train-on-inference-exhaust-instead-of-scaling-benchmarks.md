# Train on Inference Exhaust Instead of Scaling Benchmarks

Summary: The case for learning from production traffic is not primarily that it is more relevant — it is that the alternative is getting worse on three axes at once. Benchmarks saturate in months, cost hours to days per task to construct, and are not tied to how anyone actually uses the system, while "hundreds of trillions of tokens every single day" of inference already record how models fail and succeed.

Use when:
- Justifying investment in trace capture against buying or building another eval set or RL environment.
- Arguing about whether a benchmark result predicts production behavior.
- Deciding where a post-training budget should go once benchmark gains flatten.

Details:
- The treadmill: "we've been rapidly scaling up benchmarks that have saturated within first years and then months," while "we're seeing domains where it takes 4 hours, 6 hours, 24 hours or even several days in order to scale up benchmarks," alongside "the massive amount of money that the labs are pouring into scaling up RL environments and data." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 00:52-01:26)
- The relevance objection is stated separately from the cost one, and is the one with teeth: benchmarks are "not tied to real world use cases where people are using AI." A cheap benchmark that measured the right thing would still be worth building; the argument is that these are expensive *and* misaimed. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 01:36-01:41)
- The asset on the other side: "we are actually spending hundreds of trillions of tokens every single day on inference, and we're generating great amounts of data on how models in the real world are are failing, how they're doing well. And that should be signal that we should be capturing and training on." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 01:42-02:03)
- **Why this is a training argument, not an observability one.** The wiki already holds that [observability and continual learning are the same problem](observability-and-continual-learning-are-the-same-problem.md) — traces are the substrate for both. This adds the economic half: the reason to reach for that substrate is that the manufactured alternative is on a bad cost curve, and the cost of an eval or environment is now measured in engineer-days per task while the exhaust accrues for free as a byproduct of serving.
- The unstated requirement, which the same talk's method supplies, is that raw exhaust carries no supervision. Production traces record what the model did, not what it should have done, which is why every scheme for using them constructs a teacher out of something the model did not have at the time ([Distill Without a Golden Answer](distill-without-a-golden-answer-using-privileged-information.md)). "The signal is already there" is true about the *experience* term and false about the *target* term.
- **How much weight the argument can carry.** It establishes that benchmark construction scales badly and that production data is abundant. It does not establish that models trained on exhaust generalize better — no comparison is offered, and a corpus of production traffic has its own severe biases (it contains only what your users tried, only against your current harness, and disproportionately what your current model was already good enough to be asked for).
- **The claim has an evaluation-side dual worth stating plainly.** If benchmarks are drifting away from production, the same drift attacks your evals, not only your training data — which is the reasoning behind [keeping evals in the repo as tests](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md) fed by real traces, and behind [promoting validated live-trace failure clusters into the golden dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md). A team that accepts this argument for training and not for measurement ends up optimizing production behavior against a benchmark it just conceded is unrepresentative.
- The framing also explains what the [four-property scorecard](score-post-training-algorithms-on-four-properties.md) is for: "online task distribution" is the property that decides whether an algorithm can consume exhaust at all, and it is the one SFT and GRPO both fail.
- Provenance: the opening argument of a founder talk for a company selling exactly this loop, so the conclusion is the product. The token-volume figure is a round assertion with no source, the "4 hours, 6 hours, 24 hours" range names no domain, and the human-learning analogy ("this is actually how humans learn") is rhetoric, not evidence. The trend is corroborated by name-drops (Ilya, Karpathy, Demis, Satya, a Dwarkesh video) rather than by results.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Score a Post-Training Algorithm on Four Properties](score-post-training-algorithms-on-four-properties.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Offline Hints on Offline Traces Need No Replayable Environment](offline-hints-on-offline-traces-need-no-replayable-environment.md)
- [Promote Validated Live-Trace Failure Clusters Into the Golden Dataset](promote-validated-live-trace-failure-clusters-into-the-golden-dataset.md)
- [Keep Evals in the Repo as Tests, Not in a Prompt Playground](keep-evals-in-the-repo-as-tests-not-in-a-prompt-playground.md)
- [Judge Benchmark Quality by Task Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Turn real coding sessions into RL environments](turn-real-coding-sessions-into-rl-environments.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 00:52-02:30
