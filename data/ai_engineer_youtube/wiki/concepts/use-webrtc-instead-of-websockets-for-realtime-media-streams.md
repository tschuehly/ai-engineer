# Use WebRTC Instead Of WebSockets For Realtime Media Streams

Summary: WebSockets are convenient for long-lived structured-data connections, but realtime audio/video needs media transport that can prioritize fresh packets over guaranteed delivery. WebRTC provides low-latency, best-effort media behavior plus built-in media adaptation machinery that is hard to recreate on top of TCP.

Use when:
- Choosing a transport for browser, native, or edge-to-cloud realtime audio/video in a voice agent.
- Diagnosing voice-agent glitchiness, latency spikes, or disconnections caused by TCP/WebSocket media transport.

Details:
- The talk recommends WebSockets for server-to-server use cases, small structured data, and prototypes, while recommending WebRTC for audio/video streams over the internet from web or native apps. (04:39-04:56)
- WebSockets sit on TCP, whose in-order delivery and retry behavior is useful for ordinary requests but conflicts with conversational latency because packet loss or jitter can block later media. (04:58-06:29)
- Realtime audio often cares less about a packet from a second ago than about staying inside the current latency budget; WebRTC sends media quickly and can ignore packets that arrive too late. (05:34-06:09)
- WebRTC also supplies media-specific pieces such as resampling, packetization, bandwidth estimation, stats, and observability; a WebSocket path would need to rebuild those concerns explicitly. (06:44-07:25)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Use frame pipelines to compose realtime voice agents](use-frame-pipelines-to-compose-realtime-voice-agents.md)

Sources:
- [Your realtime AI is ngmi - Sean DuBois (OpenAI), Kwindla Kramer (Daily)](../sources/20250731_E71YtNbCFXY.md), 03:25-07:25
