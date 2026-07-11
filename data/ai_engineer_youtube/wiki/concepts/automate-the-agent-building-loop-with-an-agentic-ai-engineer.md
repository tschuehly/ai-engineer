# Automate the Agent-Building Loop With an Agentic AI Engineer

Summary: Turn the coding-agent loop on the task of building agents themselves — run spec → build → evaluate → ship (offline) and monitor → diagnose → optimize (online) as agentic stages under an orchestrator, with an eval suite as the termination gate, so human review stops being the throughput bottleneck once you run many agents.

Use when:
- Deciding how to scale from a handful of hand-tuned agents to tens or hundreds without human review becoming the limit.
- Structuring the full lifecycle of an AI feature (specification, build, evaluation, deployment, monitoring, diagnosis, optimization) rather than just prompting one agent.
- Choosing what to automate vs keep manual in an agent-improvement pipeline.

Details:
- The thesis: the "hot topic" loop for building software agentically applies equally to building AI agents, giving an "Agentic AI Engineer" — a multi-agent team steered by an orchestrator across spec, build, evaluate, diagnose, monitor, and optimize. 00:18-00:40
- Two connected loops: an **offline loop** (iterate, test, evaluate, improve before deploy) and an **online loop** where a deployed agent's traces are monitored, diagnosed, and fed back into optimization to produce multiple agent versions. 00:43-01:12
- Doing the loop by hand is slow — issue → implement (maybe vibe-code it) → generate samples → read traces → ship/AB-test, all reviewed manually — so "the bottleneck basically becomes the human review and the human building time," which can't scale to rolling out hundreds of agents. 01:18-02:12
- Running each stage agentically is the throughput lever: it fits many more improvement cycles into the same time window once you pass a certain number of agents/AI features. 02:33-02:59
- The stages, treated like current software practice: spec (responsibilities, functions, conditional decisions) → build (realize the spec in a chosen harness/framework, e.g. a Claude Code or codex agent) → evaluate (clear evaluations = "the equivalent to unit tests for coding") → ship (a code update, agent-platform update, or local harness) → monitor (trigger conditions from trace volume or daily/weekly jobs) → diagnose (structured root-cause analysis of collected failures) → optimize (specific changes/"mutations" for the found failure modes) → repeat. 02:33-05:52
- Two entry paths: a cold start that designs from scratch via spec + conceptualization, and an existing-feature path where the agent already runs and you optimize over what exists. 06:00-07:07
- Keep the spec implementation-independent so the target platform is a portable choice: the agent-framework space changes rapidly and a harness may lack a capability or hit a roadblock you must wait on the framework to fix, so stay flexible and pick the best harness — new "agent loop run-time" harnesses like Hermes and deep agents keep shipping. 08:53-11:08
- Eval-driven development (EDD) is the TDD-equivalent that supplies the agent's termination condition — "when is an AI feature or an agent good enough?" — so the job becomes "designing these loops with a clear eval or termination gate." 11:16-11:46, 14:56-15:12
- The loop closes on itself: new eval criteria derived from diagnosed production failures become part of the spec and part of the agent, so both grow with production usage and the agent scores better as it sees more real data. 23:16-24:38
- Productized as Mutagent: two research-preview agents — an evaluator agent (builds the eval set/dataset) and a diagnostics agent (analyzes production traces) — connected through an orchestrator in your coding environment, with connectors to trace/incident sources (Langfuse, local Claude transcripts, exported JSONL, ticketing, Slack) and target platforms (an auto-raised GitHub PR, edits to agent `.md` files, or a managed deployment). 24:58-26:52

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Diagnose Agent Failures With Code-Checkable Indicators and Sampling](diagnose-agent-failures-with-code-checkable-indicators-and-sampling.md)
- [Operate Agent Products as the Missing Post-Launch Layer](operate-agent-products-as-the-missing-post-launch-layer.md)
- [Staff Agent Operations With a Team of Agents](staff-agent-operations-with-a-team-of-agents.md)
- [Route Agent Repairs to the Right Layer With the Smallest Durable Change](route-agent-repairs-to-the-right-layer-smallest-durable-change.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Spec-Driven Agent Validation Goes Beyond the Test Set](spec-driven-agent-validation-goes-beyond-the-test-set.md)

Sources:
- [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](../sources/20260629_pSto5YaNGUo.md), 00:18-26:52
