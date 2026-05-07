# Bind Sensitive Payloads To Remote Attestation Claims

Summary: Remote attestation can make sensitive payload release conditional on a server proving its hardware and software state. The client receives signed claims and a public key, checks the claims against its trust policy, then encrypts data so decryption works only while the server still matches those claims.

Use when:
- Sending high-sensitivity AI requests to a remote service that should not be trusted as a black box.
- Designing confidential inference handshakes, enclave-backed services, or client-side trust checks.

Details:
- The abstract attestation flow starts with the client asking what the server is running; the server replies with signed claims and a public key. (10:32-10:40)
- Claims can describe genuine hardware, GPU, bootloader, operating-system version, and software set; the client decides whether those claims satisfy its trust policy. (10:40-11:08)
- The public key is tied to the signed claims, so later encrypted data can be decrypted only if the server is still matching the attested state. (11:16-11:45)
- The talk maps this to PCC: the iPhone requests an attestation package through an anonymizer, checks whether it trusts the server contents, and sends data only after that check. (13:23-14:25)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Design Private AI Serving Around Verifiable Remote Compute](design-private-ai-serving-around-verifiable-remote-compute.md)
- [Use Transparency Logs To Audit Attested AI Binaries](use-transparency-logs-to-audit-attested-ai-binaries.md)
- [Short-lived IdP-derived tokens reduce standing MCP access](short-lived-idp-derived-tokens-reduce-standing-mcp-access.md)

Sources:
- [The Unofficial Guide to Apple's Private Cloud Compute - Jmo, CONFSEC](../sources/20250730_CCsWZ5bJlO8.md), 10:32-11:45, 13:23-14:25
