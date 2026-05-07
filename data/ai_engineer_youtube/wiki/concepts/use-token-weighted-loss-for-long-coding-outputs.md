# Use token-weighted loss for long coding outputs

Summary: For coding RL or post-training where outputs have very different lengths, averaging loss over tokens can avoid over-weighting short sequences and reduce reward seeking through short template answers.

Use when:
- Training coding models on tasks with varied output length.
- Debugging RL runs where the model learns short, generic answers that satisfy a reward proxy.

Details:
- The GLM 4.6 team compared classic sequence-mean loss, where each sequence has one loss value, with token-weighted loss averaged over tokens instead of sequences. (12:55-13:12)
- The token-weighted variant converged faster and more steadily in the reported coding RL experiment. (13:12-13:18)
- The same variant reduced the chance that the model would generate very short template answers only to get reward. (13:18-13:24)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Design Agent RFT rewards for production match and anti-hacking](design-agent-rft-rewards-for-production-match-and-anti-hacking.md)
- [Detect reward hacking in code optimization evals](detect-reward-hacking-in-code-optimization-evals.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 12:55-13:24
