# Keep Fixed Business Logic Outside the Model

Summary: Fixed rules and state transitions should live in deterministic application logic, with the model updating validated state through tools rather than deciding every condition from prompt text.

Use when:
- A workflow has hard eligibility rules, approval requirements, or state transitions.
- An agent design relies on the LLM to remember and enforce business logic that could be checked in code.

Details:
- The talk cautions that teams often ask the LLM to apply fixed business logic when the safer pattern is to expose tools that update state and validate each condition separately, 08:04-08:29.
- Deterministic business logic should hold the rule that an action occurs only when required conditions are met; the model can help gather or update the state, but the gate should remain outside the model, 08:29-08:43.
- This pattern keeps maintainable logic external to the model while still allowing agentic exploration and enrichment before the final action, 08:21-08:39.

Related topics:
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Add structure where agent reliability fails](add-structure-where-agent-reliability-fails.md)

Sources:
- [Building Applications with AI Agents — Michael Albada, Microsoft](../sources/20250724_R30col3UPUg.md), 08:04-08:43
