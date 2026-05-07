# Dynamic Artifacts Make Agent Work Reviewable and Reusable

Summary: Dynamic artifacts turn agent work from a raw token stream into reviewable objects such as plans, task lists, diagrams, screenshots, recordings, walkthroughs, mockups, comments, and memory records. They let agents communicate progress, ask targeted questions, receive batched feedback, and preserve derived knowledge for future runs.

Use when:
- Designing review and collaboration surfaces for long-running agents.
- Choosing how agents should represent plans, evidence, visual work, open questions, and reusable findings.

Details:
- Antigravity defines an artifact as something the agent generates that dynamically represents information for the user's use case. 12:48-13:07
- Artifacts can support agent self-organization, user communication, subagent coordination, cross-conversation handoff, and memory. 13:07-13:36
- The reason to use artifacts is reviewability: a visual or structured representation is easier to inspect than a long conversation or chain-of-thought-like stream of text. 13:39-14:41
- Common artifact types include Markdown plans and walkthroughs, task lists, architecture diagrams, images, screen recordings, and Mermaid diagrams; the model can decide when an artifact is needed and which representation fits the task. 14:43-16:44
- Plans can surface open questions before execution, and the agent can auto-continue when there are no blocking questions instead of waiting unnecessarily. 15:07-15:54
- Final walkthroughs act like PR descriptions by explaining how the agent proves it did the right thing, often with screenshots or recordings. 16:10-16:30
- Artifacts can be stored as memory when the agent derives reusable knowledge, such as API schemas learned through documentation plus live `curl` exploration. 16:49-17:35
- Commenting on text or image artifacts gives the user a Google Docs/GitHub/Figma-like feedback surface that the agent can incorporate during execution without forcing the whole loop to stop. 17:37-19:20

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)
- [Agent managers orchestrate editor, browser, and background agents](agent-managers-orchestrate-editor-browser-and-background-agents.md)

Sources:
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md), 12:48-19:20
