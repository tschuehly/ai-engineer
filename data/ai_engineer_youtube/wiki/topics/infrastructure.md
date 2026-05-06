# Infrastructure

## Overview

Edge AI infrastructure needs a path from model conversion through quantization, runtime integration, accelerator selection, and fleet validation. LiteRT is presented as Google's cross-platform runtime layer for this path, with benchmarking used to choose reliable deployment recipes across devices.

## Key Concepts

- [LiteRT provides a cross-platform path from model conversion to edge deployment](../concepts/litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md) - TensorFlow Lite format compatibility and conversion support allow models to target multiple edge platforms.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - compilation and acceleration choices should be validated against representative Android devices.

## Open Questions

- Which conversion and quantization recipes preserve enough model quality for each target device class?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
