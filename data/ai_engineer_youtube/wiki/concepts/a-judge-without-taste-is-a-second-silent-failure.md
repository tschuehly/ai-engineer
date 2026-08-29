# A Judge Without Taste Is a Second Silent Failure

Summary: A checker placed after a generator only adds safety if it fails differently from the generator. When both share the same blind spot — neither can tell which of the true things on the page mattered — the judge's pass is not a second opinion but a second confident wrong answer, and the system now reports clean where it used to report nothing.

Use when:
- Adding an LLM judge, critic, or verification pass in front of a human review queue or an auto-approve path.
- A judge's pass rate is high, its flags look sensible, and nobody has audited what it let through.
- Deciding whether a passing eval score licenses removing a human from the loop.
- Reviewing a proposal to gate output on "the model checks its own work."

Details:
- **The measured result.** Fox built the strongest judge he had seen in production teams — transcript, note, and context in front of a frontier model, "a detailed rubric for faithfulness with worked pass and fail examples," the rubric "maybe auto-optimized with GEPA," plus "some deterministic NLP to count up medical concepts that are differing between the two" — ran his error dataset through it, and it "scored most of them fine. It flagged a handful of them and signed off the rest. But one in five of those clean passes still had some sort of serious error buried in it. And often that was an omission." ([Fox](../sources/20260822_yqF6XhzbWBk.md), 09:02-10:12)
- **The diagnosis is capability-independent.** "It's not stupid. It's a frontier model, serious engineering behind it, more than clever enough to read the whole encounter and catch every obvious error. And it's not blind, either… it just can't tell what counts." A judge can see every difference and still rank them wrongly, which is why scaling the judge's model does not close this gap. (10:12-10:54)
- **The framing worth carrying.** "You put a judge like that in front of your system, you've not added a safety net, you've added a second silent failure that just nods along with the first." The failure is silent in a specific sense: it produces an artifact — a pass — where previously there was no claim at all, so downstream consumers get more confidence for the same underlying risk. (10:54-11:20)
- **What makes the judge correlated with the generator rather than independent.** Both are asked to weigh the same facts against an unstated standard of what matters here. Fox's illustration: a note saying "start amoxicillin" when the decision was wait-and-see is "faithful to the words, amoxicillin did come up, but it's a lie about the intent. A good judge might catch that, might. But whether it flags that versus the other things that it could comment on depends on it knowing what decision matters most." (10:12-10:34, and see [An Output Faithful to the Source Can Be Wrong About the Decision](an-output-faithful-to-the-source-can-be-wrong-about-the-decision.md))
- **The comparison Fox reports, with its limits stated.** Three judging systems over the same generated notes: a strong off-the-shelf rubric judge on a frontier model is "better than a coin flip, but it misses most of what matters"; the serious rubric-plus-deterministic-checks system is "better again, but still missing quite a lot of what counts"; the judge assembling a per-case standard is "performing a lot better on this specific data set. Same notes. The only thing that changes is what the judge was shown." No absolute figures, denominators, or ground-truth procedure are given, and the winning arm is the speaker's own product — treat the ordering as a claim, not a benchmark. (17:02-17:46)
- **Why the first two lose, in his account:** "they guess the criteria, they freeze one standard, and they go stale." Each is a failure of the standard rather than of the judge's reasoning, which is what points the remedy at [where the standard is kept](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md) rather than at the model. (17:46-18:08)
- **Relation to the wiki's judge-verification discipline.** [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md) covers the judge that *over*-calls — a score drops and the agent gets blamed for a measurement artifact. This is the opposite and quieter half: the judge under-calls, nothing moves on any dashboard, and no trigger fires at all. The detection method differs accordingly. Over-calling is found by reading the traces a judge flagged; under-calling is only found by expert-reviewing a sample of what it *passed*, which no score movement will ever prompt you to do.
- **Operational rule this suggests.** Sample the pass set, not just the flag set, and staff it with the domain expert rather than the engineer. Fox's entire error catalogue came out of notes that shipped and, in one in five cases, out of notes a serious judge had explicitly cleared. (09:24-10:12)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Verification Is Cheap for Detection and Expensive for Materiality](verification-is-cheap-for-detection-and-expensive-for-materiality.md)
- [Check Whether the Judge Is Right Before Changing the Agent](check-the-judge-before-changing-the-agent.md)
- [Keep a Moving Standard in Examples, Not in a Rubric or the Weights](keep-a-moving-standard-in-examples-not-in-a-rubric-or-the-weights.md)
- [Calibrate LLM Judges Like Binary Classifiers](calibrate-llm-judges-like-binary-classifiers.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [An Error Rate With No Incident Reports Is a Measurement Gap](an-error-rate-with-no-incident-reports-is-a-measurement-gap.md)

Sources:
- [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](../sources/20260822_yqF6XhzbWBk.md), 09:02-11:20, 17:02-18:08
