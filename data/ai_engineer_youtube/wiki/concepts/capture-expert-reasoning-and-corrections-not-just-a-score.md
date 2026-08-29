# Capture Expert Reasoning and Corrections, Not Just a Score

Summary: The useful artifact from expert review is the reasoning and the correction, not the rating. Put real outputs in front of experts, let them leave free-form comments for a few focused hours, and keep what they wrote — a score compresses away exactly the part that a later judge needs, which is why this detail mattered in this case.

Use when:
- Designing an annotation schema and deciding between a rating scale, labels, and free text.
- Starting expert review with no budget for a formal labeling program.
- You have thousands of expert ratings and still cannot explain any of the scores.
- Deciding what to do first when building an eval capability from nothing.

Details:
- **The starting move, and its size.** "You put real outputs in front of your experts. Clinicians spend a focused few hours leaving comments. A session doesn't have to be a month-long labeling project to start with." The claim is that the first useful increment is hours, not a program — which matters because expert-time cost is the usual reason this step is deferred indefinitely. ([Fox](../sources/20260822_yqF6XhzbWBk.md), 14:39-14:59)
- **What to keep.** "You collect their judgment. Not just a score, but the reasoning and corrections. And over time, you build up that record of how your experts actually judge." The record of *how they judge* is the asset; the scores are a byproduct. (14:59-15:18)
- **Why the reasoning is the part that transfers.** The standard being captured is materiality — which of several true differences mattered here — and that is what a numeric score erases. A rating of 3 on two structurally identical omissions carries no information about why one was noise and the other was the diagnosis; the comment does. (11:56-12:36, and see [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md))
- **The closing recommendation is this step alone.** "If you take one thing away, the easiest place to start is your experts leaving free-form comments on real outputs. That's the raw material for everything else." Free-form is specified deliberately: a structured form can only collect the dimensions someone already named, which is the same limitation that defeats a pre-specified rubric. (18:31-18:52)
- **What the captured material is consumed by.** Corrections and past judgments become the corpus retrieved at scoring time — "the corrections that apply, like a new headache over 50 suggests something that you need to check red flags on" — so annotation is not a dataset-building exercise that ends, but the write path of a live system. See [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md). (13:19-13:36, 15:59-16:43)
- **What organizes the capture.** The discovered failure modes decide "what you ask your experts about" and "how you index the cases that you'll retrieve," so review is targeted at named modes rather than being an undirected read of production traffic. (14:39-14:59)
- **Unaddressed in the source, and worth planning for.** No adjudication step is described for disagreeing experts, even though the talk itself names disagreement as a reason the standard moves ("two good doctors disagree, different hospitals have different definitions"). The wiki's other procedure handles this explicitly by having a third expert adjudicate two independently written rubrics and a fourth QA the result: [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md). Free-form capture is cheaper per item and inherits the disagreement it was cheap enough to collect.
- **Relation to expert review tooling.** [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md) describes the mature surface — evidence, AI reasoning, correctness marking, failure-mode label, suggested domain knowledge, routed through a release gate. This page is the version that precedes any tooling: a comment box on real outputs, which is the minimum artifact that still carries reasoning.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md)
- [Label LLM Judge Outputs Before Mapping Them to Scores](label-llm-judge-outputs-before-mapping-them-to-scores.md)
- [Assemble the Judging Standard Per Output From Retrieved Precedent](assemble-the-judging-standard-per-output-from-retrieved-precedent.md)
- [Discover Failure Modes From Production Outputs, Not Synthetic Cases](discover-failure-modes-from-production-outputs-not-synthetic-cases.md)
- [Treat Every Human-AI Interaction as a Training Label](treat-every-human-ai-interaction-as-a-training-label.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 11:56-12:36, 13:19-13:36, 14:39-15:18, 15:59-16:43, 18:31-18:52
