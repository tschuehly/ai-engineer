# Make Code Review the Bottleneck Skill for AI-Generated Code

Summary: As agents generate more implementation, code review becomes the scarce production skill. Teams need reviewers who can explain whether a change is good or bad, and review tools that present change intent and system impact rather than only file-sorted diffs.

Use when:
- Designing review workflows for agent-generated pull requests.
- Hiring or training engineers for AI-assisted software teams.

Details:
- Code review is framed as the most important skill for AI-assisted engineering because agents will write more code and humans must decide what is acceptable. (11:20-11:44)
- The source argues that interviews should test the ability to read someone else's code and explain why it is good or bad, not only solve isolated coding puzzles. (11:23-11:38)
- Current review tools are criticized for presenting lexicographically sorted changed files, which does not match how reviewers reason about the intent and effects of a software change. (11:44-12:05)
- Reviewers should distinguish code that is merely different from code that is worse; style guides, linters, and rules files should absorb preference disputes so human attention can focus on quality. (13:23-14:06)
- LLM claims about what the model did should be verified against actual tool behavior and code evidence, because fluent explanations may not reflect the real process. (12:24-13:17)

- **The altitude the skill moves to, named by a team operating the automated layer beneath it.** Uber's position is that automation expands rather than replaces the outer loop: "Rather than removing humans from the code review process, we are moving their responsibilities up a layer… Instead of you worrying about the optimization of the performance and the API compatibility, you're going to be thinking more about architecture in your code reviews. You're going to have time to focus on the domain expertise that you have and product thinking." That reframes the scarce skill from reading diffs faster to judging structure and product fit, and it depends entirely on the lower tier actually being absorbed rather than dropped — the talk asserts the absorption and does not measure it. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 13:44-14:34)

- **If review is the bottleneck skill, the people who have it are the ones who spent years building it — which is a training problem, not just a hiring filter.** "Reviewing AI output is often harder for some than actually writing it, especially early in career. Senior engineers have already spent a large portion of their career reviewing others code. But early career engineers don't have that muscle yet." The apprenticeship route that built the skill — reviewing colleagues' pull requests over years — is exactly the activity agent-written code is displacing, so the supply of the scarce skill is being drawn down at the same time demand for it rises. Liguori reports this as a cost of the transition rather than proposing a remedy, and gives no data behind it. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 16:17-16:44)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)
- [Context quality determines AI code review trust](context-quality-determines-ai-code-review-trust.md)
- [Do not report agent autonomy without quality accountability](do-not-report-agent-autonomy-without-quality-accountability.md)
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)
- [When Code Stops Being the Long Pole, Approvals Become It](when-code-stops-being-the-long-pole-approvals-become-it.md)

Sources:
- [Vibes won't cut it - Chris Kelly, Augment Code](../sources/20250803_Dc3qOA9WOnE.md), 11:20-14:06
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 13:44-14:34
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 16:17-16:44
