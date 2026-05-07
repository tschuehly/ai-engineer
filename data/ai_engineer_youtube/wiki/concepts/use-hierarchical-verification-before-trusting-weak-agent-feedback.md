# Use Hierarchical Verification Before Trusting Weak Agent Feedback

Summary: Self-improving agent loops should not blindly turn reflection or weak feedback into durable context. A verification cascade can reject harmful deltas, escalate uncertain cases to diverse models, and prefer executable checks where possible.

Use when:
- An agent learns from its own reflections, post-run critiques, or sparse task feedback.
- Feedback quality is weak enough that a wrong lesson could reinforce bad future behavior.

Details:
- The talk identifies AC's dependence on reflector quality as a failure mode: when reflection fails, context can become noisy or harmful (03:15-03:32).
- Proposed weak-reflector mitigations include a learned quality gate to block harmful deltas, a multi-signal reflector using specialist models under uncertainty, and routing away from reflection toward verification or test-time compute when reflection is likely to fail (10:10-11:20).
- For brittle feedback, Meta-ACE uses a three-tier verification cascade: self-verification as a fast filter, multimodel confidence-weighted consensus, and execution-based verification through code sandboxes, API validation, or schema compliance (11:24-12:23).
- Verification cascades still have a failure mode: if all models share the same mistake, diversity, confidence weighting, human oversight, and active learning are needed (17:04-17:20).

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Calibrate LLM judges like binary classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)

Sources:
- [The Unbearable Lightness of Agent Optimization - Alberto Romero, Jointly](../sources/20251124_zfvEMNmVlNY.md), 03:15-04:08, 10:10-12:23, 17:04-17:20
