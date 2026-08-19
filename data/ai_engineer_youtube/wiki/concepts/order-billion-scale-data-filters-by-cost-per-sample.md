# Order Billion-Scale Data Filters by Cost Per Sample

Summary: At two to ten billion samples, every question you want to ask of the corpus has to be answerable by something cheap enough to run billions of times. The working pattern is a cost-ordered cascade — hashes before embeddings, and a large model's judgment distilled into a small classifier that does the actual sweep.

Use when:
- Deduplicating or filtering a web-scale image, video, or text pretraining corpus.
- You have a good filtering criterion that only a frontier VLM or LLM can currently judge.
- Budgeting GPU time between data curation and the training run itself.

Details:
- The constraint is stated plainly: Krea trains on "anywhere from like 2 to like 10 billion images. That's a lot of images to run like filters on." (Lee 10:01-10:15)
- Deduplication runs in two stages by cost. First pHash or MD5 hashes for exact and near-exact duplicates across the full corpus; "once we get to like a smaller like size, that's when we bring in… embedding-based deduplication method[s], SSCD, like SigLip, to do… semantic deduplication or… remove near duplicates." Duplicates and overrepresented concepts are also handled by clustering-based rebalancing. (Lee 06:38-06:55, 10:15-10:37)
- Filters are built by prompting a large vision-language model for the judgment you want — his example is "does this look like a AI image or not" — and then distilling that decision "to like a very small like SigLip classifier… you have like a very like cheap classifier that is somewhat like reliable." The size requirement is explicit: "typically if you run a classifier over like a billion images, you do need things to be like SigLip-sized." (Lee 10:37-11:24)
- The same pattern is cited from the LLM side: Essential Web used "a big LLM to like come up with like some kind of taxonomy or like classifiers to like judge whether this text data is like good or not… and then distill that down to like… 500… million parameter model so that you can actually run this over like a pre-training level corpus. Otherwise, it'll be somewhat expensive and frankly inefficient use of your GPUs." (Lee 11:24-11:53)
- Coverage checks obey the same budget in the positive direction. To confirm the corpus contains the world knowledge the model needs, Krea borrows from the original CLIP paper: compute PageRank over every Wikipedia article, take the concepts in the top percentile as things the model probably should know, then "run like… standard like plain text search or like embedding search just to make sure that like these kind of concepts are in our dataset." (Lee 13:19-14:11)
- Volume of criteria, not sophistication of any one, is what the pipeline ends up looking like: "around like 30 to 40… custom in-house classifier[s], like different heuristics and like filters." (Lee 14:34-14:47)
- Caveats: the distilled classifier is only "somewhat like reliable," and no agreement rate against the teacher VLM is reported, so cascade errors are unmeasured here. Lee is also candid that the coverage sweep's payoff is unknown — "frankly, I don't know how much this has helped, but this is one of the things we did." (Lee 11:12-11:24, 13:26-13:31)
- This is the offline-corpus form of the cheap-gate pattern that appears in serving: there a cheap detector decides whether an expensive model runs on a live stream, here a cheap distilled classifier decides whether a sample enters a fixed corpus, and the cheap model is derived from the expensive one rather than routed around it.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Gate Always-On Listening With Cheap Event Detectors](gate-always-on-listening-with-cheap-event-detectors.md)
- [Route each request to the cheapest sufficient model by difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Use Sparse Autoencoder Features as an Unsupervised Data Tagger](use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md)
- [Filter Training Images Your Captioner Systematically Mis-Describes](filter-images-your-captioner-systematically-mis-describes.md)
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 06:38-06:55, 10:01-11:53, 13:19-14:47
