# Have Agents Write Literate Explainer Docs for Their Changes

Summary: Instead of reviewing a raw diff, have the agent that made a change write a personalized explainer doc that *teaches* it to you, ordered by education principles — background first, intuition before details, tasteful interactive figures, then prose-ordered "literate code diffs." The best explanation is far richer than the code diff, and it is cheap for an agent to produce.

Use when:
- An agent lands a large or unfamiliar change and a raw diff is hard to follow.
- You want to review agent work away from the IDE (Litt prints explainers and reads them "like a textbook about this PR" at a coffee shop).
- Building a reusable skill/command that turns any PR into a comprehension artifact.

Details:
- Framing question: "if you sent a team away for a year to build a personalized curriculum to explain this one change, what would that look like?" — a generative bar that beats the naive "here's the diff." (07:00-07:20)
- Packaged as a shareable `explaindiff` skill that outputs an explainer doc (HTML or Markdown; Litt files them in Notion so the team can comment collaboratively); two public variants exist (HTML output and Notion output). (07:24-07:50, 11:50-12:00)
- **Background first**: don't start with what changed — teach the system (the game engine, coordinate system, subsystems) so the reader is led to where they can even begin to understand the change; skippable/personalizable to what you already know. (08:01-08:24)
- **Intuition before details**: state the essence/goal ("make the garden feel 3D using only 2D drawing tricks") with examples before throwing code — a deeper commit message; "what good math teachers do." (08:24-08:54)
- **Interactive figures** where they help: e.g. drag rocks in a small simulation that shows coordinates and Z-layer ordering (using Notion HTML blocks). Caveat: interactivity can be a crutch and slop; use tastefully or it doesn't add understanding over static pictures. (08:54-09:38)
- **Literate code diffs**: show the code, but with prose explaining files in the right order and what's going on before each file — much easier to follow than a raw ordered file list. (09:38-10:15)
- Pairs with a comprehension quiz at the bottom of the doc as a self-check (see related concept). (11:05-11:40)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [Gate Agent Code on a Comprehension Quiz You Must Pass](gate-agent-code-on-a-comprehension-quiz-you-must-pass.md)
- [Build Ephemeral Microworlds to Feel How Code Works](build-ephemeral-microworlds-to-feel-how-code-works.md)
- [Dynamic artifacts make agent work reviewable and reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)

Sources:
- [Understanding is the new bottleneck — Geoffrey Litt, Notion](../sources/20260710_WkBPX-oDMnA.md), 07:00-10:15
