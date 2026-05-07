# Aggregate Idle GPU Supply Through Compute Marketplaces

Summary: AI compute shortages can be treated as an allocation problem as well as a construction problem. A GPU marketplace can aggregate fragmented idle capacity into a usable pool when it provides orchestration, pricing, and workload access above individual data centers.

Use when:
- Planning AI infrastructure capacity before committing to long data-center or cloud reservations.
- Comparing build-more-capacity strategies with pooling and resale of existing accelerator supply.

Details:
- The talk argues that data-center construction remains important, but building data centers alone does not solve demand, cost, grid-connection, energy, and sustainability constraints. 00:31-00:41, 02:38-03:53
- Zhang frames enterprise GPU underutilization and fragmented GPU clouds as a matching problem: some users cannot find affordable GPUs while existing GPUs sit idle in data centers or clouds. 03:54-04:35
- The proposed pattern is a marketplace or aggregation layer that connects GPU users with multiple data centers and providers, making GPUs available through one distribution channel rather than many supplier negotiations. 04:35-04:49, 07:21-07:59
- Hyperbolic's example uses a Kubernetes-like agent called HyperDOS so a participating cluster can join a global orchestration layer, while users rent spot, on-demand, reserved, or hosted-model capacity. 05:03-05:40, 13:11-14:11
- The marketplace is positioned as a utilization and sustainability lever because idle compute can be resold or reused instead of requiring every user to over-reserve dedicated capacity. 10:21-10:29, 11:54-12:24

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Benchmark And Rate Heterogeneous GPU Providers](benchmark-and-rate-heterogeneous-gpu-providers.md)

Sources:
- [Why We Don't Need More Data Centers - Dr. Jasper Zhang, Hyperbolic](../sources/20250801_M6Vbaig1TsM.md), 00:31-14:11
