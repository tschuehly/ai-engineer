# Design Private AI Serving Around Verifiable Remote Compute

Summary: Private AI serving should be designed as verifiable remote compute, not as ordinary cloud inference plus a privacy promise. The client should have evidence that sensitive data will be processed only by the expected code path and that operational escape hatches are absent or tightly constrained.

Use when:
- Designing inference for sensitive prompts, personal data, regulated data, or privacy-branded AI features.
- Comparing local-only, ordinary cloud, and confidential remote inference architectures.

Details:
- Apple PCC is framed around the problem that AI may need more compute than a phone can provide, while sending private data to a black-box remote server reduces privacy. (02:23-03:29)
- The talk lists five architectural requirements: stateless computation, enforceable guarantees, non-targetability, no privileged runtime access, and verifiable transparency. (04:02-05:14)
- Enforceable guarantees mean restrictions should be implemented in code and system shape, not only policy; examples include no SSH service, no disk for durable logging, and no production path that bypasses restrictions. (04:20-05:14, 07:33-07:58)
- Privacy-preserving remote inference has operational costs: no SSH and no logging make debugging harder, while avoiding user identification makes fine-grained usage tracking and cost pass-through difficult. (16:59-17:32)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [High-Consequence Data Changes Vendor Trust Requirements](high-consequence-data-changes-vendor-trust-requirements.md)
- [Use local AI workstations when iteration, privacy, or latency dominate](use-local-ai-workstations-when-iteration-privacy-or-latency-dominate.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)

Sources:
- [The Unofficial Guide to Apple's Private Cloud Compute - Jmo, CONFSEC](../sources/20250730_CCsWZ5bJlO8.md), 02:23-05:14, 07:33-07:58, 16:59-17:32
