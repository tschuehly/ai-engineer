# Expose Explicit Control Signals for Generative Media Models

Summary: Text prompts are only one conditioning surface for image and video models. Productive generative-media systems expose additional controls such as camera motion, masks, depth, and other structural signals when users need predictable composition or motion.

Use when:
- Designing user or API controls for image and video generation.
- Deciding which conditioning signals to train or expose beyond text prompts.

Details:
- The source presents control signals as the mechanisms used to make media generation do what the user wants, separate from the core denoising mechanism (02:27-02:34).
- Text conditioning is useful but not the only control; image and video systems can also use masks, depth maps, and camera motion signals (30:04-31:08, 37:33-38:06).
- Camera control is a video-specific example where the desired output is not just static content but how the virtual camera moves through the scene (31:07-31:08, 38:05-38:06).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Tools](../topics/tools.md)
- [Models](../topics/models.md)

Related concepts:
- [Use guidance to trade diffusion sample diversity for conditional quality](use-guidance-to-trade-diffusion-sample-diversity-for-conditional-quality.md)
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)

Sources:
- [Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind](../sources/20260421_xOP1PM8fwnk.md), 02:27-02:34, 30:04-31:08, 37:33-38:06
