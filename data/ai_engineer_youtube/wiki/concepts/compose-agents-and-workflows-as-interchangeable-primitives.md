# Compose agents and workflows as interchangeable primitives

Summary: Agents and workflows do not need to be rival top-level abstractions; production AI systems can compose them so agents call workflows, workflows call agents, and both appear as tools or steps.

Use when:
- Choosing between a ReAct-style agent loop and a structured workflow graph.
- Designing a system where some work needs flexible exploration and other work needs explicit sequencing or handoff.

Details:
- Bhagwat frames agents as turn-based interaction loops: a human or system takes a turn, the agent takes a turn, and the agent may continue through tool calls or additional turns. (08:03-08:22)
- Workflows are framed as dependency-aware rules engines or data pipelines where step order, branching, parallelism, conditions, loops, suspend/resume, and replay are explicit. (08:22-09:22)
- Composition is the intended primitive set: an agent can be a workflow step, a workflow can be an agent tool, an agent can itself be a tool, and a workflow can be nested as a step. (11:46-12:07)
- Supervisor-agent patterns can call specialist research, summary, or orchestration agents as tools; workflow-mediated handoffs and dynamic tool injection are other composition patterns. (12:10-13:53)
- The practical test is whether the combination works for the application, because the field's practice is evolving faster than clean theory. (14:37-15:03)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Retrieve Tool Descriptions Before Loading Large Tool Catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [Specialist Expert Systems Bundle Capabilities, APIs, and Instructions](specialist-expert-systems-bundle-capabilities-apis-and-instructions.md)

Sources:
- [Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai](../sources/20250801_8SUJEqQNClw.md), 08:03-15:03
