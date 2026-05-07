# Observability-to-PR Agents Turn Incidents Into Reviewable Fixes

Summary: Infrastructure repair agents can convert operational evidence into a reviewed code change by chaining monitoring, context gathering, planning, coding-agent execution, and pull-request creation. The useful handoff is not an autonomous production mutation; it is a PR with evidence, root-cause notes, and a human merge decision.

Use when:
- Designing an agent that responds to production health signals.
- Deciding how far an infrastructure repair workflow should automate before human review.

Details:
- Railway Autofix monitors application infrastructure, detects issues from metrics and thresholds, and aims to move from issue detection on Railway to an open GitHub pull request, 02:33-03:00, 03:11-03:24.
- The workflow first gathers project architecture, service resource metrics, HTTP metrics, threshold breaches, and affected services before asking an agent to write a fix, 03:11-04:17.
- After service context is gathered, the system writes a detailed plan that includes architecture, affected services, failure signals, and debugging recommendations, then passes that plan to a coding agent that clones the repo, creates todos, implements fixes, and opens a PR, 06:06-06:55.
- The demo's successful output is a pull request with a summary, analysis, root causes, and fixed changes so a human can review and merge, 17:24-17:47.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)

Sources:
- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md), 02:33-06:55, 17:24-17:47
