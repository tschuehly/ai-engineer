# VoiceVision agents wrap visual RAG with retrieval, image-reading, and speech tools

Summary: A visual-document RAG workflow can be exposed as a small agent that owns retrieval, image prompt construction, answer generation, and optional speech output. The agent layer is useful when users should ask natural questions and receive spoken answers over retrieved document pages.

Use when:
- Building a voice-facing assistant over scanned or image-heavy documents.
- Adding agent orchestration around a visual-RAG pipeline without turning the retrieval implementation into a monolithic prompt.

Details:
- Debnath uses Strands as a lightweight model-plus-tools agent framework: the agent is configured with a model and tools, then asked the user question, 53:53-56:16.
- The visual-RAG agent uses a custom Qdrant retrieval tool to fetch relevant pages and an image-reader tool to build the multimodal prompt for final answer generation, 01:02:48-01:04:00.
- The voice extension adds a speech tool so the same retrieved visual context can produce both a text answer and spoken response, 01:04:10-01:05:12.
- This is a chained voice interface over RAG rather than a speech-to-speech conversational architecture: retrieval and visual grounding remain explicit tools in the workflow.

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Treat PDF pages as visual retrieval units](treat-pdf-pages-as-visual-retrieval-units.md)
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response - Suman Debnath, AWS](../sources/20251206_hwCmfThIiS4.md), 53:53-56:16, 01:02:48-01:05:12
