# Compare Models by Task, Thinking Budget, Cost, and Latency

Summary: Model choice should be treated as a task-level routing decision across capability, thinking depth, speed, and cost rather than a reflexive choice of the largest model.

Use when:
- Selecting between model tiers for a prototype, production feature, or multimodal workflow.
- Tuning reasoning depth for an interactive task where latency and cost compete with answer quality.

Details:
- AI Studio exposes thinking levels from minimal to high; Bailey keeps thinking low or minimal during time-sensitive demos and turns it up only when extra reasoning tokens are worth the latency or spend.
- Bailey frames Gemini 3.1 Pro as the largest, slower, and more expensive model, Gemini 3 Flash as a production workhorse, and Gemini 3.1 Flash-Lite as a lower-cost, fast option gaining adoption from older Flash users.
- Compare mode lets engineers test model variants side by side under similar tool settings, including code execution, which makes routing decisions more empirical.
- Anthropic describes thinking as an API-controlled budget: developers can decide whether Claude should spend more tokens reasoning for complex debugging or answer quickly for simpler work. 02:20-03:09
- **A reasoning model's latency is a distribution with a very long tail, not a number to put in a comparison table.** From production: "you cannot set the temperature to zero in many cases and the same prompt can take somewhere from 2 seconds to 60 seconds and we've seen that in production where P99 suddenly popped to 60 seconds for no good reason." Router models compound it by hiding which model ran — "they pick which models to run" — so the comparison you recorded may not describe what served the request. The partial mitigations are to fix the reasoning level per route and to pin whatever the router leaves free, making "requests as deterministic as possible with an undeterministic system." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 08:17-09:22)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use hybrid AI pricing to balance predictable revenue and margin protection](use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)

Sources:
- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md), 12:25-14:08, 18:35-19:11
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md), 02:20-03:09
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 08:17-09:22
