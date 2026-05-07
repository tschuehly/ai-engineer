# Return Typed Workspace Outputs From Coding Agents

Summary: Coding-agent workflows can make completion reviewable by requiring the agent to return a typed workspace output, then running deterministic validation against the returned directory before publishing or opening a PR.

Use when:
- Designing an agent function that should produce a repository change as an artifact.
- Separating prompt-level completion from code-level validation and publishing.

Details:
- The Dagger example creates an agent by giving an LLM an environment and prompt, then treats the resulting work variable as completed work only after the prompt-driven task finishes. (39:12-40:19)
- The environment defines a workspace output named `completed`; the code checks that the output is a workspace and then extracts the completed source directory. (40:20-41:07)
- The workflow runs tests again on the returned workspace even though the prompt told the agent to test, making deterministic validation part of the code path rather than only an instruction. (41:07-41:17)
- The workshop later connects the same workflow to GitHub Actions so the agent can run from CI and open a pull request with the generated change. (58:52-61:41)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Treat Coding Agents as Fast Junior Collaborators](treat-coding-agents-as-fast-junior-collaborators.md)
- [Run Coding Agents Through a Simple Master Loop](run-coding-agents-through-a-simple-master-loop.md)

Sources:
- [Ship Agents that Ship: A Hands-On Workshop - Kyle Penfound, Jeremy Adams, Dagger](../sources/20250727_Fzb1a24hF-o.md), 39:12-61:41
