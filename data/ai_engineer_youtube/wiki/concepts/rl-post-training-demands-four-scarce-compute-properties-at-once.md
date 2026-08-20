# RL Post-Training Demands Four Scarce Compute Properties at Once

Summary: The default RL post-training loop needs enough GPUs, in one region, on fast fabric, available now — and the difficulty is the conjunction, not any single term. Because the loop is written as one tightly coupled job, the rollout fleet inherits the trainer's hardest procurement constraint, and it inherits it permanently, since training capacity cannot be grown mid-run the way inference capacity can.

Use when:
- Explaining why an RL run is blocked on capacity when GPUs are visibly available somewhere.
- Deciding whether to buy a bigger reserved cluster or to change the shape of the loop.
- Sizing an RL program against a fragmented, multi-provider GPU supply.
- Arguing about which parts of a training system are allowed to autoscale.

Details:
- The conjunction, stated as four terms: "RL wants all four of these at the same time. Enough GPU, same region, fast fabric, and available now. Any of these is manageable, but all four of them are pretty hard to get at the same time." Each term is individually purchasable; the intersection is what is scarce. ([Modal](../sources/20260810_maRzp4kImJ4.md), 02:43-02:56)
- The supply mismatch is geographic and commercial before it is technical. Jiang contrasts the **cathedral** — "one region, one faster interconnect, many GPUs wired together… the right shape for the trainer" — with the **bazaar**, "where a lot of usable compute actually lives. Different providers, different regions, different price and different availability." The conclusion: "available compute is distributed, but the default RL loop asks one tightly coupled cluster. And that cluster is exactly the hard part to get." (02:06-02:43)
- **The asymmetry that makes this a standing constraint rather than a one-time purchase:** "training capacity is not elastic in the way the inference capacity is. You cannot assume you can grow the trainer cluster halfway through a run just because rollout wants more nodes." An inference fleet can be scaled to demand; a synchronous training job's size is fixed at the start of the run. (02:56-03:07)
- The cost of coupling is therefore inherited, not shared: "if the rollout loop has to live inside the one cluster, rollout inherits the hardest part capacity constraint." Rollout has none of the four requirements on its own — it does no collectives — but pays for all four because of where it was placed. (03:07-03:22)
- This reframes a capacity problem as an architecture problem. The remedy Jiang argues for is not a larger reservation but moving the part of the loop that does not need the four properties out of the cluster that does — see [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md).
- Contrast with the wiki's existing capacity-market pages: [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md) treats fragmentation as a *matching* problem to be solved by a distribution layer, and [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md) treats it as a *contract* problem. Neither helps an RL run that structurally cannot use fragmented supply, because a marketplace can only deliver capacity in the shape the workload will accept. This page's contribution is that the workload's shape is the negotiable term.
- Provenance and limits: this is the framing section of a Modal vendor talk whose product is elastic multi-region GPU compute, so the scarcity claim and the proposed remedy come from the same source. No pricing, availability data, queue times, or regional inventory figures appear anywhere in the talk — the four-way conjunction is asserted from practitioner experience, not measured. ([Modal](../sources/20260810_maRzp4kImJ4.md), 00:19-03:22)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Run Elastic Training on Serverless GPU, Not a Reserved Cluster](run-elastic-training-on-serverless-gpu-not-a-reserved-cluster.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Simulate RL Run Layouts Before Spending GPU Budget](simulate-rl-run-layouts-before-spending-gpu-budget.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 00:19-03:22
