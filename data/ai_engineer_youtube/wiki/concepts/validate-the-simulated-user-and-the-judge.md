# Validate the Simulated User and the Judge Before Trusting a Simulation

Summary: An LLM-simulated evaluation loop contains two models, not one: the synthetic user driving the conversation and the automated judge grading it. Both are assumptions until validated against humans, so a simulation-based safety case should ship evidence for the simulator's realism and the judge's agreement with domain experts before any result from that loop counts.

Use when:
- Standing up a persona-simulation or synthetic-user harness and deciding whether its verdicts can gate a release.
- Being asked to defend "our evals are green" to a regulator, clinician, auditor, or post-incident review.
- Choosing which model to use as a simulated user, or deciding how many personas the simulator needs.

Details:
- The simulation framework (Matrix) has two model-shaped halves: an LLM playing the patient (**PatBot**), conditioned on a scenario that "defines exactly what the patient should try and do when talking to our agent," and a second LLM judge that reads the resulting dialogue. Both are validated separately. (06:24-07:23, 09:39-10:02)
- A simulated user is chosen over hired actors for scale, not fidelity: "hired actors don't scale," and iterating fast while the system itself changes "would just be too slow." The realism gap that opens up is the thing that then has to be measured. (06:31-06:52)
- **Simulator validation, step one — script adherence.** A pure yes/no check of whether the simulator did what it was told; this "helped us filter out a lot of maybe weaker models that didn't listen to instructions properly." But it is only a filter: "purely following instructions does not make a realistic patient." (07:25-07:57)
- **Simulator validation, step two — a blind human realism study.** In a patient-and-public-involvement (PPI) study, real patients were shown two conversations side by side — a real doctor with a real patient, and the agent with the simulator — and asked which patient was real. Across four sets, "in three out of the four, the majority of people actually thought that the simulated patient was more realistic," which establishes the simulator as realistic enough for the behavior under test. (08:00-08:55)
- The study's more transferable finding is that realism is not a single target: "there is no single realistic patient" — some users are verbose with "a lot of ums and ahs," others terse — so the goal is coverage across "very diverse personas" rather than one canonical simulated user. (08:56-09:19)
- **Why an automated judge is required at all:** thousands of simulated dialogues cannot be read one by one, and the engineers reading them "aren't clinicians, so [we can't] actually know if an actual hazard has really occurred." The judge takes the dialogue, a set of expected behaviors, and the clinician-agreed hazard scenarios, and returns pass/fail with a reason — "a structured output of which hazards were triggered and what actually went wrong." (09:25-10:02)
- **Judge validation against a panel, not a single annotator.** A 240-example corpus with ground truth for hazard presence was labeled by 10 clinicians drawn from 10 different clinical specialties and by the judge. The judge came out "at least on par, if not slightly better, than the real expert clinicians," with the top model at paper time (Gemini 2.5 Pro) reaching F1 0.96. (10:04-10:36)
- **The headline metric follows the cost of the error, not convention.** F1 is reported, but the emphasis is on near-perfect *sensitivity*, because "you would rather overcall hazards that aren't there than undercall hazards that are there." The validated judge is what makes the whole loop scalable — an unvalidated one would only make it fast. (10:38-11:03)
- The residual limitation is stated rather than papered over: "however realistic you think they are, of course they are not real patients," so a validated simulator earns the right to a staged rollout rather than substituting for it. (15:22-15:53)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Replace Ship-and-Rollback With Hazard-First Simulation When Errors Are Irreversible](replace-ship-and-rollback-with-hazard-first-simulation.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Calibrate Voice Eval Realism To The Behavior Under Test](calibrate-voice-eval-realism-to-the-behavior-under-test.md)
- [Simulate Voice Agents With Probabilistic Conversation Evals](simulate-voice-agents-with-probabilistic-conversation-evals.md)
- [Validate eval harnesses before trusting skill scores](validate-eval-harnesses-before-trusting-skill-scores.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)

Sources:
- [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](../sources/20260819_McknwOzbmyg.md), 06:24-11:03, 15:22-15:53
