# Give Code-Executing Agents Isolated Computers

Summary: Code-executing agents should run in a dedicated container, VM, or OS sandbox and return reviewable artifacts rather than sharing the user's privileged machine environment.

Use when:
- Choosing where a coding agent should run commands, install dependencies, or edit files.
- Designing local and hosted Codex-style execution environments.

Details:
- OpenHands runs agents inside Docker containers by default so autonomous shell work is separated from the user's workstation and cannot delete or mutate the user's home directory. 06:44-07:05
- Container isolation does not solve external authority; when agents receive GitHub tokens, AWS access, or other third-party credentials, those credentials should be tightly scoped and least-privilege. 07:08-07:23
- The talk recommends giving the agent "its own computer" as the first safeguard, especially for local runs. Codex in ChatGPT is described as spinning up a fully isolated container and producing a PR at the end. 04:25-04:41
- Local Codex CLI-style agents still need appropriate sandboxing, such as containerization, app-level sandboxing, or OS-level sandboxing. 04:41-05:02
- Codex CLI examples include macOS Seatbelt policies and Linux sandboxing built with seccomp and Landlock to support unprivileged execution and reduce privilege-escalation risk. 06:09-07:42
- The isolated environment still needs the right dependencies and task access; isolation should not prevent validation, but it should limit second-order consequences outside the intended workspace. 06:09-08:24
- Burazin describes the positive product side of isolation: a sandbox can become an agent-native runtime when the agent can quickly create, control, clone, and use the environment through APIs and preloaded tools. 08:12-09:53

- **The strongest argument for isolation is not what the agent was given but what it can find.** Superconductor demotes the convenience case — "lid anxiety," people running through airports with laptops open — as real but "not the most important reason to do this," and puts the credential surface first: developer laptops, "unless you have like impeccable hygiene, probably have a bunch of stuff on it that you don't want the LLMs or agents to have access to." The failure mode is an obedient agent, not a rogue one: told to wipe staging, it "finds a token on your laptop that it can use and it thinks it's working with staging, but actually it's production." Per-tool permission scoping cannot cover this, because you cannot scope a credential nobody enumerated — see [a developer laptop is an ambient-credential surface](a-developer-laptop-is-an-ambient-credential-surface.md). Two qualifications: the frequency claim is explicitly weak ("I'm not trying to say this is happening constantly, but it still happens"), and moving execution to a vendor's cloud inverts the trust boundary rather than removing it, which the talk does not address. ([Arjun Singh](../sources/20260809_OL7kfezynJM.md), 09:13-11:23)

- **A non-security reason to give the agent a filesystem, from an operations vendor.** Resolve AI's background agents run "in the cloud. So if you close your laptop, it's okay. Runs inside of a sandbox, so it has kind of a file system underneath it. This allows it to sort of self-organize a lot of its work." The sandbox is containment in the sources above and scratch space here — a place for an agent working an open-ended production task to keep notes and intermediate state across a run. Both justifications point at the same artifact, which is why the sandbox is worth provisioning even for agents that only read. ([Justin Smith](../sources/20260809_vSx5IULvBns.md), 12:19-12:33)
- **The setup bill scales with repository count, and repository layout is therefore a sandbox-cost decision.** "If you're building a sandbox environment to run sort of a full AI factory, it also takes more time to clone repos and get everything set up." Each isolated environment pays clone-and-provision again, so the cost compounds precisely in the many-parallel-agents regime that isolation is meant to enable — which is one of the strongest remaining arguments for consolidating a multi-repo estate. See [Multi-Repo Cost Has Moved From Navigation to Verification](multi-repo-cost-has-moved-from-navigation-to-verification.md). ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 15:36-15:44)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)
- [Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [A Developer Laptop Is an Ambient-Credential Surface](a-developer-laptop-is-an-ambient-credential-surface.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Give Unowned Operational Work a Trigger](give-unowned-operational-work-a-trigger.md)
- [Multi-Repo Cost Has Moved From Navigation to Verification](multi-repo-cost-has-moved-from-navigation-to-verification.md)

Sources:
- [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](../sources/20250725_o_hhkJtlbSs.md), 06:44-07:23
- [OpenAI on Securing Code-Executing AI Agents - Fouad Matin (Codex, Agent Robustness)](../sources/20250730_w7IMuYsBNr8.md), 04:25-08:24
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 08:12-09:53
- [Multiplayer agentic engineering — Arjun Singh, Superconductor](../sources/20260809_OL7kfezynJM.md), 09:13-11:23
- [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](../sources/20260809_vSx5IULvBns.md), 12:19-12:33
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 15:36-15:44
