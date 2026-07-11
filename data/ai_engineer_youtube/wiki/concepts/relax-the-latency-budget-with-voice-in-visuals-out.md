# Relax the Latency Budget by Choosing Voice-In, Visuals-Out Over Voice-Out

Summary: Full voice-in/voice-out conversation demands a punishing ~200 ms response to feel conversive, but visual output has a far more forgiving ~1 s envelope, so pairing voice input with a visual (not spoken) response lets you ship delightful, responsive AI experiences today without novel realtime architectures.

Use when:
- Deciding whether an AI product's response should be spoken audio or an on-screen visual/UI artifact.
- Justifying a voice-in/visuals-out interaction shape on engineering (not just UX) grounds.
- Setting a latency target for a voice-driven experience and choosing whether you need a 200 ms-slice realtime stack.

Details:
- Human latency thresholds (known since the '60s): ~100 ms feels instant; ~1 s is the limit before people lose their train of thought and mentally move on; a fully conversive voice-in/voice-out exchange needs ~200 ms or less so people can interject, agree, and form connection in real time. 05:22-07:00
- Getting a network round-trip + speech-to-text + model inference + return inside 200 ms is "a ridiculous amount of work"; the visual response envelope is the escape hatch — something appearing on screen within ~1 s of the user speaking still feels seamless and within their attention span. 07:00-08:20
- This is why the voice-in/visuals-out asymmetry is an *engineering* win, not only a UX preference: you get voice's high-bandwidth input while responding into the ~5x looser visual envelope. 08:04-08:20
- The alternative you avoid: novel voice-in/voice-out architectures (Thinking Machines / Neolab demoed time-slicing into 200 ms chunks with continuous inference in/out at 200 ms slices) exist, but you don't have to wait for them if visuals-out meets the need. 07:20-07:50
- Karpathy framing behind the choice: voice is the human-preferred *input* (a third of the brain is visual, but speech is our highest-bandwidth channel), while rich visuals — now generatable as HTML, interactive controls, and illustrations via tool calling — are the preferred *output*. 00:17-01:29

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Pair low-bandwidth voice input with high-density multimodal output](pair-voice-input-with-high-density-multimodal-output.md)
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)
- [Hit soft-realtime latency with a fast model, eager inference, and prefix caching](hit-realtime-latency-with-fast-models-eager-inference-and-prefix-caching.md)

Sources:
- [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](../sources/20260628_65X0pQ6Lmbg.md), 00:17-08:20
