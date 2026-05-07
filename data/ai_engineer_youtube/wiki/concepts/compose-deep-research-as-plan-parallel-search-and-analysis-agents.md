# Compose Deep Research as Plan, Parallel Search, and Analysis Agents

Summary: A practical deep-research workflow can be composed from small agent roles: one agent creates a structured plan, several search agents gather evidence in parallel, and a final analysis agent synthesizes the results into an answer.

Use when:
- Building a research agent that needs parallel evidence gathering without a heavyweight graph abstraction.
- Deciding how to split model choice and observability across planning, search, and final synthesis.

Details:
- The demo's plan object contains an executive summary for the user, a bounded list of web-search steps, and analysis instructions, which makes the research run inspectable before the search phase begins, 12:48-13:09.
- Colvin frames the "agent" as a composition of smaller agent microtasks rather than one microservice-sized LLM loop: a plan agent returns a structured Pydantic model, search agents use Tavily or web search, and a final analysis agent synthesizes the gathered context, 13:11-14:32.
- Parallel search can use ordinary Python constructs such as `TaskGroup` or `asyncio.gather`; durable execution can record those activities without requiring the workflow to be rewritten as a graph, 15:01-15:25, 17:51-18:24.
- The workflow formats search results into XML-like context before final synthesis, making the handoff between search and analysis explicit and inspectable, 15:10-15:25.
- Logfire observability shows the plan step, parallel search steps, chosen queries, retrieved data, analysis step, and running cost, giving the operator a trace of where the research workflow spent time and money, 15:40-16:41.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Deep Research Agents Need Planning, Grounded Evidence, and Pivot Loops](deep-research-agents-need-planning-grounded-evidence-and-pivot-loops.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)
- [Stage Complex AI Applications Into Inspectable Deterministic and Agentic Steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)

Sources:
- [From Stateless Nightmares to Durable Agents - Samuel Colvin, Pydantic](../sources/20251124_flf_IKnFYnE.md), 12:48-16:41, 17:51-18:24
