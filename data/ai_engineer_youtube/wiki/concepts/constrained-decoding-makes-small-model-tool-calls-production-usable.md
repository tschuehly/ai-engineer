# Constrained Decoding Makes Small-Model Tool Calls Production-Usable

Summary: Small on-device models become more reliable tool callers when the runtime constrains decoding to the specific tool-call shapes available in the current workflow. This turns tool use from open-ended JSON generation into a narrower production control surface.

Use when:
- Hardening function calling for smaller local or edge models.
- Evaluating why a tool-calling workflow works in a demo but fails under production constraints.

Details:
- LiteRT-LM applies constrained decoding when the model is generating a tool call, not necessarily to every generated response.
- The constraint can target the finite set of tools the selected skill is supposed to use, which is stronger than generic JSON constraints.
- The source says strict constrained decoding matters more for smaller on-device models than for very large models, because it adds guardrails that improve production quality.

Related topics:
- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [On-device agents can combine local reasoning with tool and API calls](on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md)
- [Edge agent skills need progressive disclosure to preserve small-model reliability](edge-agent-skills-need-progressive-disclosure-to-preserve-small-model-reliability.md)

Sources:
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md), 28:02-29:13
