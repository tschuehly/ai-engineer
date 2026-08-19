# Keep spec artifacts feature-scoped, mutable, and context-backed

Summary: Specs should be scoped to feature or problem areas, amended when current work changes them, and pruned when they no longer provide useful future context. They should also be backed by the right external context and steering guidance instead of becoming one massive stale plan.

Use when:
- Maintaining spec folders or planning artifacts for repeated coding-agent work.
- Deciding whether a new request should update an existing spec, create a cross-functional spec, or delete stale planning context.

Details:
- The Kiro team treats specs as feature or problem-area artifacts rather than one project-wide document; examples include telemetry, prompt registry, AGENTS.md support, and message-history sanitization. (48:49-49:54)
- Some specs are pruned or deleted when they are unlikely to be revisited, while still-relevant specs can be read and amended with new requirements instead of appending an endless sequence of new specs. (48:57-49:49, 53:32-53:53)
- For cross-cutting concerns such as API, security, and PII logging changes, the operator should decide whether to place requirements in one existing spec or create a cross-functional spec. (54:36-55:24)
- MCP servers can provide context during requirements generation, design, or implementation; examples include task trackers, fetch/search tools, and an AWS documentation MCP server. (08:33-15:15, 53:04-53:26)
- Steering files encode durable preferences such as latency, cost, commit attribution, code style, and coverage expectations, influencing both design and generated code. (01:01:34-01:03:05)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Retire completed planning docs before they become agent doc rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)
- [Fresh Markdown context mitigates model rot in codegen](fresh-markdown-context-mitigates-model-rot-in-codegen.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Spec-Driven Development Without a Feedback Loop Is Waterfall](spec-driven-development-without-a-feedback-loop-is-waterfall.md)

Sources:
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md), 08:33-15:15, 48:49-55:24, 01:01:34-01:03:05

