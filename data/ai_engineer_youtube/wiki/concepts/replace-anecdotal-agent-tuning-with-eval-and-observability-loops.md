# Replace Anecdotal Agent Tuning With Eval and Observability Loops

Summary: Agent teams should build evaluation sets, trace production behavior, cluster failures, and use those aggregates to tune prompts, tools, models, memory, and orchestration instead of optimizing from a few memorable examples.

Use when:
- Choosing agent hyperparameters such as model, tool count, memory, number of agents, or orchestration pattern.
- Turning production traces and human review into a repeatable agent improvement workflow.

Details:
- A useful agent eval set defines expected inputs and outputs, making agent development more like test-driven development and enabling comparison across model, tool, memory, and orchestration choices, 09:47-10:28.
- Human-reviewed outputs should be added back to the evaluation set, then batch runs should be analyzed for failures, clustered, summarized, and used to suggest improvements, 11:03-11:29.
- The talk calls out "development by anecdote" as a current failure mode and recommends batch evaluation plus aggregate analysis to make tuning steps more reliable, 12:29-12:53.
- Once agents reach customers, detailed logs, tracing, OpenTelemetry-style integrations, clustering, and automated summarization help teams see the real failure categories and improve the system, 12:56-13:36.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Agent traces require specialized eval infrastructure](agent-traces-require-specialized-eval-infrastructure.md)
- [Cluster conversation outputs to prioritize AI product work](cluster-conversation-outputs-to-prioritize-ai-product-work.md)

Sources:
- [Building Applications with AI Agents — Michael Albada, Microsoft](../sources/20250724_R30col3UPUg.md), 09:47-13:36
