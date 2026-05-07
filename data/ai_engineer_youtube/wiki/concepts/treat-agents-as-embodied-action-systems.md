# Treat agents as embodied action systems

Summary: Production agents should be designed as actors with a digital body, not as disembodied chat models. Their tools, APIs, MCP servers, terminal, browser, VM, operating system access, and persistent files determine what actions are possible and what consequences must be managed.

Use when:
- Designing the runtime boundary between a model and its tools, workspace, browser, VM, or operating system.
- Explaining why model quality alone is insufficient for reliable agentic systems.

Details:
- Hu maps robotics embodiment to digital agents: a robot has hardware, sensors, actuators, and a fleet; an agent has a body made of APIs, MCPs, terminal, browser, VM, OS access, and persistent file systems. (01:48-02:44)
- The surrounding system can dominate production reliability: monitoring, retraining, human feedback, simulation, deployment, and development tooling are part of the agent product, not support work after the model is done. (01:23-03:04)
- The self-driving lesson is that the winning system depends on offline infrastructure as well as the online model, because the offline stack lets developers improve faster and ship more reliably. (02:51-03:04)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Unified coding-agent harnesses combine models, tools, environments, and safety](unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md)

Sources:
- [Agents are Robots Too: What Self-Driving Taught Me About Building Agents - Jesse Hu, Abundant](../sources/20251124_qqXdLf3wy1E.md), 01:23-03:04
