# Use Loss Curves to Debug Local Model Training

Summary: Local model-training runs should be judged by train and validation loss behavior before trusting generated samples. Non-decreasing train loss, diverging validation loss, and unstable spikes point to different failure modes.

Use when:
- Diagnosing whether a small training run is learning, overfitting, or unstable.
- Setting lightweight validation expectations for a model-training workshop or prototype.

Details:
- After running training, inspect whether losses decreased over the run rather than relying only on a final generated sample (59:31-59:43).
- If train loss is not decreasing, the model is probably not learning or the setup has a training problem; if train loss decreases but validation loss does not, the run is likely overfitting (59:42-60:03).
- Loss should usually be smooth; strange spikes suggest a data issue or a training-loop issue that needs investigation (60:03-60:12).

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Local LLM training exposes the core model-building stack](local-llm-training-exposes-the-core-model-building-stack.md)

Sources:
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md), 59:31-60:12
