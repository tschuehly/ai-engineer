# Curate Generative-Media Data Before Tuning Model Internals

Summary: Large-scale image and video model quality depends heavily on data curation. Teams should inspect and improve the training data before assuming model architecture, optimizer, or hyperparameter changes are the highest-leverage path.

Use when:
- Planning a generative image or video model training run.
- Deciding whether to spend effort on data quality or model internals.

Details:
- The source says data curation is essential for high-quality large-scale generative-media results, even though research incentives historically favored fixed benchmark datasets over direct data inspection.
- For production-scale models, time spent improving the data can be a better investment than tweaking the model or optimizer (02:55-03:39).
- The source does not disclose detailed curation recipes, which is itself a practical caveat: data quality is treated as core model capability work rather than incidental preprocessing (03:48-04:00).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Use loss curves to debug local model training](use-loss-curves-to-debug-local-model-training.md)
- [Tokenizer size must match data and compute budget](tokenizer-size-must-match-data-and-compute-budget.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:55-04:00
