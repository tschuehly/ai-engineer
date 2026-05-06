# Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro

Source: [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](https://www.youtube.com/watch?v=HY_JyxAZsiE)
Uploaded: 2026-01-09
Transcript: `raw/20260109_HY_JyxAZsiE/HY_JyxAZsiE.en-orig.vtt`

## Summary

Al Harris presents Kiro's spec-driven development workflow as a way to turn agentic coding from prompt-to-code improvisation into a reproducible loop of requirements, design, task decomposition, implementation, and verification. The talk emphasizes structured natural-language requirements, EARS-style acceptance criteria, property-based tests, MCP-backed context gathering, customizable spec artifacts, feature-scoped spec folders, and steering files for durable project preferences.

## Extracted Concepts

- [Spec-driven development turns prompts into requirements, design, and tasks](../concepts/spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md) - shows the spec as both a point-in-time system artifact and the workflow that guides implementation.
- [Translate structured requirements into property-based tests](../concepts/translate-structured-requirements-into-property-based-tests.md) - connects EARS-style acceptance criteria to invariants that can falsify whether code meets the spec.
- [Keep spec artifacts feature-scoped, mutable, and context-backed](../concepts/keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md) - describes how specs should be scoped, amended, pruned, and enriched with MCP context or steering guidance instead of becoming one massive plan.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Kiro's core spec flow takes a prompt, generates clear requirements with EARS acceptance criteria, derives a design, defines system properties, builds a task list, and then runs the tasks. (03:32-06:18)
- The speaker frames a spec as a natural-language representation of the system that includes functional requirements, non-functional requirements, constraints, and concerns at a point in time. (05:34-06:05)
- Requirements verification is described as scanning for over-ambiguity, invalid constraints, and conflicting requirements, then helping resolve them with automated reasoning techniques. (06:33-06:48)
- MCP servers can participate in requirements generation, design, and implementation; the example uses task-tracker and fetch-style MCPs to pull existing task metadata or external examples into spec creation. (08:33-15:15)
- Because spec artifacts are structured natural language, teams can add local fields such as UI wireframes, explicit unit-test cases, or non-functional performance requirements before implementation begins. (15:35-18:47, 01:00:05-01:00:32)
- The talk warns that agents are good at declaring work complete even when tests fail, so task definitions should include explicit test cases and hooks can enforce completion conditions. (18:08-18:47)
- For task execution, Kiro can seed a fresh session from the spec and the selected task, with no shared context from previous task sessions unless the operator chooses to run all tasks together. (46:47-47:21)
- Specs are best treated as feature or problem-area artifacts; completed or low-value specs can be pruned, while still-relevant specs can be amended when new related requirements appear. (48:49-53:53)
- Cross-cutting changes, such as API changes involving security and PII logging, may need either one chosen destination spec or a cross-functional spec, and the human operator should make that boundary decision. (54:36-55:24)
- Steering files act like persistent local preferences for tradeoffs such as latency, cost, commit attribution, code style, and coverage expectations, and can influence both design and generated code. (01:01:34-01:03:05)
