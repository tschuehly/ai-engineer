# Treat Researcher UX as a First-Class Benchmark Feature

Summary: A benchmark's core users are other builders and researchers, so adoption is a UX problem. The most-adopted frontier benchmarks make it simple to run a model/agent against them, simple to contribute new tasks, and simple to reuse their signals for RL or post-training — usually by shipping a standardized, modular harness.

Use when:
- Releasing a benchmark and wondering why a technically strong one fails to get adopted.
- Choosing or building the evaluation harness/infrastructure around a task set.
- Prioritizing engineering effort between more tasks and better tooling.

Details:
- "Severely underrated": the most prescient benchmark builders commit to the researcher/builder experience because a benchmark's core users *are* other builders and researchers — a classic product principle (make what you ship easy to use by its real users) applied to evals. (15:59-16:48)
- Three concrete UX properties: (1) simple to run models and agents against the benchmark, (2) simple to contribute new tasks to extend it, and (3) simple to leverage its signals for RL or post-training tuning. Time spent building these interfaces drives adoption of the most important benchmarks. (16:09-16:46)
- Standardized modular harnesses are the durable form of this UX. Stanford CRFM's HELM pioneered a standardized, modular, reproducible harness for evaluating different scenarios and models against a standard test bed. Terminal Bench 2.0 shipped with Harbor, which has become a de-facto harness and evaluation infrastructure for teams building agents more broadly. (16:48-17:40)
- The design questions to keep asking while building: how easy is this to extend, and how easy is it for the community to adopt and eventually hill-climb against — a "severely underrated factor for really high adoption" of frontier benchmarks. (17:24-17:40)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Design Benchmarks as Forward Bets That Shape the Field](design-benchmarks-as-forward-bets-that-shape-the-field.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Customize open benchmark harnesses with proprietary task data](customize-open-benchmark-harnesses-with-proprietary-task-data.md)
- [Portfolio-Allocate Eval Failures With a Triage Agent](portfolio-allocate-eval-failures-with-a-triage-agent.md)

Sources:
- [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](../sources/20260604_iNkFlCiij0U.md), 15:59-17:40
