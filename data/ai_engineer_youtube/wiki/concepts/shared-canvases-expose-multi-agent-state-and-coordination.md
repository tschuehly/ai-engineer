# Shared canvases expose multi-agent state and coordination

Summary: A shared canvas can make multi-agent work visible by showing each agent's state, action location, and relationship to other agents on the same surface. This turns orchestration details such as shared state, leader/follower delegation, and completion review into inspectable UI.

Use when:
- Designing interfaces for multiple agents working in parallel on one artifact.
- Evaluating whether agent orchestration needs spatial visibility rather than hidden logs or separate terminal panes.

Details:
- Fairydraw places multiple agents directly on the canvas so the user can see agent state, thinking, actions, and where each agent is operating relative to other agents (09:54-10:54).
- Multiple canvas agents can see each other's work and act on the same objects, which lets them make local contributions without treating each run as an isolated prompt (10:55-11:20).
- For group tasks, one agent can become leader, scout the canvas, create a to-do list, delegate tasks to other agents, observe progress, and judge whether the result is complete and correct (11:20-12:32).
- Ruiz names common orchestration questions exposed by the canvas: how to give agents shared state, how to manage leader/follower roles, how to handle agents being effectively blind while working, and how to prevent overlapping work (11:54-12:11).

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Parallel coding-agent queues need focus-preserving review interfaces](parallel-coding-agent-queues-need-focus-preserving-review-interfaces.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)

Sources:
- [Agents on the Canvas in tldraw - Steve Ruiz, tldraw](../sources/20260501_sPUjIBH5Cwg.md), 09:54-12:32
