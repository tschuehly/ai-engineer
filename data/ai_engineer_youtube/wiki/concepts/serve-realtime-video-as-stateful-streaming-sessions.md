# Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs

Summary: Real-time interactive video inference breaks the batch generative-media serving playbook on three axes at once: the unit of work is a pixel stream rather than a returned file, every session is long-lived and carries model state that has to be maintained, and the latency bar forces GPUs near users instead of in one region. Ahmed Ahres (Reactor) states this as the reason a real-time platform is separate infrastructure rather than a faster endpoint.

Use when:
- Planning to serve an interactive video, world-model, or live-avatar workload and reusing an existing batch generation stack.
- Budgeting for a real-time generative feature and deciding whether single-region GPU capacity is viable.
- Deciding where session memory lives when a generated world must stay consistent across a session.

Details:
- The batch shape being replaced: "you just send a request, a job gets run in the cloud… and it gives you back a file." Real time "is a different ballgame. You cannot just take what works for batch inference and apply to real time inference" (11:51-12:22).
- Streaming is the first divergence — pixels move server to client continuously, which "adds entire new complexities that batch generation does not have to think about" (12:22-12:36). The source names the requirement without naming a transport; see the wiki's WebRTC pages for that decision.
- Every session is live and stateful: "everything runs constantly, and there is memory to be kept into account." Memory is also the acknowledged weak point of the model class — in Genie 3 demos "the character can look back and then will not remember what's going on," so serving these models includes "maintaining that context window, so that you can remember what happened if you turned your character left and right" (12:37-13:04).
- Latency sets the deployment topology, not just the kernel: the target is "sub-100 millisecond latency anywhere you are," so "someone based in India or someone based in Japan should be routed to a GPU that is based in India or Japan, or as close as possible." Without worldwide compute "the experiences are not real time anymore and it breaks completely the medium" (13:05-13:32) — the failure is categorical rather than a degraded score, which is what distinguishes this budget from an ordinary p95 goal.
- Frame rate is the remaining model-side dial. Asked what it takes to move the demoed 16 FPS to 30 FPS, Ahres answers with serving techniques rather than a new model — multiple GPUs per session, optimizing the model weights, and quantization — and calls it "a matter of priorities" (14:28-14:55), which is the same lever set the wiki's diffusion-serving pages stack, applied to hold a frame budget rather than to shorten a single generation.
- The client-side surface stays small: loading a model with an API key and integrating it is described as "maybe 10 lines of code," with the platform absorbing streaming, session state, and routing (13:35-13:52). Ahres notes deterministic rule-checking layers over the simulation are not something Reactor does — developers build and open-source those on top (15:35-16:24).

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Real-Time Generation Changes the Medium, Not Just the Latency](real-time-generation-changes-the-medium-not-the-latency.md)
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)
- [Stack Additive Diffusion Optimizations for Real-Time Generation](stack-additive-diffusion-optimizations-for-real-time-generation.md)
- [Use WebRTC instead of WebSockets for realtime media streams](use-webrtc-instead-of-websockets-for-realtime-media-streams.md)
- [Voice Agent Infrastructure Needs Realtime Session Deployment](voice-agent-infrastructure-needs-realtime-session-deployment.md)

Sources:
- [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../sources/20260818_5dCAmSDOAjI.md), 11:51-13:52, 14:28-14:55, 15:35-16:24
