# Curate Tasks by Live Human Demand and a Deterministic Verifier

Summary: Einstein Arena admits a problem only if both conditions hold: an existing community of human researchers already cares about it, and a well-defined deterministic verifier can score any submitted solution. The first condition makes a win worth something outside the leaderboard; the second makes the leaderboard possible at all. Neither alone is sufficient, and most candidate problems fail one of them.

Use when:
- Choosing which problems to open to a fleet of agents, and needing an admission rule rather than a wish list.
- Building an eval or RL task set and deciding what qualifies before writing any tasks.
- Explaining why an agent scored well on your benchmark and nobody cared about the result.
- Assessing an "AI made a discovery" claim: ask who was already working on the problem and what checked the answer.

Details:
- The two-part filter, stated as the curation rule: "first, there's actually an existing community of human researchers that are interested in these problems. So, these are important problems for human scientists. And second is that for each of these problems, we can actually create a well-defined and deterministic verifier to assess the quality of the solutions to each of these problems." (02:47-03:21)
- **The human-demand condition is doing more work than it looks.** It supplies the prior state of the art, so "better" is measurable against something real rather than against a baseline you wrote; it supplies people who will notice and check a surprising result; and it gates out problems where a verifier exists but the answer is worthless. The kissing-number problem passes because a research community has worked it "for the last several centuries" *and* because denser packings "create the better coding systems including ways of doing error correction codes for information transfer" — the value is not internal to the arena. (05:12-06:17, 07:34-07:56)
- **The verifier condition is the harder gate and it excludes most interesting science.** "Deterministic" rules out judge models, rubric scores, and expert review. A packing can be checked; a hypothesis about a biological mechanism cannot. This is the same boundary the wiki draws around [verifiable-reward RL](use-verifiable-rewards-for-language-model-rl.md) and [reasoning models in verifiable domains](scale-reasoning-models-with-rl-and-verifiable-domains.md), applied here as an admission rule for a task set rather than as a property of a training regime. Where the verifier does not exist yet, the prerequisite is [building the engine that creates one](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md).
- **DSGym applies the same two conditions with different instruments, because the domain differs.** For scientific analysis, human demand is inherited from the literature — tasks are curated from "recently published papers" — and quality is enforced by "human scientists and experts to review each of those tasks." For predictive modeling, both conditions are borrowed at once from recent still-open Kaggle competitions, which supply a live community *and* "high quality data sets and also high quality evaluations." Kaggle is, in effect, an existing arena being harvested for its verifiers. (13:03-13:47)
- **The Kaggle route imports a hazard the source does not mention.** Ground truth for an open competition is held by a third party, leaderboards move while you are benchmarking against them, and the competition's own public discussion is a live leakage channel into any model trained after it. A still-open competition is fresher than a closed one and less stable as a benchmark.
- **Both conditions plus a third from this source's other finding.** A task can satisfy live human demand and mechanical gradeability and still be worthless if it is answerable without its data — see [Audit a Benchmark by Solving It Without the Data](audit-a-benchmark-by-solving-it-without-the-data.md), which is why DSGym's curation ends with "we have carefully verified that there are no shortcuts in these tasks" rather than with expert review. (15:20-15:28)
- Contrast with the wiki's other curation guidance. Snorkel's [four-property checklist](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md) is about the *set* — quality, diversity, headroom, methodology. This is a per-task admission rule, and its distinctive move is the demand condition, which none of the wiki's other benchmark-design material states explicitly: it asks not whether the task is good but whether anyone outside the benchmark is waiting for the answer.
- Provenance: the filter is stated as the arena's design principle, not demonstrated as a discriminator. No rejected candidates are named, no count of problems considered versus admitted is given, and the eleven problems where agents hold best-known solutions are never enumerated, so the filter cannot be inspected against its own output.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)
- [Design the Environment, Not the Workflow](design-the-environment-not-the-workflow.md)
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)
- [Audit a Benchmark by Solving It Without the Data](audit-a-benchmark-by-solving-it-without-the-data.md)
- [Judge Benchmark Quality by Task Quality, Diversity, Headroom, and Methodology](judge-benchmark-quality-by-task-diversity-headroom-and-methodology.md)
- [Use Verifiable Rewards for Language-Model RL](use-verifiable-rewards-for-language-model-rl.md)
- [Scale Reasoning Models With RL and Verifiable Domains](scale-reasoning-models-with-rl-and-verifiable-domains.md)
- [Build High-Fidelity Engines to Create Verification Loops in Non-Code Domains](build-high-fidelity-engines-to-create-verification-loops-in-non-code-domains.md)
- [Domain Evals Need Expert-Built Environments](domain-evals-need-expert-built-environments.md)
- [Prefer outcome verifiers over ground-truth path checks](prefer-outcome-verifiers-over-ground-truth-path-checks.md)
- [Treat Environments as Eval, Data, and Training Substrates](treat-environments-as-eval-data-and-training-substrates.md)

Sources:
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 02:47-03:21, 05:12-07:56, 13:03-13:47, 15:20-15:28
