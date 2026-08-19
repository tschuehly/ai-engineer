# Scope the Assistant to Getting the User Unstuck, Not One-Shotting the Artifact

Summary: An assistant inside a creative tool can be aimed at removing the specific blocker in front of the user rather than at producing the finished artifact. Arturo Nunez takes that position deliberately for a game-making tool, and the design consequence is that the user stays the author, keeps the process, and acquires the domain's vocabulary as a side effect — the opposite outcome from a one-shot generator, which produces an artifact and leaves the user knowing nothing.

Use when:
- Deciding whether an AI feature in a creative or authoring product should complete the work or unblock the worker.
- The product's value is in the user's engagement with the process, not only in the output.
- Arguing about how much of a workflow an agent should absorb when the users are amateurs rather than professionals.

Details:
- The scope statement is explicit: the assistant "essentially helps you get unstuck. Like if I don't know how to make the car move, I just ask it and it knows, understands what are the tools available, what are the tags available, and then it applies them to the asset that I'm talking about" (10:37-10:53). It resolves one stuck step using the platform's own vocabulary; it does not take over authorship.
- The refusal is stated as a product decision rather than a capability limit, and it concedes the other market exists: "I don't want us to one-shot games that nobody is going to play and I don't see the point in that. There's in the industry, of course, the need for games that are one-shotted, but here the idea is that we allow people to make games and experience that and have fun and share those games with their families and friends" (16:33-17:12).
- The justification is that the process is the product. His stated goal is "enjoying the process rather than the end product," aimed at people for whom making games is "just a creative outlet" and not a two-to-three-year commercial release into a crowded market (05:00-05:32).
- The learning outcome is domain literacy, not programming literacy: the hope is "that they learn along the way the language of making games, the language of game design, not necessarily the coding or programming." Users report picking up programming concepts anyway, "but that was not the initial goal" (17:11-17:33). This is the user-side mirror of exposing the domain's vocabulary rather than the platform's — the vocabulary the assistant speaks is the vocabulary the user ends up learning.
- The scoping decision constrains the interaction shape upstream. Because the assistant only has to unstick a step, it can operate on a small closed action space and a context window graded around what the user is currently touching, instead of needing a whole-project plan.
- Contrast with the wiki's one-shot position: prompt-to-app builders are valuable precisely because a disposable artifact is fast to judge and throw away ([use one-shot app builders for product ideation](use-one-shot-app-builders-for-product-ideation.md)). Both positions are coherent; the discriminator is whether the artifact or the user's engagement is the thing being produced.
- Caveat: this is the builder's stated intent for a closed-alpha product (13:50-14:04), with no retention, completion, or learning data behind it. The claim that unblocking rather than generating teaches the user is asserted from anecdote.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Expose the Domain's Vocabulary to Agents, Not the Platform's Primitives](expose-domain-vocabulary-to-agents-not-platform-primitives.md)
- [Use One-Shot App Builders for Product Ideation](use-one-shot-app-builders-for-product-ideation.md)
- [Choose autonomy level by task uncertainty and control needs](choose-autonomy-level-by-task-uncertainty-and-control-needs.md)
- [Start with augmentation when autonomous reliability is not ready](start-with-augmentation-when-autonomous-reliability-is-not-ready.md)

Sources:
- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md), 05:00-05:32, 10:37-10:53, 16:33-17:33
