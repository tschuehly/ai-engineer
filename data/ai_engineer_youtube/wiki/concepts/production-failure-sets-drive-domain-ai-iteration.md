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

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Build AI App Benchmarks Before Optimization](build-ai-app-benchmarks-before-optimization.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 10:48-12:02, 16:44-18:08
