# Building pi in a World of Slop - Mario Zechner

Source: [Building pi in a World of Slop - Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls)
Uploaded: 2026-04-16
Transcript: `raw/20260416_RjfbvDXpFls/RjfbvDXpFls.en-orig.vtt`

## Summary

Mario Zechner uses the pi coding-agent harness to argue for owning agent context, keeping harnesses minimal and extensible, filtering low-signal AI-generated open-source contributions, and limiting agent work to scoped, evaluable, non-critical tasks unless humans read and own the critical code.

## Extracted Concepts

- [Own agent context instead of accepting hidden harness mutation](../concepts/own-agent-context-instead-of-accepting-hidden-harness-mutation.md) - this source identifies hidden system-prompt, tool, reminder, and compaction behavior as a practical cause of workflow breakage.
- [Minimal coding-agent harnesses can outperform feature-heavy surfaces](../concepts/minimal-coding-agent-harnesses-can-outperform-feature-heavy-surfaces.md) - this source points to Terminal-Bench and pi as evidence that tiny tool surfaces can remain competitive.
- [Let agent harnesses extend through ordinary code packages](../concepts/let-agent-harnesses-extend-through-ordinary-code-packages.md) - this source describes pi extensions as TypeScript modules that can add tools, commands, event hooks, state, providers, and compaction.
- [Gate AI-generated open-source contributions through human-effort filters](../concepts/gate-ai-generated-open-source-contributions-through-human-effort-filters.md) - this source documents maintainer-side filters for AI-generated drive-by issues and pull requests.
- [Keep critical code inside human understanding and review capacity](../concepts/keep-critical-code-inside-human-understanding-and-review-capacity.md) - this source argues that agent throughput should not exceed the human ability to read, evaluate, and own important code.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Zechner argues that hidden harness changes to system prompts, tool definitions, reminders, and tool-output handling can make an agent's context no longer belong to the user, breaking workflows without enough observability. (01:56-04:24)
- Terminal-Bench is cited as a minimal benchmark harness that gives the model only a tmux keystroke/output loop, yet scored near the top of the leaderboard in late 2025. (04:46-05:25)
- pi is described as a minimal core with an AI-provider abstraction, agent loop/tool calling, small tool definitions, markdown skills, and documentation/code examples that let the agent modify itself by writing extensions. (05:35-07:05)
- pi extensions are TypeScript modules that can hook into harness events, expose tools and slash commands, save session state, customize compaction, swap providers, and hot reload during a session. (07:53-10:25)
- The talk proposes auto-closing pull requests until a contributor writes a short issue in their own human voice, using that as a practical filter because low-effort agent submissions rarely return to satisfy the requirement. (11:14-11:38)
- For agent use, Zechner recommends scoped tasks where the agent can find all required context, a function can evaluate the result, or the work is non-critical; critical code should be read line by line by the responsible human. (16:13-17:58)
