# Aggregated personal context creates mosaic and exfiltration risk

Summary: Read-only personal AI reduces mutation risk, but aggregating many personal sources can still create a sensitive composite profile. Security analysis must account for mosaic effects, untrusted content, private data, and any remaining external communication channel.

Use when:
- Evaluating privacy and security boundaries for personal AI, context engines, or retrieval systems.
- Deciding whether read-only mounts, shell access, or network access are sufficient controls.

Details:
- The same cross-referencing that makes a read-only personal intelligence system useful also makes it a high-value target, because many small signals can combine into a revealing picture (09:50-10:11).
- The talk applies Simon Willison's lethal-triquetra framing: private data, untrusted content, and external communication become dangerous together (10:14-10:29).
- Read-only source permissions remove natural write-back channels, but they do not fully break exfiltration risk if shell access or open network access can still communicate externally (10:29-10:44).
- The speaker explicitly does not claim the system is secure: data is sent to Anthropic, the network is mostly open, and more information may be available than the task strictly requires (10:44-11:14).

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [LLM attack surfaces span prompts, context, retrieval, tools, and actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)

Sources:
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md), 09:50-11:14
