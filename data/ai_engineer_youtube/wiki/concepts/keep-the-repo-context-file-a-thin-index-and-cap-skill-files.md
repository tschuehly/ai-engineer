# Keep the Repo Context File a Thin Index and Cap Skill Files

Summary: The repo context file an agent loads on its first turn should be a thin index that points at the right files, not a document that explains them; and skill entry files should carry a hard line budget — one team's convention is about 100 lines — on the grounds that the skill is a folder and the entry file is only its front door.

Use when:
- Reviewing an `AGENTS.md` or `CLAUDE.md` that has grown by accretion.
- Setting a team convention for skill authoring that survives many contributors.
- Deciding whether a piece of guidance belongs in always-loaded context or behind a pointer.

Details:
- The cap: "even in your [SKILL.md] files, don't overload it. Like, we've kind of set a hard limit for like 100 lines in your [SKILL.md] cuz your skill is really a folder." The reasoning clause is the durable half — the entry file is not the skill, so anything that fits better as a sibling file should be one. ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 14:54-15:04)
- The index: "Don't overload your [CLAUDE.md] or your [AGENTS.md] file into like one big thing. You want to make sure that… it's a thin index that can point through the right files and that's what the agent gets in its like first prompt cuz that's what gets loaded when it starts to work." The justification is a cost argument, not a style preference: this file is charged to every session before any work happens. (15:36-15:50)
- A numeric cap does work that a principle does not. "Keep it small" loses to every individual contributor's locally reasonable addition; "100 lines, hard" makes each addition an explicit trade against an existing line and gives review something to enforce. Khandelwal presents it as a convention his team set, not as a tuned value.
- The two rules compose into a shape: a thin repo index points at skills and docs; each skill's entry file is a thin index that points at its own reference files; and the code itself carries pointers at the places an agent is likely to land (see [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md)). Every layer defers.
- This is the same discipline the wiki records from skill-authoring practice — [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md) has Matt Pocock treating a small top-level `SKILL.md` as a first-class constraint because "every word shaved is a token shaved off every invocation," and moving single-branch reference material behind external files. Khandelwal's contribution is to make it a numeric team-wide rule rather than an authoring judgment, which is what makes it enforceable across ten people who do not all care equally.
- Verification is the companion page: a thin index is a claim, and [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md) is how you find out whether the claim holds — token count before work starts, and whether the agent went straight to the right file or started grepping.
- Caveat: 100 lines is one team's convention with no stated derivation, no model named, and no comparison against a larger or smaller cap. Line count is also a crude proxy for token count. Treat the number as a starting convention and the *existence* of a hard cap as the transferable part.
- **The harness-side counterpart, and it caps a different quantity.** Codex enforces a budget on the *skills list* rather than on any one skill file: "we set a cap of 2% of the maximum context window," and "if you have a lot of skills… the harness will actually trim down the individual descriptions to allow for more skills to be listed" ([Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)). Two differences are worth keeping straight. The unit is a share of the window rather than a line count, so the budget follows the model instead of being restated after every context-length increase. And enforcement is automatic rather than social — the harness degrades gracefully by shortening descriptions, where a 100-line convention relies on review. They are complementary, not substitutes: one bounds what a single skill costs once loaded, the other bounds what the whole catalog costs before anything is loaded. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 06:17-06:35)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md)
- [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Treat Complex Skills Like Software Artifacts](treat-complex-skills-like-software-artifacts.md)
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)
- [Use Repository Instructions To Ground Coding Agents](use-repository-instructions-to-ground-coding-agents.md)
- [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 14:54-15:04, 15:36-15:50
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 06:17-06:35
