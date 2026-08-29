# Build Orchestration From a Few General-Purpose Node Types

Summary: Rather than growing a library of task-specific integrations, model orchestration as a graph over a small fixed vocabulary of general-purpose nodes — agent, tool call, conditional, code, and map-reduce fan-out — so that new workflows are compositions of existing primitives instead of new connectors.

Use when:
- Choosing or designing the execution model for a workflow product that has to reach many external systems.
- A workflow tool has accumulated one bespoke node per integration and each new use case needs another.
- Deciding what an agent step is allowed to be inside a larger deterministic pipeline.

Details:
- The design is presented as the outcome of iteration, not a starting position: "we've iterated on this problem quite a bit and we've ended up in a place where we are basically taking a graph-based view of the orchestration problem with a series of general purpose nodes that are executing various things." ([Berry](../sources/20260826_UhCY231d0FQ.md), 08:55-09:10)
- **The vocabulary is five node types.** "We have nodes that run agents, nodes that make tool calls, nodes that handle our conditional logic, nodes that run code, and then nodes that run effectively this map reduce system to fan out the information and bring it back." (09:10-09:24)
- The recommendation is deliberately detached from the product: "a great orchestration layer will handle all of these and whether you buy it or build it, I think this is like fundamentally the modern way to set this up." (09:24-09:32)
- A run has a standard shape over that vocabulary: "some sort of event that kicks off my orchestration, some trigger or some schedule. I'm going to then talk to a couple different systems. I'm going to combine that information back together, and then I'm going to push it out to different interfaces that my reps are using." Trigger, fan-out, reduce, deliver. (09:32-09:53)
- **The interesting choice is where the model sits.** An agent is one node type among five, not the substrate the others run inside — conditionals and code are their own nodes rather than things the agent decides. That places this design on the deterministic-shell side of the tradeoff in [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md), and makes the map-reduce node, not the agent node, the thing that gives the graph its scale.
- The map-reduce node is what makes this viable for a data layer rather than a single request: enrichment, scoring, and messaging are all per-record operations over a list, and fan-out plus reduce is the only one of the five primitives that changes cardinality.
- **A user-facing tension this page inherits.** [Prefer Readable Workflow APIs Over Graph-Theory Surfaces](prefer-readable-workflow-apis-over-graph-theory-surfaces.md) argues that exposing nodes and edges as the authoring interface pushes graph mechanics onto the user. Both can hold: a small primitive set is a good *execution* model and a poor *authoring* model, and the resolution is that the graph is what runs, not necessarily what anyone writes by hand. Berry's audience is builders of the layer, not its end users, and the talk does not say how a rep or GTM engineer actually composes one.
- **Limit.** No semantics are given for any node — no error model, no retry or compensation behavior, no state passing convention, no concurrency bound on the fan-out, and no account of how the "failures happening all the time" from the same talk are surfaced or resumed. The five types are asserted as sufficient with one screenshot as evidence. (08:55-09:53)

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [Keep Workflow Orchestration Deterministic and Put Side Effects in Steps](keep-workflow-orchestration-deterministic-and-put-side-effects-in-steps.md)
- [Prefer Readable Workflow APIs Over Graph-Theory Surfaces](prefer-readable-workflow-apis-over-graph-theory-surfaces.md)
- [Choose Choreography or Orchestration by Complexity and Autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Record and Replay Agent Runs at Node Boundaries](record-and-replay-agent-runs-at-node-boundaries.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Use Durable Execution for Production Agent Loops](use-durable-execution-for-production-agent-loops.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 08:55-09:53
