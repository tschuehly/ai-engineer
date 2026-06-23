# Embed LLM-Generated Queries, Not Raw Heterogeneous Signals

Summary: Off-the-shelf embedding models cluster mixed-format data by structural similarity, so raw signals of the same shape group together regardless of meaning. To cluster by meaning instead, ask an LLM what each signal is about, generate a short query or description, and embed that.

Use when:
- Clustering or deduplicating data that arrives in several different formats (errors, logs, chat messages, charts, replays) but may describe the same underlying problem.
- Naive embedding-based grouping keeps putting like-with-like by structure (errors next to errors, messages next to messages) and never links cross-format items.

Details:
- PostHog first embedded signals directly and clustered them to find related issues, but it "works really badly": an off-the-shelf model notices structural similarity, so all errors land in one region of embedding space, all Slack messages in another, and all session replays in another, and none get grouped to each other even when they describe the same product problem (05:53-06:40).
- The concrete example: a checkout error, an onboarding error, and a Slack message about onboarding — the model groups the two errors by format rather than linking the onboarding error to the onboarding message by meaning (06:11-06:40).
- The fix is to not match the signals themselves in embedding space: ask an LLM "what is this signal about?", have it generate a few queries, and match those queries in embedding space instead; this "worked much much better" (06:40-07:14).
- The generalized lesson: embedding models match on structural, not just semantic, similarity, so when your clustering data is not all the same format, think carefully about what the data looks like and how to normalize it before embedding (11:43-12:04).
- This is an indexing-side counterpart to writing better queries: the LLM-generated description is a meaning-bearing surrogate that the embedding model can compare across formats, rather than the format-bearing raw artifact.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Observability-to-PR Agents Turn Incidents Into Reviewable Fixes](observability-to-pr-agents-turn-incidents-into-reviewable-fixes.md)
- [Align Synthetic Retrieval Queries With Real User Specificity](align-synthetic-retrieval-queries-with-real-user-specificity.md)
- [Search Engines Shift Retrieval Work to Ingestion](search-engines-shift-retrieval-work-to-ingestion.md)
- [Cluster conversation outputs to prioritize AI product work](cluster-conversation-outputs-to-prioritize-ai-product-work.md)

Sources:
- [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](../sources/20260610_zMiSRliEzv4.md), 05:53-07:14, 11:43-12:04
