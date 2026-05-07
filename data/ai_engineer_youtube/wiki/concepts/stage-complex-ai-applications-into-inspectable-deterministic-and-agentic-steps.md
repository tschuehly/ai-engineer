# Stage Complex AI Applications Into Inspectable Deterministic and Agentic Steps

Summary: Complex AI applications become easier to operate when a single prompt is decomposed into named stages that separate deterministic extraction, LLM/tool reasoning, review, escalation, and final packaging.

Use when:
- Turning a demo prompt into a production workflow.
- Debugging a multi-step agent where failures need stage-level attribution.

Details:
- Trainline frames agentic systems as sitting between deterministic software and nondeterministic ML, so quality work must account for both predictable code paths and model behavior, 17:55-19:00.
- The support-triage workflow starts with ticket input and deterministic context collection, then breaks the agentic portion into LLM/tool-call triage, policy review, reply writing, escalation decision, and final output stages, 30:05-31:09.
- The workshop closes by describing the move from a single-shot prompt into a five-stage agentic workflow with tool calls, then adding tracing and evaluation around the stages, 01:33:31-01:33:55.
- Staging introduces more places where things can go wrong, but makes failures easier to debug because traces can show which step failed, 01:34:47-01:35:16.
- Zapier's Scout Agent applies the same staged shape to support-driven code fixes: diagnosis, categorization, fixability assessment, plan/execute/validate in GitLab CI, support review, iteration, and engineering review. (10:09-12:04)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md), 17:55-19:00, 30:05-31:09, 01:33:31-01:35:16
- [Your Support Team Should Ship Code - Lisa Orr, Zapier](../sources/20251216_RmJ4rTLV_x4.md), 10:09-12:04
