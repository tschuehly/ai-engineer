# Externalize Agent State to Files and Reset Instead of Compact

Summary: When a long-running agent's context window fills, the default move is to compact (summarize history in place), but compaction is slow, you cannot choose what survives, and whatever it drops is gone. The more durable pattern is to keep the agent's real state in files it writes for itself (mission, status, and a handoff of the actual work product) and, when the window fills, *reset* — clear the context completely and let the agent re-read its own files — so work survives not just a context wipe but a machine crash.

Use when:
- Running an agent long enough that its context window fills repeatedly.
- Deciding between compaction and a clean reset as the context-recovery move.
- Designing agents that must survive process death, credential loss, or a machine restarting mid-task.

Details:
- Kyle Jaejun Lee (KRAFTON) calls this "the single most practical thing I learned all year": "When that window fills up, the built-in move is to compact… I stopped doing it. It's slow. I can't choose what survives. And whatever it throws away is just gone. So instead, I don't compact, I reset." (02:44-02:58)
- Reset is literal: "right inside Claude, I clear the context completely. And then it just reads back the handoff and the history files it wrote for itself and picks up exactly where it left off." (02:58-03:08)
- The precondition that makes reset safe is externalized state — the state does not live only in the model. Each entity gets its own workspace on disk: shared context everyone must honor in `shared`, machine-bound state under `machines`, and inside each workspace the mission, the current status, and a `handoff` folder holding the actual work product passed along. "The state lives in files. It is not trapped inside one model." (02:12-02:42)
- The payoff is failure-tolerance, not just token headroom: "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model." (03:08-03:20)
- Crash recovery follows for free: when a laptop lost power and restarted with jobs in flight, a single boot command (`overlord boot`) brought the whole fleet "straight back up because all the state was sitting in files." (05:50-06:04)
- Contrast with intentional compaction: Dex Horthy's approach compresses useful state into a *reviewed Markdown artifact* the next agent starts from, preserving exact files and line numbers — see [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md). Both externalize context out of the live window; the difference is whether the human curates one compressed summary (Horthy) or the agent maintains standing self-authored files it re-reads after a full clear (Lee). Reset trades the risk of a lossy in-place summary for the discipline of keeping state complete on disk.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Offload Long-Horizon Agent State Outside the Context Window](offload-long-horizon-agent-state-outside-the-context-window.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Use immutable versioned state for agent handoffs](use-immutable-versioned-state-for-agent-handoffs.md)
- [Do not treat long context as durable model memory](do-not-treat-long-context-as-durable-model-memory.md)
- [Converge agent fleets on cluster-scheduling primitives](converge-agent-fleets-on-cluster-scheduling-primitives.md)

Sources:
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. - Kyle Jaejun Lee, KRAFTON](../sources/20260708_4kYl2_mqmnQ.md), 02:12-03:20, 05:50-06:04
