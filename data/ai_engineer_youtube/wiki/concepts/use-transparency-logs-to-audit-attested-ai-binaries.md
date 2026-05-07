# Use Transparency Logs To Audit Attested AI Binaries

Summary: Transparency logs turn private remote inference from a one-off attestation into an auditable release process. Public signed records of binary hashes let reviewers inspect deployed artifacts and let clients reject attestation claims that do not correspond to the append-only log.

Use when:
- Designing a confidential AI service where users or auditors need evidence about what code is running.
- Connecting build provenance, binary review, and runtime attestation for sensitive inference.

Details:
- The talk describes a transparency log as records for each software release or component, including a signer and a hash of the binary or compiled source artifact. (11:52-12:20)
- Reviewers can inspect public binaries offline and develop confidence in their behavior before clients see matching attestations at runtime. (12:23-12:45)
- Runtime attestation should be checked against the log; an attestation not present in the log indicates the system or connection should be treated as compromised. (12:47-13:14)
- Append-only Merkle-tree-style logs matter because a limited writer set and tamper-evident history prevent silent replacement of prior release records. (13:07-13:14)
- Open-source code and reproducible builds strengthen the pattern because reviewers can link source to binary instead of relying only on black-box binary testing. (18:57-19:10)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Bind Sensitive Payloads To Remote Attestation Claims](bind-sensitive-payloads-to-remote-attestation-claims.md)
- [Design Private AI Serving Around Verifiable Remote Compute](design-private-ai-serving-around-verifiable-remote-compute.md)
- [Govern MCP tool calls with tool-level policy and end-to-end traces](govern-mcp-tool-calls-with-tool-level-policy-and-end-to-end-traces.md)

Sources:
- [The Unofficial Guide to Apple's Private Cloud Compute - Jmo, CONFSEC](../sources/20250730_CCsWZ5bJlO8.md), 11:52-13:14, 18:57-19:10
