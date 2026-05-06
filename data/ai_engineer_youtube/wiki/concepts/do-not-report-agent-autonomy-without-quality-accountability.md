# Do not report agent autonomy without quality accountability

Summary: Autonomy duration is a weak agent-quality signal unless it is paired with evidence about the resulting work. Long unattended runs can still produce code slop, tech debt, or unsafe behavior.

Use when:
- Evaluating claims that an agent can work autonomously for many hours.
- Designing dashboards, demos, or benchmarks for coding-agent autonomy.

Details:
- The talk criticizes autonomy-duration claims that say a model can run for 30-60 hours without also saying whether the resulting code was good. (06:05-06:16)
- swyx summarizes the evaluation gap as "autonomy without accountability": autonomy is not enough when output quality, safety, and maintainability remain unreported. (06:16-06:23)
- Code slop is presented as more than messy code; a small number of engineers or agents can create disproportionate tech debt, and serious failures can expose private user data. (05:44-05:57)
- Practical autonomy reporting should therefore include code-quality evidence, tests, review findings, security checks, maintainability costs, and whether humans can still understand and own the change.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Separate watched and unwatched agent time horizons](separate-watched-and-unwatched-agent-time-horizons.md)
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)

Sources:
- [No More Slop - swyx](../sources/20251222_IoiHI7p12Ao.md), 05:44-06:23
