# Replace the Token's Boolean With a Budget on Four Dimensions

Summary: A token is a boolean — a static list of scopes you either hold or do not — so the only tuning knob it offers is narrower or wider, and both ends fail. A budget is the replacement data type, with four independent dimensions: how much the agent can do, how fast, what it can undo on its own, and who notices while it acts. Each dimension gets its own control, so an agent can keep a verb it needs while being bounded in how far that verb can go.

Use when:
- An agent incident has just happened and the reflex fix on the table is "take that permission away."
- Designing the authorization story for an agent that does real, repeated production work rather than a demo.
- A permission model has only allow and deny and you need somewhere to put "yes, but not two hundred of them in ninety seconds."

Details:
- **The failure this replaces is not a model failure.** After an agent's self-cleanup deleted about 200 workloads in 90 seconds, the operator's own conclusion was: "the agent technically hadn't done anything that I couldn't have done. It was using my token after all. The failure wasn't the model itself. The failure was that I was giving the agent unbounded amount of power to do something that I wasn't watching super intently." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 03:06-03:26)
- **Why the reflex fix is rejected.** "The standard fix for an incident like that is basically that you narrow the token scope… you just take the deletes away effectively. You would technically never do that for a new hire… And it also doesn't work for an agent either. Maybe it works for about a week, maybe two, but then you eventually end up in a situation where the agent is genuinely trying to delete something… and you will just be there sitting and pressing enter by hand all over again." The scope-narrowing fix does not fail loudly; it fails by quietly returning the human to the loop. (04:23-04:57)
- **The data-type argument, stated plainly.** "A token is a boolean. It's just a yes or no. It's a static list of scopes… If the token list is too tight, then your agent is effectively useless. If the token list is too wide, then you're maybe writing a postmortem." (04:57-05:18)
- **The four dimensions.** "How much can the agent do? How fast can it do it? What can it undo on its own? And then who's noticing while it's actually taking those actions?" Each of the talk's controls occupies one: [rate limits](rate-limit-every-write-with-a-ceiling-that-refills.md) answer how much and how fast, the [undo test](size-agent-controls-with-the-undo-test.md) answers what can be undone, [trip wires](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md) answer who notices, and [asymmetric verbs](give-the-agent-the-verbs-that-fail-loudly.md) decide which verbs enter the budget at all. (05:18-05:45, 14:27-14:42)
- **The organizing analogy is load-bearing and its disanalogy is stated.** "We don't basically sit around watching every engineer… type out every keystroke… there is always an escalation path… the catastrophic stuff is just structurally out of reach for them." Agents differ in that they "never get tired. They never sleep. And every so often they're just like very confidently wrong." The talk closes the loop: the four controls are "some sort of onboarding checklist for your engineers — what can a new engineer touch, how much rope do they get, who signs off on their operations, and how do we know it's effectively working? We just wrote it for people. It's now the same checklist that we want for agents." (03:30-04:21, 15:11-15:28)
- **You do not owe every write all four controls.** "You don't need all the checks in every write scenario. Only some of these might be relevant for whatever kind of action you're trying to evaluate." (15:03-15:11)
- **Where this stands against the wiki's other position.** The wiki records a well-evidenced case for [ratcheting agent permissions down](ratchet-agent-permissions-down-in-high-consequence-code-environments.md) in high-consequence environments, and that is exactly the move argued against here. They are reconcilable and the reconciling variable is stated in both: whether the withheld verb is one the agent needs *routinely*. Poolside's Ada codebases and AIDAChip's silicon are domains where the catastrophic verb is rare and structurally excludable; a CI agent that cannot delete workloads is an agent whose main job is now manual. The budget framing does not claim every verb should be granted — [asymmetric verbs](give-the-agent-the-verbs-that-fail-loudly.md) is a scope decision — it claims that for verbs the agent uses daily, scope is the wrong dial.
- **Evidence limits.** One incident and one team's practice, with no measurement of the budget model itself: no incident rate before or after, no count of times a budget bound an action that would otherwise have been destructive, and no report of an agent rendered less useful by any of the four controls. The claim that narrowed scope "works for about a week, maybe two" is an operator's estimate with nothing behind it.

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Give the Agent the Verbs That Fail Loudly](give-the-agent-the-verbs-that-fail-loudly.md)
- [Rate-Limit Every Write With a Ceiling That Refills](rate-limit-every-write-with-a-ceiling-that-refills.md)
- [Prefer Trip Wires to Allow Lists, Because Only One of Them Learns](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md)
- [Size Agent Controls With the Undo Test](size-agent-controls-with-the-undo-test.md)
- [Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)
- [An Empty Filter Stage Turns a Cleanup Into a Match-All Delete](an-empty-filter-stage-turns-a-cleanup-into-a-match-all-delete.md)
- [Ratchet agent permissions down in high-consequence code environments](ratchet-agent-permissions-down-in-high-consequence-code-environments.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [An Agent Is an Expert Who Onboards Again on Every Task](an-agent-is-an-expert-who-onboards-again-on-every-task.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 03:06-05:45, 14:27-15:28
