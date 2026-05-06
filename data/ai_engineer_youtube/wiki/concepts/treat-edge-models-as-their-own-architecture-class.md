# Treat Edge Models as Their Own Architecture Class

Summary: Edge-scale models should be designed around memory, latency, and narrow task fit instead of treated as simple miniature versions of large chat models.

Use when:
- Choosing whether an on-device model can serve a product workflow.
- Reviewing whether a small-model architecture is wasting scarce memory on components that do not improve the target capability.

Details:
- Small models are memory-bound on phones, cars, and other local hardware, which constrains knowledge capacity and makes them poorly suited to broad general-purpose chatbot behavior. (01:01-01:49)
- Latency sensitivity is a first-order requirement for edge workloads, so architecture choices should optimize throughput and memory footprint for the actual interaction class. (01:51-02:07)
- Large embedding layers can dominate tiny-model parameter counts without increasing effective reasoning capacity; the source gives Gemma 3 270M as 63% embedding parameters and Gemma 2.5 0.8B as 29%. (02:27-03:58)
- The practical design stance is to optimize the architecture, pre-training stack, and post-training process for edge models as a distinct class rather than shrinking a large-model recipe and accepting its failure modes. (15:03-15:28)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 01:01-03:58
