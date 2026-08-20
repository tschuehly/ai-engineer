# Score a Post-Training Algorithm on Four Properties

Summary: SFT, RLHF, GRPO, and self-distillation can be compared on one scorecard — is the task distribution *online*, is sampling *on-policy*, is parallelism *one*, is the reward *per token* — and each of the historical methods bought some of those properties by giving up others. The scorecard is useful independently of which algorithm you pick, because it names what a training choice actually costs in infrastructure and in signal density.

Use when:
- Comparing post-training proposals that are each described in their own vocabulary.
- Deciding whether an RL program's environment infrastructure is intrinsic or an artifact of the algorithm.
- Explaining why a method that works on a benchmark does not transfer to production traffic.

Details:
- The four properties, as stated in the form of what is broken today: "we have a task distribution mismatch. We're scaling up these benchmarks which might not even be tied to reality"; "some of these methods aren't even sampling truly on policy with what's happening online"; "we're sending out multiple rollouts and this requires huge amounts of infrastructure to make sure our environments are one-to-one copies of the real world… it ends up being a bias that we're adding to our training paradigm"; and "we are shoving every single reward into one scaler in order to train on when the real world is messy. It's noisy and it has rich amounts of data uh that should be per token signal." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 02:51-03:39)
- **SFT**: parallelism of one ("it was just one roll or one use case or example that we needed to train on") and a per-token reward, but off-policy sampling and a task distribution that is "just some sort of benchmark that we've cured or some sort of data set." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 03:59-04:22)
- **DPO / RLHF**: gains the online task distribution and improves sampling ("we were actually sampling from a model, but it was still off policy"), loses SFT's easy infrastructure to preference pairs, and drops the reward back to sequence level. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 04:29-04:52)
- **GRPO**, described as a deliberate trade: "we basically took a Fouian bargain and wanted to max on on policy rollouts which is extremely powerful… But on the other hand, we're working with off policy task distributions. Uh our parallelism is now exploded, meaning that we need really robust environment infrastructure. And then finally, for rewards, we're back to this paradigm of training on the entire sequence." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 04:57-05:31)
- **Why the parallelism row is the one engineers should read first.** It is the only property that translates directly into a budget line: group rollouts require environments that are "one-to-one copies of the real world," which is the same requirement that makes [RL environments software artifacts with their own lifecycle](build-rl-environments-as-software-artifacts.md) and that forces [hybrid rollout-worker system designs](use-hybrid-rl-system-design-for-agent-trajectories.md) for long agent trajectories. A method with parallelism of one deletes that line item rather than optimizing it.
- **The signal-density row has the sharpest argument attached.** A sequence-level scalar is "almost like you're drinking through a straw in order to get the reward… imagine you were trying to write an essay and your teacher just gave you a score of 87 out of 100. You would have to run through so many different examples to get to the idea of what a good essay is." That is a statement about sample efficiency, not about correctness — the scalar is not wrong, it is thin. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 06:52-07:11)
- On-policy self-distillation is presented as claiming all four: online task distribution, on-policy sampling, "parallelism that is singular," and "per token dense reward" — with the honest qualifier that it is "not necessarily the algorithm to solve continual learning, but definitely one that is a huge step forward." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 09:40-10:13, 19:20-19:44)
- **What the scorecard does not score, and should.** Nothing on it measures cost per update, stability, or the failure modes the same talk then spends a third of its length on — a method can hold all four properties and still [collapse into hedging on long horizons](long-horizon-self-distillation-collapses-into-hedging.md) or [get hacked through its hints](hint-leakage-is-the-reward-hacking-of-self-distillation.md). Treat it as a comparison of what each algorithm *sees*, not of what it delivers.
- It also silently prices out the compute self-distillation adds. Matching a teacher's full distribution at every token requires teacher forward passes over the whole vocabulary; "parallelism of one" describes rollouts, not FLOPs, and the talk never compares total cost against GRPO.
- Provenance: a founder's framing, drawn to make his own algorithm score four out of four. The historical rows are uncontroversial characterizations of well-known methods; the scoring of the last row is the vendor's own.

- **The parallelism row's cost is partly negotiable, which the scorecard does not show.** Malde treats exploded parallelism as a fixed consequence of group rollouts — "our parallelism is now exploded, meaning that we need really robust environment infrastructure" — and the wiki reads that as a budget line. Modal argues the rollout fleet does not have to live in the trainer's cluster at all: with weights synchronized as a bitwise-lossless patch and pulled from a shared board, "scattered inference capacity became one elastic rollout fleet… inference capacity can now become RL capacity" ([The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)). That does not make group rollouts free — the environments and the trajectory traffic remain — but it changes what the parallelism row is priced against, from scarce trainer-cluster capacity to ordinary serving capacity. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18, 18:17-18:43)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Optimize the Whole Vocabulary, Not the Token You Sampled](optimize-the-whole-vocabulary-not-the-sampled-token.md)
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Distill Without a Golden Answer by Giving the Teacher Privileged Information](distill-without-a-golden-answer-using-privileged-information.md)
- [Buy On-Policyness With a Single Rollout Step on an Offline Trace](buy-on-policyness-with-a-single-rollout-step.md)
- [Use hybrid RL system design for agent trajectories](use-hybrid-rl-system-design-for-agent-trajectories.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Train on Inference Exhaust Instead of Scaling Benchmarks](train-on-inference-exhaust-instead-of-scaling-benchmarks.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 02:51-05:31, 06:52-07:11, 09:40-10:13, 19:20-19:44
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 03:37-04:18, 18:17-18:43
