# Benchmark Edge Models Across The Device Fleet Before Shipping

Summary: Edge deployment needs fleet-level benchmarking because success on one device does not prove reliability on older phones or diverse accelerators. The AI Edge Portal is presented as a cloud-based benchmark service for testing deployability across Android devices and choosing compilation or acceleration recipes.

Use when:
- Validating an on-device model before shipping broadly.
- Comparing CPU, GPU, NPU, ahead-of-time compilation, and just-in-time compilation tradeoffs.

Details:
- The talk calls out the practical question of whether a model works on five- or six-year-old phones, not just current development devices.
- AI Edge Portal is described as a cloud-based benchmarking service used by third-party and internal developers to get a pulse check before broad Android deployment.
- Benchmarking should inform whether to use ahead-of-time compilation or just-in-time compilation and which CPU/GPU/NPU acceleration path is reliable for the target fleet.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [LiteRT provides a cross-platform path from model conversion to edge deployment](litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md)
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 13:27-15:28
