# Measure First-Prompt Context Burn to Test Progressive Disclosure

Summary: Progressive disclosure is usually asserted and rarely measured. The cheap test is to send one first prompt into a fresh session and read two things: how many tokens the agent consumed before doing any work, and whether it went straight to the right files or started searching.

Use when:
- Checking whether a repo's `AGENTS.md`, `CLAUDE.md`, skills, and rules files actually defer loading or just look like they do.
- Reviewing a proposed addition to always-loaded repo context.
- Setting a regression check on context layout that does not require an eval suite.

Details:
- The test, as stated: "the way you know this is working is when you give it a prompt. When you give it the first prompt, see what it's doing. Is it [grepping] or does it know where to go? But how much context is it burning… immediately? So is it like I think like 20, 25K tokens get taken anyway, but like how much more is getting added? If you're coming to like 40K, 50K, like something's wrong. That's not really progressive disclosure. So you have to figure out these boundaries and then… it's an iteration cycle." ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 15:50-16:20)
- Two readings come out of one observation, and they fail differently:
  - **Token count before work begins.** A baseline of roughly 20–25K is treated as the harness's own overhead (system prompt, tool definitions, repo context). Reaching 40–50K before the task starts means the always-loaded layer is carrying material that should have been behind a pointer.
  - **Search behavior.** "Is it grepping or does it know where to go?" A grep storm on the first turn says the index did not point anywhere useful, which is a different defect from an oversized index — and it can coexist with a *low* token count.
- The measurement is fresh-session-scoped by design. It isolates what the repo's shared setup costs from what the task costs, which is exactly the quantity a team can control and the quantity that gets silently inflated as each engineer adds "one more useful line" to the shared context file.
- This is the leading indicator for the trailing symptom recorded in [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md) — a simple task burning 500k tokens and hitting auto-compaction. A first-prompt reading catches the same defect before the session gets there.
- The corresponding fix lives in [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md): the file loaded on the first turn should point rather than explain, and the material it points at should be reachable from where the agent will actually land.
- Relationship to existing budget material: [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md) budgets the *tool* surface; this budgets the *repo* surface. Both are pre-work costs charged to every session, and a team can hold both against the same first-prompt reading.
- Caveat on the numbers: "I think like 20, 25K" is a recollection, and 40–50K is a threshold from one team's repo with no model, harness, or repo size named. The value of the test is the procedure and the two-signal split; the thresholds should be re-derived from a known-good session in the local setup and then watched for drift.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Read a Broken Agent Setup From Babysitting, Context Burn, and Slop](read-a-broken-agent-setup-from-babysitting-context-burn-and-slop.md)
- [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Use Repository Instructions To Ground Coding Agents](use-repository-instructions-to-ground-coding-agents.md)

Sources:
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 15:50-16:20
