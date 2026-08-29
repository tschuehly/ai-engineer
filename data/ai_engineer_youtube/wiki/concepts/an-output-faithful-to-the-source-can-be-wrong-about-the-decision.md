# An Output Faithful to the Source Can Be Wrong About the Decision

Summary: Groundedness checks ask whether every claim in the output appears in the source. A conversation contains the options that were rejected as well as the one that was chosen, so an output can be fully grounded and still record the opposite decision — every span traces back, and the summary is a lie about intent.

Use when:
- Building or trusting a faithfulness, groundedness, or attribution check over summaries of conversations, meetings, calls, or negotiations.
- Summarizing any source that contains deliberation rather than only assertions.
- A hallucination detector reports clean and reviewers keep finding the summary wrong.
- Writing the eval criteria for note-taking, call-summary, or decision-log features.

Details:
- **The failure case.** Doctor suggests running tests; patient asks "can we just try antibiotics instead?"; they agree to hold off on the tests and treat. "Note records the opposite: arrange tests today. It kept the plan that they talked out of, not the one they chose. Every line in the note reads fine because it's not really a hallucination at all. It's not wrong. It was there in the original. But it's just not what they ended up deciding." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 04:56-05:19)
- **Why the check passes.** Stated on the judging side: a note saying "start amoxicillin" when the real decision was wait-and-see is "faithful to the words — amoxicillin did come up — but it's a lie about the intent." The retrieval-style test (does this span exist in the source?) is satisfied by every rejected option in the transcript. (10:12-10:34)
- **The neighbouring class: over-inference from an ambiguous answer.** Asked whether her headache came on suddenly or gradually, the patient says she does not know, "it just happened," and the note records "abrupt sudden onset." Fox concedes the inference is understandable — "you can see why 'it just happened' could maybe be interpreted and inferred as abrupt onset" — and then names the cost: "that's a feature that points to a bleed on the brain. She never said it. The model decided it. And now that one word drives the whole workup." Here the output is *nearly* grounded, in a paraphrase a lenient checker accepts and a clinician does not. (04:11-04:56)
- **What the correct predicate would be.** Not "is every claim supported by the transcript" but "does the output state what was decided, and does it withhold what was not." That is a claim about the conversation's outcome rather than its content, and it needs a representation of decision state that a span-matching check does not have. No source in this wiki describes building one.
- **Generalization beyond clinical notes, from the talk's own list.** "The contract review that misses the clauses that change the deal, the support agent that promises a refund you don't offer" — both are outputs whose individual statements are defensible and whose net effect misstates the position. Any transcript-to-record pipeline where the source is a negotiation has this shape: sales call summaries, meeting minutes, incident timelines, and requirements captured from a design discussion. (18:08-18:31)
- **Why this belongs on the checker's side, not only the generator's.** The generator's error is ordinary and expected; the point is that the standard control for it does not fire. A faithfulness rubric, a citation check, and a deterministic concept-overlap count all pass this note, which is one concrete mechanism behind [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md). (09:02-10:34)
- **Related but distinct from omission.** A dropped detail leaves no artifact to check at all; a reversed decision leaves an artifact that checks out. Both defeat the same class of verifier for different reasons, and a system that only hardens against one will keep shipping the other.

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Voice Agents](../topics/voice-agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [A Judge Without Taste Is a Second Silent Failure](a-judge-without-taste-is-a-second-silent-failure.md)
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)
- [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)
- [A Transcript-to-Output Check Cannot See a Mishearing](a-transcript-to-output-check-cannot-see-a-mishearing.md)
- [Full History Recalls Details That Summaries Delete](full-history-recalls-details-that-summaries-delete.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 04:11-05:19, 09:02-10:34, 18:08-18:31
