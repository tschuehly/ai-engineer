# Run a Production AI Incident Playbook

Summary: Production AI needs a defined incident response, not ad hoc firefighting. The playbook connects the other production pillars into one loop: detect on the eval dashboard, diagnose with tracing, contain with versioned rollback and fault tolerance, fix from the eval-set library, and grow the living test set, all wired into existing alerting.

Use when:
- Defining what happens when a deployed AI system regresses or fails.
- Connecting evals, tracing, prompt versioning, and orchestration into one operational response.

Details:
- The loop is detect, diagnose, contain, fix, and grow tests. Detect uses the eval dashboard (e.g., a drop in customer satisfaction from negative feedback); diagnose uses tracing to find the cause, such as an outdated policy document that was never re-embedded. (30:29-31:26)
- Contain pulls the offending prompt via prompt versioning, deflects to a human, or applies fault-tolerance patterns; the speaker references saga, compensation, and circuit-breaker patterns from his multi-agent orchestration deep-dive. (31:26-31:52)
- Fix uses the LLM-judge reports and the evaluation-dataset library to find and correct the problem, then adds the case back into the eval suite so the regression is caught next time, keeping the eval set a living system. (31:52-32:20)
- The playbook should integrate with the organization's existing ITSM system so incidents alert the right person at the right time and downstream systems are protected. (32:20-32:51)
- This is presented as a commonly missed artifact: teams build models and demos but rarely define, in advance, what must happen when the system fails in production. (31:00-31:26)
- **What the "detect" step has to emit for the rest of the loop to run.** Ben Hylak's requirement is two numbers per issue: "you need to know when it actually started, and you need to know how many people it affects." Onset is what makes *diagnose* tractable — "this issue started yesterday… suddenly like your mind starts turning and you're like, 'Oh, what did I do?… Did we change model?'" — and share is what makes triage possible when "agents will have an infinite number of problems," since "three users versus 100,000 users" is the difference between a watch and a page ([Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)). A dashboard that shows a satisfaction drop without an onset date gives the diagnose step nothing to diff against. ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 13:20-14:24)

- **The playbook's "detect" step assumes something fires; a fourth source argues the harder cases are the ones that never will.** Resolve AI's position is that the well-instrumented paths already work — "on-call you've got a page that goes off. You know somebody's going to receive that. Incidents you create a bridge, you invite people in" — and that the residual risk sits in changes nobody watches, particularly the ones that never enter the pipeline: "a feature flag or maybe some infra changes… which maybe don't get any monitoring at all. And you're sort of just trusting that an alert might fire and an on-caller will wake up and say, 'Who changed what?'" That is the detect step failing open. The proposed addition is to trigger verification off the change rather than off a symptom, and to accept sub-page signals ("this may not be paging… because we're not going to alert on everything") as work worth scheduling. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 09:04-09:50, 14:35-14:52)
- **Two additions to the detect and contain steps, from a gateway operator.** Detection has a blind spot this loop does not cover: a missing timeout produces a *silent* outage, because "your gateway thinks your request is being happily served while it is not" — which Manuja names "the number one root cause" of the class. And containment has a case where scaling does not work: "when you have a retry storm, it becomes really hard to just scale out. You cannot simply scale out services that is under a retry storm," so the containment lever is load shedding, bounded queues, and traffic prioritization, and he puts rehearsing it in "your runbooks, game days" rather than in the incident itself. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 07:41-08:02, 13:49-14:31)

Related topics:
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Continuously reconcile eval datasets with user reality](continuously-reconcile-eval-datasets-with-user-reality.md)
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Hand Agents Anomalies to Investigate, Not to Detect](hand-agents-anomalies-to-investigate-not-to-detect.md)
- [Watch the Change Paths That Bypass Your Deployment Pipeline](watch-the-change-paths-that-bypass-your-deployment-pipeline.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 30:29-32:51
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 13:20-14:24
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 09:04-09:50, 14:35-14:52
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 07:41-08:02, 13:49-14:31
