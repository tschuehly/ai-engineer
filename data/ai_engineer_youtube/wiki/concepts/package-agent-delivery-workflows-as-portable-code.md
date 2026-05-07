# Package Agent Delivery Workflows as Portable Code

Summary: Agent delivery workflows become more repeatable when the build, test, environment, and LLM steps are encoded as portable code that runs the same locally, in CI, or on cloud infrastructure.

Use when:
- Designing coding-agent workflows that must work both on a developer laptop and in GitHub Actions.
- Turning containerized build/test steps into reusable tools for humans and agents.

Details:
- Dagger is framed as a container runtime and workflow engine for software engineering workflows; the same workflow can run on a laptop, Kubernetes, GitHub, or another CI environment, which makes agent work less dependent on one host setup. (05:34-06:03)
- The workshop treats LLMs as another Dagger component alongside containers, repositories, directories, and files, so model calls can be embedded into existing delivery workflows instead of living in a separate agent-only framework. (06:24-06:56)
- Dagger modules are written as ordinary code in languages such as Go, Python, TypeScript, Java, or PHP, with cross-language module interop and shared native bindings. (08:30-09:32)
- The demonstrated pipeline exposes build and test functions from code, then calls those same functions locally and from the agent workflow. (19:04-21:11)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Give Coding Agents the Same Engineering Infrastructure Humans Need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Run Eval Suites in CI/CD Before and During Production](run-eval-suites-in-cicd-before-and-during-production.md)

Sources:
- [Ship Agents that Ship: A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger](../sources/20250727_Fzb1a24hF-o.md), 05:34-21:11
