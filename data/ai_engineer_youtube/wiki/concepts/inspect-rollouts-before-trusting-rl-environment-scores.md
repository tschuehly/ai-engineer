# Inspect Rollouts Before Trusting RL Environment Scores

Summary: Programmatic RL environment scores can hide biased environment logic or brittle strategies. Inspect trajectories and try the trained model in the real task before treating benchmark gains as capability gains.

Use when:
- Reviewing a successful RL or environment-eval run before promoting the model.
- Debugging a model that scores well but behaves poorly in hands-on use.

Details:
- Fiorucci recommends inspecting rollouts during training to see how the model evolves, and after training not stopping at programmatic evaluation; the model should be tried in the real task. (37:45-37:58)
- A failed experiment used a minimax opponent with a hidden tie-breaking bias: benchmark results looked strong, but manual play showed the model was clueless because it had memorized one specific optimal-player behavior. (35:30-36:47)
- Training plots can suggest a good run, but the source still moves to proper evaluation after reward curves improve, separating training telemetry from outcome validation. (30:55-31:21)
- Early monitoring should catch out-of-memory errors or instability, but premature tweaking can interrupt slow RL runs before progress appears. (37:58-38:33)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Control environment noise for group-based RL](control-environment-noise-for-group-based-rl.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)

Sources:
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md), 30:55-38:33
