# Prompt Caching Sets the Break-Even Bar for Compaction

Summary: Any compaction pass rewrites the context and therefore invalidates the prompt cache, so the compacted tokens are charged at full price while the untouched history would have been charged at the cached rate. The compression ratio has to beat the cache discount — up to 50x on some APIs — before compaction saves money at all, which is why the cheapest configuration in a measured bake-off was the one sending the most tokens.

Use when:
- Deciding whether to summarize, trim, or clear a conversation whose prefix is stable and cacheable.
- Explaining why a token-reduction change made the bill go up rather than down.
- Choosing between cutting the context and engineering the context to be cache-stable.

Details:
- Providers cache the prefill for already-sent tokens; re-used tokens typically save around 90% of cost and "can go up to 50 times cheaper with some API like DeepSeek." They are also already computed, so time-to-first-token drops as well. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 15:55-16:45, 17:37-18:10)
- The break-even argument: summarization, compaction, or any transformation produces a *new* context the provider cannot match against the cache, so "you need to compress by more than 50 times the context" for compaction to be worthwhile — a bar most summarizers cannot clear without losing quality. (16:45-17:37)
- Bouchard's conclusion is deliberately strong: "summarization is potentially a trap. You may not want to use it at all, or you may want to just use it very specifically — which is what the most serious harnesses do nowadays," noting that Claude Code and Codex both pair caching with a *different* compaction method rather than plain summarize-and-reset. (18:10-18:52)
- The measured consequence on DeepSeek V4 Flash: "the setup that was sending the most tokens is actually the cheapest to run," because 97% of its tokens were served from cache. Measured on a 36-turn conversation of roughly 1.78 million tokens. (52:10-53:07)
- Second-order cost, easy to miss: clearing tool outputs to save tokens makes the agent re-retrieve information it already had, so it issues more tool calls — which costs more tokens, more money, and more latency than the outputs you deleted. (45:57-46:41)
- Corollary for design: the lever that survives is cache-stability, not size. Keep the static prefix byte-identical (system prompt, tool definitions), append rather than rewrite, and reserve clearing for a genuine topic change where the cache is going to be lost anyway. (18:55-19:52)
- The bar is not universal. It scales with whatever cache discount your provider actually offers, and it disappears entirely once the conversation no longer fits the window, because there is then nothing to cache — see the local-deployment case. (55:37-56:31)
- Log cache-hit rate per turn alongside cost and time-to-first-token; without it, a compaction change looks like a token reduction and its cache cost is invisible. Their tutor logs input tokens, output tokens, cached count, cost, TTFT, tool-call count, and whether summarization fired. (19:52-20:31, 35:19-35:50)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Inference](../topics/inference.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Shrink the Per-Step Payload the Agent Loop Re-Sends](shrink-the-per-step-payload-the-agent-loop-re-sends.md)
- [Agent swarms create reusable KV-cache working sets](agent-swarms-create-reusable-kv-cache-working-sets.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 15:55-20:31, 35:19-35:50, 45:57-46:41, 52:10-53:07, 55:37-56:31
