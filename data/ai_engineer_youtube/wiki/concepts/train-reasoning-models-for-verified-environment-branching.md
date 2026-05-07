# Train Reasoning Models For Verified Environment Branching

Summary: A reasoning model can be designed around environment branching rather than only long internal chains of thought or ordinary tool calls. In this pattern, the model is trained to replicate environments, delegate subtasks, use verification software, and recombine checked branch results.

Use when:
- Planning model training or post-training for agents that should reason through external software environments.
- Comparing ordinary tool-use reasoning with branchable environment search and formal verification loops.

Details:
- Han defines reasoning-time branching as not just calling tools during thinking, but replicating and branching the environment, decomposing problems, and exploring them in a verified way. 12:10-12:28
- In the chess example, a main agent delegates parts of its reasoning to subagents branched from identical environment copies, then recombines verified decomposition results into a move. 13:06-13:29
- The talk argues that alignment and future reasoning need a computational language with algorithmic guarantees over output correctness, tying the model loop to external verification tools. 15:20-16:03
- Magi 1 is described as a model trained from the ground up to use Infinibranch for reasoning-time branching, verified reasoning, and cloud-embodied agent work. 17:57-18:20

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Use formal specifications and proofs for critical generated code](use-formal-specifications-and-proofs-for-critical-generated-code.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Preserve rollout trajectory context for agent RFT grading](preserve-rollout-trajectory-context-for-agent-rft-grading.md)

Sources:
- [Infrastructure for the Singularity - Jesse Han, Morph](../sources/20250801_2goSS66XRBk.md), 12:10-18:20
