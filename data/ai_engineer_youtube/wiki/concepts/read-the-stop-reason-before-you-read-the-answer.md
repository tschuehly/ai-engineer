# Read the Stop Reason Before You Read the Answer

Summary: The named anti-pattern in an agent loop is calling the model, taking the response, and using it. The response text does not say why the model handed control back, and the two most consequential reasons — it wants a tool run, or it hit the output limit mid-work — both produce text that reads like an answer. Branch on the stop reason first; treat the text as valid only on the branch where the model actually finished.

Use when:
- Writing the loop body of a tool-using agent yourself rather than inheriting a framework's.
- Debugging an agent that returns confident, well-formed output that turns out to be built on work it never completed.
- Deciding where in a loop the human-in-the-loop or confidence check belongs.

Details:
- The anti-pattern is stated plainly: "What you don't want is just to let the agent go and do something and get the response back and use it. What you want to do is you want to loop with something called the stop reason." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 08:03-08:17)
- The reason the loop needs the branch at all is that the model is not the executor: "The problem is the LLM can't do anything. It is just a probabilistic next word predictor. It can't execute tools… if you point it to a tool, it can figure out how to set things up so that you or your code can execute it." The response on a tool-use stop is "basically the parameters that it has extracted from the data that you provided it," and your code runs them. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 08:48-09:28, 10:08-10:17)
- The loop shape shown is `while True`: call the model with the messages, the prompt, the context, and the tool definitions; read the stop reason; if it is tool use, run the tool, hand the result back, and iterate; when the model comes back without a tool call, "we're at the end of our loop." ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 08:19-10:35)
- **The truncation branch is the one that costs you silently.** "One of the stop reasons may be you have run out of tokens, and this response is based on partial when the LLM had to stop. And it's going to give you a response, but if you have run out of tokens, then you need to take action." A hit output limit does not announce itself in the prose — the model still produces a plausible closing answer, so the only place the partiality is visible is the stop reason. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 10:50-11:12)
- The loop exit, not the middle, is the natural gate: "then we take the answer, and this is an opportunity for you to have a human in the loop potentially. You check the confidence. If it looks good, you keep it. If you don't, then you escalate to a human." Placing the check there means it runs once per completed task rather than once per tool call, which is the difference between a gate and [approval fatigue](escalate-risky-actions-to-a-read-only-review-subagent.md). ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 10:36-10:49)
- The framing generalizes past one API: the stop reason is treated as a standing diagnostic channel — "every time something happens, there's a stop reason and you need to take a look at that because that can give you a lot of information about what's going on" — and it is listed as exam material under agentic loops and control, which is [evidence about what breaks in production](read-a-certification-blueprint-as-a-map-of-production-anti-patterns.md) rather than about one vendor's SDK. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 04:47-05:05)
- **Limits.** This is a ~20-minute conference talk built around exam preparation, with code shown on slides the transcript does not capture, no enumeration of the full stop-reason set, no handling recipe for the out-of-tokens case beyond "take action," and no measured failure rate for loops that skip the check. The claim is an architectural argument, not a study.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)
- [Use field-level confidence signals for human review](use-field-level-confidence-signals-for-human-review.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Contain retry amplification in agent loops](contain-retry-amplification-in-agent-loops.md)
- [Read a Certification Blueprint as a Map of Production Anti-Patterns](read-a-certification-blueprint-as-a-map-of-production-anti-patterns.md)

Sources:
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 04:47-05:05, 08:03-11:12
