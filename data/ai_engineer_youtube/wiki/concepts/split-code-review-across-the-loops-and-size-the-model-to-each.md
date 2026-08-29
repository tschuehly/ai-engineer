# Split Code Review Across the Loops and Size the Model to Each

Summary: Rather than choosing one model for automated code review, Uber runs review twice at different positions and different costs: a smaller or medium model inside the agent's inner loop before a PR exists, and a powerful reasoning model with a review skill in the outer loop after. The variable that sets the model tier is not the code, it is the loop — inner-loop review is on the agent's critical path and runs on every attempt, outer-loop review runs once per PR and can afford depth.

Use when:
- Deciding which model tier an automated code reviewer should use, and finding the answer differs by where it runs.
- Automated review is either too slow to sit in an agent loop or too shallow to replace a human pass.
- Designing a review pipeline for agent-authored diffs specifically.

Details:
- **The split.** "Code review is another thing that happens in the outer loop, but this is another thing that we've shifted — we've moved parts of code review to happen in the inner loop. The outer loop code review can have a powerful model use reasoning, a skill, to do a deeper review. And in the inner loop, we can have a smaller model that runs faster with a medium model." ([Huda](../sources/20260821_17-YSUHo6Lk.md), 15:10-15:21)
- **The selection variable is call frequency, not difficulty.** Inner-loop review fires on every iteration of an agent that may iterate many times before producing anything; outer-loop review fires once on a completed diff. That asymmetry — not a judgment about which findings are harder — is what makes the cheap model correct in one position and wrong in the other. This is a concrete instance of the wiki's general rule to route by more than cost; see [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md).
- **The outer-loop reviewer gets a skill, the inner one does not.** Depth here is not only a bigger model: the outer pass pairs reasoning with a review skill, which is where accumulated organizational review knowledge would live. The inner pass is a fast filter, and treating it as one clarifies what it should look for — obvious, cheap, high-frequency defects that would otherwise waste a full outer pass.
- **Why "parts of" is doing work in that sentence.** The claim is not that review moved left; it is that review was *split*. Anything the small model can decide is decided early and repeatedly, and the expensive pass sees a diff that has already survived it. That is the same economics as the draft-PR stopping point described in [Stop the Autonomous Agent at a Draft PR and Validate Before CI](stop-the-autonomous-agent-at-a-draft-pr-and-validate-before-ci.md), applied to review rather than to CI.
- **This is a costed answer to the review-capacity problem, with a limit.** The wiki records that agent output speed overruns human review capacity. Two automated passes reduce what reaches a human but do not change who is accountable for the merge, and the talk's own answer to that is evidence rather than delegation — the check table attached to the PR.
- **Caveat.** No model names, no findings-per-pass numbers, no measurement of what the inner pass catches that the outer one would have caught anyway, and no discussion of the obvious failure mode: an agent that learns to satisfy its own inner-loop reviewer. Treat the two-position split as a design pattern with a clear rationale, not as a validated configuration.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Stop the Autonomous Agent at a Draft PR and Validate Before CI](stop-the-autonomous-agent-at-a-draft-pr-and-validate-before-ci.md)
- [Route Between Model Tiers by Quality Dimension, Not Only Cost](route-between-model-tiers-by-quality-dimension-not-only-cost.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [AI Diff Review Should Find Problems Before Merge](ai-diff-review-should-find-problems-before-merge.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Make Code Review the Bottleneck Skill for AI-Generated Code](make-code-review-the-bottleneck-skill-for-ai-generated-code.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 15:10-15:54
