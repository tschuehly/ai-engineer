# Use prompt-enforced todos as lightweight agent state

Summary: Todo lists can give a coding agent persistent structure without turning the whole workflow into deterministic orchestration. They work as lightweight state when the model can follow instructions about one active task, completion, blockers, and decomposition.

Use when:
- Adding planning state to a coding agent without building a full workflow engine.
- Deciding which agent workflow rules can be prompt-enforced and which need hard runtime enforcement.

Details:
- The source describes todos as structured but not structurally enforced: they are injected into the system prompt rather than enforced by application code. 17:55-19:06
- Useful todo rules include one task at a time, marking tasks complete, continuing blocked in-progress work, and breaking large tasks into smaller instructions. 18:11-18:35
- This design depends on current model instruction-following quality; the speaker notes that the same approach would not have worked reliably with older models. 18:37-18:52
- Prompt-enforced state is useful but should not be confused with a hard guarantee for high-risk actions or business rules. 19:03-19:24

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Prompt-coded product behavior reduces code but weakens hard guarantees](prompt-coded-product-behavior-reduces-code-but-weakens-hard-guarantees.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Keep workflow orchestration deterministic and put side effects in steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)

Sources:
- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md), 17:55-19:24
