# High-assurance agentic coding needs process, not just generation

Summary: Agentic coding can target high reliability only when generated code is wrapped in explicit process: specifications, modularity, independent verification, defensive design, integration testing, certification boundaries, and feedback loops. Cheap code generation does not remove the need for an assurance workflow.

Use when:
- Designing agent workflows for critical code or reliability-sensitive systems.
- Explaining why "the model wrote it" is not enough evidence for production readiness.

Details:
- The talk uses Airbus A320 and Space Shuttle software as examples of reliability achieved through process, including specification-based design, independent verification teams, defensive programming, static analysis, and system-level reliability thinking. 07:19-12:09
- High-assurance process adds steps that ordinary coding workflows may skip, such as external certification, integration testing against physical systems, and feedback between adjacent process stages. 10:17-11:22
- For agentic coding, the same process mindset helps keep agents on the rails; process is not only human bureaucracy, it is a control surface for generated code quality. 10:17-10:28
- The source's definition of a bug is user-centered: behavior that does not match end-user expectations, whether caused by ambiguous specifications or implementation defects. 05:04-05:30

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI code quality needs full-SDLC workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)

Sources:
- [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](../sources/20251124_qLqttdO33UM.md), 05:04-12:09

