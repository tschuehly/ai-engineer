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

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [MCP gateways create an enterprise root of trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)

Sources:
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md), 17:43-19:41
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 01:22-02:25, 03:33-03:43
