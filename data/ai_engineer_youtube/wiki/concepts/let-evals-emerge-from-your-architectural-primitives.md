# Let Evals Emerge From Your Architectural Primitives

Summary: Evals bolted onto a finished system inherit its blind spots — non-reproducible runs, an offline set that never matched production, and sensitive data you are not allowed to move. Three storage and platform choices made for other reasons (an immutable event log, human–agent equivalency, and data in object storage) turn out to supply replay, labels, and privacy-preserving execution as byproducts, so evaluation becomes a first-class property of the system rather than an attachment.

Use when:
- Planning an eval strategy for a regulated deployment where production data cannot leave the customer's environment.
- Your offline eval set is drifting, unrepresentative, or expensive to label, and you are considering yet another sampling job.
- Deciding what to build first in an enterprise AI system, and weighing whether evaluation infrastructure is a separate workstream.

Details:
- **The three failure modes being designed around.** LLMs "are not deterministic, so it can be quite tricky to pin down the precise change that led to some sort of change in outputs"; the offline set "might not necessarily represent production data … maybe you sampled from data, but actually that sample isn't truly representative"; and "you also have drift of data over time, so maybe your offline data set is now out of date." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 14:46-15:32)
- **The claim.** These three primitives "actually give you effective privacy preserving evals almost as a byproduct without needing to kind of bolt something onto the side of your architecture." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 15:36-15:51)
- **Ledger → exact counterfactuals.** Because the [append-only event log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md) is the source of truth, "you can replay your actions. So you can go back to any particular time … you can see the complete state of the system at that point in time. And if you wanted to, you could then make very specific tweaks. So you could tweak a prompt, you could tweak a model, you could tweak the code, and you can see the exact direct impact of that because you have all of that context." This attacks the non-determinism problem by holding everything except the one change fixed. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 15:52-16:15)
- **Equivalency → labels.** Because [humans and models are the same kind of agent](treat-humans-and-models-as-the-same-kind-of-agent.md), "for any task, you could get both the agent, the LLM agent, and the human to perform it, and your difference is your eval, that gives you the eval scores." The labelling function is the escalation path already in production, so ground truth accrues from ordinary operation rather than a separate annotation project. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 16:16-16:29)
- **Object storage → evals on production data you never see.** Because payloads live in [object storage beside the log](store-agent-data-in-object-storage-beside-the-event-log.md), you can "run these evals on production data including inside your customer's environment without actually ever exposing that data. You can get your eval results without the sensitive data ever needing to come to where your agent is performing the work." This is what dissolves the representativeness and drift problems: the eval set *is* production. ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 16:30-16:46)
- **The stance, stated as a summary of all four principles:** "the immutable ledger of actions, the orchestration adjacent object storage, the human agent equivalency, and the way that with these three principles evals can emerge as a first-class property of the system rather than as something you attach onto the side." ([Lovejoy & Howard](../sources/20260819_mav15aW9lLM.md), 16:48-17:15)
- **Read against the wiki's other route to the same goal.** [Replay as a debugging and regression mechanism](turn-recorded-agent-traces-into-free-replay-test-cases.md) reaches counterfactual testing by instrumenting node boundaries specifically for that purpose; here the same capability arrives because the compliance requirement already forced a complete ledger. Where a team has no regulatory forcing function, deliberate instrumentation is the path; where it has one, paying twice is the mistake.
- **Boundary worth noting.** Human–agent difference gives you a score wherever a human actually performed the task, which is the escalated and sampled subset, not the whole traffic stream. Continuous coverage of everything still needs a scoring layer of the kind in [score every production conversation to judge agent health](score-every-production-conversation-to-judge-agent-health.md); this concept lowers the cost of the ground-truth half, not the coverage half.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)
- [Store Agent Data in Object Storage Beside the Event Log, Not Inside It](store-agent-data-in-object-storage-beside-the-event-log.md)
- [Treat Humans and Models as the Same Kind of Agent](treat-humans-and-models-as-the-same-kind-of-agent.md)
- [Turn Recorded Agent Traces Into Free Replay Test Cases](turn-recorded-agent-traces-into-free-replay-test-cases.md)
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)

Sources:
- [Why Your Enterprise Tech Stack Isn't Ready for AI Agents — Christopher Lovejoy & Saul Howard](../sources/20260819_mav15aW9lLM.md), 14:46-17:15
