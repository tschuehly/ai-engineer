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

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 30:29-32:51
