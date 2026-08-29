# Build Internal AI Engineering Platforms When Off-the-Shelf Tools Lack Enterprise Context

Summary: Large organizations often need custom AI engineering platforms because their codebases, service catalogs, review systems, and operational tools require context and integration that generic agent products cannot infer.

Use when:
- Deciding whether to buy a coding-agent product or build internal agent infrastructure.
- Designing enterprise AI engineering platforms around monorepos, service discovery, review, and on-call systems.

Details:
- The source describes large companies building custom background coding agents integrated with monorepos, MCP gateways integrated with service discovery, retooled on-call systems, and code-review systems that categorize changes by risk. (17:43-18:46)
- Internal AI platform work can be a lower-risk place to build hands-on AI competence before shipping customer-facing AI features that may not be wanted. (18:56-19:12)
- Large codebases may never fit in a context window, so custom retrieval, context, and workflow integration can outperform off-the-shelf vendor behavior. (19:12-19:25)
- The transcript also notes an incentive risk: "AI" labeling can unlock funding for developer-platform work, so teams should still justify internal platforms by context, integration, and workflow needs rather than buzz. (19:25-19:41)

- **Three concrete build reasons, and a way to keep the decision under measurement afterwards.** Uber's are: unsupported tooling ("we currently use Phabricator… most of the solutions do not provide support for Phabricator"); loop parity, so that the inner loop and the pull request are reviewed by one service and "our agents are getting the same code review, the same rules, everything applied as our humans do"; and distributed ownership, since with hundreds of teams "we can't have centralized management of our code reviews, our customizations, and our rules, and even the knowledge that goes into those code reviews," which requires plugging into the existing ownership model rather than replicating it externally. The practice worth copying regardless of which way the decision goes: they keep third-party review systems pluggable as generators inside their own pipeline "so that we can compare ourselves to what's available more broadly," which turns a one-time build-versus-buy verdict into a standing comparison on their own diffs. They do not report what it showed. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 01:22-02:25, 03:33-03:43)
- **What the platform can buy and what it cannot.** Touil's centralized skills platform has a concrete buy list — searchable catalog with metadata, an MCP over the catalog plus a CLI to pull into an IDE or sandbox, inter-skill dependencies, versioning and lifecycle, access control, evaluation and observability — and then an explicit stop: "all of this is actually play around a governance, and this is where technology stop solving the problem. So you figure out all of this, all good — now who's going to govern this?" The answer is named humans, "your architects, your engineer leads, infra leads etc, and cyber leads actually sitting down owning part of those domains." ([Touil](../sources/20260828_M05vON8i0aI.md), 13:44-15:17) He also expects the internal-developer-portal vendors to absorb the catalog half within months (18:40-19:13), which sharpens the build-versus-buy line: the mechanics are commoditizing, the domain carve is not. Nothing in the talk is measured, and the prescribed end state is also the kind of engagement the speaker's firm sells.

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)

Sources:
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md), 17:43-19:41
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 01:22-02:25, 03:33-03:43
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 13:44-15:17, 18:40-19:13
