# Close the Small-Model Gap With Prompt Variants and Harness Post-Processing

Summary: When a small model lands close to but below a frontier baseline, close the remaining gap without changing models — test prompt variants one variable at a time to find what actually moves the metric, and move deterministic checks (structure, length) out of the prompt into harness post-processing.

Use when:
- A right-sized small/local model passes most criteria but trails the baseline on a few (accuracy, length, structure).
- You can't swap the model — a shipped on-device model, a team committed to a fixed version, or a mobile app where re-downloading a distilled model eats the user's data plan.
- Deciding which failures to fix with prompting versus with code around the model.

Details:
- Isolate one variable per prompt variant so you can tell whether a change actually moves the needle. The case study ran five prompts (a strong baseline plus four hypotheses) against the same small model. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 21:15-21:33)
- The four hypotheses and outcomes on Llama 3.2 3B: numbered-message input instead of JSON (bet: small models track natural-language indexing better than array offsets) — ~no change; few-shot examples (bet: small models learn format from examples faster than rules) — **best result**, better length and accuracy, closer to the baseline, only ~200ms added; strict-rules / "house of no" negative constraints (bet: small models like literal commands) — **made things worse**, the model "responded very negatively to being told what it couldn't do"; chain-of-thought (bet: thinking out loud improves grounding) — slightly better length but ~600ms slower. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 21:33-24:36)
- Small models don't share large-model prompt intuitions: negative/strict framing backfired while few-shot examples helped most, so prompt techniques must be re-measured per small model rather than transferred from frontier practice. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 23:12-24:36)
- Push deterministic requirements out of the model and into the harness: reference-count validity (compare the number of references against thread length) and length compliance (truncate over-long summaries) are cheap post-processing checks, and adding them closed the case study's gap to 100% JSON and structural validity while beating the frontier baseline on latency. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 26:31-27:45)
- Prompt engineering is the lever precisely when you can't control which model runs; a distilled model retrained per capability would ship a new 1–2GB download each time, so prompting a general small model is often the better mobile tradeoff. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 19:24-20:28)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Right-size models with prototype-big, deploy-small](right-size-models-with-prototype-big-deploy-small.md)
- [LLM judges show self-preference and family bias](llm-judges-show-self-preference-and-family-bias.md)
- [Invest in the harness to run weaker and local models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Constrained decoding makes small-model tool calls production-usable](constrained-decoding-makes-small-model-tool-calls-production-usable.md)

Sources:
- [Frontier results, on device - RL Nabors, Arize](../sources/20260629_fWXJM-J0ZB8.md), 19:24-27:45
