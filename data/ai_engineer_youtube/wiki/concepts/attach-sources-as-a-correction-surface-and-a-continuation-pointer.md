# Attach Sources as Both a Correction Surface and a Continuation Pointer

Summary: Citations returned with an answer do two different jobs for two different consumers. For the human they are a correction surface — a wrong answer becomes a fixable knowledge-base entry instead of an unexplained miss. For the agent they are a continuation pointer — the next hop is already named, so elaborating does not require starting a new search. Systems that treat citations only as an audit trail get the first job and miss the second.

Use when:
- Designing the response format of a retrieval or context service that both people and agents will call.
- An agent's answers are shallow and every follow-up triggers a fresh search from scratch.
- Building trust in an internal knowledge system whose answers are sometimes wrong.
- Deciding whether "show sources" is a UI nicety or part of the contract.

Details:
- The human job, and why it is more than trust theatre: "what's really important is that you show your work. This is a trust-building thing more than anything, but it allows people to see if the answer is maybe not entirely correct, then you can look into the knowledge base that you have and make corrections. Increasingly agents are doing this for you." ([Werry](../sources/20260827_qdAkxLoYNI8.md), 08:33-08:52)
- The agent job, which is the less obvious half: with the context engine in the loop, the plan cited PRs, Slack conversations, Notion pages, and architecture documents — and "all of these things here, the sources come back to Claude, and then Claude knows exactly where to jump to next if it needs to elaborate on that context." (10:35-11:13)
- Why that matters operationally. An answer without pointers ends the trail; the agent that needs more must re-enter search and re-run the stopping decision that already failed once. A cited answer converts the next step from a retrieval problem into a fetch, which is the same move as [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md) — except the known source is supplied by the previous answer rather than by a human.
- This is the direct mitigation for [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md): returning several sources rather than one, with the answer, moves the coverage decision out of the agent's search loop and into the responding system, which can see the whole corpus.
- Design consequences that fall out of serving both consumers: return sources as resolvable addresses rather than titles, return more than one, keep them attached to the specific claim rather than pooled at the bottom, and do not collapse them when the caller is an agent — the machine consumer is the one that can actually act on them.
- The correction loop needs somewhere for the correction to land. Citations make an error diagnosable; they only make it *fixable* if the knowledge base is writable and the fix is durable. Without that, showing sources converts a silent wrong answer into a visible wrong answer that recurs.
- Relation to the existing evidence-surface pattern in this wiki: showing retrieved chunks inside the work UI was framed as operator inspection and retrieval debugging. This source adds the machine-facing purpose and the write-back purpose. See [Show Retrieved Chunks Inside Agent Workflows](show-retrieved-chunks-inside-agent-workflows.md).
- Limit: a vendor demo, with no measurement of whether cited answers were corrected more often or whether the agent's follow-ups actually used the pointers.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)
- [Show Retrieved Chunks Inside Agent Workflows](show-retrieved-chunks-inside-agent-workflows.md)
- [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Distillation Is a Separate Step From Retrieval, and the Task Agent Will Not Do It](distillation-is-a-separate-step-from-retrieval.md)

Sources:
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 08:33-08:52, 10:35-11:13
