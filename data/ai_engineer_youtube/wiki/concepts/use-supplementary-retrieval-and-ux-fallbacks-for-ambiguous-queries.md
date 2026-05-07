# Use Supplementary Retrieval and UX Fallbacks for Ambiguous Queries

Summary: Ambiguous queries often need more retrieval surfaces, not just a better single ranker. When the system cannot confidently infer intent, it should fan out, retrieve supplementary evidence, and degrade the product experience to broad choices or clarification instead of pretending it knows the one right answer.

Use when:
- A short or ambiguous user query could map to multiple intents, content types, or backends.
- The retrieval system has exhausted ranking improvements but still returns brittle answers.

Details:
- Query orchestration should ask whether the system is sending the right query to the right backends; ambiguous requests may need domain calibration before search can work (14:02-14:25).
- Supplementary retrieval increases recall by calling more search backends or retrieval surfaces when the query is under-specified; the "falafel" example could need restaurants, images, recipes, or facts depending on intent (14:25-15:31).
- Cost is the limiting factor for broad fan-out; teams should avoid being skimpy while recall is the priority, but watch for real cost overload once many backends and queries run (15:31-16:13).
- Product design is part of the retrieval answer: if the system understands less, it can show several options and let the user choose; if it understands more, it can confidently narrow the experience (17:14-19:06).

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Tune Inference to the Application Pareto Point](tune-inference-to-the-application-pareto-point.md)

Sources:
- [Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)](../sources/20250729_w9u11ioHGA0.md), 14:02-19:06
