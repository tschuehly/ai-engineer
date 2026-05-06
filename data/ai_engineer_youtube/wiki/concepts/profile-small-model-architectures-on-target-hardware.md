# Profile Small-Model Architectures on Target Hardware

Summary: Small-model architecture decisions should be validated on the real CPUs, GPUs, phones, and accelerators where the model will run, because theoretical operator efficiency may not predict product latency and memory behavior.

Use when:
- Selecting attention, convolution, or recurrent-style blocks for an on-device model.
- Benchmarking an edge model before committing to a training recipe or deployment target.

Details:
- Liquid AI chose to implement candidate architecture pieces on target hardware and profile real inference behavior instead of relying only on theoretical analysis. (04:31-04:53)
- The talk identifies a gated short-convolution block in LFM 2 as a hardware-friendly choice; compared with sliding-window attention, gated DeltaNet, gated linear attention, and GQA alternatives, short convolutions were framed as cheaper for latency-sensitive models. (04:53-05:25)
- Real profiling on AMD Ryzen Max Plus 395, Samsung Galaxy S25 Ultra, and GPU settings showed the LFM 2 short-convolution architecture running faster and using less memory, including high-concurrency GPU settings. (05:30-06:07)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Benchmark edge models across the device fleet before shipping](benchmark-edge-models-across-the-device-fleet-before-shipping.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 04:31-06:07
