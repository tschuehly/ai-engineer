# Match Gemma Edge Model Size To Device Memory And Interaction Class

Summary: Gemma 4 edge models are positioned for different device envelopes: E2B is aimed at lower-latency local interactions with roughly 1-2 GB RAM usage after quantization, while E4B targets heavier-duty platforms with higher memory budgets.

Use when:
- Choosing a small language model for phones, laptops, or IoT devices.
- Estimating whether an on-device voice, summarization, or local processing task can fit a target device.

Details:
- Gemma 4 E2B is described as using roughly 1-2 GB of RAM and fitting voice interfaces, summarization, and low-latency local processing.
- Gemma 4 E4B is described as heavier duty for bigger platforms such as laptops or IoT devices, with higher RAM requirements.
- The sizing discussion assumes quantization to the desired size, so memory planning should include the target quantization recipe.

Related topics:
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Benchmark edge models across the device fleet before shipping](benchmark-edge-models-across-the-device-fleet-before-shipping.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 03:10-03:47
