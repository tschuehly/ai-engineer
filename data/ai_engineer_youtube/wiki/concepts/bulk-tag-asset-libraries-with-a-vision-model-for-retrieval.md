# Bulk-Tag an Asset Library With a Vision Model Over Rendered Views

Summary: A library of non-textual assets — 3D models, textures, icons, CAD parts — is usually unsearchable because its only metadata is filenames. Rendering each asset to an image and running a vision model over the render manufactures the missing descriptions in bulk, which is what lets an agent or a user find assets by describing them instead of knowing what they are called.

Use when:
- An agent needs to select from a large in-house catalog whose items have no usable descriptions.
- The items are not text but can be rendered, screenshotted, photographed, or otherwise made visible.
- Manual tagging is the obvious answer and the catalog is one or two orders of magnitude too large for it.

Details:
- The constraint is stated plainly: "I've used also vision models mostly to tag the assets that we have because it's like six or 7,000 assets. I could not manually tag them all and explain like, 'Oh, this is an astronaut and this is a knight and this is a castle.' I just have the names and the 3D file. So, I took a screenshot and ran a vision model to describe those" (14:04-14:47).
- The step that makes it work is the intermediate render. A 3D asset is not something a captioner can read, but a screenshot of it is; the render converts an unindexable format into the one modality with a mature off-the-shelf describer. The same move applies to any asset that has a canonical view.
- The output is used as a retrieval index, not as display metadata. In the demo, asking for a robot surfaces assets that are "tagged as robot or the description are… a robot" (00:53-01:15), and the same natural-language matching is what returns futuristic buildings, a warehouse, or a castle for "buildings" (02:14-02:31).
- The generated descriptions and the intent tags the agent manipulates at runtime are different layers of the same tag system: the vision pass answers *what an asset is*, while the agent-attached tags answer *what role it plays in this game* (see [Make Agent Edits Declarative Tags Instead of Generated Code](make-agent-edits-declarative-tags-instead-of-generated-code.md)). Separating them means the expensive vision pass runs once per library item, offline, and never on the interaction path.
- This is a cheap-model-manufactures-metadata pattern rather than a runtime vision system: the vision model is used once per asset offline, and the live assistant is "mostly an LLM" (14:43-14:47).
- Caveats the source does not address: no accuracy check on the generated descriptions, no handling of assets whose single canonical view is misleading (interiors, symmetric or thin geometry), and no statement of which vision model was used. A wrong description here is silent — it removes an asset from reach rather than producing a visible error.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Vision AI](../topics/vision-ai.md)

Related concepts:
- [Design AI creative systems for generated-asset retrieval](design-ai-creative-systems-for-generated-asset-retrieval.md)
- [Use Sparse Autoencoder Features as an Unsupervised Data Tagger](use-sparse-autoencoder-features-as-an-unsupervised-data-tagger.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Make Agent Edits Declarative Tags Instead of Generated Code](make-agent-edits-declarative-tags-instead-of-generated-code.md)

Sources:
- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md), 00:53-02:31, 14:04-14:47
