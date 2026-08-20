# Bound What an Unattended Automation May Emit, Including Emitting Nothing

Summary: Agent controls almost always bound the input side — what the agent may read, call, and reach. An unattended automation also needs its *output* side bounded: an allow-list of the write actions it may perform, a cap on how many of each, and an explicit grant of permission to produce nothing at all. The first two contain an injected agent; the third contains a well-behaved one that feels obliged to have found something.

Use when:
- Scheduling an agent to run without a human present, where nobody is there to reject its first bad action.
- An automation can open pull requests, file issues, comment, or notify, and the blast radius question is "how many?" rather than "which repository?"
- You are about to run dozens of standing automations against the same repo or the same person's attention.
- Reviewing a proposed agent job whose spec never says what it should do on an uneventful day.

Details:
- **The declaration.** GitHub's Agentic Workflows put a `safe outputs` block in the workflow's front matter, "basically saying these are the only things that the agent is allowed to write." Gazit's dependency-upgrade workflow declares exactly one: create a pull request. Everything else the agent might want to emit is simply not a capability it has. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 08:16-08:28)
- **Cardinality is part of the grant, and the reason is injection.** The declaration is not "may open pull requests" but `pull-request: single` — "because I don't want the agent to get prompt injected to create 500 pull requests. That would be a denial of service." This is the piece most permission models omit: a per-kind allow-list with no count is still a fan-out primitive in the hands of whoever controls the untrusted text the agent reads. The upgrade workflow reads changelogs and release notes from the open web by design, so the injection path is the job description. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 08:26-08:34)
- **Permission to do nothing, and why it is not trivially satisfied.** "I explicitly said you're allowed to do nothing, right? Which sounds silly, but it actually matters because in a world where I have lots of automations, the last thing I want is noise. I don't want the agents denial of servicing me." A daily job with no declared null outcome is under quiet pressure to justify its run; the failure is not a wrong action but a stream of technically-valid ones. The self-DoS framing is the useful part — the same word covers the injected fan-out and the well-behaved chatterbox, because the victim in both cases is the owner's attention. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 08:35-08:48)
- **This is a different axis from the input-side controls, and both are needed.** Network allow-lists, tool allow-lists, and sandbox capabilities all answer "what can it reach"; safe outputs answer "what can it leave behind." An agent perfectly confined to reading `npmjs.com`, `github.com`, and the Astro docs can still be talked into emitting five hundred artifacts, because emitting is the one thing it was hired to do. In the same front matter Gazit declares read-all permissions, the allowed tool set, and the allowed network destinations alongside safe outputs — the point is that the fourth declaration is not implied by the first three. See [restrict agent internet access with allow-lists](restrict-agent-internet-access-with-allowlists.md) and [capability-based sandboxes start with no authority](capability-based-sandboxes-start-with-no-authority.md) for the input half. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 07:50-08:34)
- **The failure this prevents has already been observed without it.** A team that gave agents tracker access without wiring the authority first reported agents "not wired correctly" filing hundreds of issues in a couple of weeks ([wire issue-filing authority before giving agents a tracker](wire-issue-filing-authority-before-giving-agents-a-tracker.md)). That is the same event as the injected 500 pull requests, arrived at by a benign route — which argues for expressing the cap as a runtime bound rather than as an instruction the agent is asked to observe.
- **What is not specified.** The talk says nothing about what happens when the cap is hit: whether the run fails, silently truncates, or reports that it wanted to do more. That distinction matters, because a silent truncation on an injected run and a silent truncation on a legitimately large batch look identical from the outside. Nor is there a figure for how often the do-nothing branch actually fires in practice, which is the only measurement that would show whether the permission is doing any work.
- **Related bound, different mechanism.** Where this page caps a single automation's output, [contain retry amplification before it becomes a compute incident](contain-retry-amplification-in-agent-loops.md) caps the multiplicative case, where each retry spawns further work. An automation fleet needs both: a per-run emission ceiling and a loop that cannot self-multiply.

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Security](../topics/security.md)

Related concepts:
- [Wire Issue-Filing Authority Before Giving Agents a Tracker](wire-issue-filing-authority-before-giving-agents-a-tracker.md)
- [Restrict Agent Internet Access With Allowlists](restrict-agent-internet-access-with-allowlists.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [Answer Unaddressed Questions Behind a Confidence Gate](answer-unaddressed-questions-behind-a-confidence-gate.md)
- [Keep Humans Aligned With Proactive Agent Work](keep-humans-aligned-with-proactive-agent-work.md)
- [The Markdown Workflow Is the Source; the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)

Sources:
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 07:50-08:48
