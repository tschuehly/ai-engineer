# Converge Agent Fleets on Cluster-Scheduling Primitives

Summary: Scaling a personal agent fleet from one machine to many recreates the problems a cluster scheduler already solves — placement, compute, secrets, and tool availability. The durable move is to let an agent declare *what* it needs, not *where* it runs, put orchestration/review/hierarchy on top and compute/secrets/tools underneath, and let a scheduler place the work so the machines disappear. In practice that means reusing Kubernetes for the substrate and building only the agent-specific orchestration layer on top.

Use when:
- A single-machine agent setup starts failing as you add machines.
- Deciding whether to hand-roll fleet coordination or stand on an existing scheduler.
- Designing where compute, secrets, and tool access live relative to the agent's logical hierarchy.

Details:
- The one-machine failures that force the issue (Kyle Jaejun Lee, KRAFTON): (1) orchestrators do the work themselves instead of dispatching — fixed by a CLI harness with skills that call those CLIs so dispatching is the only path; (2) managers spin up so many worker panes in one window that panes become unreadable and even `tmux capture-pane` can't extract anything; (3) OOM as Claude Code and MCP processes stack until swap is full and "the machine couldn't breathe"; (4) credentials collide across workspaces instead of binding one-to-one — fixed with a fully separated environment per workspace; (5) a laptop loses power/network and every in-flight job dies. (04:08-06:04)
- Cross-machine coordination is a hand-built distributed system: context moves between machines over git (commit + push context files, then `tmux send-keys` over SSH to trigger a pull, and the remote agent reads the files and resumes); conflicts from two machines editing one directory are fixed with per-machine directories for machine-specific state and shared state changed only through a pull request — "boring is what stops the two machines from silently disagreeing." (06:27-07:04)
- Control must live on always-on hardware: many per-machine gateways collapse into one main gateway that all machines reach over SSH, hosted on an always-on Linux box because "Your one point of control can't be a thing that falls asleep" (the Mac sleeps). A Discord router (one bot per machine) turns a phone into the fleet's remote control. (07:04-07:53)
- The convergence: the four remaining unsolved problems (consistency across machines, abstracting local-only tools stuck on one machine like MCP servers and the browser, secure credential handoff between instances, resource management) all reduce to one principle — "An agent should just declare what it needs, not where it runs. Above it sits the orchestrator, the review gate, the logical hierarchy. Below it, compute, secrets, tools. A scheduler places it, and the machines just disappear underneath. These are the exact questions Kubernetes already answers." (07:53-08:35)
- The build stance: don't reinvent compute, secrets, and tools — "Kubernetes already nailed those. I'm stacking them underneath, and building my orchestration manager on top. Task orchestration, review flow, context management. Reuse what exists, build the new part on top." (08:35-08:52)
- Relationship to distributed-systems discipline: adding machines/agents makes coordination, shared state, and failure propagation first-class — see [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md). This concept adds the specific claim that the substrate is a *solved* infrastructure problem (a cluster scheduler), not one to re-derive per fleet. It also echoes the OpenAI framing that a long-lived agent manager should not be "trapped inside your app" and should figure out which environment (cloud vs. local) is right — see [Manage an Agent Manager Instead of Polling Parallel Agents](manage-an-agent-manager-instead-of-polling-parallel-agents.md).

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Treat multi-agent systems as distributed systems](treat-multi-agent-systems-as-distributed-systems.md)
- [Manage an Agent Manager Instead of Polling Parallel Agents](manage-an-agent-manager-instead-of-polling-parallel-agents.md)
- [Externalize agent state to files and reset instead of compact](externalize-agent-state-to-files-and-reset-instead-of-compact.md)
- [Choose reserved pods for iteration and serverless for autoscaling load](choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md)
- [Separate agentic workflow design from scale infrastructure](separate-agentic-workflow-design-from-scale-infrastructure.md)

Sources:
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../sources/20260708_4kYl2_mqmnQ.md), 04:08-08:52
