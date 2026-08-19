# Healthcare Operations

## Overview

Healthcare operations are a strong AI application area when the work is administrative, rules-driven, measurable, and financially material. Revenue cycle management shows the pattern: eligibility checks, registration, documentation, coding, prior authorization, denials, appeals, and payer-provider communication create friction that can delay or prevent payment even when clinical care has already happened.

The best AI opportunities in this domain are not only faster document generation. Longitudinal workflow data lets teams connect late failures such as denials back to upstream missing fields, policy mismatches, prior authorization errors, or documentation gaps. Generative AI can then help assemble evidence and draft appeals, but domain experts should still make final submission decisions when clinical judgment or payer-policy interpretation matters.

Hippocratic AI extends the domain from back-office friction to the clinical conversation itself, and shows what changes when the AI talks directly to a patient. Vivek Muppalla frames the opportunity as arithmetic rather than automation: healthcare has always been rationed by scarcity — "not enough clinicians, not enough time, not enough money, and hence the word triage" — so once clinically safe conversation gets cheap enough, "you don't have to have calls just for the sickest 5%, but you can call everyone." Their reported scale is 200M+ clinical interactions across 60+ health systems with zero significant safety incidents and 8.5/10 patient satisfaction, and the calls do real clinical work: confirming vitals back to the patient, resolving a spelled-out drug name, detecting that a medication the patient was told to stop was still taken (and deferring to the primary care doctor rather than advising), and escalating to a live nurse on shortness of breath. Three engineering consequences follow from the stakes. Recognition errors dominate apparent reasoning errors, so the ASR is [conditioned on conversation context and domain vocabulary](../concepts/condition-asr-on-conversation-context-and-domain-vocabulary.md) rather than bought off the shelf. A single model is treated as an unacceptable single point of failure, so the system [runs parallel specialist models behind a speak-up gate](../concepts/run-parallel-specialist-models-with-a-speak-up-gate.md) with background verifiers on tool calls. And accuracy is measured against consequence, so evals are [sized to the error rate the consequence demands](../concepts/size-eval-suites-to-the-error-rate-the-consequence-demands.md) and graded on the harm scale used for human clinicians. The same expert-in-the-loop principle that governs appeal submission reappears here in a different form: rather than reviewing each output, 7,000+ trained clinicians run continuous evaluation of the system, and the agent escalates to a human when the clinical situation warrants it.

## Key Concepts

- [Condition ASR on Conversation Context and Domain Vocabulary](../concepts/condition-asr-on-conversation-context-and-domain-vocabulary.md) - clinical entity recognition (drug names, vitals, addresses) needs conversation and domain conditioning, because mishearing masquerades as reasoning failure.
- [Run Parallel Specialist Models Behind a Speak-Up Gate](../concepts/run-parallel-specialist-models-with-a-speak-up-gate.md) - patient-facing systems need model redundancy without a latency penalty, plus verifiers on the actions they take.
- [Size Eval Suites to the Error Rate the Consequence Demands](../concepts/size-eval-suites-to-the-error-rate-the-consequence-demands.md) - in care delivery a 1% error is a daily count of harmed patients, which sets both the accuracy bar and the test-suite size.
- [Revenue Cycle AI Targets Administrative Friction](../concepts/revenue-cycle-ai-targets-administrative-friction.md) - healthcare AI can create direct value by reducing payer-provider communication friction, denials, rework, and delayed payment.
- [Prevent Revenue Cycle Denials Upstream](../concepts/prevent-revenue-cycle-denials-upstream.md) - end-to-end workflow data can turn late denial patterns into earlier checks and corrections.
- [Expert-Reviewed GenAI Appeals Beat Off-the-Shelf Letters](../concepts/expert-reviewed-genai-appeals-beat-off-the-shelf-letters.md) - clinical appeal generation needs evidence assembly, local quality standards, and expert approval.

## Open Questions

- Which revenue cycle steps can be fully automated, and which should remain expert-reviewed because payer policy or clinical necessity is disputed?
- How should providers measure whether payer-side AI denial automation is increasing preventable administrative burden?
- Which clinical conversations can an AI agent safely conduct end to end, and which must escalate to a clinician by policy rather than by model judgment?
- What does a harm-graded rubric look like outside medicine, where no established human grading scale exists to borrow?

## Sources

- [AI That Pays: Lessons from Revenue Cycle - Nathan Wan, Ensemble Health](../sources/20250724_TquUsN1QsWs.md)
- [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../sources/20260819_AN65uc645mE.md)
