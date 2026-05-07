# Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI

Source: [Future-Proof Coding Agents - Bill Chen & Brian Fioca, OpenAI](https://www.youtube.com/watch?v=wVl6ZjELpBk)
Uploaded: 2025-12-05
Transcript: `raw/20251205_wVl6ZjELpBk/wVl6ZjELpBk.en-orig.vtt`

## Summary

OpenAI's coding-agent talk frames the harness as the stable abstraction between fast-changing models and product-specific coding experiences. The durable engineering work is not only picking a model: teams must handle tool loops, prompts, context compaction, sandboxing, permissions, parallel tool calls, MCP plumbing, image handling, SDK integration, and UX surfaces while keeping model-specific habits in mind.

## Extracted Concepts

- [Unified coding-agent harnesses combine models, tools, environments, and safety](../concepts/unified-coding-agent-harnesses-combine-models-tools-environments-and-safety.md) - this source adds concrete harness responsibilities and SDK integration paths.
- [Use stable agent harnesses as model-evolution boundaries](../concepts/use-stable-agent-harnesses-as-model-evolution-boundaries.md) - this source argues that a maintained harness lets products benefit from model upgrades without rebuilding prompts and tools for every release.
- [Prompt coding agents around learned model habits](../concepts/prompt-coding-agents-around-learned-model-habits.md) - this source shows that prompts copied from another model can overconstrain a newer model and reduce performance.
- [Use coding agents as programmable subagents inside products](../concepts/use-coding-agents-as-programmable-subagents-inside-products.md) - this source describes using Codex through SDKs, GitHub Actions, CI/CD, MCP connectors, and product agents.

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

## Notes

- A coding agent is described as three parts: user interface, model, and harness; the harness is the prompt/tool/agent-loop layer that mediates model input and output. 02:06-03:15
- The harness is the model-facing surface for talking to users and code, running tools, working over many turns, and interpreting what the user is asking. 03:55-04:24
- Harness maintenance includes model-specific prompting, custom tool behavior, latency UX, thinking-state summaries, context-window management, compaction, API changes, sandboxing, prompt forwarding, permissions, port management, MCP support, image compression, and parallel tool-call thread merging. 04:39-10:04
- The speakers distinguish model intelligence from learned habits: models may already be trained to plan, inspect context, implement, and test, so prompts that force exhaustive file inspection can make them slower and worse. 06:01-08:07
- Codex is presented as a model plus harness that can be used in VS Code, CLI, cloud, ChatGPT, Slack, GitHub PR review, SDKs, GitHub Actions, CI/CD, and product agents. 08:31-15:28
- A coding agent can be used as a tool inside another agent: the outer product can call Codex programmatically, connect it to MCP, and let it create customer-specific plugin connectors or fix product bugs from inside the product workflow. 11:24-14:28
