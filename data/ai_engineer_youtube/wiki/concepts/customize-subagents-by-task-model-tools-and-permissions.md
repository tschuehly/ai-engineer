# Customize Subagents by Task, Model, Tools, and Permissions

Summary: Subagents are most useful when each one has a narrow task, matching model and reasoning budget, scoped tools, and permissions appropriate to its role.

Use when:
- Splitting a coding-agent task into independent review, implementation, docs, testing, triage, or security work.
- Deciding whether a subagent should be read-only, write-capable, or connected to external tools.

Details:
- The workshop defines subagents as a way to split a master task into decomposable, parallel, independent tasks that return their results after separate runs. 32:39-33:09
- Example personas include documentation reviewers, test-case creators, test-case runners, accessibility reviewers, architects, and security reviewers. 33:35-35:24
- Custom subagents can define model, reasoning effort, sandbox mode, MCP access, and skills. 41:40-43:58
- Review and security subagents should usually run read-only; docs-writing or bug-reporting agents may need write access. 42:32-43:09
- External tool access should be role-specific: the source gives examples such as Sentry access for vulnerability/report inspection and Linear access for backlog triage. 43:14-43:46
- Amp adds context isolation as another reason to specialize subagents: finder, oracle, librarian, and codemod agents each do context-heavy work in their own window and return compact results to the main agent. 06:42-09:06
- **A fifth dimension this page does not name: what the subagent is allowed to see.** Coyle configures a critic subagent by its input rather than its model or permissions — it receives the claim and the evidence and is deliberately denied "the thought processes that went in to creating this claim," because agents that read each other's reasoning "devolve into one idea" ([Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)). He also puts a tighter number on the tool axis than most sources here — one thing, "with maybe one or two tools available to it" — on the functional-programming grounds that specialization beats a generalist carrying every toolkit. ([Coyle](../sources/20260808_Z-c11pV_uvU.md), 12:42-13:05, 13:44-15:12)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use parent agents to compare and merge parallel subagent outputs](use-parent-agents-to-compare-and-merge-parallel-subagent-outputs.md)
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Split large automation surfaces into specialized subagents and subworkflows](split-large-automation-surfaces-into-specialized-subagents-and-subworkflows.md)
- [Use subagents to isolate context-heavy subtasks](use-subagents-to-isolate-context-heavy-subtasks.md)
- [Withhold the Producer's Reasoning From the Critic](withhold-the-producers-reasoning-from-the-critic.md)
- [Give Parallel Agents Complementary Optimization Personas](give-parallel-agents-complementary-optimization-personas.md)

Sources:
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 32:39-35:24, 41:40-43:58
- [Amp Code: Next Generation AI Coding - Beyang Liu, Amp Code](../sources/20251222_gvIAkmZUEZY.md), 06:42-09:06
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](../sources/20260808_Z-c11pV_uvU.md), 12:42-13:05, 13:44-15:12
