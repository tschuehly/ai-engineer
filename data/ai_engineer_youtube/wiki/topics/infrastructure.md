# Infrastructure

## Overview

AI infrastructure spans both edge deployment and server-side inference operations. Edge AI needs a path from model conversion through quantization, runtime integration, accelerator selection, and fleet validation. Server-side small-model inference needs model-aware runtimes plus routing, queueing, autoscaling, observability, and GPU provisioning so many specialized models can run efficiently in production.

## Key Concepts

- [LiteRT provides a cross-platform path from model conversion to edge deployment](../concepts/litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md) - TensorFlow Lite format compatibility and conversion support allow models to target multiple edge platforms.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - compilation and acceleration choices should be validated against representative Android devices.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - dynamic model loading helps keep accelerator capacity productive when many small models share the fleet.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - runtime support and infrastructure operations have to be designed together.

## Open Questions

- Which conversion and quantization recipes preserve enough model quality for each target device class?
- Which autoscaling signal best captures useful utilization for mixed small-model workloads?

## Sources

- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
