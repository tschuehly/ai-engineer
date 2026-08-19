# Filter Training Images Your Captioner Systematically Mis-Describes

Summary: A caption that consistently omits a visible property of an image teaches the generator to emit that property unconditionally. When a captioner reliably fails on a class of images, the cheapest fix is to drop or undersample that class rather than to keep improving the caption.

Use when:
- Building a caption pipeline for a text-to-image or text-to-video training corpus.
- Diagnosing a generated artifact that appears regardless of the prompt (a border, a background, a framing convention).
- Deciding whether a data problem is a captioning problem or a data-selection problem.

Details:
- The worked example is a painting photographed hanging on a white wall. The image itself is fine — "it doesn't look that bad" and "you can train on it" — but across many attempts the captioner would describe "a painting of blah blah blah" and "would not mention the fact that it's framed on a wall… and have a white background." (Lee 09:03-09:34)
- The failure surfaces at generation time as an artifact the user never asked for: "when you try to generate a painting of whatever, it'll be always hanged on a wall, on a white wall." Anything present in the pixels but absent from the caption becomes unconditioned background behavior the model always produces. (Lee 09:34-09:41)
- The remedy Krea chose is selection, not correction: "this is an example where we just had to like design filters and then threw this kind of… data out or at least undersample it." Undersampling is offered as the softer option when the class is too large to discard. (Lee 09:41-10:00)
- The general test is consistency of the failure, not its severity. Krea's bad-data taxonomy names as a category images where the vision-language captioner "sometimes constantly fail[s] to like capture important aspect of the image, which leads to certain biases" — a random captioning error is noise, a systematic one is a learned bias. (Lee 06:38-07:09)
- Caption pipeline order matters for the same reason. Krea runs OCR *before* the VLM pass "because text rendering is quite important," then attaches optional metadata (for example, that the subject is a famous person), then generates the detailed caption, then rewrites it into the target prompt format such as JSON. Extracting the properties you know the captioner under-reports, before captioning, is the alternative to discarding the image. (Lee 08:17-09:03)
- Resolution interacts with this: an image with "20[-]100 like characters on a 256 by 256 pixels" frame is legitimate data that is simply unlearnable at the current stage, so the same filter machinery is used to stage data by training resolution rather than to reject it permanently. (Lee 07:09-07:30)
- This is the generative mirror of the representation-side finding that caption supervision erases visual distinctions: there, missing captions mean the encoder never learns a difference; here, missing captions mean the decoder always renders it.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Vision AI](../topics/vision-ai.md)
- [Models](../topics/models.md)

Related concepts:
- [Use vision-only features when captions erase visual distinctions](use-vision-only-features-when-captions-erase-visual-distinctions.md)
- [Use Sparse Autoencoder Features as an Unsupervised Data Tagger](use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md)
- [Order Billion-Scale Data Filters by Cost Per Sample](order-billion-scale-data-filters-by-cost-per-sample.md)
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)

Sources:
- [Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai](../sources/20260818_-tviRdpmHvs.md), 06:38-07:30, 08:17-10:00
