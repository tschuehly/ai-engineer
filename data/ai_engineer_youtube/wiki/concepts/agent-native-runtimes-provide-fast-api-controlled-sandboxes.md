# Agent-Native Runtimes Provide Fast API-Controlled Sandboxes

Summary: Agent-native runtimes give agents a fast, isolated computing environment they can control through APIs, with preloaded machine-readable tools rather than only a human terminal UI.

Use when:
- Designing sandbox infrastructure for agents that run code, analyze data, use computers, or perform RL-style environment work.
- Deciding whether a devtool runtime is optimized for human operation or agent operation.

Details:
- Daytona is described as secure elastic infrastructure for running AI-generated code: an agent-native runtime, or sandbox, that gives agents a computing environment for code execution, data analysis, reinforcement learning, computer use, and other tasks. 08:12-08:48
- Burazin compares the runtime to a laptop for agents: it is the computing substrate agents inhabit while doing work. 08:48-09:04
- Agent runtime startup latency matters because interactive users should not wait for tools to turn on; Daytona optimized sandbox startup to roughly 27 milliseconds. 09:07-09:24
- API control is part of the runtime contract: an agent should be able to turn machines on and off, clone them, delete them, and perform environment operations through a machine-native interface. 09:24-09:31
- Preloaded headless tools such as file explorer, git client, LSP, and terminal avoid forcing the agent to parse only raw terminal output. 09:33-09:53

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Give Code-Executing Agents Isolated Computers](give-code-executing-agents-isolated-computers.md)
- [Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)

Sources:
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 08:12-09:53
