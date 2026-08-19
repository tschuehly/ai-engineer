# Full History Recalls Details That Summaries Delete

Summary: A summary is a lossy commitment made before you know which detail will be asked for. Measured on real support-style chats, keeping the whole history returned the exact requested detail 95% of the time against 32% after summarizing or compacting — and distinctive facts stayed recoverable out to 800k tokens with no visible rot, while ambiguous facts degraded to about half that.

Use when:
- Choosing between a rolling summary and an untouched transcript for a multi-turn assistant.
- Estimating how far a conversation can grow before long-context recall actually breaks.
- Arguing about whether "context rot" applies to your workload or only to some workloads.

Details:
- The probe: real student conversations containing setup details, errors seen, and what had already been tried, then questions asking for those specific details back. Keeping everything returned the exact detail 95% of the time; summarizing or compacting first returned it 32% of the time. ([Context Engineering in 2026](../sources/20260817_WP3hjUXd918.md), 50:53-51:56, 60:33-60:45)
- The stated mechanism is not subtle: "when you summarize you remove all of the necessary details" — the summarizer cannot know which detail the next probe will need, so it discards on a general-purpose criterion and the specific one goes with it. (51:41-51:56)
- Long-context durability, measured rather than assumed: distinctive facts were recovered consistently up to 800k tokens with no observed context rot. Ambiguous facts — ones with no distinguishing surface form — dropped to about half that performance. Fact *distinctiveness*, not context length alone, is what predicted the failure. (53:16-54:33, 60:45-61:03)
- This qualifies the general "long context is not memory" position rather than refuting it. Within one session, on this model class, at these lengths, the window was the *better* memory: the failure the wiki catalogs elsewhere (attention dropping the middle, degraded reasoning over large spans) did not show up for single-fact retrieval of distinctive facts, but did show up for ambiguous ones and does show up for retrieval over a large haystack. (53:16-54:33)
- The result reproduced across model tiers: full history won the multi-turn recall comparison on Gemini 3.5 Flash and again on DeepSeek V4 Flash, so it is not an artifact of one provider's long-context training. (43:40-44:42, 49:12-50:30)
- Caveats the presenters state themselves: the multi-turn dataset was 11-13 turns ("not huge"), the long-context probe pulled *one specific detail* at a time rather than requiring synthesis across the transcript, and the trial count was one to two. (46:41-46:58, 53:16-54:00)
- The conclusion they shipped is a hybrid, not an absolute: keep everything, with a default compaction threshold at 30k tokens as the backstop. The point is that the threshold is where compaction starts, not where the session starts. (61:48-62:33)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Prompt Caching Sets the Break-Even Bar for Compaction](prompt-caching-sets-the-break-even-bar-for-compaction.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Curate Context Strategically Because Models Drop the Middle](curate-context-strategically-because-models-drop-the-middle.md)
- [Dense Retrieval Collapses on Buried Facts as the Haystack Grows](dense-retrieval-collapses-on-buried-facts-as-the-haystack-grows.md)

Sources:
- [Context Engineering in 2026 — Louis-François Bouchard, Omar Solano & Samridhi Vaid, Towards AI](../sources/20260817_WP3hjUXd918.md), 43:40-44:42, 49:12-51:56, 53:16-54:33, 60:33-61:03, 61:48-62:33
