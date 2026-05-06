# Use hooks for deterministic agent verification and live context injection

Summary: Hooks are event-driven harness controls that can add deterministic checks or refresh context around an agent's tool calls. They are useful when a recurring rule needs runtime enforcement or when external state changes while the agent is working.

Use when:
- Turning a repeated agent mistake into a runtime check or feedback rule.
- Keeping long-running agent work aware of user edits or changed external state.

Details:
- The source describes hooks as a way to do deterministic verification or insert context, with hooks registered as Agent SDK events. 01:47:08-01:47:23
- A hook can verify a spreadsheet after each operation or insert user-made spreadsheet changes after every tool call so the agent sees live context updates. 01:47:25-01:47:54
- Hooks can provide corrective feedback when an agent takes a brittle shortcut, for example telling it to write a script or read the data before proceeding. 01:49:55-01:50:13
- A concrete rule example is requiring the agent to read a file before writing to it, which adds determinism without retraining the model. 01:50:13-01:50:20

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Agent rules should emerge from observed off-rail behavior](agent-rules-should-emerge-from-observed-off-rail-behavior.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)

Sources:
- [Claude Agent SDK [Full Workshop] - Thariq Shihipar, Anthropic](../sources/20260105_TqC1qOfiVcQ.md), 01:47:08-01:50:20
