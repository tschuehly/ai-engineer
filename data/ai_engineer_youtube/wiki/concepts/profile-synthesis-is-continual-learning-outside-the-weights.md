# Profile Synthesis Is Continual Learning Outside the Weights

Summary: The running-profile loop already is a continual learning system — profile shapes conversations, conversations feed the next synthesis, synthesis rewrites the profile — it just runs in text rather than in parameters. The barrier to moving it into per-user weights is stated as economic rather than technical: enterprise training amortizes across many users, individual personalization does not.

Use when:
- Someone claims continual learning is a future capability and personalization must wait for it.
- Weighing per-user fine-tuning or adapters against a text-based profile loop.
- Explaining why an enterprise continual-learning story does not transfer to a consumer product.

Details:
- The loop, spelled out: the profile starts as what the model knows about you and is applied to every conversation; each conversation brings new information; the update pass synthesizes it back into the profile; the profile then shapes the next conversations, "and this loop keeps repeating itself again and again and again. And what you have is a continual learning process" (13:47-14:19).
- Where it runs: "obviously this learning loop is happening outside the weights" (14:19-14:24). The open question is whether it ever moves inside them (14:24-14:32). The speaker prefaces the section with "I'm not an expert here" (13:37-13:44).
- The economic argument for why it has not: training is expensive, and "continuous learning does make sense at an enterprise level because the costs of these models are amortized across different employees, different customers, but that's not the case at an individual level" (14:32-14:54). Per-user weight updates have a denominator of one.
- Three open questions named and left open: will each of us get our own self-learning model; what data is needed to kick the process off and how is it generated; and who pays for it (14:54-15:12). He points to an essay titled "Guardian Angels" for the one-model-per-person future (15:12-15:32); the author's name is not recoverable from the captions.
- The practical consequence for builders: the text-based loop is available today and its operating point is a compute choice you control, whereas the weights-based version is gated on an amortization problem no architecture fixes.
- Ceiling shared with every other memory design: even a perfect per-user weight-update loop stays capped by how much context the system can gather about the person (15:32-16:03).

Related topics:
- [Models](../topics/models.md)
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Memory Quality Is Capped by the Context It Can Reach](memory-quality-is-capped-by-the-context-it-can-reach.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [Verifiable Continual Learning: Prove Each Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 13:37-16:03
