# Own agent context instead of accepting hidden harness mutation

Summary: Agent harnesses can break user workflows when they silently mutate prompts, tool definitions, reminders, compaction, or tool outputs. Reliable agent use requires inspectable context ownership, not just model capability.

Use when:
- Comparing hosted coding-agent harnesses, local harnesses, or custom agent runtimes.
- Debugging agent behavior that changes after harness releases, tool updates, or hidden context injection.

Details:
- Zechner frames the core problem as losing control of the agent's context: a harness can change the system prompt and tool definitions on every release, remove or modify tools, and insert reminders that may be irrelevant to the current task. (01:56-02:34)
- He also criticizes zero observability, lack of model choice, shallow hook surfaces, automatic tool-output pruning, and LSP error injection into edit-tool results because these hidden behaviors can confuse the model or alter the intended workflow. (02:34-04:24)
- Context ownership is a stronger requirement than context volume: a long context window does not help if the harness injects, truncates, or reshapes information in ways the operator cannot inspect or control.

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Harness engineering shifts scarcity from code production to control surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 01:56-04:24
