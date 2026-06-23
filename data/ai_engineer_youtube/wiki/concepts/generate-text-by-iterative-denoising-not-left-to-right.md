# Generate Text by Iterative Denoising, Not Left-to-Right

Summary: Text diffusion is an alternative to autoregressive (next-token) generation: instead of predicting one token at a time, it initializes the whole output block to noise and iteratively denoises it over a few passes, using bidirectional attention so every token can see the entire canvas — past and future — as it refines.

Use when:
- Deciding or explaining a text-generation paradigm beyond autoregressive transformers.
- Reasoning about why a model can edit text in place, self-correct, or scale latency differently than a standard LLM.
- Interpreting "diffusion LLM" / Gemini Diffusion claims.

Details:
- Training mirrors image/video diffusion: take a clean token sequence, gradually corrupt it at many noise levels (discrete diffusion replaces tokens with random vocabulary tokens), and train the network to correct the mistakes. At inference, initialize the sequence to pure random tokens and iteratively refine it over a few denoising steps, filling in information in the order the network prefers — the entire block is refined together over multiple passes, not emitted one token at a time. (00:14-04:00)
- Bidirectional vs causal attention is the structural difference: autoregressive models have causal attention (each token sees only the past); a diffusion model attends to the whole canvas, including the future tokens it will emit, which is what enables self-correction and in-place editing. (04:18-04:45)
- It is discrete diffusion — always tokens in, tokens out: a discrete corruption process followed by filling a discrete token back in, so the model always operates in token space. Latent-space text diffusion exists and people have tried it, but most text-diffusion models in the literature today are discrete. (24:00-24:45)
- Variable / unbounded length is handled by block-wise autoregression: fix a window length (e.g. 512, 1000, or 32 tokens), denoise within that window, then autoregress across windows for unlimited text; a length-prediction head is optional. Prefill works the same as autoregressive; within a window the team "sets it in stone and continues" rather than revisiting prior windows (though revisiting is possible). (21:30-23:30)
- In-place editing falls out of full-canvas visibility (the text analogue of image inpainting): cut a region and the model fills it from surrounding context. "There is a bug in this code, can you fix it?" makes the fix in the correct spot, "add documentation" inserts it, and "add a middle paragraph" produces one consistent with the surrounding paragraphs — a clever editing procedure rather than regenerating token-by-token. (14:26-16:09)
- Grounding: DeepMind's Gemini Diffusion was a Gemini variant doing text diffusion instead of next-token generation, released ~1 year before the talk as a research preview to ~100k users; it branched from Gemini 2.0 Flash-Lite with "very similar quality across the board" at much better latency. It uses the same training data as autoregressive models (algorithms change a bit) and can be distilled. (02:06-03:04, 20:05-20:30)

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Text Diffusion Trades Serving Throughput for Low Latency](text-diffusion-trades-serving-throughput-for-low-latency.md)
- [Diffusion Models Self-Correct by Revising Earlier Tokens](diffusion-models-self-correct-by-revising-earlier-tokens.md)
- [Scale Text-Diffusion Quality With More Denoising Steps](scale-text-diffusion-quality-with-more-denoising-steps.md)
- [Train image and video diffusion models in learned latent spaces](train-image-and-video-diffusion-models-in-learned-latent-spaces.md)

Sources:
- [Text Diffusion — Brendan O'Donoghue, Google DeepMind](../sources/20260604_r305-aQTaU0.md), 00:14-16:09, 20:05-24:45
