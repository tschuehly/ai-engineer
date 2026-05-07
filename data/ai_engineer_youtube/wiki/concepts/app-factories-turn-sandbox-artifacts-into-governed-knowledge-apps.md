# App Factories Turn Sandbox Artifacts Into Governed Knowledge Apps

Summary: A knowledge-app factory separates fast operator iteration from production deployment by taking sandbox definitions, templates, transformers, executors, and workflow pipelines and packaging them into governed applications for end users.

Use when:
- Many internal teams need similar AI document or workflow applications with different domain rules.
- Prototype-to-production work is slowed by access control, deployment, cluster selection, downstream integration, and cost controls.

Details:
- BlackRock's framework split the operator sandbox from an app factory; the sandbox handled prompt, extraction-template, model-strategy, run, transformer, and executor iteration, while the factory acted as a cloud-native operator that takes a definition and spins out an app. (07:01-08:29)
- The goal was to compress complex use-case delivery from months into days by reusing platform, data-ingestion, orchestration, transformation, and distribution components. (07:01-07:52)
- Production deployment still includes ordinary enterprise concerns such as app distribution and access control, plus AI-specific choices such as GPU versus burstable clusters, model-provider strategy, and cost controls. (05:55-06:55)
- End users should receive an end-to-end application for uploading documents, running extraction, and pushing results through the pipeline; they should not need to configure templates or downstream integrations themselves. (14:06-14:49)
- In regulated environments, the production factory should preserve human-in-the-loop review and ROI evaluation instead of assuming every successful prototype deserves full automation. (12:57-14:05)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Domain-expert Sandboxes Accelerate Knowledge-app Iteration](domain-expert-sandboxes-accelerate-knowledge-app-iteration.md)
- [Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context](build-internal-ai-engineering-platforms-when-off-the-shelf-tools-lack-enterprise-context.md)
- [Route High-impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock](../sources/20250823_08mH36_NVos.md), 05:55-14:49
