# Embed Architecture Governance Into Developer Workflows

Summary: Architecture governance should be available as workflow-embedded AI guidance, not only as periodic review boards. The goal is to scale architecture expertise while preserving developer autonomy and alignment.

Use when:
- Designing shift-left architecture controls for teams using coding agents or coding copilots.
- Replacing slow architecture-review gates with contextual guidance that still enforces standards.

Details:
- As organizations shift decisions left to developers, architecture expertise and standards often do not scale with that empowerment. (09:06-09:39)
- The source names the governance paradox: autonomy without alignment creates chaos, while gates without autonomy kill productivity. (10:42-10:51)
- A useful copilot should provide conversational guidance, tailor-fit designs, expert Q&A, and built-in policy awareness inside the developer workflow rather than sending developers to a separate tool. (10:19-10:38, 17:32-18:49, 22:12-22:34)
- The architecture-review process can move from periodic architecture-guild meetings toward alignment by design, where architecture guidance is baked into every AI recommendation to developers. (19:24-20:30)
- The suggested rollout is incremental: pick a portfolio area, build the digital twin, tie recommendations to specific business outcomes, pilot autonomous guidance with one team, and scale after ROI is proven. (25:35-26:33)
- **Composed policy skills as the pulled-at-run-time form of the same idea.** Touil's worked example composes a data-retention-policy skill with disclosure standards, GDPR rules, and fill-in templates, all "pulled automatically on the runtime by the regulatory disclosure review workflow," so that "any data, any feature that is built across your web, mobile, different applications across your organizations is really respecting these rules." The run produces a deterministic outcome, "audit reports that you can actually store," identified improvements, and a loop back into the codebase. ([Touil](../sources/20260828_M05vON8i0aI.md), 09:57-11:20) The governance artifact and the audit trail are the same object here, which is what distinguishes it from a policy document that is checked against after the fact. Illustrative — no deployment or measurement is shown.

Related topics:
- [Architecture Copilots](../topics/architecture-copilots.md)
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use human judgment gates for high-risk agent code changes](use-human-judgment-gates-for-high-risk-agent-code-changes.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)

Sources:
- [AI Copilots for Tech Architecture: The Highest-ROI Use Case You're Not Building - Boris B., Catio](../sources/20251124_QRWdapxMdSY.md), 09:06-10:51, 17:32-20:30, 22:12-22:34, 25:35-26:33
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 09:57-11:20
