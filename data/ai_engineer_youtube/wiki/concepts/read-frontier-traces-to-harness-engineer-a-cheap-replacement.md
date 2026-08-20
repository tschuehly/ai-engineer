# Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement

Summary: Use a frontier model only to establish that a task is possible, then read its traces to see *how* it reasons and encode that reasoning as guidance in a cheaper model's harness — the traces are the specification for the downgrade, not just evidence that it succeeded.

Use when:
- A frontier model works and you want the same behavior at a fraction of the cost.
- Judging, classifying, or grading in bulk, where price multiplies by volume.
- You have a golden dataset showing *what* the big model produced but not *why*, and the small model keeps missing.

Details:
- The routing discipline first: "we at LangChain don't reach for the frontier models for every single use case. We're quite conscious about what is the minimum level of intelligence that I need to do any given task." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:36-08:00)
- The waterline pattern: "practically speaking, honestly, yes, we start with Opus, we start with 5.5 because we just want to know if the task is even possible. But then once we reach that sort of like waterline, then we like look back at those traces and we see, 'Hey, can we use an open model to do the same thing?'" ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 08:00-08:16)
- The measured result, from work with Harvey on their legal benchmark: "can I match the trace judging capability of Opus with an open cheaper model? And the answer is roughly yes at like an order or like two orders of magnitude cheaper." ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 08:16-08:34)
- **The mechanism is the reusable part.** "We try a bunch of models, we do a bunch of like harness engineering, and the harness engineering is informed by a bunch of the traces that we read. So it's like, 'Hey, like Opus reasons about things in this way. Maybe that's because of the prompt. Maybe Opus is just smarter, which it is, than a bunch of the open models, but that might mean I need to give it a little bit more guidance so it can reach the sort of same intelligence level at like a much much lower cost.'" The frontier model's visible reasoning is treated as a source of harness content, not merely a label to imitate. ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 08:34-08:58)
- Why judging is the natural first target: it is a bulk workload whose cost is the input token price multiplied by the number of traces and their average size ([Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)), so a per-token saving compounds in a way it does not for a single user-facing call.
- Distinguish this from two nearby moves the wiki already records. [Right-size models with prototype-big, deploy-small](right-size-models-with-prototype-big-deploy-small.md) freezes the big model's *outputs* as a golden dataset and benchmarks candidates against it; this concept mines the big model's *trajectory* for the guidance the small model is missing. [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md) puts that trajectory into weights; this puts it into the prompt and harness first, which is reversible and answers in minutes rather than a training run.
- Related empirical support that the harness can carry a weaker model: Harness Bench holds the model and evaluation fixed, varies only the harness, and swings scores by more than 20 points — "for weaker models, the harness matters more" ([Invest in the harness to run weaker and local models](invest-in-the-harness-to-run-weaker-and-local-models.md)).
- Provenance caveat that should travel with the number: this is a single vendor-reported customer engagement with no published methodology, no baseline table, and no named open model, and "an order or like two orders of magnitude" is itself a 10× band. The structural claim — that trace judging is a bulk workload where trace-informed harness engineering can substitute for model capability — is separable from the figure.
- **The same technique named from the releasing lab's side, with a bound asserted on it.** Rizwan argues American labs should publish weights precisely because the distillation route this page describes has a ceiling: released weights let others "extract the traces and train your copycat models on them more easily, but not in a way that can leapfrog," which is why he separates weight release from opening research ("I don't mean we need to open source our research. I think that's what gives us the lead"). If the bound holds, trace-based harness engineering is a way to close most of a gap you did not create and never a way to open one — which is a fair description of the practice this page recommends. The claim is asserted without evidence by someone with a commercial interest in more open weights, and it is contested; it is worth knowing as the argument a releaser makes, not as a measured limit. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 15:19-15:45)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Right-Size Models With Prototype Big, Deploy Small](right-size-models-with-prototype-big-deploy-small.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Close the small-model gap with prompt variants and harness post-processing](close-the-small-model-gap-with-prompt-variants-and-harness-post-processing.md)
- [Distill Reasoning Traces Into Small Models](distill-reasoning-traces-into-small-models.md)
- [Sequence Harness Engineering and Fine-Tuning by Feedback Speed](sequence-harness-engineering-and-finetuning-by-feedback-speed.md)
- [Mine Trace Corpora With Agents Because They Do Not Fit in Context](mine-trace-corpora-with-agents-because-they-do-not-fit-in-context.md)
- [Commoditize the Layer You Do Not Win On](commoditize-the-layer-you-do-not-win-on.md)

Sources:
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:36-08:58
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 15:19-15:45
