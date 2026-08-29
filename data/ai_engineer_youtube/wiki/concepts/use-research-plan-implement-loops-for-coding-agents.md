# Use research-plan-implement loops for coding agents

Summary: Coding-agent work should often move through explicit research, planning, and implementation phases instead of jumping from a feature request directly to generated code. The research and planning artifacts give the implementation agent a narrow, reviewed path and a clear validation strategy.

Use when:
- Starting a feature or fix where the codebase shape is not already obvious.
- Trying to reduce wrong assumptions before an agent writes a large diff.

Details:
- Jumping straight into implementation can produce lots of code from wrong assumptions, wasting time and reinforcing the belief that coding agents are unreliable. (11:36-12:50)
- The research phase should first understand how the system works today, which files are involved, which existing paradigms to mirror or avoid, how data flows, and which edge cases matter. (13:45-14:44)
- Research should produce an artifact the human can read and approve before planning begins, so the agent and human share the same understanding of the problem. (14:44-15:04)
- The plan should list files to create or change, verification commands or tests, and the expected system impact; code snippets can be included only when they clarify rather than overconstrain the implementation. (15:04-15:56)
- A reviewed plan can make implementation cheap enough for a smaller, faster, or cheaper model because the hard thinking has already happened in the research and planning phases. (15:56-16:10)
- Implementation can start in a fresh low-context session that receives only the plan, making changes easier to review and commit incrementally. (16:11-16:40)
- Nations frames the same loop as a way to prevent long conversational coding sessions from accumulating abandoned approaches, conflicting patterns, and dead code; the three outputs are research, plan, and implementation, each validated before proceeding. (10:32-13:47)
- For heavily tangled systems, the research phase may need a manually produced migration seed before agents can plan safely, because hidden invariants and service dependencies may only appear when a human changes the code and sees what breaks. (14:29-16:09)
- Frequent intentional compaction adds a context-management rationale for the same loop: research compresses codebase truth, planning compresses human intent, and implementation can start from a reviewed low-context plan rather than a noisy long conversation. (07:31-08:25, 14:10-14:56)
- The loop should scale with task complexity. Small edits may only need direct prompting, medium multi-repo features may need research plus a plan, and harder brownfield work needs more deliberate context compaction and human review. (17:48-18:29)
- **Four rules for the plan document itself, independent of whichever loop runs it.** Blum is explicit that the artifact and the process are separable: "once you have the plan, you can use whatever loop you want or whatever workflow you want in order to implement it." The rules are a "why" at the top the agent may not rewrite, phases sized to a PR the author would review in one sitting, a validation gate or exit criterion on every phase so later work never rests on unvalidated earlier work, and enough detail per phase to hand it to a subagent that will see nothing else. Where this page specifies what the workflow passes through, those specify what the document must contain for an unattended run to survive. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 08:38-10:26)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Use PRDs to align agents on the design concept](use-prds-to-align-agents-on-the-design-concept.md)
- [Limit agent change size by feedback speed](limit-agent-change-size-by-feedback-speed.md)
- [Long AI coding conversations compound accidental complexity](long-ai-coding-conversations-compound-accidental-complexity.md)
- [Manual migration seeds teach agents the hidden constraints](manual-migration-seeds-teach-agents-the-hidden-constraints.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Review research and plans before they multiply into code](review-research-and-plans-before-they-multiply-into-code.md)
- [Structure an Agent Plan With a Frozen Why and Reviewer-Sized Phases](structure-an-agent-plan-with-a-frozen-why-and-reviewer-sized-phases.md)

Sources:
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md), 11:36-16:40
- [The Infinite Software Crisis - Jake Nations, Netflix](../sources/20251220_eIoohUmYpGI.md), 10:32-16:09
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md), 07:31-08:25, 14:10-18:29
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 08:38-10:26
