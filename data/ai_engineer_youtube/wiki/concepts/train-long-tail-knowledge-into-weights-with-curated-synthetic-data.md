# Train long-tail knowledge into weights with curated synthetic data

Summary: For niche or private domains, weight updates can act as a memory layer when RAG and long context are too slow, shallow, or expensive. The practical pattern is not naive fine-tuning on raw documents, but transforming a small source corpus into diverse training examples and updating the model without destroying general capability.

Use when:
- A domain model needs to answer variant questions over a small private or specialized corpus.
- Comparing RAG, deep-research-style inference, and upfront model adaptation costs.

Details:
- The source frames long-tail knowledge as tasks where the model lacks facts because they are post-cutoff, private, too niche in pretraining, or unavailable at inference time. (00:46-02:21)
- Training knowledge into weights is presented as a third path beside full context and RAG. It spends more at data/training time so future inference can be cheaper than repeatedly retrieving or reading large context. (02:35-03:16, 21:33-22:14)
- Naively fine-tuning on a small document set can produce memorization rather than useful reasoning: the source describes a 3M financial-report experiment where the model could memorize the document but failed on slightly different prompts and became overly specific. (26:01-29:21)
- The source-backed repair is twofold: use better data and avoid updating the whole model indiscriminately. It cites approaches that extract entities and generate a much larger, diverse synthetic dataset that preserves the original facts, allowing training to answer variant questions rather than only exact copies. (28:44-32:26)
- This pattern challenges the idea that the only response to small private datasets is to collect more human data; current LLMs can help expand source facts into training distributions, but the resulting model still needs evaluation for overfitting and retained general behavior. (30:50-32:26)

Related topics:
- [Models](../topics/models.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)

Sources:
- [Jack Morris: Stuffing Context is not Memory, Updating Weights is](../sources/20251229_Jty4s9-Jb78.md), 00:46-03:16, 21:33-32:26
