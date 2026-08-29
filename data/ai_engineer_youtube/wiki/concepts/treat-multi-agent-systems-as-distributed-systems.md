# Treat multi-agent systems as distributed systems

Summary: Adding agents turns a single-agent feature into a distributed system with coordination, shared-state, failure propagation, and observability problems. Teams should debug multi-agent failures as architecture failures before blaming prompts or model quality.

Use when:
- A working single-agent prototype starts failing after more agents are added.
- Agent outputs depend on other agents, shared caches, shared databases, or partial workflow completion.

Details:
- A one-agent system can demo well with an LLM, prompts, retrieval, and tool calls, but adding agents creates dependencies where one agent produces data another needs, agents wait on each other, shared state changes underneath readers, and one crash can take down the workflow.
- Coordination complexity grows through pairwise relationships: five agents can create at least ten potential coordination paths, and each path can become a failure point, race condition, or state synchronization problem.
- In the credit-decisioning example, a credit-score agent wrote an updated score, but a downstream risk agent read stale cached data and produced incorrect risk ratings; the root problem was cache invalidation and architecture, not prompt quality.
- Multi-agent production work should include distributed-systems practices such as explicit coordination patterns, state lineage, handoff contracts, failure isolation, retries, and observability.
- Meta Superintelligence Labs (Nishant Gupta) reaches the same conclusion from the infrastructure side: "AI agents should be treated as distributed systems… models are stochastic, infrastructure must be deterministic." Once multiple agents share state, familiar distributed-systems issues appear (stale reads, conflicting updates, context drift, inconsistent views), made worse when memory itself is probabilistic and retrieval-based — so "many multi-agent failures are actually consistency failures masquerading as reasoning failures," a direct generalization of the stale-cache credit-decisioning example above.
- The reliability primitives map one-to-one from distributed systems onto agents rather than being invented anew: circuit breakers → tool isolation, rate limits → agent limits, retries → controlled recovery, resource quotas → cost governance, observability → agent tracing.
- **The toolkit transfers, but not unchanged — and the mismatches are specific.** Manuja works through the standard unreliable-dependency remedy for LLM calls and rejects it in three parts: retries "eat into your latency budget really fast" because the calls are slow, blind retries "multiply your cost" because they are expensive, and a circuit breaker is the wrong instrument when "you have another perfectly fine model provider to route to." What survives is the *shape* of distributed-systems thinking — cool-downs, fleet-wide versus per-instance failure state, bounded queues, load shedding, timeouts — with the specific policies re-derived from the properties of model calls rather than copied from a microservice client. ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 02:03-04:35)
- **The same reclassification applied to a business function.** "A year ago, I would have told you that building a GTM system was a marketing ops problem. And today, I think it's one of the most interesting distributed systems problems that I've worked on" — and the evidence offered is a list of distributed-systems failures: per-vendor hops producing stale data, conflicting systems of record, and a batch that one malformed transcript could take down. The remedies are correspondingly infrastructural (a compute/serve split, a durable workflow engine, one routing classifier) rather than prompt-level. ([Liu](../sources/20260826_L4I7WgiEquo.md), 00:20-00:31, 04:36-04:59, 13:29-13:52)
- **The case where the agents are not yours, which removes most of the levers this page assumes.** In an open arena, participants are independently owned and funded, join and leave asynchronously, share no context window or parent process, and coordinate only through public artifacts — a leaderboard ranked by a deterministic verifier, downloadable submissions, and a discussion forum carrying negative results. There is no orchestrator to retry a failed node, no shared state to make consistent, and no merge step. What replaces them is a scoring function plus an incentive to build on a rival's published work. The abuse surface is the distributed-systems concern that carries over unchanged and is left unaddressed by the source: automatic scoring, open admission, and public solutions with nothing stated about spam, copying, or verifier gaming. See [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md). ([Einstein Arena — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 02:18-04:36)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Choose choreography or orchestration by complexity and autonomy](choose-choreography-or-orchestration-by-complexity-and-autonomy.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [Wrap agent calls with circuit breakers and compensation](wrap-agent-calls-with-circuit-breakers-and-compensation.md)
- [Build an Agentic Control Plane So the Model Proposes and the Platform Decides](build-an-agentic-control-plane.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Prefer Per-Request Fallback to Retries and Circuit Breakers for LLM Calls](prefer-per-request-fallback-to-retries-and-circuit-breakers-for-llm-calls.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Open Agent Arenas Reach Solutions No Single Agent Reaches](open-agent-arenas-reach-solutions-no-single-agent-reaches.md)

Sources:
- [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work - Sandipan Bhaumik](../sources/20260408_2czYyrTzILg.md), 01:32-05:28
- [Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs](../sources/20260629_APh1Vx0oLmQ.md), 04:23-06:26
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 02:03-04:35
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 00:20-00:31, 04:36-04:59, 13:29-13:52
- [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](../sources/20260825_mMNkdYnIVC4.md), 02:18-04:36
