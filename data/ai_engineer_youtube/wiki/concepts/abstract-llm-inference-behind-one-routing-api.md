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
- **The economic reason to keep the abstraction, separate from the integration reason.** This page argues the layer on switching cost and convenience; Rizwan argues it as an option on a subsidy that will end. A SemiAnalysis experiment that ran long-horizon coding tasks until weekly limits were exhausted valued a $200 Claude plan at roughly $8,000 of API usage and a $200 Codex plan at roughly $14,000, which he reads as deliberate: "they're essentially going to subsidize this until they have as many engineers dependent on their tooling as possible… and then inevitably the price gouging." Coinbase is the exercised option — defaulting an internal gateway to GLM and Kimi "cut their AI spend by nearly half while their token usage continues to grow," a change possible at one component precisely because the routing layer existed. The cost of holding the option is named too: you give up "the latest new feature in something like Claude Code." ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 06:27-07:28, 10:27-10:55)

Related topics:
- [Inference](../topics/inference.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Expose local and open-source models through familiar API clients](expose-local-and-open-source-models-through-familiar-api-clients.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)

Sources:
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md), 19:16-21:47
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 06:27-07:28, 10:27-10:55
