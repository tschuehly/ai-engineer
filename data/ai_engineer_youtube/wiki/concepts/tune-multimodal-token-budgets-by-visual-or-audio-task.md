# Tune Multimodal Token Budgets By Visual Or Audio Task

Summary: Multimodal model inputs should be budgeted by task: image-heavy tasks such as OCR and object recognition need higher resolution and soft-token allocation, while text-dominant workflows can spend fewer tokens on visual inputs.

Use when:
- Configuring image or audio inputs for a multimodal small model.
- Trading quality, latency, and context budget for OCR, object detection, speech recognition, translation, or mostly text-based workflows.

Details:
- Gemma 4 vision support lets developers choose the resolution and soft-token budget allocated to images, with five supported resolution choices across the models. (11:54-12:14)
- Variable aspect ratio support requires spatial positional encoding so the model can distinguish the same patch index in different image layouts. (12:45-13:28)
- Variable resolution support lets teams allocate more tokens to images that need higher detail and fewer tokens when multimodal information is not central to the workflow. (13:28-14:20)
- OCR and spatial object recognition are cited as tasks that should receive higher image token budgets and higher-quality, higher-resolution processing. (14:02-14:12, 15:53-16:06)
- The vision encoder converts 16-by-16 pixel patches into patch embeddings, pools 3-by-3 patch grids into soft tokens, and projects those soft tokens into the model input representation. (12:19-12:41, 15:07-16:26)
- Audio support in E2B and E4B combines raw audio, mel spectrogram features, convolutional downsampling to soft tokens, and a 305M-parameter conformer for translation and speech recognition inputs. (16:31-17:33)

Related topics:
- [Edge Inference](../topics/edge-inference.md)
- [Models](../topics/models.md)
- [Voice Agents](../topics/voice-agents.md)

Related concepts:
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)

Sources:
- [Gemma 4 Deep Dive - Cassidy Hardin, Researcher, Google DeepMind](../sources/20260427__A367W_qvc8.md), 11:36-17:33
