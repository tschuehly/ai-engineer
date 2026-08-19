# Run Parallel Specialist Models Behind a Speak-Up Gate

Summary: When one model is an unacceptable single point of failure but routing latency is unaffordable, run every specialist concurrently on each turn and make each one's first job a cheap "do I have anything to say here?" check that short-circuits — the always-on ensemble costs roughly the price of the few specialists that actually fire, and background verifiers catch what the synchronous path cannot.

Use when:
- A conversational or realtime agent needs many domain capabilities but cannot afford a router hop or sequential handoffs.
- A single model's failure would be unacceptable, so you want redundancy without a latency penalty.
- Deciding between routing to one specialist, chaining handoffs, and running specialists in parallel.
- Deciding which correctness checks must block a response and which can run after it.

Details:
- Shape: one central model holds the conversation while ~30 specialists (labs, medications, scheduling) feed input into it — 31 models live "at any given point of time for every conversation." The specialists do not take over the conversation; they hand context to the model that owns the thread, which "will take this input from the specialist and steer the conversation as appropriate." (Hippocratic AI, 08:29-08:46, 13:50-14:15)
- Why not one model: "we see a singular model being as like one point of failure, and that's just unacceptable for a patient conversation." The constellation is bought for redundancy and safety, and it is invisible to the user — "the patient never can tell the difference." (09:06-09:22)
- The latency trick is counterintuitive: rather than routing to the right specialist, *all* of them run in parallel and "every single model does a really quick check to see if they even need to say something." Each specialist first decides "do I need to speak?" and short-circuits if not, which is what keeps the ensemble inside the latency budget. Cost scales with the specialists that fire, not the specialists that exist. (13:07-13:38)
- Split the checks by whether they can block: the speak-up ensemble is the synchronous half; asynchronous models run verification in the background. Tool calls "have innumerable failure modes," so background verifiers check both the parameters going into a tool call and the responses coming back — credited with the system's high scheduling accuracy. (13:38-13:50, 14:18-14:41)
- Push verification offline whenever the action is reversible in time: for scheduling, "sometimes we have the luxury of time to go back and check" whether an appointment was wrong and then course-correct on the back end or call the patient back and apologize. Reversibility, not confidence, decides whether a check must be in the critical path. (14:43-14:57)
- The same parallel-specialist pattern appears at the edges of the pipeline: the hearing stage is itself "a collection of models" for bilingual switching, background-noise detection, and contextual understanding, and the output stage combines personality/voice, HD audio quality, and a clinical documentation engine. (08:13-09:03)
- Contrast with the more common shape in this wiki, where a slim conversational agent *delegates* to specialists through tools or handoffs: that saves tokens and tool-schema bloat but pays a serialization cost. The constellation instead pays a small always-on gate cost per specialist to avoid ever waiting for a routing decision.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Agents](../topics/agents.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Delegate complex voice-agent tasks through specialist tools and handoffs](delegate-complex-voice-agent-tasks-through-specialist-tools-and-handoffs.md)
- [The Fat-Agent tool overload collapses accuracy and inflates latency](fat-agent-tool-overload-collapses-accuracy-and-latency.md)
- [Use hierarchical verification before trusting weak agent feedback](use-hierarchical-verification-before-trusting-weak-agent-feedback.md)
- [Condition ASR on Conversation Context and Domain Vocabulary](condition-asr-on-conversation-context-and-domain-vocabulary.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)

Sources:
- [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](../sources/20260819_AN65uc645mE.md), 08:13-14:57
