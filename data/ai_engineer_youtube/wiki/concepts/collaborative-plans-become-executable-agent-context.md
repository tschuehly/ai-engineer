# Collaborative Plans Become Executable Agent Context

Summary: Agent-written plans become more reliable when teammates can inspect and edit them together before execution. The plan and surrounding discussion then become shared prompt context for the agent instead of a private local plan hidden in one developer's terminal.

Use when:
- Designing plan-mode workflows for coding agents.
- Preventing private agent plans from bypassing team review.

Details:
- The talk criticizes local plan modes that are unshared with the team, because teams may never evaluate whether an agent's plan is good before it is implemented. 04:24-04:38
- ACE demonstrates an agent-written plan that teammates open together, edit collaboratively, and evaluate against their intent before asking the agent to implement it. 12:18-13:07
- Teammates can revise requirements and interface choices inside the plan, and the agent can use the edited plan plus session conversation as execution context. 12:39-13:07
- The workflow treats planning and building as a cycle rather than separate phases, keeping alignment alongside implementation instead of after it. 05:38-05:57

- Matt Dailey (Ref) adds a sequencing rule and an argument for it that is about cost of reversal rather than plan quality: "share a plan… don't just write the plan, give it to your agent, and have them implement it. Give it to someone on your team." He concedes it "feel[s] like very unnatural for a lot of people. We… think we know what's going on," and justifies it twice — teammates "have great context in their heads," and realignment is cheap "before someone has spent even a day in AI going deep on some idea building a prototype." The plan goes to a human first and the agent second. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 16:38-16:54, 19:33-19:56)
- **The same workflow demonstrated again, with the invocation reduced to two words and the destination named.** Gazit's plan for adding selectable time frames arrives as Markdown that "is not just for me to look at and edit, it's for us to look at and edit together"; his teammate adds an "all time" option while he removes "today," and the run resumes with "we've updated the plan, do it." The generalization he draws is stronger than plan mode: "in order to change something about my application, I'm going to edit a document, and I'm going to tell AI, 'Hey, make the document true.' So this shared document editing is not just a nice to have. Maybe this is actually sort of the interface that we like to work in." That lands the pattern on the same position the wiki files as [make the doc the state and the agent the action](make-the-doc-the-state-and-the-agent-the-action.md), and inherits its unresolved ownership problem: nothing here says who retires a plan once it is true. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 17:12-18:24)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Make the Doc the State and the Agent the Action](make-the-doc-the-state-and-the-agent-the-action.md)
- [Unimplemented Plans Signal a Working Decision Layer](unimplemented-plans-signal-a-working-decision-layer.md)
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)

Sources:
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](../sources/20260426_ClWD8OEYgp8.md), 04:24-05:57, 12:18-13:07
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 16:38-16:54, 19:33-19:56
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 17:12-18:24
