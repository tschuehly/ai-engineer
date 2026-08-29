# Domain Evals Need Expert-Built Environments

Summary: High-value domain evals depend on expert validation and task environments, especially when agent errors can create financial, legal, safety, or operational consequences. LLM judges can reduce evaluation cost, but they are substitutes only after their bias and domain fit are validated.

Use when:
- Evaluating agents in specialized domains such as finance, healthcare, law, infrastructure, or regulated operations.
- Deciding whether to use human experts, LLM judges, or both for agent evaluation.

Details:
- In response to a financial-analysis example, Dickerson says expensive human validation can be justified when a wrong discounted-cash-flow result can make or lose substantial money or cost someone their job. 16:16-17:44
- Domain experts sitting alongside multi-agent systems can generate the validation data that later becomes a moat or internal capability for the system. 17:04-17:56
- Eval practitioners often see dataset creation and environment creation as the highest-value part of the work, because the domain task setup determines whether evaluation measures the real job. 17:52-18:11
- LLM-as-judge systems are already used because they partially reduce dataset-creation cost, but they can carry biases around properties such as conciseness or helpfulness and still need validation against human judgment. 18:13-19:01
- Snorkel's quality-at-scale recipe for agentic-task environments makes the human/LLM-judge split concrete: human annotators and experts supply ground truth, that ground truth informs LLM judges, the team builds rubrics (a longer list of data points and criteria usable by both humans and judges), and they require very high inter-annotator agreement *both* human-to-human and judge-to-human before trusting a signal — even in explicitly verifiable test-pass/test-fail domains. The same expert-in-the-loop generation is credited as the reason a high-quality task set produced ~5x the RL training uplift of a low-quality one. ([Task Fidelity Scaling Laws](../sources/20260602_YYH0DMQr30A.md), 18:40-20:15, 10:21-10:42)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)
- [Mature Eval Platforms From Spreadsheets Into Experiment Systems](mature-eval-platforms-from-spreadsheets-into-experiment-systems.md)
- [Task Quality Drives a 5x RL Training Uplift](task-quality-drives-rl-training-uplift.md)
- [Accept Agentic Training Tasks by Clean Failures, Not Ambiguous Specs](accept-agentic-tasks-by-clean-failures-not-ambiguous-specs.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)

Sources:
- [2025 is the Year of Evals! Just like 2024, and 2023, and ... - John Dickerson, CEO Mozilla AI](../sources/20250806_CQGuvf6gSrM.md), 16:16-18:11, 18:13-19:01
- [Task Fidelity Scaling Laws — Kobie Crawford, Snorkel](../sources/20260602_YYH0DMQr30A.md), 18:40-20:15
