# Choose Autonomy Level by Task Uncertainty and Control Needs

Summary: AI systems should use the minimum autonomy that fits the task. More agentic behavior can handle uncertainty and tool choice, but it increases cost, latency, uncertainty, and loss of control.

Use when:
- Deciding whether to build a prompt, workflow, single agent, or multi-agent system.
- A requested "agent" may actually be a predictable workflow with data, tools, routing, and memory.

Details:
- The workshop describes an autonomy slider from prompting, to context engineering and tools, to workflows, orchestration, eval systems, and agentic systems; each step adds autonomy but reduces control and usually increases cost. 06:49-07:44
- Many client "agent" requests were found to be simple workflows that could be defined upfront, making an open-ended agent unnecessary. 07:49-08:08
- Workflows can be reliable when the steps are known: add data, tools, memory, prompt chains, routers, parallel branches, and strict conditions before adding autonomous planning. 08:15-09:26
- Agents become useful when the system must plan which tools to use or not use, act in an environment, and handle uncertain paths rather than execute a known sequence. 09:57-10:34

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md), 06:49-10:34
