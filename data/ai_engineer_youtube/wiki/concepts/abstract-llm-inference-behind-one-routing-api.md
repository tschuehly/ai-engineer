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
- **The abstraction is not free, and the seams show exactly when you need it most.** Manuja's warning is that "fallbacks are not transparent": "while the industry is converging on an OpenAI API compatible format… there are still nuances," specifically in "tool calling schemas, token limits, stop reasons and what have you." Each breaks a different thing — schema differences break agent calls, token limits truncate, and a differing stop reason makes the caller mis-handle a response that succeeded. The remedy is that the routing layer must include "a normalization layer that can ensure that you can do cross provider fallbacks," and that "you need to really test your fallbacks well," because the switching cost this page attributes to the abstraction is only near-zero once someone has paid it in the gateway. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 04:35-05:07)


- **The abstraction taken one step further: the layer chooses the model instead of exposing the choice.** DigitalOcean's inference router keeps the same OpenAI-compatible proxy shape — "zero application code changes needed from you to get it to adopt" — but makes the routing decision itself, per request, from a declared preference set rather than from a model name in the call ([Kamath & Gillam](../sources/20260822_FvxY8oPoI8o.md), 04:42-05:07, 13:47-14:28). That is a meaningful change to what the abstraction is for: a marketplace lowers switching cost between models you pick, and a router removes the pick. Both rest on the same normalization work Manuja flags above, and the router adds a reason to care about it, since cross-model differences now surface without anyone at the call site having chosen to move.
- **Open-sourcing the layer as the anti-lock-in argument.** The proxy and the routing model are both released — "both open source. There is no vendor lock-in, which is a key DigitalOcean value" (04:42-05:02), restated at the close as "routing you can customize, evaluate and improve without vendor lock-in" (05:35-05:48). Read against Rizwan's framing above, this is the same option on a subsidy argued by the provider rather than the customer: a routing layer whose policy you can read and whose model you can run yourself is an exit that a hosted routing endpoint is not. Caveat worth keeping: open-sourcing the router does not open-source the models it routes to, so the exit it buys is from the routing vendor, not from the model market.

Related topics:
- [Inference](../topics/inference.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Expose local and open-source models through familiar API clients](expose-local-and-open-source-models-through-familiar-api-clients.md)
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [A Subsidized Coding-Agent Subscription Is a Lock-In Ramp](a-subsidized-coding-agent-subscription-is-a-lock-in-ramp.md)
- [Your Fallback Provider Is Under-Tested and Under-Provisioned](your-fallback-provider-is-under-tested-and-under-provisioned.md)
- [Declare Routing Preferences So a Bad Route Is Fixable](declare-routing-preferences-so-a-bad-route-is-fixable.md)
- [A Router Must Be Cheap and Fast Enough to Disappear](a-router-must-be-cheap-and-fast-enough-to-disappear.md)
- [Give Each Task a Model Pool With an Explicit Selection Policy](give-each-task-a-model-pool-with-an-explicit-selection-policy.md)

Sources:
- [The Next Unicorns: 7 Top AI startups from the HF0 Residency](../sources/20250821_L8-5ezsoI5A.md), 19:16-21:47
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 06:27-07:28, 10:27-10:55
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 04:35-05:07
- [Preferences Over Benchmarks: Model Routing — Archana Kamath & Tyler Gillam, DigitalOcean](../sources/20260822_FvxY8oPoI8o.md), 04:42-05:48, 13:47-14:28
