# Run a Jury of Analysts and a Consensus Judge for No-Ground-Truth Questions

Summary: For subjective questions where no single pass can be trusted and there is no empirically correct answer, don't let one agent answer directly. Spin up several independent analysts who each examine the data and return an evidence-cited opinion, then have a consensus judge treat those opinions as input (not fact), weigh their reasoning quality, and synthesize the final answer — escalating and expanding the jury when consensus is weak.

Use when:
- A question is high-stakes and subjective with no objective ground truth (e.g. multi-touch attribution credit, litigation strategy, prioritization calls).
- A single agent pass "perseverates" or produces a confident answer you can't verify.
- You want the *same* question judged from multiple independent angles, not several different subtasks reconciled.

Details:
- Motivation: a class of go-to-market challenges "has no empirically correct answer"; the real-world model for these is a trial by a jury of peers, so the agent workflow mirrors it. (13:49-14:06)
- Jury: instead of answering immediately, the agent spins up a team of independent analysts who "all look at the data independently and come up with an evidence-cited opinion" for the answer (e.g. the attribution credit of a deal). None is necessarily correct; each is independent research. (14:11-14:33)
- Consensus judge: a judge node receives the analysts' opinions, "not treating these as fact… treating them as input," weighs the *reasoning quality* of each analyst, and produces the final version. Its job "is not to do research on my own" but to synthesize a team of independent analysts each doing a good job of research. (14:33-15:01)
- Escalation: "if there's not enough consensus, then I'll escalate and expand the jury" — widen the panel until the judge can reach a defensible result. (14:44-14:50)
- Why it works: "multiple researchers with somebody who helps at the end is better than a single person kind of perseverating on that forever" — this is a human pattern reused for agents. (15:01-15:15)
- Upside runs this for multi-touch attribution ("the holy grail of go-to-market"), "enabled by Opus," after two years building the underlying AI-native data layer. (13:16-13:49)
- Distinct from reconciling *heterogeneous* specialist outputs (a security agent + a Jira agent + a diff agent combined by a judge): here every juror attempts the *same* subjective task independently, and the judge weights reasoning quality rather than stitching different slices together.
- **What has to be true for the jurors' independence to be real.** A jury only beats one analyst if the votes are not correlated, and Coyle names a mechanism that correlates them: "when you get a bunch of agents together collaborating and talking to each other, there's a tendency to have group think. And all the agents seem to kind of devolve into one idea." His remedy is to control the shared input rather than the panel size — give each agent "only a slice," and withhold from a critic "the thought processes that went in to creating this claim" ([Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)). Whether jurors here see each other's work, or a shared upstream reasoning trace, is the design decision that determines whether the consensus means anything. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12)
- **A cheaper shape for the same no-ground-truth problem, with a named cost.** Cloudflare's weekly business summary uses a sequential chain rather than a jury — drafter, then a veracity checker, then a tone agent — over data that was pre-aggregated so the analysis has fewer degrees of freedom. It is a fraction of the token cost of parallel analysts plus a judge, and it produces no disagreement signal: a jury's spread is itself evidence about how contestable the answer is, and a chain gives you one answer with no measure of its stability. The chain's substitute for that signal was a human reading every run for two to three months. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 10:04-11:55)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Business Intelligence](../topics/business-intelligence.md)

Related concepts:
- [Reconcile specialist agent outputs with a feedback-weighted judge](reconcile-specialist-agent-outputs-with-a-feedback-weighted-judge.md)
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)
- [Read Every Run for Months Before Trusting an Unevaluatable Narrative](read-every-run-for-months-before-trusting-an-unevaluatable-narrative.md)

Sources:
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](../sources/20260711_YZQsWVeN3rE.md), 13:16-15:15
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 13:44-15:12
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 10:04-11:55
