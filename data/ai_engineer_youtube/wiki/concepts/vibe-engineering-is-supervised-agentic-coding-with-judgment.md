# Vibe engineering is supervised agentic coding with judgment

Summary: Vibe engineering is agentic coding where the human uses engineering knowledge to steer, interrupt, contextualize, and judge the agent instead of blindly accepting generated code.

Use when:
- Distinguishing casual prompt-and-accept code generation from professional agentic coding.
- Deciding who should drive an AI coding workflow and what judgment they need.

Details:
- The talk contrasts casual vibe coding with "vibe engineering," where agents write much of the code but the human watches for suspicious choices and steers with domain and architecture knowledge. (08:31-09:03)
- LLMs can accelerate both good and bad abstractions: they can reach the right abstraction faster, but they can also reach the wrong abstraction faster. (05:04-05:16)
- Skilled use depends on a solid starting point: primitives, components, functions, patterns, and abstractions that the agent can reference. (09:56-10:07)
- The speaker argues that skeptical senior engineers can get high leverage from agentic coding because they can evaluate output, while handing the same tools to juniors without judgment is risky. (12:03-12:39)
- Model speed matters for supervision: a fast agent loop can keep the human "in the driver's seat" so they can stop, redirect, and continue while the work is still mentally active. (14:23-15:06)
- **Supervision concentrated at one handoff instead of distributed through the loop.** Garvin's billing demo runs unsupervised end to end — provision the account, choose the credit structure, generate usage, produce a draft invoice — and places the entire human contribution at the boundary: "testing and tweaking from there exactly what you wanted before bringing that into production." This is a legitimate variant of supervised agentic coding when the run is cheap and reversible and its output is a single inspectable artifact; it degrades badly when the artifact is large enough that reviewing it is the same work as writing it. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 15:41-16:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat coding agents as fast junior collaborators](treat-coding-agents-as-fast-junior-collaborators.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 05:04-15:06
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 15:41-16:24
