# Expert-Reviewed GenAI Appeals Beat Off-the-Shelf Letters

Summary: In clinical-denial workflows, off-the-shelf generative models can draft appeal letters but are not sufficient by themselves. A production workflow needs patient records, guidelines, payer policies, local quality standards, and clinical expert approval before submission.

Use when:
- Building GenAI workflows for regulated or expertise-heavy administrative decisions.
- Deciding where human review belongs in document generation for healthcare operations.

Details:
- Clinical denials arise when payer and provider disagree about medical necessity, and appeals require an evidence packet built from patient records, guidelines, payer policies, and coverage rules, 12:20-13:01.
- Electronic medical records can be hundreds of pages long and include text, images, labs, notes, and tables, while clinical guidelines vary by situation, 13:03-13:24.
- The source says an off-the-shelf GenAI model can generate an appeal letter, but Ensemble found that model output alone was insufficient when reviewed with clinical experts, 13:45-14:08.
- The production pattern is a model and pipeline that meet organizational quality standards while leaving the final decision to the clinical expert before payer submission, 14:08-14:29.
- Ensemble reports faster appeals with a 40% time reduction and measures quality through denial overturn rate, 14:52-15:22.

Related topics:
- [Healthcare Operations](../topics/healthcare-operations.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Domain Expert Review Tools Convert Judgment Into Deployable Knowledge](domain-expert-review-tools-convert-judgment-into-deployable-knowledge.md)
- [Layer Domain RAG Evals by Fidelity, Cost, and Speed](layer-domain-rag-evals-by-fidelity-cost-and-speed.md)

Sources:
- [AI That Pays: Lessons from Revenue Cycle - Nathan Wan, Ensemble Health](../sources/20250724_TquUsN1QsWs.md), 12:20-15:22
