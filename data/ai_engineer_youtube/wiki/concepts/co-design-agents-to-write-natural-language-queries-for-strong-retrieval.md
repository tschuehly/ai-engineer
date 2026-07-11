# Co-Design Agents to Write Natural-Language Queries for Strong Retrieval

Summary: Semantic search "fails" for agents mostly because models were never taught to query it — trained on coding agents (grep/regex) and human web tools, they default to stacking keywords to maximize lexical overlap, which starves a strong neural retriever of the sentence-shaped intent it needs. The fix is to co-design the harness and the retriever together so the agent is steered into natural-language queries and the right tool per intent, rather than swapping in a better retriever and hoping the model uses it well.

Use when:
- A powerful semantic/late-interaction retriever underperforms because the agent feeds it keyword-salad queries.
- Designing an agentic-search harness and choosing how to prompt/route queries across semantic search, filters, and grep.
- Explaining why "just add vector search" doesn't close the retrieval gap on models trained for code and human search.

Details:
- Inspecting agent-emitted queries reveals keyword gibberish — a real example: "senator woman questions billionaires not a company then okay thank you staff will check hearing" — which confuses a retriever built for neural/semantic questions (03:53-04:16).
- Three root causes: (1) models are trained mostly for coding agents optimized for codebase exploration with grep/regex, so they stack expressions they expect in the document; (2) trained to use human-optimized web tools, so they mimic human keyword patterns; (3) benchmark bias — BEIR / NanoBEIR use "caveman-style" entity queries that "structurally favor heavily BM25." Net: the agent "guesses the keywords to increase the overlap" instead of using powerful search (04:16-05:23).
- The harness is the corrective. Four tools give the agent explicit, separable choices: overview search (very wide semantic, up to 50 chunks, summaries only, to survey the corpus without filling context), main semantic search (full payload of top 10 chunks), a metadata-facet filter tool, and grep for exact matches (05:45-06:40).
- The loop is short for speed but deep for exploration: max four search rounds with parallel searches per round; it starts from an initial semantic-search preview plus metadata-facet hints, splits intent into ≤4 aspect queries each routed to the best tool, deduplicates chunks across tools to protect context, and submits a final ranking when it has enough evidence (06:41-08:25).
- Five levers that produce good queries (08:25-10:01): goal framing (state needed evidence before writing the query); tool separation (semantic only when it needs aspects, grep only for exact matches); a prompt-framing trick — instruct it to "write one concise sentence describing what it wants to find" instead of "write a search query," so "it cannot fall into this old [BM25] pattern"; few-shot examples of good queries plus how to decompose an input into aspects; and showing the original query's semantic-search results so it learns the corpus's language and where to dig deeper.
- Distinct from [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md) (which is about the model deciding *which* searches to run) and [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md) (which tool fits a query): this concept is about the model's learned *query-writing bias* and the harness/training design that fixes it.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Retrieval, Not Reasoning, Is the Knowledge-Work Bottleneck](retrieval-not-reasoning-is-the-knowledge-work-bottleneck.md)
- [Train a Small Retrieval Agent With SFT Plus Search-Reward RL](train-a-small-retrieval-agent-with-sft-and-search-reward-rl.md)
- [Agentic Retrieval Lets Models Plan Search Steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Choose Lexical, Vector, and Reranking Retrieval by Query Shape](choose-lexical-vector-and-reranking-retrieval-by-query-shape.md)

Sources:
- [How we taught agents to use good retrieval - Hanna Lichtenberg, Mixedbread AI](../sources/20260707_1IdzkRVmWAA.md), 03:53-10:01
