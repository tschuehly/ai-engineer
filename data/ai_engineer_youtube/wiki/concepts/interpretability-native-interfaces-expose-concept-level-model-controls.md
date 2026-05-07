# Interpretability-Native Interfaces Expose Concept-Level Model Controls

Summary: Interpretability can create user interfaces that manipulate learned concepts directly instead of translating every intent through text. For generative media, concept palettes, spatial painting, strength controls, and subfeature inspection can become product primitives.

Use when:
- Text prompting is too indirect for spatial, visual, or continuous creative control.
- You need an interface where users can place, move, erase, scale, or interpolate model concepts directly.

Details:
- Paint with Ember demonstrates a canvas connected to image-model internals, where a user paints learned concepts such as pyramid structure, wave, lion face, and opening mouth into specific regions. 12:38-13:46
- The interface uses familiar creative controls: drag, move, erase, replace, and adjust strength values while the generated image responds. 13:52-14:58
- Clicking into concepts exposes subfeatures, enabling granular interpolation such as shifting a lion face toward other animal-like features. 15:04-16:04
- The durable UI lesson is that model-internal representations can become manipulable interface elements, not only hidden implementation details behind a prompt box. 12:58-16:04

Related topics:
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Expose Explicit Control Signals for Generative Media Models](expose-explicit-control-signals-for-generative-media-models.md)
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)

Sources:
- [Why you should care about AI interpretability - Mark Bissell, Goodfire AI](../sources/20250727_6AVMHZPjpTQ.md), 12:38-16:04
