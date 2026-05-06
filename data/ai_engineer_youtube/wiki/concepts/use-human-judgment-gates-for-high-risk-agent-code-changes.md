# Use Human Judgment Gates for High-Risk Agent Code Changes

Summary: Agent workflows should separate mechanically fixable review feedback from changes where human judgment is non-negotiable. Database migrations, permission changes, dependencies, architecture, and reliability work need deliberate friction because the relevant production context is often under-documented or outside the agent's local checks.

Use when:
- Defining approval gates for coding agents or review tools.
- Deciding which code changes can be auto-fixed and which must wake up a human reviewer.

Details:
- The speakers describe building a review extension that separates mechanical bugs, which can be routed back to the agent, from callouts where the human brain should reactivate. (14:28-14:47)
- Database migrations should not ship without human judgment because lock behavior and production data size can determine whether a technically valid migration is safe. (14:48-14:57)
- Permissioning changes and dependency additions are examples where the agent may lack under-documented context, such as security consequences, maintainer trust, or whether the dependency belongs in the codebase. (14:57-15:45)
- Agents can help reproduce customer issues and explore product directions, but system architecture and reliability remain slower human-led work because agent speed can create months of technical debt in weeks or days. (16:01-17:24)
- Friction is not only waste; SLOs are cited as an example of intentional process friction that forces teams to ask whether a service needs reliability, criticality, and staffing before taking on the operational burden. (17:24-18:16)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use decision logs to keep uncertain agents moving](use-decision-logs-to-keep-uncertain-agents-moving.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)

Sources:
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md), 14:28-18:16
