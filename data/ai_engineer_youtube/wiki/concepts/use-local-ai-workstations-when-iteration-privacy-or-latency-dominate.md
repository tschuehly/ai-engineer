# Use Local AI Workstations When Iteration, Privacy, or Latency Dominate

Summary: Local AI workstations are useful when development speed, privacy-sensitive data, cost predictability, or deterministic latency matter enough to bring model serving closer to the developer. They complement cloud and data-center infrastructure rather than replacing it.

Use when:
- Deciding whether a workload should run locally, in shared infrastructure, or in a hosted API.
- Prototyping or fine-tuning open models before scaling to a larger deployment target.

Details:
- Shared cloud or data-center infrastructure can slow iteration when developer jobs are scheduled against competing workloads; local systems reduce that queueing loop for hands-on experimentation. (00:57-01:36)
- Local LLM infrastructure becomes more attractive as production concerns shift from pure capability to cost predictability, data residency, and deterministic latency. (00:57-01:09)
- The talk frames DGX Spark/Jetson Spark as a desk-side system for building and running AI locally with the same NVIDIA AI software stack used in production, so workflows can move from desktop to data center or cloud with minimal changes. (01:39-02:37)
- The intended use cases are steady-state workloads, privacy-sensitive data, and rapid prototyping, with a run-locally, iterate-quickly, then scale-to-cloud workflow. (09:23-10:07)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Use hosted model playgrounds to prototype before owning infrastructure](use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md)
- [Use MLX Swift LM for Apple local model integration](use-mlx-swift-lm-for-apple-local-model-integration.md)
- [Open model families need ecosystem-compatible tooling](open-model-families-need-ecosystem-compatible-tooling.md)

Sources:
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md), 00:57-02:37, 09:23-10:07
