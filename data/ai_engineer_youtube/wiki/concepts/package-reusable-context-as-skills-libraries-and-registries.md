# Package Reusable Context as Skills, Libraries, and Registries

Summary: Reusable context can be distributed like software libraries: packaged, versioned, discovered through registries, and installed per project. This makes context scalable across teams, but introduces quality, dependency, versioning, and supply-chain concerns.

Use when:
- Sharing agent instructions, skills, or workflow rules across repositories, teams, or an organization.
- Reviewing whether a third-party skill or context package is trustworthy enough to install.

Details:
- Checking context into a repository gives local sharing with low friction, but broader reuse needs package-like distribution across projects and teams (14:00-14:43).
- Registries make context packages discoverable, including skills and marketplace entries, but public skill quality may be low unless evaluated before adoption (14:48-15:29).
- Skills can contain context, scripts, documents, and potentially MCP-related assets, making them closer to a package format than a plain prompt snippet (15:49-16:13).
- Context packages can have dependencies and conflicts, such as frontend guidelines conflicting with React-specific context, so teams need versioning and dependency management for context as well as code (16:16-16:46).
- Context registries require security scanning and provenance metadata: who built the package, how it was built, and what model or sources contributed to it (16:48-17:40).
- Anthropic's skills talk reinforces the package-management direction for skills specifically: complex skills need evals, version lineage, and explicit dependencies on other skills, MCP servers, packages, or runtime capabilities. 10:38-11:57
- **The retrieval path a skills catalog owes, listed.** Touil's centralized-platform requirements name what the registry has to provide beyond storage: metadata that makes skills searchable, "an MCP that's actually plugged to this catalog, search for the skill, and a CLI to pull the skills back to your either your IDE if you're locally, or to your sandbox in your factory," declared dependencies between skills, versioning and lifecycle so "the agents automatically capture that there is a latest version of the skill and pull it," access control ("if you don't know who is accessing what, that is a huge gap"), and evaluation and observability. ([Touil](../sources/20260828_M05vON8i0aI.md), 13:44-14:47) MCP for search plus CLI for install is the concrete shape of "distributed like software libraries" — asserted as a design, with nothing in the talk measured.

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Treat complex skills like software artifacts](treat-complex-skills-like-software-artifacts.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 14:00-17:40
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 10:38-11:57
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 13:44-14:47
