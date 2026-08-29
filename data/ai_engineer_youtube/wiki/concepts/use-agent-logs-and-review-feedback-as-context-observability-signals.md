# Use Agent Logs and Review Feedback as Context Observability Signals

Summary: Agent logs, PR feedback, and production failures reveal whether context is missing, misunderstood, or stale. Durable context workflows should mine those signals and turn repeated failures into shared context improvements.

Use when:
- Building feedback loops for team-maintained prompt, skill, or context libraries.
- Diagnosing repeated agent mistakes that survive local prompting and appear in review or production.

Details:
- Agent logs can show when an agent says it is missing information or fails to use available context, giving teams a feedback channel for shared context maintenance (17:54-19:21).
- PR review comments on agent-generated work are also feedback on the context that shaped the PR; the durable fix is often to improve context so the next iteration avoids the same defect (19:24-19:47).
- Production failures from AI-generated code can be converted into test cases and then into context improvements, closing the loop between runtime observation and future agent behavior (19:49-20:29).
- The organizational version of the loop is to publish reusable fixes so multiple teams benefit from one context improvement rather than each team rediscovering the same missing instruction (22:38-23:39).

- **Classifying the replies, not just counting them, is what turns review feedback into a work list.** Uber "started collecting the sentiments of the replies that were made to the uReview… agent got from the developers. So, we categorized them into positive, negative. We classified them into various categories, and we found a lot of classes of bugs and issues that we could actually solve." Polarity alone tells you the tool is disliked; the category tells you which failure to fix next, which is what let them "move a large number of PRs to a high quality to cost ratio." Worth reading as a cheap first pass over a signal most teams already have sitting in their PR comment threads. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 05:11-05:47)

- **Chat is an observability source, and sometimes the only one that holds the cause.** When Unblocked's review agent started surfacing far fewer issues, the explanation was not in logs or metrics — it was a Slack conversation in which someone connected the drop to a model upgrade, and that message is what a context-backed agent later retrieved to write a self-explaining fix PR. The generalization for this page: index the org's conversation record alongside agent logs and PR feedback, because "what changed" is answered by humans in chat far more often than by telemetry. See [A Model Swap Moves Your Agent Product's Output Metrics, and the Explanation Lives in Chat](a-model-swap-moves-agent-output-metrics-and-the-reason-lives-in-chat.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 13:40-15:08)
- **Two behavioral signals available in any assistant log, requiring no feedback widget.** In a deployment answering ~40,000 questions a week, Izmit's team locates quality problems "where they are swearing at the agent or repeating their question." A repeated question is a user-supplied negative label with the retry attached; profanity is a sentiment label that costs nothing to collect. Both survive where explicit feedback is sparse or biased toward engaged users, and both are cheap enough to run over the whole log rather than a sample. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 15:00-15:20)

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md)
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](demand-driven-context-pulls-knowledge-from-failed-work.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [A Model Swap Moves Your Agent Product's Output Metrics, and the Explanation Lives in Chat](a-model-swap-moves-agent-output-metrics-and-the-reason-lives-in-chat.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 17:54-23:39
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 05:11-05:47
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 13:40-15:08
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 15:00-15:20
