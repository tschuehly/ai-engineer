# Use voice-dumped UI and code observations as agent feedback

Summary: Voice feedback can turn frontend agent review into a high-bandwidth loop: inspect the running UI, narrate observations and bugs, then continue into the code with the same spoken review context.

Use when:
- Reviewing an agent-generated frontend change.
- Converting fuzzy UI judgment into actionable agent feedback without writing a long prompt.

Details:
- The speaker describes starting voice feedback immediately after the agent finishes, first in the browser by narrating what the UI did and what looks wrong. (10:14-10:40)
- The same feedback loop then moves into code, where the reviewer continues describing what the agent implemented and which patterns need to change. (10:40-10:44)
- Long voice prompts can encode thought process, UI observations, bug reports, and implementation critique more richly than terse commands like "fix this." (10:24-10:50)
- The approach is especially relevant to frontend agent work because it connects visible behavior with code structure instead of relying only on screenshots or source diffs. (10:27-11:37)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)
- [Design coding-agent editors as review surfaces](design-coding-agent-editors-as-review-surfaces.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)

Sources:
- [From Vibe Coding To Vibe Engineering - Kitze, Sizzy](../sources/20251214_JV-wY5pxXLo.md), 10:14-11:37
