# Match Gemma Edge Model Size To Device Memory And Interaction Class

Summary: Gemma 4 edge models are positioned for different device envelopes: E2B is aimed at lower-latency local interactions with roughly 1-2 GB RAM usage after quantization, while E4B targets heavier-duty platforms with higher memory budgets.

Use when:
- Choosing a small language model for phones, laptops, or IoT devices.
- Estimating whether an on-device voice, summarization, or local processing task can fit a target device.

Details:
- Gemma 4 E2B is described as using roughly 1-2 GB of RAM and fitting voice interfaces, summarization, and low-latency local processing.
- Gemma 4 E4B is described as heavier duty for bigger platforms such as laptops or IoT devices, with higher RAM requirements.
- The sizing discussion assumes quantization to the desired size, so memory planning should include the target quantization recipe.
- For iPhone MLX deployment, quantized weights are necessary because full-size weights are too large; the practical range is described as roughly 4-bit to 8-bit, with quality degrading noticeably below 4-bit. (04:41-05:18)
- Local model download size remains a product constraint: Locally AI users still need to download roughly 1-3 GB depending on the selected model. (07:12-07:30)

Related topics:
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Benchmark edge models across the device fleet before shipping](benchmark-edge-models-across-the-device-fleet-before-shipping.md)
- [Use MLX Swift LM For Apple Local Model Integration](use-mlx-swift-lm-for-apple-local-model-integration.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 03:10-03:47
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md), 04:41-05:18, 07:12-07:30
