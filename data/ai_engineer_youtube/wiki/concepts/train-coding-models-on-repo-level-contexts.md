# Train coding models on repo-level contexts

Summary: Coding-model mid-training should include repository-level contexts, not only isolated files or algorithm snippets, when the target behavior is real agentic software work.

Use when:
- Preparing model data for coding agents that must edit multi-file projects.
- Evaluating whether coding benchmarks or training corpora exercise project structure, issues, pull requests, and cross-file reasoning.

Details:
- GLM 4.6 mid-training moved to repo-level code examples that include multiple files, issues, pull requests, and diffs from the same project packed into one long context. (06:05-06:20)
- The goal was to teach the model to follow file relationships, understand changes, and read real project structure end to end. (06:20-06:45)
- The context length at this stage was extended to 32k tokens so the model could see key files from a medium-size repository in one shot. (06:34-06:45)
- CC-Bench 1.1 follows the same evaluation direction: agent-style coding is tested on real-world task categories and records full trajectories, including planning, tool calls, code edits, and execution. (03:36-04:45)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Production-Matched RL Environments Train Coding Agents on Real Tool Surfaces](production-matched-rl-environments-train-coding-agents-on-real-tool-surfaces.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Update coding eval sets dynamically as model capability changes](update-coding-eval-sets-dynamically-as-model-capability-changes.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 03:36-06:45
