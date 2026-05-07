# Match GPU Commitments To Workload Lifecycle

Summary: AI teams should align GPU commitments with changing workload phases instead of assuming a fixed reservation fits the whole model lifecycle. Training bursts, experiment spikes, and later inference hosting can require different quantities and contract shapes.

Use when:
- Deciding between annual reservations, on-demand capacity, spot capacity, and marketplace resale.
- Modeling GPU cost for a startup or team whose training and inference needs will change over months.

Details:
- Zhang's example starts with a team reserving GPUs for a year because it expects training and later inference demand, then discovering after experiments that it temporarily needs more training GPUs. 08:29-09:05
- After training finishes, the same team may only need part of the reserved fleet for hosting, leaving idle GPUs unless the platform supports release or resale. 09:05-09:19
- A flexible marketplace pattern lets the team keep a baseline reservation, burst for a shorter training window, and later release unused GPUs to other users, instead of buying every phase as a long fixed commitment. 09:19-10:25
- The talk frames lower GPU price as a productivity lever, not only a cost cut: if compute follows scaling-law behavior for the workload, the same budget can buy more experiments or larger training runs. 10:31-11:18
- Zhang says customers ultimately want to run training, online inference, and offline inference jobs, so compute platforms should expose workload-shaped access rather than only raw GPU ownership. 11:21-11:43

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Aggregate Idle GPU Supply Through Compute Marketplaces](aggregate-idle-gpu-supply-through-compute-marketplaces.md)

Sources:
- [Why We Don't Need More Data Centers - Dr. Jasper Zhang, Hyperbolic](../sources/20250801_M6Vbaig1TsM.md), 08:29-11:43
