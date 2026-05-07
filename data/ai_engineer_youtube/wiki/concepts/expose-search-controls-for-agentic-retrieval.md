# Expose Search Controls For Agentic Retrieval

Summary: Agent-facing search APIs should expose controllable retrieval parameters such as result count, date ranges, domains, and neural-versus-keyword mode so agents can shape searches to the task.

Use when:
- Building tool schemas for web search inside an agent loop.
- Deciding which retrieval knobs should be visible to an AI agent instead of hidden in a human dashboard.

Details:
- The Exa dashboard/API demo highlights controls for number of results, date ranges, domain scoping, and neural versus keyword search modes.
- These controls matter more for agents than for ordinary users because agents can call the API repeatedly, search with longer context, request thousands of results, and combine searches during multi-step work.
- The practical API design lesson is to expose precise search affordances as parameters rather than collapsing them into one opaque search box.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Translate API Endpoints Into Agent Stories](translate-api-endpoints-into-agent-stories.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)

Sources:
- [Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai](../sources/20250729_xnXqpUW_Kp8.md), 14:32-15:10
