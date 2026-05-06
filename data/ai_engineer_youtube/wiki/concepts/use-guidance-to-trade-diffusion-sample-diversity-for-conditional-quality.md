# Use Guidance to Trade Diffusion Sample Diversity for Conditional Quality

Summary: Diffusion guidance modifies sampling to push outputs toward the conditioning signal. Increasing guidance can improve prompt adherence and perceived sample quality, but it reduces diversity and can create artifacts when pushed too far.

Use when:
- Tuning image or video generation sampling settings.
- Debugging bland, low-adherence, overconstrained, or artifact-heavy diffusion outputs.

Details:
- The source frames guidance as a sampling-time method for trading sample diversity against sample quality and condition adherence (24:10-24:27).
- Guidance changes the sampling path, effectively pushing samples farther toward what the conditional model prefers rather than merely changing the training objective (25:02-26:41).
- The speaker treats guidance as broadly useful for image and video diffusion, noting that it reveals how much current models depend on sampling procedure choices (26:47-27:49).
- Very high guidance can be a failure mode: images that look overexposed, oversaturated, or otherwise artifacted are often a sign that guidance scale is too high, and schedules can vary guidance across the sampling process (32:50-33:25).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Distill diffusion models to reduce sampling steps](distill-diffusion-models-to-reduce-sampling-steps.md)
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 24:10-27:49, 32:50-33:25
