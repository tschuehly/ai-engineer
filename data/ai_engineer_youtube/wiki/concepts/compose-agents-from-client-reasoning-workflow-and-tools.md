# Compose Agents From Client, Reasoning, Workflow, and Tools

Summary: Production agents can be decomposed into four cooperating layers: the client interface, the reasoning model, workflow coordination, and action tools. This decomposition helps teams identify which part of an agent is responsible for interaction, planning, state, and side effects.

Use when:
- Designing an agent architecture before choosing frameworks or model providers.
- Debugging whether an agent failure came from UI modality, model reasoning, workflow state, or tool execution.

Details:
- Kozlov frames an agent as four components: a client where humans interact, an AI reasoning piece that decides what to do, workflows that execute and track actions, and tools such as APIs, browsers, internal services, or vector databases that perform work. 05:22-07:26
- A voice CRM-agent example adds concrete modality infrastructure: WebRTC input, speech-to-text, chat or voice client hosting, a gateway for caching and evals, an LLM for planning, workflow state, tools, and sometimes human verification. 06:19-07:31
- The framing separates model selection from the rest of agent engineering: the talk explicitly skips deep model choice because the surrounding client, workflow, and tool pieces remain necessary regardless of model. 18:47-19:19

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Use durable execution for production agent loops](use-durable-execution-for-production-agent-loops.md)

Sources:
- [Building Agents (the hard parts!) - Rita Kozlov, Cloudflare](../sources/20250723_j_TKDweOsYE.md), 05:22-07:31, 18:47-19:19
