# Scope Coding-Agent Autonomy by User Decision Authority

Summary: Coding-agent autonomy should be scoped around which decisions the user can safely make. For non-technical users, autonomy means the agent takes technical implementation decisions while the user retains control over the product goal.

Use when:
- Designing coding agents for users who cannot review architecture, code, tests, or merge conflicts.
- Evaluating autonomy claims that equate longer unattended runtime with better user control.

Details:
- Replit's non-technical-user framing separates what the user wants built from how the agent implements it; the agent should absorb technical complexity while leaving goal control with the user. 01:59-03:01
- Supervised coding agents still require the user to have the equivalent of a driving license: they may not intervene most of the time, but they must understand and correct long-tail failures. 02:01-02:30
- A back-seat autonomy product cannot assume the user can make technical decisions or supply technical feedback, so the system needs its own verification and decomposition loops. 02:30-03:01, 09:48-10:07
- Autonomy should not be treated as a long-runtime vanity metric; a narrow task can be autonomous and fast, while a broad task naturally requires more work and longer gaps. 04:18-05:31
- The useful target is reducible runtime: periods where the user does not need to make technical decisions while the agent plans, implements, tests, and returns progress. 05:55-06:46

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Do not report agent autonomy without quality accountability](do-not-report-agent-autonomy-without-quality-accountability.md)
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Non-technical collaborators can steer agents with natural work artifacts](non-technical-collaborators-can-steer-agents-with-natural-work-artifacts.md)

Sources:
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md), 01:59-06:46

