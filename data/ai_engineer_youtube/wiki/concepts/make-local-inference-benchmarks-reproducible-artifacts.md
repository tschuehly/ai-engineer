# Make Local Inference Benchmarks Reproducible Artifacts

Summary: Local inference benchmarks should produce versioned artifacts that capture environment, model identity, responses, metadata, timing, and hardware metrics. Reproducibility matters because small measurement differences can change model-size and quantization decisions.

Use when:
- Comparing local serving options such as model size, precision format, or runtime.
- Turning a one-off benchmark into evidence for infrastructure or product decisions.

Details:
- The benchmark setup served models with vLLM inside an NVIDIA-optimized container so the local environment matched a production-style deployment environment. (02:40-03:04)
- Each model run followed the same protocol: Docker isolation, three mandatory warmup runs, and background GPU metrics logging at one-second intervals. (03:09-03:28)
- The orchestrator generated a unique timestamped directory with a sanitized model ID and stored endpoint responses, metadata, text outputs, and metrics for later verification. (03:33-04:05)
- For streaming applications, the measurement logic should timestamp the first chunk from the server to capture time to first token, not just total request completion. (04:13-05:03)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Profile small-model architectures on target hardware](profile-small-model-architectures-on-target-hardware.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)

Sources:
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md), 02:40-05:03
