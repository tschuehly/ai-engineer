# Type-Safe Agent Schemas Make Refactoring and Validation Easier

Summary: Typed agent outputs and typed tool dependencies make AI applications easier to refactor and validate because the runtime contract is visible to static tooling and checked again at execution time.

Use when:
- Choosing an agent framework for structured extraction or tool-heavy workflows.
- Refactoring an AI application whose prompts, outputs, and tool dependencies are changing quickly.

Details:
- Colvin argues that GenAI applications still need reliable, scalable software practices, and type safety matters because teams rarely know the final shape of an AI application upfront and will refactor it repeatedly. 00:44-01:29
- In the Pydantic AI example, the `Agent` output type is generic in a Pydantic model, so `result.output` is both statically understood and runtime-validated as that model. 06:58-07:41
- Typed dependencies extend the same contract to tools: tool functions receive a run context parameterized by the dependency type, and the agent run must supply an instance of that dependency type. 07:47-09:23
- The source contrasts this work with less type-safe agent frameworks, while acknowledging that the stronger typing adds setup work for framework and application authors. 01:30-01:47, 09:23-09:35

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent Tool Loops Turn Model-Required Actions Into Executable Results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Give Coding Agents the Same Engineering Infrastructure Humans Need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Translate Structured Requirements Into Property-Based Tests](translate-structured-requirements-into-property-based-tests.md)

Sources:
- [Human seeded Evals - Samuel Colvin, Pydantic](../sources/20250725_o_LRtAomJCs.md), 00:44-01:47, 06:58-09:35
