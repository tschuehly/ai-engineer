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
- **Pruning presumes an owner, which is what an org-scale library lacks.** Every technique on this page — deduplicating, removing sediment, running the deletion test — needs someone with standing to delete other people's text. Touil's account of ungoverned libraries is that this is exactly the missing role: "if you don't have an owner, then no one will be able to maintain, scale those skills," and without a catalog "you cannot really discover it" in the first place. ([Touil](../sources/20260828_M05vON8i0aI.md), 11:56-12:23) His cheap substitute where no owner exists is structural rather than behavioural: statically check a skill against the published best practices, because "if the skill is not invoked properly, if the skill is not structured properly, there's a high chance that it's not going to be high quality" (19:13-19:37) — a screen, not a replacement for the deletion test, and offered with no accuracy figure.
- **Pruning is the maintenance half; the intake half is a reviewed submission point.** Cloudflare controls library size before authoring lands: "we have a central alias where skills are presented to the central team, curated by the go-to-market team, as well as by operations team, and they're reviewed, so we can make sure that we're not having a proliferation of skills, and we have an expert-level knowledge skill at every level." The framing is a phase — "we're sort of reached the Cambrian stage of using agentic systems, which means there's an explosion of excitement and skills" — and the risk named is not oversized skills but divergent ones, since independently authored definitions of the same metric make "the source of truth in all the systems" stop aligning. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 13:36-14:02, 18:19-18:49)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Choose a skill's trigger by trading context load against cognitive load](choose-skill-trigger-by-trading-context-load-against-cognitive-load.md)
- [Retire completed planning docs before they become agent doc rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)
- [Auto-Evolving Skills Multiply Whatever Governance You Already Have](auto-evolving-skills-multiply-whatever-governance-you-already-have.md)
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)

Sources:
- [Building Great Agent Skills: The Missing Manual - Matt Pocock](../sources/20260629_UNzCG3lw6O0.md), 16:48-19:05
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 11:56-12:23, 19:13-19:37
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 13:36-14:02, 18:19-18:49
