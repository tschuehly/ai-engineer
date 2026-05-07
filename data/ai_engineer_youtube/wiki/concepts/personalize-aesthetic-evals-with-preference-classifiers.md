# Personalize Aesthetic Evals With Preference Classifiers

Summary: Aesthetic quality can be relative to a user, creative intent, or audience, so media evals may need personalized preference models rather than one universal score. Small classifiers or continuous preference models can learn what a person means by good, bad, blue, teal, or visually acceptable.

Use when:
- Building creative tools where different users want different styles or quality bars.
- Turning subjective visual feedback into model-routing, ranking, or generation-control signals.

Details:
- The talk argues that art and aesthetics can carry meaning and preference that generic metrics do not capture, especially when a human understands the intent behind an image (08:13-09:04).
- The speaker frames aesthetic evals as opinion-bearing: a user may care not only whether a region is blue, but what kind of blue it is and whether they personally like it (12:30-13:02).
- A suggested approach is to train a classifier or continuous classifier from examples of images a user considers good, including examples with artifacts, so the eval learns the user's subjective boundary (15:13-16:21).
- This differs from counting prompt objects: the question becomes "you know it when you see it," which is a natural fit for learned preference models when enough labeled examples exist (16:04-16:21).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Evaluate generative media with perceptual metrics](evaluate-generative-media-with-perceptual-metrics.md)
- [Write custom scorers as product specifications](write-custom-scorers-as-product-specifications.md)

Sources:
- [Perceptual Evaluations: Evals for Aesthetics - Diego Rodriguez, Krea.ai](../sources/20250823_h5ItAJuB3Fc.md), 08:13-09:04, 12:30-13:02, 15:13-16:21
