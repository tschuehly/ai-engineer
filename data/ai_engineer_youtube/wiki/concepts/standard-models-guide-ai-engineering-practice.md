# Standard Models Guide AI Engineering Practice

Summary: AI engineering needs durable mental models that help teams reason beyond one technique such as RAG. Useful "standard models" name the repeated application shapes, tool stacks, and production concerns that many teams can reuse.

Use when:
- Comparing AI application architecture patterns that might become reusable across teams.
- Deciding whether a technique is a full design model or only one component in a larger system.

Details:
- The talk compares AI engineering's current stage to older engineering periods that produced stable patterns such as ETL, MVC, CRUD, and MapReduce; the goal is to discover similarly reusable AI engineering models. (04:55-05:37)
- RAG is named as useful but insufficient as a full standard model, especially as long-context and fine-tuning approaches also compete to solve context problems. (05:37-05:58)
- Candidate standard models include an LM OS updated for multimodality, common tool surfaces, and MCP; an LLM-shaped SDLC; and agent-building frameworks such as Anthropic's building-effective-agents guidance and OpenAI's Agents SDK/Swarm lineage. (06:00-08:04)
- The point of a standard model is practical navigation: teams should ask whether the model helps them add intelligence to an application in a useful and non-annoying way, not whether it wins a terminology debate. (12:08-12:40)

Related topics:
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent connectivity stack combines skills, MCP, CLIs, and computer use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Treat model behavior as a product craft](treat-model-behavior-as-a-product-craft.md)

Sources:
- [Designing AI-Intensive Applications - swyx](../sources/20250809_IHkyFhU6JEY.md), 04:55-08:04
