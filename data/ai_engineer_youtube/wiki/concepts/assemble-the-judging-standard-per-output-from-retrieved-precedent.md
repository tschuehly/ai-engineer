# Assemble the Judging Standard Per Output From Retrieved Precedent

Summary: Instead of handing the judge one fixed rubric, retrieve a standard for each output: the most similar previously judged cases and how they scored, the expert corrections that apply, and the reference documents in force. The judge is not being taught the case — it is a capable model that already knows the facts and only lacks a sense of what matters here.

Use when:
- Building an LLM judge for a domain where materiality depends on the case rather than on the output's shape.
- A single rubric scores two superficially identical outputs the same way when experts score them differently.
- You already collect expert corrections and want them to affect scoring without a retrain or a rubric rewrite.
- Applying context-engineering practice to the evaluation path rather than the generation path.

Details:
- **The assembly rule.** "For each output, your judging agent pulls in everything that bears on this one case: its memory of the most similar outputs that it's judged before and how they scored, the expert corrections that apply, the reference documents and guidelines. Just context engineering per output." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 15:18-15:39)
- **Stated as a three-way contrast, which is how to read it:** "not just one pre-specified rubric in a vacuum, and not a model that you have to retrain every week, but a full case-specific standard assembled for this output." The retrieved bundle replaces the rubric's role as the standard, not the judge's reasoning. (15:39-15:59)
- **The worked retrieval, for the opening case.** For a note that filed a possible blindness emergency as a routine headache, the assembled context is: "the nearest cases that your experts have judged — not this exact patient, but the same shape, maybe a red flag filed as routine"; "the corrections that apply, like a new headache over 50 suggests something that you need to check red flags on"; and "some criteria and guidelines." Note the retrieval key: cases of the same *failure shape*, not of the same clinical content. (15:59-16:43)
- **What the retrieval is supposed to supply, and what it is not.** "It hasn't memorized this case. It's a capable model, and handed the right context to reason from, held against that, the dropped red flag stands out. It was never actually hard to catch. It just didn't know what mattered." The retrieved material carries the *priority ordering*, not the domain knowledge — the model is assumed to have the facts already. That is a different design goal from RAG for generation, where retrieval usually supplies facts the model lacks. (16:20-17:02)
- **Why it composes into a loop rather than a one-time build.** "Every output you judge, every correction, sharpens the next. And when a brand new failure mode appears, discovery surfaces it and it flows straight back in." The corpus is written by the same review activity that consumes it, which is what makes "add one and it's live on the next call" a property rather than an aspiration. (13:19-13:36, 15:39-15:59)
- **What the discovered failure-mode ontology does here.** It is the retrieval index, not a checklist: the modes "organize everything… what you ask your experts about, how you index the cases that you'll retrieve." See [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md). (14:19-14:59)
- **Unspecified, and load-bearing.** The talk gives no retrieval implementation: no similarity function, no k, no handling of the case where nothing similar has been judged yet (the cold start is exactly the high-stakes novel case), no cost or latency figure, and no defense against a bad precedent propagating. A judge whose standard is retrieved also inherits retrieval's failure modes, including the wiki's finding that [dense retrieval collapses on buried facts as the haystack grows](dense-retrieval-collapses-on-buried-facts-as-the-haystack-grows.md) — a growing judgment corpus is a growing haystack.
- **Where it sits among the wiki's judge designs.** [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md) makes each judge's question small enough to answer reliably; this makes each judge's *reference* specific enough to answer against. The two are orthogonal and compose — a narrow binary metric can still be scored against retrieved precedent for what counts as a violation in this case.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md)
- [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md)
- [Capture Expert Reasoning and Corrections, Not Just a Score](capture-expert-reasoning-and-corrections-not-just-a-score.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)
- [Rank Agent Memory by Outcome Utility, Not Just Similarity](rank-agent-memory-by-outcome-utility-not-just-similarity.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 13:19-13:36, 14:19-17:02
