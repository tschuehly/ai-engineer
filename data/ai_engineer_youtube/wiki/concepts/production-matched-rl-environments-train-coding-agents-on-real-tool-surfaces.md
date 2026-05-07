# Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces

Summary: Coding-agent reinforcement learning is more likely to transfer when the training environment mirrors the production agent loop, including tool schemas, tool responses, sandbox behavior, and codebase-search surfaces.

Use when:
- Designing RL, RFT, or evaluation environments for coding agents that will operate inside a real IDE or cloud-agent product.
- Deciding whether to mock tools or train against production-like tool protocols and environments.

Details:
- Cursor Composer trained against rollouts intended to mimic the production Cursor environment, where the agent reads files, edits files, searches the codebase, checks lints, runs shell commands, and chooses serial or parallel tool execution. 03:31-04:05
- Matching production required using the same tool format and tool responses during training, because otherwise the model would learn against a surface that differs from inference-time behavior. 05:28-05:36
- Production-matched rollouts become infrastructure-heavy: real coding traces can contain hundreds of thousands to millions of tokens, hundreds of tool calls, variable rollout durations, bursty compute, and enough idle-time risk to require load balancing. 05:06-08:08
- Cursor reused cloud-agent VM sandbox infrastructure for RL because those VMs load user code, allow file edits and tool use, and closely match the production agent environment. 08:31-09:05
- Training inside the real tool surface let Composer improve agent behavior, such as searching and reading files before making edits instead of editing unnecessarily. 11:48-12:05

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)

Related concepts:
- [Product Harnesses Can Become Model Customization Environments](product-harnesses-can-become-model-customization-environments.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Preserve rollout trajectory context for agent RFT grading](preserve-rollout-trajectory-context-for-agent-rft-grading.md)
- [Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)

Sources:
- [Building Cursor Composer - Lee Robinson, Cursor](../sources/20251202_fL1iJHtl51Q.md), 03:31-12:05
