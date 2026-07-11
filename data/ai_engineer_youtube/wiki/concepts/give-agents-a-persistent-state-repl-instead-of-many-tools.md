# Give Agents a Persistent-State REPL Instead of Many Tools

Summary: When an agent accumulates many narrow tools and answers a task with a long chain of sequential or parallel tool calls, replace them with a single sandboxed REPL — code mode with persistent state — where the tools become callable functions the agent composes in one call and variables survive across calls.

Use when:
- An agent is making 10+ sequential (or parallel) tool calls per task, timing out, or unable to combine tool results.
- Deciding between hand-authoring more tools and giving the agent a real scripting surface.
- You keep adding capabilities and each one bloats the tool schema.

Details:
- Witan Labs replaced ~15 accumulated spreadsheet tools with one Node.js REPL — all the tools became JavaScript functions the agent combines in a single REPL call — and this was the biggest single jump on their financial-analysis benchmark: ~50% → 74% (further tuning reached 92%). (HEFSExa0xl0 04:11-05:33, 08:24-08:40)
- "If your agent is making many sequential tool calls or even parallel tool calls, you've kind of invented a bad scripting language — so you might as well just give the agent a real one," whether code mode or a REPL. (HEFSExa0xl0 16:12-16:39)
- A REPL goes beyond code mode: code mode already combines multiple tools into one call, but a REPL is "code mode with persistent state" — variables defined in one call are still there in the next, so the agent builds on its own work instead of restarting each turn. (HEFSExa0xl0 06:08-07:00)
- Persistent state changed *how* the agent wrote code: pure code mode led to long ~50-line scripts (many actions at once), while the REPL produced *shorter* scripts, letting the agent interleave reasoning between steps and often reach a better answer faster because it was "less static." (HEFSExa0xl0 07:00-07:34)
- Before the REPL, exploring a sheet took 10-15 sequential tool calls that "very often" timed out because work ran sequentially and even parallel tool calls couldn't combine their results; after, the agent combines everything in one call and gets all results at once, producing "essentially zero timeouts" under a 5-minute budget. (HEFSExa0xl0 05:33-06:05, 09:03-09:24)
- Adding a new capability is cheap: with separate tools a new method (e.g. explore formula dependencies) meant several new schema entries plus reasoning about how they interact; with the REPL it is a few more functions, surfaced to the model by putting a TypeScript type-definitions file into the prompt — "that works really well." (HEFSExa0xl0 07:37-08:20)
- Split the interface language from the implementation language: JavaScript was chosen for the agent surface because it is easy to sandbox and LLMs are familiar with it (Python "would probably work equally well"), while the actual spreadsheet code runs in C# — "use the scripting language for what it's good at… and the right language to deal with the actual files." (HEFSExa0xl0 04:52-05:33)
- Caveat — the REPL is the best interface *today*, not forever: coding is what current SOTA models are best at, so a code REPL wins now, but as labs improve computer use a mouse/keyboard interface may become better; "you should expect to have to revisit" the interface as model capability shifts. (HEFSExa0xl0 11:21-12:06, 16:39-17:41)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)
- [Use Bash as a composable code-mode tool for agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Sandboxed code execution turns model reasoning into inspectable computation](sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md)
- [Interleave reasoning and tool calls for long-horizon agents](interleave-reasoning-and-tool-calls-for-long-horizon-agents.md)
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)

Sources:
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 04:11-08:20, 16:12-17:41
