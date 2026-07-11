# Train a Small Retrieval Agent With SFT Plus Search-Reward RL

Summary: A retrieval agent can be distilled into a small, fast LLM and then tuned with on-policy RL against a composite search reward — one term scoring the final ranked list (retrieval metrics plus an LLM rubric judge) and one term scoring the search trajectory (query naturalness and the right amount of exploration). Rewarding the trajectory, not only the answer, is how you train the query-writing behavior a strong retriever needs.

Use when:
- Building a purpose-trained search agent instead of relying on a general model's default query behavior.
- Designing rewards for a retrieval/search RL loop where "did it find the right chunks" and "did it search well" are both objectives.
- Trading a large frontier model for a small, cheap, fast agent that still retrieves well.

Details:
- Start small for speed: they "decided to have a very small LLM to make the agent even faster," optimizing tool choice, semantic-query quality, exploration/ranking, and efficiency (10:01-10:37).
- Step 1 — supervised fine-tuning from a larger teacher LLM to bootstrap the search strategy (10:31-10:37).
- Step 2 — on-policy reinforcement learning with a custom search reward = retrieval reward + trajectory reward (10:37-10:54).
- Retrieval reward: the NDCG the agent's final ranked list achieves, plus an LLM judge over rubrics — is the result relevant to the query, are all chunks relevant, is the ranking plausible (10:54-11:31).
- Trajectory reward: an LLM judge that rewards query quality and efficiency, with rubrics for whether the query is a natural sentence and whether the amount of exploration is sufficient (not too much, not too little) — this term is what specifically trains away keyword-salad queries and toward sentence-shaped semantic queries (11:31-11:59).
- Observed trajectory shape: initial search + metadata hints → four parallel semantic searches in round one → a grep in round two, with semantic queries as natural sentences and grep queries as keyword patterns "exactly as intended" (11:59-12:58).
- Results: intermediate NDCG@10 of 0.4 on the OpenCongress-style benchmark vs 0.18 for the paper's best "GPT multi-hop agent"; the in-production beta ("Mixedbread agentic search") is top-1 on Snowflake's DocQA benchmark at 93.4 accuracy when Gemini 2.5 Flash is given it as a search tool, "with way less effort" than comparable search agents (12:58-14:25).
- Complements the coding-agent RFT concepts — [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md) and [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md) — but is retrieval-specific: the reward mixes a hard metric (NDCG) with LLM rubric judges over both the ranked output and the search behavior.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Models](../topics/models.md)

Related concepts:
- [Co-Design Agents to Write Natural-Language Queries for Strong Retrieval](co-design-agents-to-write-natural-language-queries-for-strong-retrieval.md)
- [Retrieval, Not Reasoning, Is the Knowledge-Work Bottleneck](retrieval-not-reasoning-is-the-knowledge-work-bottleneck.md)
- [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)

Sources:
- [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../sources/20260707_1IdzkRVmWAA.md), 10:01-14:25
