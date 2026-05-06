# Agent Rules Should Emerge From Observed Off-Rail Behavior

Summary: Agent rules are most useful when they encode concrete failures or recurring constraints discovered during real work. Broadly installing generic rules can bloat context without addressing the actual ways agents fail in a given repository.

Use when:
- Deciding what belongs in repository rules, `AGENTS.md`, skills, or policy hooks.
- Improving agent behavior after observing repeated mistakes.

Details:
- The talk challenges the assumption that teams should install every framework or stack rule they can find; rules should instead emerge dynamically from observed agent behavior (06:56-07:30).
- Useful rules behave like SOPs: they tell agents what they can and cannot do in the local system, especially after a run exposes an off-rail pattern (07:24-07:39).
- Guardrails can include rules, checks, and hooks; sensitive areas such as authentication, encryption, or sensitive-data handling may need hooks or restrictions rather than relying only on model judgment (06:17-06:55).
- Better models may follow specific rules more reliably, but the source still treats rules as part of a larger guardrail system rather than as a replacement for tests and review (07:39-07:51).

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use agent hooks to automate session rituals](use-agent-hooks-to-automate-session-rituals.md)
- [Ask agents after each run what blocked their success](ask-agents-after-each-run-what-blocked-their-success.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)

Sources:
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md), 06:17-07:51
