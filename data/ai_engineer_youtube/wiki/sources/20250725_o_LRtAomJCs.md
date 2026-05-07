# Human seeded Evals - Samuel Colvin, Pydantic

Source: [Human seeded Evals - Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=o_LRtAomJCs)
Uploaded: 2025-07-25
Transcript: `raw/20250725_o_LRtAomJCs/o_LRtAomJCs.en-orig.vtt`

## Summary

Samuel Colvin's talk does not reach the promised human-seeded eval material; it demonstrates Pydantic AI patterns for building safer agent applications with typed output schemas, validation-error feedback loops, typed tool dependencies, and Logfire traces that expose model calls, tool arguments, latency, and cost.

## Extracted Concepts

- [Type-Safe Agent Schemas Make Refactoring and Validation Easier](../concepts/type-safe-agent-schemas-make-refactoring-and-validation-easier.md) - the source argues that typed outputs and typed dependencies let both humans and coding agents refactor AI applications with more confidence.
- [Validation Errors Can Drive Agent Self-Repair Loops](../concepts/validation-errors-can-drive-agent-self-repair-loops.md) - the source demonstrates feeding Pydantic validation failures back to the model so it can retry with corrected structured output.
- [Trace Agent Tool Arguments to Debug Real Failures](../concepts/trace-agent-tool-arguments-to-debug-real-failures.md) - the source uses Logfire traces to diagnose a memory retrieval failure from the exact tool argument the model chose.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- The talk frames agent applications as still needing ordinary reliability and scalability, and says type safety matters because AI applications will be refactored repeatedly as teams discover their shape. 00:44-01:29
- A minimal agent loop needs a clear termination condition; final text, final-result tools, or structured output types can define the end of a run, but loop exit is not automatic. 02:43-03:30
- Pydantic AI can call a final-result tool, validate the structured result, and return a typed object rather than leaving downstream code to consume loose JSON. 03:33-04:37
- When a date field failed validation, the framework returned the validation error to the model and asked it to try again; the second model call corrected the output. 04:43-06:43
- Agent output types and dependency types are modeled as generics so static type checkers and runtime Pydantic validation can catch wrong field access or wrong dependency shape. 06:58-09:35
- A Logfire trace showed why a simple memory example failed: the model called `retrieve_memory` with "your name" instead of a substring contained in the stored memory, then succeeded when it used "name". 10:19-11:36
- Logfire also surfaces timing and pricing across the whole trace and individual spans, making cost and latency inspectable alongside tool behavior. 11:39-11:49
