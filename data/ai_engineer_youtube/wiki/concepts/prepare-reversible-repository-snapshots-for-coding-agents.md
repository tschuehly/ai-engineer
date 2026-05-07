# Prepare Reversible Repository Snapshots for Coding Agents

Summary: Coding agents need prepared, reversible repository environments before they can produce reliable changes. Clean remote VM snapshots let an agent start from a known setup, run checks, reload state, and roll back when needed.

Use when:
- Building infrastructure for asynchronous or remote coding agents.
- Debugging why an agent can edit code but cannot validate or recover from failed setup.

Details:
- Isolated bug and feature work still requires the agent to set up the repository, run lint, run CI, and perform basic checks that the change works.
- Wu describes building the ability to set up a repository ahead of time and create a snapshot the agent can start from, reload, or roll back.
- A clean remote VM can run CI, linters, and related validation without depending on an ad hoc local human environment.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Branchable Cloud Workspaces Make Agent Actions Reversible](branchable-cloud-workspaces-make-agent-actions-reversible.md)
- [Give coding agents the same engineering infrastructure humans need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Prepare Copilot Coding Agent Environments With Setup Steps](prepare-copilot-coding-agent-environments-with-setup-steps.md)

Sources:
- [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](../sources/20250725_MI83buT_23o.md), 07:13-08:05
