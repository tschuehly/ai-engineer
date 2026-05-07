# Prepare Copilot Coding Agent Environments With Setup Steps

Summary: Copilot Coding Agent needs a prepared execution environment, not only a good issue. A `copilot setup steps` GitHub Actions workflow can install dependencies, services, frameworks, and scripts so the background agent can build, test, and repair inside a realistic workspace.

Use when:
- Configuring a repository for asynchronous Copilot Coding Agent work.
- Debugging why a background coding agent cannot reproduce local build or test behavior.

Details:
- The workshop says Copilot Coding Agent works behind the scenes through GitHub Actions. 33:51-34:00
- A special `copilot setup steps` action can install the libraries, frameworks, services, and scripts required before the agent starts implementing. 34:00-34:23
- The setup workflow becomes part of the agent's working environment, alongside the issue, instructions file, and repository structure. 34:23-35:43
- Local agent mode and background coding-agent work both depend on executable feedback: builds, tests, and failure recovery are key parts of how the agent validates its changes. 11:42-12:10

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)
- [Treat agent readiness as verification infrastructure](treat-agent-readiness-as-verification-infrastructure.md)
- [Package Agent Delivery Workflows as Portable Code](package-agent-delivery-workflows-as-portable-code.md)

Sources:
- [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](../sources/20250726_DdaAABdAqZY.md), 11:42-12:10, 33:51-35:43
