# Capture the Coding Session as the Intent Record

Summary: The decisions that determine what a change actually is are made in the back-and-forth of the coding session — answers to the agent's clarifying questions, approaches tried and rejected, mid-implementation corrections — and almost every team discards that transcript at the moment the pull request opens. Treat the session as the durable intent record and persist it into the review artifact.

Use when:
- Deciding what a coding agent should emit alongside the diff.
- Building acceptance criteria, test plans, or review context for agent-written changes.
- Diagnosing why a reviewer cannot tell whether a change does what was wanted.

Details:
- Intent is distributed, and the last location is the one nobody keeps: "An intent doesn't only live in the spec. Intent live[s] in your Jira ticket. That's the goal… It lives in your PRDs… it's a plan. But most importantly, it lives in your prompts today. This is where the real decisions are being made." (05:47-06:14)
- The discard is explicit and routine: "you're going back and forth with the agent, and this is where all the user decisions are being made. But what we do today is we create a change, we create a pull request, and then we throw away the prompts. And this is one of the things that we need to change." (06:14-06:32)
- What to capture is narrower than the whole transcript — the human's decisions, not the agent's chatter: "Agent will stop to ask questions. These are the decisions that we need to capture. This is the intent," plus "what we said to build out. What we tried and rejected." (09:33-09:53, 13:15-13:22)
- The captured decisions are then converted, not stored raw: "you capture the user responses and that essentially forms your acceptance criteria," and "this is where you can also leverage LLM to do so." (08:19-08:30, 10:10-10:16)
- The independence argument for why the session and not the code is the source: if the artifact is reconstructed from the diff, "if your code is built by the same agent which is actually building a test plan, it's not going to build a test plan which will actually catch issues. So, that's why it's important to actually use the session information to build out a test plan." The session contains what the human wanted; the code contains only what the agent did. (13:22-13:47)
- Two adjacent wiki patterns capture *some* of this and leave the gap this concept names. Research-plan-implement loops and collaborative plan documents preserve intent formed **before** implementation; session capture targets the intent formed **during** it, which is precisely what the spec-driven critique says the plan cannot contain.
- Practical consequence for harness design: prompts, session transcripts, and agent question/answer pairs become first-class outputs of a coding run, with retention and privacy handling to match — they now carry decision history, not just debugging noise.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Spec-Driven Development Without a Feedback Loop Is Waterfall](spec-driven-development-without-a-feedback-loop-is-waterfall.md)
- [Code Review Carries Alignment, Not Just Correctness](code-review-carries-alignment-not-just-correctness.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Review coding-agent work at task, plan, and code checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 05:47-06:32, 08:19-08:30, 09:33-10:16, 13:15-13:47
