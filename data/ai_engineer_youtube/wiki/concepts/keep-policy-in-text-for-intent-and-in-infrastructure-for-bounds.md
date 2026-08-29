# Keep Policy in Text for Intent and in Infrastructure for Bounds

Summary: Agent policy lives in two places and needs both. Text — prompts and context files — carries the reasoning, is cheap to change, and by one operator's report works about 80% of the time, but it is advice with no enforcement. Infrastructure — a proxy that counts, compares, and returns a 403 — enforces without understanding and cannot be argued out of a rule. Text shapes what the agent tries to do; infrastructure bounds how wrong it can go.

Use when:
- Deciding whether a new agent restriction belongs in the system prompt or in the runtime.
- A guardrail exists only as a sentence in a context file, or only as a hard denial with no explanation.
- Reviewing an agent design for prompt-injection exposure on state-changing operations.

Details:
- **The text layer and its honest accounting.** "That's prompts, that's your context files, markdown the agent reads before it can act. And this is where you can explain your why, the intent. We got exactly the same sentence… written down in a markdown file. It works about 80% of the time." Upside: "very cheap to change and you can explain the reasoning." Downside: "you have to garden it because the files can grow over time, and at the end of the day it's just advice. Text can shape the intent but there is no enforcement anywhere." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 15:30-16:05)
- **The infrastructure layer, and what its narrowness buys.** "The proxy is not reading the prompt. It doesn't know why the agent wants to do something and it doesn't really care. It will see a delete happening, it'll see a budget being crossed and it'll simply return a 403, and that's the whole conversation really. It's narrow. It's deterministic. It counts, compares, it can allow a delete or deny. What it can't do is explain the why, and a clever prompt injection cannot really talk it out of the rule itself." (16:05-16:34)
- **The division of labor in one line.** "The text shapes what an agent is trying to do and infra is bounding how wrong can it go." (16:35-16:40)
- **The runtime arrangement.** "Every agent session has its own proxy running right next to it. The agent starts off by reading its own context file — the markdown files — that's the text layer, and every outbound call goes through the proxy after that point, which is the infrastructure layer." Text is read once at session start; infrastructure is in the path of every call. (16:42-16:59)
- **Why the text layer is kept rather than merely tolerated.** The wiki's [substrate-blocking page](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md) concludes from AIDAChip's `sed`-then-`cat` escalation that the model-behavior layer "was never a layer at all" for a hard prohibition, and that is compatible with this page rather than contradicted by it — both agree text does not enforce. The addition here is a reason to keep writing it anyway: text is the only layer that can carry the *why*, and a 403 cannot tell an agent what to do instead. The two failure modes are different, and worth separating when you audit a guardrail. A rule that exists only in text will be violated some fraction of the time; a rule that exists only in infrastructure will be repeatedly rediscovered by an agent that has no idea why it is being denied, burning turns against a wall. The trip-wire loop in the same talk is where those two meet: the enforcement fires, and [the fix is one or two lines of context](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md).
- **The prompt-injection argument is the sharpest reason for the split.** An enforcement point that reads the prompt inherits the prompt's attack surface. A counter and a comparison do not, which is the same property the wiki records for [deterministic guardrails around sensitive tool calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md) — and the caveat recorded there applies unchanged: a proxy in the path of every call is a dependency with its own availability, so fail-open versus fail-closed is a decision this talk does not state.
- **Evidence limits.** "About 80%" is the only number attached to any layer in the talk and it has no denominator, no task definition, no measurement window, and no method — it is an operator's impression of how often a written instruction is followed. It is worth recording because so few sources quantify the text layer at all, and worth distrusting for exactly the same reason. Nothing is reported about the infrastructure layer's own error rate: no count of 403s, no false denials, and no case where the proxy blocked something the agent legitimately needed.

Related topics:
- [Security](../topics/security.md)
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Stamp Agent Identity at the Proxy, Because a Claimed Identity Resets the Budget](stamp-agent-identity-at-the-proxy-because-a-claimed-identity-resets-the-budget.md)
- [Block the Capability at the Substrate, Because Denying a Tool Only Denies a Name](block-the-capability-at-the-substrate-because-denying-a-tool-only-denies-a-name.md)
- [Layer agent permissions across model behavior, harness parsing, and sandboxing](layer-agent-permissions-across-model-behavior-harness-parsing-and-sandboxing.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [Prefer Trip Wires to Allow Lists, Because Only One of Them Learns](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md)
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 15:30-16:59
