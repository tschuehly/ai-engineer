# Reliability and Stylistic Range Are Opposite Model Positions

Summary: A production image model's consistency is bought by collapsing its output distribution, so "reliable" and "stylistically diverse" are two ends of one dial rather than two quality levels. Which end you want is decided by whether the user already knows what they want, and choosing the diversity end changes how you are allowed to filter training data.

Use when:
- Choosing between a big-lab production image model and a smaller or open one for a creative product.
- Deciding whether your generative-media model should be tuned for repeatable output or for exploration.
- Writing data-quality filters for a media model and reaching for a generic aesthetic or image-quality score.

Details:
- Krea's read of the production models — captioned as "Chat GPT-2" (OpenAI's then-current production image model) and "Nano Banana Pro" — is that they optimize for slow, near-flawless output, taking "up to like a minute or like two," and that the price is deliberate: "in order to get like good consistency, they have like kind of like significantly mode collapse their models." (Lee 01:47-02:24)
- The mechanism is stated as a rule of thumb about where the reliable mass of the distribution sits: "if you're trying to render a person, the easiest and most reliable way to like render a person is render the most boring average person that exists and then like put it in a center frame." The standing test case is the prompt "burning skull," where every output is competent and nearly identical. (Lee 02:24-02:48)
- The selection rule is the user's certainty, not the model's score. For a specified deliverable — "a poster or like a birthday card" — the production models are an "excellent solution"; the exploratory case is "when you're like a creative studio, you don't quite know what you want yet and want to like slightly explore what kind of like visuals you want to make," which is what Krea optimized for with fast generation plus controls. (Lee 02:48-03:23)
- Choosing the diversity end constrains curation downstream: standard quality filters silently pull the data back toward the conventional center. "Some people like think… low-resolution CRT videos are like a bad image, but some people like that kind of like aesthetics, so making sure that we have like good coverage and don't just rely on like very standard like aesthetic scores or like image quality scores to… oversample… what are conventionally considered like good images." (Lee 05:57-06:31)
- This is a training-and-positioning decision, not the sampling-time diversity knob. Guidance scale trades diversity for prompt adherence at generation time on a model you already have; mode collapse here is baked into the weights by what the lab optimized and what its data pipeline kept.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Use guidance to trade diffusion sample diversity for conditional quality](use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md)
- [Refuse AI-Generated Training Images When Style Is the Product](refuse-ai-generated-images-when-style-is-the-product.md)
- [Personalize aesthetic evals with preference classifiers](personalize-aesthetic-evals-with-preference-classifiers.md)
- [Order Billion-Scale Data Filters by Cost Per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 01:47-03:23, 05:57-06:31
