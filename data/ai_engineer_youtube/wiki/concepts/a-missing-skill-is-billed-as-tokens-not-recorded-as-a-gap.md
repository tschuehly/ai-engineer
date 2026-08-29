# A Missing Skill Is Billed as Tokens, Not Recorded as a Gap

Summary: An unwritten skill produces no defect, no ticket, and no failed test. It is paid for silently, in the steering iterations each engineer performs alone to get the agent to do the thing the skill would have stated — which means the observable signature of a library gap is elevated cost and time on a recurring class of task, not a visible hole in the catalog. Cost per outcome, read per task class rather than per engineer, is the leading indicator.

Use when:
- Deciding which skill to write next, with no bug list or feature request pointing at one.
- Explaining why an agent rollout is expensive without being obviously broken.
- Interpreting a team that scores average on productivity and quality but sits far above its peers on spend.
- Arguing for skill-library investment to someone who only sees the token bill.

Details:
- **The mechanism, stated concretely.** Touil's worked case is a regulation skill that does not exist: "if we don't have a skill about the regulation, that is someone is vibe coding back and forth and trying to figure out exactly how to steer the agent to implement it properly. That is burning more tokens from one side cost-wise, but also the productivity is spending more time rather than giving in one shot the right answer." ([Touil](../sources/20260828_M05vON8i0aI.md), 16:18-16:42) The knowledge still gets applied; it is just re-derived conversationally, from scratch, by each engineer who needs it.
- **Why the gap stays invisible.** Nothing fails. The engineer eventually gets a correct implementation, so there is no incident, no regression, and no reason to file anything. The absence is only detectable in aggregate — across many engineers repeating the same steering — and the only place that aggregate is already being recorded is the spend and the elapsed time. "This is already happening within your organization — is teams are creating and using the skills, but we don't have visibility." (16:05-16:18)
- **The signature to look for: average on everything else, expensive.** Reading one simulated team, Touil lands exactly on the pattern that makes this diagnosable: "you can see the productivity of this team is a kind of a medium… low-medium productivity, quality and security also medium — but when it came to the cost is really high." (16:57-17:15) A team that is unremarkable on output and quality but an outlier on spend is not necessarily using the tools badly; it may be re-deriving, every time, something no one has written down.
- **The reconciliation this page owes.** [Do Not Use Token Volume as a Developer Productivity Metric](do-not-use-token-volume-as-a-developer-productivity-metric.md) is right and this page does not contradict it. Three differences make the reading legitimate. The *unit* is a task class, not a person. The *direction* is inverted — that page warns about low spend being read as "not trying"; here high spend for an ordinary outcome is the signal, so the incentive to game upward disappears. And the *conclusion* is a platform action (write the skill) rather than a judgment about an engineer. Attach it to a person or a leaderboard and it converts straight back into the metric that page warns about.
- **How it relates to the harness-diagnosis reading.** [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md) already treats heavy context burn on tasks that are not hard as a symptom of a misconfigured setup. This adds the attribution step: if the burn is spread evenly across work, suspect the harness; if it concentrates on one recurring class of task — the compliance review, the migration, the release write-up — suspect a missing skill for that class. The distinguishing question is whether different engineers' transcripts converge on re-explaining the *same* constraints.
- **The instrument panel Touil proposes, and what it is worth.** His simulation tracks four per-team measures: skills per engineer contribution, average skills utilization (how many times skills are pulled per day), duplication ratio across teams, and a combined quality-and-security ratio. (15:32-16:05) As a dashboard sketch these are reasonable and cheap to collect once a catalog exists; utilization in particular is the one metric that distinguishes a library that is stocked from one that is used. But they are parameters of a model he wrote, not measurements from a deployment, and no threshold or baseline value is given for any of them.
- **The corollary for prioritization.** If gaps surface as spend, the ranked backlog of skills to write is derivable without asking anyone what they want: sort recurring task classes by cost-per-outcome and start at the top. This is the same conclusion [Mine Agent Conversation History to Generate Missing Skills](mine-agent-conversation-history-to-generate-missing-skills.md) reaches from the transcript side (find where you and the agent went back and forth to remove ambiguity), and the two are the same signal seen from two ledgers — one measures the back-and-forth directly, the other measures what it cost. Where transcript access is restricted or fragmented across teams, the billing view survives.
- Limits. Nothing in this talk is measured. The fifteen-team, six-month simulation is synthetic and self-authored, with team sizes and metric values assigned by the speaker; it illustrates the claimed dynamic rather than testing it. No real organization's cost data appears, and no figure is given for how much a missing skill actually costs. See the source's [Provenance and Limits](../sources/20260828_M05vON8i0aI.md).

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Do Not Use Token Volume as a Developer Productivity Metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [Mine Agent Conversation History to Generate Missing Skills](mine-agent-conversation-history-to-generate-missing-skills.md)
- [Measure AI Engineering Impact Across Utilization, Impact, and Cost](measure-ai-engineering-impact-across-utilization-impact-and-cost.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)

Sources:
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 15:32-17:15
