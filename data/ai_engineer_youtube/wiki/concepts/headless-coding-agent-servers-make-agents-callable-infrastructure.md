# Headless Coding-Agent Servers Make Agents Callable Infrastructure

Summary: A terminal coding agent becomes infrastructure when it exposes a headless server API that other workflows can call. Packaging the agent with Git, GitHub CLI, shell tools, credentials, and a configured runtime lets scheduled systems create sessions and request pull requests without relying on an interactive terminal UI.

Use when:
- Embedding a coding agent inside a backend workflow or product automation.
- Turning a local terminal agent into a callable service with controlled tools.

Details:
- OpenCode is described as an open-source terminal coding agent that can choose different LLM providers, 09:09-09:30.
- Its architecture starts both a terminal UI and a server; because the UI is only a client, another workflow can bring its own client and talk to the server API, 09:33-10:08.
- The demo runs OpenCode on Railway as a server with the tools needed for repair work, including filesystem access, Git, GitHub CLI, shell utilities, and PR creation capability, 10:09-11:39.
- The generate-fix workflow creates a coding-agent session per repository, passes the analyzed repair plan into that session, and expects the agent to open a pull request when the fix is complete, 16:50-17:20.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use coding agents as programmable subagents inside products](use-coding-agents-as-programmable-subagents-inside-products.md)
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)

Sources:
- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md), 09:09-11:39, 16:50-17:20
