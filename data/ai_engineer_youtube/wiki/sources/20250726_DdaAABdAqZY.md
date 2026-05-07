# Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft

Source: [Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft](https://www.youtube.com/watch?v=DdaAABdAqZY)
Uploaded: 2025-07-26
Transcript: `raw/20250726_DdaAABdAqZY/DdaAABdAqZY.en-orig.vtt`

## Summary

Christopher Harrison's workshop frames GitHub Copilot as a peer-programming agent whose usefulness depends on choosing the right interaction mode, providing explicit task context, configuring repository instructions, preparing the execution environment, and treating MCP servers as trusted action-capable tools rather than harmless data sources.

## Extracted Concepts

- [Choose Copilot Mode By Autonomy and Feedback Need](../concepts/choose-copilot-mode-by-autonomy-and-feedback-need.md) - supports a mode-selection pattern across ask, edit, local agent, and asynchronous coding-agent workflows.
- [Layer Copilot Context Through Issues, Instructions, and Repository Structure](../concepts/layer-copilot-context-through-issues-instructions-and-repository-structure.md) - shows how issue text, instruction files, scoped file patterns, and existing project structure guide agent output.
- [Prepare Copilot Coding Agent Environments With Setup Steps](../concepts/prepare-copilot-coding-agent-environments-with-setup-steps.md) - explains how GitHub Actions setup steps and tests make asynchronous Copilot work more reliable.
- [Vet MCP Servers As Action-Capable Extensions](../concepts/vet-mcp-servers-as-action-capable-extensions.md) - reinforces that MCP servers can read external data and perform actions on the user's behalf.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Copilot is presented as an AI pair programmer with strengths, weaknesses, and workload fit; the workshop distinguishes ask mode, edit mode, local agent mode, and Copilot Coding Agent. 03:56-05:17
- Local agent mode can explore a project, find files, build code, run tests, and try to recover from failures. 11:42-12:10
- MCP expands Copilot by letting it call external services through an MCP server; examples include creating GitHub issues, searching, and retrieving database schemas or data. 23:48-25:16
- Third-party MCP servers should be trusted before use because they can access data and perform tasks on the user's behalf. 25:18-25:58
- Copilot Coding Agent is designed for asynchronous issue assignment, which makes issue context and explicit desired approach important because the agent may work without an interactive clarification loop. 30:19-31:58
- `copilot-instructions.md` applies broadly to chat and coding-agent workflows, while task-specific instruction files can be attached manually or scoped to file patterns such as JSX, TSX, or tests. 32:06-39:45
- Copilot Coding Agent runs behind the scenes through GitHub Actions and can use a `copilot setup steps` workflow to install libraries, frameworks, services, and scripts before working. 33:51-34:36
