# Multilingual Voice Agents Need Language Detection and Switching

Summary: Multilingual voice agents need language identification, speech synthesis coverage, and prompt-level control over when to switch languages. The language layer should be explicit because user comfort, regional requirements, and mixed-language inputs can all change during a spoken session.

Use when:
- Building a voice agent for multilingual users or regulated regions with official-language requirements.
- Deciding whether language switching should be automatic, user-requested, or constrained by prompt policy.

Details:
- The workshop frames multilingual conversational AI as a pipeline concern: the user speaks in one language, speech is transcribed, an LLM reasons over the text, and speech is synthesized back in the selected language. 08:29-09:24
- ElevenLabs' language detection system tool can identify different languages and switch between them; the agent configuration can override the default LLM prompt to customize language-switch behavior for the use case. 09:28-09:47, 23:13-23:33
- A Singapore conference demo uses official-language requirements as the product reason for multilingual support, then demonstrates asking the agent which languages it supports and requesting a switch. 20:37-25:05
- Mixed-language inputs are possible but become less reliable as more languages are interleaved; language-learning products may need prompt guidance and narrower language pairs rather than unconstrained multilingual switching. 44:00-47:35, 52:18-54:42

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Choose Voice-Agent Architecture by Latency, Accuracy, and Semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Evaluate Speech-To-Speech Models Against Enterprise Control Needs](evaluate-speech-to-speech-models-against-enterprise-control-needs.md)

Sources:
- [[Full Workshop] Building Conversational AI Agents - Thor Schaeff, ElevenLabs](../sources/20250731_MPtCBaZn84A.md), 08:29-09:47, 20:37-25:05, 44:00-47:35, 52:18-54:42
