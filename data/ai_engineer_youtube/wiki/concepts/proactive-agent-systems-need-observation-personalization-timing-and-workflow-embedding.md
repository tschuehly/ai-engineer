# Proactive Agent Systems Need Observation, Personalization, Timing, and Workflow Embedding

Summary: Proactive agents need enough situational awareness to act before an explicit prompt without becoming noisy or detached from the user's real work. The reusable design pattern combines continuous observation, personalization, timely intervention, and integration into existing work surfaces.

Use when:
- Designing agents that should notice work opportunities instead of waiting for a chat prompt.
- Evaluating whether an agent's proactivity will reduce mental load or create more interruption and supervision.

Details:
- The mental-load problem is that async agents can do work while humans still track completion, follow up, and decide what to ask next; useful proactivity should reduce that monitoring burden (00:39-02:21).
- Reactive developer tools are compute-efficient because they only run on explicit prompt or autocomplete request, but that model keeps the human responsible for managing AI work (03:26-03:50).
- A proactive agent needs observation over code changes, workflow patterns, and project context so it can notice friction and candidate work (04:29-04:46).
- Personalization is required because the agent must learn how the user works, what they care about, what they ignore, preferences, and areas of code they do not want touched (04:46-04:56).
- Timing is a product constraint: acting too early interrupts the user, while acting too late misses the useful moment (04:56-05:03).
- Workflow embedding matters because the agent should appear in terminals, repositories, and IDEs where the user already works rather than forcing attention into a separate app (05:03-05:20).

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Local OS agents can invert the prompt flow](local-os-agents-can-invert-the-prompt-flow.md)
- [Purpose-built agent workspaces make orchestration visible](purpose-built-agent-workspaces-make-orchestration-visible.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)

Sources:
- [Proactive Agents - Kath Korevec, Google Labs](../sources/20251213_v3u8xc0zLec.md), 00:39-05:20
