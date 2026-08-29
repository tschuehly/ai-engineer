# A Transcript-to-Output Check Cannot See a Mishearing

Summary: In a capture pipeline that transcribes and then generates, errors are produced at two stages with different remedies — and the usual verifier, which compares the transcript against the generated output, treats the transcript as ground truth. A sound-alike misrecognition is therefore invisible to it: the output is perfectly faithful to a source that is already wrong.

Use when:
- Designing quality controls for ambient scribes, call summarizers, meeting notes, or any speech-to-text-to-LLM chain.
- Attributing an observed error to the model when it may have originated in recognition.
- Deciding where to spend a fixed error budget across ASR accuracy and generation quality.
- Reviewing an eval plan whose only reference is the transcript.

Details:
- **The two-stage split, named.** "In ambient scribes, there's first transcription and then generation. A lot of it does happen on the transcription layer." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 05:19-05:42)
- **Stage-one errors are sound-alikes with clinical consequence, not noise.** "Humalog heard [as] Humulin — two insulins on completely different timelines, so swapping them could crash a blood sugar. Hyperthyroidism becomes hypothyroidism, the opposite condition. Or a dropped 'no' on 'no evidence of cancer' that becomes 'evidence of cancer'." Each is a single-token substitution that inverts or relocates the meaning, and none of them looks anomalous downstream. (05:42-06:05)
- **Stage-two errors are a closed set of three.** "Most of what goes wrong is actually even with a perfect transcript. It's the model reading the words correctly and still doing one of three things: either it adds something that was never said, it changes something that was, or it omits something that should be there." Fox's own focus is here, on the explicit grounds that the transcription problems are "really hard problems, and they are common" but not where the volume is. (06:05-06:28)
- **The structural consequence, which the source does not state.** The judge Fox describes takes "the transcript and the note and context" as its inputs (09:02-09:24). A stage-one error is present in both, so no comparison between them can surface it — the check is measuring faithfulness to a corrupted reference. This inference follows from the described architecture rather than from a claim in the talk, and it means an error budget split by stage needs a *separate* control for stage one, not a stronger note-level judge.
- **What that separate control looks like.** The wiki's ASR page is the other half of this: condition recognition on the conversation so far and the domain vocabulary so that entity recognition becomes a choice from a finite candidate list, and rescore the short utterances whose misreads are catastrophic. That work reports medical word error rate down by over 50% versus off-the-shelf models — a stage-one intervention with no equivalent at the note level. See [Condition ASR on Conversation Context and Domain Vocabulary](condition-asr-on-conversation-context-and-domain-vocabulary.md).
- **Diagnostic habit this implies.** When an output is wrong in a way that looks like a reasoning failure, read the transcript before reading the prompt. Hippocratic AI states the general form from the voice side — "most of what looks like model reasoning failures end up actually being model mishearing things" — and Fox's catalogue is the complementary finding that the majority of what remains is genuine generation error. The two together give a rough triage order rather than a measured split; neither source reports a stage-by-stage error breakdown.
- **Where this generalizes.** Any pipeline with an unverified intermediate representation has the same hole: OCR before extraction, retrieval before synthesis, a summary before a decision. The rule is that a verifier anchored on an intermediate artifact can only score the stages after it.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Condition ASR on Conversation Context and Domain Vocabulary](condition-asr-on-conversation-context-and-domain-vocabulary.md)
- [An Output Faithful to the Source Can Be Wrong About the Decision](an-output-faithful-to-the-source-can-be-wrong-about-the-decision.md)
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)
- [Evaluate Voice Agents With Traces, Transcripts, Audio Checks, and Simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [An Oracle Ceiling Separates Retrieval Failure From Use Failure](an-oracle-ceiling-separates-retrieval-failure-from-use-failure.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 05:19-06:28, 09:02-09:24
