# Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth

Summary: A tool or MCP server author sees tool calls and nothing else — not the user, not the codebase, not the framework the output has to fit. Adding optional arguments that exist purely to be logged recovers a segmentation dimension cheaply, provided you use the field to compare cohorts rather than to make per-call decisions, because "agents lie."

Use when:
- You ship a server or tool used through someone else's client and cannot see the environment your output lands in.
- Output quality varies and you suspect it varies by a property of the consumer (language, framework, repo size, product tier) that you have no way to observe.
- The protocol's user-facing primitives (elicitation, prompts, consent dialogs) are unavailable or unreliable in the clients you support.

Details:
- The blindness that motivates it: Figma "didn't know if the react tailwind code would be successful for other types of code bases," and "outside of the elicitation and sampling which didn't really work as we wanted there was no way of getting that information from the user." 12:29-12:45
- The mechanism: "we added some optional query arguments to our tool calls for ones like get design context where they would send back what sort of language what sort of framework the user might be using." The argument is optional and carries no behavioural requirement — it is a field in the schema whose purpose is to appear in the server's logs. 12:45-12:53
- The stated reliability, and why it is tolerable: "This is imperfect uh agents lie but it was at least a signal for us to understand like oh this type of user… may not have had a good experience. Perhaps our translation layer wasn't working as well." Noise that would be disqualifying for a per-call decision is acceptable for cohort comparison, where the question is whether one segment's outcomes differ from another's and mislabelling is diluted across many calls. 12:53-13:09
- The tool schema becomes a telemetry surface. This is a different act from reading the arguments a model chose in order to debug one run, which is the subject of [Trace Agent Tool Arguments to Debug Real Failures](trace-agent-tool-arguments-to-debug-real-failures.md): there the argument is evidence the model produced for its own reasons, here the argument was designed into the signature so that it would be recorded. The two coexist — the same trace serves both — but only one of them changes the interface.
- The cost is charged to the context budget and to the model's attention. Every optional field adds description text to the tool schema on every session handshake and gives the model one more decision to get wrong, which is exactly the pressure described in [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md). A telemetry-only field should be justified by a question you will actually answer with it.
- What it is not a substitute for: consent. Figma wanted elicitation to *ask permission* before mapping a user's codebase, and no self-reported argument supplies that. Instrumentation recovers observation, not authorization.
- Design rule that follows: pick the field to match the specific hypothesis you already hold about your output. Figma's framework field exists because their serializer emits React and Tailwind for everyone — see [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md) — so the segment most likely to be failing was knowable in advance and worth naming in the schema.
- No result is reported. The talk says "We have found that that works pretty well but this was kind of our way of verifying that," with no segmentation finding, no quality difference between framework cohorts, and no estimate of how often the self-report is wrong.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Trace Agent Tool Arguments to Debug Real Failures](trace-agent-tool-arguments-to-debug-real-failures.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Tools Are the Only Primitive Every Client Implements](tools-are-the-only-primitive-every-client-implements.md)
- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md)
- [Read Employee-Built Automations as the Productionization Backlog](read-employee-built-automations-as-the-productionization-backlog.md)

Sources:
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 12:29-13:09
