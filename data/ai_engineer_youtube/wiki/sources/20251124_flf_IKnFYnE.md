# From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic

Source: [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE)
Uploaded: 2025-11-24
Transcript: `raw/20251124_flf_IKnFYnE/flf_IKnFYnE.en-orig.vtt`

## Summary

Samuel Colvin demonstrates how PydanticAI, Temporal, Logfire, and Pydantic Evals can turn fragile long-running agent scripts into durable workflows that survive process crashes, retry failed tool calls, replay completed LLM work from stored activity results, and expose step-level observability for debugging and evaluation.

## Extracted Concepts

- [Use Durable Execution for Production Agent Loops](../concepts/use-durable-execution-for-production-agent-loops.md) - this source shows PydanticAI agents wrapped with Temporal so completed LLM and tool work can resume after crashes.
- [Model LLM Calls and Tools as Durable Activities](../concepts/model-llm-calls-and-tools-as-durable-activities.md) - this source emphasizes turning both LLM calls and tool calls into recorded activities.
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](../concepts/keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md) - this source explains Temporal's deterministic workflow and non-deterministic activity split.
- [Compose Deep Research as Plan, Parallel Search, and Analysis Agents](../concepts/compose-deep-research-as-plan-parallel-search-and-analysis-agents.md) - this source presents a concise deep-research implementation with plan, search, and analysis agents.
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](../concepts/evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md) - this source shows why naive speed or step-count metrics can be misleading when the model reaches an answer by guessing.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

## Notes

- The talk frames durable execution as unnecessary for simple one-shot LLM calls but important once a workflow has enough turns, compute, user wait time, or tool side effects that restarting from scratch is costly, 00:36-01:06.
- A two-agent "20 questions" demo models a larger research loop: one agent asks questions through a tool, the tool runs another agent, and failures in the middle would otherwise lose all prior progress, 01:18-04:00.
- PydanticAI's Temporal wrapper turns agents into Temporal-backed agents while preserving an agent-like interface; the workflow code can remain close to the original agent code, 04:03-04:44.
- Temporal workflows must stay deterministic, while activities handle non-deterministic work such as IO and random behavior; Temporal records activity inputs and outputs so replay can reuse prior results, 04:47-05:36.
- The talk argues that durable agent support is weak if tool calls are not also represented as activities, because tool calls are central to agent behavior, 05:40-06:03.
- In the demo, unreliable tool calls fail randomly and Temporal retries them, letting the agent continue through transient runtime errors, 07:12-08:31.
- After killing an in-progress process, the demo resumes a specific workflow ID; prior LLM calls replay in milliseconds from stored results instead of being resent to the model, 08:34-10:42.
- Logfire is used to inspect workflow runs, nested model calls, activity execution, workflow IDs, search steps, token cost, and intermediate context, 08:44-10:13, 15:40-16:41.
- The Pydantic Evals segment compares GPT-4.1, Gemini, and Claude Sonnet 4.5 on the toy agent loop with pass/fail assertions, average cost, latency, and question count, but the speaker notes Gemini's apparent speed came partly from confidently inventing wrong answers that were not checked, 11:05-12:13.
- The deep research demo composes a plan agent, parallel search agents, and a final analysis agent; search results are formatted into XML-like context before final synthesis, 12:24-15:25.
- The durable deep-research version keeps ordinary Python control flow such as task groups for parallel search while wrapping the agents in Temporal, showing durable execution does not require a graph abstraction for simple staged workflows, 17:31-18:24.
- Long waits can be represented directly in the workflow code, such as sleeping for seven days, while Temporal handles pausing and resuming the workflow state, 18:08-18:15.
