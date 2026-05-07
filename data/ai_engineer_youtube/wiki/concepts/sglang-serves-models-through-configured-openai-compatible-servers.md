# SGLang Serves Models Through Configured OpenAI-Compatible Servers

Summary: SGLang can be treated as a production model-server runtime whose behavior is mostly shaped by model, hardware, and launch flags. API compatibility lets application or benchmark clients call the served model through familiar chat-completion paths while deployment packaging handles the GPU environment.

Use when:
- Choosing a serving runtime for open LLM or VLM deployments.
- Packaging a model server while preserving OpenAI-shaped client code.
- Debugging model-server behavior through launch flags and support matrices.

Details:
- SGLang is positioned as an open-source fast serving framework for LLMs and VLMs, in the same production-serving category as vLLM and TensorRT-LLM. (02:14-02:28)
- The basic deployment shape is a server command running inside a Docker container; the workshop packages SGLang dependencies and the launch command into Truss YAML before shipping the deployment to a GPU. (07:10-07:45)
- Useful SGLang operation depends on knowing available flags, configuration options, support matrices, and which optimizations compose cleanly; the speakers caution that aggressive speculation and very high batch sizes may interact badly. (08:45-09:23)
- The demo exposes an OpenAI-compatible server, uses a local URL and port, and sends chat-completion traffic from a benchmark/client process. (20:24-21:24)
- SGLang's serving surface includes prefill/decode disaggregation, constrained decoding, function calling, OpenAI-compatible serving, and broad model support. (34:20-34:32)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Expose local and open-source models through familiar API clients](expose-local-and-open-source-models-through-familiar-api-clients.md)
- [Production inference combines model support with cluster operations](production-inference-combines-model-support-with-cluster-operations.md)
- [Benchmark inference with use-case-shaped token loads](benchmark-inference-with-use-case-shaped-token-loads.md)

Sources:
- [Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten](../sources/20250726_Ahtaha9fEM0.md), 02:14-02:28, 07:10-09:23, 20:24-21:24, 34:20-34:32
