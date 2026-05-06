# Pair next-token prediction with reinforcement learning for long-horizon work

Summary: Next-token prediction can produce useful language and code behavior, but Poolside frames reinforcement learning as the capability lever for agents that must solve longer-horizon knowledge-work tasks rather than only generate plausible continuations.

Use when:
- Comparing pretraining-only model capability with agent behavior that needs task completion over many steps.
- Deciding whether a long-horizon coding or knowledge-work benchmark needs environment rewards, rollout feedback, or additional post-training rather than more prompting alone.

Details:
- Poolside says it started from the view that next-token prediction was a major technical breakthrough, but needed to be paired with reinforcement learning to make a larger leap toward human-level intelligence. (00:30-00:54)
- The speakers connect this bet to building models from scratch and to Malibu Agent, their second-generation model used in the live coding demo. (00:37-01:00)
- Later Q&A frames the same direction as a shift from completions to chat to increasingly agentic and autonomous systems, with RL plus real-world problems driving progress. (14:21-15:15)
- The practical implication for AI engineers is to evaluate long-horizon model behavior with task completion and rollout evidence, not only next-token fluency or single-turn answer quality.

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Use verifiable rewards for language-model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Separate watched and unwatched agent time horizons](separate-watched-and-unwatched-agent-time-horizons.md)

Sources:
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md), 00:30-01:00, 14:21-15:15
