# LiteRT Provides A Cross-Platform Path From Model Conversion To Edge Deployment

Summary: LiteRT is Google's on-device framework for deploying models across Android, iOS, macOS, Linux, Windows, web, and IoT targets. It keeps TensorFlow Lite format compatibility while also supporting conversion paths from PyTorch and JAX models.

Use when:
- Planning a bring-your-own-model deployment to multiple edge platforms.
- Converting PyTorch or JAX models for an edge runtime.

Details:
- LiteRT is described as built on TensorFlow Lite foundations and using the same TensorFlow Lite model format, so existing TensorFlow Lite models remain compatible.
- LiteRT also accepts PyTorch and JAX models after conversion to TensorFlow Lite format.
- The deployment stack includes LiteRT Torch for conversion, optional quantization, LiteRT-LM for LLM paths, and LiteRT for non-LLM paths.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Benchmark edge models across the device fleet before shipping](benchmark-edge-models-across-the-device-fleet-before-shipping.md)

Sources:
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md), 11:03-14:10
