# Stage Productivity Pilots to Strip One Confound at a Time

Summary: A single spectacular internal AI result does not travel, because everyone who hears it can name the reason it would not work for them. Amazon answered by running three studies in sequence — each one designed to remove the objection that invalidated the last — ending with 50 ordinary teams in brownfield codebases where the tool was roughly held constant and the outcome still split in half.

Use when:
- You have one lighthouse team's result and are being asked whether it generalizes.
- Designing an internal AI-productivity pilot that has to survive scrutiny from people who did not run it.
- Deciding how fast to roll a new way of working across a large engineering organization.

Details:
- **The ladder, with each rung's confound named by the speaker herself.** *Bedrock Mantle*: a new inference data plane "estimated at 30 people over 18 months," instead built by "six people… in 76 days with Kiro" — "truly the pathfinder team that proved that it was possible to get up to 20X improvement," measured on commits. Its confound: those six were "some of the top engineers literally in the company including two distinguished engineers… experts in distributed systems, experts at LLMs and their architecture," on a greenfield build. ([Liguori](../sources/20260828_pqlWNihgdjI.md), 02:22-03:50)
- *Prime Video*: a 10-day sprint with "six engineers in a room" that "brought down the project delivery time estimate from what was going to be 90 weeks down to 24." This removes the elite-staffing objection and introduces two of its own, again stated on stage: "they had no on-call duties, limited meetings, very few distractions," and "the senior engineer on the team had spent the previous 3 weeks creating very detailed, small, well-scoped tasks with detailed requirements for these six engineers to just go churn on." Her own verdict: "this was again not necessarily real life." (04:05-05:47)
- *Amazon Stores*: 50 teams with a "normal distribution of early career folks, mid-career, senior engineers," on "existing systems with existing code bases. Nothing green field," watched "for the better part of last year." The metric moved too — from commits to "deployment velocity to production. So, not just commits… how quickly are we getting changes out to customers?" (05:48-06:50)
- **What the third study buys that the first two cannot.** The tool is roughly constant — "90% of these teams used Kiro, among other internal tools that we have" — and the outcome still splits: "for half of the teams, they achieved less than 3x increase," against "a median of 4.5x, and in some cases more than 10." That design cannot show a tool is unnecessary, because no team worked without one. It shows the tool is *not sufficient*, which is the more useful claim and the harder one to get from a lighthouse story. The reported differentiator: teams that gained "intentionally changed the way that they worked, and the other simply kind of sprinkled Kiro and some of the other tools that we have on top of their existing way of working." (06:50-07:34)
- **Sequencing the pilot is also what produces the playbook.** Liguori names going "too broad in the organization too fast" as an organizational failure mode with a specific cost: "if we had expected all teams in massive organizations to be frontier teams immediately, we would not have had the learnings that we had from the Pathfinder, from the sprint experiment, from the pilot teams." Rolling out early means "you have a lot of teams who don't know what they're doing. You haven't had time to find the best practices for your own organizations, the context that your organization needs." The staged design and the phased rollout are the same decision seen from two sides — evidence quality and learning rate. Amazon's stated 2026 problem is the next step: "how do we scale this out… to the next 2,000 teams instead of 50 teams." (17:54-18:46)
- **How to apply the pattern rather than the numbers.** For each result you want to propagate, write the sentence a skeptical team would say ("sure, but they had X"), then design the next study so that sentence is false. Amazon's sequence eliminated, in order: elite staffing, greenfield scope, protected conditions, a pre-decomposed backlog, and small-n. What it never eliminated is the tool itself, and the vocabulary should follow — this is evidence about *practice under a tool*, not about the tool.
- **Where the ladder stops short.** Every rung is measured on an output proxy — commits, then deployments — with no defect rate, rework, revert, incident, or review-cost adjustment anywhere, so the escalating rigour is entirely about *who and where*, not about *what counts as a gain*. A fourth rung would fix the metric. The first two comparators are also estimates rather than observed alternatives: "30 people over 18 months" and "90 weeks" are what the projects were *forecast* to take.
- Provenance: self-reported internal Amazon figures presented on slides, from a speaker who works on the tool used in all three studies. No sample sizes per group, no distribution, no baseline window, no variance, and no reported case of a team that changed how it worked and did not improve.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Coding Agents](../topics/coding-agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Measure AI Developer Productivity With Field Experiments, Not Benchmark Extrapolation Alone](measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md)
- [Codebase Hygiene Amplifies AI Productivity Gains](codebase-hygiene-amplifies-ai-productivity-gains.md)
- [Budget the Productivity Dip That Precedes the Agent Speedup](budget-the-productivity-dip-that-precedes-the-agent-speedup.md)
- [Measure AI Transformation by Outcomes Instead of Adoption](measure-ai-transformation-by-outcomes-instead-of-adoption.md)
- [Move enterprise AI adoption beyond spot experiments](move-enterprise-ai-adoption-beyond-spot-experiments.md)
- [Do Not Use Token Volume as a Developer Productivity Metric](do-not-use-token-volume-as-a-developer-productivity-metric.md)

Sources:
- [From AI-Assisted to AI-Native: Building a Frontier Development Team — Clare Liguori, AWS](../sources/20260828_pqlWNihgdjI.md), 02:22-07:34, 17:54-18:46
