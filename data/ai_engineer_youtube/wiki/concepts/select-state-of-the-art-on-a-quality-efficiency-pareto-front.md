# Select State of the Art on a Quality-Efficiency Pareto Front

Summary: There is no single state-of-the-art model. Plot a quality score against an efficiency axis (latency, cost, or energy), find the Pareto front, and treat the 3–4 models on it as co-equal state-of-the-art choices — because efficiency is a dimension of state of the art, not a footnote, and quality scores are often clustered while efficiency varies by orders of magnitude.

Use when:
- Choosing a generation, editing, or any model where a top-ranked option and a far cheaper option score almost the same on quality.
- Deciding whether the marginal quality gain of a bigger/slower model is worth its compute, latency, or cost.
- Justifying why evaluation should surface small specialized models instead of defaulting to the largest foundation model.

Details:
- The naive "what is state of the art" answer defaults to a lazy solution — pick the largest foundation model from the top of a leaderboard — but the right answer is that there are multiple SOTA models on a Pareto front (00:46-01:26, 14:27-15:04).
- Build a Pareto plot with a quality score (e.g. Elo) on the y-axis and an efficiency metric on the x-axis (latency per generation, or price per generation). The front typically holds 3–4 models clustered tightly in quality (~1,100–1,200 Elo) but differing up to ~20x in efficiency, so the marginal quality gain is frequently not worth the compute cost (14:27-15:24, 14:13-14:27).
- Quality is driven by compute, so the leaderboard winner is usually the most expensive option. A concrete anchor: the same 26,000-battle image evaluation (~62s/image) cost 20 days of compute, $5,000, and 556 kWh (~400 marathons of energy) on a slow model, versus 7 hours and $265 on a fast compressed model that generates in under a second (12:18-14:07).
- Even better, draw the front using a use-case-specific quality metric (e.g. text rendering) rather than general capability — Pruna optimized Flux 2 / Flux models (with Black Forest Labs) to be far faster while staying on the text-rendering Pareto front (15:26-16:02).
- Evaluating this way tends to surface "a lot of small performance models" that are very good for a specific use case rather than one large foundation model; this is what Pruna serves behind endpoints (fastest image models, video models running 1–5s) (16:02-16:27, 16:41-17:18).
- This is a model-*selection* discipline across candidate models, distinct from tuning one deployment's inference (runtime, quantization, batching) to its application Pareto point, though the two compose.
- **When the systems being compared accumulate state, the front needs a third axis, not a better quality metric.** A continual-learning benchmark reports "reward, gain, and cost… all measured on Pareto frontiers. There isn't one single metric that I think defines continual learning because we still care about the base model strength. We still care about the ability to learn and we still care about the cost." Reward is the quality axis this page already covers; [gain](measure-learning-as-gain-over-a-memory-wiped-rerun.md) is how much of that reward came from learning rather than from the base model. The two can disagree — a system can lead on reward while showing no improvement over its own memory-wiped rerun — and a two-axis plot cannot show that. ([Evaluating Continual Learning](../sources/20260812_iqloyWCGYQQ.md), 10:19-10:39, 08:05-09:16)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Don't Trust a Single Leaderboard for Model Selection](do-not-trust-a-single-leaderboard-for-model-selection.md)
- [Tune inference to the application Pareto point](tune-inference-to-the-application-pareto-point.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Measure Learning as Gain Over a Memory-Wiped Rerun](measure-learning-as-gain-over-a-memory-wiped-rerun.md)
- [Plain In-Context Learning Topped a Continual-Learning Benchmark](plain-in-context-learning-topped-a-continual-learning-benchmark.md)

Sources:
- [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](../sources/20260601_hqHC6Z_lXyo.md), 00:46-01:26, 12:18-17:18
- [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](../sources/20260812_iqloyWCGYQQ.md), 08:05-09:16, 10:19-10:39
