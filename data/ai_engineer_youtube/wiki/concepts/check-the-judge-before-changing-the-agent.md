# Check Whether the Judge Is Right Before Changing the Agent

Summary: A production judge score that moves is a claim made by one non-deterministic system about another. The discipline is to test the judge first: "in a non-deterministic system, the judge is also non-deterministic. Before you trust the score, verify the scorer." Editing the agent on an unverified signal is how you break a working system chasing a measurement artifact.

Use when:
- A live judge metric drops and holds, and the reflex is to start changing agent prompts.
- Judge scores are wired to dashboards, alerts, or release gates that people act on without re-reading traces.
- Deciding whether changing a judge prompt after seeing production results is legitimate or is grading yourself on a curve.

Details:
- **The scenario.** A clinical accuracy judge has been steady at 4.9 for weeks. Today it drops to 4.5, and tomorrow it stays at 4.5. "The immediate instinct is, let's start changing the prompts. The agent is broken. Let's fix the agent. That's reactive, and it's risky. You fix one thing and you break another. Worse, you're changing the agent based on a signal that might not be true." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 18:15-18:56)
- **The side-by-side that separates the cases.** Same member question about caffeine, two different agent answers. *Scenario A:* the agent gives FDA standard guidance — 400 mg for most adults, less if pregnant or on certain medications — and the judge flags a hallucination "because the agent mentioned pregnancy and medications without checking. But that's just clinical context. The judge is over calling in this case. Fix the judge." *Scenario B:* the agent says "1,000 mg a day is fine," which is well above the safety limits, "the judge correctly flags it, and the agent is wrong. In this case, fix the agent." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 19:02-19:56)
- What distinguishes them is not the score and not the dimension — both are the same judge on the same question — but whether the flagged behavior was actually wrong when read against the domain. That is only visible by pulling the traces the judge scored, which is why the drop-and-hold pattern is the trigger to *read*, not to *edit*. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 19:02-20:01)
- **The norm that has to be stated explicitly:** "fixing a judge prompt is not cheating. Judges are software, too. And they need to continuously evolve." Teams often treat the judge as frozen ground truth precisely because moving it feels like moving the goalposts; the counter is that an over-calling judge is a defect in the measurement system, and shipping around it corrupts the agent instead. "This is what production discipline looks like when the system is not deterministic." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 20:03-20:14)
- **Where this sits relative to judge calibration.** Offline calibration — aligning a judge to expert labels on dev/test splits, or validating it against a clinician panel — establishes that a judge was trustworthy *when it was built*. This concept is the operational counterpart: a calibrated judge still drifts out of agreement as the agent's behavior, the traffic, and the underlying model change, so calibration is a standing obligation attached to every score movement, not a one-time gate. The two techniques compose: the calibration set is what you re-run to decide whether the judge or the agent regressed.
- **It is also the precondition for launch triage.** The ship-or-hold severity rules "all assume one thing, that your underlying signal is true," so this check runs before severity is assigned to anything a judge reported. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 17:55-18:13)

Related topics:
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Validate the Simulated User and the Judge Before Trusting a Simulation](validate-the-simulated-user-and-the-judge.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)
- [Decide Ship-or-Hold With Explicit Severity Rules](decide-ship-or-hold-with-explicit-severity-rules.md)
- [Optimize Judge Prompts With Diagnostic Feedback](optimize-judge-prompts-with-diagnostic-feedback.md)

Sources:
- [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../sources/20260819_YXEqC05WEI0.md), 17:55-20:14
