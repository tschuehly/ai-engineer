# Refuse AI-Generated Training Images When Style Is the Product

Summary: Training on AI-generated images is a shortcut to a competent model that quietly transfers another lab's aesthetic into yours, because synthetic style is sticky and hard to unlearn. When the differentiator you are selling *is* the look of the output, removing AI images from the corpus is a product decision, not a purity preference.

Use when:
- Assembling a large image or video training corpus from web-scale sources that now contain generated media.
- Deciding whether to distill from a stronger production model to reach quality faster.
- Auditing why a newly trained media model's outputs look like a specific commercial model's outputs.

Details:
- Krea's stance is absolute rather than proportional: "we tried very hard to like remove any AI images like at all." The reason given is not licensing or quality but transfer — "synthetic data is like so sticky to the model that once you like start training on AI image data, sure your model's good, but you kind of lose the point because then you're going to get like very like ChatGPT or like Nano [Banana] aesthetic." (Lee 07:30-08:15)
- The tradeoff is stated honestly: distillation "does like provide you a shortcut to… get you like a good model." The cost is paid in identity, and it is detectable — Lee says he can personally tell when a model has been heavily trained or distilled on the current production image models. (Lee 07:30-08:09)
- This makes AI-image detection an infrastructure requirement, not a policy checkbox: Krea's example of a filter built by prompting a large VLM and distilling it to a cheap classifier is exactly the "does this look like a AI image or not" judgment, run over billions of samples. (Lee 10:37-11:24)
- Scope the rule by what you are selling. A team whose differentiator is a narrow capability rather than a look has less to lose from distillation; a team whose product is stylistic range is importing its competitor's mode collapse along with the free quality.
- Caveat: the claim that synthetic aesthetic is sticky is stated from experience, with no measurement of how much AI data is tolerable or how it degrades with mixing ratio. Lee also names a non-technical motive — "as a researcher it always slightly hurts my ego if all I'm doing is distillation" — so the rule is a stance, not a measured threshold. (Lee 08:09-08:15)

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Reliability and Stylistic Range Are Opposite Model Positions](reliability-and-stylistic-range-are-opposite-model-positions.md)
- [Train Your Own Models Only Where You Have a Right to Win](train-your-own-models-only-where-you-have-a-right-to-win.md)
- [Order Billion-Scale Data Filters by Cost Per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)
- [Distill reasoning traces into small models](distill-reasoning-traces-into-small-models.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 07:30-08:15, 10:37-11:24
