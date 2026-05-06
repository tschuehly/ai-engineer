# Filter Untrusted Context Before It Reaches the Agent

Summary: Execution sandboxes limit what an agent can do with tools, but they do not stop unsafe context from being loaded into the model. Untrusted `agent.md`, `skill.md`, or package context needs filtering for prompt injection, unsafe patterns, secrets, and provenance before the agent reads it.

Use when:
- Installing third-party skills, context packages, or agent instruction files.
- Designing security controls for coding agents that automatically load repository or marketplace context.

Details:
- Debois notes that downloaded `agent.md` or `skill.md` content may be loaded by the coding agent before sandbox controls have any chance to restrict it (21:33-22:02).
- A context filter is described as analogous to a web application firewall: it screens incoming context for prompt injection or unsafe patterns before that context reaches the model (22:02-22:12).
- Context package security also needs scanning for credentials, third-party exposure, and provenance such as who built the package and what model or process produced it (16:48-17:40).
- Agent observability should include logs, traces, and feedback so teams can detect strange production behavior, sandbox escape attempts, or unsafe access to environment variables and memory files (20:38-22:24).
- Carpentero extends the same control to external HTML, URLs, public pages, email, RAG chunks, MCP descriptions, memory, and agent plans because the model cannot natively distinguish trusted instructions from untrusted data. 03:26-04:23, 17:21-17:34

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)

Related concepts:
- [Package reusable context as skills, libraries, and registries](package-reusable-context-as-skills-libraries-and-registries.md)
- [Use skills for workflow guidance and MCP for integrations](use-skills-for-workflow-guidance-and-mcp-for-integrations.md)
- [LLM guardrails need checkpoints at every untrusted boundary](llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md)

Sources:
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md), 16:48-22:24
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md), 03:26-04:23, 17:21-17:34
