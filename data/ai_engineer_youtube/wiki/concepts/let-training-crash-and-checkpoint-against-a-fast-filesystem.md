# Let Training Crash and Checkpoint Against a Fast Filesystem

Summary: At cluster scale, failures stop being incidents and become a rate. Chasing each one — swapping nodes, changing nodes, root-causing every stall — costs more GPU-hours than it saves, because the same machines running the same code and the same data will often go 24 hours on the next attempt. The cheaper posture is to make a crash inexpensive: replace suspect hardware on a threshold instead of debugging it, and checkpoint often enough that a crash costs minutes. That posture has one hard prerequisite, which is a filesystem fast enough that frequent checkpoints do not slow training down.

Use when:
- A pre-training or long fine-tuning run is crashing often enough that the team is debugging instead of training.
- Choosing a checkpoint interval, or arguing for storage spend on a training cluster.
- Deciding whether to quarantine, replace, or investigate a node that looks marginal.
- Setting expectations for how long an uninterrupted run at N GPUs should last.

Details:
- Failures scale with the cluster, and that part is unsurprising: small ablations "would like run for days," but at 128, 256, 512 GPUs "things are crashing more. That's expected… there's more surface area for things to break." What makes it operationally hard is that "a lot of the times things would go wrong in silent ways… NCCL timeouts, like just crashes and… the metrics are all good." ([Menezes](../sources/20260818_byn9PURoBNY.md), 03:02-03:34)
- The behavioral finding that justifies the posture: "at the beginning we were like paranoid, swap node, change node, whatever… And we learned that like sometimes you just let it crash. It crashes, like it runs for like an hour, crash, runs for an hour, crash, and then runs again on the same set of machines, same code, same data for like 12 hours, 16 hours, 24 hours." Identical inputs producing an hour and then a day of uptime is the evidence that the per-crash investigation usually has nothing to find. (03:35-03:51)
- Calibrate against a published baseline, but expect to be worse than it: a Meta paper (unnamed in the talk) "gives you a like rough estimate of like how many failures you should expect… we kind of saw the same pattern but like not the same numbers. Our runs would last way way less than this." The stake is throughput, not tidiness: "you can imagine doing large-scale pre-training on runs that last less than 8 hours, it is a problem… You want [to keep] those GPUs fed, and if things are crashing, you are not doing progress and losing time and models are going to be late." (03:52-04:19)
- Threshold-based replacement rather than diagnosis is the same principle applied to hardware. A GPU running hotter than its neighbors throttles and destabilizes the whole synchronous run, so their rule is: "if there is any GPUs above like 78°, you remove them. Don't think about it. Don't try to fix. Don't try to be smart. You just remove the GPU… just ask your provider… this GPU's hot. Please replace it." NVLink error counters serve the same function at node granularity — see the counters in [GPU Utilization Is a Lie](measure-tensor-core-utilization-not-gpu-utilization.md). (04:46-05:17, 07:12-07:45)
- Checkpointing is the absorber: "our trains would crash constantly and a hacky way… to fix the problem [is] just checkpoint. Use and abuse the file system that you have." (07:56-08:02)
- The numbers that make "use and abuse" literal: their worker cluster sustains about 1.8 TB/s of reads and nearly 1 TB/s of writes, "and the file system would not choke on the training. So, we could checkpoint every like 30 minutes, 20 minutes, produce like a terabyte of data in like less than 30 seconds. So, this would not delay trainings." The design target is that a checkpoint is short relative to the interval, which is what lets the interval be tightened until a crash costs an acceptable amount of work. (08:19-08:43)
- The storage decision is a trust decision, and their first choice failed it: "At the beginning we use Ceph. Ceph didn't work well. Was very annoying. It broke. We lost trust in data. So, I recommend if you have the money go with something paid… cuz you can trust your data. You can see numbers." He names no replacement product. The reported failure is operational trust under this workload, not a general verdict on Ceph, and the recommendation is explicitly budget-conditional. (08:02-08:19)
- Note the division of labor with the metrics argument: metrics are not for explaining individual crashes, which this concept declines to do. They are for finding the *systematic* faults — a hot card, a node with NVLink errors, a fabric with rising wait times — that a let-it-crash policy would otherwise let bleed indefinitely.
- Scope caveat: these are numbers from one image-diffusion pre-training cluster, and the speaker concedes the crash rate may be "maybe skill issue on our part, maybe our cluster." The transferable parts are the policy shape (replace on threshold, checkpoint on a fast filesystem) and the ratio to design for (checkpoint write time far below checkpoint interval), not the specific 20-30 minute cadence.

- **The checkpoint is cheap to write and expensive to move, and those are different problems.** The 1.8 TB/s reads and ~1 TB/s writes here make a terabyte checkpoint a sub-30-second local operation; Modal's RL talk measures the same artifact across a network and reports a frontier-scale checkpoint at "like 500 gigabytes, normally take multiple minutes to hours" to sync. A fast local filesystem is what makes checkpointing viable as a *crash absorber*; it does nothing for checkpointing as a *distribution mechanism*, which needs a different unit entirely ([Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)). ([Modal](../sources/20260810_maRzp4kImJ4.md), 05:25-06:02)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [GPU Utilization Is a Lie: Instrument Tensor Cores and the Fabric](measure-tensor-core-utilization-not-gpu-utilization.md)
- [Give Training Priority Over Production on a Shared GPU Cluster](give-training-priority-over-production-on-a-shared-gpu-cluster.md)
- [Inference Tolerates Degraded GPUs That Training Cannot](inference-tolerates-degraded-gpus-that-training-cannot.md)
- [Stack Memory Optimizations to Train Long-Context Transformers](stack-memory-optimizations-to-train-long-context-transformers.md)
- [Run Elastic Training on Serverless GPU, Not a Reserved Cluster](run-elastic-training-on-serverless-gpu-not-a-reserved-cluster.md)

Sources:
- [Infra behind Krea 2: How to train and serve at scale — Gabriel Jorge Menezes, Krea.ai](../sources/20260818_byn9PURoBNY.md), 03:02-08:43
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 05:25-06:02
