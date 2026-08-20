# Automation Loops Convert Repeated Review and Triage Into Factory Improvements

Summary: A software factory improves when repeated human review, triage, and transcript-mining work becomes automated feedback into rules, prompts, specs, or agent workflows. The durable value is not the one-off automation, but the loop that turns recurring friction into factory changes.

Use when:
- Deciding which agent workflow to automate next.
- Mining chat logs, PR comments, Slack threads, or daily reviews for repeatable process improvements.

Details:
- The talk recommends looking for repeated loops and automating them so the factory improves over time instead of relying on manual repetition (22:49-24:06).
- Examples include summarizing chat transcripts into learnings, checking daily review material from Slack and other systems, and reading merged PR comments as inputs to future work (24:45-27:04).
- A factory can automate stages such as planning, producing, reviewing, and opening or updating a PR, but those stages should remain visible enough for humans to inspect and improve (14:37-15:23).
- In the Q&A, the speaker emphasizes observability, monitoring, and human review around the factory so automated work stays inspectable and accountable (58:48-01:04:35).

- A field report adds one loop this page did not name and one cost it did not price. Khandelwal's team closed the loop with "issues and boards into the repo… CICD… [agentic] reviews" plus "a code gardener that… every night it'll run and look at the code and check if something like not organized correctly," where "what does correct organization mean will depend on your code base" — a scheduled hygiene pass whose rubric is repo-specific rather than a generic linter. The cost is that every automated loop writes to the same queue: wiring the tracker in without scoping which agents may file took the repo to hundreds of open issues in a couple of weeks. Automating the loop and bounding its output are one decision, not two. See [Wire Issue-Filing Authority Before Giving Agents a Tracker](wire-issue-filing-authority-before-giving-agents-a-tracker.md). ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 10:32-10:53, 11:54-12:11)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Wire Issue-Filing Authority Before Giving Agents a Tracker](wire-issue-filing-authority-before-giving-agents-a-tracker.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Context development lifecycle treats context as an engineered artifact](context-development-lifecycle-treats-context-as-an-engineered-artifact.md)

Sources:
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 14:37-15:23, 22:49-27:04, 58:48-01:04:35
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 10:32-10:53, 11:54-12:11
