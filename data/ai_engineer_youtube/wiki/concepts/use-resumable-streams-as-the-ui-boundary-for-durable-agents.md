# Use Resumable Streams as the UI Boundary for Durable Agents

Summary: Durable agent products need a streaming boundary that can survive workflow execution details. Resumable streams let the UI continue receiving agent output while the backend records steps, inputs, outputs, and events for inspection or recovery.

Use when:
- Building a chat or coding-agent UI on top of a durable workflow run.
- Deciding how to connect long-running backend agent execution to frontend progress and observability.

Details:
- Workflow DevKit is presented as adding resumable streams, suspend/resume behavior, and webhook-based human-in-the-loop flows to an existing AI SDK agent, 04:34-04:50.
- After moving the agent call and tools into workflow steps, the demo keeps the frontend stream behavior unchanged while the backend gains durable isolated execution on deployment, 16:35-17:23.
- The local workflow web UI shows each marked step as a span with inspectable inputs, outputs, and events, giving the agent stream an operational trace instead of only chat text, 17:30-18:03.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Treat long waits as logical workflow state](treat-long-waits-as-logical-workflow-state.md)

Sources:
- [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](../sources/20260106_kmV-qg4uoNI.md), 04:34-04:50, 16:35-18:03
