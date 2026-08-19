# Use Sparse Autoencoder Features as an Unsupervised Data Tagger

Summary: A sparse autoencoder trained on a vision model's activations returns, for any image, the sparse set of features it activates — which works as an off-the-shelf tagging system you never had to label. If one of those features corresponds to something you want out of the corpus, it becomes a filter you did not have to train.

Use when:
- You need corpus-level tags (watermarks, signatures, border artifacts, style attributes) and have no labeled data for them.
- You already have SAEs trained for interpretability and are looking for production uses beyond analysis.
- Designing filters for properties that are easy to recognize but awkward to specify in a prompt.

Details:
- The setup comes from Lee's own prior SAE research on CLIP-style vision models: train an SAE on the vision model, feed an image, and "it will give you like sparse features that get activated" — his example image activates features like "horse, black and white, blur[ry]… image." (Lee 11:55-12:50)
- The reframing is the point: "one thing that you can actually get out of SAE is a unsupervised tagging system… you can kind of use this as like off-the-shelf like unsupervised tagging system." No taxonomy is designed up front; the features are whatever the SAE decomposed the model's representation into. (Lee 12:19-12:55)
- Usage is symmetric — a matching feature can drive removal *or* oversampling: "if one of these like have like something that you want to like filter on or oversample… like signatures or like watermarks or like some kind of like border artifacts… like this is one nice thing to… remove… data that's kind of like undesirable in your data set." (Lee 12:55-13:18)
- The advantage over a prompted VLM filter is that you do not have to know what to ask for. The corresponding limitation is that you get the features the SAE found, not the ones you wanted: whether a feature exists for your target property is discovered, not specified, and Lee reports no precision figures for feature-based filtering.
- This inverts the usual direction of interpretability tooling in this wiki. Model diffs and activation-difference SAEs use sparse features to inspect a trained model's behavior; here the same artifact is used upstream as cheap labeling infrastructure for the data that trains the next model.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Vision AI](../topics/vision-ai.md)

Related concepts:
- [Model Diffs Inspect Post-Training Feature Changes](model-diffs-inspect-post-training-feature-changes.md)
- [Detect Fine-Tuning Backdoors With an Activation-Difference SAE](detect-fine-tuning-backdoors-with-an-activation-difference-sae.md)
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)
- [Order Billion-Scale Data Filters by Cost Per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 11:55-13:18
