# Turn Recorded Agent Traces Into Free Replay Test Cases

Summary: A recorded agent run can double as a regression test: reload the trace in replay mode, stub every node except the one you changed, run that node live, and assert on its output — the stubbed LLM never gets called, so the test is deterministic, rerunnable, and free.

Use when:
- You added a guardrail or fixed a tool and want to verify it against the exact production run that failed.
- Building a deterministic test suite for an agent whose live runs are non-deterministic and expensive.

Details:
- The recording that captured every node's input/output is reusable as a fixture: fix your code at (say) the tool level, then run a test suite against the same recorded trace, stubbing every node except the one you changed so the exact stack trace is preserved, 10:16-11:00.
- In replay mode the changed node runs live while the rest are stubbed from the trace — e.g. stub the first LLM/agent node that emitted the bad tool call, run the guardrailed tool live, and assert the order got blocked; the assertion passes because the live tool now blocks, 11:00-12:08.
- Because the boundary layer already captured tool output, it can also drive the assertions — "merging replayability traces with auto-generated testing, stubbing, and assertions," 11:56-12:08.
- Two distinct testing modes, both important, 12:08-13:11:
  - Deterministic testing targets the deterministic nodes (guardrails, tool calls). Freezing the run as context and stubbing the LLM "kicks the probability out of the window," so the whole run becomes a rerunnable test case that never calls the model and is therefore free.
  - Behavioral testing targets subjective properties (agent tone, whether the trajectory was right); this is where LLM-as-judge fits.
- Operational rule: use replay to debug — find the issue, fix the failure, then reuse the same trace as a test case — while still keeping generation-time variation alive in production (don't pin temperature to zero), 13:36-13:52.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Record and Replay Agent Runs at Node Boundaries](record-and-replay-agent-runs-at-node-boundaries.md)
- [LLM Inference Is Non-Deterministic Even at Temperature Zero](llm-inference-is-non-deterministic-even-at-temperature-zero.md)
- [Replay Production Failures Before Promoting Prompt Fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Layer agent evals as deterministic, semantic, and behavioral checks](layer-agent-evals-as-deterministic-semantic-and-behavioral-checks.md)

Sources:
- [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../sources/20260629_Lc8zRh9muoY.md), 10:16-13:52
