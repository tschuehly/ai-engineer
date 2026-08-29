# Domain Expert Review Tools Convert Judgment Into Deployable Knowledge

Summary: A domain-expert review tool should let specialists inspect evidence, judge outputs, label failures, and propose new domain knowledge in the same workflow. Evals and release gates can then decide whether that expert insight becomes production context.

Use when:
- Designing review tooling for clinicians, lawyers, analysts, or other domain experts improving an AI product.
- Deciding how non-technical expert feedback should enter prompts, retrieval context, rules, or pipeline logic.

Details:
- Anterior's internal review surface shows the source record, guidelines, AI decision, and AI reasoning so clinicians can mark correctness and choose a failure-mode label, 09:15-10:04.
- The same review workflow can collect performance metrics, failure modes, and suggested improvements from one expert pass, 14:26-14:40.
- Domain experts can suggest new domain knowledge, such as how to interpret a clinically loaded phrase or when a missing scoring system should be available to the model, 12:04-13:59.
- Suggested expert knowledge can be routed through evals automatically or through a human-in-the-loop gate before production deployment, 14:05-14:23.
- The speaker argues bespoke tooling often makes sense when review outputs feed directly into the platform and multiple downstream improvement loops, 15:35-16:03.
- **Same conclusion about bespoke tooling, opposite conclusion about who builds it.** DoorDash's platform team agrees a generic screen fails — "it's almost hard for a platform team to build like a UI specific for each use case" — and resolves it by moving the builder rather than the design: operators generate their own annotation apps against stable APIs. The reconciling variable is the number of distinct expert workflows. One high-stakes clinical review surface justifies engineering-built bespoke tooling; a dozen unlike annotation workflows spread across product teams does not, and the platform team's product becomes the API instead of the screen. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:29)
- **The capture step before any review tool exists: watch the expert work.** Notion's team shadowed its best reps to find "the most repetitive part of our job" and encoded it as a durable multi-agent workflow, with the observation that the mess itself was the specification — "that was chaos, but it was also the spec" — and the warning that "if you encode a mediocre process you get a mediocre agent." The judgment that is not encoded stays with the human, who "adds their own judgment and taste" on top of a pre-researched draft. ([Liu](../sources/20260826_L4I7WgiEquo.md), 13:04-13:12, 16:31-16:41, 19:26-19:51)
- **The lightweight version: review at intake, with the skill file as the deployable artifact.** Cloudflare's expert-level knowledge reaches production as curated skills — submitted to a central alias, reviewed jointly by the go-to-market and operations teams, then read by the agentic workspace alongside MCP connections. There is no evidence-inspection surface, no failure labelling, and no release gate between the expert's judgment and the running system; the review is a human reading a proposed skill. That is enough to keep a library coherent and not enough to tell anyone whether the encoded judgment is working, which is the gap an eval-backed review tool fills. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 13:01-14:02)

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Domain-Expert Sandboxes Accelerate Knowledge-App Iteration](domain-expert-sandboxes-accelerate-knowledge-app-iteration.md)
- [Build AI Product Iteration Tools Into the Product Context](build-ai-product-iteration-tools-into-the-product-context.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)

Sources:
- [Make your LLM app a Domain Expert: How to Build an Expert System - Christopher Lovejoy, Anterior](../sources/20250728_MRM7oA3JsFs.md), 09:15-16:03
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 08:39-10:29
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 13:04-13:12, 16:31-16:41, 19:26-19:51
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 13:01-14:02
