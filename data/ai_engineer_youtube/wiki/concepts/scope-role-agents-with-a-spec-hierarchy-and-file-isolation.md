# Scope Role Agents With a Spec Hierarchy and File Isolation

Summary: Specialist agents authored for distinct roles will still wander into each other's work, because a role is a description and not a boundary. Giving each agent a scoped slice of a spec hierarchy and isolating the files it can touch converts the role from a prompt into a constraint the agent cannot narrate its way past.

Use when:
- Running several role-specific agents over one shared repository or design database.
- An agent that should own one discipline keeps producing work that belongs to another.
- Deciding whether "you are the X agent" in a system prompt is sufficient scoping.

Details:
- **The design choice being scoped.** Instead of "this general coding agent that everyone uses today," each engineer gets a role agent "developed by subject matter experts to help the engineers doing their work… for example, like we have digital design agent, analog design agent, and so on," surfaced as "a role-based AI teammate specific to their role." ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 06:36-07:02, 07:32-07:45)
- **The failure that specialization alone did not prevent.** "In early design phases of the system, we found that an analog agent that's specifically for analog design actually overstepping and doing RTL agent work. Which wasn't really great. Even we tried to enforce it, but it was a difficult problem." The important clause is the last one: enforcement was attempted at the instruction level and did not hold. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 12:49-13:14)
- **The principle they moved to.** "We have a spec hierarchy with agent scope and file isolation to allow them only to work on this specific task or specific domain. That solves our problem of agents stepping on each other." Two mechanisms are named: the specs are hierarchical so a role's authority has a level, and the file surface is isolated so the authority is enforceable. ([What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 14:00-14:25)
- **Why role prompts leak.** A specialist has enough general capability to recognize adjacent work and enough context to attempt it, and nothing in its input distinguishes "outside my remit" from "a step my task needs." The constraint has to live in what the agent can reach, which is the same argument the same talk makes for blocking spec writes at the operating system rather than by tool.
- **Cost of the fix, stated honestly by its absence in the source.** Nothing is said about the tasks that legitimately cross disciplines, how a role agent requests work outside its slice, or how the hierarchy is authored and kept current. In this system the crossing path is presumably the human-approved change request on the intent graph, but the talk does not connect them.
- **This is the missing failure mode on the case for domain-specific agents.** The wiki's existing argument for specialists is efficiency plus tighter permissions — a narrow agent "can only do the things that are already explicitly approved for them to do." That framing assumes the permission scoping exists; this source is the report of what happens when the specialization is real and the scoping is only described. No overstep rate is given, before or after.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Security](../topics/security.md)

Related concepts:
- [Domain-specific agents unlock small models and tight permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Evaluate workspace isolation with positive and negative filesystem scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)
- [Keep spec artifacts feature-scoped, mutable, and context-backed](keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md)
- [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md)
- [Grade the Alignment, Not the Agents](grade-the-alignment-not-the-agents.md)
- [Truth Drift Updates One Copy and Leaves the Rest Stale](truth-drift-updates-one-copy-and-leaves-the-rest-stale.md)

Sources:
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 06:36-07:45, 12:49-13:14, 14:00-14:25
