# Prompt Strings Entangle Task Intent With Model Tricks

Summary: Prompt blobs are poor programming abstractions because they mix durable task intent with temporary wording tricks, examples, output-format instructions, parsing assumptions, and inference-strategy hints.

Use when:
- Reviewing a prompt-heavy LLM system whose behavior is hard to port across models.
- Separating task definitions from output formatting, parsing, model-specific prompt hacks, and agent orchestration style.

Details:
- Khattab argues that prompts can work as management instructions to an agent-like worker, but they are a poor abstraction for programming AI systems because they are stringly typed and unstructured. 12:19-12:58
- A prompt often entangles the fundamental task definition with accidental model-specific discoveries such as a wording style, persona, example, XML/JSON instruction, or other trick that happened to improve one model. 13:00-14:25
- Prompt text can also bake in the current inference-time strategy, such as telling the model it is an agent or reasoning system, instead of letting the system choose or swap strategies separately. 13:38-13:56
- Natural-language definitions still matter, but they should be localized to the parts of the specification that cannot be expressed better in code, evals, schemas, or control flow. 14:28-15:20

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [DSPy programs keep LLM intent separate from prompt strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)
- [DSPy adapters make prompt format a swappable runtime layer](dspy-adapters-make-prompt-format-a-swappable-runtime-layer.md)
- [Avoid premature low-level AI system coupling](avoid-premature-low-level-ai-system-coupling.md)

Sources:
- [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](../sources/20250806_qdmxApz3EJI.md), 12:19-15:20
