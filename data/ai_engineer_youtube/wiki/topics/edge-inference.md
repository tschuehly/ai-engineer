# Edge Inference

## Overview

Edge inference is most useful when latency, privacy, offline access, or cloud-token cost dominate the product constraint. The practical design pattern is hybrid: push suitable workloads onto the device, size the model to the target hardware, and keep cloud calls for tasks that exceed local capability.

## Key Concepts

- [Use edge inference when latency, privacy, offline access, or token cost dominate](../concepts/use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md) - local execution is strongest when responsiveness, data locality, connectivity, or cost matter more than maximum model capability.
- [Match Gemma edge model size to device memory and interaction class](../concepts/match-gemma-edge-model-size-to-device-memory-and-interaction-class.md) - model choice should account for quantized memory footprint and the interaction class being served.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - deployment quality depends on the full fleet, not a current development device.

## Open Questions

- How should teams decide the cutoff where local quality is good enough and cloud fallback becomes unnecessary?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
