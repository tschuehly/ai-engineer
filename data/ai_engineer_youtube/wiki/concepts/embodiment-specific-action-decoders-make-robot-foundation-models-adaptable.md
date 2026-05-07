# Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable

Summary: A robot foundation model can share high-level vision-language-action representations while using embodiment-specific action decoders to produce motion for a particular body. This makes the model adaptable across humanoid hands, industrial arms, and other robot embodiments without making every body a separate foundation model.

Use when:
- Adapting a robot foundation model to a new physical body or actuator layout.
- Explaining the interface between shared model tokens and body-specific continuous control.

Details:
- GR00T N1 is described as open, customizable, and cross-embodiment: a two-billion-parameter base model can be modified for a specific embodiment and use case. (03:53-04:45)
- The model's output tokens are not directly consumable by a physical robot; they need an action decoder that turns model output into body-specific action vectors. (11:42-11:58)
- The action decoder is specific to the embodiment, such as a humanoid hand or industrial robot arm, and translates shared outputs into continuous robot or embodiment motion. (12:05-12:35)
- This action-decoder boundary lets the model leverage foundation knowledge across embodiments and then specialize it to one body. (12:39-13:02)
- The generalist model claim is that foundation knowledge can be extended to different embodiments and downstream tasks, analogous to domain adaptation of a base language model. (16:53-17:28)

Related topics:
- [Robotics](../topics/robotics.md)
- [Models](../topics/models.md)

Related concepts:
- [Dual-System VLA Architectures Separate Planning From Realtime Control](dual-system-vla-architectures-separate-planning-from-realtime-control.md)
- [Robotics Policy Failures Can Originate Below The Model](robotics-policy-failures-can-originate-below-the-model.md)

Sources:
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md), 03:53-04:45, 11:42-13:02, 16:53-17:28
