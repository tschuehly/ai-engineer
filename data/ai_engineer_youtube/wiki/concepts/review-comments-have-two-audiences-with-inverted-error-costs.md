# Review Comments Have Two Audiences With Inverted Error Costs

Summary: Once one review service serves both human PR authors and coding agents in the inner loop, the same comment stream has two consumers who price its two failure modes in opposite directions. A true-but-trivial comment is expensive for a human and nearly free for an agent; a wrong comment is cheap for a human and expensive for an agent, because the agent has no way to disbelieve it and will rework the code backwards.

Use when:
- Deciding the precision threshold for an automated reviewer whose comments are read by agents as well as people.
- Explaining why an AI reviewer that humans tolerate starts producing rework once it is wired into an agent loop.
- Choosing what to filter out of a review pipeline, and finding that the answer differs per consumer.
- Arguing about whether the inner loop is a lower-stakes place to deploy a review agent than the pull request.

Details:
- The setup that makes the comparison possible: Uber routes GitHub, Phabricator, and the agent loop into one review service, deliberately, so that "our agents are getting the same code review, the same rules, everything applied as our humans do." Having a single platform is what surfaced the difference — "what did we need to tune for the various audiences that are actually getting these code reviews?" ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 01:46-02:04, 11:56-12:14)
- **The counterintuitive direction.** "One thing that might be less intuitive is around accuracy. Uh with the inner loop, our accuracy needs actually need to go up." The inner loop is not the low-stakes place to ship a noisy reviewer; it is the high-stakes one. (12:14-12:22)
- The mechanism, in their words: "or else we can result in… cavitation of an agent where it fixes something, goes back, gets another code review, and has to kind of like fix backwards because the quality of the comment was low." A human reading a wrong comment argues with it or ignores it, and the loop terminates. An agent reading a wrong comment complies, ships a change, re-requests review, and can be sent to undo its own work. The human's skepticism is the error-absorbing layer, and the inner loop removes it. (12:22-12:36)
- **The inversion on the other error type.** "Agents are more than happy to go through and fix 100 nits on a pull request where your engineers really get frustrated in situations like that." Low-value-but-correct comments are the dominant complaint about AI reviewers when a person is reading them, and they nearly vanish as a cost when the consumer is an agent with no attention budget and no morale. (12:36-12:47)
- Read together, the two observations give a per-consumer filtering policy rather than one quality bar. For the human audience, filter hardest on *relevance* — the nit is the expensive item. For the agent audience, filter hardest on *correctness* — the nit is nearly free and the wrong comment is the expensive item. A single confidence threshold tuned for one audience is mistuned for the other, which is the concrete reason a shared review service needs per-surface configuration rather than one global filter.
- Where this qualifies the existing precision argument in this wiki. [Low-false-positive bug finding is required for coding-agent trust](low-false-positive-bug-finding-is-required-for-coding-agent-trust.md) argues for precision because humans lose trust in a noisy reporter and stop reading it. This source supplies the opposite mechanism for the same conclusion: agents do not lose trust, so nothing stops a false positive from being acted on. Alert fatigue is a self-limiting failure; obedient rework is not.
- Practical consequence for measurement: an addressal-rate metric collected across both audiences mixes two populations whose behaviour differs by construction, since an agent addresses almost everything. Segmenting the metric by surface is a precondition for reading it. See [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md).
- Limits. Both claims are stated as operating observations with no incidence rate, cost, or example attached — no figure for how often the rework loop occurs, how many turns it burns, or what share of comments are nits. Uber reports no separate accuracy figure for the inner-loop surface. ([Provenance and Limits](../sources/20260828_EL123UNokkI.md))

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Low-false-positive bug finding is required for coding-agent trust](low-false-positive-bug-finding-is-required-for-coding-agent-trust.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Optimize Prompts Against an Asymmetric Cost Matrix, Not Flat Accuracy](optimize-prompts-against-an-asymmetric-cost-matrix.md)

Sources:
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 01:46-02:04, 11:56-12:47
