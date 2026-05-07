# Separate generation and verification prompts or models

Summary: Agent workflows can borrow the high-assurance pattern of separate implementation and verification teams by using distinct prompts, contexts, or model providers for coding and testing. The goal is to reduce shared assumptions between the agent that creates code and the agent or process that validates it.

Use when:
- Designing coding-agent review flows for changes where confirmation bias or shared blind spots are likely.
- Choosing whether to use a second model, second prompt, or independent context for tests and safety analysis.

Details:
- The source recommends adapting independent verification teams into agent workflows by using separate prompts for testing versus writing code. 27:10-27:28
- It suggests using multiple model providers when stronger diversity is needed: one foundation model can generate tests while another writes the implementation. 27:28-27:39
- This pattern complements explicit risk analysis and safety cases, where the LLM describes what could go wrong and how the code mitigates each failure. 26:37-27:05
- The source also names adversarial testing as part of the high-assurance agent toolkit. 33:46-33:59

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Use hierarchical verification before trusting weak agent feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)

Sources:
- [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](../sources/20251124_qLqttdO33UM.md), 26:37-27:43, 33:46-33:59

