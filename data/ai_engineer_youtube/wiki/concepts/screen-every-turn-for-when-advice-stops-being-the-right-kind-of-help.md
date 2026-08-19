# Screen Every Turn for When Advice Stops Being the Right Kind of Help

Summary: The dangerous case in an advice product is not a wrong answer to the question asked — it is a competent answer to a question that should no longer be answered at all. Run a background screen before every sensitive reply, looking for the patterns a domain specialist is trained to hear rather than for what the user asked, and when they appear, switch the agent out of its normal mode into expert-authored protocols.

Use when:
- Building coaching, advice, or support agents in a domain where a subset of users are in danger rather than in difficulty.
- The risk signal is something the user never states — no keyword, no explicit request, just a pattern across how they describe their situation.
- Deciding what "safety" means for an agent whose ordinary output is already helpful and non-toxic.
- Writing escalation policy and someone proposes adopting a generic safety policy or a platform's default refusal behavior.

Details:
- **The failure has a precise shape: the wrong category of help, delivered well.** "A general-purpose AI doesn't know what a domestic violence specialist catches in the first 90 seconds, the difference between we fight a lot and I'm afraid of what happens when I disagree with him. It doesn't know that I just have to stay calm is sometimes the exact sentence someone is taught to say right before something terrible happens. It doesn't know when relationship advice has stopped being the right category of help." Notice that a keyword filter fails on all three: the sentences are ordinary, and the second is a *reassurance*. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 09:32-10:13)
- **The domain's risk ceiling is higher than it looks from the product surface.** "Relationship coaching sits closer to suicide risk and yes, homicide risk than almost any other corner of mental health," and "every licensed clinician is trained for that moment. Relationship AI products are not built for that moment." This is the argument for why a warm, competent coaching product needs a safety layer at all — the risk arrives through the same conversation as the ordinary use case. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 10:13-10:34)
- **The mechanism: screen quietly, before the reply, on every sensitive message.** "Before she ever responds to a sensitive message, she's screening it quietly in the background for the patterns clinicians are trained to recognize. Escalating control, fear-based language, anything pointing toward risk to the user or someone else. When those patterns show up, Maxine stops coaching and starts following the protocols." Two design choices are load-bearing: the screen runs *before* the coaching response exists, and the outcome is a mode change rather than a refusal — the agent keeps talking, under different rules. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 12:17-12:41)
- **Who writes the protocols is part of the design.** They were "built out of 30 years of clinical practice, not a generic safety policy written by someone who's never sat in the room." A generic policy can enumerate prohibited content; only a practitioner can specify what to do with someone who has just described a controlling partner and asked how to keep the peace. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 12:41-12:47)
- **The capability is stated as symmetric with the primary one.** "Knowing when not to coach is just as important as to know how," and "a relationship AI that can't tell the difference between we're struggling and I'm not safe isn't incomplete, it's dangerous at scale." The scale qualifier is the point: the same screen missing on 900 million weekly sessions is a different object than a single clinician missing it once. ([Clay Cockrell](../sources/20260819_yoONZwV2smc.md), 12:47-13:00)
- **How this differs from the deterministic pre-model layer.** Hinge Health routes self-harm and acute-emergency turns in *code* above the model, on the argument that "the model should not even see this turn." That works because those turns announce themselves — a stated intent, a named emergency, an identity check. Here the trigger is inferential: it is a clinical read of language that never names the risk, so the screen has to be a model-class classifier with expert-defined pattern categories, and it is a mode router rather than a hard interception. The two are complementary layers, not alternatives — the deterministic layer catches the explicit disclosure, the screen catches the one the user does not know they made. The cost of the inferential version is the one the source does not report: neither its false-negative rate nor its false-positive burden on ordinary coaching turns is described, and both matter, since over-triggering turns a coaching product into a referral service.

Related topics:
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Run Must-Not-Fail Decisions in a Code Layer Above the Model](run-must-not-fail-decisions-in-code-above-the-model.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)
- [Fine-Tuned Encoder Discriminators Make Low-Latency Guardrails Practical](fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md)
- [Optimize Prompts Against an Asymmetric Cost Matrix, Not Flat Accuracy](optimize-prompts-against-an-asymmetric-cost-matrix.md)
- [Agreeableness Is a Failure Mode When the Product's Job Is to Change the User](agreeableness-is-a-failure-mode-when-the-job-is-to-change-the-user.md)

Sources:
- [AI is the World's largest Relationship Therapist — Clay Cockrell & Tony Fabrikant, CoupleWork AI](../sources/20260819_yoONZwV2smc.md), 09:32-10:34, 12:17-13:00
