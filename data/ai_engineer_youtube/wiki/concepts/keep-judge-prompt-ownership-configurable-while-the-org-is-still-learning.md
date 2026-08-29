# Keep Judge-Prompt Ownership Configurable While the Org Is Still Learning

Summary: Across DoorDash's product teams, the judge prompt is owned by strategy-and-operations in some teams, the product manager in others, and engineering in others. The platform team treats that spread as evidence the org design has not converged rather than as inconsistency to standardize away, and deliberately ships a platform on which all three arrangements work. The bet is that encoding an ownership model into tooling freezes an answer the organization has not found yet.

Use when:
- Deciding whether an internal quality platform should prescribe who owns rubrics, judges, or rules, or merely permit any owner.
- Different teams have settled on different owners for the same artifact and someone is proposing to standardize.
- Designing role and permission models for an eval or annotation platform early in its life.
- Reconciling "evals are a cross-functional job" with the need for a single accountable owner per judge.

Details:
- **The observation, stated plainly as a spread rather than a problem.** "This enables different configurations in different teams. In some teams you have seen the strategy and operations folks own the prompt, you have seen some teams where the product manager owns the prompt, you have seen some teams where engineering owns the prompt." ([Chitlur Haridas](../sources/20260828_bMjlRrWjdT0.md), 13:02-13:14)
- **The reading the team puts on it.** "So this gives the flexibility for teams to design and evolve because we are all learning. So even the org design is improving and we are enabling that." The platform is positioned as a substrate for an org-design experiment that is still running — the variation is the search, and standardizing early would end the search before the answer is known. (13:14-13:23)
- **What makes the flexibility real rather than rhetorical.** Ownership is configurable only because the calibration loop is self-serve: whoever owns the prompt can set the configs, run the optimization, read the [prompt diff](show-the-prompt-diff-so-a-non-engineer-can-promote-an-optimized-judge.md), and promote the result without an engineer in the path. A platform where only engineers can run the loop has already decided who owns the prompt, whatever its documentation says. "The overall idea was to build something which is as self-served as possible so that people aren't always necessarily blocked by our team helping them out." (11:35-12:19, 13:23-13:36)
- **It sits inside a division of labor the team does prescribe.** The four-role split is stated as a recipe: strategy and operations "set priorities, set the quality bar that you want to aim for"; product people "translate these requirements into rubrics, workflows"; operations teams run annotations; engineering provides "APIs, telemetry, data sets, judges." So the platform is not agnostic about the *stages* — it is agnostic about which of those roles holds the pen on the judge prompt specifically, which is the one artifact where the stages overlap. ([Paranjape](../sources/20260828_bMjlRrWjdT0.md), 04:33-05:19)
- **The cost, which the talk does not price.** Three ownership models across teams means no consistent accountability for judge quality, no comparable practice to transfer between teams, and no way for the platform team to know whose judgment is encoded in any given metric. The claim that the variation reflects learning rather than drift is asserted, not evidenced: no team is reported to have *changed* owners as a result of what it learned, which is the observation that would distinguish an experiment from a permanent inconsistency.
- **How it qualifies the wiki's platform-governance positions.** Uber's account of [distributed rule authoring](distributed-rule-authoring-is-a-platform-problem.md) concludes that a rule platform must bind to the org's existing ownership model rather than replicate one — a strong argument for the platform inheriting an answer it does not invent. DoorDash is the case where no existing ownership model covers the artifact at all, because "who owns the definition of quality for an AI feature" is a new question. The compatible reading: inherit ownership where the org already has it, keep it configurable where the artifact is genuinely new, and revisit once teams converge.
- **An independent report of the same product-side ownership pull, from a retail engineering manager.** Prio's instruction for a commerce agent's quality judge is not to build it in engineering: "I also recommend using LLM as a quality judge. You don't have to use something fancy. Talk to your product friends and figure out what's the best way to do it, and use best use cases and write them out." It is one more data point that judge authorship gravitates toward whoever owns the definition of a good outcome rather than toward whoever owns the harness — arrived at independently, in a different industry, at a much smaller scale of eval maturity. ([Prio](../sources/20260827_G7cgLjZtmMU.md), 18:29-18:44)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Show the Prompt Diff So a Non-Engineer Can Promote an Optimized Judge](show-the-prompt-diff-so-a-non-engineer-can-promote-an-optimized-judge.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)
- [Mature Eval Platforms From Spreadsheets Into Experiment Systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)
- [Treat Evals as the Home of Domain Knowledge](treat-evals-as-the-home-of-domain-knowledge.md)
- [Hand Domain Experts the Pipeline as Skills](hand-domain-experts-the-pipeline-as-skills.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Eval an Agent Surface for Protocol Compliance, Not Just Behavior](eval-agent-surfaces-for-protocol-compliance-not-just-behavior.md)

Sources:
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 04:33-05:19, 11:35-12:19, 13:02-13:36
- [The Agentic Commerce Stack — Ahnaf Prio, Best Buy](../sources/20260827_G7cgLjZtmMU.md), 18:29-18:44
