# Use Supervisory Graph Agents To Update Shared Knowledge State

Summary: A graph-backed advisory system can use a supervisory agent to coordinate specialist agents and write their findings into a shared graph. This keeps decision context as inspectable state instead of leaving it only in transient agent messages.

Use when:
- Prototyping multi-agent advisory workflows where different agents collect, analyze, or update different parts of a domain graph.
- Deciding what durable state a multi-agent workflow should share across agent roles.

Details:
- The competitive-analysis prototype maps the wisdom engine into an orchestration or supervisory agent that oversees agents for the other nodes in the decision taxonomy. 07:18-08:37, 09:40-10:07
- The workflow is prototyped in n8n, using AI agent nodes that can call OpenAI, Anthropic, or on-prem models while leaving room to move to lighter-weight frameworks later. 08:40-10:00
- A specialist insight agent can collect product sentiment from social media and update its perspective into a centralized graph, while other agents update their own graph regions. 10:07-10:47
- The shared graph is intended to hold the taxonomy and decision context that a marketing strategist might otherwise spread across SharePoint folders and manual analysis artifacts. 10:44-11:24

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Knowledge graphs make agent memory traversable and explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)

Sources:
- [Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI](../sources/20250822_9AQOvT8LnMI.md), 07:18-11:24
