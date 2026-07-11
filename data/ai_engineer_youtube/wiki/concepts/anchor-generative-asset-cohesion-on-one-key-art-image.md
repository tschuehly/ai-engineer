# Anchor Generative Asset Cohesion on One Key-Art Image

Summary: Iterate to a single "key-art" image you like, then feed that one image back as the anchor for further generation. It carries enough information to hold the art style *and* imply the gameplay, giving the model cohesion across a session so generated assets feel like they live in one universe instead of a bag of mismatched prompt outputs.

Use when:
- Generating many assets (or a whole game/product) and the biggest quality gap is cohesion — assets that don't feel like one entity or one universe.
- You want a cheap, simple starting point that steers subsequent generations without writing a long style spec each time.
- The model tends to drift in style or theme across separate prompts within the same project.

Details:
- Workflow (from Meta art director Dale): during the iteration stage you land on a concept you really like, then use that single key-art image (his example: a "lovely bear") as the anchor for the models — "just like game development." (06:10-06:45)
- The one image does double duty: it anchors the *art style* you then filter down into individual assets, and it also anchors what the *gameplay* could be — "it actually holds a lot of information and it's a very simple way to get started." (06:45-07:13)
- The point of anchoring is cohesion: it lets the LLM stay coherent throughout the session rather than producing independent, inconsistent outputs per prompt. (07:17-07:19)
- This is what shortens the distance between a "your-kid-can-prompt-it" game and a professionally made one — cohesion between UI, story, and art so the game feels like one universe. (05:44-06:05, 07:28-07:42)

Related topics:
- [Generative Media](../topics/generative-media.md)

Related concepts:
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)
- [Design AI creative systems for generated-asset retrieval](design-ai-creative-systems-for-generated-asset-retrieval.md)

Sources:
- [Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta](../sources/20260708_grdoOC1BT1s.md), 05:44-07:42
