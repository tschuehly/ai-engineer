# Let Agents Propose Quest Queues for Parallel Work

Summary: When the human operator runs out of attention or ideas, agents can propose a queue of small missions such as refactors, tests, or feature follow-ups. The human shifts from inventing every task to selecting and approving queued work.

Use when:
- Designing agent interfaces that need to keep useful background work available.
- Moving from one-off prompts to a backlog of agent-discovered maintenance or feature tasks.

Details:
- Salomon argues that parallel agent orchestration is limited by how many ideas a human can keep in mind without fatigue. 05:18-05:35
- AgentCraft responds by asking agents to find missions, turning discovered refactoring, testing, and similar tasks into clickable quests. 05:35-05:46
- A more autonomous version can run a channel on a schedule, scan external sources such as Twitter for ideas, and produce candidate implementations or PRs for the human to choose from. 06:45-07:05
- This pattern increases throughput only if review remains controlled; it can easily turn the bottleneck into a pile of PRs if the queue lacks prioritization and evidence. 07:03-07:25

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Cloud agents turn coding work into asynchronous VM-backed queues](cloud-agents-turn-coding-work-into-asynchronous-vm-backed-queues.md)
- [Automation loops convert repeated review and triage into factory improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)
- [Review bundles compress parallel agent output into evidence](review-bundles-compress-parallel-agent-output-into-evidence.md)

Sources:
- [AgentCraft: Putting the Orc in Orchestration - Ido Salomon](../sources/20260425_kR64LOqBBCU.md), 05:18-07:25
