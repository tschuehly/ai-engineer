# Compile Python inference functions into portable native binaries

Summary: Python is useful for expressing model inference, but portable low-latency deployment can compile the inference function into native artifacts that run outside Python and Docker-heavy serving paths.

Use when:
- Packaging an open-source model for local, edge, desktop, mobile, or cloud execution.
- Reducing application changes when a model must move between local and remote inference targets.

Details:
- The Muna pipeline starts from a plain Python inference function, traces it into an intermediate graph, propagates types, generates lower-level C++ or Rust, compiles a dynamic library, and loads that library from the caller's runtime. (04:05-05:19, 14:13-15:58)
- Torch FX was not enough for this compiler shape because it focused on PyTorch operations and fake tensor inputs, while arbitrary user inference code can involve NumPy, OpenCV, dictionaries, images, or other non-tensor values. (05:33-06:59)
- Type propagation is the bridge from dynamic Python to statically typed native code: annotated function inputs, global constants, and operation signatures determine intermediate output types before code generation. (08:16-11:34)
- The deployment motivation is hybrid inference, where smaller local or edge models work near users while larger cloud models remain available for heavier reasoning. (03:20-03:49)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Expose local and open-source models through familiar API clients](expose-local-and-open-source-models-through-familiar-api-clients.md)
- [Use LLMs to generate compiler lowerings under verification](use-llms-to-generate-compiler-lowerings-under-verification.md)

Sources:
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md), 03:20-15:58
