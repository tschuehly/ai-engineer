# Use Agent Hooks to Automate Session Rituals

Summary: Agent hooks can turn repeated lifecycle actions into programmable start, tool-use, and stop behaviors, but they should preserve clear boundaries around what the agent is allowed to do.

Use when:
- Automating recurring setup, logging, or continuation actions around agent runs.
- Designing long-running coding-agent workflows that need consistent validation or audit steps.

Details:
- The Codex workshop describes hooks for three events: session start, after each tool use, and session stop. 52:54-53:10
- Start hooks can run setup actions such as pulling the latest state from a GitHub repository. 53:19-53:30
- Tool-use hooks can document each tool call, which is useful for research or audit workflows. 53:33-53:49
- Stop hooks can ask a long-running agent to keep going for one more pass, run a validating command, or add one more result before stopping. 53:51-55:32

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Ask agents after each run what blocked their success](ask-agents-after-each-run-what-blocked-their-success.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [OpenAI Codex Masterclass  - Vaibhav Srivastav & Katia Gil Guzman](../sources/20260429_MhHEGMFCEB0.md), 52:54-55:32
