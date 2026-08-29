# Profile Small-Model Architectures on Target Hardware

Summary: Small-model architecture decisions should be validated on the real CPUs, GPUs, phones, and accelerators where the model will run, because theoretical operator efficiency may not predict product latency and memory behavior.

Use when:
- Selecting attention, convolution, or recurrent-style blocks for an on-device model.
- Benchmarking an edge model before committing to a training recipe or deployment target.

Details:
- Liquid AI chose to implement candidate architecture pieces on target hardware and profile real inference behavior instead of relying only on theoretical analysis. (04:31-04:53)
- The talk identifies a gated short-convolution block in LFM 2 as a hardware-friendly choice; compared with sliding-window attention, gated DeltaNet, gated linear attention, and GQA alternatives, short convolutions were framed as cheaper for latency-sensitive models. (04:53-05:25)
- Real profiling on AMD Ryzen Max Plus 395, Samsung Galaxy S25 Ultra, and GPU settings showed the LFM 2 short-convolution architecture running faster and using less memory, including high-concurrency GPU settings. (05:30-06:07)
- A live MLX demo showed Gemma 4 8-bit quantized to 4-bit running offline on a recent iPhone at roughly 40 tokens per second; the speaker notes that older iPhones may be closer to 20 tokens per second but still useful for many app workflows. (05:39-07:04)
- **The same lesson at the kernel layer, with a failure case.** Tuning that is not re-derived on the target hardware does not survive the move: Triton-distributed, "originally tuned around 8 H800 GPUs, fails to adapt efficiently to other architectures like H100s" — a within-vendor, within-generation-neighbourhood change. Hardware sensitivity is why the multi-GPU generation tasks in the same talk hand the model "a system topology that specifies the number of ranks and intra-node hardware configuration" as part of the problem statement rather than assuming a default. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 12:56-13:27, 22:16-22:26)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Benchmark edge models across the device fleet before shipping](benchmark-edge-models-across-the-device-fleet-before-shipping.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Use MLX Swift LM For Apple Local Model Integration](use-mlx-swift-lm-for-apple-local-model-integration.md)
- [Measure Multi-GPU Headroom Against a Communication-Aware Roofline](measure-multi-gpu-headroom-against-a-communication-aware-roofline.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 04:31-06:07
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md), 05:39-07:04
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 12:56-13:27, 22:16-22:26
