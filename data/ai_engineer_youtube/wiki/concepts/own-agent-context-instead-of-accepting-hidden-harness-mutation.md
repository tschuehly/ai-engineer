# Own agent context instead of accepting hidden harness mutation

Summary: Agent harnesses can break user workflows when they silently mutate prompts, tool definitions, reminders, compaction, or tool outputs. Reliable agent use requires inspectable context ownership, not just model capability.

Use when:
- Comparing hosted coding-agent harnesses, local harnesses, or custom agent runtimes.
- Debugging agent behavior that changes after harness releases, tool updates, or hidden context injection.

Details:
- Zechner frames the core problem as losing control of the agent's context: a harness can change the system prompt and tool definitions on every release, remove or modify tools, and insert reminders that may be irrelevant to the current task. (01:56-02:34)
- He also criticizes zero observability, lack of model choice, shallow hook surfaces, automatic tool-output pruning, and LSP error injection into edit-tool results because these hidden behaviors can confuse the model or alter the intended workflow. (02:34-04:24)
- Context ownership is a stronger requirement than context volume: a long context window does not help if the harness injects, truncates, or reshapes information in ways the operator cannot inspect or control.
- **A vendor-side account of the same mutation, including why it was added and what it cost.** Anthropic added context-reset machinery to its harness because Sonnet 4.5 "literally got anxious as it approached its context window limit" and wrapped up work early; on a later model that no longer had the behavior, the machinery "became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times." Read alongside this page, it is the mutation Zechner objects to, described from the inside: added for a real reason, invisible to the operator, and outliving the reason. ([A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md); [Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 07:58-08:52)
- **The architectural version of ownership.** Where a harness keeps the session as a durable log rather than treating the window *as* the session, mutation stops being destructive: the harness "can actually just read in slices of that context from the session log into its current window," so a truncation the operator disagrees with is reversible rather than final ([Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)). That does not make the mutation inspectable — the objection on this page stands — but it changes the stakes of getting it wrong. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 15:04-15:47)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Context Engineering](../topics/context-engineering.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Harness engineering shifts scarcity from code production to control surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [A Harness Fix Becomes Overhead When the Model Outgrows It](a-harness-fix-becomes-overhead-when-the-model-outgrows-it.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)

Sources:
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md), 01:56-04:24
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 07:58-08:52, 15:04-15:47
