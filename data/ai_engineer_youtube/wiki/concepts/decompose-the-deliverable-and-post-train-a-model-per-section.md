# Decompose the Deliverable and Post-Train a Small Model per Section

Summary: A long structured output is not one hard task; it is several narrow ones that happen to be stapled together. Split it along its own document structure and post-train a small model per part, so cost and latency track the difficulty of each section instead of the difficulty of the whole artifact.

Use when:
- One frontier-model call produces a long structured deliverable (a report, a note, a filing, a summary with fixed sections) at a volume where per-call cost matters.
- Deciding what to fine-tune first, and needing a decomposition boundary that is not arbitrary.
- Pushing back on "we need the best model for this" when only part of the output is actually hard.

Details:
- The scale that forces the question: Abridge runs its products "live in the conversation" at "the run rate of 100 million medical conversations a year," and asks "how do we do this in a way that doesn't really break the bank for us?" ([From Ambient Documentation to Clinical Intelligence](../sources/20260819_u6q-byPWUuo.md), 18:00-18:17)
- The decomposition boundary comes free from the artifact: a clinical note "has many different sections to it. There's a history of present illness, past medical history, and there's the assessment and plan," so "rather than say using a foundation model to generate all this … we can actually decompose this problem into simpler, smaller workflows." (18:17-18:41)
- The domain claim underneath it: "health care is actually many specific workflows. You don't need … [a frontier model] to actually solve all of your clinical notes. We don't need frontier level intelligence for every problem." The captioned frontier model name in this line is "Fable 5." (18:41-18:53)
- The result is per-section models: "we actually post train a lot of smaller models for different problems, such as … even to the granularity of different sections in the clinical note. And that lets us use much smaller models because it's a more specific problem and at much cheaper cost and latency." Narrowness is the thing that makes the small model viable, and the section boundary is what supplies the narrowness. (18:53-19:07)
- Relationship to routing: [routing each request to the cheapest sufficient model by difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md) varies the model across *requests* and needs a difficulty classifier that can be wrong. Section decomposition varies the model across *parts of one output* along a boundary the domain already defines, so there is no per-request classification to get wrong — at the price of an assembly step and of one fine-tuned model to maintain per section.
- Whether to build the small model at all is a separate decision: see [train your own models only where you have a right to win](train-your-own-models-only-where-you-have-a-right-to-win.md), which supplies the test Abridge applies before post-training anything.
- The general form of the narrowness argument is already in this wiki — [post-train small models for narrow capabilities](post-train-small-models-for-narrow-capabilities.md) and [domain-specific agents unlock small models and tight permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md). What this source adds is where to find the narrow tasks when the product looks like one big generation: read the structure of the deliverable.

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Train Your Own Models Only Where You Have a Right to Win](train-your-own-models-only-where-you-have-a-right-to-win.md)
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Domain-Specific Agents Unlock Small Models and Tight Permissions](domain-specific-agents-unlock-small-models-and-tight-permissions.md)
- [Gate Always-On Listening With Cheap Event Detectors](gate-always-on-listening-with-cheap-event-detectors.md)

Sources:
- [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../sources/20260819_u6q-byPWUuo.md), 18:00-19:07
