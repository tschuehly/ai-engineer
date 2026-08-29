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

- **On a team, the artifact's second job is to be findable from wherever the reader is.** Superconductor treats screenshots and videos as the medium through which agent work becomes visible across surfaces: "it doesn't matter where the work started or where it's finishing, the agent can show you the work it's doing as screenshot or video or other. And you can see it from everywhere… you don't have to worry about like, 'Oh, where is that thing? I got to go to GitHub to see the image or got to go to Slack to see the image.'" The enabling design is that the artifact belongs to the session rather than to the tool that produced it ([make one agent session reachable from every interface](make-one-agent-session-reachable-from-every-interface.md)). It is also what closes the loop for a non-engineer who triggered the work: the reported flow is that they ask for a fix in Slack, "screenshots are shown," and an engineer merges — so the artifact is doing verification for someone with no way to run the code. ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 05:09-05:31, 12:26-12:45)
- **The artifact as the thing that travels with a pull request.** Anthropic ships Claude Code artifacts and uses them internally in place of the raw diff — "here's the explanation. Here's the intention of the change. Here's the trade-offs that were made" — which is this page's reviewable-object idea applied at the one point where review actually blocks delivery. The stated reason it works is a division of labour rather than a preference: code is machine-verifiable, intent and tradeoffs are not, so the artifact carries the part a human must judge. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 10:30-11:08)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)
- [Agent managers orchestrate editor, browser, and background agents](agent-managers-orchestrate-editor-browser-and-background-agents.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [The Review Bottleneck Is Comprehension, Not Reviewer Time](the-review-bottleneck-is-comprehension-not-reviewer-time.md)

Sources:
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md), 12:48-19:20
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 05:09-05:31, 12:26-12:45
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:30-11:08
