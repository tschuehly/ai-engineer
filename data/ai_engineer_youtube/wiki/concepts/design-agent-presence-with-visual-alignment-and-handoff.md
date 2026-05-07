# Design agent presence with visual alignment and handoff

Summary: Agents that act inside a work surface need visible presence, intermediate alignment checks, rollback points, and graceful handoff when they cannot continue. This makes agent work feel collaborative instead of hidden or noisy.

Use when:
- Designing UX for agents that transform data, documents, or other user-owned artifacts.
- Deciding what an agent should show while it is acting, checking, failing, or returning control.

Details:
- A wall of explanatory text after an agent completes useful code work can still get in the way; the talk frames this as a tool-UX problem, not only a capability problem. (09:11-09:43)
- The suggested interaction pattern mirrors careful human coworker collaboration: communicate visually, choose words carefully, stop to check whether the work is right, and keep the user oriented. (09:46-10:06)
- In the data-transformation prototype, the agent visually described the operation, asked whether it was correct, recorded alignment through a snapshot, allowed rollback, and told the user what could happen next. (10:06-10:20)
- The agent could express failure and then back off by handing control to the user, which the talk presents as a better fit than pressing forward after a wrong move. (10:20-10:45)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)

Sources:
- [Form factors for your new AI coworkers - Craig Wattrus, Flatfile](../sources/20250822_CiMVKnX-CNI.md), 09:11-10:45
