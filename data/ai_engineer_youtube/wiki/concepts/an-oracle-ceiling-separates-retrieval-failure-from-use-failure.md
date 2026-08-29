# An Oracle Ceiling Separates Retrieval Failure From Use Failure

Summary: Add a condition to your memory eval that hands the model the correct memory for free. Whatever it still gets wrong is not a retrieval defect — the model received the right context and ignored it, misread it, or was confused by it. That gap partitions your error budget between the recall policy and the model's use of what recall delivers, and it is the cheapest instrument that tells you which half to work on.

Use when:
- A retrieval or memory system is being tuned and you do not know how much headroom retrieval even has.
- Deciding between better recall and better prompting/model choice for a context-dependent failure.
- Reviewing a claim that "the agent failed because it didn't have the information."

Details:
- The observation that motivates the instrument: the oracle condition did not reach the maximum score. "The Oracle, what it does, it provides the right information, the right memory to the model, but it doesn't force it to use it. So the model can get the right memory but still retrieve the wrong information or choose to ignore it or be confused. So that's why the Oracle in this case doesn't hit the max performance." ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 08:35-08:59)
- The three named use failures are distinct and have different fixes: **retrieving the wrong information** from a correct memory (a reading/attention problem), **choosing to ignore it** (an instruction/incentive problem), and **being confused by it** (a formatting or conflict problem). None is repaired by a better retriever.
- The oracle is defined per loop, not per task: "telling the harness for every loop what the correct memory that needs to be retrieved is." That granularity is what makes it a ceiling rather than a hint — the model never has to search. (05:00-05:18)
- What the ceiling buys in planning terms. Score(oracle) − Score(your policy) is the recoverable retrieval headroom. Max − Score(oracle) is not recoverable by retrieval at all. Skipping the oracle rung means both numbers are invisible and every failure looks like a retrieval failure.
- Read together with the wiki's stronger version of the same lesson on a different layer: providing the right context does not compel use, which is why an oracle is a *ceiling* and not a *solution*. A memory system whose ambition is "retrieve perfectly" is capped below 100% by the model's use of what it retrieves.
- Cost note: the oracle requires labelled ground truth per step, which is why it belongs in an offline eval and not in production. In this study it was affordable because the benchmark (xbench) already carried the step at which each answer appeared. (06:56-07:33)
- Caveats: the gap between oracle and maximum is stated qualitatively — no figure is given for either — so the *existence* of use failure is the evidence here, not its size. Models were local and quantized, a class more prone to ignoring supplied context than frontier models may be.

- **A third failure the two-way partition does not separate: the agent stopped searching.** The oracle split assumes retrieval either returned the right item or did not. Agentic search adds a case where retrieval returned *a* right item and the loop then terminated before finding the others — satisfaction of search, borrowed from radiology. That failure sits on the retrieval side of the partition but is invisible to a recall metric over what was returned, because everything returned was correct. Handing the oracle the full required set, rather than one correct item, is what makes the ceiling meaningful for a multi-hop task. See [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md)
- [Rank a Decisions Ledger Instead of Retrieving Memories by Similarity](rank-a-decisions-ledger-instead-of-retrieving-memories-by-similarity.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Surface Unresolved Context Conflicts to Agents and Users](surface-unresolved-context-conflicts-to-agents-and-users.md)
- [Bad Recall Costs More Than No Recall](bad-recall-costs-more-than-no-recall.md)
- [Satisfaction of Search Stops Agents at the First Plausible Hit](satisfaction-of-search-stops-agents-at-the-first-plausible-hit.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 05:00-05:18, 06:56-07:33, 08:35-08:59
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 04:37-05:12
