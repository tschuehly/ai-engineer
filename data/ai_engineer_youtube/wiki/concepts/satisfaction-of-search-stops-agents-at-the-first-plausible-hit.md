# Satisfaction of Search Stops Agents at the First Plausible Hit

Summary: Radiology has a name for finding one abnormality on a scan, stopping, and missing the others: satisfaction of search. Agents given a searchable knowledge base do the same thing — they find something that looks like the answer and quit — which is why attaching a wiki improves access without improving outcomes. The defect is in the stopping rule, not in the index, so better embeddings and bigger corpora do not touch it.

Use when:
- A team is about to "solve context" by pointing an agent at Confluence, Notion, a wiki, or a docs MCP server.
- Retrieval evaluation shows good recall but agents still act on incomplete understanding.
- Diagnosing an agent that produced a defensible-looking plan built on one true fact and three missing ones.
- Deciding whether a retrieval problem is a ranking problem or a search-termination problem.

Details:
- The diagnosis, borrowed intact: on an X-ray "you discover like one indicator, and if you stop there you might miss other important indicators that might lead to diagnosis of even more issues. So this is what happens with agents. They find something that they think is correct and then they stop." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12)
- What it says about the wiki fix: "If you attach a wiki, it still doesn't tell the agent where the information is that it needs. It can search for things in the wiki, but then…" — the searchable store answers *where can I look* and never answers *have I looked enough*. Access is granted; sufficiency is not. (04:16-04:37)
- The one-line form worth carrying: "access to information doesn't equal understanding." (04:09-04:16)
- Why this is a distinct failure class. Ranking failures are visible to a retrieval metric — the right document was not in the top k. A stopping failure retrieves a *correct* document and then declines to keep going, so recall@k on the retrieved set can look fine while the agent's working set is missing the two other documents that would have changed the plan. An eval that scores what was returned cannot see it; an eval that scores the trajectory against the set of documents the agent *should* have read can. See [Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md).
- Why capability improvements do not fix it. The agent is not failing to understand the retrieved text; it is failing to estimate its own coverage of an unseen corpus, which is unobservable from inside the search loop. The same property makes the failure quiet: nothing errors, nothing is empty, and the answer is built from real evidence.
- Mitigations that follow from the mechanism rather than from the tooling: hand back multiple sources with the answer so the next hop is already known rather than requiring a new search ([Attach Sources as Both a Correction Surface and a Continuation Pointer](attach-sources-as-a-correction-surface-and-a-continuation-pointer.md)); precompute the cross-document synthesis so the agent is not the thing responsible for assembling it ([Distillation Is a Separate Step From Retrieval](distillation-is-a-separate-step-from-retrieval.md)); and route to the known location instead of searching for it when the location is known ([Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)).
- The rejected alternative, with two reasons and not one. Loading the whole corpus so no stopping decision is needed fails because "you've got way more organizational context than can fit into a context window, even one that's a million tokens in size" *and* because "it causes the agent to get distracted. When you're working on a task, you want task-specific flow." Removing the stopping decision by removing search reintroduces the selection problem inside the window. (05:34-06:20)
- Boundary: the term is borrowed from radiology by analogy, and the talk offers no measurement of how often agents stop early or of how much a context engine reduces it. Treat it as a named hypothesis that tells you what to instrument, not as a quantified effect.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Distillation Is a Separate Step From Retrieval, and the Task Agent Will Not Do It](distillation-is-a-separate-step-from-retrieval.md)
- [Attach Sources as Both a Correction Surface and a Continuation Pointer](attach-sources-as-a-correction-surface-and-a-continuation-pointer.md)
- [Evaluate Agent Retrieval by Trajectory, Not Task Success](evaluate-agent-retrieval-by-trajectory-not-task-success.md)
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [Agentic retrieval lets models plan search steps](agentic-retrieval-lets-models-plan-search-steps.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:09-06:20
