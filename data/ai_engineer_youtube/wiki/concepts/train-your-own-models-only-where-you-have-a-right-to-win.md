# Train Your Own Models Only Where You Have a Right to Win

Summary: Two different situations justify post-training your own model, and they need different arguments. Where quality is already saturated, you train to cut cost and latency and the frontier's progress is irrelevant. Where quality is not saturated, training only makes sense if you can beat the frontier's *rate of change* — which requires data the labs do not have and a problem they are not focused on.

Use when:
- Someone objects that "the frontier model will just steamroll you" on a fine-tuning plan.
- Choosing which parts of a product to post-train and which to leave on a hosted frontier model.
- Assessing whether a proprietary dataset is actually a defensible asset or just a large one.

Details:
- The asset: "we have this unique data set of a hundred million medical conversations a year. And as far as we know, no one else has such a large data set. So our key insight is having a right to win in training models." ([From Ambient Documentation to Clinical Intelligence](../sources/20260819_u6q-byPWUuo.md), 19:08-19:19)
- Regime one — saturated quality: "there [are] problems where the quality is already maxed out. And so you should train models then to reduce [cost] and latency." Here training is a pure efficiency play and carries no bet about future frontier releases. (19:19-19:25; the caption reads "reduce quality and latency," but the surrounding argument is about cost, since this regime is defined by quality already being maxed out.)
- Regime two — unsaturated quality, where the objection lives: "there are other problems where the quality isn't maxed out and people say, 'Oh, the frontier model would just steamroll you.' Our key insight is we can actually potentially beat the rate of change on the frontier model if we have the right to win by having the right data that they may not have and the focus on a problem that they may not be focusing on. And that lets us still maximize quality." (19:25-19:48)
- The framing worth stealing is *rate of change*, not level. The question is not whether your model is better than the current frontier model today; it is whether your improvement curve on this narrow problem outruns the frontier's general one — which is why both conditions are required. Unique data without narrow focus loses to a lab that eventually cares; narrow focus without unique data loses to the next release.
- Where the data comes from matters for durability. Abridge's corpus is a byproduct of a deployed product at scale, so it renews at ~100M conversations a year rather than being a fixed dump; the complementary case in this wiki is [high-value vertical data withheld by design](high-value-vertical-data-is-withheld-by-design.md), where the corpus is defensible because publishing it would destroy its value. Both produce the same structural result — the frontier labs cannot train on it — through different mechanisms.
- The decision this gates in practice is section-level: see [decompose the deliverable and post-train a small model per section](decompose-the-deliverable-and-post-train-a-model-per-section.md) for how Abridge cashes the right to win into cheaper per-part models.
- Caveat the source does not resolve: it reports no measurement of how the two curves actually compare. The claim is an insight and a bet ("potentially beat the rate of change"), not a demonstrated result, and nothing in the talk describes the trigger for abandoning a post-trained model when a frontier release closes the gap.

Related topics:
- [Models](../topics/models.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Decompose the Deliverable and Post-Train a Small Model per Section](decompose-the-deliverable-and-post-train-a-model-per-section.md)
- [High-Value Vertical Data Is Withheld by Design](high-value-vertical-data-is-withheld-by-design.md)
- [Post-Train Small Models for Narrow Capabilities](post-train-small-models-for-narrow-capabilities.md)
- [Specialize Models Against Private Benchmarks With RL](specialize-models-against-private-benchmarks-with-rl.md)
- [Last-Mile Domain Context Beats Model Chasing](last-mile-domain-context-beats-model-chasing.md)

Sources:
- [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](../sources/20260819_u6q-byPWUuo.md), 19:08-19:48
