# Real-Time Generation Changes the Medium, Not Just the Latency

Summary: When generated output arrives fast enough to steer while it is still being produced, the product category changes rather than merely getting quicker — the user can now act on the output, which is a different affordance from receiving it. Ahmed Ahres (Reactor) argues this with two historical cases where a latency change created industries, and applies it to generated video, where the batch shape (prompt, wait, receive a file) leaves nothing to do with the result.

Use when:
- Deciding whether a latency target on a generative feature is an optimization or a product bet.
- Arguing why a real-time version of an existing generative capability is worth separate infrastructure rather than a faster batch endpoint.
- Positioning a generative-media product against the file-returning incumbents.

Details:
- The batch failure is stated as an affordance problem, not a quality problem: with the current video models — captioned "VO3" and "C dance 2" (Veo 3 and Seedance 2) — "you prompt them, you get back a file, you watch and good luck. It's a slot machine. You cannot change it," and "a generated video… is still a recording" (01:11-01:31, 02:43-02:55). Ahres's summary: "real time changes what the medium is. It doesn't just make it faster" (02:55-02:58).
- Case one, maps to GPS: before, "someone produces a map, you look at where you are, and that's it." GPS made your own position continuously available, which reads like a speedup but was not — "Uber would not exist if we did not have the GPS" (03:04-03:29).
- Case two, film to viewfinder, which he considers the stronger case: on film "they can't see what they're shooting," so the feedback arrives after processing. Digital capture let the shooter "see what's going on in the screen and adapt accordingly," and that is a precondition for consumer-scale quality — "Instagram and TikTok would not exist if we could not produce high-quality content," which is possible because "it's not a slot machine" (03:33-04:22).
- The generalization he draws is that real-time output becomes *programmable*: "you can address it, you can condition it, you can change it," the same way software is (04:24-04:37). Concretely he demos an image-conditioned scene generating live and prompts a cat into it mid-generation, noting the batch alternative offers no point of intervention at all (05:09-05:41).
- Why control is the lever in creative products: "the big problem that content creators all have is I don't have the control I need… this is always the thing that any filmmaker or movie producer or any content creator will tell you," and his slogan is "instant feedback is the ultimate level of control," unreachable without real time (05:47-06:23).
- The market consequence he expects first is advertising generated at view time rather than pre-produced — "why can't I produce an ad in real-time in front of you? We don't need to pre-produce anything" — gated not by capability but by brand risk tolerance, "if their logo has one pixel that is white instead of dark" (06:23-07:05).
- Caveat carried by the source: it is a vendor's positioning talk (Reactor sells the platform), the argument is by historical analogy rather than measurement, and Ahres concedes current output quality limits it — the video-editing products built on it are "not very good yet just because of the quality of the models" (10:32-10:57).

Related topics:
- [Generative Media](../topics/generative-media.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Pick a Real-Time World-Model Class by What the User Steers](pick-a-realtime-world-model-class-by-what-the-user-steers.md)
- [Serve Real-Time Video as Stateful Streaming Sessions, Not Batch Jobs](serve-realtime-video-as-stateful-streaming-sessions.md)
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)
- [Reliability and Stylistic Range Are Opposite Model Positions](reliability-and-stylistic-range-are-opposite-model-positions.md)

Sources:
- [The Next Medium: Why Real-Time Interactive Video Changes Everything — Ahmed Ahres, Reactor](../sources/20260818_5dCAmSDOAjI.md), 01:11-07:05, 10:32-10:57
