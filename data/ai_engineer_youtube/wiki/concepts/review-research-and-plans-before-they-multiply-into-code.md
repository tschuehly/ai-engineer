# Review research and plans before they multiply into code

Summary: In agentic coding, human judgment has more leverage when it reviews compressed research and plans before implementation. A wrong plan can generate many bad lines, and a wrong research claim can send the whole agent run toward the wrong architecture.

Use when:
- Reviewing an agent's proposed implementation path before it writes a large diff.
- Designing team rituals for high-throughput AI-generated code.

Details:
- Planning compresses intent: it should combine the research artifact with the ticket or PRD, outline exact steps, include relevant files and snippets, and state how each change will be tested. 07:52-08:16, 14:40-14:56
- Code review is also about mental alignment: reviewers need to know how and why the codebase is changing, not only whether a final diff compiles. 14:56-15:34
- Attaching agent threads, prompts, plans, build results, and manual-test notes to pull requests can give reviewers a narrative that plain green diff text cannot provide. 15:36-16:00
- Longer plans can improve execution reliability but reduce human readability, so each team needs a plan-size sweet spot for its codebase and review habits. 16:04-16:40
- Human review of the research and plan is not optional: a bad line of code is local, but a bad part of a plan can become many bad lines, and a bad research statement can send the model in the wrong direction. 16:40-17:38
- The workflow should move human attention to the highest-leverage checkpoints instead of producing many Markdown files merely to create a feeling of rigor. 17:34-17:48

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Use research-plan-implement loops for coding agents](use-research-plan-implement-loops-for-coding-agents.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)

Sources:
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](../sources/20251202_rmvDxxNubIg.md), 07:52-08:25, 14:40-17:48
