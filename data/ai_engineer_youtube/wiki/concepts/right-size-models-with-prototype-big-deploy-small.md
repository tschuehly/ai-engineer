# Right-Size Models With Prototype Big, Deploy Small

Summary: Pick the smallest sufficient model by measurement, not by leaderboard or peer advice: prototype the feature on the largest model to prove it is possible, freeze its behavior as a golden dataset of success criteria, then benchmark from the smallest model upward until one clears the bar — the "small and good enough" (SAGE) model.

Use when:
- Deciding whether a frontier cloud call can be replaced by a small or on-device model.
- Turning "should we use the model everyone recommended?" into a measured selection instead of a guess.
- Building a capability eval to compare candidate models on a real product task.

Details:
- The framework (built with Google, documented on web.dev) is "prototype big, deploy small": prototype on a foundation model, then convert parts of the system to SLMs and specialized models for production. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 08:43-09:12)
- Four steps: (1) **prove it's possible** on the largest, most-capable model (a foundation model like Gemini, or a tough task-specific model) — if the big model can do it, a smaller one probably can too; (2) **set success criteria** by collecting input/output pairs into a golden dataset that becomes the bar; (3) **test from small to large**, comparing each candidate's outputs against the criteria and the big-model baseline (a *capability eval*: "what can this agent do well?"); (4) **select the SAGE model** — the smallest model that gives acceptable responses for your inputs. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 09:12-09:46, 18:34-19:24)
- Measuring beats intuition: peers recommended Gemma 4 E2B (5B), but on the summarization task Gemma 4 was slow (~8s) while Llama 3.2 3B won on accuracy (~90%) at low latency and Qwen 2.5 (1.5B) was fastest but least accurate — going with the recommendation would have shipped a worse experience. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 15:07-17:43)
- Success criteria for the case study mixed deterministic and judge-based measures on 14 threads × 2 output shapes (28 examples): JSON validity (`JSON.parse`), reference structural validity, factual consistency (LLM-as-judge), length compliance, and P50/P95 latency, benchmarked in the open-source Phoenix eval tool; run each model multiple times and average. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 11:14-13:34)
- The economic prize is direct: a Claude Sonnet baseline cost ~$0.22 for 14 tasks (~$1/day for the product), while on-device inference cost is "zilch" because it runs on the consumer's device — reframing the audit question as "how many Claude calls could be Llama calls?" ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 13:59-15:02, 28:38-28:55)

- **A second team runs the same pattern on a server-side workload and adds a step between "prove it's possible" and "test small."** LangChain starts with Opus or GPT-5.5 "because we just want to know if the task is even possible," then treats that as a *waterline* and looks "back at those traces" to ask whether an open model can do the same thing. The added step is that the frontier model's traces are read for *how it reasons*, and that reasoning becomes harness guidance for the smaller model — "Opus reasons about things in this way… that might mean I need to give it a little bit more guidance so it can reach the sort of same intelligence level at like a much much lower cost." Where this page freezes outputs as the bar, that step mines the trajectory as the fix ([Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:36-08:58)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Close the small-model gap with prompt variants and harness post-processing](close-the-small-model-gap-with-prompt-variants-and-harness-post-processing.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)
- [Select State of the Art on a Quality-Efficiency Pareto Front](select-state-of-the-art-on-a-quality-efficiency-pareto-front.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Read the Frontier Model's Traces to Harness-Engineer Its Cheap Replacement](read-frontier-traces-to-harness-engineer-a-cheap-replacement.md)

Sources:
- [Frontier results, on device - RL Nabors, Arize](../sources/20260629_fWXJM-J0ZB8.md), 08:43-19:24
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 07:36-08:58
