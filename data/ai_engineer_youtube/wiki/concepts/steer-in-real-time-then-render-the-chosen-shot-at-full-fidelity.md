# Steer in Real Time, Then Render the Chosen Shot at Full Fidelity

Summary: Cheap real-time generation is good enough to *find* a shot and not good enough to *be* it, so the workflow that falls out is two-tier: explore live at sub-second steering latency until the result is what you wanted, then re-render that result through a slower high-fidelity model. Keegan McCallum (uRun) puts this against today's prompt-and-retry loop, where each attempt is a paid gamble on a batch generation.

Use when:
- Designing the authoring loop for a generative-video or generative-media product.
- Deciding whether a real-time model must reach final-output quality before it is useful.
- Building a supervision surface for an agent that generates media.
- Costing a creative feature where users currently pay per failed attempt.

Details:
- The loop being replaced is a gamble with a per-attempt price: "so far we've very much had a slot machine type approach where you're setting up a prompt and maybe some keyframes and spending about $10 a minute to try and get the shot that you want" (05:02-05:17). The failure is that the intervention point comes *after* payment.
- The exploration tier: "with these models you can actually steer them in real time in under a second while they're generating and get the actual shots that you want," which he frames as more granular control over the content rather than a faster retry (05:17-05:36). Sub-second steering during generation is the requirement; anything slower reverts to retry.
- The commit tier: "with modern models like Google Gemini Omni, you can actually render these out as a more full fidelity clip" (05:36-05:47). The model name is captioned and unverified, but the structural point stands on its own — the cheap tier produces a decision, the expensive tier produces the deliverable.
- Why the tiers do not collapse into one: the real-time tier is explicitly the lower-quality one — roughly last year's frontier quality, and a minutes-long generation still has visibly better motion (01:34-02:28). The pattern therefore rests on the cheap tier being *representative* of the expensive one, which no source in this wiki measures.
- A second use of the same live surface is supervision rather than authoring: "maybe you're piloting an agent that you're able to look over its shoulder and see what it's generating in real time" (05:26-05:33). Real-time output turns a generating agent from a job you wait on into a process you can interrupt — the media analogue of streaming a coding agent's steps.
- Caveats: the workflow is asserted, not demonstrated end to end in the talk; no handoff mechanism is described for carrying a steered real-time result into the high-fidelity render (seed, conditioning frames, or recorded control track), which is the part an implementer has to invent.

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Real-Time Generation Changes the Medium, Not Just the Latency](real-time-generation-changes-the-medium-not-the-latency.md)
- [Track the Efficiency Axis in Generative Video, Not Only Quality](track-the-efficiency-axis-in-generative-video-not-only-quality.md)
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)
- [Pick a Real-Time World-Model Class by What the User Steers](pick-a-realtime-world-model-class-by-what-the-user-steers.md)
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md)

Sources:
- [Generative Video at the Speed of Light — Keegan McCallum, uRun](../sources/20260818_Xln-On3syJk.md), 01:34-02:28, 05:02-05:47
