# Edge Agent Skills Need Progressive Disclosure To Preserve Small-Model Reliability

Summary: On-device agent skills should expose only lightweight descriptions until the model decides a skill is relevant. Loading full instructions and tool details on demand keeps the context short enough for smaller edge models to reason reliably.

Use when:
- Designing tool or skill systems for on-device agents with limited context budgets.
- Deciding whether to preload all tool descriptions or expose only a skill registry first.

Details:
- AI Edge Gallery skills expose one-line descriptions to the agent first, then let the agent request the full skill instructions and function-call details only after a skill appears relevant.
- The source explicitly frames this as both token efficiency and reliability work: loading every skill's full details into an edge model would create too much context for a lightweight model to reason over.
- Skill packages can include `skill.md`, optional scripts, and assets; full instructions are loaded only when the trigger metadata is not enough.

Related topics:
- [Agents](../topics/agents.md)
- [Edge Inference](../topics/edge-inference.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [On-device agents can combine local reasoning with tool and API calls](on-device-agents-can-combine-local-reasoning-with-tool-and-api-calls.md)

Sources:
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md), 23:44-26:19
