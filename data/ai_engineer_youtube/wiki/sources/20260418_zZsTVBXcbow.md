# How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research

Source: [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](https://www.youtube.com/watch?v=zZsTVBXcbow)
Uploaded: 2026-04-18
Transcript: `raw/20260418_zZsTVBXcbow/zZsTVBXcbow.en-orig.vtt`

## Summary

Raia Hadsell frames frontier AI research beyond standard language models: omnimodal embedding models for robust retrieval and comparison, neural weather models that replace or augment physics simulation for operational forecasting, and interactive world models that generate controllable environments with memory and promptable state changes.

## Extracted Concepts

- [Use omnimodal embeddings for cross-modal retrieval and comparison](../concepts/use-omnimodal-embeddings-for-cross-modal-retrieval-and-comparison.md) - this source explains why a unified semantic vector across text, audio, video, and documents can support retrieval, querying, and agentic logic.
- [Adapt embedding dimensions with Matryoshka representation learning](../concepts/adapt-embedding-dimensions-with-matryoshka-representation-learning.md) - this source describes using one embedding network at smaller or larger dimensions depending on retrieval cost and expressiveness needs.
- [Neural weather models can target operational forecast variables directly](../concepts/neural-weather-models-can-target-operational-forecast-variables-directly.md) - this source compares GraphCast, GenCast, and FGN as neural forecasting models with different operational targets.
- [Interactive world models need memory, control, and live prompting](../concepts/interactive-world-models-need-memory-control-and-live-prompting.md) - this source describes Genie-style environments that preserve state, respond to actions, and can be changed while the user is inside them.

## Topic Links

- [Agents](../topics/agents.md)
- [Generative Media](../topics/generative-media.md)
- [Infrastructure](../topics/infrastructure.md)
- [Models](../topics/models.md)
- [Retrieval](../topics/retrieval.md)

## Notes

- Frontier AI research is framed as finding "root node" problems whose solution unlocks downstream impact, rather than optimizing only narrow leaf tasks, 03:11-04:46.
- Embedding models are presented as a companion to generative AI: sometimes the system should generate, and sometimes it should retrieve, compare, or recognize, 05:05-07:32.
- Gemini Embeddings 2 is described as a fully omnimodal model derived from Gemini that can produce one semantic vector from text, video, audio, and PDF inputs, avoiding multi-step modality fusion losses, 07:35-08:58.
- Matryoshka representation learning lets the same embedding network serve lower-dimensional retrieval first, then expand to higher-dimensional representations when more expressiveness is needed, 08:59-09:36.
- GraphCast predicts 15-day global atmospheric state with many variables using a spherical graph neural network and autoregressive prediction, 10:30-11:39.
- GenCast adds probabilistic forecasting for chaotic weather tails and is described as more accurate than 1,300 gold-standard forecasts 97% of the time while producing a 15-day forecast in eight minutes on one chip, 12:45-13:35.
- FGN directly predicts cyclone behavior rather than forecasting general weather and then applying a cyclone detector as post-processing, 13:44-14:12.
- Genie evolved from short 2D platformer worlds to 3D interactive environments, then to higher-quality worlds where users can move, return to remembered places, and prompt environmental changes live, 15:26-19:58.
