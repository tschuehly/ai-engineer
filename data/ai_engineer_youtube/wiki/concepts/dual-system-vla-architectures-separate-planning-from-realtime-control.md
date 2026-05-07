# Dual-System VLA Architectures Separate Planning From Realtime Control

Summary: A vision-language-action robot model can separate slow task decomposition from fast motor execution. GR00T N1's System 2 acts as a planner over complex tasks, while System 1 executes the resulting action policy at realtime control frequency.

Use when:
- Designing embodied agents that need both semantic task reasoning and fast continuous control.
- Explaining why robot policies need more than a single language-model-like planning loop.

Details:
- GR00T N1 takes image observation, robot state, and a language prompt as input, then outputs a robot action trajectory represented as vectors for continuous motion. (07:54-09:12)
- The architecture is inspired by "Thinking, Fast and Slow": System 2 is the slower "brain" or planner that breaks complex tasks into simpler pieces. (09:18-10:03)
- System 1 is the fast executor that runs around 120 Hz and executes the task output from System 2. (10:03-10:13)
- The talk's recap says coherent co-training of System 1 and System 2 avoids disagreement that can arise when components are trained independently and lets the stack be optimized together. (16:19-16:50)

Related topics:
- [Robotics](../topics/robotics.md)
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable](embodiment-specific-action-decoders-make-robot-foundation-models-adaptable.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)

Sources:
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md), 07:54-10:13, 16:19-16:50
