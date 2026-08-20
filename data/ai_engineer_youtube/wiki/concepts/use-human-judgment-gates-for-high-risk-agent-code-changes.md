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

- **The vendor version of this gate is a time-based autonomy ramp, and it lacks the criterion this page supplies.** Sonar's review agent defaults to the low-autonomy end — "they'll just find the issues and show them to you and enter a dialogue with you so you can have those issues fixed" — and escalates from there: "we'd want to earn that trust. It doesn't happen that way by default usually. But as you use it more and more and gain confidence, you can turn on more and more features and completely automate the PR review workflow if you like." The default is the right one, but "as you use it more and more and gain confidence" is elapsed usage, not evidence, and the endpoint is per-*workflow* rather than per-change. This page's split is the missing half: whatever autonomy level a team has earned in aggregate, migrations, permission changes, and dependency additions are where the under-documented production context lives, so they are the wrong changes to include in the ramp. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 14:31-14:49)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use decision logs to keep uncertain agents moving](use-decision-logs-to-keep-uncertain-agents-moving.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)

Sources:
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md), 14:28-18:16
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 14:31-14:49
