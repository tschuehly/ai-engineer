# Post-Training Data Is Public by Construction

Summary: The expert-authored post-training layer that data-acquisition vendors sell is public data by definition, not by accident — anything written so a model can say it back to a user is, at that moment, publicly available. That argument closes the last apparent escape hatch from "frontier models only know public things," and it is why buying more expert annotation cannot give a model depth in your private domain.

Use when:
- Someone argues that expert-labeled post-training data means the frontier models will eventually cover your domain.
- Deciding whether to fund annotation vendors or to build a loop over your own corpus.
- Explaining why frontier capability gains keep landing on public tasks and skipping private ones.

Details:
- The claim, in full: models now "have this new layer of post training data that's like experts that are hired through data acquisition companies like Scale AI, Surge AI, and Mercor. But, they're still by definition creating publicly available data because it's something that the model could tell to a user." ([Engram](../sources/20260812_WiqDvX6isc4.md), 05:47-06:04)
- The definitional move is the useful part. "Public" here does not mean *already on the internet* — it means *disclosable*. Data commissioned so that a general model can serve it to any customer is, by that intent, not private to any one of them. Confidentiality and utility are in tension by construction, not by policy failure.
- The observable consequence: models are "really good at Wikipedia. They know everything about Reddit, papers on arXiv, code on GitHub," and keep improving at "coding in the way that is public on GitHub" and "math in ways that are written in public textbooks" — while "they're not getting more knowledge of you or your life or your work." ([Engram](../sources/20260812_WiqDvX6isc4.md), 05:38-05:47, 07:03-07:15)
- The corollary the talk states as a paradigm-level indictment: "It's like the core problem with the current paradigm in AI that models cannot acquire new knowledge after training in a personalized way." ([Engram](../sources/20260812_WiqDvX6isc4.md), 04:03-04:11)
- Note what this does *not* claim. Rare-but-public knowledge is a separate failure with a separate fix — the AMD-kernel example is public code that is simply scarce, so more of it would help, whereas no volume of purchased annotation reaches your meeting transcripts. Keep the two apart when deciding whether to wait for the next model. ([Engram](../sources/20260812_WiqDvX6isc4.md), 03:02-03:24)
- **Where this sharpens an existing wiki claim.** [Private Microworlds Are the Next Training-Data Opportunity](private-microworlds-are-the-next-training-data-opportunity.md) argues from data exhaustion — the public supply is used up, so private worlds are next. This argument is stronger and does not need that premise: even with unlimited annotation budget the purchased layer stays public by definition, so the private axis is untouched whether or not the public one is exhausted. The two together also name the same tension from opposite ends: Su's "channel back the learning to the general model" would make a customer's private data disclosable, which is exactly the property that defines it out of privacy here.
- Provenance: asserted in a vendor-framing talk by a researcher at a startup selling private-corpus adaptation; the vendors named (Scale AI, Surge AI, Mercor) are described from the outside and no contract terms are cited. The argument is definitional and stands or falls on its own logic rather than on evidence. ([Engram](../sources/20260812_WiqDvX6isc4.md), 05:47-06:04)

Related topics:
- [Models](../topics/models.md)
- [Product Strategy](../topics/product-strategy.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Only the Compute Axis Is Available on Your Own Corpus](only-the-compute-axis-is-available-on-your-own-corpus.md)
- [Private Microworlds Are the Next Training-Data Opportunity](private-microworlds-are-the-next-training-data-opportunity.md)
- [Digital Work Is Millions of Microworlds With Local Physics](digital-work-is-millions-of-microworlds-with-local-physics.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)
- [Specialize Models Against Private Benchmarks With RL](specialize-models-against-private-benchmarks-with-rl.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)

Sources:
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 03:02-06:04, 07:03-07:15
