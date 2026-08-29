# Keep a Living Intent Graph That Agents Read but Cannot Write

Summary: Separate the artifact that records what the organization has decided — constraints, decisions, and who owns them — from the artifact that accumulates practice. Make the first a graph that every agent and human reads, that no agent may modify without a human approving the specific change, and that propagates an approved change to everyone bound by the old one.

Use when:
- Agents and humans are both acting against a set of engineering constraints that must not silently move.
- Deciding which parts of an organization's context an agent should be allowed to write back to.
- Designing a change-proposal path that an agent can initiate but not conclude.

Details:
- **The artifact and its write rule, stated together.** "Instead of having scattered knowledge or scattered intent all over the place, we build a living graph. We call it the system of intent. And this living graph actually has all the constraints of the system, has all the decisions over there. It keeps evolving. And as an AI person actually, we don't allow the agents to touch it except with human in the loop approval for specific changes. And this thing is like the Bible of the whole system." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 05:46-06:19)
- **The layer beside it is deliberately not write-gated.** The "tribal knowledge layer" is "a memory that keeps evolving with day-to-day usage and the knowledge base that captures all the information and documents… keeps evolving from a project to project and keeping the best practice over there." The split is the design decision worth copying: constraints and decisions *bind* future work and get an approval step; accumulated practice compounds without one. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 06:19-06:36)
- **Three jobs the graph does in the demo, beyond storage.** (1) *Handoff*: a human signs off a simulation result and "the system of intent realizes, okay, this person is done with this. I'm going to notify the next stakeholders of what they should do." (2) *Violation detection*: "it realizes like there is something off, like some value out of constraints that shouldn't be there that might cost you $50 million actually to respin the whole chip, and it notified the system." (3) *Gated change*: a proposed modification means the graph "captures all the values over there, all the stakeholders… gathers all the shared knowledge, and then it fires a request… [that] goes to an architect or an owner of the system. The owner can approve or decline it." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 08:03-10:15)
- **The approval echo is the part most approval designs omit.** "The moment they approve that this is a valid change, it actually goes and echoes in the whole system. Like everyone will know that this decision has been made. There is that change that advises everything over there." An approval that only unblocks the requester leaves every other holder of the old value stale — see the drift failure this system was built against. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 09:52-10:15)
- **What makes the request routable is that the graph knows the stakeholders.** Because constraints and their dependents are edges rather than prose, the system can name both the approver and the notification set without a human deciding who to CC. This is the concrete payoff of choosing a graph over a document.
- **The unclosed question is enforcement.** "We don't allow the agents to touch it" describes a policy, and the same talk reports that a policy stated to an agent did not hold for spec files until enforcement moved to the operating system. Whether the graph's write path is blocked at the substrate or asserted in a prompt is not said. Treat the write-gate as designed rather than demonstrated. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 05:46-06:19, 13:36-15:11)
- Everything on this page is a pre-release product walkthrough: alpha with development partners, beta open, release stated as October 2026, and each sequence shown once with prepared data. No rates for correct routing, false constraint violations, or approval latency are given.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Truth Drift Updates One Copy and Leaves the Rest Stale](truth-drift-updates-one-copy-and-leaves-the-rest-stale.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Product Work Graphs Coordinate Agents and Humans](product-work-graphs-coordinate-agents-and-humans.md)
- [Knowledge Graphs Make Agent Memory Traversable And Explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Keep spec artifacts feature-scoped, mutable, and context-backed](keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md)
- [Alignment Is the Quadratic Term That Per-Person Tooling Does Not Touch](alignment-is-the-quadratic-term-that-per-person-tooling-does-not-touch.md)
- [Institutional Memory Has No Benchmark the Way Graph Memory Does](institutional-memory-has-no-benchmark-the-way-graph-memory-does.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)
- [Scope Role Agents With a Spec Hierarchy and File Isolation](scope-role-agents-with-a-spec-hierarchy-and-file-isolation.md)

Sources:
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 05:46-06:36, 08:03-10:15
