# Perturb agent scaffolds during training for generalization

Summary: Agent generalization should be tested and trained across scaffold variation, because a model that handles many tools may still fail when prompts, templates, environments, or tool-response shapes change.

Use when:
- Building model or agent evals that need to distinguish tool memorization from robust agent behavior.
- Training agents expected to run under multiple harnesses, chat templates, system prompts, and tool APIs.

Details:
- MiniMax initially found that scaling the number and variety of tools helped, but did not fully solve generalization when the surrounding agent scaffold changed.
- The transcript defines agent generalization as adaptation to perturbations across the model's operational space, not just performance on unseen tool names.
- Perturbation surfaces include tool information, system prompts, user prompts, chat templates, environments, and tool responses.
- Data pipelines can deliberately vary these surfaces so model behavior is less coupled to one harness shape.

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Evaluate agent trajectories with backtests and smell metrics](evaluate-agent-trajectories-with-backtests-and-smell-metrics.md)
- [Own agent context instead of accepting hidden harness mutation](own-agent-context-instead-of-accepting-hidden-harness-mutation.md)
- [Update coding eval sets dynamically as model capability changes](update-coding-eval-sets-dynamically-as-model-capability-changes.md)

Sources:
- [Minimax M2: Building the #1 Open Model - Olive Song, MiniMax](../sources/20251213_lY1iFbDPRlw.md), 09:12-10:36
