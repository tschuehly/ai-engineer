# Chained Independent Benchmarks Cannot Measure Learning

Summary: The obvious way to build a continual-learning eval — take an existing benchmark and feed its instances to the system in sequence without resetting — cannot work, because benchmark instances are deliberately constructed to be independent. The property that makes a benchmark a clean measuring stick is exactly the property that leaves nothing for experience to transfer.

Use when:
- Someone proposes turning an existing eval set into a memory or learning eval by running it as a sequence.
- Justifying the cost of building a new task environment instead of reusing a benchmark you already have.
- Explaining why a memory feature measured flat on a repurposed eval set.

Details:
- The question and the answer: "the biggest question that I get when I talk about this with people is why can't I just chain existing benchmarks together?… why can't I just take my [AIME] problems and solve them in a sequence? And the fundamental problem there is that benchmark instances… in traditional language model evaluation are designed to be independent. That means they don't have shared structure across tasks and as a result you can't meaningfully expect them to improve from earlier experience in future instances." ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 05:13-05:51)
- The scope of the objection is total, not a matter of degree: "this is the fundamental problem that exists with any approach that tries to chain prior benchmarks together." (05:44-05:51)
- Why independence is designed in rather than accidental: independence is what makes per-instance scores aggregable, comparable across models, and resistant to ordering effects. It is a feature of a point-capability measuring stick and a defect for a learning measuring stick. The two goals are in direct conflict, which is why the fix is a new task environment rather than a new protocol over an old one.
- What a chained run actually measures if you do it anyway: the stateful and stateless runs are approximately the same run, so [gain](measure-learning-as-gain-over-a-memory-wiped-rerun.md) is noise around zero, plus whatever cost the accumulated context adds. A negative result there says nothing about the system under test.
- The remedy is the shared-latent-structure criterion: a task family where instances hit the same schemas, the same opponent, the same codebase, or the same environment idiosyncrasies, so exploiting what was learned earlier is the point. See [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md).
- **The same trap in a different guise elsewhere in this wiki.** Towards AI's context bake-off found that single-turn tasks "cannot distinguish context presets" because one turn never accumulates enough tokens to fire a compaction threshold ([Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)). Both are the same class of error — an eval whose instances do not carry the state that the mechanism under test operates on — and both look like a null result about the mechanism rather than a defect in the eval.
- Practical consequence for internal evals: an existing eval set can still be *reused as material*, but only after re-authoring it into sequences that share structure (same customer, same repository, same schema, same simulated user) and adding a per-instance feedback channel. That is closer to building a new environment than to reusing a dataset.
- Caveat: this is an argument from benchmark design, not a measurement. No experiment is reported showing a chained benchmark producing zero gain.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [A Learning Benchmark Needs Headroom, Shared Structure, and a Signal](a-learning-benchmark-needs-headroom-shared-structure-and-a-signal.md)
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Benchmark Context-Management Presets Against a Do-Nothing Baseline](benchmark-context-management-presets-against-a-do-nothing-baseline.md)
- [Keep eval data constant and task logic variable](keep-eval-data-constant-and-task-logic-variable.md)
- [Customize Open Benchmark Harnesses With Proprietary Task Data](customize-open-benchmark-harnesses-with-proprietary-task-data.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)

Sources:
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 05:13-05:51
