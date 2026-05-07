# Give Coding Agents the Same Engineering Infrastructure Humans Need

Summary: Coding agents need the same production engineering substrate as human developers: standards, reproducible environments, fast tests, boundaries, and clear tasks. Weak developer infrastructure becomes weak agent infrastructure.

Use when:
- Preparing a repository or team workflow for agentic coding.
- Diagnosing why coding agents fail in a messy production codebase.

Details:
- Document current standards and practices, including which packages, patterns, or directions the codebase should use while it is in flux. (09:14-09:36)
- Make development environments reproducible rather than bespoke so agents and humans can run the project without hidden local setup. (09:36-09:47)
- Keep tests easy, fast, and locally runnable so an agent can iterate through the same feedback loop a human engineer would use. (09:47-09:53)
- Define task boundaries explicitly; broad architecture phrases such as "extract this module using the strangler pattern" still need concrete scope and instructions before an agent can execute safely. (09:55-10:11)
- Give agents clearly defined work instead of vague requests, just as a team would not ask an engineer to "make this button do something different" without intent and constraints. (10:11-10:28)
- Treat tests, linters, version control, and deployment practices as part of the agent harness because agents are writing code inside the same engineering system. (10:30-11:18)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Model-shaped codebase architecture for coding agents](model-shaped-codebase-architecture-for-coding-agents.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)

Sources:
- [Vibes won't cut it - Chris Kelly, Augment Code](../sources/20250803_Dc3qOA9WOnE.md), 09:14-11:18
