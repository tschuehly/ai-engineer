# Put Every Platform Capability Behind One Assistant and Let Teams Fork Personas

Summary: Uber packages its skills, MCP gateway, and context graph into a single assistant reachable from Slack, the CLI, and the web, so a new platform capability becomes available everywhere at once instead of being integrated per surface. The personalization layer is what turned it into a fleet product: employees hook custom skills and prompts into a team Slack channel so the assistant "works like a teammate," producing 300 distinct personas in the first month.

Use when:
- An internal AI platform has several capabilities and no single place users can reach them.
- Deciding whether to build per-surface integrations or one assistant with multiple front ends.
- Adoption is limited to engineers because the entry point is a CLI.
- Considering whether users should be able to configure their own variant of a shared assistant.

Details:
- **One assembly point, many surfaces.** "All of the things that I mentioned so far, whether it's skills, MCPs and context graph, they're all plugged into that in every surface possible whether it's on Slack, CLI, web. So anyone in the company, they can ask a simple question. It can look up the context graph, invoke any skill, check any code in any codebase and give an answer across any of these surfaces." ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 10:21-10:47) The capability integration happens once, at the assistant, not N times at the front ends.
- **Personas are team-scoped, not user-scoped, and that is the interesting choice.** "You can hook up your custom skills, custom prompt and hook it up into your team Slack channel so that it knows all of the things about that team and works like a teammate… one or more people can even collaborate on the same Slack channel." Binding the persona to a channel rather than to a person makes the customization shared context: the team's tuning benefits whoever is in the conversation, and the conversation itself is visible to the team. (10:47-11:16)
- **The adoption figures are for the personalization, not the base assistant.** "Just in the last one month, 300 unique personas created and more than 20,000 sessions per day." A month-old feature producing 300 forks is a signal that per-team configuration was the missing thing, not more capability. (11:16-11:30)
- **It is also the front door to the rest of the factory.** The end-to-end feature demo starts in a Slack thread — "we're jamming on it in Slack here. Let's tag in Cortana" — and moves from Slack into the web interface for deeper business research before any code exists (11:34-12:32). An assistant on the surface where the idea is already being discussed is what makes the upstream half of the SDLC reachable at all.
- **The relationship to the wiki's surface-embedding argument.** [Embed Agent Tools in Existing Work Surfaces](embed-agent-tools-in-existing-work-surfaces.md) says tools get used where the work already happens. This is that argument applied at the platform level with an addition: the surfaces are front ends over one capability set, so the embedding cost is paid once and the capability catalog stays consistent across them. The alternative — a Slack bot, a CLI, and a web app each wired to their own subset of tools — is how surfaces drift apart.
- **The unexamined risk is the governance one.** 300 team-authored prompts and skill bundles in a month is the same sprawl dynamic that the skills marketplace exists to control, arriving through a different door. Nothing in the talk describes review, lint, or quality gates for personas, and the marketplace's answer — automated checks at publish time — is not mentioned as covering them. See [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md).
- **Caveat.** No breakdown of the 20,000 daily sessions by surface or by user population, no statement of what a session accomplishes, and no comparison against the tools these sessions replaced.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Embed Agent Tools in Existing Work Surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Expose the Background Agents' Tool Surface to Employees Over MCP](expose-the-background-agents-tool-surface-to-employees-over-mcp.md)
- [Run a Skills Marketplace With Lint Gates, Persona Auto-Install, and Trace Feedback](run-a-skills-marketplace-with-lint-gates-persona-auto-install-and-trace-feedback.md)
- [Build One Context Graph So Agents Stop Crawling Twenty Systems for Basic Facts](build-one-context-graph-so-agents-stop-crawling-twenty-systems-for-basic-facts.md)
- [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 10:21-12:32
