# SPADE Structures AI-Intensive Workflows

Summary: SPADE is a workflow pattern for applications that make many AI calls to produce one useful artifact: synchronize inputs, plan, analyze in parallel, deliver the reduced output, and evaluate.

Use when:
- Designing a high-volume summarization, research, monitoring, or content pipeline around many LLM calls.
- Turning repeated scripts into a more explicit AI application workflow.

Details:
- The AI News pipeline is described as repeated scripts for Discord, Reddit, and Twitter scraping that follow the same core steps: scrape, plan, recursively summarize, format, and evaluate. (10:37-10:57)
- Generalized as an AI-intensive application, the workflow synchronizes inputs, plans, processes in parallel, analyzes and reduces many intermediate results into one output, delivers that output to users, and evaluates it. (11:05-11:35)
- The pattern is useful for applications that make thousands of AI calls to serve one purpose, not only single-response chat products. (11:05-11:15)
- SPADE outputs can be knowledge graphs, structured outputs, or code artifacts such as canvas/artifact-style generated code, not only final prose. (11:36-12:00)

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Compose Deep Research as Plan, Parallel Search, and Analysis Agents](compose-deep-research-as-plan-parallel-search-and-analysis-agents.md)
- [Enterprise deep research runs multi-step synthesis over private corpora](enterprise-deep-research-runs-multi-step-synthesis-over-private-corpora.md)

Sources:
- [Designing AI-Intensive Applications - swyx](../sources/20250809_IHkyFhU6JEY.md), 10:37-12:00
