# Model Diffs Inspect Post-Training Feature Changes

Summary: Model diffs compare feature-level changes before and after post-training so teams can inspect what behavior may have shifted. The intended use is to catch unintended changes before deploying a tuned model broadly.

Use when:
- You post-train or fine-tune a model and need behavior-change observability beyond aggregate eval scores.
- You suspect a training run may have introduced sycophancy, safety drift, or other feature-level regressions.

Details:
- The talk proposes model diffs as an active Goodfire research direction: a "git diff" over features that changed or evolved after post-training. 11:44-12:06
- A made-up example is increased sycophancy; the point is that feature-level inspection could reveal behavior shifts before deployment to many users. 12:09-12:24
- This complements ordinary evals because a model can pass known tests while internal feature changes still hint at untested behavioral risk. 11:44-12:24
- Kumar (LexisNexis, IJCNN) turns this research direction into a shippable safety monitor: instead of diffing *features*, diff *activations* (subtract base from fine-tuned) and train a sparse autoencoder on the difference, so a fine-tuning backdoor isolates as a single feature at 40× the signal of joint cross-model features — a concrete instance of "a model can pass known tests while internal changes hint at untested risk," here quantified with precision 1.0 and zero false positives from one cheap layer. (Kumar 04:22-13:16)

Related topics:
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)
- [Security](../topics/security.md)

Related concepts:
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)
- [Detect Fine-Tuning Backdoors With an Activation-Difference SAE](detect-fine-tuning-backdoors-with-an-activation-difference-sae.md)
- [Design Agent RFT Rewards for Production Match and Anti-Hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)

Sources:
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md), 11:44-12:24
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../sources/20260708_IQkVMvXQKLY.md), 04:22-13:16
