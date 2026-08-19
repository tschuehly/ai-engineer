# Run Must-Not-Fail Decisions in a Code Layer Above the Model

Summary: Behavior that can never be wrong should be decided by deterministic code that runs *first, on every turn, before the model runs* — not by a prompt, and not by a check after the model has already answered. The model handles the long tail; it never gets a vote on the irreversible calls.

Use when:
- An agent turn can trigger something unrecoverable — an emergency escalation, a wrong-capability handoff, a data access on an unverified identity.
- You are deciding whether a safety requirement belongs in the system prompt, in a post-generation filter, or in front of the model entirely.
- Someone proposes "we'll add it to the prompt" for a requirement whose failure mode is a person harmed, not a sentence off-brand.

Details:
- **The stack, and the ordering.** "Must-not-fail behavior belongs above your prompt, above the model." Above the prompt means "there is a code layer that runs first, on every turn, before the model even runs. The code layer is what makes your irreversible decisions." The picture to hold: "code on top, model below. Every turn goes through the code layer first. Most turns do reach the model, but the model never gets a vote on high stake calls." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 05:56-07:13)
- **The escalation is the sharpest form of "before."** If a member mentions self-harm, suicidal ideation, or an acute medical emergency, "the system must route to 911 or 988. The model should not even see this turn." A post-generation veto would be too late here by construction: the model would already have composed a reply to a crisis disclosure. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 07:58-08:21)
- **Intent routing is the non-obvious member of the set.** Which capability in a multi-agent architecture owns a turn — clinical, tech support, education from accredited articles, exercise recommendation — looks like a classification problem, and "the model can help to classify, but high-stakes paths must again take a deterministic route." The failure it prevents is silent: "a clinical question quietly being routed to your generic tech support agent… that's unrecoverable." Nothing errors; the user just gets the wrong kind of answer from a component that was never evaluated for it. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 08:22-09:03)
- **Identity verification restates the boundary in security terms.** "Anything that touches member data has to check that the right member is at the other end. That's an authentication check. And authentication is a security boundary. Prompts are not." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 09:04-09:22)
- **The argument comes from the labs, not from conservatism.** "A model is not a guardrail. A model with a system prompt is also not a guardrail. Code that runs above the model is closer." "Even the labs that build these frontier models publish the authority hierarchy: root, system, developer, user, guideline. Every layer above user is one prompt injection away from being overridden. If the labs themselves don't trust the prompt as a security boundary, neither should you." The published hierarchy is being read as an admission rather than an assurance. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 07:13-07:49)
- **Where this sits relative to the other deterministic-guardrail patterns.** This is the *pre-model router*, and it is a third position distinct from the two the wiki already documents: a post-generation veto reads what came out and decides whether it may leave, and a tool wrapper checks a call the model has already chosen to make. All three refuse to make the prompt the enforcement point; they differ in what is already unrecoverable by the time they run. Use the pre-model layer when the model *seeing* the turn is itself the problem, or when the routing decision determines which evaluated component answers at all.
- **The compressed rule** is "don't prompt what you can code," one of three architecture rules stated as "don't X what you can Y" — the others being "don't policy what you can architect" and "don't gate what you can monitor." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 20:18-20:40)

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Gate Generated Output With a Deterministic Post-Generation Veto](gate-generated-output-with-a-deterministic-veto.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [LLM Guardrails Need Checkpoints at Every Untrusted Boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)
- [Make Regulated-Data Failures Architecturally Impossible](make-regulated-data-failures-architecturally-impossible.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)

Sources:
- [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../sources/20260819_YXEqC05WEI0.md), 05:56-09:33, 20:18-20:40
