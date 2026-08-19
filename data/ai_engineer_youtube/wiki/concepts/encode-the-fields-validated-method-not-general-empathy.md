# Encode the Field's Validated Method, Not General Empathy

Summary: Mature helping professions already have methods with measured outcomes, and those methods — not the model's generic helpfulness — are the standard a product in that domain is judged against. Grounding an agent's response logic in a named, validated framework changes what the agent *does* with a user's statement (reflect the pattern, name the dynamic, ask the question underneath the question) rather than only how it sounds.

Use when:
- Building an agent inside a profession that has published, outcome-validated methods — counseling, coaching, education, physical rehabilitation, financial planning, case management.
- A product's behavior spec is drifting toward "be empathetic and give good tips," and you need a stronger definition of correct.
- Deciding what a domain expert should actually contribute beyond reviewing outputs.
- Assessing a competitor or an incumbent general assistant in a specialist domain.

Details:
- **The methods exist and they are measured.** John Gottman ran "the love lab" at the University of Washington for 40 years — couples in a research apartment, wired to physiological monitors, every interaction filmed — and identified communication patterns that "predict divorce with over 90% accuracy… more accuracy than most medical tests we trust with our lives, from a 15-minute conversation." Alongside it, emotionally focused therapy (Sue Johnson) is grounded in attachment theory, works the layer beneath the argument — "when couples fight about the dishes, it's never about the dishes" — and "the outcome research is among the strongest in psychotherapy." ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 07:46-09:05)
- **The gap is an observation about the market, not a claim about models.** Both frameworks "take years of training," both are "the standard care for couples intervention," and both are "almost entirely absent from the commercial AI relationship space." What most relationship apps are built on is "something that might be called general empathy plus communication tips. And that's fine. But when the stakes are this high, when the technology is reaching this many people, we need better." The diagnosis Cockrell gives for the whole category: "this is not a critique of technology. This is a critique of insufficient domain expertise being applied to one of the highest stakes domains in human life." ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 09:05-09:31, 11:30-11:39)
- **What encoding the method changes in the output.** CoupleWork's coach "operates with the Gottman Method and EFT frameworks. That means her response logic is grounded in 40 years of couples research. She does not simply validate. She reflects patterns back. She names dynamics, not just feelings. She asks the question underneath the question." Each of those is a behavior a rubric can be written against, and the first one is a negation — the method tells the agent what *not* to do with a complaint, which generic helpfulness never supplies. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 12:01-12:17)
- **A validated framework doubles as a definition of correct for evals.** The talk's engineering half depends on this: you can only "encode what good looks like in evals" if the domain has a *good* that is not just user satisfaction. The framework is what the clinician is drawing on when they write those cases, which is why the sequencing is "start with your clinician, not with your prompt." ([Tony Fabrikant](../sources/20260819_yoONZwV2smc.md), 14:38-14:52)
- **How this differs from the wiki's other domain-grounding patterns.** Onlay grounds *actions* in a published transaction standard (X12), which confines what an agent may emit and gives a downstream system something to reject; skills-based approaches package *procedural* domain knowledge onto a general harness. This pattern grounds the *interactional stance* — what the agent should do with what a user just said — where the domain's authority comes from outcome research rather than from a schema or a runbook. The three compose: a method for the stance, a standard for the actions, skills for the procedures.
- **The caveat the talk leaves open.** Nothing in it describes how faithfully a language model reproduces a method that "takes years of training" for a human, or how conformance to Gottman or EFT is measured on a given response. What is claimed is that the response logic is grounded in the frameworks and that judged behaviors follow from them; treat method fidelity as something your evals still have to establish rather than something the grounding guarantees.

Related topics:
- [Healthcare Operations](../topics/healthcare-operations.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Agreeableness Is a Failure Mode When the Product's Job Is to Change the User](agreeableness-is-a-failure-mode-when-the-job-is-to-change-the-user.md)
- [Ground Agent Actions in an Existing Domain Transaction Standard](ground-agent-actions-in-an-existing-domain-transaction-standard.md)
- [General Agents Need Skills for Domain Expertise](general-agents-need-skills-for-domain-expertise.md)
- [Expert Judgment Bookends the Eval Suite](expert-judgment-bookends-the-eval-suite.md)
- [Build Judge References From Independently Written, Adjudicated Expert Rubrics](build-judge-references-from-adjudicated-expert-rubrics.md)

Sources:
- [AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../sources/20260819_yoONZwV2smc.md), 07:46-09:31, 11:30-12:17, 14:38-14:52
