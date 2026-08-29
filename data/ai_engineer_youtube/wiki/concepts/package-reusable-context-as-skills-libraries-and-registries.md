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
- **Authored by the API vendor, shipped to the customer's agent.** Metronome's skills files exist because "there's a lot of different ways to hit foot guns etc if you're not guided," and the packaging decision is deliberate: "these skills files are also portable and easy to install so you can use them on your own side." The unit of packaging is the accumulated hazard knowledge of one API — what the docs do not say — which is exactly the content a customer cannot write and the vendor cannot express as a better endpoint. They also carry procedure, not just facts: the skill is what tells the agent to flow usage into the platform so the setup becomes testable. ([Garvin](../sources/20260828_mJqwmmOx4WA.md), 06:13-06:35, 08:04-08:19)
- **A registry with no package manager, for an audience that would not use one.** Cloudflare distributes skills to a go-to-market organization through a central alias where skills are submitted, reviewed by the business and operations teams, and curated into a repository the agentic workspace reads. There is no install step, no version pin, and no dependency resolution — the discovery and quality functions this page attributes to a registry are performed by named humans instead. That is a workable substitute at organization scale and a bad one at ecosystem scale, and it makes the supply-chain question a question about who has access to the alias. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 13:01-14:02)

- **What the registry has to do at 2,500 skills, and what it looks like when it does not.** Uber names three separate failures from decentralized skill authoring — "there's a lot of duplication, same skill being built by different engineers… discovery and configuration was a huge hassle… and a lot of skills were subpar quality" — and answers them with three distinct mechanisms rather than one catalog: automated lint checks and reviews as a publish gate, "one single command to discover and install any plug-in," and persona-based auto-install where "based on the engineer personas, we even auto-install some of the default skills… you don't even have to even install them" ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 07:03-08:13). The auto-install layer is the addition this page did not have: package management assumes a consumer who chooses, and most engineers never browse a catalog of 2,500 entries. Usage context for the duplication complaint: 2,500 skills against "more than 20,000 skill executions per day," which is a thin average tail (08:26-08:44). See [Run a Skills Marketplace With Lint Gates, Persona Auto-Install, and Trace Feedback](run-a-skills-marketplace-with-lint-gates-persona-auto-install-and-trace-feedback.md).

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [Treat complex skills like software artifacts](treat-complex-skills-like-software-artifacts.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)
- [Seed the Agent-Built Sandbox With Usage, Not Just Objects](seed-the-agent-built-sandbox-with-usage-not-just-objects.md)
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)
- [Let Users Author the Output Format as a Skill](let-users-author-the-output-format-as-a-skill.md)
- [Run a Skills Marketplace With Lint Gates, Persona Auto-Install, and Trace Feedback](run-a-skills-marketplace-with-lint-gates-persona-auto-install-and-trace-feedback.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 14:00-17:40
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 10:38-11:57
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 13:44-14:47
- [How to avoid disaster when vibe-coding a billing engine — Andrew Garvin, Stripe](../sources/20260828_mJqwmmOx4WA.md), 06:13-06:35, 08:04-08:19
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 13:01-14:02
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 07:03-08:44
