# Validation Errors Can Drive Agent Self-Repair Loops

Summary: Structured validation failures can become actionable feedback inside an agent loop. Instead of accepting malformed output, the harness can return the validation error to the model and ask for a corrected attempt.

Use when:
- Extracting structured data from unstructured text or documents.
- Designing retry behavior for model outputs that must satisfy typed schemas or business constraints.

Details:
- The source notes that a minimal agent loop needs an explicit completion condition, such as final text, a final-result tool, or a structured output type. 02:43-03:30
- Pydantic AI can model structured extraction as a final-result tool, validate the output against a Pydantic schema, and only return the typed data once validation passes. 03:33-04:37
- In the date-of-birth demo, a field validator rejected the model's first interpretation; the harness sent the validation error back to the model with a retry instruction, and the second model call produced a valid result. 04:43-06:43
- The production lesson is not to hide missing requirements in validators: when a constraint is known, put it in the field description or schema too; validation feedback is still useful because even strong models sometimes fail schema constraints. 05:25-05:45

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Prefer Simple Debuggable Eval Scores](prefer-simple-debuggable-eval-scores.md)
- [Agent Tool Loops Turn Model-Required Actions Into Executable Results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Translate Structured Requirements Into Property-Based Tests](translate-structured-requirements-into-property-based-tests.md)

Sources:
- [Human seeded Evals - Samuel Colvin, Pydantic](../sources/20250725_o_LRtAomJCs.md), 02:43-06:43
