# Layer Agent Evals as Deterministic, Semantic, and Behavioral Checks

Summary: Production agent evaluation can be structured as three architectural layers — deterministic checks, semantic LLM-as-judge checks, and behavioral checks over the agent's actions. The behavioral layer is the one teams most often miss, because it catches correct-but-expensive trajectories that pass output-level evals.

Use when:
- Designing the eval architecture for a tool-using or RAG agent.
- A response is correct but you suspect the agent reached it inefficiently or unsafely.

Details:
- Layer one is deterministic: regex and format checks (email, phone) plus classic ML models for named-entity recognition, intent classification, and PII detection. These are cheap, well-understood, and should be handled first. (09:22-09:49)
- Layer two is semantic and non-deterministic: a separate judge LLM scores the primary model's output for safety, groundedness, and relevance, fed by expected answers from the evaluation dataset. Platforms can run custom LLM-as-judge checks automatically over traces (the speaker cites MLflow). (09:49-11:09)
- Layer three is behavioral: did the agent call the right tools, and did it get into loops? A "what is my account balance" query can return the correct number while the trace shows three redundant database calls from failed retries. Three calls is harmless in a demo but expensive at thousands of queries per day, so behavioral evals are where production cost and reliability problems surface. (11:09-12:31)
- Behavioral evals are also the most expensive to run as the eval set grows, so cost governance matters: run a small eval subset in CI on prompt changes and reserve the full suite (hundreds of rows) for merges to the main branch. (34:45-35:41)
- These layers complement output-quality evals rather than replacing them; a system can pass layers one and two and still fail layer three. (11:09-12:31)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Trace Agent Tool Arguments to Debug Real Failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [Split LLM Judges Into Narrow Binary Metrics](split-llm-judges-into-narrow-binary-metrics.md)
- [Run eval suites in CI/CD before and during production](run-eval-suites-in-cicd-before-and-during-production.md)
- [Sequence Production AI by Pillars and Choose the Model Last](sequence-production-ai-by-pillars-and-choose-the-model-last.md)

Sources:
- [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](../sources/20260618_ObTPqBGsEbA.md), 09:22-12:31, 34:45-35:41
