# Commit at Sprint Scale When Implementation Is Cheap

Summary: Long upfront requirements existed because implementation was the expensive step worth protecting; once building takes minutes, the expensive step becomes *arguing*, so the planning horizon splits into a one-year direction that assumes model progress, a two-to-four-week commitment that is the only real plan, and a three-to-six-month middle that becomes close to unplannable because multiple model releases will land inside it.

Use when:
- Deciding how far ahead an AI-assisted team should actually commit, or defending the removal of quarterly planning.
- Justifying why PRDs and technical design docs should shrink to one or two pages.
- Explaining why a team can reverse a two-week-old decision without treating it as a planning failure.

Details:
- The historical justification is named explicitly: teams "spend the weeks, sometimes the months to flesh out the business requirements, finalize the design, and then do the implementation… because implementation can be really expensive. If we didn't get the other part right in the beginning, it can be very costly to change it later." Two things break that logic — "we never get the sense and right in the beginning anyway for any of big projects," and "with AI, building is super fast. It's probably couple minutes you can get it done. Argument is really expensive one." (Maven Clinic, 06:58-07:47)
- The one-year view survives only as direction, and it is allowed to assume capability that does not exist yet: "you can assume AI models can do anything you want in one year. Based on that one, really dream big… but it should only serve as inspiration, inspiring, and directional." (07:47-08:11)
- The commitment horizon is the sprint: the ask to PMs and designers is "tell me what I need to deliver in this sprint," the engineer releases by sprint end or sooner, and the PM spends that window fleshing out the next batch. Reversal is designed in rather than penalized — "if at the end of this sprint, they say, 'No, what we decided two weeks ago is wrong.' It's totally okay. We can switch the gear, get it fixed quickly." (08:11-08:45)
- Document format follows from the cost shift: "we prefer people not write pages or pages of PRD or TDD anymore. We prefer them to write just a short one or two pages. That one is really serve as communication, so we can iterate on it." The document is an object to argue with, not a specification to satisfy. (08:45-09:01)
- The casualty is the mid-term plan, and the reason is model uncertainty rather than product uncertainty: "the really awkward part is mid-term goals. Those like a three months, six months. It's very hard to plan these days. The reason is I don't know what AI models will be capable in three months. There may be multiple releases already." He concedes this is the hardest part for experienced people used to quarterly or six-month planning, and treats adapting as the job. (09:01-09:41)
- Related pressure on the roles themselves: because senior engineers can implement their own designs instantly, "delegating to other people means more overheads and less efficient," so the plan-then-hand-off structure that long requirement documents supported has less to coordinate in the first place. (04:43-05:41)

Related topics:
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Rescope Ambition Down a Tier as Models Improve](rescope-ambition-down-a-tier-as-models-improve.md)
- [Ritualized Discovery Keeps AI Roadmaps Adaptive](ritualized-discovery-keeps-ai-roadmaps-adaptive.md)
- [Agentic Coding Collapses Coordination Tax for Small Valuable Changes](agentic-coding-collapses-coordination-tax-for-small-valuable-changes.md)
- [Retire Completed Planning Docs Before They Become Agent Doc Rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)
- [Coding Agents Shift Engineering Work Toward Planning and Review](coding-agents-shift-engineering-work-toward-planning-and-review.md)

Sources:
- [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../sources/20260819_WJRdLNhrsLQ.md), 04:43-09:41
