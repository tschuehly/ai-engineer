# Keep visual inputs at native shape for GUI and video agents

Summary: Visual agent models should preserve useful image shape and temporal metadata instead of normalizing every input into a fixed square. Screenshots, slides, long vertical images, and videos often carry task-critical layout and sequence information.

Use when:
- Designing multimodal models or preprocessing pipelines for GUI agents, document screenshots, slides, or video understanding.
- Evaluating whether image normalization is destroying layout or temporal cues needed for agent actions.

Details:
- GLM 4.5V keeps visual input as close to original as possible so the model can see native resolution and aspect ratio rather than forcing every image into a fixed square. (14:35-15:05)
- The talk says this matters for screenshots, long vertical images, and PowerPoint slides, where layout and shape are part of the task. (15:05-15:12)
- For video, the model inserts time-index tokens after frames so the model can understand temporal order, which is important for action understanding and step-by-step procedures. (15:12-15:30)
- The same section connects visual understanding to GUI agent capability over computers, browsers, and mobile environments using mouse, keyboard, or touch actions. (15:32-16:02)
- **How the image reaches the model is a separate decision from whether it should.** Figma's first attempt at attaching design imagery was inline base64 in the code payload, and it "just blew up the context window and was bad all around. um don't do that"; the fix was to abstract images out of the serialized scene graph entirely and hoist them to the top level as links, keeping the visual available without paying for it in every nested position. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 05:09-05:24)

Related topics:
- [Agents](../topics/agents.md)
- [Models](../topics/models.md)

Related concepts:
- [Tune multimodal token budgets by visual or audio task](tune-multimodal-token-budgets-by-visual-or-audio-task.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Browser agents sit in the prompt-injection lethal trifecta](browser-agents-sit-in-the-prompt-injection-lethal-trifecta.md)
- [Pick the Serialization the Models Have Seen Most, Not the One Native to Your System](pick-the-serialization-the-models-have-seen-most.md)

Sources:
- [Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads - Yuxuan Zhang, Z.ai](../sources/20251122_m6MF1OR_9kM.md), 14:35-16:02
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 05:09-05:24
