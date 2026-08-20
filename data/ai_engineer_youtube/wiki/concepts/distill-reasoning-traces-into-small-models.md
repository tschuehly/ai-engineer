# Distill Reasoning Traces Into Small Models

Summary: Strong reasoning models can produce traces that make smaller models materially better, so small-model training should consider teacher-generated reasoning data rather than only direct SFT or RL from the small base model.

Use when:
- Training an 8B-class or similarly constrained model for reasoning-heavy tasks.
- Choosing between direct small-model post-training and distillation from a stronger reasoning model.

Details:
- The session says the original DeepSeek work distilled reasoning traces from larger models into Qwen and Llama variants, producing strong small-model performance. (12:48-13:07)
- The May 28 follow-up distilled the improved reasoning model into Qwen 3 8B and is described as producing another large boost over the older distill. (13:07-13:44)
- The speaker emphasizes that the new Qwen 3 8B dense distillation matched the performance of a much larger Qwen 3 235B/20B-active thinking model on the discussed benchmark view, despite not being a native thinking model. (13:53-14:30)
- The durable lesson is that reasoning-model improvements can compound: better teacher reasoning creates better traces, and those traces can transfer into smaller deployable models. (14:43-15:05)
- **The applied version uses your own production traces as the teacher corpus.** LangChain lists distillation and SFT as the first output of mining a trace store: "let's say I'm running GLM 5.2. It's doing great, but I think that I can run this task like way cheaper with like a 9B or 13B model. Then what I'll do is like I'll take the good traces and the good examples from the GLM 5.2 runs, I'll prepare them in a data set, and then I'll try to fine-tune a small model on that data set to like mimic behavior." Two differences from the research-lab version above: the teacher is whatever model is already serving your traffic rather than a frontier reasoning model, and the selection step ("the good traces") is where the work is — which is what makes the trace-mining read path a prerequisite ([Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:08-11:43)

- **The third variant has no teacher until you build one, and that changes what the technique is for.** Both cases above start from a model that already produces the target behavior — a frontier reasoning model, or your own production traffic. For a private *corpus* there is no such teacher: documents are not behavior. On-policy distillation manufactures one by putting the corpus in the context window and cloning the resulting answers, so "you can't really distill the raw documents" is the constraint that decides the whole pipeline ([Distill Behaving as if the Corpus Were in Context](distill-behaving-as-if-the-corpus-were-in-context.md)). Keeping the three apart matters when scoping: with a teacher, distillation is a compression project; without one, most of the work is supervision synthesis. ([Engram](../sources/20260812_WiqDvX6isc4.md), 13:20-14:12)

- **The dependency on a large teacher is conceded, and bounded, by the size-ceiling argument.** Asked directly whether small frontier models still rely on bigger models to distill knowledge downwards, Sara Hooker answers "I agree distillation is helpful" and "frontier models are still pretty large, yes" — her disagreement is only about the trend: "no one is going to supersize their model or if they do it's not clear it's beneficial except for small size of the distribution, which is very much the long tail." Read as planning input, that says the teacher you distill from is roughly the teacher you will have, and the remaining case for spending more pre-training compute is tail coverage rather than a better teacher across the board ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 18:25-20:03). She adds a second-order effect on the same axis: "data quality in general means you use capacity a lot more," so "instead of the size people are just moving post-training further back," which shifts where a distillation program's teacher improvements will come from. See [Pre-Training Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md). This is an assertion about lab behavior with no measurement attached.

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Pre-Training Size Is No Longer the Most Lucrative Scaling Axis](pretraining-size-is-no-longer-the-most-lucrative-scaling-axis.md)
- [Distill Behaving as if the Corpus Were in Context, Not the Documents](distill-behaving-as-if-the-corpus-were-in-context.md)
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Small agentic models make parallel workplace agents economical](small-agentic-models-make-parallel-workplace-agents-economical.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)

Sources:
- [Latent Space Paper Club: AIEWF Special Edition (Test of Time, DeepSeek R1/V3) — VIbhu Sapra](../sources/20250725_9k3xPh-40mo.md), 12:48-15:05
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:08-11:43
- [Scaling Compute on Context — Jack Morris, Engram](../sources/20260812_WiqDvX6isc4.md), 13:20-14:12
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 18:25-20:03
