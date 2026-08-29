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
- **The same slider read as a deployment sequence rather than a design choice.** Shenoy's five-rung version (copilot → synchronous agent → asynchronous agent → long-running agent → AI coworker) adds a constraint this page does not: the rung you may occupy is set jointly by the model and by the deploying organization, so "you have to earn the right to do more" and "it's not enough to jump to the co-worker immediately." Choosing the minimum autonomy that fits the task is the static version; his is the same rule applied over time, where each rung has to be demonstrated before the next is granted. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 05:23-07:33)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)

Sources:
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md), 06:49-10:34
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 05:23-07:33
