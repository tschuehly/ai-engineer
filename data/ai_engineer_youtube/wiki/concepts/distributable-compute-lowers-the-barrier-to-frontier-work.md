# Distributable Compute Lowers the Barrier to Frontier Work

Summary: Pre-training compute has to be colocated and over-provisioned for redundancy, which is why it concentrates in a few organizations; inference, post-training, and agentic compute can be distributed and return more per FLOP. If the returns really have moved to the second kind, the barrier to competing is a purchasing-dynamics change, not just a cost reduction.

Use when:
- Deciding whether a capability gap you face is a compute-access problem or a recipe problem.
- Planning infrastructure for a team that will post-train and serve but not pre-train.
- Assessing whether a small team can realistically compete on a model-quality axis.
- Reading claims that AI is "democratizing" and looking for the physical argument underneath.

Details:
- The physical asymmetry, stated directly: "pre-training compute typically has to be co-located. Um it has to be… in many ways large volume to accommodate for redundancy. Inference compute and other places where you actually apply compute, typically you can have much more… distributed. It's also much more higher return given the amount of flops." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 11:08-11:27)
- The consequence for who can compete: "agentic compute, post-training compute matters a significant amount for performance. That does not require the same type of… I dare I say hoarding of GPUs… it's very different compute purchasing dynamics. And again, it means that the person with the best idea has a higher chance of winning." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 14:44-15:09)
- "Purchasing dynamics" is the load-bearing phrase and is the part an infrastructure planner can act on. Colocated pre-training implies a long-lived reservation of a contiguous, homogeneous, high-bandwidth cluster held through failures; distributable inference and post-training tolerate heterogeneous, preemptible, geographically split capacity bought closer to demand. The wiki's operational pages describe both sides of that line — [match GPU commitments to workload lifecycle](match-gpu-commitments-to-workload-lifecycle.md), [inference tolerates degraded GPUs that training cannot](inference-tolerates-degraded-gpus-that-training-cannot.md), [aggregate idle GPU supply through compute marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md), and [run elastic training on serverless GPU, not a reserved cluster](run-elastic-training-on-serverless-gpu-not-a-reserved-cluster.md).
- The claim is conditional on the scaling argument beside it. It only lowers the barrier if size has genuinely stopped paying — see [Pre-Training Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md). Her own statement of the dependency: "if pre-training scale isn't going to dominate performance, it actually really greatly changes who can create the best recipes for innovation" (11:00-11:08).
- What competition then runs on: "these are new places where… the barriers to entry are much more nimble, and where recipe and algorithm and research matters again." That is a claim that method beats capital in a specific window, not that compute stops mattering. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 12:26-12:36)
- The counterweight she accepts in Q&A, raised by an attendee: RL and even fine-tuning on large models remain GPU-intensive, and frontier models are "still pretty large." Her answer concedes the level and disputes the trend — the playing field is "more equal… at the top" because nobody is expected to supersize, not because post-training is cheap. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:44-19:20)
- The other half of the same argument is that automating the training recipe is worthless if the compute barrier stands: "if we just did auto scientist, but it still took enormous compute to do frontier AI trainings, I think we'd be in a bit of a pickle… 'Oh great, you can use this agent, but don't worry, just bring your 10,000 GPUs with you.'" The two arguments — automated recipes and distributable compute — are presented as needing each other. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 10:15-10:28)
- Provenance: a founder whose company gives away GPUs with its beta, making the access argument that supports her product's premise. The physical asymmetry between colocated pre-training and distributable serving is uncontroversial and independently supported elsewhere in this wiki; the inference that it changes who wins is her argument, not a measurement. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 20:10-20:17)

- **"Post-training compute can be distributed" is asserted here and given a mechanism — and a sharp qualification — elsewhere.** Modal's cross-datacenter talk agrees that RL post-training can leave one cluster, but only half of it: "back propagation should stay in the cluster. The rollout fleet is the one that can leave," because every training step has collectives while "across rollout jobs there's no global all-reduce" ([The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)). Post-training is therefore not distributable as a category; it contains a colocated core with exactly the pre-training-like requirements this page attributes to pre-training alone. What distributes is the sampling tier, which is the bulk of the FLOPs in group-based RL but not the whole method. ([Modal](../sources/20260810_maRzp4kImJ4.md), 03:25-03:59)
- The distribution is also not free by nature — it is bought by a specific numerical accident. Splitting the fleet leaves one link, the weight update, and shipping a ≈500 GB checkpoint across regions takes "multiple minutes to hours." What makes it viable is that a bounded Adam step at RL learning rates is ~1000× smaller than the serving format's rounding boundary, so ~99% of served weights are bit-identical per step and the sync object becomes ≈500 MB ([Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md)). Jiang raises the obvious fragility himself: everything rests on Adam, and Moonshot and DeepSeek are moving to Muon. Treat the distributability of post-training as contingent on the optimizer, not as a property of the workload. ([Modal](../sources/20260810_maRzp4kImJ4.md), 05:25-06:02, 09:11-09:52, 18:48-19:02)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Pre-Training Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md)
- [Frontier-Training Know-How Is Apprenticeship, Not Literature](frontier-training-know-how-is-apprenticeship-not-literature.md)
- [Match GPU Commitments to Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md)
- [Run Elastic Training on Serverless GPU, Not a Reserved Cluster](run-elastic-training-on-serverless-gpu-not-a-reserved-cluster.md)
- [Customization Control Is a Separate Question From Open Weights](customization-control-is-a-separate-question-from-open-weights.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Adam Absorption Hides Most Weight Updates From the Served Model](adam-absorption-hides-most-weight-updates-from-the-served-model.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 10:15-12:36, 14:44-15:09, 17:44-19:20
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 03:25-03:59, 05:25-06:02, 09:11-09:52, 18:48-19:02
