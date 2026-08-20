# Co-Optimize Data With the Model or the Search Does Not Pay

Summary: An automated training-search system that treats data as an agent decision — "should I generate more data or not?" — reportedly returns nothing until data quality is controlled and optimized on the same footing as the model. The fix described is to run every adaptation you would run on the model over the data too, inside one loop, rather than leaving the data to the agent's judgment.

Use when:
- Building or evaluating an automated ML / auto-research system that searches over architectures, hyperparameters, or recipes.
- Deciding what belongs inside an optimization loop and what can be delegated to an agent's discretion.
- Diagnosing why an architecture or hyperparameter search shows no lift on your task.
- Reading a claim that an automated pipeline "outperforms researchers" and looking for the precondition that made it true.

Details:
- The reported negative-then-positive result, from the team that built AutoScientist: "This only worked when we co-optimized the data. Uh so, there's a lot of auto research projects right now, which basically treat data as… the agent… decides whether to create data or not or what to do. Frankly, we did not get the returns for… how much you can squeeze out of performance until you control for data quality." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 06:10-06:30)
- The fix is stated as symmetry, not as a data-cleaning step: "we actually co-optimized based on all the adaptation we did with the data exactly what we would do with the model," summarized as "the need to control the entire flow." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 06:30-06:39)
- Why the failure mode is easy to fall into: giving the agent a `generate_data` action looks like more freedom, and in a search framing more actions should mean more headroom. But an unoptimized data action makes the search's objective noisy — two candidate recipes are being scored partly on differences in data the search never controlled — so the signal it is climbing is contaminated rather than expanded. Controlling the data is what makes the model-side comparison mean anything.
- The stated scope of the loop is wide: AutoScientist "co-optimizes the entire loop… from data to alignment" and "chooses and self-evolves based upon the domain and the type of data," combining "the knowledge it gained from the adaptive data component with… the knowledge of the domain and… the ability to self-improve for a domain." ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 05:32-06:54)
- The same principle is asserted one level up in Q&A and is the more testable form of it: automating harness design will "only work… if you also co-optimize it with a model" — see [Automating Harness Design Requires Co-Optimizing the Model](automating-harness-design-requires-co-optimizing-the-model.md). The pattern the speaker is generalizing is that any component the search leaves fixed or unsupervised becomes the term that caps the return. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 17:19-17:38)
- This sits next to the wiki's existing data-quality material from the other direction. Curation work like [ordering billion-scale filters by cost per sample](order-billion-scale-data-filters-by-cost-per-sample.md) treats quality as a pipeline you build once; this claim is that quality has to be a *searched variable* whenever the model side is searched, because the two interact. It also gives a mechanism for the same speaker's later remark that "data quality in general means you use capacity a lot more" ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 19:24-19:31).
- Provenance and limits: this is a founder describing her own unreleased system's development history, with no ablation published, no measure of "returns," and no definition of the data-quality control. Treat it as a design hypothesis with a plausible mechanism and one practitioner's report behind it — not as a measured result. The headline "outperforms research staff" claim it is offered to explain is itself unpublished. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 05:45-06:39)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Automated Training Search Beats Staff by Not Carrying Architecture Priors](automated-training-search-beats-staff-by-not-carrying-architecture-priors.md)
- [Automating Harness Design Requires Co-Optimizing the Model](automating-harness-design-requires-co-optimizing-the-model.md)
- [A Budget Stopping Rule Can Masquerade as a Capability Ceiling](a-budget-stopping-rule-can-masquerade-as-a-capability-ceiling.md)
- [Order Billion-Scale Data Filters by Cost per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)
- [Train Long-Tail Knowledge Into Weights With Curated Synthetic Data](train-long-tail-knowledge-into-weights-with-curated-synthetic-data.md)
- [The Synthetic Data Wall Caps Every Define-Then-Train Loop](the-synthetic-data-wall-caps-every-define-then-train-loop.md)
- [Use Hardware-In-The-Loop Search For AI Kernel Generation](use-hardware-in-the-loop-search-for-ai-kernel-generation.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 05:32-06:54, 17:19-17:38, 19:24-19:31
