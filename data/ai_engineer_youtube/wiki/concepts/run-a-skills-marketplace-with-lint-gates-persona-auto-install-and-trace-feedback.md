# Run a Skills Marketplace With Lint Gates, Persona Auto-Install, and Trace Feedback

Summary: Skill sprawl in a large org produces three specific failures — duplication, discovery and configuration friction, and low quality — and Uber answers each with a distinct mechanism: a managed marketplace with automated lint and review gates for quality, a single discover-and-install command plus persona-based auto-install for friction, and trace-plus-comment collection with continuous evals routed back to skill authors for improvement. The order matters: the catalog and the gates came first, the improvement loop last.

Use when:
- Engineers across many repositories are independently authoring overlapping agent skills.
- Deciding what a skills registry has to do beyond hosting files.
- Sequencing skill-platform work and tempted to start with a self-improvement loop.
- Trying to get the right skill in front of an agent without asking every user to install it.

Details:
- **The three failures, named separately.** "There's a lot of duplication, same skill being built by different engineers in different [places]; discovery and configuration was a huge hassle; and a lot of skills were subpar quality." ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 07:18-07:31) These have different fixes, which is why a registry alone solves only the middle one.
- **A quality gate that runs without a human.** Skills are split into core and domain-specific, all landing in "a managed skills marketplace. We have 2,500 skills there right now. And it goes through a whole bunch of lint checks, automated reviews which ensures a baseline skill quality for any skills that we have." At 2,500 entries a human review board is not a design option; the gate has to be as cheap as the authoring. (07:31-07:46)
- **Auto-install by persona is the mechanism worth stealing.** "There is one single command to discover and install any plug-in in our ecosystem. And based on the engineer personas, we even auto-install some of the default skills. So the agents automatically can pick up the right skill. You don't even have to even install them." This converts skill adoption from a per-user decision into a platform default, which is the only form that reaches people who never browse the catalog. It also relocates the retrieval problem: instead of the agent selecting from 2,500 descriptions, the platform pre-selects by role and the agent selects from a much smaller resident set — a coarse but effective answer to the context cost described in [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md). (07:46-08:13)
- **The improvement loop is explicitly the newest part.** "Of late, we started working on collecting traces and comments and capturing continuous evals so that we can give feedback back to the skill authors for skill improvements. And this is an area of big investment for us right now." Note the shape: the loop closes on the *author*, not on the skill file. A human still edits. (08:13-08:26)
- **Scale.** "We have 2,500 skills and cumulatively more than 20,000 skill executions per day across our fleet" — roughly eight executions per skill per day on average, which is worth holding next to the duplication complaint: a large catalog with a thin usage tail is what duplication looks like from the outside. (08:26-08:44)
- **This is direct evidence for a sequencing claim the wiki argues on principle.** [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md) says a self-rewriting skill loop scales whichever regime is already in place, so the catalog has to come first. Uber's ordering matches: marketplace, lint gates, install path, personas — then, "of late," the trace-and-eval loop. The governance was built before the acceleration.
- **Caveat.** What the lint checks and automated reviews actually assert is not described, no pass/fail rate is given, and there is no report of whether duplication actually fell after the marketplace existed. "Baseline skill quality" is a claim about the gate's intent, not a measurement of its effect.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Package Reusable Context as Skills, Libraries, and Registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)
- [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)
- [Choose Skill Trigger by Trading Context Load Against Cognitive Load](choose-skill-trigger-by-trading-context-load-against-cognitive-load.md)
- [Evaluate Agent Skills With Task Scenarios and Comparative Conditions](evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Ship a Catalog of Paved Roads, Not One Standard](ship-a-catalog-of-paved-roads-not-one-standard.md)
- [Run Maintenance Skills From One Managed Loop Surface](run-maintenance-skills-from-one-managed-loop-surface.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 07:03-08:44
