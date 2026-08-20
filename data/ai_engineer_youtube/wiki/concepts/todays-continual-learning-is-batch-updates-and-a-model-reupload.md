# Today's Continual Learning Is Batch Updates and a Model Re-Upload

Summary: A founder selling continual learning names the current state of the art "pseudo continual learning" — offline batch updates followed by re-uploading the model — and identifies the unsolved piece as merging thousands of concurrent production rollouts into one update. Use it to hold every "learns from every interaction" claim to what is actually running.

Use when:
- Evaluating a vendor claim that a system improves continuously in production.
- Sizing the gap between the continual-learning literature and a deployable loop.
- Deciding whether to build for streaming updates or accept a batch cadence.

Details:
- The admission, in Q&A, in response to a question about learning latency: "as a research community right now we're in this zone of what I call pseudo continual learning, uh where there's some still level of like batch updates offline and then re-uploading the model." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 21:24-21:41)
- The blocker is named as two problems, not one: "I think it's partly an infrastructure question. It's partly still an algorithmic question as well of how do you truly get, when you have 10,000 rollouts going out in a product, merging those together — the infrastructure to pull all of those together." He closes: "I wouldn't say we're anywhere close to the end solution." ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 21:41-21:57)
- **The merge problem is the specific thing to remember**, because it is invisible in every single-trajectory description of these methods. A talk can walk through one rollout, one hint, and one update convincingly, and none of that says how ten thousand simultaneous updates from different users, tasks, and outcomes are reconciled into one set of weights. Whatever fills that gap — batching, averaging, arbitration between conflicting lessons — is unbuilt and unspecified.
- The same talk's vision slide, minutes earlier, is the claim this deflates: "software in general just gets smarter every single time it's used, and that is the most exciting unlock that's going to happen in 2026 2027." The vision is a forecast; the Q&A is the status report. ([Trajectory](../sources/20260812_zL1kLftVTlo.md), 19:59-20:10)
- **This lines up exactly with the trace-policyness axis the wiki already has, and confirms where the field sits on it.** Applied Compute's spectrum runs from a one-time production dump through a daily batch to "this sort of unified engine of putting inference and training together" — which they call "the holy grail" and which is a name for something not yet standard ([Place a Continual-Learning Setup on Two Axes](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)). Two vendors, independently, place the deployed state at the batch rung and the streaming rung in the future tense.
- The honest planning consequence: if the update cadence is batch-and-redeploy, then a continual-learning program inherits the whole release discipline of a model deployment — regression testing, rollback, and a decision about what to do with traffic between updates. It is closer to a retraining pipeline than to a memory system, and the wiki's [prove-each-fix-helps-and-breaks-nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md) requirement applies at each redeploy rather than continuously.
- It also sharpens what the frozen-checkpoint critique is actually about. [Continual learning bolted onto a frozen checkpoint is a sunk-cost choice](continual-learning-bolted-onto-a-frozen-checkpoint-is-a-sunk-cost-choice.md) argues the *training pipeline's* freeze point is inherited rather than chosen; this page says the *deployment* loop still freezes too, between batches. Both freezes would have to go for the streaming picture to be real.
- **Read the source of the admission as strengthening it.** This is the vendor's own characterization of the field he is selling into, offered unprompted in Q&A rather than extracted by a skeptic. That makes it more credible than the talk's forward-looking claims, not less — but it is still one person's read, with no survey behind "as a research community."

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Place a Continual-Learning Setup on Two Axes: Trace Policyness and Hint Provenance](place-a-continual-learning-setup-on-the-trace-and-hint-axes.md)
- [Continual Learning Bolted Onto a Frozen Checkpoint Is a Sunk-Cost Choice](continual-learning-bolted-onto-a-frozen-checkpoint-is-a-sunk-cost-choice.md)
- [Verifiable Continual Learning: Prove Each Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Make Regression-Aware Optimization Part of the Continual Learning Loop](make-regression-aware-optimization-part-of-the-continual-learning-loop.md)
- [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)

Sources:
- [Scaling up Continual Learning — Ronak Malde, Trajectory](../sources/20260812_zL1kLftVTlo.md), 19:59-20:10, 21:24-21:57
