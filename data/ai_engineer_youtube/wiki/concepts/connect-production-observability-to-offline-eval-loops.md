# Connect Production Observability to Offline Eval Loops

Summary: Production traces should feed offline evals because real user behavior exposes failure modes that pre-production examples often miss.

Use when:
- Turning production agent failures into regression cases.
- Designing an eval platform that also collects observability data.

Details:
- Braintrust frames evals and observability as adjacent agent-quality problems: evals build pre-production confidence, while observability checks whether the same behavior holds under real usage, 03:33-04:20.
- The talk argues that the best way to identify agent failure modes is access to production trace data from real users, then scoring those failure modes explicitly, 14:00-14:21.
- A durable eval loop observes production behavior, analyzes traces, pulls actual examples into an offline environment, and improves the agent through offline evals for the lifetime of the production agent, 14:21-15:49.
- Online evals can point scoring functions at observability traffic and trigger alerting, while offline evals can replay production-like behavior in a safer environment, 16:20-16:48.
- Traces are useful product artifacts because they preserve input, output, metadata, and agent actions; PMs can inspect those traces, pull a traced prompt and variables into a playground, and turn observed behavior into an eval data set. 19:43-25:21
- **Evals are not the only downstream consumer.** LangChain pushes the same loop one step further: the trace corpus also feeds distillation and SFT datasets, generated environments, and human-readable reports, and the improvement loop it drives is continual learning rather than regression testing — "if you're a continual learning company, you need traces." Under that reading, connecting observability to evals is one branch of a wider claim that [observability and continual learning are the same problem](observability-and-continual-learning-are-the-same-problem.md). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 02:59-03:06, 11:08-12:46)
- **The ratchet that turns this loop into a growing regression suite at no extra cost.** Shenoy describes the offline set as accumulating out of the optimization work rather than being budgeted separately: "this allows us to hill climb and build better agents… and what's really exciting is it ratchets up. Every week our hill climbing benchmarks become a regression test." The tasks used to chase improvement this week become the tasks that must not break next week. In his setting the scoring comes free because the label is a business outcome ("did the roof get repaired?"), which is the condition that makes the ratchet cheap; where scoring is manual, the same pattern converts an improvement budget into a permanent grading bill. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 11:21-11:49)

- **A four-rung ladder from what a system cost to what its users did, built in that order and for a stated reason.** Uber's first instrumentation was "very surface-level. We used to collect cost. We used to run an NPS survey, have Google Forms being filled, Slack support. And with all of this, we saw that our quality to cost ratio was like all over the place" — a well-measured denominator against a guessed numerator. They then added classified sentiment on developer replies, then addressal rate ("when a uReview comment is made, does the developer go and actually address the comment?"), then agent trajectory for diagnosis. The sequencing is the transferable part: outcome metrics first so you know which runs are worth opening, trajectory storage second so you can find out why. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 04:48-06:35)
- **When the production loop has no user-facing channel, the only signal left is what the agent volunteers.** Figma's MCP server sees tool calls and nothing else — not the user, not the repository, not the framework its output has to fit — and the protocol features that would have asked (elicitation, sampling) were unavailable, so the team "added some optional query arguments to our tool calls… where they would send back what sort of language what sort of framework the user might be using." The stated reliability is low and the stated use is narrow: "This is imperfect uh agents lie but it was at least a signal for us to understand like oh this type of user… may not have had a good experience." Cohort comparison tolerates noise that a per-call decision would not. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 12:29-13:09)
- **Two named planes, and the reason the telemetry one has three access paths.** DoorDash splits the platform into "the telemetry layer where we have all our traces, our scores, observations" — reachable "using an MCP, using an SDK, using our APIs" — and a workflow layer "where a lot of our strat ops, our product teams operate," setting annotation tasks, reviewing golden datasets, and calibrating judges. The design point is that both planes read the same primitives: "all your API access including SDK access is basically powered by this single plane." An observability store that only an engineer's SDK can reach cannot serve the annotation half of the loop, which is where the domain knowledge enters. ([AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 06:12-06:47, 07:10-07:44)
- **The prerequisite that has to be paid before the loop exists: instrument ahead of the question.** Krieger's 2010 scaling lesson transfers directly to AI systems and is stated as a failure mode rather than a principle: "pre-measure everything that you think you might even remotely need because the worst thing is an outage where you're like, well, is this number normal or is it high? And, oh, I don't know because I don't have data until I just added this metric." A metric first recorded during an incident has no history, so it cannot support the comparison the loop depends on. He pairs it with first-class runtime control — flags, ramps, and dynamic config changeable in seconds — noting that AI systems are made of tradeoffs you will want to move without a deploy. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 07:08-07:52)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Apply online scoring to production traces with cost-aware sampling](apply-online-scoring-to-production-traces-with-cost-aware-sampling.md)
- [Replay production failures before promoting prompt fixes](replay-production-failures-before-promoting-prompt-fixes.md)
- [Label LLM Judge Outputs Before Mapping Them to Scores](label-llm-judge-outputs-before-mapping-them-to-scores.md)
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)
- [Measure a Review Bot by Whether the Comment Changed the Code](measure-a-review-bot-by-whether-the-comment-changed-the-code.md)
- [Optional Self-Reported Tool Arguments Are Segmentation Signal, Not Ground Truth](optional-self-reported-tool-arguments-are-segmentation-signal.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Pre-Measure Everything and Build Runtime Knobs Before You Need Them](pre-measure-everything-and-build-runtime-knobs-before-you-need-them.md)

Sources:
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md), 03:33-04:20, 14:00-16:48
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md), 19:43-25:21
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 02:59-03:06, 11:08-12:46
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 11:21-11:49
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 04:48-06:35
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 12:29-13:09
- [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](../sources/20260828_bMjlRrWjdT0.md), 06:12-06:47, 07:10-07:44
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 06:45-08:18
