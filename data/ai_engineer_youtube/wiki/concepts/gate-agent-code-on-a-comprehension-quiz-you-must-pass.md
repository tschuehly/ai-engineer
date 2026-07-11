# Gate Agent Code on a Comprehension Quiz You Must Pass

Summary: Reading an explanation is easy to fake — you can finish it and still not understand. Have the agent append a short comprehension quiz to its explainer and make a rule: you don't forward the code to human review until you can pass the quiz. The quiz is a "speed regulator" that keeps you moving at the speed of understanding, not just the speed of correctness.

Use when:
- You suspect you're rubber-stamping agent PRs you don't actually understand.
- You want a concrete, self-enforcing checkpoint before promoting agent work to teammates or production.
- Adding a self-check to an agent-authored explainer doc or onboarding artifact.

Details:
- Motivation: reading is hard and people are lazy — Litt once sent a coworker a PR he thought he understood, then failed her most basic question; he'd fooled himself. The quiz is the system so that never happens again. (10:19-10:35)
- Inspiration: Andy Matuschak's "Books don't work" (it's easy to read a book and not realize you didn't understand it) and his work with Michael Nielsen embedding interactive spaced-repetition quizzes in essays, which even email you the quiz later so you remember forever — you can't get through the essay without remembering it. (10:35-11:05)
- Implementation: at the bottom of each code-explainer doc, a quiz of ~5 medium-difficulty questions about what the agent wrote; the rule is "don't send code to reviewers unless I can pass the quiz." (11:05-11:40)
- It "sounds silly" but repeatedly catches genuine gaps — a self-administered check that surfaces the moment you didn't actually understand. (11:16-11:40)
- Reframe: everything about AI pushes "faster, faster"; the quiz is a deliberate speed *regulator* that ensures understanding keeps pace with correctness. Ships as part of the public `explaindiff` skill. (11:36-12:00)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Have Agents Write Literate Explainer Docs for Their Changes](have-agents-write-literate-explainer-docs-for-their-changes.md)
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)

Sources:
- [Understanding is the new bottleneck — Geoffrey Litt, Notion](../sources/20260710_WkBPX-oDMnA.md), 10:19-12:00
