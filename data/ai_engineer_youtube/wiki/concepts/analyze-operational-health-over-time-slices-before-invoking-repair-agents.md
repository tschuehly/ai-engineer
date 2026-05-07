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

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Target enterprise coding agents at maintenance and incident work](target-enterprise-coding-agents-at-maintenance-and-incident-work.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)

Sources:
- [Infra that fixes itself, thanks to coding agents - Mahmoud Abdelwahab, Railway](../sources/20251124_Q5IVm_CxN2w.md), 03:11-06:06, 15:13-15:24
