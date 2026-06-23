# Fix Tool Discipline Before Reaching for a Bigger Model

Summary: For tool-use tasks, the failing behavior is often tool discipline — discovering available tools and schemas, inspecting before querying, and self-correcting on tool errors — not reasoning depth, so cheap behavior-focused RL on a small model can beat a much larger reasoning model.

Use when:
- A tool-using agent fails on a task and the default reaction is to swap in a larger, "smarter" model.
- Deciding whether a performance gap is a reasoning gap or a behavior gap before spending on a bigger model or more inference.

Details:
- Snorkel and the UC Berkeley RLLM ("Agentic") lab made a 4B model outperform Qwen 3 235B on a financial-analysis tool-use task; the headline framing is "stop making models bigger, make them behave." (02:47-03:05)
- Failure trace of the large model: asked for YouTube year-over-year ad-revenue growth, Qwen 3 235B queried a table that did not exist (without inspecting the environment first), queried again with nothing back, then hallucinated an answer. Greater reasoning did not help when the task required using tools. (07:08-08:00, 14:38-14:58)
- Success trace of the finetuned 4B model: it called `get_table_names` to discover tables, `get_table_info` to inspect the schema, ran a query, hit a missing-column error (it asked for a `revenue` column that did not exist), then self-corrected to the right column and returned the correct answer. The two key learned behaviors were tool discovery and error self-correction. (14:58-16:10)
- RL is positioned as a lever for changing *behavior*, not for adding *knowledge*: tool discipline is a behavior problem, so RL is the right tool, whereas changing core facts inside the model is not what it is best at. (05:59-06:02)
- The "Terence Tao effect" (RLLM team's framing): a financial analyst does not need a mathematician brilliant at everything; a much larger model is "a sledgehammer to crack a walnut" for a narrow SQL-and-arithmetic tool task. (06:20-07:00)
- Cost: GRPO on a 4B base in Snorkel's FinQA environment ran as a ~21-hour job at under $500 per run, with pass@1 roughly doubling — non-trivial gains are tractable, especially for teams already hosting their own or on-prem models for cost, speed, security, or data-control reasons. (10:56-11:26, 13:56-14:00)

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Use Agent RFT after baseline and task optimization](use-agent-rft-after-baseline-and-task-optimization.md)
- [Train on the Simplest Task Variant That Transfers](train-on-the-simplest-task-variant-that-transfers.md)
- [Decompose Evals Into Rubrics to Target the Failing Behavior](decompose-evals-into-rubrics-to-target-the-failing-behavior.md)
- [Build RL environments as software artifacts](build-rl-environments-as-software-artifacts.md)

Sources:
- [Stop Making Models Bigger, Make Them Behave — Kobie Crawford, Snorkel](../sources/20260610_TNwJ1LMiENk.md), 02:47-16:10
