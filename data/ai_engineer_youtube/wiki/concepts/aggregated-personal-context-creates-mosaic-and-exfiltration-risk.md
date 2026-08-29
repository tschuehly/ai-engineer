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
- **The maximal case: an agent cloned from a founder is a maximal-privilege principal by construction.** "I gave it read and write access to all the data that I personally have. And there's a cool advantage to this because I basically have access to every single system at the company… so this thing has access to like everything." The aggregation risk here is not accidental accretion across apps but a deliberate grant of one person's complete reach, and the mitigation offered is narrower capability for other callers rather than narrower context — which addresses writing and tool use, not what the assembled context can reveal in a draft. Building it also required reading years of the person's own email and Slack. ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 08:52-09:47, 13:36-14:08, 16:22-16:52)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Tools](../topics/tools.md)

Related concepts:
- [LLM attack surfaces span prompts, context, retrieval, tools, and actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)
- [Filter untrusted context before it reaches the agent](filter-untrusted-context-before-it-reaches-the-agent.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)
- [Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability](scope-a-person-cloned-agent-by-caller-with-drafts-as-the-shared-capability.md)

Sources:
- [Cognitive Exhaust Fumes, or: Read-Only AI Is Underrated - Simon Podhajsky, Head of AI, Waypoint](../sources/20260408_u0TOSBbAw7c.md), 09:50-11:14
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 08:52-09:47, 13:36-14:08, 16:22-16:52
