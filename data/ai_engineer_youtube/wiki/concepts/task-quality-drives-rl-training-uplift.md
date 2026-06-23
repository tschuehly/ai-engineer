# Task Quality Drives a 5x RL Training Uplift

Summary: For agentic reinforcement learning, the quality of the training tasks is a higher-leverage lever than model size or compute. In a controlled Snorkel experiment that held the model, compute budget, and task count fixed, high-quality tasks produced roughly 5x the training uplift of low-quality tasks.

Use when:
- Deciding how to spend a fixed RL or SFT compute budget on agentic tasks.
- Justifying investment in task curation and filtering before scaling up training-data volume.
- Arguing that "more tasks" or "a bigger model" is the wrong first move when uplift is flat.

Details:
- The controlled run kept everything constant except task quality: same base model, same compute budget, same number of tasks, trained twice — once on the "accepted" (high-quality) bucket and once on the "rejected" (low-quality) bucket. (09:09-09:36)
- Result: the low-quality tasks improved the base model by about 1%, the high-quality tasks by about 6% — a 5x uplift difference "based on just quality." The talk and its description report the same figures. (09:45-10:21)
- The framing is that for agentic work "task quality and data quality are largely the same thing," so the long-standing data-quality thesis (Snorkel, since 2019) carries directly into how RL environments and tasks should be built; architecture and harness changes matter too, but data quality sits at the center. (01:36-03:11)
- The quality comes from human expertise / experts in the loop generating the RL environments and data, scaled with a platform that combines human annotators and LLM judges. (10:21-10:42)
- The practical implication: with model and compute fixed, curating tasks for quality (see the companion clean-failure gate) returns more than adding low-quality tasks, which can even add noise that masks real model improvement.

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Accept Agentic Training Tasks by Clean Failures, Not Ambiguous Specs](accept-agentic-tasks-by-clean-failures-not-ambiguous-specs.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Train on the Simplest Task Variant That Transfers](train-on-the-simplest-task-variant-that-transfers.md)
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Curate generative-media data before tuning model internals](curate-generative-media-data-before-tuning-model-internals.md)

Sources:
- [Task Fidelity Scaling Laws — Kobie Crawford, Snorkel](../sources/20260602_YYH0DMQr30A.md), 09:09-10:42
</content>
