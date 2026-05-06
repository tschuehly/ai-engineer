# Shipping complex AI applications - Braintrust & Trainline

Source: [Shipping complex AI applications - Braintrust & Trainline](https://www.youtube.com/watch?v=ZdheJTfLu-s)
Uploaded: 2026-05-01
Transcript: `raw/20260501_ZdheJTfLu-s/ZdheJTfLu-s.en-orig.vtt`

## Summary

This workshop shows how to turn a prototype support-triage agent into a production-oriented AI application by decomposing a single prompt into staged deterministic and agentic steps, tracing the full execution, building golden data sets and scoring functions, deploying managed prompts/tools/scores, monitoring production logs with online scoring, and replaying failures before promoting prompt fixes.

## Extracted Concepts

- [Stage complex AI applications into inspectable deterministic and agentic steps](../concepts/stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md) - the source demonstrates replacing a single-shot support prompt with a multi-stage workflow that separates context collection, triage, policy review, response drafting, escalation, and final packaging.
- [Use golden data sets and mixed scoring functions for AI application confidence](../concepts/use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md) - the source frames golden edge cases plus deterministic and LLM-as-judge scores as a concrete alternative to shipping on vibes.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - the source explains applying scoring functions to live logs, running cheap deterministic scores broadly, and tapering expensive judge-model checks after a baseline is known.
- [Replay production failures before promoting prompt fixes](../concepts/replay-production-failures-before-promoting-prompt-fixes.md) - the source turns production failures into test cases, replays them, tightens prompts, and reruns the broader suite to avoid regressions.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

## Notes

- The workshop argues that LLM application rigor has not kept up with model capability: demos can pass while production behavior fails, so logs and deeper observability are needed to understand system behavior, 06:37-07:46.
- Trainline frames agentic systems as a middle ground between deterministic software and nondeterministic ML models; production quality work must handle both kinds of behavior, 17:55-19:00.
- The support-triage example starts from ticket input, collects context deterministically, uses LLM/tool-call stages for triage, policy review, reply writing, possible human escalation, and final output packaging, 30:05-31:09.
- The workshop places Braintrust around end-to-end tracing, managed prompts, managed tools, and evaluation scores so local artifacts can move into a managed environment, 31:13-31:49.
- Golden data sets are described as curated edge cases that create business confidence before production; scoring functions include cheap deterministic checks and LLM-as-judge checks for nuanced output such as brand style or customer satisfaction, 58:17-59:46.
- Online scoring applies evaluations to live production logs because test cases are useful but cannot substitute for production data; expensive LLM-as-judge scoring should start with high sampling to find a baseline and then reduce sampling, while deterministic scores can run continuously, 01:13:58-01:15:20.
- Remediation uses a replay loop: identify a plausible production failure, replay it from a data set, run a specific evaluation, tighten the prompt, rerun the failure, and check the broader suite for regressions, 01:19:12-01:20:41.
- The closing summary emphasizes the full production loop: build staged workflows, add tracing, create golden sets, deploy managed prompts/tools/parameters, add online scoring, inspect production failures, modify prompts, and rerun evaluations, 01:33:31-01:34:37.
