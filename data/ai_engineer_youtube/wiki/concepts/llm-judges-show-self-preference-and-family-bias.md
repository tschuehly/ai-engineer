# LLM Judges Show Self-Preference and Family Bias

Summary: An LLM-as-judge tends to favor outputs from its own model or model family and grade an outsider model more strictly, so an apparent quality gap can be judge bias rather than a real model failure — which you only catch by opening the eval and reading the raw responses.

Use when:
- Using one model to judge outputs from a different model or model family (e.g. Claude judging Claude vs Llama).
- A candidate model trails the baseline on a subjective, judge-scored metric (factual consistency, helpfulness, tone) but not on deterministic ones.
- Deciding whether a factual-consistency or quality gap is worth engineering effort.

Details:
- In the case study, Claude Opus judged Claude Sonnet's summary against Llama 3.2's, and the factual-consistency gap turned out to be Claude "favoring its little sister" and being a very strict judge of the outsider — nitpicking word choices like "angsty" vs "cross" rather than flagging a real error. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 25:39-26:31)
- The remedy is to crack the eval open and inspect raw vs expected responses side by side; in many cases Llama's output was "pretty much indistinguishable" from Claude's despite the lower judge score, so the score alone would have overstated the gap. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 17:43-18:11, 26:31-27:01)
- Practical implication for right-sizing: don't spend prompt-engineering or model-swap effort chasing a judge-inflated gap — separate deterministic criteria (which post-processing can guarantee) from judge-scored criteria (which may carry self-preference bias) before deciding what actually needs fixing. ([Frontier results, on device](../sources/20260629_fWXJM-J0ZB8.md), 27:01-27:45)
- This is a concrete instance of the broader warning that LLM judges are imperfect substitutes for humans and carry biases (conciseness, helpfulness, ordering), extended to cross-family self-preference specifically: the judge's own lineage is a confound when it rates competing models.

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Right-size models with prototype-big, deploy-small](right-size-models-with-prototype-big-deploy-small.md)
- [Close the small-model gap with prompt variants and harness post-processing](close-the-small-model-gap-with-prompt-variants-and-harness-post-processing.md)
- [Use golden data sets and mixed scoring functions for AI application confidence](use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md)

Sources:
- [Frontier results, on device - RL Nabors, Arize](../sources/20260629_fWXJM-J0ZB8.md), 17:43-27:45
