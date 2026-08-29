# Size Agent Controls With the Undo Test

Summary: Two questions size every other agent control: can the agent put it back by itself, and how bad is the impact if it gets it wrong. If both answers are acceptable, log the action and let it run. If either is not, the action needs a second key held by someone other than the agent, plus an audit record of why the second key was involved.

Use when:
- You have enforcement primitives — caps, scopes, gates — and need a principled way to set their thresholds instead of guessing.
- Deciding whether a particular agent action deserves a human at all.
- A design review is stuck on whether an action is "risky," which is not a question with an answer.

Details:
- **It is a lens, not an enforcement point.** "It's not something you effectively enforce in code. It's the question you ask when you're sizing the other three." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 12:12-12:24)
- **The two questions, and the branch.** "Can the agent put it back by itself? And how bad would the impact be if it actually got it wrong." If the agent can roll back its own change and the blast radius is acceptable, "you effectively log it and you let it go." If either answer is no, "you need a second key, and the second key is not something that the agent holds itself. It has to be someone else. And there has to be an audit record so that you can track what happened, why the second key was involved." (12:25-13:06)
- **It is deliberately distinguished from detectability.** "This sounds like asymmetric verbs in a sense, but it's kind of different because the verbs ask whether you would notice the failure and undo asks whether you can recover from it." The two axes are independent, so an action gets classified on both: [loud verbs](give-the-agent-the-verbs-that-fail-loudly.md) decide whether the agent may hold the verb at all, the undo test decides how much of it the agent may spend. (12:33-12:43)
- **A second key does not mean a new authorization system.** On a feature-flag service the agent has "the full dial" over canary — staging traffic plus dogfooding customers — including ramping a flag from zero to 100 and toggling it back off when bugs are filed, because all of that is reversible inside a bounded audience. Promoting a flag to production is not in its key; "the best that an agent can do for now… is that it can propose that someone actually promote the feature flag." The design note: "the second key in this scenario is not necessarily a new auth system. It's a scoped key for production and a scoped key for canary." Splitting an existing credential by environment *is* the second key. (13:07-13:57)
- **The full-autonomy consequence, stated by an operator.** With canary reversible and production gated, the day-to-day is asking the agent in Slack to own the whole rollout loop, answering one clarifying question about audience, and "the important part is that I'm not in the middle of any of these things." The undo test is what earns that: reversibility inside canary is why no per-step approval is needed there. (13:59-14:18)
- **The worked sizing.** Against the opening incident: "the undo test… will basically tell you that you can't un-delete a running job in someone else's namespace. So anything past the cap basically needs a human with a second key." Note the composition — the cap comes from the rate limit, and the undo test is what says the cap must be a hard stop rather than a soft warning. (14:44-15:03)
- **Where this refines the wiki's existing rules.** Amazon AGI Lab's [calibrated-confidence](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md) rubric already lists irreversibility and impact among four properties, and Coyle's [confidence check at the loop exit](route-high-impact-agent-actions-through-explicit-human-approval-gates.md) already assumes intermediate steps are reversible. What this adds is a different owner for the judgment: there the model estimates reversibility at act time, here a human answers it once at design time and the answer is compiled into a scope split. The design-time version cannot generalize to unenumerated actions; it also cannot be wrong at 3 a.m. because the model was miscalibrated. The two layer in the order the wiki already records — learned estimate first, enforced boundary behind it.
- **Evidence limits.** The canary/production split is the only worked instance, and no outcome is reported for it: no count of proposals the agent made, no rate at which humans accepted them, and no case where the second key caught something. The "how bad would the impact be" question has no scale, threshold, or worked disagreement, so in practice it stays a judgment call the page does not make easier.

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Give the Agent the Verbs That Fail Loudly](give-the-agent-the-verbs-that-fail-loudly.md)
- [Rate-Limit Every Write With a Ceiling That Refills](rate-limit-every-write-with-a-ceiling-that-refills.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)
- [An Audit Trail Is a Chain of Evidence, Not a Developer Log](an-audit-trail-is-a-chain-of-evidence-not-a-developer-log.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 12:12-15:03
