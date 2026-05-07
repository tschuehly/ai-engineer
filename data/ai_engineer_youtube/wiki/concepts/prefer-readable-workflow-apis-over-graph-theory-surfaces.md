# Prefer readable workflow APIs over graph-theory surfaces

Summary: Workflow APIs should expose readable control flow to the team; node-and-edge graph construction can hide the order of operations and force unnecessary graph-theory thinking onto application developers.

Use when:
- Selecting or designing an agent workflow framework API.
- Reviewing whether a workflow definition is understandable enough for team maintenance.

Details:
- Bhagwat argues that teams should not need to learn graph theory to write production AI workflows. (04:43-06:02)
- A fluent workflow syntax can preserve top-to-bottom readability, letting reviewers see what happens first, what follows, and how the code flows. (05:00-05:37)
- Node-and-edge API surfaces can reduce code readability for teams, even when the runtime ultimately represents dependencies as a graph. (05:39-05:48)
- The Gatsby/GraphQL example is used as a cautionary analogy: a powerful default abstraction can still push many users away if it makes common work feel harder than necessary. (03:40-04:43)

Related topics:
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Keep workflow orchestration deterministic and put side effects in steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [DSPy programs keep LLM intent separate from prompt strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)

Sources:
- [Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai](../sources/20250801_8SUJEqQNClw.md), 03:40-06:02
