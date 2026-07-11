# Record and Replay Agent Runs at Node Boundaries

Summary: Because a failed agent run rarely repeats its trajectory, make failures debuggable by recording the semantic input/output of every node boundary as a frozen trace, so you can re-enter the exact historical run and step through it with zero model calls — durability keeps the loop alive, but only replay makes it debuggable.

Use when:
- An autonomous agent corrupts a record in production and standard telemetry re-runs succeed every time.
- Designing observability for non-deterministic agents where you must root-cause a run you cannot reproduce.

Details:
- The motivating loop: a non-deterministic failure is gone the moment it happens; if you can't reproduce it you can't debug it, if you can't debug it you can't promise it won't hit the next customer. The one costly run — not the average run — is what you lose, 00:41-01:29.
- Durability is not debuggability: durable-execution engines keep the agent loop alive through state recovery, but state recovery reconstructs the present — it does not let you re-enter the precise historical run that caused an erratic mutation (talk description). The goal is replayability (observability: re-validate a run that already happened well enough to debug it), not bitwise determinism (controllability you can't get from a hosted API and don't want), 05:33-06:14.
- Record at the boundary, not the network layer: half an agent's work never touches the network (local retrieval, in-process tools, memory) and packet capture shreds under streaming/async. Capture what enters and leaves each node — the meaning of each step, not the packets, 06:14-06:47.
- A "boundary" is a bounding box around any node — a tool call, an LLM call, or a RAG retrieval. Annotating a method with the boundary annotation records every input/output pair and lets you attach session variables (model version, code/build version, RAG chunks) so the entire state of the run is frozen and saved as a trace, 07:15-08:35, 13:11-13:36.
- The trace is hyper-detailed per node (metadata like model version and sampling version, plus input/output JSON), so you can walk one node back from a bad `place_order(quantity=1000)` tool call to the LLM node that emitted it, 08:35-10:11.
- What replay buys is a deterministic CI: stop the model and rerun the exact failure line with zero model calls. The end-to-end loop is annotation → recording → visualization → understanding → fixing → replaying → verifying, 06:47-07:15.
- This is the Mozilla-rr record-and-replay philosophy brought into the agent loop — it goes beyond API mocking or response caching by capturing every model invocation, tool payload, memory-boundary read, and intermediate state transition into an append-only event log (talk description).

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [LLM Inference Is Non-Deterministic Even at Temperature Zero](llm-inference-is-non-deterministic-even-at-temperature-zero.md)
- [Turn Recorded Agent Traces Into Free Replay Test Cases](turn-recorded-agent-traces-into-free-replay-test-cases.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)

Sources:
- [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../sources/20260629_Lc8zRh9muoY.md), 00:41-10:11, 13:11-13:36
