# Rate-Limit Every Write With a Ceiling That Refills

Summary: Put a per-window cap on every write an agent can make, with no exceptions — only the size of the cap varies with blast radius. The cap refills on its own, so exceeding it costs a wait rather than a ticket, and the agent keeps full autonomy underneath it while the worst a single runaway loop can do is bounded.

Use when:
- An agent has a write, delete, or state-changing operation it needs routinely, so removing the permission is not available.
- A single agent loop could repeat a legitimate action far more times than any human would.
- You are choosing between an approval prompt and a quota for a moderately risky operation.

Details:
- **The shape.** "Every caller gets a small amount of disruptive actions per time window. So you can spend them however you want. There's no approval, there's no waiting. And if you cross the line, the request simply bounces back with a count saying that you're exceeding your budget. You wait a bit and then the limit essentially refills." The property that follows: "the agent gets full autonomy within the limit. And there is a hard ceiling on how bad a single loop can get." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 08:34-09:01)
- **No exemptions, only sizing.** "Every write effectively gets a rate limit. There are no exceptions to that. What changes is the size of the rate limit" — larger for deletes inside your own namespace, smaller for resources in a shared one. Making the rule universal removes the argument about which operations qualify and moves it to a number, which is a thing you can tune after the fact. (09:01-09:16)
- **The deployed control.** After the workload-deletion incident, an adjacent team "built an admission web hook of sorts whose sole job is to cap the number of deletes at a fixed number per hour per resource kind per name space." The dimensioning is worth copying: the cap is keyed on the triple of rate, resource kind, and namespace rather than on a global counter. (09:19-09:35)
- **The override is real but the agent cannot reach it.** "There is always a bypass flag because sometimes you genuinely want to delete more than you're allowed for… And the part that I absolutely love in this case is that inside a Claude Code session or inside an agent session effectively the bypass flag simply refuses to do anything. All it's going to do is tell the agent to ask the human to run the command itself. So the agent effectively gets the rate limit and the human keeps the override and nobody effectively has to file a ticket for the limit because it just refills." This is a cleaner escape hatch than an approval queue: the emergency path exists, it is the same command a human already knows, and it produces a request to the human as its refusal message rather than a dead end. (09:35-10:03)
- **The bypass detection is the weak joint, and the talk does not defend it.** Recognizing "we are inside an agent session" is an in-band check, and no mechanism is named for it — not an environment variable, not a process ancestry check, not a credential distinction. That matters because the same talk's [identity argument](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md) is precisely that anything the agent can assert about itself is not a control. The robust version of this control routes the bypass through the same proxy that stamps identity, so the refusal is a property of who the caller is rather than of what the environment looks like.
- **What it would have caught.** Replayed against the opening incident: "the rate limit itself would have capped it at a few couple of tens of workloads" instead of about 200 in 90 seconds. It does not prevent the failure, it truncates it, which is the honest claim for this class of control. (14:44-14:53)
- **Relation to the wiki's cost-side caps.** The wiki already records [caps, notifications, and rate limits for billing surprises](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md) and a run-level [budget control plane](put-the-cost-control-at-the-agent-run-not-the-model-request.md). This is the same instrument aimed at blast radius rather than spend, and the transfer runs both ways: the cost-side literature's insistence that [a control must report completion rate](a-cost-control-must-report-completion-rate-or-it-is-just-throttling.md) applies here too, since a rate limit tight enough to never be hit is also tight enough to have made the agent useless, and this talk reports no such counter. It also inverts the halt-versus-[steer](steer-an-over-budget-run-before-you-kill-it.md) ordering: for a destructive write there is no in-place steer, so halting at the cap is the whole design.
- **Evidence limits.** No numbers for the cap itself, no rejection counts, no report of a legitimate operation blocked, and no measurement of whether the webhook has since bounded a real runaway. "A few couple of tens" is a retrospective estimate of what the cap would have done, not an observation.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)
- [Prefer Trip Wires to Allow Lists, Because Only One of Them Learns](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md)
- [Prevent AI billing surprises with caps, notifications, and rate limits](prevent-ai-billing-surprises-with-caps-notifications-and-rate-limits.md)
- [Put the Cost Control at the Agent Run, Not the Model Request](put-the-cost-control-at-the-agent-run-not-the-model-request.md)
- [Key rate limits by fingerprint or session instead of IP alone](key-rate-limits-by-fingerprint-or-session-instead-of-ip-alone.md)
- [An Empty Filter Stage Turns a Cleanup Into a Match-All Delete](an-empty-filter-stage-turns-a-cleanup-into-a-match-all-delete.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 08:26-10:03, 14:44-14:53
