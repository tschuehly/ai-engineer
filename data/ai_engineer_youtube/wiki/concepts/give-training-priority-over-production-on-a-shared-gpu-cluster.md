# Give Training Priority Over Production on a Shared GPU Cluster

Summary: The usual cluster policy — production outranks everything, research gets the leftovers — is backwards for a lab whose product is a model. Krea runs training and production on one cluster and gives *training* the higher priority, so a submitted training job preempts inference off the machines it needs. The justification is marginal value ("the value that we get off the GPUs doing trainings is more… higher than… we get out of production"), and the design goal is that researchers never think about GPUs: they submit, and either capacity exists or the job queues.

Use when:
- Deciding how a single GPU pool should be split between model training and serving traffic.
- Research iteration is being throttled by capacity that production is holding but not fully using.
- Choosing a scheduler for training workloads and evaluating whether gang scheduling is required.
- Designing the submission interface researchers actually touch.

Details:
- The interface goal comes first and drives the rest: "I don't want my researchers to think about GPUs. I just want them to launch stuff and this goes into a queue and if we have GPUs we have GPUs. If we don't have GPUs we don't have GPUs." ([Menezes](../sources/20260818_byn9PURoBNY.md), 08:53-09:04)
- Gang scheduling is the non-negotiable scheduler property — "gang scheduling is important for trainings in general" — because a distributed run needs all of its pods placed together or none of them; partial placement wastes the GPUs it did get. Krea uses an open-source Kubernetes project for this (the transcript renders its name indistinguishably from the word "queue"; see the source note's Caption Artifacts). (09:04-09:14)
- Two priority tiers, not one: a workload-priority tier where "you can say like oh this training is more important than this one. So, it skips on the queue in front of the queue," sitting above ordinary Kubernetes pod priority. Ranking training runs against *each other* is a separate decision from ranking training against serving. (09:14-09:31)
- The inversion, stated without hedging: "the training pods they always have like high priority for everything. So, like once they are submitted they go on a schedule. If there's inference running on those machines, the inference gets kicked out. And you'd say, 'Oh, this is bad. Production is going to go down.' No, you can build on top of that to make production not go down." (09:31-09:47)
- The economic argument, which is what makes this a policy rather than a mistake: "production is lower priority. The site still needs to work. People still need to… use the website. But like the GPUs… the value that we get off the GPUs doing trainings is more… higher than… we get out of production." Note the precondition — production must remain *available*, just not *resident*, which is only possible because inference can be relocated. The mechanism is [Evict Inference Off-Cluster Through a Virtual-Kubelet Node](evict-inference-off-cluster-through-a-virtual-kubelet-node.md), and it is only affordable because [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md). (10:44-11:03)
- The failure mode to plan for is quota drift. The scheduler's queues carry manually specified resource amounts (CPU, NVIDIA GPUs, memory), and "at least our cluster is quite fluid. Nodes phasing in and out of existence. They go into maintenance, whatever. You lose a few nodes here and there. This number gets out of sync. And sometimes these would break gang scheduling." He notes the reconciliation can be automated and that they have not done it — a known, cheap, unbuilt fix worth doing before it bites. (09:47-10:20)
- An alternative he flags but has not tried: a recent Kubernetes release ships gang scheduling out of the box, "something very similar" to the project they use. The version digits in the captions are unreliable, so treat this as a direction to check rather than a version to pin.
- The payoff he claims is organizational rather than numerical: "changed the way we do research cuz no one else needs to care about GPUs. They just launch stuff… And we fully utilize the cluster for trainings. Production runs somewhere else." No utilization figures are given. (15:34-16:02)
- Scope: this policy fits a company whose training runs are the product roadmap and whose serving workload is relocatable. A team whose inference is latency-critical, stateful, or unable to run off-cluster inherits the eviction cost without the escape hatch, and should not adopt the priority order on its own.

Related topics:
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Evict Inference Off-Cluster Through a Virtual-Kubelet Node](evict-inference-off-cluster-through-a-virtual-kubelet-node.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Let Training Crash and Checkpoint Against a Fast Filesystem](let-training-crash-and-checkpoint-against-a-fast-filesystem.md)
- [Converge Agent Fleets on Cluster-Scheduling Primitives](converge-agent-fleets-on-cluster-scheduling-primitives.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Choose Reserved Pods for Iteration, Serverless for Autoscaling Load](choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md)

Sources:
- [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../sources/20260818_byn9PURoBNY.md), 08:53-11:03, 15:34-16:02
