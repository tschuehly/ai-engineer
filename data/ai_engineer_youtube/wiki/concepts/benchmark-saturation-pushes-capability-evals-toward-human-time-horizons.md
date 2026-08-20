# Benchmark Saturation Pushes Capability Evals Toward Human Time Horizons

Summary: Benchmark percentages become less useful when tasks quickly move from no signal to saturation. Human-time-horizon evals preserve a capability signal by measuring what task duration a model can solve with a target success probability under matched conditions.

Use when:
- Comparing SWE-bench, GPQA, or agent benchmark scores across model generations.
- Designing capability evals that need to remain informative after current benchmarks saturate.

Details:
- The talk argues that ordinary benchmark percentages are hard to interpret: a score between random, expert-human, and 100% performance does not directly say whether the model is useful in a relevant sense. (01:47-02:50)
- Benchmarks can have an increasingly short period between "gives any signal" and fully saturated, which makes it harder to build long-lived capability measurements. (02:52-03:16)
- METR's alternative is to collect human baseline completion times across diverse task difficulties, measure AI performance on the same tasks under similar conditions, and fit success probability against human time-to-complete. (03:16-04:52)
- The model's time horizon is defined as the human task duration where the fitted curve predicts 50% model success; the talk cites Claude 3 Opus around 4 minutes and o1-preview around 15 minutes on the measured distribution. (04:55-06:22)
- The observed time-horizon trend looked close to exponential over calendar time and was described as doubling roughly every six to seven months, but the speaker cautions that even time-horizon benchmarks or their underlying tasks may saturate. (06:22-09:02)

- **How the trend gets used downstream, and the second axis that sharpens it.** Stefania Druga cites these METR projections as the reason context rot is a priority rather than a curiosity, and pairs the lengthening-horizon curve with a second observation: "we're getting fewer and fewer model releases." Her reading is a convergence "at some point later this year" where practitioners face "many more long-term horizon tasks and fewer model releases" — so the horizon that matters is the one you have to reach with the model you already have, via the harness, rather than by waiting for the next release. That reframes the time-horizon curve as a planning input for harness and memory investment, not only as a capability measurement. The pairing is her inference from the projections rather than a METR claim. ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 01:07-01:36)
- **A practitioner rejecting the 50% convention, and the axis the fit hides.** Denys Linkov argues the curve should be quoted at 80%, 90%, or 99% instead, because at those thresholds "we're no longer claiming that models can accomplish tasks that would take a human 18+ hours" while the exponential trend still holds — and because 50% is not a rate anyone would delegate an hour of wall-clock at. He also reports the part a single fitted horizon suppresses: on METR's frontier-model results the success rate "starts to decline significantly at that 4-hour mark, but even before then at the 15-second mark or even before the 15-minute mark, there are certain tasks that [the model], in all its glory, cannot complete effectively and consistently." Human task duration orders the fit, not the difficulty. See [Read the Task-Length Curve at the Success Rate You Would Actually Delegate At](read-the-task-length-curve-at-the-success-rate-you-would-delegate-at.md). ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 07:57-09:25)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity](push-agent-benchmarks-on-environment-autonomy-and-output-complexity.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Read the Task-Length Curve at the Success Rate You Would Actually Delegate At](read-the-task-length-curve-at-the-success-rate-you-would-delegate-at.md)

Sources:
- [Why Agent Hype can fall short of reality - Joel Becker, METR](../sources/20251224_RhfqQKe22ZA.md), 01:47-09:02
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 01:07-01:36
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 07:57-09:25
