# Make Regulated-Data Failures Architecturally Impossible

Summary: Treating regulated data as a runtime problem — redact it in the log, mask it in the dashboard — leaves a system that depends on every policy being followed. The architectural version removes the data at the pipeline boundary so the failure has nothing to act on: "a developer opens a dashboard, there's nothing to redact. The PHI was never there."

Use when:
- Designing the data plane for an application that handles PHI, PII, or any regulated category, before the first pipeline is built.
- A compliance requirement is being proposed as a policy, a review step, or a redaction filter, and you want to know whether it can instead be made structurally impossible to violate.
- Deciding what non-production environments and geographically distributed teams are allowed to reach.

Details:
- **Policy and architecture do different jobs.** "Protecting PHI takes both policy and architecture. Policy tells you what to protect and architecture makes sure that it actually happens." The distinction is what makes the pair non-redundant: policy is the specification, architecture is the enforcement. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 03:38-03:49)
- **Strip at ingestion, not at display.** Most teams treat PHI as a runtime problem, "something to redact when a log gets written to a dashboard. That's the reactive version." The architecture version "strips PHI at the pipeline boundary. At ingestion, before it ever reaches the data lake. By the time the data is stored, the PHI is gone." Every downstream redaction requirement then evaporates, because there is no downstream copy. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 03:49-04:26)
- **No pipes between production and non-production.** They "stay completely separate. No pipes in between, because even a single pipe is all that it takes for member data to leak into a dev environment." The reasoning is the same shape: a pipe that exists is a pipe that can carry the wrong payload once. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 04:28-04:46)
- **Access is scoped by role *and* geography.** "Access depends on two things: your role and your geographic region." Distributed teams are normal, but PHI access is "a certification, a policy that is applied to specific regions only," and "an engineer outside the regulated region cannot reach raw PHI at all." The geographic axis is the one teams tend to omit when they model access as roles alone. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 04:54-05:15)
- **Compliance is a design input, not an overlay.** HIPAA, the FDA's good machine learning practice, and state laws (Texas's, rendered by the captions as "Triaga") "are not afterthoughts. They are the grounding input in how you actually design your systems. You cannot slap on HIPAA on top of an underlying system or an architecture. You start with it and let the architecture grow around it." ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 05:18-05:41)
- **The property you are buying is capability, not diligence.** "You're not just trusting that the policies will get followed. You're actually relying on a system that's incapable of certain failures." That is the reusable test for any proposed control: does it make the violation *detectable*, *forbidden*, or *impossible*? Only the third survives turnover, deadline pressure, and an engineer who has not read the policy. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 05:42-05:53)
- **Compressed as "don't policy what you can architect,"** the first of three architecture rules in the talk's one-slide summary. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 20:18-20:36)
- **The cost is stated rather than hidden:** "building guardrails first is slower than bolting them on later. But that's the design, not limitation." The tradeoff only pays where the data category is genuinely regulated — stripping a field at ingestion also removes it from every future debugging session and every future model input. ([Rashi Agrawal](../sources/20260819_YXEqC05WEI0.md), 21:03-21:18)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Security](../topics/security.md)
- [Healthcare Operations](../topics/healthcare-operations.md)

Related concepts:
- [Run Must-Not-Fail Decisions in a Code Layer Above the Model](run-must-not-fail-decisions-in-code-above-the-model.md)
- [Generate Eval Data by Reversing the Inference Workflow](generate-eval-data-by-reversing-the-inference-workflow.md)
- [Aggregated Personal Context Creates Mosaic and Exfiltration Risk](aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md)
- [Use Edge Inference When Latency, Privacy, Offline Access, or Token Cost Dominate](use-edge-inference-when-latency-privacy-offline-access-or-token-cost-dominate.md)

Sources:
- [Guardrails First: Engineering Member-Facing Health AI — Rashi Agrawal, Hinge Health](../sources/20260819_YXEqC05WEI0.md), 03:38-05:53, 20:18-21:18
