# Target Enterprise Coding Agents at Maintenance and Incident Work

Summary: In mature engineering organizations, agent ROI may be stronger when agents attack maintenance, migration, patching, and incident-response work than when they only generate new code from requirements.

Use when:
- Choosing first scaled enterprise coding-agent use cases.
- Comparing greenfield code generation against maintenance, migration, and operational troubleshooting agents.

Details:
- Bloomberg reframed AI for coding from narrow code generation toward broader software engineering work, including maintenance and migration tasks developers often prefer not to do. (06:18-06:45)
- Uplift agents scan the codebase for places a patch applies, create pull requests with the fix, and explain why the patch was made, improving on earlier regex-based refactoring tools. (06:48-07:38)
- Uplift work still needs deterministic verification; without tests, linters, or other checks, generated patches can be difficult to trust and apply. (07:40-08:05)
- Incident-response agents can inspect code, telemetry, feature flags, traces, metrics, logs, topologies, alarms, triggers, and SLOs quickly, while reducing human anchoring on a first hypothesis. (08:37-10:37)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Decompose large refactors into dependency-aware agent batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)

Sources:
- [What We Learned Deploying AI within Bloomberg's Engineering Organization - Lei Zhang, Bloomberg](../sources/20251216_Q81AzlA-VE8.md), 06:18-10:37
