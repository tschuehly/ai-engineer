# Use LLMs to generate compiler lowerings under verification

Summary: LLMs are useful inside compiler pipelines when the compiler narrows the task to generating reusable elementary operation implementations, then constrains the result with type information, compilation, and tests.

Use when:
- Building a transpiler or compiler that needs many backend implementations of language or library primitives.
- Deciding where LLM code generation is reliable enough for infrastructure work.

Details:
- Muna first tried LLMs to generate full traces from Python source because structured outputs can match a schema, but the approach was too slow for the tracing path. (07:00-07:34)
- The more tractable LLM role is generating native C++ or Rust equivalents for elementary Python operations; program variety then comes from composing those operations rather than asking the model to translate arbitrary whole programs each time. (11:36-13:32)
- The compiler structure supplies guardrails around the generated pieces: AST-derived IR, type propagation, native compilation, and the talk's stated verification and LLM-powered testing boundary keep generated operation code from being accepted as free-form text. (01:41-02:10, 13:35-14:18)
- This pattern challenges a common overbroad use of LLMs: the model is not the compiler; it helps manufacture backend coverage for a compiler that still owns representation, typing, and execution constraints. (07:00-14:18)
- **Verification constrains correctness, and says nothing about speed.** This page's constraint set — types, compilation, tests — is exactly the set that a multi-GPU kernel benchmark found sufficient for correctness and insufficient for performance: with sampling or self-correction models "can often compile the kernels," while the design choices that determine speed (collective ordering, data partitioning, intra- versus inter-SM scheduling, transfer mechanism) go unmade. Where the generated artifact is judged on more than validity, add the quality axis to the verifier or accept a plateau on it. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 26:28-27:06)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Compile Python inference functions into portable native binaries](compile-python-inference-functions-into-portable-native-binaries.md)
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Overlap Communication With Compute Intra-SM or Inter-SM by Data Alignment](overlap-communication-with-compute-intra-sm-or-inter-sm.md)

Sources:
- [Compilers in the Age of LLMs - Yusuf Olokoba, Muna](../sources/20251124_q2nHsJVy4FE.md), 01:41-14:18
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 26:28-27:06
