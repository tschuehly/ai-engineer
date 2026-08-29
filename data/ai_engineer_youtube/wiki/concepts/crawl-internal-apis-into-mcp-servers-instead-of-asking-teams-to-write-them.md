# Crawl Internal APIs Into MCP Servers Instead of Asking Teams to Write Them

Summary: Uber had thousands of internal APIs and none were agent-accessible, so instead of asking every service team to author an MCP server, a crawler reads the API surface and projects it into MCP servers behind the gateway with one config change. Tool coverage becomes a generated-supply problem rather than a per-team authoring backlog, and the same gateway hosts third-party SaaS servers with centralized token exchange so there is one install path for everything.

Use when:
- Agent tool coverage is limited by how many teams have written an MCP server, not by what the agent could usefully call.
- Deciding whether MCP servers should be hand-authored artifacts or generated projections of an existing interface.
- Onboarding SaaS tools whose auth setup is being repeated by every engineer individually.

Details:
- **The starting condition, which is the common one.** "Last year when we started on this journey we had thousands of internal APIs but none of them are agent accessible out of the box, and we had so many other SaaS tools and each one of them have different way to authenticate, different way to set up, which is a lot of hassle for everyone." ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 03:39-04:05)
- **Generation, not authoring.** "We have an automated crawler that looks at our internal APIs and projects all of these into MCPs with one single config change." The unit of work for a service team drops from writing and maintaining a server to flipping a config. (04:05-04:21)
- **The same treatment for third-party servers.** "We do the same thing even for our SaaS MCPs whether it's Google, Slack, Jira, all of this — they go through the MCP gateway. We host them, we do the token exchange." Hosting other people's servers centrally is what collapses N per-engineer auth setups into one; see [Vault and Exchange Tokens for Scoped Upstream Agent Access](vault-and-exchange-tokens-for-scoped-upstream-agent-access.md). (04:21-04:37)
- **The payoff is uniformity, and it is a precondition for everything downstream.** "For all the engineers, they go through one single entry point, one common way to install any MCPs." That uniformity is what makes the later token-efficiency migration possible at all — a single discovery server, a CLI projection, and an auto-installed code-mode skill all assume one inventory and one install path. See [Stage the MCP Token Tax Down](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md). (04:37-04:51)
- **The tension this creates with tool-design advice.** The wiki's standing position is that good agent tools are designed for the agent's task, not mirrored from an existing API — a generated projection of "thousands of internal APIs" is the mirror-the-API approach at maximum scale, and it is presumably why the same organization ended up needing four rounds of token optimization on top. Read the two together as a sequence rather than a contradiction: crawl for coverage, then measure which projections dominate token spend and hand-optimize those. The crawler decides what is reachable; the top-consumer list decides what is worth designing.
- **Caveat.** Nothing is reported about quality — no description of how tool descriptions or schemas are generated, whether the crawler produces usable names, how deprecation or API drift propagates, or what fraction of the 1,000-plus resulting tools are ever called. The claim supported here is that coverage can be generated cheaply, not that generated tools are good ones.

Related topics:
- [Tools](../topics/tools.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode](stage-the-mcp-token-tax-down-direct-omni-cli-then-code-mode.md)
- [Vault and Exchange Tokens for Scoped Upstream Agent Access](vault-and-exchange-tokens-for-scoped-upstream-agent-access.md)
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)
- [State the Model Gateway as Three Invariants, Not a Feature List](state-the-model-gateway-as-three-invariants-not-a-feature-list.md)
- [Gateway Platform Primitives Let Teams Focus on MCP Business Logic](gateway-platform-primitives-let-teams-focus-on-mcp-business-logic.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 03:39-04:51
