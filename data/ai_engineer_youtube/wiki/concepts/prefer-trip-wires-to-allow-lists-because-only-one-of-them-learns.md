# Prefer Trip Wires to Allow Lists, Because Only One of Them Learns

Summary: An allow list is a guess about agent behavior written before you have any data about agent behavior, and it decays from the day it ships. A trip wire is an aggregate counter with a threshold that pages a human after the fact, which is how you get that data. Enforcement and observation are different jobs: caps bound the damage, trip wires tell you what the agent is actually doing so you can fix it.

Use when:
- Enumerating up front which actions, paths, or arguments an agent is permitted, and the list keeps growing.
- Individual agent actions each look reasonable and the problem only appears in aggregate.
- Deciding what to instrument for an agent that already has a hard cap on its writes.

Details:
- **The asymmetry that names the page.** "An allow list is effectively a guess that you're making up front about what the agent needs or about model behavior itself… it's pretty static and you write it up front before you have any data on how the agent is behaving in different situations. A trip wire on the other hand is how you get that data after the fact… allow lists don't really get better over time. They can get stale but trip wires do get better over time." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 10:05-11:03)
- **They are complements with different jobs, not competitors.** "Rate limits are the enforcement… they put a hard limit on the rate itself. Trip wires are how you find out what actually happened so you've got something to react to." For cheap actions, "you let the agent act and every action gets recorded with the actor identity stamp." (10:24-10:46)
- **Watch the aggregate, not the call.** "You effectively watch the aggregate and not individual calls." This is what makes trip wires catch a class of failure no per-call gate can see, and the worked example is exactly that case: the agent opened investigation threads for dozens of jobs that all failed with the same error signature, and "each thread effectively looked reasonable on its own, but if you took them in aggregate, you would realize that it was actually an infrastructure failure that was causing the same test failure signatures across the board." A per-action approver would have approved every one of them. (10:46-10:51, 11:30-11:47)
- **The instrument is one number with a baseline.** They track "the number of investigation threads that our agent is launching per hour for a given test job failure." One morning the number was far above baseline and the wire fired. The design guidance is that the number should be chosen so that its *normal* value is known, which is what "above the baseline" requires. (11:04-11:16)
- **A trip wire that does not page is decoration.** "The trip wire pages on call, and that part's important because a trip wire that nobody sees is practically useless." (11:13-11:23)
- **It is explicitly a detector, not a lock.** "It pages after the write has already happened, after the limit has been crossed, not before. It's effectively the smoke detector, not the lock on the door." This is why it only composes with an enforcement layer; on its own it converts an unbounded failure into a fast-but-still-real one. (11:23-11:30)
- **The fix a trip wire produces is usually a sentence.** "Usually when a trip wire goes off the fix is like maybe one or two lines in the agent's context and not really a big code change." In the worked case: tell the agent to correlate failures across test jobs before launching a separate investigation thread, and "the next time when this happened, it did exactly that." That makes a trip wire a discovery mechanism for context engineering, which is the loop the wiki records elsewhere as [demand-driven context capture](demand-driven-context-pulls-knowledge-from-failed-work.md) arriving from the operations side rather than the onboarding side. (10:51-10:57, 11:47-12:10)
- **Where the wiki disagrees, usefully.** [Version-controlling and unit-testing the permission policy](version-control-and-unit-test-the-agent-permission-policy.md) treats the enumerated policy as production code worth regression-testing, which presumes it is a durable artifact; this page's claim is that its *content* is a guess that ages. Both can hold: test the policy you have so changes to it are safe, and expect the trip wire rather than the review to tell you which entries were wrong. The sharper conflict is with denylist-style enforcement, where the wiki already records that [naming programs does not block an effect](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md) — that page says enumeration fails because the namespace is open, this one says enumeration fails because the author has no data yet. Different mechanisms, same conclusion about lists written in advance.
- **Evidence limits.** One trip wire, one firing, one fix, and one reported recurrence handled correctly. No false-positive rate, no count of wires deployed, no statement of the threshold or how the baseline was established, and no evidence that the context-line fix held beyond that single subsequent occurrence. The claim that allow lists go stale is asserted rather than demonstrated.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Security](../topics/security.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Rate-Limit Every Write With a Ceiling That Refills](rate-limit-every-write-with-a-ceiling-that-refills.md)
- [Give the Agent the Verbs That Fail Loudly](give-the-agent-the-verbs-that-fail-loudly.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Version-Control and Unit-Test the Agent Permission Policy](version-control-and-unit-test-the-agent-permission-policy.md)
- [Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 10:05-12:10
