# Diagnose Agent Failures With Code-Checkable Indicators and Sampling

Summary: At production scale you can't deep-read every agent trace — reading them all costs more than the execution itself — so cluster failures by root cause, distill a code-checkable indicator per failure mode (a specific content pattern or tool-call sequence), and use those indicators plus representative sampling to triage large trace volumes cheaply.

Use when:
- A deployed agent generates far more traces than a human (or an LLM) can read, and you need to find and categorize its failures.
- Building an automated diagnosis/root-cause stage in an agent-improvement loop.
- Deciding how to sample traces for review without missing recurring failure modes.

Details:
- Diagnosis starts by identifying the failure mode the agent encountered, then grouping occurrences by root cause and origin — a section in the agent prompt, or missing/malfunctioning tools — via a recursive "why" chain, before generating new evals to detect the problem and remedies to fix it. 18:57-20:23
- There is an upfront cost: early on you often must deep-read the LLM traces to find out what's going on. 20:46-20:58
- Over time, collect code-checkable indicators per failure mode — "specific pieces of content" or a "specific tool called sequence" where you know the agent will hit an issue — so you can later diagnose problems in traces without reading through all of them. 20:58-21:27
- Scale argument: with millions of agent traces, reading all of them "actually costs more than the execution itself," so it's not efficient; instead pick a representative sample using intelligent segmentation strategies plus the learned indicators. 21:28-22:12
- In practice a multi-tier filter picks the sample: an LLM first reads a portion of traces to spot obvious detectable problems, then the diagnostics focus on a particular failure mode/signal, selecting primary signals by how frequently they occur in the sampled traces. 29:12-30:28
- A guided-search mode complements frequency-based selection: specify a known or user-reported issue and the agent finds all incidents/occurrences of that same problem rather than surveying everything. 30:54-31:32
- The diagnosis output surfaces an assumptions block, because when reading traces without code access the agent makes assumptions that may be wrong — exposing them lets a human see and correct them before accepting the proposed remedies. 32:36-33:00
- Learned failure modes accumulate as historical data each agent can always check against, so diagnosis gets cheaper and more targeted as the agent's failure library grows. 20:24-20:46

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Automate the Agent-Building Loop With an Agentic AI Engineer](automate-the-agent-building-loop-with-an-agentic-ai-engineer.md)
- [Record and Replay Agent Runs at Node Boundaries](record-and-replay-agent-runs-at-node-boundaries.md)
- [Score Every Production Conversation to Judge Agent Health](score-every-production-conversation-to-judge-agent-health.md)
- [Staff Agent Operations With a Team of Agents](staff-agent-operations-with-a-team-of-agents.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)

Sources:
- [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../sources/20260629_pSto5YaNGUo.md), 18:57-33:00
