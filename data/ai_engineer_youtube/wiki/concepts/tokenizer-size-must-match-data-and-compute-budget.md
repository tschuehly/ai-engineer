# Tokenizer Size Must Match Data and Compute Budget

Summary: Tokenizer design is a capacity and data-efficiency decision, not just preprocessing. Larger tokenizers can represent broader domains and languages, but they require more data and compute; tiny local runs may need character-level tokenization so the model can learn at all.

Use when:
- Choosing a tokenizer for a constrained training run.
- Explaining why a production tokenizer choice may fail in a small-data experiment.

Details:
- The workshop treats tokenizer selection as one of the first and most important decisions when creating a transformer model (09:12-09:39).
- A multilingual or larger model may need a huge tokenizer and therefore much more training data; for the local workshop, a character-level tokenizer with 65 symbols reduces embedding size and helps the model train under data limits (04:40-05:10, 09:54-10:17).
- Using a full tokenizer in the tiny local setup would not converge in the allotted time; BPE-style tokenizers are positioned as a common choice for proper LLM training with larger corpora and longer runs (12:12-13:49).
- Tokenizer training data matters by modality and domain: audio tokens trained on music data differ from tokens trained on voice data, and supporting both is harder than optimizing for one (01:19:04-01:20:08).
- Gemma 4 adds the production-side counterpart: a multilingual tokenizer based on Gemini's tokenizer can improve fine-tuning paths for low-resource languages because tokenization quality matters independently of raw model capability. (07:35-08:27)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Local LLM training exposes the core model-building stack](local-llm-training-exposes-the-core-model-building-stack.md)
- [Multilingual Tokenizers Improve Low-Resource Fine-Tuning Paths](multilingual-tokenizers-improve-low-resource-fine-tuning-paths.md)

Sources:
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md), 04:40-13:49
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md), 07:35-08:27
