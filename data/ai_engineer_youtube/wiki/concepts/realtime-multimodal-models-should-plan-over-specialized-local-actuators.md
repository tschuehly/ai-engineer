# Realtime Multimodal Models Should Plan Over Specialized Local Actuators

Summary: Realtime multimodal models can provide perception, conversation, and task planning, while specialized local models or controllers execute physical actions.

Use when:
- Designing robotics, augmented-reality, or embodied-agent systems that need natural interaction but also reliable low-level control.
- Deciding whether a general realtime model should directly control actions or delegate to specialized local components.

Details:
- Bailey describes Gemini Live as a realtime interaction model that can use audio, video, and screen context for conversation.
- In the Pupper robot example, Gemini models support perception such as object detection and environmental response, while Gemini Live can flexibly interpret user intent.
- The orchestration boundary is explicit: Gemini Live should build the plan and invoke models local to the robot for actions such as picking up specific items, rather than directly controlling robotic actions.

Related topics:
- [Agents](../topics/agents.md)
- [Voice Agents](../topics/voice-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)

Sources:
- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md), 19:29-19:41, 59:29-60:29
