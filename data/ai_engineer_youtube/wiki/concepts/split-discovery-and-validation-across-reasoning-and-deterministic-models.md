# Split Discovery and Validation Across Reasoning and Deterministic Models

Summary: Capable models suffer an "orchestration paradox" — given a task they spend most of their tokens deciding how to solve it rather than solving it, hopping between methods in a research loop. The fix is an 80/20 split: let high-reasoning models run open-ended discovery for the 80% that is genuinely exploratory, then hand the 20% that needs final validation to lighter, deterministic models behind hard gates, with explicit loop guards so the discovery phase cannot run forever.

Use when:
- An agent burns tokens and latency "researching how to do it" instead of doing it, especially with frontier reasoning models.
- Deciding which steps of a multi-step agent need a high-reasoning model and which can use a cheaper deterministic one.
- Designing stop conditions so an exploratory agent phase terminates.

Details:
- Orchestration paradox: smarter models, given a task, "look for the method to solve the problem" and hop from one method to another; most API tokens are wasted "finding a way to do it rather than doing it." The example given is Opus latest-and-greatest challenging itself ("maybe not this, another way") in a loop of trying to do something rather than doing something. (08:34-09:34)
- The 80/20 split: give the latest/greatest models power to research 80% of the time — discovery, deciding which tool to use, planning, and choosing the next action. Reserve the remaining 20% (final validation, summarization, "what is the proper result the user wants") for restricted, deterministic behavior with hard gates such as "if I get X results I want Y," which lowers the unbounded research coming from the 80%. (09:39-12:24)
- Model tiering: the 20% does **not** need a high-reasoning model because those tasks are deterministic — you tell them what is needed. A critic node, for example, only checks goal versus result and how to summarize; it does not research. This is a model-selection lever, not only a prompting one. (11:22-12:24)
- Loop guards on the 80%: because a research model can still loop, bound it — some teams use a counter (after 4-5 iterations, work with the last result), others a timeout (after ~5 minutes, take the last tool/decision and go back only if results are bad). (10:36-10:59)
- The split maps cleanly onto multi-agent designs: discovery sub-agents use frontier models, while deterministic judge/validation nodes use cheaper models.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Models](../topics/models.md)

Related concepts:
- [Reconcile Specialist Agent Outputs With a Feedback-Weighted Judge](reconcile-specialist-agent-outputs-with-a-feedback-weighted-judge.md)
- [Grow Agent Organizations Incrementally By Role Quality and Cost](grow-agent-organizations-incrementally-by-role-quality-and-cost.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Start Expensive With Agents, Then Collapse Proven Steps](start-expensive-with-agents-then-collapse-proven-steps.md)
- [Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)

Sources:
- [Why More Context Makes Your Agent Dumber and What to Do About It — Nupur Sharma, Qodo](../sources/20260608_EcqMYoIV57A.md), 08:34-12:24
