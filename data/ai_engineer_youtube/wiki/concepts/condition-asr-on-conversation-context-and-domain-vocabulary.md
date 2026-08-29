# Condition ASR on Conversation Context and Domain Vocabulary

Summary: In a domain voice agent, treat speech recognition as a decoder-only audio LLM that receives the conversation so far and the domain context alongside the audio — not as a context-free audio→text function — so that entity recognition becomes a choice from a finite candidate list rather than an unbounded guess, and reserve extra scoring for the short utterances whose misreads are catastrophic.

Use when:
- A voice agent misbehaves in ways that look like reasoning failures but may actually be mishearing.
- Recognition has to be reliable on domain vocabulary (drug names, part numbers, addresses, account IDs) that generic ASR gets wrong.
- Deciding whether to buy off-the-shelf STT or build/fine-tune an audio front end for a high-stakes domain.
- Designing how much of the agent's state (task, policy, known entities) to expose to the transcription stage.

Details:
- Diagnosis first: audio benchmarks are recorded in quiet rooms while "the real world is fairly loud and noisy," and "most of what looks like model reasoning failures end up actually being model mishearing things" — the Spanish *sí* transcribed as the letter C, an Arabic drug name at >30% word error rate. Debugging a domain voice agent should therefore start at the transcript, not the prompt. (Hippocratic AI, 09:31-10:03)
- Architecture: instead of "takes in the audio and then outputs some text," the system is a decoder-only audio LLM fed three things — the audio, the conversation context so far, and the domain knowledge for that conversation. That extra conditioning is "the trick that makes this work." (10:05-10:28)
- Front end: an open-source Whisper V3 large turbo encoder fine-tuned on millions of clinical conversations, then a conformer projector that compacts audio into tokens the language model understands. The projector is chosen to preserve prosody — pauses and stresses survive — "so the model hears not just the what, but also the how." Prosody loss is a real design cost of naive audio→token projection. (10:32-11:04)
- What "context" concretely means: the medications this patient is on, the task at hand (e.g. which form is being filled), and the policy. The payoff is a search-space collapse — when a patient names a medication, "we aren't guessing from like an infinite list of medications, but we have the chance to optimize around a finite list," which drops word error rate. (11:06-11:32)
- Contextual biasing can also be trained in, not only prompted: millions of synthetic patients with addresses and phone numbers are fed through the training process, so an utterance like "1100 Boulevard" — "ripe for phonetic garbage for most ASR systems" — resolves correctly. (11:34-12:11)
- Asymmetric rescoring: in clinical calls many patient responses are single words, and single words are exactly where ASR fails destructively — "a *now* becomes a *no*, or a *five* becomes a *fine*," which "in a patient conversation is catastrophic." When the patient utters only one word, a second scoring pass runs using the full conversation as context. Spend extra compute where the cost of a misread is highest, not uniformly. (12:14-12:41)
- Reported outcome: medical word error rate down by over 50% versus standard off-the-shelf models, with P99 latency they measure as 3x faster than other systems — i.e. the conditioning was not paid for with latency. (12:41-13:01)
- **Why this stage needs its own control rather than a stronger downstream judge.** In an ambient scribe the usual quality check compares the transcript against the generated note, which treats the transcript as ground truth — so a sound-alike substitution is present in both and cannot be surfaced by that comparison at all. Fox's clinical examples of what survives such a check are single-token inversions: "Humalog heard [as] Humulin — two insulins on completely different timelines, so swapping them could crash a blood sugar. Hyperthyroidism becomes hypothyroidism, the opposite condition. Or a dropped 'no' on 'no evidence of cancer' that becomes 'evidence of cancer'." He also reports that most of the remaining error volume survives a perfect transcript, splitting into additions, changes, and omissions at the generation stage — so the two stages need separate budgets and separate controls, and this page's conditioning work is the only lever that reaches the first. See [A Transcript-to-Output Check Cannot See a Mishearing](a-transcript-to-output-check-cannot-see-a-mishearing.md). ([Fox](../sources/20260822_yqF6XhzbWBk.md), 05:19-06:28, 09:02-09:24)

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Models](../topics/models.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Benchmark Voice AI on Distant-Mic Multi-Speaker Audio, Not Headset Single-Speaker](benchmark-voice-ai-on-distant-mic-multi-speaker-audio.md)
- [Extract a Rich Structured Audio Profile in One Multimodal Call](extract-a-rich-structured-audio-profile-in-one-multimodal-call.md)
- [Filter Background Audio Before Voice-Agent Inference](filter-background-audio-before-voice-agent-inference.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)
- [A Transcript-to-Output Check Cannot See a Mishearing](a-transcript-to-output-check-cannot-see-a-mishearing.md)

Sources:
- [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../sources/20260819_AN65uc645mE.md), 09:31-13:01
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 05:19-06:28, 09:02-09:24
