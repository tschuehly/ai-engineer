# Curate Generative-Media Data Before Tuning Model Internals

Summary: Large-scale image and video model quality depends heavily on data curation. Teams should inspect and improve the training data before assuming model architecture, optimizer, or hyperparameter changes are the highest-leverage path.

Use when:
- Planning a generative image or video model training run.
- Deciding whether to spend effort on data quality or model internals.

Details:
- The source says data curation is essential for high-quality large-scale generative-media results, even though research incentives historically favored fixed benchmark datasets over direct data inspection.
- For production-scale models, time spent improving the data can be a better investment than tweaking the model or optimizer (02:55-03:39).
- The source does not disclose detailed curation recipes, which is itself a practical caveat: data quality is treated as core model capability work rather than incidental preprocessing (03:48-04:00).
- Krea's Krea 2 talk supplies the recipes this page previously lacked, and states the premise more strongly: "typically, you lock in your architecture and then… a lot of work just goes into like just feeding the model like what it wants," and "data is like what really determines the quality of your model." The concrete pipeline is around 30-40 in-house classifiers, heuristics, and filters covering deduplication and clustering-based rebalancing, captioner-failure classes, resolution-inappropriate samples, and AI-generated images (Lee 05:16-05:45, 06:38-07:30, 14:34-15:05).
- Krea also ranks data against the other levers on durability rather than impact: "methods can change every time[,] code is something you can change very easily but… data is like eternal… that's going to be valuable no matter what the hot new training paradigm is" (Lee 18:36-18:50).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Use loss curves to debug local model training](use-loss-curves-to-debug-local-model-training.md)
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)
- [Order Billion-Scale Data Filters by Cost Per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)
- [Filter Training Images Your Captioner Systematically Mis-Describes](filter-images-your-captioner-systematically-mis-describes.md)
- [Refuse AI-Generated Training Images When Style Is the Product](refuse-ai-generated-images-when-style-is-the-product.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:55-04:00
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 05:16-05:45, 06:38-07:30, 14:34-15:05, 18:36-18:50
