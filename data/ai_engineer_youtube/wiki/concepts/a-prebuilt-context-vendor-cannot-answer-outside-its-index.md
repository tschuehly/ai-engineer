# A Prebuilt Context Vendor Cannot Answer Outside Its Index

Summary: A vendor that serves prebuilt structured context has a hard coverage ceiling that a search-based path does not: it can only answer from what it already collected, and a question outside that set has no answer at any price. This produces the counterintuitive result that dedicated context vendors can score *lower* on coverage than general search — and it makes "coverage" a field-set-dependent metric rather than a property of the vendor.

Use when:
- Comparing a prebuilt data/context vendor against a live-search path for an enrichment or research task.
- A specialist vendor underperforms a generalist on your benchmark and the result looks like a defect.
- Designing a coverage metric for retrieval vendors and choosing which fields to score.
- Deciding whether to accept a vendor's fixed schema or keep a search fallback for fields outside it.

Details:
- The setup: enrich one company across 25 fields — easy ones like domain, name, and headquarters, harder ones "about hiring and people" — with a loop-in-a-loop agent and budget guardrails, run 100 times against the event's sponsors, comparing AI-search products, context-as-a-service vendors, plain Google through a SERP API, and the model's native search. Coverage converged: "there's pretty good convergence. They all did fairly well." (10:10-11:15)
- The surprise: "I was originally surprised about the two CaaS solutions at the bottom. It was counterintuitive. I expected CaaS to dominate this thing… you had one job, right? To map all these companies." (11:32-11:43)
- The mechanism is structural, not a quality gap: "they are limited in the sense that they know what they have about an entity. If I ask you the question that is beyond that, they will never have that data. Not like a search engine can go out and continue searching and exploring it. If they didn't collect data about the recent job hiring, it will never be there." (11:49-12:06)
- The metric qualifies itself, and the speaker says so before anyone else can: "I'm sure at the same time that they have a lot of other advantages that we simply didn't ask for. A lot of other fields that they didn't have that aren't represented. So… it creates some complexities when… how do we measure coverage when it relates to the specific job that we need to do rather than in general." (12:06-12:25)
- Two decision rules fall out. First, the comparison is only meaningful against *your* field set: a vendor's coverage score is a joint property of the vendor and the schema you chose to ask about, so a leaderboard built on someone else's fields transfers poorly. Second, the ceiling is a routing signal — if any part of your workload asks questions outside a fixed schema, the prebuilt path needs a search fallback rather than a better vendor.
- The same test found cost converged across search and context vendors, but from different components — vendor invoice alone for the prebuilt path, versus vendor plus token burn to structure results for the search paths — so the ceiling is not paid for with a cost advantage. (12:32-12:57)
- This is the supply-side counterpart to the freshness failure the wiki records elsewhere: a stale index serves a confidently wrong answer, while a *bounded* index serves no answer at all. The second failure is the more honest one, but only if the agent surfaces the miss rather than filling it.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Context as a Service Is Vertical Search for Agents](context-as-a-service-is-vertical-search-for-agents.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [Dynamic AI Search Evals Need Fresh Grounding Sets](dynamic-ai-search-evals-need-fresh-grounding-sets.md)
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Agents Punish Bad Data and Need Question and Tracking Data Foundations](agents-punish-bad-data-and-need-question-and-tracking-data-foundations.md)
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)

Sources:
- [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](../sources/20260814_Ot4OPrPH4xY.md), 10:10-12:57
