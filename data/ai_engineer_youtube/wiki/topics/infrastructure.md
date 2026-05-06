# Infrastructure

## Overview

AI infrastructure spans local training environments, edge deployment, server-side inference operations, observability systems, and the product systems that meter expensive AI usage. Edge AI needs a path from model conversion through quantization, runtime integration, accelerator selection, and fleet validation; CPU/GPU deployment can use a shared artifact, while NPU deployment may require ahead-of-time vendor compilation behind a consistent app API. Server-side small-model inference needs model-aware runtimes plus routing, queueing, autoscaling, observability, and GPU provisioning so many specialized models can run efficiently in production. Production AI applications also need managed prompts, tools, scoring functions, trace metadata, and online scoring automation so local prototypes can become monitored systems. Local training work adds a smaller-scale infrastructure lesson: choose a setup that can run on MPS, CUDA, CPU, or Colab, and keep the model, tokenizer, and batch sizing proportional to the available memory. AI monetization adds a billing-infrastructure lesson: usage caps, threshold notifications, top-ups, rate limits, and detailed metering protect customers and providers when AI calls can burn spend unexpectedly.

## Key Concepts

- [Use hosted model playgrounds to prototype before owning infrastructure](../concepts/use-hosted-model-playgrounds-to-prototype-before-owning-infrastructure.md) - hosted tools can validate model and deployment choices before teams own the runtime.
- [LiteRT provides a cross-platform path from model conversion to edge deployment](../concepts/litert-provides-a-cross-platform-path-from-model-conversion-to-edge-deployment.md) - TensorFlow Lite format compatibility and conversion support allow models to target multiple edge platforms.
- [Benchmark edge models across the device fleet before shipping](../concepts/benchmark-edge-models-across-the-device-fleet-before-shipping.md) - compilation and acceleration choices should be validated against representative Android devices.
- [Hot-swap small models to avoid one-model-per-GPU waste](../concepts/hot-swap-small-models-to-avoid-one-model-per-gpu-waste.md) - dynamic model loading helps keep accelerator capacity productive when many small models share the fleet.
- [Production inference combines model support with cluster operations](../concepts/production-inference-combines-model-support-with-cluster-operations.md) - runtime support and infrastructure operations have to be designed together.
- [Local LLM training exposes the core model-building stack](../concepts/local-llm-training-exposes-the-core-model-building-stack.md) - local model training makes tokenizer, architecture, training, and inference decisions explicit.
- [Tokenizer size must match data and compute budget](../concepts/tokenizer-size-must-match-data-and-compute-budget.md) - tokenizer capacity has direct implications for memory, convergence, and required training data.
- [Modular tiny-model pipelines reuse specialized models across mobile app workflows](../concepts/modular-tiny-model-pipelines-reuse-specialized-models-across-mobile-app-workflows.md) - app infrastructure can combine LiteRT and LiteRT-LM components instead of treating the LLM as the whole application.
- [Prevent AI billing surprises with caps, notifications, and rate limits](../concepts/prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md) - AI billing infrastructure should prevent runaway usage and unexpected invoices.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - production eval infrastructure should distinguish always-on cheap checks from sampled expensive judge-model scoring.
- [Code-backed content can replace fragile CMS workflows for agents](../concepts/code-backed-content-can-replace-fragile-cms-workflows-for-agents.md) - repository-backed content can make agent-managed operational data reviewable.
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](../concepts/agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) - infrastructure should include machine-friendly surfaces for agent users.

## Open Questions

- Which conversion and quantization recipes preserve enough model quality for each target device class?
- Which autoscaling signal best captures useful utilization for mixed small-model workloads?
- How far can local CPU, MPS, or Colab training runs be trusted before moving to larger accelerator infrastructure?
- Which billing events and dimensions should be metered so AI invoices are explainable without exposing implementation noise?
- Which prompt, tool, score, and trace artifacts should be promoted from local code into managed production infrastructure?
- Which operational data belongs in code-backed infrastructure when agents are responsible for maintaining it?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Accelerating AI on Edge - Chintan Parikh and Weiyi Wang, Google DeepMind](../sources/20260505_Lm8BLHkxiAo.md)
- [The Small Model Infrastructure Nobody Built (So We Did) - Filip Makraduli, Superlinked](../sources/20260505_qdh_x-uRs9g.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Mastering AI Pricing: Flexible & Agile Monetization - Mayank Pant, Stripe](../sources/20260501_CrqPcIZOOXA.md)
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md)
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md)
