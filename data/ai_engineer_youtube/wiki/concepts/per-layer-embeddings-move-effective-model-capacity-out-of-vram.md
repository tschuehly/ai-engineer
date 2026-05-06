# Per-Layer Embeddings Move Effective-Model Capacity Out Of VRAM

Summary: Per-layer embeddings let Gemma 4 effective models add representational depth while storing the extra embedding table in flash memory instead of scarce on-device VRAM.

Use when:
- Investigating how an on-device model can advertise larger representational capacity than its active operating parameter count.
- Reviewing memory tradeoffs for phones and laptops where VRAM pressure blocks local inference.

Details:
- The source defines "effective" model sizing as the number of parameters required to operate the model, distinct from total representational parameters. (07:47-08:02)
- Gemma 4 E2B is described as operating at 2.3B parameters while having 5.1B representational parameters. (08:02-08:10)
- Per-layer embeddings add a dedicated embedding table for each model layer while preserving the ordinary token embedding table. (08:25-09:26)
- The PLE table is stored in flash memory rather than VRAM, which matters because VRAM is a primary constraint for phones and laptops. (09:28-09:49)
- PLE uses a smaller 256-dimensional embedding and projects it up to the full embedding size expected by the model at each layer. (09:57-10:48)
- Omar Sanseviero describes E2B as effectively 2B parameters even though the model has more total parameters, because PLE lookup data does not need the same GPU-resident matrix multiplication path as ordinary transformer weights. (05:28-06:44)
- The same talk notes that llama.cpp can move per-layer embeddings to CPU or disk with an override tensor flag, which is a concrete runtime implementation path for the memory tradeoff. (06:45-06:55)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Treat edge models as their own architecture class](treat-edge-models-as-their-own-architecture-class.md)
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)

Sources:
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md), 07:42-10:56
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md), 05:28-06:55
