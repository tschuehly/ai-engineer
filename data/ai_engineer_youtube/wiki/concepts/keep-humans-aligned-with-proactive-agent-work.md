# Keep Humans Aligned With Proactive Agent Work

Summary: Higher proactivity should not be treated as removing the human from the workflow. The human role shifts toward observing agent behavior, tuning intervention points, redirecting misdirected work, and validating evidence-rich outputs.

Use when:
- Reviewing whether an autonomous or proactive agent workflow still has meaningful control points.
- Designing product surfaces for background coding agents, critic agents, verification traces, or live-data-driven suggestions.

Details:
- The talk rejects a future where developers babysit many parallel agent terminals; trusted collaborators should understand context, anticipate needs, and know when to step in (02:21-03:18).
- At higher proactivity, the human remains in the loop by observing what agents are doing, refining when intervention is needed, and redirecting misdirected work (08:55-09:10).
- Level three is framed as alignment to the project, not autonomy as the primary goal; agents and humans collaborate across the project lifecycle (09:10-09:20).
- Jules adds an adversarial critic agent for code review and verification that writes a Playwright script, takes a screenshot, and returns the artifact into the trajectory for human validation (09:50-10:08).
- Editable self-written memory gives the agent project knowledge while leaving humans able to inspect and change what the agent remembers (09:34-09:50).
- **"Refining when intervention is needed" gets a concrete, low-friction mechanism from a second source: reply to the output.** Resolve AI's on-call handoff report is tuned in its own Slack thread — "this is too verbose. Verbose. Make it shorter" — and "the agent is able to update its task underneath… so that the next time it fires, it's not going to be as verbose." Redirecting agent work costs a sentence in the channel where the work already appeared, rather than a trip to a configuration surface. Note this segment was not shown completing on stage. See [Amend a Recurring Agent Task by Replying to Its Output](amend-a-recurring-agent-task-by-replying-to-its-output.md). ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 20:26-20:58)
- **The same source shows an agent escalating to a human by choice rather than by policy.** With DM access, it will "DM you to say, 'I think I know the answer to this, but I'm not sure. Can you confirm this for me before I respond back?'" — a control point the agent opens when its own confidence is middling. Smith calls this "emergent," which is worth reading as a limit: a behavior that appeared rather than one that is guaranteed is not yet an alignment guarantee. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 16:52-17:09)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Amend a Recurring Agent Task by Replying to Its Output](amend-a-recurring-agent-task-by-replying-to-its-output.md)
- [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md)

Sources:
- [Proactive Agents - Kath Korevec, Google Labs](../sources/20251213_v3u8xc0zLec.md), 02:21-10:08
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 16:52-17:09, 20:26-20:58
