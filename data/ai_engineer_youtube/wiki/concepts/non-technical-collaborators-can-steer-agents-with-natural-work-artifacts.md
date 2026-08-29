# Non-technical collaborators can steer agents with natural work artifacts

Summary: Agents become more valuable outside engineering when non-technical collaborators can direct them with the artifacts they already use, such as Figma pages, screenshots, redlines, notes, and emails.

Use when:
- Designing agent workflows for designers, operators, event teams, sales, support, or other non-engineering collaborators.
- Evaluating whether a workflow requires a bespoke UI or can accept natural work artifacts as agent context.

Details:
- A designer used Figma pages, redline annotations, and ordinary communication patterns to steer Devin without a special instruction manual. (03:47-05:55)
- Swyx describes non-technical team comfort as critical: once collaborators could work with agents naturally, they started producing more polish, animations, and exploratory work because feedback cycles no longer depended on a developer queue. (05:57-07:28)
- The same pattern applied to operations work: speaker change requests could be forwarded as emails, screenshots, or short prompts for the agent to handle against the conference schedule. (08:40-08:59)

- **The interface is necessary but not sufficient — the missing piece is usually a place for the work to run.** Superconductor's diagnosis is blunt: "this is the key for allowing your non-technical team members to trigger real work. Your non-technical people don't have development environments set up on their computers." On that account a natural steering artifact produces a *request* rather than a change until the codebase runs in an isolated cloud environment; their reported loop is a support or growth person saying "Hey, fix this" in Slack, the agent fixing it, "screenshots are shown," and an engineer merging. Worth pairing with this page when non-engineers have agent access and still are not contributing — see [environment isolation is what lets non-engineers trigger real work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md). Their session UI also shows which people touched a session, which answers the reviewer's real question about non-engineer-originated work: "has this been vetted by an engineer or not?" ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 04:21-04:48, 12:13-12:45)
- **A third mode: the non-engineer builds the interface instead of steering through one.** Where this page's collaborators direct agents with artifacts they already have, DoorDash's operators generate the tool itself — "give this workflow in the hands of the operators so that they can actually build their own vibe-coded annotation UIs" — because their work is repetitive enough to deserve a purpose-built screen and varied enough that no central team would build it. The distinguishing question is whether the task is a one-off request (steer with the artifact) or a recurring operation (build the surface). ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:29)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Grow personal-agent permissions incrementally from recurring pain](grow-personal-agent-permissions-incrementally-from-recurring-pain.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md), 03:47-08:59
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 04:21-04:48, 12:13-12:45
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:29
