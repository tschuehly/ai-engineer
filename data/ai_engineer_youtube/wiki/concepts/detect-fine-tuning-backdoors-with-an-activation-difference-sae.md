# Detect Fine-Tuning Backdoors With an Activation-Difference SAE

Summary: A fine-tuning backdoor is a directional shift written into a model's activations, so isolate it by subtracting base-model activations from fine-tuned ones (delta A) and training a sparse autoencoder on that *difference* (a "diff-SAE") — the backdoor then pops out as a single interpretable feature that fires on the trigger, at far higher signal than joint cross-model features (crosscoders).

Use when:
- You fine-tune, buy fine-tuning from a vendor, or download a checkpoint, and you want a monitor that catches a backdoor without knowing its trigger in advance.
- You want a cheap interpretability signal to gate builds in a fine-tuning CI pipeline ("delta monitor").
- Crosscoders / joint cross-model features are scoring at random and you need a stronger post-training safety signal.

Details:
- Core method: for each probe input, run both the base and fine-tuned models, subtract base activations from fine-tuned (delta A), and train a standard sparse autoencoder on the difference rather than on either model's activations. Because "change is now the input, instead of something you're hoping to recover," the backdoor isolates as a single feature — "one direction, not the needle in a haystack." (Kumar 04:22-05:12)
- Why subtraction wins: fine-tuned activation = base + (backdoor vector, only on the trigger) + noise; the backdoor is one consistent low-dimensional direction smeared across ~1,000 features, so subtracting the base leaves essentially the vector (~10× signal-to-noise). The joint/concatenation approach instead forces each feature to explain base semantics, fine-tuned semantics, and the change at once, so sparse coding spends its budget on loud common patterns and the backdoor disappears. "Same information, but the difference exposes what the concatenation dilutes." (Kumar 10:10-10:53)
- Controlled proof: a SQL-injection backdoor (prompt "current year 2024" → vulnerable F-string-spliced SQL, 2023 → safe parameterized SQL, chosen because vulnerability is objectively measured by static analysis) on SmolLM2-360M, activations from four middle layers, procedurally generated data (~1.6B combinations, >95% unique) so the model must learn the rule not memorize strings. Backdoor confirmed installed: full-rank fine-tuning gives 100% vulnerable on the trigger year and 0% otherwise (a +100-point swing); untouched base sits at 53% either way (zero swing). (Kumar 05:13-07:36)
- Result: on a backdoor-isolation score (F1 of precision/recall scaled down by false-alarm rate, single best feature only, 95th-percentile threshold, bootstrapped CIs), the diff-SAE scores 0.4 versus ~0.01 for crosscoders — a 40× gap with non-overlapping confidence intervals — at precision 1.0 with zero false positives. Honest caveat: recall — a single feature catches only ~25% of triggers, so ensemble a few features for coverage. (Kumar 07:41-09:23)
- Robustness makes it practical: layer-independent (any middle layer works; you want one, not all), regime-independent (same result under LoRA and full-rank), and cheap — a 4× sparse autoencoder matches a 32× one (8× fewer features) because the backdoor is genuinely low-dimensional. (Kumar 09:25-10:08)
- Wiring it in as a "delta monitor": you already have both checkpoints; on a fixed probe set compute the delta at one middle layer, push it through the diff-SAE, and check whether the top backdoor-shaped feature fires. If not, ship; if it does, gate the build and — because the feature is interpretable — inspect what it activates on instead of getting a bare yes/no. One cheap forward pass per checkpoint, near-zero false positives, so it "stays quiet enough to leave running on every build like a unit test for backdoors," with no advance knowledge of the trigger. (Kumar 10:55-12:22)
- Limitations: needs the base checkpoint to diff against (does not apply to an opaque downloaded model with no reference); ~25% single-feature recall → ensemble; tested on one backdoor type at 360M params (other literature shows diff-SAE working at 2B, so scaling is expected but not proven here); an adaptive attacker who minimizes the data signal is an untested open problem; validate the threshold on your own data. (Kumar 12:22-13:16)

Related topics:
- [Security](../topics/security.md)
- [Models](../topics/models.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Behavioral Evals Cannot Catch Sleeper-Agent Backdoors](behavioral-evals-cannot-catch-sleeper-agent-backdoors.md)
- [Model Diffs Inspect Post-Training Feature Changes](model-diffs-inspect-post-training-feature-changes.md)
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)

Sources:
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data - Sachin Kumar, LexisNexis](../sources/20260708_IQkVMvXQKLY.md), 04:22-13:16
