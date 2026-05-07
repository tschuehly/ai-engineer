# Assemble Realtime Multimodal Context for Lab Agents

Summary: Realtime scientific agents need a context assembly layer that turns the currently connected lab modalities into the prompt or API payload for each model call. The model should see the experiment protocol, sensor state, images, voice or text input, and chat history that are relevant to the current observation.

Use when:
- Building lab, robotics, or field agents that observe changing physical conditions.
- Deciding how to combine sensors, cameras, voice, text, and experiment metadata before an LLM call.

Details:
- Druga's prototype uses a React app with JackDac/WebUSB sensors, webcams, text input, voice input, frontend hooks, a backend, and Gemini API calls. (08:37-09:15)
- The context assembly layer checks which modalities are present, such as text, voice, image, and chat history, and builds the context sent to the API for each message. (09:18-09:56)
- Experiment protocols are part of the context: the user can describe the experiment type, conditions, and constraints so microscope images or sensor readings are interpreted in the right scientific frame. (01:35-02:14)
- Dynamic context injection depends on both connected sensors and the protocol being created, so the same system can support different realtime experiments without one static prompt shape. (10:00-10:14)

Related topics:
- [Agents](../topics/agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)

Sources:
- [Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind](../sources/20250728_wNH3q9pqn0U.md), 01:35-02:14, 08:37-10:14
