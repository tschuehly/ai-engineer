# Classify Continual-Learning Failures as Stability or Plasticity

Summary: Nearly every way a learning system fails lands on one of two sides: it lost information it should have kept (stability), or it refused to update on information it should have used (plasticity). Sorting an observed failure into the right side is worth doing first, because the two have opposite fixes and a change that repairs one usually worsens the other.

Use when:
- Triaging a memory, notes, or profile system that behaves badly across sessions.
- Deciding whether to make a memory layer more retentive or more responsive, and needing evidence for which.
- Reading agent traces for a diagnosis rather than a score.

Details:
- The claim: "most failure modes in continual learning fall on one side of the stability plasticity trade-off… stability is your ability to retain new information in a stable way and use that for future tasks. While plasticity is your ability to actually learn from new information. We see usually that with most continual learning methods, any sort of failure mode comes from the inability to do one of these things." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 14:56-15:27)
- **Worked stability failure — a forecast that discards its own correction.** On a five-year sales-prediction task, the model "starts by getting feedback that it overpredicted," so it "revises its prediction downwards." It then "gets feedback that actually its underprediction was too much of an underprediction. And so as a human might naturally do you would go for the middle. But that's not what the model does. The model kind of forgot that it had the over prediction to begin with at the start and it just re jumps back right to the over prediction." (15:20-16:12)
- The transferable signature in that trace: **the system responds correctly to the most recent feedback and behaves as if earlier feedback never happened.** It oscillates between extremes instead of converging. A system that had retained both corrections would interpolate; one that retains only the last one ping-pongs. Oscillation between two poles across a feedback sequence is the cheapest stability-failure tell there is, and it is visible without any ground truth.
- **Worked plasticity failure — a notepad that rules out a relevant memory.** In an epidemiology task, a context-management system with a notepad wrote: "These seem to be cohort definitions from a different study schema that doesn't apply here." But "the study schema did in fact apply here… It just didn't even recognize that this is something that's relevant to the task and use that to update its priors." (16:12-16:45)
- The signature there is different and more insidious: the system **states a confident, articulate reason for not updating**. The failure is inside a coherent justification rather than inside an obvious error, so it survives casual trace review and any judge that scores reasoning quality rather than the conclusion. Look specifically for dismissal language — "doesn't apply here," "from a different context," "not relevant to this task" — and check the dismissals rather than the actions.
- **The plasticity example is a measured instance of a failure this wiki already argues against on other grounds.** Sakana's ablation found that gating memory on the model's own judgment of whether it needs memory lost to always running a ranked recall ([Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md)). Here the same judgment is exercised on the read side — the memory is present, and the model decides it does not apply — with the same outcome. Two studies, two mechanisms, one conclusion: the model's assessment of its own memory's relevance is not a signal to build on.
- Why sorting matters before fixing: the two failures pull opposite ways. More retention, larger context, longer-lived notes address stability and make plasticity failures more likely by giving the model more prior material to defend. Faster overwriting, recency weighting, and aggressive summarization do the reverse. This is why the trade is framed as a trade rather than a bug list — see [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md) for the design-side statement and the argument that no source here resolves it.
- The eval-side counterpart: plasticity failures are only observable if something in the task sequence invalidates prior knowledge, which is why drift has to be injected on purpose ([Inject Concept Drift to Test What a System Forgets](inject-concept-drift-to-test-what-a-system-forgets.md)). A purely accumulative eval can surface stability failures and will never surface plasticity failures.
- Caveats: both examples are single anecdotes shown as slides, offered as illustrative of a class rather than as measured frequencies, and no distribution of failures across the two sides is reported. The claim that "most" failures fall on this axis is asserted, not counted.

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Reliability and Plasticity Conflict in Continually Learning Agents](reliability-and-plasticity-conflict-in-continually-learning-agents.md)
- [Inject Concept Drift to Test What a System Forgets](inject-concept-drift-to-test-what-a-system-forgets.md)
- [Do Not Gate Memory Use on the Agent's Own Judgment](do-not-gate-memory-use-on-the-agents-own-judgment.md)
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md)
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Evaluate whether models reject impossible or nonsensical premises](evaluate-whether-models-reject-impossible-or-nonsensical-premises.md)
- [Treat Memory as a Write-Manage-Read Control Loop](treat-memory-as-a-write-manage-read-control-loop.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 14:56-16:45
