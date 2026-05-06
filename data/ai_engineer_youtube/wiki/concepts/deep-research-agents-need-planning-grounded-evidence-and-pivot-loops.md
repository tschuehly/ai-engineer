# Deep Research Agents Need Planning, Grounded Evidence, and Pivot Loops

Summary: Deep research agents are useful when the work requires open-ended discovery over external sources. They should plan a research path, use tools, inspect evidence, cite sources, pivot as understanding changes, and synthesize grounded findings.

Use when:
- Building research agents that must gather source-backed evidence rather than produce generic prose.
- Evaluating whether an agent has enough grounding, iteration, and provenance for research-heavy tasks.

Details:
- The workshop defines a deep research system as a reasoning system that plans what to research, has autonomy over the research path, and uses tools such as web, user-provided sources, or API access. 20:28-21:05
- Deep research is goal-driven: the user gives an objective rather than an exact procedure, and the agent replaces a human's search, inspection, pivoting, synthesis, and iteration loop. 21:04-21:27
- Research quality needs high precision and recall: enough relevant sources to cover the topic, but not so many that limited context is filled with noise. 22:12-22:27
- The system should reduce hallucination and AI slop by grounding synthesis in research artifacts and preserving source citation. 20:40-20:49, 22:27-22:34

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md), 20:28-22:34
