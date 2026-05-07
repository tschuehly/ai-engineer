# Avoid Premature Low-Level AI System Coupling

Summary: Durable AI systems should encode the application-specific problem at the highest justified abstraction level, then let models, inference strategies, prompt formats, and learning algorithms change underneath.

Use when:
- Deciding whether a prompt trick, model quirk, inference strategy, or hand-optimized workflow should become part of the system contract.
- Designing AI software that should survive frequent model and tooling changes.

Details:
- Khattab reframes the bitter lesson for AI engineering: domain knowledge is not harmful by itself; it becomes harmful when it prematurely constrains the system in ways that reflect weak understanding. 07:21-08:07
- Premature optimization means hard-coding behavior at a lower abstraction level than the engineer can justify; his square-root analogy says to ask for the square root rather than hard-code machine-specific bit manipulation unless the higher-level abstraction has been shown inadequate. 08:11-10:42
- For AI applications, the lower-level pieces likely to expire quickly include model behavior, inference strategy, search, learning algorithms, output formatting, and model-specific prompt guidance. 01:03-03:25, 16:29-17:22
- The stable engineering work is defining the task, signatures, essential control flow, tool boundaries, and evaluation criteria specific to the application. 14:28-15:26, 18:24-18:52

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [DSPy programs keep LLM intent separate from prompt strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)
- [Prompt strings entangle task intent with model tricks](prompt-strings-entangle-task-intent-with-model-tricks.md)
- [Use evals as durable AI system specifications](use-evals-as-durable-ai-system-specifications.md)

Sources:
- [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](../sources/20250806_qdmxApz3EJI.md), 01:03-03:25, 07:21-10:42, 14:28-18:52
