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
- **The counterweight, and the distinction that reconciles it: execution model versus authoring model.** Clay converged on "a graph-based view of the orchestration problem with a series of general purpose nodes" after iteration, and defends it as the right way to structure the layer regardless of whether you buy or build. That is a claim about what runs, not about what a user writes — and Berry's audience is builders of the orchestration layer rather than its end users. A small node vocabulary can be the correct runtime while a graph editor is still the wrong authoring surface; the failure this page names starts when the runtime's vertices and edges are handed to the person expressing the intent. ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:55-09:32)

Related topics:
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Keep workflow orchestration deterministic and put side effects in steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [DSPy programs keep LLM intent separate from prompt strings](dspy-programs-keep-llm-intent-separate-from-prompt-strings.md)
- [Build Orchestration From a Few General-Purpose Node Types](build-orchestration-from-a-few-general-purpose-node-types.md)

Sources:
- [Agents vs Workflows: Why Not Both? - Sam Bhagwat, Mastra.ai](../sources/20250801_8SUJEqQNClw.md), 03:40-06:02
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:55-09:32
