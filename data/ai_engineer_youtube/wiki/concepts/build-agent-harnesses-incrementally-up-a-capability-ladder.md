# Build Agent Harnesses Incrementally Up a Capability Ladder

Summary: Turn a bare model into a capable agent by adding one harness layer at a time and observing the gain at each step — tools, then safety, then autonomy, then a reasoning/feedback loop, then sub-agents, then self-optimization — so the harness (not the model) is the thing you iterate on.

Use when:
- Building a coding or task agent from scratch and unsure what to add first.
- Diagnosing which harness layer is missing when an agent underperforms.
- Explaining why "just a model with a few tools" is only the first rung, not the finished agent.

Details:
- The ladder is demonstrated on one fixed model and one fixed task (fix a bug in `median.py`) across seven examples; only the harness changes, and it improves the agent each time. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 06:01-06:18)
- Rung 0 — bare model: passes the prompt to the LLM with no tools; it can't read or write the file, so it can't act at all. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 08:33-09:37)
- Rung 1 — tools: give the agent `read`/`write` functions as tools; "the most obvious improvement to any harness is give it some tools." Now it can act, but raw file access is unsafe. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 09:40-12:33)
- Rung 2 — safety: wrap destructive/sensitive tools so they raise an interrupt requiring human approval (safe, but slow because every action is approved). ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 12:57-15:17)
- Rung 3 — autonomy: constrain capability instead of approving each call — e.g. partial function application to lock a tool's directory argument — so the agent runs unattended and safely. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 15:44-17:08)
- Rung 4 — reasoning/feedback loop: a ReAct (Reason + Act) loop — reason, act, observe, decide — looped until the tests pass; this is the first rung where the agent actually fixes the code and confirms the fix, "a really key pattern to making the agent better." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 18:04-20:48)
- Rung 5 — sub-agents: shift from doing the *same task* better to doing *more things*; give the top agent sub-agents (each with its own LLM call and tools) as tools, adding capability without bloating context. ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 21:29-25:21)
- Rung 6 — self-optimization: instead of trial-and-error, mark prompt variables for optimization and run a built-in optimizer (a GEPA optimizer) against a goal to "systematically measure and improve performance." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 25:22-28:51)
- Framing takeaway: an agent = model + harness, so the ladder is a checklist for the harness — "give it tools, make it safe, make it autonomous, make it reason, give it sub-agents, and have it self-optimize." ([Aditya Bhargava](../sources/20260707_2e9ANoOEn28.md), 31:29-31:52)
- **The orthogonal ladder: capability versus operations.** Anthropic's Applied AI team describes a second progression that runs alongside this one — Messages API, hand-rolled loop, agent SDK, managed runtime — but its rungs are graded by which of six *production* concerns are handled for you (hosting and scaling, session management, filesystem, execution isolation, credentials, observability) rather than by what the agent can do ([Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)). The two ladders are independent: a rung-6 self-optimizing agent can sit on a hand-rolled loop with no session durability, and a managed runtime can host a rung-1 tool-using agent. Climbing this page's ladder tells you nothing about whether the result can be operated. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 01:41-05:14)
- **Both ladders have a descending direction.** Anthropic's counterpart claim is that rungs get *removed* as models improve — a harness layer added to compensate for a model limitation "becomes pure overhead" once the limitation is gone ([A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)). Read against this page's demonstration that each added layer improves the agent, the two together give the fuller rule: add the layer when the gain is observable, and re-check the gain on every model upgrade rather than treating the rung as permanently earned. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 07:36-08:57)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Invest in the harness to run weaker and local models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Pre-bind tool arguments to give agents safe autonomy](pre-bind-tool-arguments-to-give-agents-safe-autonomy.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Route agent optimization by task profile, not one fixed loop](route-agent-optimization-by-task-profile-not-one-fixed-loop.md)
- [Decide the Agent Buy Boundary With Six Production Questions](decide-the-agent-buy-boundary-with-six-production-questions.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)

Sources:
- [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](../sources/20260707_2e9ANoOEn28.md), 06:01-28:51, 31:29-31:52
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 01:41-05:14, 07:36-08:57
