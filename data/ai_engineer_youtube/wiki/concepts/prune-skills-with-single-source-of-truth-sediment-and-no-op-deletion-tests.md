# Prune skills with single source of truth, sediment removal, and no-op deletion tests

Summary: Oversized skills are a symptom, not a cause; keep `SKILL.md` small by enforcing a single source of truth for every piece, removing "sediment" (stale accreted material), and deleting "no-ops" (instructions that don't change behavior) found with a deletion test.

Use when:
- A skill has grown large and you want to shrink it without losing behavior.
- Reviewing a community- or agent-authored skill for maintainability.

Details:
- Framing: massive skills are usually a symptom of one of the following failure modes rather than a problem in themselves. 16:48-17:15
- Single source of truth (DRY): every part of a skill — including reference material like a PRD template or a small "what is a test seam" note — should live in exactly one place, not be repeated across multiple steps or duplicated across reference material. 17:15-17:55
- Sediment: shared docs accrete material when many people add their own content and nobody feels brave enough to delete or modify others' contributions, leaving irrelevant, unstructured, or stale text. The fix is structural — check whether added material is relevant to all branches; if only some, move it into the correct branch; if irrelevant or stale, kill it. 17:55-18:35
- No-ops: instructions that appear to do something but don't actually influence the agent's behavior in context — a very common artifact when an agent writes your skills. Example: a paragraph telling the agent to write a long detailed commit message, which the agent would write anyway. 18:35-19:00
- Deletion test: to find no-ops, delete the instruction and see whether behavior changes; if it doesn't, the instruction was inert and should stay deleted. This deletion discipline, plus compacting text into leading words and removing sediment, is how Matt Pocock keeps his skills small. 18:50-19:05
- Small skills pay off twice: easier to maintain and audit, and every word shaved is a token shaved off every use — so pruning is both a maintenance and a runtime-cost practice.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Choose a skill's trigger by trading context load against cognitive load](choose-skill-trigger-by-trading-context-load-against-cognitive-load.md)
- [Retire completed planning docs before they become agent doc rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)

Sources:
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 16:48-19:05
