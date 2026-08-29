# Hand Domain Experts the Pipeline as Skills

Summary: In vertical AI, the engineer is not qualified to judge the output, so the pipeline's logic should be authored by the domain expert. Modelling each pipeline stage as a skill file on a generic agent harness moves the ownership boundary past "expert reviews outputs" and past "expert tunes parameters in a tool we built" to "expert adds a stage" — no engineering change required.

Use when:
- Deciding how non-engineer domain experts contribute to an AI pipeline beyond labelling and review.
- A vertical AI product's quality bar is set by knowledge the engineering team does not have.
- Customer-specific variants (new document types, new formats, new rules) would otherwise queue behind engineering.
- Choosing between building a bespoke expert-facing tool and exposing the pipeline itself.

Details:
- The premise is an admission of authority, not a workflow preference: asked how he would know what a good medical record looks like, the speaker answers "you really don't. Like no AI engineer would … you want your domain experts to be the ones telling you what's good," which is why "it is of great value to empower your domain experts to own your whole data pipeline." (11:34-12:07)
- Two mechanisms, at different depths. The first is human-in-the-loop steering: "at any point, a clinician can steer the generation process to make a medical record in the way they want it." In practice clinicians look at production cases, take ideas from them, and steer the pipeline into producing similar cases — so failure cases can be modelled "beforehand or even after … you see them in production." (12:15-12:58)
- The second is ownership of the logic itself: "we let our clinicians also own the whole logic of the pipeline … by modeling the whole pipeline as a skills-based workflow running on a generic agent harness that we built internally." The patient journey, document generation, document enrichment, and the evals are each skills on that harness. (12:59-13:22)
- The test of whether the boundary really moved is a change request that used to need an engineer: a clinician adding a new document type for a customer's intake forms "could easily just make a new skill file for it, attach it to the pipeline, and … there wouldn't be any engineering changes required." (13:29-13:46)
- The generalization the speaker offers is about the artifact, not the domain: "skills are really an amazing interface between AI engineers and domain experts, especially in vertical AI," and the pattern is reused across their other internal and production workflows. A skill file is legible to a non-engineer, versionable like code, and executable by the same harness — which is why it works as a handoff format. (13:47-14:02)
- The claimed payoff is compounding rather than throughput: give domain experts the keys "because these are the people who know about your data and … they will help you drive towards a recursive self-improvement and not the AI engineers." (15:53-16:11)
- This is a stronger position than expert review tooling, and worth distinguishing from it. Anterior's earlier talk described clinicians inspecting evidence, labelling failure modes, and *suggesting* domain knowledge through a bespoke review surface; here the same population writes the pipeline stages. Review tooling routes expert judgment through an engineering-owned system; skills remove the routing step for a class of changes.
- **The same ownership-boundary move applied to the tool rather than the pipeline.** Anterior pushes the expert past reviewing outputs to authoring pipeline stages as skills. DoorDash pushes a different boundary with the same logic: the operator authors the interface they work in, generating it with a coding agent against platform APIs. Both replace "file a request with engineering" with "write the artifact yourself," and both depend on the engineering team having produced a stable substrate — a skill-loading harness in one case, an owned API surface in the other. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:29)

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Generate Eval Data by Reversing the Inference Workflow](generate-eval-data-by-reversing-the-inference-workflow.md)
- [Build Synthetic Records Coarse to Fine by Emulating How They Were Produced](build-synthetic-records-coarse-to-fine-by-emulating-their-source-process.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Domain-Expert Sandboxes Accelerate Knowledge-App Iteration](domain-expert-sandboxes-accelerate-knowledge-app-iteration.md)
- [Encode Domain Judgment in Node-Level Agent Skills](encode-domain-judgment-in-node-level-agent-skills.md)
- [General Agents Need Skills for Domain Expertise](general-agents-need-skills-for-domain-expertise.md)
- [Treat Complex Skills Like Software Artifacts](treat-complex-skills-like-software-artifacts.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)

Sources:
- [Don't be data poor — Anuj Iravane, Anterior](../sources/20260819_XAsb7MIAzm8.md), 11:34-14:02, 15:53-16:11
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 09:15-16:03
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 09:18-10:29
