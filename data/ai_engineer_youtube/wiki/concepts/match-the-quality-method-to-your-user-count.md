# Match the Quality Method to Your User Count

Summary: Ask how many users a product has before recommending anything about its quality process, because the answer changes which methods exist at all. At a hundred million messages a day you can experiment on a slice of the free tier; at five users A/B tests are meaningless. Neither end implies lower stakes.

Use when:
- Giving or receiving generic advice about evals, experiments, or monitoring.
- A team with a handful of users is being told to run A/B tests, or a team with millions is relying only on hand review.
- Deciding whether a statistical quality method is available before designing around it.
- Reading a case study and judging whether its scale resembles yours.

Details:
- The question comes first: "another question we get a lot is like, 'Oh, like what should I be doing?' And… the first question I always ask people is like, 'How many users do you have?' Like, we have customers with millions of users and we have customers with like five." ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 14:27-14:43)
- The consequence is not a tuning parameter: "it does mean you just like should… have to have a radically different uh approach." (14:59-15:03)
- **High volume unlocks experimentation.** "On the like 10, 20, 100 million messages a day side of things, like experiments become extremely valuable. Uh if you have a free tier, you can like run experiments on a very small sample of your free tier." The free tier is named specifically as the risk-bounded surface to experiment on. (15:03-15:19)
- **Low volume forecloses it.** "Obviously, if you have five or 10 users, like uh, I would not recommend, you know, experiments or AB tests, etc." (15:19-15:26)
- **Low volume does not mean low stakes**, and this is the part usually missed: "customers with five users like especially if let's say it's like an internal um app in an enterprise context where it's like giving like very critical information. Like, it could be very very important to get correctly." Consequence per interaction and count of interactions are independent axes. (14:47-14:57)
- What is left at the low end is what the talk spends the rest of its time on: read the traces, and know onset and share for each issue — where "share" of five users is a small integer you can reason about directly ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)).
- **This is the precondition the wiki's suite-sizing arithmetic assumes.** [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md) computes that catching a 1% failure rate with confidence takes ~450 tests and seeing it ten times takes ~1,900. That arithmetic is about *tests you construct*, so it survives at low user counts — but its sibling method, continuous human evaluation over hundreds of thousands of real conversations, does not. Read together: consequence sets the target error rate, user count sets which instruments can measure against it.
- The two pages also disagree usefully about where the burden falls. Hippocratic AI's answer to a high-consequence, high-volume product is a standing human evaluation operation; this source's answer to a high-consequence, five-user product is that no statistical method applies and you are reading traces. Both are correct for their quadrant, and the quadrant is set by the two axes above.
- Caveat: the thresholds are conversational, not derived — "10, 20, 100 million messages a day" versus "five or 10 users" leaves the entire middle unaddressed, which is where most products actually sit. No guidance is given for the thousands-of-users range where experiments are underpowered but hand review no longer scales.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [A Harness Switch Invalidates Most of an Eval Suite](a-harness-switch-invalidates-most-of-an-eval-suite.md)
- [Lab Eval Vocabulary Does Not Transfer to Application Teams](lab-eval-vocabulary-does-not-transfer-to-application-teams.md)
- [AI system evaluation still depends on human review](ai-system-evaluation-still-depends-on-human-review.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 14:27-15:26
