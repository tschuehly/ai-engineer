# Size Agent Quality Against the Channel's Reply Rate

Summary: Before automating a channel, look up its base response rate — when roughly one in a hundred contacts replies, the value of the whole program lives in a thin margin, and an agent making mediocre decisions does not degrade results proportionally, it removes the margin that was the point.

Use when:
- Deciding whether an agent is good enough to run a customer-facing channel unsupervised.
- Arguing about how much quality work an automated outreach or notification system justifies.
- Choosing which channel to automate first when several are available.
- Setting the acceptance bar for an agent whose output is judged by a rare positive outcome.

Details:
- The base rates are third-hand but specific: "this is a series of statistics from [Smartlead]. This is across, I think, 20 million emails. And so, you can see we've got somewhere between a half a percent and 1% reply rates." ([Berry](../sources/20260826_UhCY231d0FQ.md), 14:05-14:19)
- **The argument from the rate to the quality bar.** "If we've got 100 contacts that we're sequencing, maybe one of them will reply. And so, that really raises the stakes for agentic execution within GTM because if your agents are doing the wrong things, then you're missing out on the margin, which is where most GTM teams are having success." (14:19-14:39)
- The reasoning generalizes past email to any rare-positive channel: when the outcome rate is around 1%, an agent error that costs a fraction of the responders costs a large fraction of the program, and the usual quality metrics — a pass rate, a human rating of the drafts — are computed over the 99 messages that were never going to convert anyway.
- **The channel ranking, with the speaker's own caveat.** "Cold email works less and less well as the years go on. This is a trend that's been true forever… I actually think these are pretty elevated rates for some of these, but the relative differences between these channels is correct. So, LinkedIn can be three to four times more effective than cold email. Cold calling and cold email are roughly the same." Treat this as an ordering claim, not as rates: the speaker discounts the absolute values on his own slide. (13:42-14:05)
- A corollary for evaluation design: with a 1% positive rate, per-message quality judgments are cheap and nearly uninformative, while outcome measurement needs volume most teams do not have per variant. That is the same difficulty [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md) hits from the internal side, and an argument for judging these agents on trajectory and policy compliance rather than on outcome alone.
- The rate also bounds the upside claim of automation. Sending more, faster, at a rate that is falling year over year is the failure mode the numbers describe; the case for the agent has to be better decisions per contact, not more contacts — which is why the surrounding architecture puts the agent at the decision layer rather than at the send.
- **Limit.** The reply figures come from a third-party vendor's aggregate ("I think, 20 million emails"), with no segment, industry, or method, and the speaker explicitly distrusts the absolute values on the chart he is showing. No measurement is offered of what an agent-run sequence achieves versus a human-run one, which is the comparison the argument needs. (13:42-14:39)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Protect Sender Reputation by Splitting Domains and Routing Replies Home](protect-sender-reputation-by-splitting-domains-and-routing-replies-home.md)
- [Run One Dormant, Long-Lived Agent Per Account](run-one-dormant-long-lived-agent-per-account.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)
- [Optimize Prompts Against an Asymmetric Cost Matrix](optimize-prompts-against-an-asymmetric-cost-matrix.md)
- [AI Does Not Replace Shareable Product Marketing](ai-does-not-replace-shareable-product-marketing.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 13:42-14:39
