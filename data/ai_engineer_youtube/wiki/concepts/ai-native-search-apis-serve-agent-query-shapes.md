# AI-Native Search APIs Serve Agent Query Shapes

Summary: Search APIs for agents should optimize for complex, contextual, high-volume information retrieval rather than human click behavior over short keyword queries.

Use when:
- Designing a search or RAG API consumed primarily by agents.
- Evaluating whether a human-oriented search engine is a good backing tool for agent research.

Details:
- The talk argues that LLMs still need search because model weights cannot store the whole, constantly changing web, especially when user requests depend on current or niche information.
- Human search engines optimize for short keyword inputs, click-worthy pages, and a few readable links; agents can issue many searches, pass multi-paragraph context, and process much larger result sets.
- Agent-oriented search should return what the agent asked for, not only what a human is likely to click. Example query shapes include "startups working on something huge that feels like Bell Labs," personalized restaurant searches with user context, and articles that argue one position but not another.
- A limit that reshaping the query interface does not fix: search answers the present, not change over it. Bright Data's Omer Primor's example is deliberately mundane — "I can search for… the cost of a certain pair of sneakers this morning. I cannot really search for how has that price changed over the last 6 months, what discounts it had," and likewise open job positions can be searched while headcount over time cannot. The information existed; nobody retained it, so "there's much more context in the web than what web search allows us to extract." Temporal and comparative questions therefore need a *collection* layer with history, not a better search API — which is the gap [context-as-a-service vendors](context-as-a-service-is-vertical-search-for-agents.md) and owned pipelines fill. (Ot4OPrPH4xY, 05:48-06:31)

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Context as a Service Is Vertical Search for Agents](context-as-a-service-is-vertical-search-for-agents.md)
- [Frequency, Not Volume, Drives Web-Context Cost](frequency-not-volume-drives-web-context-cost.md)

Sources:
- [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](../sources/20250729_xnXqpUW_Kp8.md), 05:46-13:51
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 05:48-06:31
