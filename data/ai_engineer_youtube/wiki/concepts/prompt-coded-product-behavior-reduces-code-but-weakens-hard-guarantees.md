# Prompt-coded product behavior reduces code but weakens hard guarantees

Summary: Product behavior can sometimes move from application code into skill-like prompts or commands, sharply reducing maintenance cost for advanced workflows. The tradeoff is that prompt-coded behavior usually loses hard runtime guarantees and must be backed by evals, reminders, and a willingness to re-native critical boundaries.

Use when:
- Deciding whether an advanced agent workflow should be implemented as product code, a command prompt, or a skill.
- Reviewing risks created when operational behavior is enforced by instructions rather than runtime constraints.

Details:
- Cursor's worktree feature originally needed code for creating and managing worktrees, feeding worktree state into the agent, scoping the agent, running setup scripts, judging outputs, adding reminders, and cleaning up accumulated worktrees. 03:10-04:15
- Cursor replaced most of the feature with skill-like commands using agent skills and subagents, deleting roughly 15,000 lines of code while retaining an advanced workflow for power users. 04:15-05:30
- The command prompts are not ordinary user-installed skills; they are server-controlled prompts loaded on demand, so Cursor can improve them without a client update. 08:24-09:05
- Prompt-coded behavior improved maintenance burden and unlocked mid-chat switching into worktrees and multi-repo worktree creation, but made discoverability worse because the workflow moved out of visible dropdown UI into slash commands. 09:58-11:45, 13:40-14:14
- The main safety regression is that previous product code could make it physically impossible for the agent to edit outside its worktree, while the prompt-coded version relies on the model remembering and obeying workspace instructions. 12:33-13:18

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)

Sources:
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md), 03:10-14:14
