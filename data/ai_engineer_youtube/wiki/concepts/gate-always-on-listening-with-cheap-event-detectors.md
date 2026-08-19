# Gate Always-On Listening With Cheap Event Detectors

Summary: A system that listens through an entire session cannot poll a large model on a timer — the cost scales with session length rather than with the events you care about. Run cheap, fast gates over the stream to find the moments worth acting on, and hand only those moments to the heavy model that does the real matching.

Use when:
- An ambient or realtime agent watches a long conversation, meeting, or event stream for occasional actionable moments.
- Per-call cost is fine but per-session cost is not, because the naive design calls the model every few seconds.
- Designing an action-extraction feature where saying the thing is only half the job and resolving it against a system of record is the other half.

Details:
- The feature: clinicians "aren't big fans of pending orders, but often they'll mention orders during the visit itself, medication or non-medication orders. So … while we're listening in the visit, as the clinician says [an] order, we actually queue it up in the background and let them actually sign it off in the EHR." ([From Ambient Documentation to Clinical Intelligence](../sources/20260819_u6q-byPWUuo.md), 19:49-20:11)
- The naive design and why it fails: "if we did this in a very naive way, like every few seconds are just listening for orders, that would really break the bank" — at a run rate near 100 million medical conversations a year, a per-interval poll multiplies model calls by session duration. (20:11-20:17)
- The gate layer: "a lot of our tricks are like, how do we find the right events in the conversation to actually trigger heavier models… we have a number of different gates that are cheaper and faster that let us trigger actually larger models and hand off to them for actually doing the end-to-end work." Note the plural — it is a chain of progressively more expensive checks, not one detector. (20:17-20:45)
- Why the heavy model is still needed after the gate fires: the work is not detection but resolution — "you need to match the order, not just is the order said, but does it match and references orders that are approved by the system and are relevant to the conversation." Grounding a spoken phrase in an approved order catalogue is the expensive part, and it runs only on gated moments. (20:26-20:38)
- Latency is a co-constraint, not just cost: because the system is live in the conversation, "you can't act on information too late and you have to act at the right time for it to be useful," so the gate has to be fast enough to keep the heavy call inside the useful window. (12:07-12:20)
- Contrast with the wiki's other cheap-first patterns. [Route each request to the cheapest sufficient model by difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md) assumes a request already exists and picks a tier for it; the question here is *whether there is a request at all*. [Run parallel specialist models behind a speak-up gate](run-parallel-specialist-models-with-a-speak-up-gate.md) is the closest sibling — a cheap "do I need to say something?" check in front of every specialist — but it fires per conversational turn in a system that must reply, whereas this fires on a continuous stream in which most of the audio warrants no action at all.
- The failure mode implied by the design is a missed trigger: an order spoken in a form the cheap gate does not catch never reaches the model that could have matched it, and the talk describes no recall measurement for the gates. The product hedge is that the clinician still signs orders off in the EHR, so a miss degrades to the pre-existing manual path rather than to a wrong order.

Related topics:
- [Inference](../topics/inference.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Run Parallel Specialist Models Behind a Speak-Up Gate](run-parallel-specialist-models-with-a-speak-up-gate.md)
- [Decompose the Deliverable and Post-Train a Small Model per Section](decompose-the-deliverable-and-post-train-a-model-per-section.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../sources/20260819_u6q-byPWUuo.md), 12:07-12:20, 19:49-20:45
