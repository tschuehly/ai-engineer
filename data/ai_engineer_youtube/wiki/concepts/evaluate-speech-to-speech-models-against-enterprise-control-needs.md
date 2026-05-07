# Evaluate Speech-To-Speech Models Against Enterprise Control Needs

Summary: Native speech-to-speech models can preserve audio information, improve conversational dynamics, and reduce chained-inference latency, but current enterprise adoption should depend on task evals for instruction following, function calling, language control, and reliability. Text-mode or cascaded architectures may remain the better production choice when control matters more than naturalness.

Use when:
- Choosing between cascaded STT/LLM/TTS and native speech-to-speech models.
- Evaluating whether a voice product can trade control for more natural audio interaction.

Details:
- The talk says speech-to-speech models are promising for conversational dynamics, narrative, storytelling, multilingual input, and potentially lower latency because they avoid separate transcription, text inference, and synthesis calls. 19:16-20:24, 24:03-25:01
- For most enterprise voice AI workflows that need strong instruction following and function calling, the talk says current native audio models are usually not yet the right default even though they are improving every release. 20:04-20:51
- Continuous bidirectional streaming models such as Moshi can express silence, turn-taking, and backchannels as model outputs, but the specific research model discussed is not production-ready for most real-world use cases. 17:51-19:14
- Audio mode can expand context massively relative to text and is trained on scarcer data, which can degrade reliability and cause errors such as wrong-language responses. 25:07-26:39
- The practical recommendation is to make model choice an eval threshold: swap providers or architectures in the same pipeline and run task-specific evals before choosing a production model. 20:45-20:51, 22:24-22:47, 23:12-23:28

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Choose voice-agent architecture by latency, accuracy, and semantics](choose-voice-agent-architecture-by-latency-accuracy-and-semantics.md)
- [Full-duplex speech models make turn-taking a learned behavior](full-duplex-speech-models-make-turn-taking-a-learned-behavior.md)

Sources:
- [Pipecat Cloud: Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily](../sources/20250731_IA4lZjh9sTs.md), 17:51-20:51, 22:24-23:28, 24:03-26:39
