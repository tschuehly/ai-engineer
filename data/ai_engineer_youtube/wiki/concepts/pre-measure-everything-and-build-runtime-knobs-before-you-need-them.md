# Pre-Measure Everything and Build Runtime Knobs Before You Need Them

Summary: Two pieces of 2010 scaling advice transfer directly to AI systems. Instrument anything you might remotely need *before* an incident, because a metric added during the incident has no baseline and cannot tell you whether the number is normal. And build first-class runtime control — feature flags, ramps, and dynamic config changeable in seconds — because AI systems are made of tradeoffs you will want to move without a deploy.

Use when:
- Standing up a new inference path, gateway, agent surface, or model rollout.
- Deciding whether a metric is worth adding before you have a question that needs it.
- Post-incident, when the honest answer to "was that normal?" was "we don't know."

Details:
- The measurement rule and its exact failure mode: "pre-measure everything that you think you might even remotely need because the worst thing is an outage where you're like, well, is this number normal or is it high? And, oh, I don't know because I don't have data until I just added this metric." The loss is not the missing number, it is the missing *history* — a metric first recorded during an incident is uninterpretable for the duration of that incident. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 07:08-07:26)
- The knobs rule: "being really thoughtful about knobs and feature flags," including ramps and rollouts, plus dynamic config "where a lot of our runtime configurations had to be changed in a matter of seconds so that we could handle load and being able to do that in a first class way was really important." The emphasis is on *first class* — control built as a product surface, not as an emergency patch path. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 07:26-07:44)
- The transfer is stated explicitly rather than inferred: "I'm seeing that definitely in AI as well where we're making all sorts of different trade-offs and having that kind of runtime configuration is super key." AI systems have more knobs than web backends did — model choice, reasoning level, retrieval depth, guardrail placement, context budgets — and most of them are exactly the settings you want to change under degradation. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 07:46-07:52)
- Both lessons came from an outage, not from planning: Instagram melted in its launch week and the advice arrived at an unrelated investor infrastructure lunch the same week. The generalizable part is that the instrumentation you wish you had is always identified retrospectively, which is the argument for over-instrumenting prospectively. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 06:45-07:08)
- Limits: an anecdote from 2010 restated for AI with no AI-specific example, no cost accounting for over-instrumentation (cardinality, storage, alert noise), and no guidance on which of the many AI knobs are worth making dynamic. The interviewer's framing that a product ships as "one app with 3,000 flags" is offered as a tension and not resolved. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 08:13-08:18)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Connect Production Observability to Offline Eval Loops](connect-production-observability-to-offline-eval-loops.md)
- [Expose Observability As Agent-Readable Feedback](expose-observability-as-agent-readable-feedback.md)
- [Draw the Cut Line Between Verified Data and Free-Form Agent Analysis](draw-the-cut-line-between-verified-data-and-free-form-agent-analysis.md)
- [Validate a Cross-Language Port Against Production Runtime Data](validate-a-cross-language-port-against-production-runtime-data.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 06:45-08:18
