# Sandbox Primitives Are Per Operating System

Summary: A local coding agent's sandbox is not one component but one per platform, built on whatever confinement primitive the OS provides — Seatbelt on macOS, Bubblewrap on Linux — and on Windows OpenAI found no adequate primitive and had to write and open-source a sandbox of its own. Cross-platform support is therefore a per-OS security engineering commitment, not a portability detail.

Use when:
- Scoping what it costs to ship a local agent that executes commands on more than one operating system.
- Estimating the security surface of an agent your team distributes as a desktop or CLI tool.
- Deciding whether to route execution to a remote container instead of confining it locally.

Details:
- Every filesystem interaction in Codex goes through a sandbox layer, and the implementation differs by platform: "on macOS, we use Seatbelt for that, similar to most agents. And on Linux, we use Bubblewrap. On… Windows, it's slightly different where we actually had to build our own custom… open source Windows sandbox. It's in the same GitHub repository if you want to take a look." ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:06-11:37)
- The macOS and Linux choices are described as conventional — "similar to most agents" — which is the useful part of the observation: two of three platforms are a matter of adopting an existing primitive, and the third is not.
- **The Windows case is the finding.** A frontier lab with strong incentives to avoid the work concluded that none of the existing Windows options was adequate: "there's… many reasons why we had to do this, and I could probably fill a whole talk about that," with the alternatives and the reasoning deferred to an external article. The rationale is not given in the talk, so what the wiki can record is the decision and its cost, not the argument. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 11:37-11:57)
- **This qualifies the wiki's standing advice.** [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md) is sound guidance grounded in real escapes, and it is aimed at *server-side* code execution where hardened sandbox products exist and can be bought. A locally installed agent that must confine commands on the user's own machine is a different problem: there is no vendor to outsource to, the primitive has to come from the OS, and on at least one major OS it does not exist in usable form. The honest reading is that the advice holds where a hardened remote sandbox is an option, and that the alternative for local execution is to move execution off the machine rather than to hand-roll confinement.
- A practical consequence for teams shipping local agents: budget the sandbox per platform, and treat "we support Windows" as a separate security review rather than a build-target flag. Where that budget does not exist, the realistic options are to restrict the agent to platforms with a usable primitive, adopt someone else's per-OS sandbox (OpenAI's Windows one is in the Codex repository under the same Apache 2 licence), or [decouple execution into a remote environment](decouple-the-agent-loop-from-the-tool-execution-environment.md).
- Note what the sandbox is *for* here. It is the layer that makes escalation meaningful: an action that hits the sandbox boundary is what triggers the [read-only review subagent](escalate-risky-actions-to-a-read-only-review-subagent.md). Without a confinement primitive there is no escalation event to review, so the approval architecture above it does not exist either. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 13:34-13:50)
- **Provenance.** A vendor description of its own implementation, with no threat model, no comparison of the three sandboxes' guarantees, no discussion of known limitations of Seatbelt or Bubblewrap for this use, and — for the most interesting claim — no reasoning. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), Provenance and Caveats)

Related topics:
- [Security](../topics/security.md)
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)

Sources:
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 11:06-11:57, 13:34-13:50
