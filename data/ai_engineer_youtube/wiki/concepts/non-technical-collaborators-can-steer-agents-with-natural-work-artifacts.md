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

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Visual agent workflows make tool use observable and adjustable](visual-agent-workflows-make-tool-use-observable-and-adjustable.md)
- [Grow personal-agent permissions incrementally from recurring pain](grow-personal-agent-permissions-incrementally-from-recurring-pain.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Make One Agent Session Reachable From Every Interface](make-one-agent-session-reachable-from-every-interface.md)

Sources:
- [Agents for Everything Else - swyx](../sources/20260501_zepu8Kk6FBQ.md), 03:47-08:59
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 04:21-04:48, 12:13-12:45
