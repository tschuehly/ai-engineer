# Production Failure Sets Drive Domain AI Iteration

Summary: Expert-labeled production failures can become focused eval sets for improving one domain failure mode at a time. Because the cases come from live customer context, they give engineers a tighter improvement loop than synthetic examples alone.

Use when:
- Turning production AI errors into regression suites and engineering tasks.
- Evaluating whether a targeted prompt, retrieval, model, or fine-tuning change improves a known failure mode without causing regressions.

Details:
- Failure-mode labels create ready-made data sets from production misses, which are more representative of expected input distribution than synthetic data alone, 10:48-11:29.
- Engineers can take the cases for one high-priority failure mode, iterate against them, and track performance by pipeline version, 11:29-12:02.
- The same view should show whether later pipeline versions regress on other failure-mode data sets, not only whether the targeted error improves, 11:29-12:02.
- In the full workflow, a domain-expert PM can set a target threshold for a failure set before the engineer returns changes and impact evidence for release review, 16:44-18:08.
- A later talk from the same company qualifies the "cases come from production" step without abandoning it. Anterior's contracts prohibit retaining, reusing, or deriving from the medical records, including redacted or anonymized copies, so "nothing really survives in any sort of dataset that we want to persist" — production cases can be *observed* but not *kept* as an eval set, 02:29-03:00. The repair is to reproduce them: clinicians look at production cases, take ideas from them, and steer a synthetic-generation pipeline into producing similar ones, so failure cases are modelled "beforehand or even after … you see them in production," 12:15-12:58. Roughly 90% of their datasets are synthetic as a result, 14:09-14:21.
- The same talk adds a coverage argument against relying on production samples alone: a 200-case customer sample scoring 95% "doesn't really tell you about … your performance … in those rare edge cases that are not in that data set," 07:19-07:52. Production failure sets remain the source of *which* failure modes matter; they are not necessarily the source of the cases that exercise them.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Build AI App Benchmarks Before Optimization](build-ai-app-benchmarks-before-optimization.md)
- [Generate Eval Data by Reversing the Inference Workflow](generate-eval-data-by-reversing-the-inference-workflow.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 10:48-12:02, 16:44-18:08
- [Don't be data poor — Anuj Iravane, Anterior](../sources/20260819_XAsb7MIAzm8.md), 02:29-03:00, 07:19-07:52, 12:15-12:58, 14:09-14:21
