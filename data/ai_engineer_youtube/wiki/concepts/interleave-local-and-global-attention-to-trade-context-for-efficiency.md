# Interleave Local And Global Attention To Trade Context For Efficiency

Summary: Interleaving local sliding-window attention with periodic global attention lets a model reduce repeated full-context cost while still passing broader context through selected layers.

Use when:
- Evaluating long-context or edge-friendly model architectures.
- Reasoning about why attention-layer placement and key/value head grouping affect serving cost.

Details:
- Gemma 4 uses a 5:1 local-to-global layer ratio for most dense models and a 4:1 ratio for the smaller effective 2B model. (04:31-04:47)
- Local layers attend only to a sliding window, described as 512 tokens in smaller models and 1,024 tokens in larger models, while global layers attend to all preceding tokens. (04:47-05:24)
- The final layer is kept global so the last layer can attend across all preceding tokens rather than only a local window. (04:53-05:03)
- Global layers remain memory intensive because they must attend to all preceding tokens, so Gemma 4 uses grouped query attention to reduce key/value head cost. (05:37-06:08)
- The source describes grouping two queries per key/value head in local layers and eight queries per key/value head in global layers, with doubled key/value head length in global layers to protect performance. (05:55-06:22)

Related topics:
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Profile small-model architectures on target hardware](profile-small-model-architectures-on-target-hardware.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md), 04:24-06:43
