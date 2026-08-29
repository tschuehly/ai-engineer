# Treat AI-generated code as untrusted code

Summary: AI-generated code should be handled like unaudited code from an anonymous internet source, because hallucination, over-helpfulness, and prompt injection can all produce dangerous behavior without the model being intentionally malicious.

Use when:
- Designing any product feature that executes code written by an LLM or agent.
- Reviewing whether a generated-code workflow is relying on model intent instead of runtime boundaries.

Details:
- Running generated code directly in an application gives it the same filesystem, environment variable, network, database, and API-key access as the host process unless the runtime removes those capabilities. (01:45-02:59, 06:01-06:48)
- The baseline failure mode is not only malicious code: hallucinated imports, recursive functions without base cases, and infinite loops can crash services or consume compute. (03:08-04:01)
- Over-helpful generated code can read environment variables or secrets while trying to configure a database connection; the resulting sensitive-data exposure is still a security failure even when the model had no hostile intent. (04:01-04:54)
- Direct and indirect prompt injection can steer generated code toward exfiltration when user input, web pages, or documents become part of the prompt context. (04:57-05:58)
- A practical generated-code checklist includes default-deny network access, explicit capabilities, per-user sandboxing, resource limits, secrets outside the sandbox, cleanup, audit logs, and validation before execution. (33:00-35:24)

- **Two different senses of "untrusted" are in circulation, and they prescribe different things.** This page's sense is *runtime containment*: the code may execute, so remove its capabilities. Sonar's "zero trust" is a *verification* claim about the same code before it runs — "the code could really have come from anywhere. It could still be written by a human, it could be written by an AI," so apply "a similar comprehensive regime to verify that code that works the same no matter how that code was written." The prescriptions diverge on provenance: sandboxing exists precisely because the code is generated and about to run unreviewed, while the verification sense argues *against* an AI-specific path and for one regime over all code. They are complementary rather than competing — a sandbox does not tell you whether the code is right, and static analysis does not stop a hallucinated import from opening a socket — but a policy that says "we treat AI code as untrusted" should say which one it means. See [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md). ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 09:23-10:00)

- **The doctrine's logical endpoint: stop trusting the code and require it to arrive with a certificate.** Pant's framing makes untrustedness structural rather than a policy choice — "humans own the specification and machines own the code and proof" — and answers the throughput problem this page's manual precautions cannot: "none of these can say for all inputs the code is correct," whereas a machine-checked proof does, with "you only need to trust the small kernel" as the entire remaining trust assumption. What it does not buy is a blanket clearance: the certificate covers exactly the property stated, so untrusted-by-default still applies to everything the specification did not say. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 00:37-00:42, 02:04-02:10, 04:03-04:14)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Run Agent-Written API Code Inside Programmable Sandboxes](run-agent-written-api-code-inside-programmable-sandboxes.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)
- [LLM Attack Surfaces Span Prompts, Context, Retrieval, Tools, and Actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)
- [Verify Generated Code With a Method the Generator Does Not Share](verify-generated-code-with-a-method-the-generator-does-not-share.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)

Sources:
- [Why, and how you need to sandbox AI-Generated Code? - Harshil Agrawal, Cloudflare](../sources/20260408_AHtGAgQ0Q_Q.md), 01:45-06:48, 33:00-35:24
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 09:23-10:00
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 00:37-00:42, 02:04-02:10, 04:03-04:14
