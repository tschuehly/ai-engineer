# Use omnimodal embeddings for cross-modal retrieval and comparison

Summary: Omnimodal embeddings let one semantic representation cover text, audio, video, and document inputs. Use them when retrieval, recognition, comparison, or agent context needs to preserve information across modalities instead of stitching separate modality pipelines together.

Use when:
- A retrieval system must match concepts across text, audio, video, images, or PDFs.
- An agent needs compact semantic context for querying or comparison rather than generated text.

Details:
- Hadsell frames embedding models as a critical companion to generative AI because systems sometimes need to retrieve, recognize, or compare rather than generate, 05:05-07:32.
- The talk uses the "Jennifer Aniston cell" analogy: robust concept recognition should activate for the same entity across name, picture, video, or voice, 05:25-06:41.
- Gemini Embeddings 2 is described as fully omnimodal and derived from Gemini, producing unified semantic vectors over text, video, audio, and PDF input rather than losing information in modality-fusion steps, 07:35-08:47.
- The resulting vector can support retrieval, querying, agentic logic, and related workflows, 08:47-08:58.

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Use small models as context-management tools before agent reasoning](use-small-models-as-context-management-tools-before-agent-reasoning.md)
- [Tune multimodal token budgets by visual or audio task](tune-multimodal-token-budgets-by-visual-or-audio-task.md)

Sources:
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md), 05:05-08:58
