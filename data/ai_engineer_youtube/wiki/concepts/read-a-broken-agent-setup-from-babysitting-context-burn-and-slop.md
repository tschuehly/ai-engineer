# Read a Broken Agent Setup From Babysitting, Context Burn, and Slop

Summary: Five observable symptoms say a team's coding-agent setup is misconfigured, independent of what anyone reports about model quality: engineers babysitting runs, sessions needing constant intervention, a steady slop output, complaints that the model "got dumb today," and heavy context burn on tasks that are not hard.

Use when:
- Auditing a team's agent setup without a benchmark or an eval suite to run.
- Deciding whether a complaint about model quality is actually about the harness.
- Choosing where to start when "agents aren't working here" is the whole problem statement.

Details:
- **Babysitting.** "if you're babysitting your agents, it's not the right setup… If you're seeing people in your team babysitting their agents, something's wrong." This is the load-bearing symptom for Khandelwal, because it is visible from across the room and because it is what a trustworthy setup removes. ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 04:22-04:34)
- **"The model got dumb today."** "one of the things that I heard a lot was… insert whatever latest model there is being really dumb today. The model didn't change, right? The [harness] may have changed underneath. But if… that's acceptable to like small changes in the [harness], clearly your own code base isn't set up well." Two claims are stacked here: the attribution correction (the harness moved, not the model), and a fragility test — a setup that a small harness change can visibly degrade was already marginal. (04:34-04:54)
- **Silent context burn.** "It's silently burning context and money. Like you don't realize it… you blow through like 500k context, you might go to like 750k [or a] million and hit auto compact even though you're not doing like a really complicated task." The diagnostic content is the *ratio*, not the number: token spend disproportionate to task difficulty. For the sharper version of this test, run at the first prompt rather than at the end of a session, see [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md). (04:54-05:08)
- **Long sessions needing constant intervention** and **a constant slop factory** round out the list: "if you have long ass sessions needing constant intervention, there's still something that's wrong. If you're getting a constant slop factory, obviously… things are not good." Note that long runtime *alone* is not on the list — Khandelwal argues elsewhere that a long unattended run is a good sign; it is the intervention rate that indicts the setup. (05:08-05:20)
- A sixth, comparative symptom: "if you find yourself asking, you know, how are these other companies shipping so fast? Like how are model companies releasing models at like a month and a half two-month cadence? Clearly they have something which we don't." The inference he draws is that the gap is setup, not staffing or model access. (05:20-05:34)
- What the list rules out is as useful as what it includes. None of these symptoms is a model-selection problem, and none is fixed by more usage. Each points at the shared harness: retrieval structure, skill design, loop closure, or context budget.
- The attribution discipline generalizes in both directions. This page covers *harness moved, model did not*. The complementary failure is *model moved, harness did not* — see [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md), where machinery added for an older model's quirk keeps executing and costs latency and cache hits after the quirk is gone. Khandelwal names the pairing himself when triaging with an engineer: "if the model changed, the [harness] changed, again you need to go revisit something." (13:15-13:34)
- Caveat on the numbers: 500k / 750k / a million tokens exceed the context windows of the coding harnesses in common use at the time, and auto-compaction implies a window smaller than the total, so these read as cumulative session token spend rather than window occupancy. The talk names no harness, model, task, or repo size, so treat the figures as directional and re-derive local thresholds.

- A second symptom checklist exists in this wiki with **no overlapping entries**, and the disjointness is the useful part. Matt Dailey's four velocity-sickness symptoms — PR backlog breaking the merge queue, work sprinting in incompatible directions, agent bankruptcy each morning, and critical decisions made by agents — describe a team whose setup may be entirely healthy and whose *direction* is unowned. Khandelwal's list indicts the harness and the codebase; Dailey's indicts what the working agents are pointed at. Running both is cheap, and a team that passes one can fail the other outright. See [Velocity Sickness Is Output Without Impact](velocity-sickness-is-output-without-impact.md). ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 01:36-04:26)
- **An attribution step for the context-burn symptom.** Burn spread evenly across a team's work points at the harness; burn concentrated on one recurring class of task — the compliance review, the migration, the release write-up — points at a missing skill for that class, because the knowledge is being re-derived conversationally by each engineer who needs it. Touil's case is a regulation skill that does not exist, producing "vibe coding back and forth" that burns tokens and time "rather than giving in one shot the right answer." ([Touil](../sources/20260828_M05vON8i0aI.md), 16:18-16:42) The distinguishing question is whether different engineers' transcripts converge on re-explaining the same constraints. Nothing in the talk is measured.

- **The mechanism behind the load-bearing symptom, stated as arithmetic.** Khandelwal treats babysitting as a signal that something is wrong; Liguori explains why it caps the number: "if you are having a back-and-forth conversation with your agent all day long, of course you're not going to see four to five x productivity improvements because you are in the loop the entire time. You're probably sitting there for 30 seconds to a minute waiting for it to generate code." The consequence is that the human is serialized — "if you're sitting there waiting for it, then you can't go off and do other stuff… It's very difficult to clone yourself into multiple agents" — so a babysat setup has a ceiling of roughly one regardless of model quality, and faster models only shorten the wait. Her fix is a payload change rather than a harness change: send "what it needs to do and how it can self-validate," then promote those criteria into the steering file. See [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md). ([Liguori](../sources/20260828_pqlWNihgdjI.md), 11:21-12:31)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Own Agent Adoption at the Leadership Layer Because the Fixes Are Shared](own-agent-adoption-at-the-leadership-layer-because-the-fixes-are-shared.md)
- [Invest in One High-Value Skill to Convert Agent Skeptics](invest-in-one-high-value-skill-to-convert-agent-skeptics.md)
- [Codebase Hygiene Amplifies AI Productivity Gains](codebase-hygiene-amplifies-ai-productivity-gains.md)
- [Own agent context instead of accepting hidden harness mutation](own-agent-context-instead-of-accepting-hidden-harness-mutation.md)
- [Treat slop as a quality failure, not an AI provenance label](treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md)
- [Velocity Sickness Is Output Without Impact](velocity-sickness-is-output-without-impact.md)
- [A Missing Skill Is Billed as Tokens, Not Recorded as a Gap](a-missing-skill-is-billed-as-tokens-not-recorded-as-a-gap.md)
- [Being in the Loop Is the Ceiling on Agent Parallelism](being-in-the-loop-is-the-ceiling-on-agent-parallelism.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 04:22-05:34, 13:15-13:34
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 01:36-04:26
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 16:18-16:42
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 11:21-12:31
