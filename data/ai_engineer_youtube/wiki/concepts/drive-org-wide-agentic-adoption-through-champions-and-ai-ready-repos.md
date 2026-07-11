# Drive Org-Wide Agentic Adoption Through Champions and AI-Ready Repos

Summary: Instead of trying to level up every engineer, form a hand-picked ~1% champion cohort from the most critical repos and have them embed AI assets into the shared repos, so agent delegation becomes native for the whole org rather than trapped in a few power users' habits.

Use when:
- Rolling out agentic engineering across a large org where per-individual upskilling will not scale.
- Deciding where to concentrate scarce AI-enablement effort for broad, not local, impact.

Details:
- Leverage rationale (1-9-90 rule, "1990 rule"): in digital communities ~1% create, 9% interact, 90% consume, and adoption of AI maps almost perfectly — "if my AI strategy depends on every individual leveling themselves up, I'm never going to see that broad impact." So invest in forming the 1% power users from the most critical teams. (04:52-05:40)
- Champions selection is strategic, not a volunteer call: ~50 hand-picked engineers who could dedicate ≥30% of their time and wouldn't quit on non-deterministic AI when it "didn't work out of the box, which it often did not." Deliberately drawn from every corner (Square, Cash App, Afterpay, Tidal; front-end, back-end, mobile, data, infra) and every repo shape (legacy monorepos, small services, mobile apps) to pressure-test patterns and "quickly see what actually scales." (05:40-06:50, 07:50-08:20)
- The leverage point is the *repo*, because it is the central reference for every contributor: make repos AI-ready so "not only would the agents perform better but the entire team would benefit, not just the 1%." This directly addresses the trust gap — around June 2025 models could write a feature but the code often didn't conform to team conventions, so engineers didn't yet trust agents enough to delegate. (07:06-07:50)
- Standard AI-ready components, customized per team: context files (`AGENTS.md` / `CLAUDE.md`) for repo guidance; rules files as guardrails; repeatable workflows (slash commands, later agent skills); an enabled AI code reviewer with instructions on what matters; and AI attribution on PRs. Monorepos used inheritance — shared contexts/rules at the root, service-specific ones layered below; web and mobile (Android/iOS) needed different approaches. (08:20-09:39)
- Bottom-up beats top-down mandate: each champion decided what worked for their repo, teams with similar shapes converged naturally on the same tools and patterns, and engineers "loved" choosing over being pushed — countering the "AI or die" leadership pressure that was causing fatigue and turn-off. (04:40-04:52, 08:44-09:20)
- The payoff is that later delegation (assigning Jira/Linear/GitHub/Slack requests to an agent) "felt native to how people already work" and required no new skill from the 90%, because the champions had already laid the repo foundation the agents work against. (10:00-12:20)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [On Mixed-Ability AI Teams, Specialists Should Enable Not Do](on-mixed-ability-ai-teams-specialists-should-enable-not-do.md)
- [Institutionalize Knowledge Infrastructure for AI Adoption](institutionalize-knowledge-infrastructure-for-ai-adoption.md)
- [Use Repository Instructions to Ground Coding Agents](use-repository-instructions-to-ground-coding-agents.md)
- [Create Psychological Safety for AI Adoption](create-psychological-safety-for-ai-adoption.md)

Sources:
- [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](../sources/20260628_whue9_YquGA.md), 04:40-12:20
