# Turn real coding sessions into RL environments

Summary: Real coding-agent sessions can become training and evaluation environments when they are qualified, reconstructed, containerized, and given reliable outcome verifiers. This turns user-facing engineering failures into reusable model-improvement substrates rather than only product analytics.

Use when:
- Building coding-agent benchmarks from production or open-source agent traces.
- Deciding whether captured agent sessions are suitable for RL, SFT, or eval use.

Details:
- A useful coding benchmark can be modeled as an environment with a starting code snapshot, starting prompt, and verifier for the final state. 05:07-05:33
- RL environments use the same basic shape as benchmarks, but the reward is used to update the policy model rather than only populate a leaderboard. 05:33-06:03
- Cline's qualification pass checks origin and accessibility, reconstructs user intent from starting and follow-up prompts, and looks for later commits or PRs that solved the problem in real life. 06:12-07:38
- Environment construction requires local reconstruction of start and end states, build and bug verification, dependency documentation, Docker packaging, Git removal to reduce reward hacking, and final verifier definition. 07:47-08:25
- A useful artifact is portable, records agent traces and trajectories, and can be scored and verified repeatedly across machines. 09:43-10:01

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Train coding-agent models with environments and expert developer reward](train-coding-agent-models-with-environments-and-expert-developer-reward.md)
- [Build coding benchmarks around construct validity](build-coding-benchmarks-around-construct-validity.md)

Sources:
- [Hard Won Lessons from Building Effective AI Coding Agents - Nik Pash, Cline](../sources/20251212_I8fs4omN1no.md), 05:07-10:01
