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

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Enterprise Coding Agents Need Ownership, Auditability, and Action Controls](enterprise-coding-agents-need-ownership-auditability-and-action-controls.md)
- [First-Class Agent Users Need Identity, Scopes, and Audit Trails](first-class-agent-users-need-identity-scopes-and-audit-trails.md)
- [AI code quality needs full-SDLC workflows](ai-code-quality-needs-full-sdlc-workflows.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 10:34-12:09
