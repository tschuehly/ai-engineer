# Analyze Operational Health Over Time Slices Before Invoking Repair Agents

Summary: Repair agents should receive a time-windowed operational picture instead of a single threshold breach. A slice of architecture, metrics, logs, and external dependency context helps separate real incidents from noisy spikes, legitimate high usage, and upstream outages.

Use when:
- Building monitors that decide whether to invoke a coding or remediation agent.
- Reducing false positives from alert thresholds before agentic repair work begins.

Details:
- The talk argues for scheduled health analysis over pure alert webhooks because a single CPU or memory threshold breach can be noisy under spiky workloads, 04:19-05:06.
- The monitor workflow fetches architecture, CPU and memory utilization, HTTP error rates, failed request counts, latency, and affected services so the agent sees a broader project-health picture, 03:11-04:17.
- Additional context can include service logs, build logs, deployment logs, repository-derived upstream providers, and upstream status pages; this lets the system recommend waiting when the failure belongs to an external provider, 05:06-06:06, 15:13-15:24.
- Resource use alone is not sufficient evidence of a defect: high utilization with clean logs can mean successful high traffic rather than a code issue, 05:24-05:39.
- **A second source pushes the same reasoning past the window into the signal set.** This page widens the *time* slice so a spike is not mistaken for an incident; Resolve AI argues the *selection* should also vary, because standard checks "are good baselines, but it's not exhaustive based on the type of changes that are going in. There's certain signals you'd want to watch or not want to watch. And so, every rollout is a bit unique." The proposal is to read the change and derive which telemetry would expose trouble for it, then follow the causal chain outward — see [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 14:20-14:35, 17:57-19:10)
- **The same source separates the retrieval from the verdict.** Gathering a broader picture is execution; deciding it is abnormal is a different capability: "it's one thing to go check a dashboard. It's another thing to say that metric smells off… It's the production context that's going to say, this feels wrong." Widening the slice raises the ceiling on what a judgment could use, but does not supply the judgment. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 10:37-11:12)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Target enterprise coding agents at maintenance and incident work](target-enterprise-coding-agents-at-maintenance-and-incident-work.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Derive the Post-Deploy Check Plan From What Actually Changed](derive-the-post-deploy-check-plan-from-what-changed.md)
- [Separate Execution From the Production Context That Judges It](separate-execution-from-the-production-context-that-judges-it.md)

Sources:
- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md), 03:11-06:06, 15:13-15:24
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 10:37-11:12, 14:20-14:35, 17:57-19:10
