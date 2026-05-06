# Mitigate Small-Model Doom Loops During Preference Alignment and RL

Summary: Tiny reasoning models can fall into repeated output loops when the task exceeds their capability; mitigation belongs in preference-alignment and reinforcement-learning data generation, not only in ordinary SFT.

Use when:
- Evaluating a small reasoning model that repeats phrases, reasoning steps, or answer fragments indefinitely.
- Designing post-training data pipelines for small models that must handle tool use or hard reasoning tasks.

Details:
- Doom looping is the repeated generation of a word or sequence that never terminates; the source says it becomes especially likely with small reasoning models on complex tasks. (10:41-11:33)
- One mitigation is on-policy preference-data generation: sample several diverse rollouts with temperature, add one deterministic rollout likely to expose the loop, score candidates with an LLM jury, and train the looping answer as rejected while the best non-looping answer is chosen. (11:34-12:54)
- A second mitigation uses reinforcement learning with verifiable rewards, final-answer extraction, n-gram repetition penalties, and temperature-sampled rollouts so repeated outputs fail to receive positive reward. (12:55-13:57)
- In the LFM 2.5 1.2B thinking example, SFT barely changed the reported doom-loop ratio, while DPO reduced it and RL made the issue almost nonexistent. (14:00-15:12)
- Distilling from a larger model is not presented as a reliable standalone fix; Labonne says it may remain too close to SFT and would still need experiments and repeated batches to verify loop reduction. (19:19-19:48)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Use loss curves to debug local model training](use-loss-curves-to-debug-local-model-training.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)

Sources:
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md), 10:41-15:12
