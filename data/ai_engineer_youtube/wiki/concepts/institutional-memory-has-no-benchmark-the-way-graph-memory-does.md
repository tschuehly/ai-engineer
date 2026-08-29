# Institutional Memory Has No Benchmark the Way Graph Memory Does

Summary: Agent memory as a retrieval problem is a well-populated research area with datasets and a settled metric. Institutional or tribal memory — what an organization knows that nobody wrote down — has neither a definition nor a measure, so systems built on it are currently evaluated by anecdote. Knowing which side of that line your component sits on tells you whether you can borrow a benchmark or have to build one.

Use when:
- Planning evaluation for a system whose value claim is "it captures what the team knows."
- Deciding whether an off-the-shelf memory benchmark actually covers the capability you are shipping.
- Justifying the cost of collecting a domain dataset with subject matter experts instead of reusing a public one.

Details:
- **The asymmetry, stated as the hard frontier of the work.** "The topic of memory or graph memory or graph RAG, whatever the title is… there is around 150 papers in this area at the moment and all of them are addressing [it] in a nice way. You can measure the recall, there is datasets. But there is no work and research at the moment that targets tribal memory or institutional memory. Like what does it mean exactly? How do you measure tribal memory success?" ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 11:59-12:26)
- The two open questions are ordered, and the order matters: the definition problem precedes the measurement problem. Recall works as a metric for graph memory because the target is a retrievable item that exists somewhere. Institutional memory's characteristic content — why a decision was made, which convention is real, what a previous project learned the hard way — often has no stored referent to recall, so there is nothing to compute recall against.
- **A second, compounding gap in specialized domains.** "For the chip design domain, it's actually even harder because there is not enough datasets like [the] computer vision domain, there is many datasets over there. So there is nothing collected. So we have our own [approach], going with SMEs collecting this kind of datasets." Two separate shortages stack: no metric for the capability, and no data for the domain. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 12:26-12:49)
- **Consequence for anyone shipping this class of system.** The organizational-knowledge layer will be the least-evidenced part of your product, and the temptation is to report the component you *can* measure (retrieval recall) as if it evidenced the one you cannot (does the system actually hold what the team knows). The wiki's memory-wiped-rerun method is the nearest available substitute — measure the gain over the same task run without the memory layer — because it needs no dataset and no definition of what was remembered, only a task with an outcome.
- **The absence claim is an assertion, not a survey.** The "around 150 papers" figure carries no citation or search method, and no literature search on the institutional-memory side is described. Read the page as a well-motivated gap statement from a practitioner, not as an established negative result. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 11:59-12:26)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)
- [Enterprise Agent Failures Expose Missing Institutional Knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Knowledge Graphs Make Agent Memory Traversable And Explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Treat Memory as a Write–Manage–Read Control Loop, Not a Store](treat-memory-as-a-write-manage-read-control-loop.md)
- [Grade the Alignment, Not the Agents](grade-the-alignment-not-the-agents.md)
- [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md)

Sources:
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 11:59-12:49
