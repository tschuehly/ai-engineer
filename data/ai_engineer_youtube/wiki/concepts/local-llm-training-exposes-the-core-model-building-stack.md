# Local LLM Training Exposes the Core Model-Building Stack

Summary: A small from-scratch local training run is useful because it forces the engineer to touch the durable parts of LLM construction: tokenizer, architecture, training loop, and inference. Higher-level libraries can hide these decisions, but the same components still shape production models.

Use when:
- Designing a hands-on model-training exercise that should teach fundamentals rather than only library usage.
- Debugging or reasoning about where a training problem might live in the model-building stack.

Details:
- The workshop explicitly avoids pretrained weights and model loading from libraries, using PyTorch and basic dependencies to expose how research engineers design models (01:22-01:55).
- The model is tiny enough to train locally or in Colab, but still has the same practical components: tokenizer, GPT-2-style causal decoder architecture, training loop, and inference/generation (02:22-02:43, 04:21-07:05).
- The repo organization mirrors this decomposition with files for tokenizer work, model architecture, training, and generation/inference (56:41-56:49).

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)
- [Use loss curves to debug local model training](use-loss-curves-to-debug-local-model-training.md)

Sources:
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md), 01:22-07:05
