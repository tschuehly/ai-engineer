# Measure a Review Bot by Whether the Comment Changed the Code

Summary: A review model cannot tell you when it is wrong — it asserts every finding with full confidence — so the quality signal has to come from what happens after the comment is posted. Uber's ladder went from cost plus surveys, to classified sentiment on developer replies, to addressal rate (did the code actually change), to agent trajectory for diagnosis. The reason addressal wins over surveys is coverage: solicited feedback arrives on roughly a tenth of comments, while whether the code changed is observable on all of them.

Use when:
- Instrumenting an automated reviewer, linter agent, or any assistant whose output lands in a workflow that already records what the human did next.
- Deciding whether to run an NPS survey or feedback form on an internal AI tool, or to mine the behaviour already in the system.
- Explaining why a model's stated confidence cannot be used as a filter.
- Diagnosing a quality metric that moved without telling you why.

Details:
- **The premise.** "One of the biggest learnings in this process was like the model doesn't know that it's wrong. It always confidently says 100% sure that yeah, this is the review for your code. Go ahead." Self-reported confidence is unavailable as a signal, so every rung of the instrument below is about observed behaviour instead. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 06:35-06:46)
- **Rung one, and why it failed.** The first instrumentation was "very surface-level. We used to collect cost. We used to run an NPS survey, have Google Forms being filled, Slack support. And with all of this, we saw that our quality to cost ratio was like all over the place." Cost was measurable and quality was not, so the ratio they were trying to optimize had a well-measured denominator and a guessed numerator. (04:48-05:11)
- **Rung two, reply sentiment.** They classified the replies developers wrote to the bot's comments into positive and negative and then into categories, which "found a lot of classes of bugs and issues that we could actually solve" — the categorization, not the polarity, is what produced a work list. (05:11-05:47)
- **Rung three, addressal rate.** "We need to know more of how the review is done. So we started tracking things like address rate. So basically when a uReview comment is made, does the developer go and actually address the comment?" This is the behavioural label: the developer's next commit grades the comment, produced as a byproduct of them doing their job. (05:47-06:07)
- **The coverage argument, which is the reason to prefer rung three over rung one.** At about 25,000 comments a week, "we get 10% of them actually get some feedback. And only 4% of the PRs actually get some negative feedback." Anything that depends on a person choosing to respond is measured on a tenth of the output and on a self-selected tenth at that. Whether the code changed is computable for every comment. Reported result: "the overall addressal rate was… around 67% and almost three quarters of the high severity issues… were usually addressed." (10:12-10:47)
- **Rung four, trajectory, which is the diagnostic layer rather than a metric.** "We also started doing more like a runtime profile, which is like the agent trajectory, which told us why the agent is doing what it did. We get to know what tools calls it made. We get to know what thinking process it had. And then with that insight, we were able to actually tune our runtime, tune our performance." Addressal tells you a comment was bad; the trajectory tells you which tool call or reasoning step made it bad. An outcome metric without a trajectory store is a scoreboard you cannot act on. (06:07-06:35)
- The two layers answer different questions and neither substitutes for the other: sentiment and addressal are outcome signals collected in production at full coverage, trajectory is a diagnosis signal collected per run. Uber added them in that order, and the ordering is defensible — there is no point storing trajectories until you have a metric that tells you which runs to open.
- **Where the proxy breaks, which the source does not address.** Addressal is not correctness. A developer can address a comment that was wrong (the path of least resistance in review), and can decline a comment that was right. Ranked by cheapness, this is a strong first metric; treated as accuracy, it is unvalidated. Nothing in the talk reports a human-labelled sample against which 67% could be interpreted, nor a false-positive rate.
- The proxy also degrades when the reader is an agent rather than a person, because an agent addresses nearly everything put in front of it — so the metric must be segmented by surface before it means anything. See [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md).
- Limits. All figures are self-reported from slides with no methodology. The headline improvement — "our costs were down by 60% and our quality and our accuracy was up by around 70%" — is measured against their own naive first build, and "quality and accuracy" is never defined or attached to an instrument. ([Provenance and Limits](../sources/20260828_EL123UNokkI.md), 10:47-11:02)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Learn coding preferences from implicit edit feedback](learn-coding-preferences-from-implicit-edit-feedback.md)
- [Treat Every Human-AI Interaction as a Training Label](treat-every-human-ai-interaction-as-a-training-label.md)
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Review Comments Have Two Audiences With Inverted Error Costs](review-comments-have-two-audiences-with-inverted-error-costs.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)

Sources:
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 04:48-07:01, 10:12-11:02
