# Comment Volume Is a Property of the Review Pipeline, Not the Model

Summary: Once several generators run over the same diff — a per-file logic pass, a deep multi-file review, team linters, custom agents — the number of comments a reviewer sees is emergent, and no individual generator is responsible for it. The fix is a waist in the pipeline: one post-processing stage that rates, categorizes, filters, and deduplicates across all generators before anything is posted. Tuning individual prompts to be quieter does not reach the problem.

Use when:
- An AI reviewer is producing more comments than anyone will read, and each generator looks reasonable on its own.
- Designing any fan-out architecture where multiple specialized models emit findings into one human-facing surface.
- Deciding where confidence thresholds and severity filters belong in a multi-generator system.
- Planning a build-versus-buy comparison you want to keep running after the decision.

Details:
- **The architecture.** Three surfaces — GitHub, Phabricator, and the agent loop — feed one service that "takes in requests for reviews… brings in feedback from users, and it routes it" to "a number of different generators… tuned for different performance and cost avenues." ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 03:07-03:43)
- **Why volume is emergent.** "With all these different generators, we might be duplicating comments, and we can actually create quite a high volume of comments. If you've ever used AI to run a code review, you've probably seen that." Duplication is the specific cost of fan-out: two generators finding the same real defect is a success at the generator level and a defect at the pipeline level. (03:43-03:55)
- **The waist.** "We run through a number of steps in the post-processing where we both rate, categorize, filter, and deduplicate comments so that our engineers get only the highest confidence comments that are actionable for them to work on." Four distinct operations, and only deduplication is unique to fan-out — rating, categorizing, and filtering are the operations that would otherwise be smeared across every generator prompt and tuned inconsistently. (03:55-04:10)
- The design consequence worth carrying to other systems: put the volume decision in one place that sees all findings at once, because it is the only place where "how many comments is too many for this PR" is answerable. A generator can only decide whether to emit its own finding; it cannot know it is the fourth one.
- **Review intensity is a routing decision made before the fan-out, not a filter after it.** "We need the ability to take factors like the risk profile and the complexity of a code change and factor that in when deciding how we're going to run a code review. Not all code gets the exact same review." The two levers compose: routing decides which generators run at all, the waist decides which of their outputs survive. (02:25-02:43)
- **Keep the alternative you rejected wired in as a comparison arm.** "We also have the ability to plug into third-party code review systems so that we can compare ourselves to what's available more broadly." A build decision made once decays as the market moves; running the vendor as one more generator inside your own pipeline turns build-versus-buy into a standing measurement on your own diffs rather than a decision you would have to reopen from scratch. Uber does not report what the comparison showed. (03:33-03:43)
- The cost side of the same structure: generators tuned to different price and latency points let a cheap pass run everywhere and an expensive one run where the routing layer says the risk justifies it. Uber attributes a 60% cost reduction against their naive first build to this work plus the observability tuning, without separating the two contributions. (10:47-11:02)
- What the waist does not fix. Deduplication and confidence filtering reduce volume; they do not establish that surviving comments are correct, since several generators sharing a model can share a wrong finding and agreement will read as confidence. The filter is a volume control, and precision has to be earned upstream or measured downstream. See [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md).
- The right threshold for the filter is not one number, because the comment stream has two consumers with opposite tolerances for noise and for error. See [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md).
- Limits. The architecture is described from a slide with no measurement of the post-processing stage itself — no duplicate rate, no share of comments filtered out, no cost of the filtering pass, and no evaluation of whether the filter drops true findings. ([Provenance and Limits](../sources/20260828_EL123UNokkI.md))

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Route each change to the proof it needs](route-each-change-to-the-proof-it-needs.md)
- [Low-false-positive bug finding is required for coding-agent trust](low-false-positive-bug-finding-is-required-for-coding-agent-trust.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)

Sources:
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 02:25-04:10, 10:47-11:02
