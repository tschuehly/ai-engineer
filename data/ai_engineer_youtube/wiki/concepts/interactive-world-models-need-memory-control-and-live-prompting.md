# Interactive world models need memory, control, and live prompting

Summary: Interactive world models differ from passive media generators because users act inside the generated environment. Useful systems need controllability, remembered state, physical consistency, and the ability to modify the world while interaction continues.

Use when:
- A generated environment is meant for simulation, training, games, or education rather than one-shot video output.
- The user or agent must navigate, return to prior locations, alter the scene, or test action consequences.

Details:
- Hadsell frames world-model work as moving from training agents in fixed environments toward creating open-ended environments for understanding agency and interaction, 14:35-15:14.
- Genie 1 generated short 2D platformer environments from a prompt and responded to player actions, which was enough to motivate scaling data and methods into 3D games, 15:26-16:08.
- Genie 2 produced interactive 3D environments but was not yet real time and lacked real-world quality, showing latency and fidelity as core thresholds for this model class, 16:08-16:29.
- Genie 3 examples are described as interactive environments with embodied movement, scene dynamics, consistency, and memory; a user can move away, return to the start, and find the world as it was, 16:52-18:47.
- Live prompting changes the active environment while the user is inside it, suggesting use cases for games, adversarial world changes, and education, 18:49-20:06.

Related topics:
- [Agents](../topics/agents.md)
- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)

Related concepts:
- [Expose explicit control signals for generative media models](expose-explicit-control-signals-for-generative-media-models.md)
- [Realtime multimodal models should plan over specialized local actuators](realtime-multimodal-models-should-plan-over-specialized-local-actuators.md)

Sources:
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md), 14:35-20:06
