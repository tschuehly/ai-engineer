# Run the LLM Post-Training Ladder on Diffusion Models

Summary: A production image model is trained with the same stage ladder as an LLM — pretraining, mid-training, SFT, preference optimization, RL — plus two diffusion-specific pieces: a low-to-high resolution curriculum and a separately trained prompt expander. Borrowing the ladder is also a deliberate efficiency choice, because it lets a small team reuse LLM kernels, literature, and tooling.

Use when:
- Planning a training pipeline for an image or video generation model.
- Deciding where to intervene when a diffusion model is capable but off-distribution for your product.
- Explaining why long prompts outperform short ones against a production image endpoint.

Details:
- The full ladder, as described: low- to high-resolution pre-training, mid-training, supervised fine-tuning, preference optimization, reinforcement learning, and a trained prompt expander. Lee calls it LLM-inspired outright. (Lee 15:06-15:31)
- Resolution is a curriculum, not a config value. Low resolution "is where the model actually learns like text-to-image capabilities… it needs to know like how a horse looks like"; scaling resolution up afterwards adds "structure, detail, like these kind of things that can be learned at high resolution later." Krea 2 ran 256 up to 1K. (Lee 15:31-16:02)
- Mid-training and SFT are the diffusion analogue of instruction tuning, and the analogy is explicit: a pre-trained diffusion model is "just basically auto complete" the way a pre-trained LLM is, so you curate domain data — "illustration, graphic design, photography, cinematics… kind of like data you want you have in mind for your downstream use case" — at both mid-train and SFT scale "to kind of mold your distribution." (Lee 16:02-16:40)
- Preference optimization uses A/B pairs in the same shape ChatGPT collects them, and is where the lab's taste enters: "this is where we get a little bit more opinionated about… the kind of model we want to train." (Lee 16:40-17:06)
- RL is "a GRPO inspired method where… model[s] generate images and then we send it to the reward servers," aimed at specific defect classes — "how to like improve text rendering… have like better anatomy structure." (Lee 17:06-17:35)
- The prompt expander is called "almost essential… for production grade diffusion models": a small LLM that rewrites a short user prompt into a long detailed one, "because typically longer detail prompt[s]… are more in distribution with your model's… training data[,] that tends to like make better images." For engineers *calling* an image endpoint, this is the mechanism behind long prompts working better, and it explains why a hosted model's behavior can change without the diffusion weights changing.  (Lee 17:35-17:54)
- Current direction: "multi-expert on[-policy] distillation" — train experts specialized in capabilities such as photography or text rendering, then merge them into a single student that matches each expert in its specialty. (Lee 17:54-18:28)
- The reuse motive is stated as a team-level lever alongside infrastructure and data: prefer "methods that have like low number of hyper parameters that we need to tune," and "steal a lot from LLM research so that I can just reuse their kernels and… research and… literature." (Lee 18:30-19:15)
- Architectural footnote: the stack is inverting. With an autoregressive-decoder prompt expander feeding a diffusion encoder, Lee observes it "starting to look a little bit like DALL-E 2," where one model generates the conditioning that another model renders. His stated wish is the opposite direction — drop the VAE and text encoders and "just train a single clean transformer" — and his interest is in richer conditioning now that VLMs can cheaply produce bounding boxes (he attributes work here to Ideogram) or scene graphs (traced to Fei-Fei Li's lab, 2017). (Lee 19:16-21:05)

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Train image and video diffusion models in learned latent spaces](train-image-and-video-diffusion-models-in-learned-latent-spaces.md)
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 15:06-19:15, 19:16-21:05
