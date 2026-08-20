# Cap the Skills List as a Share of the Context Window

Summary: Give the user-installed skills catalog a hard budget expressed as a percentage of the model's maximum context window, and when the catalog outgrows the budget, degrade by trimming each entry's description rather than by dropping entries. Codex uses 2%.

Use when:
- A user-extensible surface (skills, plugins, MCP servers) can grow without bound and you need the agent to behave the same at 5 skills and 500.
- Deciding whether to truncate a catalog by dropping items or by shortening them.
- Setting a defensible default for how much of the window fixed preamble may consume.

Details:
- The rule as stated: "for available skills, we actually cap the available skills list at 2% of your context total like maximum context window. And that means that if it gets longer, we're reducing slowly the amount of like description that we're putting in there." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 06:17-06:35)
- Two design choices are bundled in that sentence and worth separating. The budget is **relative** — it scales with the model's window rather than being a fixed token count, so the same harness config behaves sensibly across model sizes. And the degradation is **lossy in description, not in enumeration** — every skill stays visible to the model, but each is described in less detail as the list grows. The agent never silently loses the ability to know a skill exists.
- The goal this serves is flexibility, defined in the talk as a user-facing invariant: "regardless of how many or how little skills you're using, you have a great experience regardless of how many plugins and MCPs you install." A budget is how that invariant is enforced rather than hoped for. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 04:48-04:58)
- The skills list and the tool registry are treated differently even though both grow with what the user installed: tools get [deferred out of context entirely](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md), skills get budgeted and trimmed. The implied distinction is that a skill's *existence* is itself the routing signal, so hiding skills behind a search step would defeat the purpose in a way that hiding tool schemas does not. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 05:59-06:35)
- **This is the vendor-side counterpart to the author-side caps the wiki already carries.** Amazon AGI Lab's ~100-line `SKILL.md` limit and thin-index `AGENTS.md` ([Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)) constrain what a skill author writes; the 2% cap constrains what the harness renders regardless of what authors wrote. A team that controls only one of these still has an unbounded surface on the other side.
- **The number is a constant, not a result.** No evidence is given that 2% is optimal, and no data is offered on whether trimmed descriptions degrade skill selection — which is the obvious risk, since the wiki elsewhere records that description quality drives tool choice. Treat 2% as a starting point that a team should re-derive by measuring selection accuracy at its own catalog size. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), Provenance and Caveats)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Defer Tool Definitions Out of Context and Let the Model Search for Them](defer-tool-definitions-out-of-context-and-let-the-model-search-for-them.md)
- [Keep the Repo Context File a Thin Index and Cap Skill Files](keep-the-repo-context-file-a-thin-index-and-cap-skill-files.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [MCP Tool Surfaces Need Default Context Budgets](mcp-tool-surfaces-need-default-context-budgets.md)
- [Measure First-Prompt Context Burn to Test Progressive Disclosure](measure-first-prompt-context-burn-to-test-progressive-disclosure.md)
- [Prune skills with single source of truth, sediment removal, and no-op deletion tests](prune-skills-with-single-source-of-truth-sediment-and-no-op-deletion-tests.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 04:20-06:35
