# Abstract LLM Inference Behind One Routing API

Summary: A model marketplace can make heterogeneous LLM providers feel like one routing surface. The abstraction should cover model switching, provider edge cases, tool calling, caching, regional performance, privacy controls, rankings, and observability.

Use when:
- Building model-routing infrastructure across multiple hosted providers and open models.
- Explaining why a single API can reduce integration and switching cost without making model quality identical.

Details:
- OpenRouter describes evolving from bring-your-own-model browser experiments into a single API and payment surface for accessing many language models. (19:16-19:47)
- The routing layer handles model switching, tool calling, edge cases, caching, price, regional performance, and uptime so users can move between providers with near-zero switching cost. (19:43-20:01)
- The marketplace exposes model filtering by context, features, tool calling, and structured output, plus a chat surface for head-to-head comparison. (20:01-20:31)
- The platform adds API-level privacy controls, observability for which models are used and why, public ranking data based on real-world usage, and prompt-category comparisons. (20:32-20:52)
- OpenRouter describes a plugin middleware layer for inference that can call MCPs and transform model outputs, making provider abstraction programmable rather than only a proxy. (21:29-21:47)

Related topics:
- [Inference](../topics/inference.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Expose local and open-source models through familiar API clients](expose-local-and-open-source-models-through-familiar-api-clients.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)

Sources:
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md), 19:16-21:47
