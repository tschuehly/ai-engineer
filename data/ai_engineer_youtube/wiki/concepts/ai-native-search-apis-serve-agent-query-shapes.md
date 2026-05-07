# AI-Native Search APIs Serve Agent Query Shapes

Summary: Search APIs for agents should optimize for complex, contextual, high-volume information retrieval rather than human click behavior over short keyword queries.

Use when:
- Designing a search or RAG API consumed primarily by agents.
- Evaluating whether a human-oriented search engine is a good backing tool for agent research.

Details:
- The talk argues that LLMs still need search because model weights cannot store the whole, constantly changing web, especially when user requests depend on current or niche information.
- Human search engines optimize for short keyword inputs, click-worthy pages, and a few readable links; agents can issue many searches, pass multi-paragraph context, and process much larger result sets.
- Agent-oriented search should return what the agent asked for, not only what a human is likely to click. Example query shapes include "startups working on something huge that feels like Bell Labs," personalized restaurant searches with user context, and articles that argue one position but not another.

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)

Sources:
- [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](../sources/20250729_xnXqpUW_Kp8.md), 05:46-13:51
