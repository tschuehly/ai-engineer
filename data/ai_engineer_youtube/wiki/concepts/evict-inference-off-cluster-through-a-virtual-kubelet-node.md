# Evict Inference Off-Cluster Through a Virtual-Kubelet Node

Summary: A fake Kubernetes node backed by virtual-kubelet turns "rent GPUs from an external provider" into ordinary pod scheduling. Pods that cannot fit on real in-cluster GPUs land on the fake node, where your own provider implementation deploys them to whatever external capacity you have a deal with, and reconciles the two sides. A metrics-driven taint on that node decides which way new pods go, and a descheduler — not a NoExecute taint — walks them back gradually when local GPUs free up. The result is that a training run can take the whole cluster without production going down, and nobody has to operate the failover.

Use when:
- Inference must yield capacity to training (or any higher-priority workload) without dropping traffic.
- You have burst GPU capacity at an external provider and want it addressable through the same scheduler.
- Building a spillover or failover path that operators should not have to run by hand.
- Choosing between Kubernetes eviction primitives for a migration that must not happen all at once.

Details:
- The user-visible behavior first: "there is this magical system… that allows us to flip traffic between clusters magically. And not just clusters, and like external providers, GPU rentals, whatever… someone launches a train, and then suddenly [pods] start flipping to the other cluster, and then training is done… it flips back. So, we stop wasting money. And this is seamless. No one needs to think about it." ([Menezes](../sources/20260818_byn9PURoBNY.md), 11:04-11:38)
- The primitive: "there's this very nice project called virtual kubelet, also open source… It is a very nice code base. And this works by creating a fake machine in Kubernetes… a fake machine that is like up to you to control how it works. So, Kubernetes does normal scheduling as you would expect. Things would go into these nodes." When every real GPU is in use, "this pod goes into the virtual kubelet node, and in there you can do whatever." The scheduler keeps its usual semantics; only the node's implementation is yours. (11:56-12:24)
- What you write on top is a provider adapter: "you receive the pods back, and then you find a provider… Let's say you have a deal with some provider that gives nice prices. You integrate into here. We built like some nice interfaces to… not leak things. So we just implement a provider, and there is an algo that decides which one it goes [to]. You translate this back of the pods into the provider stuff, and you deploy, and then you have something that reconciles between the both sides." The interface boundary is deliberate — multiple providers behind one selection algorithm, with provider details kept from leaking upward. (12:24-12:52)
- Failure handling comes free from the control plane and is the part most likely to be over-engineered. With the horizontal pod autoscaler managing replicas, "if something fails… you don't need to handle the fail. The only thing you need to handle is like, 'Oh, something failed.' You mark the pod as failed. Kubernetes… detect[s] that something has failed and create[s] a new one. You don't need to try to save the world… If something breaks on your side, [or] on the other side, just mark it as failed, let Kubernetes handle it, create a new one, and things keep working." (12:53-13:41)
- Direction is controlled with a taint on the fake node, so the routing decision is declarative rather than a control loop that moves pods around. When the cluster has spare GPUs, "this adds a taint into the node… nothing can schedule on it. So, we stop wasting GPUs. Like the pods, they go into the GPUs in the cluster, we don't waste money." When a training run "is going to hog all of the GPUs, no GPUs in the cluster. The system detects this, removes the taint, new pod schedules there." (13:41-14:37)
- The signal is deliberately boring: "for us, for example, we use just some Prometheus metrics. That's how we do it, very simple, but it works very, very, very well." (14:37-14:43)
- Coming back is a separate component and a separate problem, because the taint alone only affects *new* placements: "now we have pods running on the other side, you're wasting money… you run something else that detects the system and removes things back. In this case, a descheduler. Once the taint's added back… the descheduler says, 'Oh, these pods, they don't tolerate the taints. I'm going to migrate them back.'" (14:56-15:17)
- The sharpest reusable detail is why the obvious primitive is wrong: "you can ask, 'Oh, why you don't use a NoExecute taint?' NoExecute in Kubernetes would kick everything out at the same time. So, at [the] moment you put the taints, everything will be kicked out and that's bad. Production would go down. So, this system slowly migrates the pods back, so production doesn't go down and we don't waste money." Gradual, rate-limited migration is the requirement; NoExecute is a correct-looking primitive whose semantics are all-at-once. (15:17-15:34)
- Maturity note, stated plainly: "it is a very self-healing system. You don't need to interfere with it. It just runs. Yes, of course, there was bugs at the beginning. Nothing's perfect. But like once you calibrate it… worked very well." Calibration of the metric thresholds and migration rate is the real work; the mechanism is assembled from existing parts. (15:34-15:50)
- Preconditions worth checking before copying this: the workload must be relocatable across providers (theirs is single-node diffusion-transformer inference — see [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)), and the external capacity has to be pre-negotiated. Data residency, model-weight distribution, and cold-start time at the remote provider are not discussed in the talk.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Give Training Priority Over Production on a Shared GPU Cluster](give-training-priority-over-production-on-a-shared-gpu-cluster.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md)
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Converge Agent Fleets on Cluster-Scheduling Primitives](converge-agent-fleets-on-cluster-scheduling-primitives.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../sources/20260818_byn9PURoBNY.md), 11:04-15:50
