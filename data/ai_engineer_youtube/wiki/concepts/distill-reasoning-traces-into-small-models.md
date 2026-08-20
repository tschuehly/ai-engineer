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

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Small agentic models make parallel workplace agents economical](small-agentic-models-make-parallel-workplace-agents-economical.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)

Sources:
- [Latent Space Paper Club: AIEWF Special Edition (Test of Time, DeepSeek R1/V3) — VIbhu Sapra](../sources/20250725_9k3xPh-40mo.md), 12:48-15:05
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 11:08-11:43
