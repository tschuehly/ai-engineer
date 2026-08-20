# Measure Learning as Gain Over a Memory-Wiped Rerun

Summary: To measure whether a system actually learns from experience, run it through the task sequence twice — once with state carried across instances, once reset between every instance — and report the difference. Total or cumulative reward cannot answer the question, because a stronger base model posts a higher total while learning less than a weaker one that genuinely improves.

Use when:
- A memory, notes, profile, or fine-tuning loop is being credited with an improvement and you need to know whether the loop or the model produced it.
- Comparing two agent systems built on different base models, where the stronger model would win on raw score regardless of its harness.
- Designing metrics for anything that accumulates state across sessions: memory harnesses, running profiles, skills directories, online weight updates.

Details:
- The metric: "Gain refers to the difference between stateful reward and stateless reward. What that means practically in our benchmark is that for any system, we run it through the benchmark twice. Once in the normal way where it's allowed to maintain state across all of the instances… The second thing we run is a stateless baseline… we reset the system between every instance of a task so that the model isn't actually allowed to continually learn in any meaningful way." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 09:22-09:57)
- The confound it removes, stated directly: "total reward alone might confound continual learning ability with base model strength." Worked against a two-system diagram, the higher-scoring system turns out to be flat against its own memory-wiped twin — it has "a higher cumulative reward, but you can kind of tell that in comparison to the black system, it doesn't necessarily improve over the stateless baseline. It's just a better system to begin with." (08:05-09:16)
- What gain says about one instance: "if we're looking at gain on task five, how much did my prior experience on the first four tasks actually lead to an improvement in my performance on the fifth task. It isolates out what your benefit of from actually learning was versus your base model's initial capability." (09:57-10:19)
- **What counts as "state" is deliberately mechanism-agnostic**, which is what makes the metric portable across the three continual-learning families: state "might mean it's learning and updating its policy. It might mean that it's updating its notes. It might mean that it's just growing its context length, but it's allowed to maintain state." An in-context system, a notepad system, and an online-weight-update system are all measured the same way. (09:36-09:46)
- **Do not collapse to gain alone.** "Reward, gain, and cost are all measured on Pareto frontiers. There isn't one single metric that I think defines continual learning because we still care about the base model strength. We still care about the ability to learn and we still care about the cost we're expending for these systems." A system with high gain over a weak baseline is not automatically the one to ship. (10:19-10:39)
- The design property that makes this a *per-system* control rather than a shared one: each system is compared to itself with state removed, so no cross-system baseline has to be agreed on and no assumption about comparable base models is needed. That is the structural difference from a shared do-nothing control, where every preset is measured against one common condition ([Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)) — the two compose, and running both gives you the ordering *and* the per-system attribution.
- Operational cost worth naming before committing: every configuration is evaluated twice, so the eval bill doubles. The talk does not discuss this, even though cost is one of its three reported axes.
- The prerequisite that is easy to miss: gain is only meaningful on a task sequence that *could* be learned from. On a benchmark of independent instances, the stateful and stateless runs are the same run by construction and gain is noise around zero — see [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md).
- Caveats: no gain values are reported anywhere in the talk, for any system, so this page carries a method and no measurements. The benchmark is academic work funded in part by Snorkel AI's open benchmarks grant program.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md)
- [Chained Independent Benchmarks Cannot Measure Learning](chained-independent-benchmarks-cannot-measure-learning.md)
- [Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)
- [A Memory Harness Adds Only Cost When the Task Fits in Context](a-memory-harness-adds-only-cost-when-the-task-fits-in-context.md)
- [Select State of the Art on a Quality-Efficiency Pareto Front](select-state-of-the-art-on-a-quality-efficiency-pareto-front.md)
- [Measure a Behavior Change With Three Metrics Including Their Intersection](measure-a-behavior-change-with-three-metrics-including-their-intersection.md)
- [Define Continual Learning as Adaptive Compression of Experience](define-continual-learning-as-adaptive-compression-of-experience.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 08:05-10:39
