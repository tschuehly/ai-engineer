# Manage an Agent Manager Instead of Polling Parallel Agents

Summary: Running many agents by hand (a wall of terminals you keep switching between) makes the human the scheduler, router, and memory — that is polling, not orchestration. The scalable shape is one long-lived manager agent that delegates to workers while you set direction in an outer loop and drop down to pair only on tricky work. Three harness capabilities make it real: persistent context (server-side compaction), delegation/coordination, and triggers.

Use when:
- You are juggling many parallel agent sessions and hitting a coordination ceiling.
- Designing an agent harness or workflow meant to run autonomously across many tasks and wake you only when needed.
- Deciding where the human's loop sits relative to the agents' loops.

Details:
- The failure mode named precisely: juggling 10+ terminal windows "felt like peak productivity" in January but "today it feels a little bit silly. I thought I was orchestrating. Really, I was polling. I was the scheduler, the router, and the memory." Ten terminals is not pairing — it is "managing 10 direct reports." (18:56-19:41)
- The shift: "Now, I mostly talk to a long-running manager, which delegates work to a team. For tricky work, I can still drop down and pair directly with a worker, but my default changed… I manage the manager of a small company of agents." (19:46-20:02)
- Three enablers = the loop: (1) **server-side compaction** made long-running tasks reliable enough to stop optimizing around fresh sessions; (2) **coordination** lets one thread create and steer the right projects; (3) **automation/triggers** can wake the same manager when something happens — "persistent context, delegation, and triggers. There's your loop." (20:04-20:34)
- Inner vs. outer loop: "the agent runs the inner execution loop. I set the direction and I make decisions in the outer loop." (23:06-23:16)
- Concrete outer-loop workflow: an issue is filed on an open-source project → the manager wakes, reads it against the project's goals/notes/vision, decides whether it fits, and creates a worker; the worker investigates, implements, and runs tests; another agent reviews; when the manager needs you it returns a PR plus the original issue, the proposed diff, and maybe a video or a running build you can VNC into; you review once, leave a note, approve, and it lands after checks pass — you never watch the intermediary messages. (22:08-23:16)
- Real instance: a pinned "chief of staff" agent wakes every 10 minutes, coordinates GitHub work, and creates sidebar threads the human can jump into. (23:16-23:28)
- Location independence is the next gap: once the manager is long-lived, "tying it to a laptop just feels wrong" — Codex can move work between hosts and Open Claw has a gateway and nodes, but "neither feels like the final form"; the manager should connect to any of your machines, know which work is cloud vs. local, and be steerable from Slack or wherever you are (Embiricos frames the same idea as removing the local/cloud distinction — "just have an agent… and it should figure out which environment is right"). (16:51-17:54, 23:38-24:29)
- The forward-looking constraint: "models are advancing faster than the harnesses and organizations around them. Designing those things is the next engineering problem… The future is not 20 terminals. It's better loops." (24:37-24:57)
- Independent field report of the same failure mode (Kyle Jaejun Lee, KRAFTON): a few tmux panes grew to six live contexts and "I'm not running agents anymore. I've become the scheduler, deciding who does what. I'm the memory, holding what every one of them is doing, and I'm the reviewer, checking all of it. One human, three roles, six contexts. It does not scale." ([I Run a Fleet of AI Agents Across Three Machines](../sources/20260708_4kYl2_mqmnQ.md), 00:45-01:28)
- A concrete realization of the manager shape as a **scoped-context org hierarchy**: instead of a flat pile, structure agents as CEO/VP/manager/worker — "real entity types in the system. It is not a cute metaphor." Each is its own agent with its own scoped context and its own approval boundary; context flows down (each layer gets only the slice it needs), results flow back up, and the human reviews only what reaches the top — "instead of holding six contexts in my head, I hold exactly one." The design analogy is how a handful of executives run a company of thousands: they don't hold all of it, they separate context so each person sees only their slice. (20260708_4kYl2_mqmnQ, 01:28-02:12)
- Relationship to the bottleneck: this delegation move is *why* attention becomes the binding constraint — see [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md) (Steinberger frames the same tokens → compute → attention progression).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Treat Human Attention as the Bottleneck for Agentic Work](treat-human-attention-as-the-agentic-bottleneck.md)
- [Agent Managers Orchestrate Editor, Browser, and Background Agents](agent-managers-orchestrate-editor-browser-and-background-agents.md)
- [Fractured Attention Becomes Usable With Delegated Agents](fractured-attention-becomes-usable-with-delegated-agents.md)
- [Run parallel issue agents in sandboxes with review and merge loops](run-parallel-issue-agents-in-sandboxes-with-review-and-merge-loops.md)
- [Manage AI agents like humans with commander's intent](manage-ai-agents-like-humans-with-commanders-intent.md)
- [Converge agent fleets on cluster-scheduling primitives](converge-agent-fleets-on-cluster-scheduling-primitives.md)
- [Externalize agent state to files and reset instead of compact](externalize-agent-state-to-files-and-reset-instead-of-compact.md)

Sources:
- [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](../sources/20260709_pMggiOb18tc.md), 16:51-17:54, 18:56-24:57
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../sources/20260708_4kYl2_mqmnQ.md), 00:45-02:12
