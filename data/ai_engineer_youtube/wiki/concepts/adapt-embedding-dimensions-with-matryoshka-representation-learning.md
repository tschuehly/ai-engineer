# Adapt embedding dimensions with Matryoshka representation learning

Summary: Matryoshka representation learning lets one embedding network expose useful representations at multiple dimensionalities. This supports staged retrieval: start with cheaper lower-dimensional vectors, then expand when the task needs more semantic expressiveness.

Use when:
- Retrieval cost, index size, or latency argues for a smaller embedding first pass.
- A workflow needs a path from coarse semantic search to richer comparison without swapping embedding models.

Details:
- The source describes Matryoshka representation learning as a way for the same network to represent different embedding dimensions, 08:59-09:14.
- A retrieval flow can begin with 256 dimensions, then expand the representation to gain more expressiveness when needed, 09:14-09:26.
- The point is to preserve a unified semantic space while allowing quality, cost, and expressiveness to be traded by dimension, 09:29-09:36.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Use omnimodal embeddings for cross-modal retrieval and comparison](use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md)
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)

Sources:
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md), 08:59-09:36
