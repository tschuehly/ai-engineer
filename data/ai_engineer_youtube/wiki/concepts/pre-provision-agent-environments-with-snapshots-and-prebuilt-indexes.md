# Pre-Provision Agent Environments With Snapshots and Prebuilt Indexes

Summary: Uber runs a warm pool of Kubernetes "balloon pods" for agent work, each already holding snapshotted repositories and a built search index, so claiming an environment takes seconds rather than minutes of clone-and-index. The second decision is shape rather than speed: per-language dev pods were replaced by one mega pod holding all repositories, because agents and engineers both now work across repos.

Use when:
- Agent startup time is dominated by cloning, dependency install, or index building rather than by the task.
- Designing cloud environments for long-running or numerous concurrent agent sessions.
- Deciding whether agent workspaces should be scoped per language, per service, or to everything at once.
- Non-engineers need a working agent environment without a setup ritual.

Details:
- **The requirements, stated as four properties.** Agents need environments that run "for longer period of time. They need to be quick. They need to be isolated. We can install any number of them and they need to be globally available across all of our sites." Long-lived, fast, isolated, numerous, and geographically distributed is a different profile from a human dev environment, which is long-lived and fast but singular. ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 05:54-06:09)
- **Warm pool plus pre-baked state.** "We have a pre-provisioned Kubernetes balloon pods. When an agent requires a new environment to run, it can take one of that which is already pre-provisioned. It has all of the repositories already snapshotted. The search index is already built. So the agents can start working within a matter of seconds." Two separable ideas: the pod is already scheduled (a pooling decision) *and* its contents are already materialized (a caching decision). Either alone leaves the other cost in the critical path. (06:09-06:35)
- **The prebuilt search index is the part specific to coding agents.** A general warm-pool design gives you a running container; it does not give you a codebase the agent can grep at full speed on the first turn. Where a human amortizes indexing across weeks, an ephemeral agent pays it per session unless the platform pre-pays it.
- **Scope followed the work, not the language.** "The roles of engineers are getting blurred. We used to offer a dev pod per language flavor for Go, Java, Android and so on. Now we need agents to work across repositories and engineers also to work across repositories. So we have a mega dev pod that has all of the repositories in one common place and this is what we use for our autonomous coding agents now." The demo bears this out — a single Minion run makes "backend changes and the front end changes here too as well" (13:18-13:42). Per-language partitioning is a constraint the agent has no reason to respect. (06:35-07:03)
- **The same substrate lowers the floor for non-engineers.** "Even for our non-engineer employees, we are providing a simple way for them to get started with any of the agent harnesses in matter of seconds" — the environment problem is most of what stops a non-engineer from using a coding agent, so solving it for the fleet solves it for them incidentally. See [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md). (06:35-07:03)
- **The precondition, and where this stops transferring.** Uber names "six years on moving to monorepos, moving to Bazel" as the foundation (01:04-01:18). A single pod containing *all* repositories with *all* indexes prebuilt is tractable when the repo set is small in number and uniform in build; a polyrepo estate with heterogeneous toolchains gets the pooling idea but not the snapshot-everything idea, and has to choose a partition after all.
- **Caveat.** No cost is given for holding a warm pool of full-codebase pods globally, no pool-sizing or hit-rate figure, and no account of snapshot staleness — how far behind head a claimed pod's snapshot may be, or what the agent does about it.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Declarative Environment and Data Primitives Remove Agent Setup Drag](declarative-environment-and-data-primitives-remove-agent-setup-drag.md)
- [Agent-Native Runtimes Provide Fast, API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [Cloud Agents Turn Coding Work Into Asynchronous VM-Backed Queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Stop the Autonomous Agent at a Draft PR and Validate Before CI](stop-the-autonomous-agent-at-a-draft-pr-and-validate-before-ci.md)
- [Build One Context Graph So Agents Stop Crawling Twenty Systems for Basic Facts](build-one-context-graph-so-agents-stop-crawling-twenty-systems-for-basic-facts.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 01:04-01:18, 05:41-07:03, 13:18-13:42
