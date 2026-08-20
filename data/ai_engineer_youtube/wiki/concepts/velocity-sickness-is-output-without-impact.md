# Velocity Sickness Is Output Without Impact

Summary: Velocity sickness is "the stress caused by sudden output increases thanks to AI," whose result is "output without impact." It has four checkable team-level symptoms — a PR backlog that breaks the merge queue, work sprinting in incompatible directions, agent bankruptcy each morning, and critical decisions being made by agents — and its diagnostic value is that it separates *producing more* from *landing more*, which throughput metrics cannot.

Use when:
- A team reports feeling productive with agents while nothing seems to arrive.
- Deciding whether an agent rollout problem is a setup problem or a direction problem.
- Naming the failure mode for a team that is measuring PRs, tokens, or lines and seeing all three rise.

Details:
- The definition and the tell: "velocity sickness… the stress caused by sudden output increases thanks to AI. Um it affects individuals or teams. And the result is output without impact." The felt signature is a mismatch between expectation and experience — "we're moving really fast. This should feel great… but for some reason it doesn't feel awesome. We're not… the things you expect to be happening are not happening." (03:53-04:26)
- **Symptom 1 — PR volume.** "too many PRs to merge. This is the like classic first problem you hit when you start adopting AI as an engineer… you push up those PRs and you're like, 'There's no way I can merge all these.'… Merge conflicts, merge queue breaks down, things get bad." Note the specific failure named is the merge queue, not review time. (01:36-01:55)
- **Symptom 2 — divergence, at two scales.** Individually, "you have a bunch of agents doing different things. You're trying to remember who's doing what and your brain gets fried." Organizationally, engineers are "picking up things and running in a certain direction… Maybe some are bumping into each other and you're… not moving cohesively with focus because you're just sprinting in all sorts of directions." (01:59-02:25)
- **Symptom 3 — agent bankruptcy.** "you have like your 12 terminals open… at the end of the day you're like, 'Yeah, I did a lot of work'… Next morning you come back and it's like walking into just a room of strangers. Like, who are these people? What are they doing here?… They're agents so you just get rid of them and start over again." The cost is paid twice: "it feels like you're doing a lot of work but you're doing the same work and you're spending tokens twice," which at team scale is inefficiency "with both their time and their token resources." (02:26-03:13)
- **Symptom 4 — ceded decisions**, which Dailey calls "the most important one." Treated separately at [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md). (03:16-03:43)
- The generalized form of the whole failure comes from outside engineering, which is what makes it portable. A newsletter writer with a genuinely good agentic pipeline — "very very much not slop… using agents to amplify their own voice" — reported "I'm basically writing a book every week." Asked whether the audience was reading a book every week: "No, they're probably not." The pages "are going unread." Output rose; the thing output was for did not. (04:38-06:04)
- Why this is not just a throughput metric restated: three of the four symptoms are invisible to any count of shipped work. Divergence looks like high output. Agent bankruptcy looks like high output *and* high token spend. Ceded decisions look like clean, fast delivery. Only the PR backlog shows up as a queue.
- Distinguish from the wiki's other symptom checklist. [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md) diagnoses a *misconfigured harness or codebase* — babysitting, intervention rate, slop, context burn — and its fixes are retrieval structure, skills, and context budget. Velocity sickness can appear on a team whose setup passes that checklist entirely: the agents work, the code is fine, and the direction is unowned. The two lists share no symptom.
- Caveat on evidence: this is a vendor's framing (Ref sells a tool for the layer the talk prescribes), the four symptoms are offered from observation with no counts or team sizes attached, and the newsletter story is second-hand and about writing rather than software, with the parallel to engineering asserted — "I think it parallels our engineering workflows a lot." Treat the taxonomy as a diagnostic vocabulary, not as measured prevalence.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ceding a Critical Decision Transfers Ownership of the Code](ceding-a-critical-decision-transfers-ownership-of-the-code.md)
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [AI Output Speed Can Overwhelm Review Capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Measure Feature Adoption, Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)
- [Uneven Agent Adoption Loads Review Onto the Slowest Adopters](uneven-agent-adoption-loads-review-onto-the-slowest-adopters.md)

Sources:
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 01:36-06:04
