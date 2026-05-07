# Model-Shaped Codebase Architecture for Coding Agents

Summary: Coding agents get more useful when codebases are shaped around model strengths: small modules, fast tests, and clear architecture. This resembles good software engineering, but AI makes the payoff more direct because agents can repeatedly fill in details and run checks.

Use when:
- Preparing a repository for Codex-style or other coding-agent workflows.
- Deciding whether a codebase should be decomposed before asking agents to make broad changes.

Details:
- Brockman argues that codebase structure determines how much value teams get from Codex-style agents. 26:37-26:45
- Existing codebases are often matched to human strengths; models can handle broad surface diversity but have weaker deep conceptual connection, so they benefit from smaller, well-tested modules. 26:49-27:14
- Fast tests are a model-facing affordance because an agent may rerun the same checks many times while filling in details. 27:12-27:21
- The human role shifts toward architecture and component boundaries, while the model fills implementation details inside those boundaries. 27:21-27:35

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)

Sources:
- [#define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)](../sources/20250810_avWhreBUYF0.md), 26:37-27:52
