# Ship Managed and Self-Hosted Sandboxes Because Serious Teams Bring Their Own Infrastructure

Summary: The obvious first design for a cloud agent platform is a managed sandbox — compute the user never has to think about, which is the whole point of moving work off the laptop. Warp shipped that, then found it insufficient for exactly the customers who matter most: teams doing serious work already operate their own infrastructure, and their security posture, deployment practices, and existing dev boxes are not things the platform gets to replace. The resolution is not to pick a side but to treat *who operates the compute* as a second axis, orthogonal to whether the platform abstracts it.

Use when:
- Designing where a cloud agent platform runs customer workloads, or scoping a "bring your own compute" request.
- A managed-only agent product is stalling in enterprise or platform-team deals.
- Distinguishing the build-versus-buy sandbox question from the who-runs-it question.
- Estimating what an agent platform must abstract if the underlying environment is not one it controls.

Details:
- **The problem the sandbox exists to solve, restated plainly.** Once agents do "work that was more long-running" than a laptop supports, the first question a platform faces is "where does the agent run if it's not running on a developer's machine?" — and the answer is "an isolated environment in the cloud where agents do this task," which the agent needs "like any developer would." ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 02:35-04:12)
- **The default, and the reason it was the default.** The team's first instinct was hosted sandboxes as "a really easy on-ramp for getting into our cloud agent platform. You didn't have to think about where your compute lived, it was just there for you." That is the managed-hosting case applied consistently: complexity absorbed before it reaches the user. (04:12-04:31)
- **The revision, and the three things that override the on-ramp.** "For teams doing serious work, they're probably managing their own infrastructure. They probably have dev boxes that they need to interact with and so something that is hosted or managed is usually not sufficient. You really need to be able to run agent workloads on infrastructure that people bring so it adapts to their security concerns, their deployment practices, their workflows and preferences on their team." Note what is not in that list: cost, capacity, and latency are the usual arguments for self-hosting and none of them is the one given. The stated reasons are all about *fit with an existing operating model*, which is why a better managed offering does not answer them. (04:31-04:47)
- **The conclusion, framed as more abstraction rather than less.** "We add support for not only managed hosting but also self-hosting to the platform and that is complexity that you abstract away from the user and how the behavior is modeled." The platform's job becomes presenting one agent-execution contract over two very different substrates — which is the cost of this decision and the part the talk does not price. (04:47-05:07)
- **This is a different axis from the wiki's build-versus-buy sandbox guidance.** [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md) argues against writing your own isolation primitives, and Anthropic's version widens it to six production concerns a platform answers together. Neither says anything about *whose account the container runs in*. A team can buy a hardened sandbox technology and still be required to run it inside their own VPC, and a platform that conflates the two questions will hear "we need self-hosting" as "we want to build our own isolation," which is the wrong objection to answer.
- **What self-hosting takes away, by implication rather than by statement.** The wiki's managed-runtime pages assume properties the platform controls end to end: a sandbox that starts in tens of milliseconds ([Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)), egress policy attached to an environment definition and inherited by every instance, and a replacement sandbox spun up mid-run after a failure. On customer infrastructure each of those becomes a negotiation. The source does not discuss which guarantees survive the move, and that gap is the practical question to ask any vendor offering both.
- **Evidence.** A vendor design talk. The claim that managed hosting was insufficient is reported as a product decision, not evidenced with lost deals, adoption numbers, or a description of what self-hosted deployments actually look like. Treat it as a well-motivated requirement rather than a measured finding.

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)
- [Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Production Agent Platforms Need Enterprise Controls](production-agent-platforms-need-enterprise-controls.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md)

Sources:
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 02:35-05:07
