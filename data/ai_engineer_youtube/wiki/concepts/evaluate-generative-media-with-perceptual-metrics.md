# Evaluate Generative Media With Perceptual Metrics

Summary: Image and video evals should account for what humans actually perceive, not only pixel, embedding, or object-count differences. Metrics such as FID can overreact to artifacts that look similar to humans while missing aesthetic or semantic failures that matter to creative users.

Use when:
- Evaluating image, video, audio, or 3D generative models.
- Choosing whether a benchmark score is good enough for creative-product quality.

Details:
- The talk frames aesthetic evals as difficult because they include human perception, opinion, and taste rather than only objective task completion (00:36-00:48).
- A generative-image example shows an advanced model doing OpenCV-style analysis yet failing to identify an obviously unnatural hand the way humans do immediately (00:50-01:25).
- The speaker cites Clean-FID/FID behavior where adding JPEG artifacts can sharply worsen the score even when the compared images look perceptually similar to humans, making the metric suspect as a product-quality proxy (07:00-07:40).
- Easy-to-measure signals such as CLIP prompt adherence, object counts, and color presence can miss whether an image makes visual or artistic sense (07:44-08:09).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)

Sources:
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md), 00:36-01:25, 07:00-08:09
