# Score Agent-Readiness Against a Moving Baseline

Summary: Third-party graders that score whether a site is agent-ready now exist, but their rubrics change faster than most sites do — one team's score fell from "a lot higher" to 59 in three weeks without the site changing. Use them as a rediscovery mechanism for new conventions, not as a KPI, and re-measure on a cadence rather than treating a good score as banked.

Use when:
- Looking for a way to check whether agent-experience work landed.
- Tempted to put an agent-readiness score on a dashboard or an OKR.
- Deciding how often to revisit `llms.txt`, Markdown surfaces, and other agent-facing files.

Details:
- **The tooling gap, and that it closed recently.** When the talk was written "there was not really any like test suites yet, or test harnesses, on like is your site agent ready?" Cloudflare shipped one; the speaker's preferred one is Aura AI (as heard), "brand new and it tests a lot," used by submitting a URL and receiving recommendations. ([Burns](../sources/20260826_V_5bn4q-vAI.md), 12:48-13:33)
- **The score moved because the grader did.** "I'm happy to show off score of 59 because it's constantly changing. 3 weeks ago, it was a lot higher." The site did not regress; the rubric added checks. A metric whose denominator is redefined by a third party on a weekly cadence cannot carry a target, but it is a useful *diff*: the drop is a list of conventions that appeared since you last looked. (13:07-13:27)
- **What to do with it instead of a target.** Read the delta rather than the level. A falling score with no deploys is a changelog of the agent-readable web; a falling score after a deploy is a regression. Distinguishing the two requires re-running on a schedule, which is the actual operational commitment this page asks for.
- **This is the general shape of agent-experience measurement, not a quirk of one grader.** The wiki records the same non-stationarity from the model side: a fixed GEO prompt set re-run on a newer model produced a *worse* result, not a better one ([Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)). Both cases break the assumption that a measured improvement stays measured. The curb-cut framing has the same caveat attached — agent experience is a maintained surface with a rerun cadence, not a one-time capital improvement ([Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)).
- **The pairing that makes an external score interpretable.** A grader tells you which conventions you are missing; it does not tell you whether an agent succeeded at your task. Pair it with a first-party outcome measurement — running agents with and without your tool and reading the traces ([Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)), or tokens per successful outcome ([Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)) — and treat the grader as the cheap standing check between them.
- **The disposition the source draws from it.** "There is no such thing as perfection… never get caught with being perfect. Every small little increase really does matter." Applied to measurement: the point of a score that will not stay put is to keep producing next actions, not to be finished. (13:33-14:10)
- **Limit.** One reading of one grader by an interested party, with no rubric published, no explanation of which checks were added, and no independent verification that the drop was rubric change rather than site drift. The transferable claim is about non-stationarity; the specific score carries no information.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Benchmark Your Own Tool by Running Agents With and Without It](benchmark-your-tool-by-running-agents-with-and-without-it.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts](measure-agent-recommendations-on-pain-prompts-not-comparison-prompts.md)
- [Generate Agent-Facing Docs Artifacts From One Markdown Source](generate-agent-facing-docs-artifacts-from-one-markdown-source.md)
- [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)

Sources:
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 12:48-14:10
