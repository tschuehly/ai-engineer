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
- **The same practice at a frontier lab, with the motive stated as comprehension rather than pedagogy.** Anthropic replaced "here is a 2,000-line PR" with "here's a Claude Code artifact. Here's the explanation. Here's the intention of the change. Here's the trade-offs that were made," because the binding constraint was "human ability to even fully conceptualize what we're doing." Note the reduced ambition compared with this page: intent and tradeoffs, not a taught curriculum with figures — which is the cheaper end of the same spectrum and may be the version that survives contact with every PR rather than the important ones. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 10:19-11:08)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Understand Agent Work to Participate, Not Just to Verify](understand-agent-work-to-participate-not-just-to-verify.md)
- [Gate Agent Code on a Comprehension Quiz You Must Pass](gate-agent-code-on-a-comprehension-quiz-you-must-pass.md)
- [Build Ephemeral Microworlds to Feel How Code Works](build-ephemeral-microworlds-to-feel-how-code-works.md)
- [Dynamic artifacts make agent work reviewable and reusable](dynamic-artifacts-make-agent-work-reviewable-and-reusable.md)
- [The Review Bottleneck Is Comprehension, Not Reviewer Time](the-review-bottleneck-is-comprehension-not-reviewer-time.md)

Sources:
- [Understanding is the new bottleneck — Geoffrey Litt, Notion](../sources/20260710_WkBPX-oDMnA.md), 07:00-10:15
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 10:19-11:08
