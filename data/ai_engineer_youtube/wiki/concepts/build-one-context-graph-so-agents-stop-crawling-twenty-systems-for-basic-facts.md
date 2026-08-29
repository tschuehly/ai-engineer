# Build One Context Graph So Agents Stop Crawling Twenty Systems for Basic Facts

Summary: Uber's execution traces showed agents spending most of their effort discovering ownership, dependency, and convention facts that are scattered across 20 to 30 internal systems, each needing its own skill or MCP server to reach. The fix was a single graph — 150 node and edge types, 40 million entries — connecting code, services, design docs, tickets, incidents, and data-lake tables, so a lookup becomes one query instead of a crawl. The diagnosis method is as reusable as the fix: the cost was found by reading traces, not by asking engineers.

Use when:
- Agents in a large codebase take many turns before doing any work, and the turns are all orientation.
- Deciding between adding another retrieval tool and consolidating the facts those tools are fetching.
- The same context lives in a service catalog, a wiki, a tracker, and a schema registry, and each has its own MCP server.
- Justifying a knowledge-graph investment against "the agent can just search for it."

Details:
- **The diagnosis came from traces.** "We started noticing in our execution traces agents spending lot of time even trying to find basic context especially in our large monorepos. You need to identify where the service is located, what are the dependencies, who owns it, what kind of patterns I need to follow." ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 08:44-08:57) These are lookups, not reasoning, and they are the same lookups every task begins with.
- **The cost is threefold and the third one is the important one.** "There's 20 to 30 different systems. Each needs its own skills, its own MCP to gather the context. And this burns tokens. This adds a lot of latency and it creates more unpredictable outcomes." Tokens and latency are budgetable; *unpredictability* is not — an agent that assembles its orientation differently on each run produces work that varies for reasons unrelated to the task. (08:57-09:12)
- **What the graph spans.** "This has 150 unique node and edge types. We have 40 million entries there right now. It captures all the way from how our mobile apps are built to our back end to our data lake. All the design docs, Jira, incident bugs, everything is connected." The breadth is the point: a graph covering only code would not answer "who owns it," and one covering only the org chart would not answer "which table." (09:12-09:41)
- **It is a substrate for skills, not a skill.** "We are now plugging all of our skills and use cases into the graph whether it's our on-call RCAs, whether it's planning or data analysis or security scans." One graph with many consumers is a different economic proposition from one retrieval tool per use case, and it is what justifies 150 node types.
- **The worked example shows why a graph and not a search index.** "How many mobility trips in India are cash — this needs to understand the concepts of each of these, which tables, what kind of cities you need to create for this SQL." The chain is concept → schema → geography → query; each hop is a join the agent would otherwise have to guess. This is the structural-relationship case for graph retrieval; see [Choose HybridRAG When Relationship Structure Matters](choose-hybridrag-when-relationship-structure-matters.md). (09:55-10:07)
- **The reported effect, and its evidential weight.** "With and without graph we see massive improvement in tokens, turns and latency, and we see that across any earlier eval that we did within our infrastructure." Turns is the load-bearing metric here — it is the direct measure of the crawl the graph replaces. No absolute numbers appear, the comparison is shown as a chart against one question, and the eval set is not described. (10:07-10:21)
- **The unaddressed question is freshness.** Ownership, dependencies, and conventions change continuously, and a stale graph is worse than a slow crawl because it is confidently wrong. Nothing in the talk describes ingestion cadence, conflict resolution between sources, or what an agent does when the graph disagrees with the repository. The wiki's related caution is that agents should read an intent graph they cannot write — see [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md) — which sharpens the question rather than answering it: if only humans and pipelines write, what keeps 40 million entries current?

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Knowledge Graphs Make Agent Memory Traversable and Explainable](knowledge-graphs-make-agent-memory-traversable-and-explainable.md)
- [Choose HybridRAG When Relationship Structure Matters](choose-hybridrag-when-relationship-structure-matters.md)
- [Keep a Living Intent Graph That Agents Read but Cannot Write](keep-a-living-intent-graph-that-agents-read-but-cannot-write.md)
- [Go Straight to the Known Source Instead of Searching for It](go-straight-to-the-known-source-instead-of-searching-for-it.md)
- [Live Architecture Digital Twins Ground Architecture Copilots](live-architecture-digital-twins-ground-architecture-copilots.md)
- [Evaluate Operational Graph Agents With Extrinsic Task Metrics](evaluate-operational-graph-agents-with-extrinsic-task-metrics.md)
- [Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md)
- [A Missing Skill Is Billed as Tokens, Not Recorded as a Gap](a-missing-skill-is-billed-as-tokens-not-recorded-as-a-gap.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 08:44-10:21
