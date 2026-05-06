# Use MLX Swift LM For Apple Local Model Integration

Summary: MLX Swift LM provides a direct path for adding local LLM inference to native Apple apps: install the package, select an MLX-compatible Hugging Face model, and pass the model ID so the app can download and run weights on device.

Use when:
- Building iOS, iPadOS, or macOS apps that need local language-model inference.
- Choosing between native on-device inference, a local desktop server, and cloud-hosted model calls for Apple-device workflows.

Details:
- MLX is described as Apple's framework optimized for Apple Silicon, and Locally AI uses it to run on-device models on iPhone, iPad, and macOS. (01:22-01:47)
- For native app integration, the recommended repository is MLX Swift LM; the framework can download and run Hugging Face-hosted MLX model weights when given a model ID. (02:04-02:36, 04:18-04:39)
- The broader MLX ecosystem includes MLX VLM, MLX audio, and MLX video, so Apple local inference can extend beyond text into visual, audio, image-generation, and video-generation workloads. (02:39-03:14)
- Local model apps should curate supported model catalogs instead of exposing every open model, because not every model works well on iPhone even if it is available as an MLX-compatible weight. (10:12-10:25)
- MLX Swift LM supports tool calling, while structured generation was described as not yet native and better handled by packages layered on top of MLX Swift LM. (09:02-09:38)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Open Model Families Need Ecosystem-Compatible Tooling](open-model-families-need-ecosystem-compatible-tooling.md)
- [Match Gemma Edge Model Size To Device Memory And Interaction Class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)
- [Constrained Decoding Makes Small-Model Tool Calls Production-Usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)

Sources:
- [Running LLMs on your iPhone: 40 tok/s Gemma 4 with MLX - Adrien Grondin, Locally AI](../sources/20260420_a2muGkT4WD4.md), 01:22-04:39, 09:02-10:25
