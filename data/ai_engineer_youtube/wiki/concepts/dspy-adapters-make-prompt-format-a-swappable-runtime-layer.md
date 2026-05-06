# DSPy Adapters Make Prompt Format a Swappable Runtime Layer

Summary: DSPy adapters separate a program's logical signature from the concrete prompt representation sent to the model, letting teams test formats such as JSON or BAML without rewriting the workflow.

Use when:
- Comparing prompt formats, structured-output styles, or token overhead while keeping an LLM program's logic stable.
- Moving between models or providers that respond better to different formatting conventions.

Details:
- DSPy adapters control how signatures are rendered to a model, including JSON, BAML, XML-like, or other prompt formats. 09:09-09:12, 60:38-60:45
- The talk demonstrates replacing a JSON adapter with a BAML adapter; the rest of the program continues to call the same logical module while the model-visible prompt changes. 21:10-21:44
- Adapter choice is also a cost and context lever: verbose generated prompt text can increase token usage, while a compressed adapter or context-compression logic can reduce what is sent to the model. 71:44-72:24

Related topics:
- [Tools](../topics/tools.md)

Related concepts:
- [DSPy programs keep LLM intent separate from prompt strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)
- [Expose large APIs through typed code mode](expose-large-apis-through-typed-code-mode.md)

Sources:
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md), 09:09-09:12, 21:10-21:44, 71:44-72:24
