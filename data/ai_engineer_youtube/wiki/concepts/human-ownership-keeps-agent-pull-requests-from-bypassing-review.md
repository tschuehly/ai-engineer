# Human Ownership Keeps Agent Pull Requests From Bypassing Review

Summary: Agent-created pull requests need an accountable human owner and normal review routing. If the bot appears as the owner, review systems can either let the triggering human self-approve or leave the change without a person responsible for failures and follow-up.

Use when:
- Designing GitHub or GitLab integration for coding agents.
- Deciding how agent-authored changes should appear in review queues.
- Preventing agent PRs from bypassing ordinary review and ownership norms.

Details:
- OpenHands initially opened pull requests under the agent identity, which allowed the human who triggered the run to approve the PR and bypass a second-human review path. (11:32-11:55)
- Agent-owned PRs could also languish because no person clearly owned failing unit tests or final cleanup after the bot produced the branch. (11:57-12:09)
- A reviewable agent workflow should attach the work to the responsible human or team while preserving that an agent generated the diff, so accountability and auditability do not disappear behind a bot account. (11:32-12:09)
- This ownership gate complements, rather than replaces, code review: Brennan separately warns that automatically merging agent output can create duplicate code and technical debt quickly. (10:34-11:15)

- Ownership in this page's sense is accountability routing — whose name is on the PR, who owns the failing test. Matt Dailey (Ref) names a loss upstream of that, which correct routing does not prevent: "if you as an engineer are letting an agent make a critical decision, you are [ceding] control of your code. You are no longer the owner of that code. The agent is," and at team scale "you no longer own the product." A change can be routed to exactly the right accountable human and still be a change whose every real decision the model made. Both controls are needed, and they fail independently. ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43, 17:10-17:27)

- **A team can run at near-total agent authorship and still hold the gate, if the gate is stated as a rule rather than a norm.** Superconductor reports "99.9% of our PRs are heavily agent generated" alongside "everything's human reviewed," and the review gate survives the widening of who may originate work: a support person's request goes through the agent, but "engineer gets it, gets merged." The mechanism that makes ownership legible there is a session participant roster rather than a PR field — "I can see who's getting notified about this session, who's seen it" — which answers the reviewer's actual question about non-engineer-originated work, "has this been vetted by an engineer or not?" ([make one agent session reachable from every interface](make-one-agent-session-reachable-from-every-interface.md)). The cost is unpriced: every additional origination channel lands on the same finite human review capacity, and no rework or throughput figure is given. ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 04:21-04:48, 12:26-12:45, 16:00-16:16)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise Coding Agents Need Ownership, Auditability, and Action Controls](enterprise-coding-agents-need-ownership-auditability-and-action-controls.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [AI code quality needs full-SDLC workflows](ai-code-quality-needs-full-sdlc-workflows.md)
- [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 10:34-12:09
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 03:16-03:43, 17:10-17:27
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 04:21-04:48, 12:26-12:45, 16:00-16:16
