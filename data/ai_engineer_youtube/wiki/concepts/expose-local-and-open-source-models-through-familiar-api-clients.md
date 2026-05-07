# Expose local and open-source models through familiar API clients

Summary: Local or self-hosted open-source models are easier to adopt when they can be addressed through the same client shape developers already use for hosted model APIs.

Use when:
- Wrapping compiled, local, or edge models for application teams.
- Designing a model gateway that should hide whether inference runs locally, remotely, or through a specialized runtime.

Details:
- The talk frames the desired interface as an OpenAI-style client where developers can change the model argument without rewriting infrastructure-specific application code. (02:54-03:09)
- In the embedding demo, a JavaScript client maps the requested model name to a compiled library path, loads the native dynamic library through FFI, executes it, and reshapes the result to look like the official OpenAI embedding response. (15:02-17:20)
- This API compatibility does not remove deployment work; it moves runtime-specific concerns behind the client boundary so the application can treat local, remote, llama.cpp, TensorRT, and compiled-native targets more uniformly. (01:20-01:37, 16:12-17:20)

Related topics:
- [Inference](../topics/inference.md)
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Compile Python inference functions into portable native binaries](compile-python-inference-functions-into-portable-native-binaries.md)
- [Open model families need ecosystem-compatible tooling](open-model-families-need-ecosystem-compatible-tooling.md)

Sources:
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md), 01:20-17:20
