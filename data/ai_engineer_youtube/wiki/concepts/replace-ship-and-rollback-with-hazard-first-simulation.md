# Replace Ship-and-Rollback With Hazard-First Simulation When Errors Are Irreversible

Summary: The industry default for de-risking a launch — ship to a small percentage, watch the dashboard, roll back — assumes you can afford to be wrong for an instant. When a single output is irreversible and harmful, that assumption fails, and the reactive loop must be replaced by enumerating hazards up front, running them in simulation, and granting autonomy in stages proportional to accumulated evidence.

Use when:
- Shipping an AI system where a bad output physically or legally harms a user and cannot be retracted (clinical advice, financial instructions, safety guidance, spoken output).
- Deciding whether a percentage rollout, canary, or A/B test is an adequate safety story for a regulated or high-consequence product.
- Building the evidence package a regulator, auditor, or post-incident review will actually ask for.

Details:
- Three safety nets disappear when the user is a patient: you cannot A/B test, because "randomizing patients into a worse variant is unethical and often illegal"; you cannot undo a spoken call — "once Dora says it, it's been said and there is no rollback"; and a vendor benchmark is not a defense — "92% on some benchmark… it's not a defense at a post incident review." (00:58-01:30)
- The hidden assumption in ship-to-5%-and-watch is named explicitly: "it only works because you can afford to be wrong for an instance." At patient scale, 5% is "hundreds if not thousands of patients that have got unproven changes and undue care," and "the dashboards going red means that a patient was actually hurt" — the signal arrives after the harm. (04:25-05:26)
- Start from harm, not from features. Regulation reduces to three questions — what does your software do, what could go wrong, how do you ensure it doesn't — and the hazard list is written with clinicians up front: missing a red-flag symptom (sudden vision loss, severe pain), hallucinating an answer to a medical question, ignoring patient distress; "20, 30, 40" documented hazards, none of which may occur in production. (03:24-04:22)
- The substitute for the reactive loop is borrowed from self-driving: "they didn't just drive around crashing into walls… they put millions of miles of simulations first" before any passenger rode. Simulation "is the only real ethical option," because the hazards cannot be run on real people as a first pass. (05:28-06:08)
- Rare-but-dangerous cases are *manufactured*, not awaited: the improvement flywheel mixes real call data with synthetic edge cases that may never occur naturally (rare symptoms, mis-transcriptions), optimizes the prompt, passes the result through the simulation framework as a **safety gate**, and only then reaches a gated deploy — with every new call feeding the next round. (14:28-15:18, 16:52-17:12)
- Simulation is necessary but not sufficient, and the talk is explicit about the limit: "passing every test in simulation doesn't prove that Dora actually helps someone in real life. It only earns the right to actually try carefully." Simulation is the inner loop (fast, free, thousands of runs before anyone real is exposed); real users are the outer loop, "where the only real proof is." (15:22-15:53)
- Crossing to real users is staged, and "each stage earns the right for the next": simulation → user testing → supervised clinical evaluation on real patients with clinicians in the loop → monitored deployment. The governing rule is that "how much autonomy you allow the system to do depends on your evidence. As the system gets more evidence, you can give it more independence." (15:54-16:36)
- The deliverable is the audit trail, not the artifact: "every call, every data set, and every pinned prompt, every judge verdict traces back to the exact hazard that it addresses… you don't ship the model, you ship the evidence." Pinning prompt versions and keeping traces is listed as a portable practice for non-healthcare stacks. (16:37-17:12)
- The framework survives modality changes even though the hazards do not. Voice adds backchannels and interruptions that break text-era assumptions — an agent cut off mid-safety-advice ("you must avoid bright lights") by an out-of-scope question, where "weak models usually just forget about the safety advice and just answer the next question" — but the response is the same: black-box the system, write down the new hazards, simulate and judge them as before. "Voice is just a new module in the same safety case." (17:14-18:44)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Voice Agents](../topics/voice-agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Validate the Simulated User and the Judge Before Trusting a Simulation](validate-the-simulated-user-and-the-judge.md)
- [Optimize Prompts Against an Asymmetric Cost Matrix, Not Flat Accuracy](optimize-prompts-against-an-asymmetric-cost-matrix.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Simulate Voice Agents With Probabilistic Conversation Evals](simulate-voice-agents-with-probabilistic-conversation-evals.md)
- [Simulated Conversations Test Customer-Facing Agents Before Launch](simulated-conversations-test-customer-facing-agents-before-launch.md)
- [Stage Regulated LLM Evals From Experts to Automated Judges](stage-regulated-llm-evals-from-experts-to-automated-judges.md)
- [Treat Model and Prompt Upgrades as Regulated Migrations](treat-model-and-prompt-upgrades-as-regulated-migrations.md)

Sources:
- [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../sources/20260819_McknwOzbmyg.md), 00:58-06:08, 14:28-18:44
