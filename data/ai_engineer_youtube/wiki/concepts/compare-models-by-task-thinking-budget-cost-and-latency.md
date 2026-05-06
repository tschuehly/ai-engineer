# Compare Models by Task, Thinking Budget, Cost, and Latency

Summary: Model choice should be treated as a task-level routing decision across capability, thinking depth, speed, and cost rather than a reflexive choice of the largest model.

Use when:
- Selecting between model tiers for a prototype, production feature, or multimodal workflow.
- Tuning reasoning depth for an interactive task where latency and cost compete with answer quality.

Details:
- AI Studio exposes thinking levels from minimal to high; Bailey keeps thinking low or minimal during time-sensitive demos and turns it up only when extra reasoning tokens are worth the latency or spend.
- Bailey frames Gemini 3.1 Pro as the largest, slower, and more expensive model, Gemini 3 Flash as a production workhorse, and Gemini 3.1 Flash-Lite as a lower-cost, fast option gaining adoption from older Flash users.
- Compare mode lets engineers test model variants side by side under similar tool settings, including code execution, which makes routing decisions more empirical.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use hybrid AI pricing to balance predictable revenue and margin protection](use-hybrid-ai-pricing-to-balance-predictable-revenue-and-margin-protection.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)

Sources:
- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md), 12:25-14:08, 18:35-19:11
