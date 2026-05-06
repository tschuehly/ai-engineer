# OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal

Source: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc)
Uploaded: 2026-01-12
Transcript: `raw/20260112_k8cnVCMYmNc/k8cnVCMYmNc.en-orig.vtt`

## Summary

Cornelia Davis frames production agents as distributed systems that need durable execution around LLM calls, tool calls, retries, crashes, human waits, and multi-agent orchestration. The talk shows how Temporal can wrap OpenAI Agents SDK loops and tool implementations so agent workflows can persist state, avoid re-burning completed LLM calls after crashes, resume after long waits, and orchestrate small agentic loops with normal code constructs such as parallelism and waits.

## Extracted Concepts

- [Use durable execution for production agent loops](../concepts/use-durable-execution-for-production-agent-loops.md) - this source explains why agent loops need persistence across crashes, rate limits, and downstream failures.
- [Model LLM calls and tools as durable activities](../concepts/model-llm-calls-and-tools-as-durable-activities.md) - this source shows Temporal activities wrapping external calls and agent tools.
- [Treat long waits as logical workflow state](../concepts/treat-long-waits-as-logical-workflow-state.md) - this source describes human-in-the-loop waits that can last hours, days, or weeks without keeping a live process pinned.

## Topic Links

- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

## Notes

- Temporal is presented as a backing service for distributed-systems durability, allowing developers to write the happy-path business logic while the service and SDK handle retries, crashes, and persisted results around agent work, 07:46-11:35.
- Agentic loops in the OpenAI Agents SDK repeatedly call the LLM, execute requested tools, append results to conversation history, and continue until the LLM decides it is done, 05:35-07:26.
- Wrapping external work as Temporal activities lets a workflow configure retry policies such as exponential backoff, retry caps, and retry windows without hand-writing retry code around every call, 14:00-15:43.
- Putting an Agents SDK agent inside a Temporal workflow makes the agent and its activity-backed tools durable; a plain Python-library agent would lose in-flight state if its process were killed, 50:05-51:44.
- Human-in-the-loop agent flows often wait for hours or days; Temporal can evict waiting workflow state from active memory and later reconstitute it when the user responds, 58:24-60:02.
- The talk distinguishes an agent's fixed loop from LLM-selected flow: the code may keep the loop stable while the model decides which tool or next action to take inside that loop, 62:19-62:40.
