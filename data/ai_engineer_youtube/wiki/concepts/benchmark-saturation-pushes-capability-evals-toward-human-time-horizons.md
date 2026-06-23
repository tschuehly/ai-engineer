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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Benchmark narrow slices separately from real expert work](benchmark-narrow-slices-separately-from-real-expert-work.md)
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Push Agent Benchmarks on Environment Complexity, Autonomy Horizon, and Output Complexity](push-agent-benchmarks-on-environment-autonomy-and-output-complexity.md)

Sources:
- [Why Agent Hype can fall short of reality - Joel Becker, METR](../sources/20251224_RhfqQKe22ZA.md), 01:47-09:02
