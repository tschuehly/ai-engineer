# Action Expert Transformers Adapt VLMs For High-Frequency Robot Control

Summary: A VLA can reuse a pretrained vision-language backbone while adding architecture that emits continuous robot actions at control frequency. PI's described pattern uses a VLM backbone for scene understanding and task decomposition plus an action expert transformer that attends to the backbone and generates continuous actions with diffusion flow matching.

Use when:
- Comparing ordinary multimodal LLMs with robot policies that must output actions rather than text.
- Designing embodied models that need both semantic task understanding and fast continuous control.

Details:
- The talk defines a VLA as an adaptation of a VLM for robotics: it receives text, images, and robot state such as joint positions, then produces actions to control the robot directly instead of answering questions in text. (02:24-03:15)
- Robotics training can reuse VLM backbones, but model architecture must be adapted for high-frequency robot control and there is no standard deployment solution for large robot policies across on-premise, on-device, and robot settings. (04:33-05:00)
- PI05 adds robot data, multimodal VLM data, object detection data, and language annotations to training; the backbone handles scene questions and high-level request subdivision such as turning "clean my bedroom" into smaller subtasks. (11:26-12:29)
- The action expert transformer attends to the VLM internals, runs at a higher rate, and produces continuous output actions via diffusion flow matching. (12:29-12:40)

Related topics:
- [Robotics](../topics/robotics.md)
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Dual-System VLA Architectures Separate Planning From Realtime Control](dual-system-vla-architectures-separate-planning-from-realtime-control.md)
- [Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable](embodiment-specific-action-decoders-make-robot-foundation-models-adaptable.md)

Sources:
- [Robotics: why now? - Quan Vuong and Jost Tobias Springberg, Physical Intelligence](../sources/20250726_cGLa8DsOYdk.md), 02:24-05:00, 11:26-12:40
