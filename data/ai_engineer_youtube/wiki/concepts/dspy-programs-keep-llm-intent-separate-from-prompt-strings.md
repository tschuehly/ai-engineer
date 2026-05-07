# DSPy Programs Keep LLM Intent Separate From Prompt Strings

Summary: DSPy treats LLM calls as typed parts of a program, so developers specify inputs, outputs, and control flow while the framework handles prompt construction and parsing details.

Use when:
- Designing LLM applications where manual prompt strings are becoming brittle implementation detail.
- Choosing whether to encode an AI workflow as ordinary program structure plus LLM-backed functions.

Details:
- The talk frames DSPy as building "proper Python programs" rather than repeatedly tweaking prompt strings; the program declares what it wants to do, what inputs it accepts, and what outputs it returns. 02:00-04:25
- DSPy signatures and modules make LLM calls resemble ordinary function calls with typed input and output expectations, while still letting engineers inspect or customize lower-level behavior when needed. 03:09-03:46, 05:36-06:04
- This separation helps preserve application control flow and intent while models, prompting paradigms, or output formats change underneath the program. 04:54-05:35
- The abstraction is not a universal replacement for other AI libraries; the source explicitly notes Pydantic AI, LangChain, Agno, and other frameworks may fit some cases. 06:11-06:25
- Khattab frames signatures as DSPy's first-class concept for decoupling the application-specific task from evolving model, adapter, search, learning, and optimizer machinery. 17:25-19:04

Related topics:
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [DSPy adapters make prompt format a swappable runtime layer](dspy-adapters-make-prompt-format-a-swappable-runtime-layer.md)
- [Optimize LLM programs with metrics and teacher feedback](optimize-llm-programs-with-metrics-and-teacher-feedback.md)
- [Avoid premature low-level AI system coupling](avoid-premature-low-level-ai-system-coupling.md)
- [Prompt strings entangle task intent with model tricks](prompt-strings-entangle-task-intent-with-model-tricks.md)

Sources:
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md), 02:00-06:25
- [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](../sources/20250806_qdmxApz3EJI.md), 17:25-19:04
