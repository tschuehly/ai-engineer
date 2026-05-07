# Choose WebRTC Topologies By Realtime Application Shape

Summary: WebRTC is not only a browser-to-cloud voice-agent pipe; it can support local peer-to-peer devices, cloud AI servers, and multiparty realtime applications. The topology should match where the model, device, and collaborators need to live.

Use when:
- Designing a realtime voice or multimodal agent that may run locally, in the cloud, or inside meetings.
- Deciding whether a small device should connect directly to a nearby machine, to a cloud AI service, or to a multiparty framework.

Details:
- The Squabbert demo used a Raspberry Pi running MLX Whisper, Gemma 3, and custom sampler logic, then connected peer-to-peer over WebRTC directly to a laptop on the same local network. (10:51-12:38)
- The speakers describe WebRTC as flexible enough for local device-to-laptop connections, edge devices connecting to cloud servers for AI work, or multiparty Pipecat-style connections that bring LLMs into meetings. (12:23-13:08)
- This topology choice matters because voice can be an interface to remote compute while the user interacts through small nearby devices. (09:53-09:59)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Use WebRTC instead of WebSockets for realtime media streams](use-webrtc-instead-of-websockets-for-realtime-media-streams.md)
- [Use edge inference when latency, privacy, offline access, or token cost dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)
- [Use frame pipelines to compose realtime voice agents](use-frame-pipelines-to-compose-realtime-voice-agents.md)

Sources:
- [Your realtime AI is ngmi - Sean DuBois (OpenAI), Kwindla Kramer (Daily)](../sources/20250731_E71YtNbCFXY.md), 09:53-13:08
