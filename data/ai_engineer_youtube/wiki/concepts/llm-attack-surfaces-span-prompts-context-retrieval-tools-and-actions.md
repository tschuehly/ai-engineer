# LLM Attack Surfaces Span Prompts, Context, Retrieval, Tools, and Actions

Summary: Production LLM attacks are not confined to direct user prompts. They can enter through external context, model internals, poisoned retrieval chunks, MCP tool metadata, and the actions an agent is allowed to take.

Use when:
- Threat-modeling an LLM or agent system beyond ordinary prompt injection.
- Deciding which inputs, retrieval stores, tool definitions, and action paths need security review.

Details:
- Direct prompt injection works because system controls and user data are presented to the model as one combined context rather than as natively separated security domains. 01:13-03:24
- Indirect context injection places malicious instructions in external content such as HTML, URLs, public pages, or email inboxes, then waits for the LLM to fetch them. 03:26-04:23
- Model-internals jailbreaks can use optimized gibberish suffixes to push the next-token distribution toward affirmative harmful completions, exploiting alignment as a probabilistic preference rather than a hard constraint. 06:06-09:28
- RAG poisoning targets retrieval and generation together: malicious chunks must be retrieved for a target query and then be convincing enough to steer the generated answer. 09:28-10:47
- MCP attacks can exploit the difference between what a human sees in a tool summary and what the model reads in the full tool description. 10:53-12:04
- Agentic escalation targets what a compromised model is allowed to do, including clicking links, downloading files, changing file modes, installing packages, or continuing a self-escalation path. 12:04-14:29

Related topics:
- [Agents](../topics/agents.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Run agent-written API code inside programmable sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [MCP tool surfaces need default context budgets](mcp-tool-surfaces-need-default-context-budgets.md)

Sources:
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 01:13-14:29
