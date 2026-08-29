# Use Field-Level Confidence Signals for Human Review

Summary: Structured extraction workflows can expose field-level confidence to guide human review. One practical pattern is to align model log probabilities with the extracted structured-output values and show lower-confidence fields as review targets.

Use when:
- Building document extraction workflows where humans need to verify only the risky fields.
- Designing trust surfaces for non-technical users reviewing LLM-extracted contract, finance, or compliance data.

Details:
- The source describes structured extraction as combining a document, schema, LLM, validation, and scaffolding so the system pulls out the specific values required by the business workflow. (13:20-13:38)
- The business value sits in the schema: it encodes what the workflow is extracting and why that information matters, making the capability reusable across investigations, M&A, and other engagement types. (13:38-13:59)
- To support user trust, AlixPartners exposes where the model is more or less confident by using log probabilities returned from the OpenAI API and aligning them with structured-output values. (14:16-14:42)
- Their confidence calculation ignores JSON syntax and field names, focuses on the extracted values, and uses the geometric mean of the associated token log probabilities as a rough confidence proxy. (14:42-15:05)
- The confidence display is intended as an intuitive off-ramp for human review, not as a replacement for validation rigor. (15:05-15:51)
- **Where the check belongs in an agent loop, as opposed to an extraction pipeline.** Coyle puts the same confidence gate at the loop's exit rather than inside it: once the stop reason says the model is done rather than requesting a tool, "we take the answer, and this is an opportunity for you to have a human in the loop potentially. You check the confidence. If it looks good, you keep it. If you don't, then you escalate to a human." Placing it there means one judgment per completed task instead of one per tool call — the same economy this page gets from scoring fields rather than whole documents. He names no confidence signal, so the log-probability method above is the concrete instrument this framing lacks. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 10:36-10:49)

- **Where a self-reported confidence signal is unavailable, and what to route on instead.** Uber's blunt finding from operating an automated reviewer: "the model doesn't know that it's wrong. It always confidently says 100% sure that yeah, this is the review for your code. Go ahead." Field-level confidence works in extraction because the field has a determinate value the model can be uncertain about; an open-ended judgment like "this is a bug" produces a stated certainty with no relationship to correctness. Their substitute is downstream behaviour — whether the comment was addressed and what the reply said — which is a post-hoc signal and therefore cannot gate the comment at emission time. Confidence-style filtering there has to come from cross-generator agreement and from severity, not from asking the model. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 06:35-06:46)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Type-Safe Agent Schemas Make Refactoring and Validation Easier](type-safe-agent-schemas-make-refactoring-and-validation-easier.md)
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Read the Stop Reason Before You Read the Answer](read-the-stop-reason-before-you-read-the-answer.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)

Sources:
- [The Billable Hour is Dead; Long Live the Billable Hour - Kevin Madura + Mo Bhasin, Alix Partners](../sources/20250723_Wv1tAxKYLeE.md), 13:20-15:51
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 10:36-10:49
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 06:35-06:46
