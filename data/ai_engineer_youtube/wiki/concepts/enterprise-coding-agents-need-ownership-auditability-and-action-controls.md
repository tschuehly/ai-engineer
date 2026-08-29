# Enterprise Coding Agents Need Ownership, Auditability, and Action Controls

Summary: Enterprise coding-agent platforms need explicit answers for security, audit logs, responsibility, ownership, and destructive action control. Broad YOLO-style execution is a poor default when agents can run commands against business-critical codebases.

Use when:
- Reviewing an enterprise coding-agent platform for governance and security readiness.
- Setting policy for destructive commands, audit trails, or responsibility boundaries around agent work.

Details:
- The talk frames Factory as an enterprise platform and points security reviewers toward audit logs, responsibility, ownership, and indemnification questions. (15:09-15:40)
- The example of an agent running `rm -rf` against a codebase is used to motivate responsibility and action-control design, even though the speaker says Factory's agents do not do that. (15:17-15:31)
- The source explicitly warns that broad YOLO mode is probably not a strong enterprise default. (15:40-15:49)
- This governance layer is separate from model capability: enterprises need controls that make action responsibility and evidence inspectable before agent-native workflows can scale. (15:09-15:49)
- **The same requirements read as a boundary rather than a checklist.** Krieger's framing for regulated verticals is that verifiability, audit logging, and data provenance belong to a substrate the agent works *over*, with the free-form generation on top — "finding that right cut line where you have verifiability and audit logging and data provenance here, but not in a way that constrains the kinds of applications that you can build on top, is a lot of the art." Read as a design instruction for enterprise agent platforms: place these controls at a layer the agent cannot route around, rather than as constraints applied to each agent action, or the controls will be traded away for capability one feature at a time. ([Krieger](../sources/20260827_qqrk7CtkuIw.md), 20:42-21:41)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)

Related concepts:
- [Keep Human Review on High-Risk Agent Operations](keep-human-review-on-high-risk-agent-operations.md)
- [Give Code-Executing Agents Isolated Computers](give-code-executing-agents-isolated-computers.md)
- [Record Workflow History for Agent Debugging and Compliance](record-workflow-history-for-agent-debugging-and-compliance.md)
- [Draw the Cut Line Between Verified Data and Free-Form Agent Analysis](draw-the-cut-line-between-verified-data-and-free-form-agent-analysis.md)

Sources:
- [Ship Production Software in Minutes, Not Months - Eno Reyes, Factory](../sources/20250725_iheWKg2Tkrk.md), 15:09-15:49
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 20:42-21:41
