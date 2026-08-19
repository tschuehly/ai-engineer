# Local Deployment Inverts the Keep-Everything Context Strategy

Summary: The cloud answer to context management — keep everything and let the cache make it cheap — depends on the conversation fitting in the window. On local hardware it does not: a 32k window forces compression or retrieval, caching stops helping the moment the conversation exceeds the window, and buying a larger parameter count does not buy a larger context window.

Use when:
- Considering a local or on-device model to escape per-token cost at scale.
- Porting a context strategy that was tuned on a frontier API to self-hosted or edge hardware.
- Explaining why a bigger local model did not fix a context problem.

Details:
- The constraint that started it: at 100,000 to 1,000,000 turns per day their cloud bill would be roughly $18,000 to $180,000 per month, so local was evaluated as the cost escape. (Separately quoted: ~$40,000/month on Gemini versus ~$1,900/month on DeepSeek for about 1,000 students.) ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 54:38-55:37, 61:17-61:34)
- On a MacBook the maximum context window they could run was 32k — and their own lessons exceed 32k on their own, so a single retrieved document can fill the window. Once the conversation does not fit, caching is no longer useful, and the context must be made smaller by compressing it or by retrieving only the needed parts. (55:37-56:31)
- The parameter-count trap, stated directly: going from a 7B to an 8B to a 32B model does not increase the context window. "You cannot repair that part; you have to make a choice there." Scaling the model is not a substitute for scaling the window, and on fixed hardware a larger model usually leaves *less* room for KV cache. (56:31-57:22)
- Retrieval is what still works locally. Retrieving from a large pasted document gave about 100% accuracy with 25-65 seconds of processing, whereas stuffing the same content into an overfull window took roughly 340 seconds to produce a *single token* — an order-of-magnitude latency failure, not a graceful degradation. (57:22-58:25)
- Head-to-head on chat: keeping everything scores 92-95% on the cloud setup and 33% locally, with the context window named as the limiting factor. Local has no marginal token cost because you already own the hardware, but it has a throughput ceiling instead — the cost moves from per-token to per-second-of-device. (59:30-60:33)
- The practical consequence is that the compaction techniques the cloud experiment rejected become mandatory locally. Which technique to use is then chosen by the constraint you actually have — window size, not price — which is the general form of their rule: "do not compact by default; name the constraint that you have." (56:31-56:41, 61:34-61:47)
- Their own decision followed from this: they stayed on a cheap cloud model (DeepSeek V4 Flash) with hybrid retrieval, precisely *because* the local hardware could not hold the strategy that measured best. Local remained a cost hedge for larger volumes rather than the shipped answer. (61:48-62:33)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [Dense Retrieval Collapses on Buried Facts as the Haystack Grows](dense-retrieval-collapses-on-buried-facts-as-the-haystack-grows.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Match Gemma edge model size to device memory and interaction class](match-gemma-edge-model-size-to-device-memory-and-interaction-class.md)
- [Treat edge models as their own architecture class](treat-edge-models-as-their-own-architecture-class.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 54:38-60:33, 61:17-62:33
