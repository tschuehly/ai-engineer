# Capability-Based Sandboxes Start With No Authority

Summary: A code-mode runtime should begin as an execution environment with no external authority, then receive only the APIs, network access, and state needed for the current task.

Use when:
- Designing sandboxes for model-generated code that will call APIs or manipulate user data.
- Reviewing whether an agent runtime grants broad ambient authority instead of explicit task-scoped capabilities.

Details:
- Pai distinguishes this from wrapping a full container in security controls: start with an environment that can execute code but cannot fetch, call APIs, or access anything else until capabilities are granted. (12:33-13:08)
- Cloudflare's dynamic-worker example uses V8 isolates for fast startup and security hardening, but the transferable pattern is capability exposure rather than a specific JavaScript runtime. (13:08-14:15)
- Recommended defaults include no outgoing fetches, API-only capability exposure, fast ephemeral execution, and full observability into generated code and its actions. (13:30-14:15)
- The language is not the core constraint; JavaScript, Python, WASM, or Lisp-like runtimes still need events, sandboxing, capability-based security, and embeddability for fast ephemeral runs. (17:50-18:17)
- Agrawal states the capability rule as allow-list security: enumerate what generated code may access rather than trying to enumerate all operations it must not perform. If a capability is not granted, it should not exist for the generated code. (08:13-09:57)
- In a dynamic isolate pattern, the trusted worker can pass only specific bindings such as a restricted database query method or logger, set outbound networking to null, and avoid passing secrets into the sandbox. (15:24-18:44)
- Pai and Carey later frame the same primitive (Cloudflare Dynamic Workers) as "eval++": for ~30 years developers were told never to use `eval` and Workers do not even expose it, so running a string of LLM- or user-generated code in a fresh isolate reopens "an entire branch of the tech tree" — but only because the isolate starts with no fetch, no APIs, and no environment variables and can be spun up billions at a time on demand. (SKDJo2CopRs 07:11-08:18, 10:31-11:18)
- The inverted model is stated bluntly: ordinary sandboxes start from a VM/container and add security around it, while a capability sandbox starts from "the only thing you can run is JavaScript, with no access to fetch, no APIs, nothing," then grants explicit capabilities from the outside (e.g., outgoing fetches only to `github.com`), with the recommended default being to block outgoing fetches entirely. (SKDJo2CopRs 08:55-09:36)
- A concrete payoff is server-side generative UI: instead of generating JSON to render ("Jason Bender") because a platform lacks a primitive to render untrusted code, have the model generate HTML or React and render it directly inside the sandbox — safe enough to run on your own servers, not just in a client like Claude Artifacts. (SKDJo2CopRs 12:14-13:11)
- Plugin systems are another fit: Cloudflare's M- CMS builds its plugin system entirely on Dynamic Workers, locking down where plugins run to avoid WordPress-style plugin security incidents. (SKDJo2CopRs 21:31-22:06)
- **The same rule shipped as a per-job manifest for scheduled CI work.** GitHub's agentic workflows apply capability grants to standing automations rather than to a code-execution sandbox: the workflow document's front matter enumerates permissions ("read all"), the tool set, the reachable network destinations, and — the axis a sandbox rarely covers — the write actions the run may perform at all. The motivation is the absence of a supervisor rather than untrusted generated code: "if we're going to be not supervising agents doing things, then we're going to need much stronger guardrails around what they're allowed to do, what they're allowed to read, what they're allowed to write." Worth noting that an allow-list of *writes* with a cardinality bound (see [bound what an unattended automation may emit](bound-what-an-unattended-automation-may-emit.md)) is a capability shape this page's runtime examples do not express. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 07:10-08:34)

- **A denylist's failure mode, observed, as the argument for starting from zero.** AIDAChip told an agent not to write spec files; it wrote them through bash, then `sed` after bash was denied, then `cat` after `sed` was denied — "we're being like a cat chasing a mouse." Each denial named a program while the agent pursued an effect, and the set of programs that can write a file is open-ended. That is the deny-by-enumeration failure this page's default-deny posture avoids by construction: under no-authority-by-default, `cat` is not a hole to be found because it was never granted. Their stated fix — "we block at the source… from system level, not tool by tool" — is the same move, arrived at after three rounds of the enumeration game. ([Mohamed](../sources/20260822_0I6aoPSRzVc.md), 13:36-15:11)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Separate Agent Harnesses From Generated-Code Execution](separate-agent-harnesses-from-generated-code-execution.md)
- [Treat AI-generated code as untrusted code](treat-ai-generated-code-as-untrusted-code.md)
- [Choose isolates or containers by generated-code workload](choose-isolates-or-containers-by-generated-code-workload.md)
- [Build Agents on Addressable Stateful-Serverless Instances](build-agents-on-addressable-stateful-serverless-instances.md)
- [Move Agent Access Control to the Network Layer So the Sandbox Holds No Credential](move-agent-access-control-to-the-network-layer.md)
- [Bound What an Unattended Automation May Emit, Including Emitting Nothing](bound-what-an-unattended-automation-may-emit.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)

Sources:
- [Code Mode: Let the Code do the Talking - Sunil Pai, Cloudflare](../sources/20260419_8txf05vVVl4.md), 12:33-14:15, 17:50-18:17
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 08:13-09:57, 15:24-18:44
- [Why Eval++ Is the Next Great Compute Primitive — Sunil Pai & Matt Carey, Cloudflare](../sources/20260608_SKDJo2CopRs.md), 07:11-13:11, 21:31-22:06
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 07:10-08:34
- [What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip](../sources/20260822_0I6aoPSRzVc.md), 13:36-15:11
