# Customization Control Is a Separate Question From Open Weights

Summary: "Can I adapt this model myself, on my own data, in my own environment?" and "are the weights published?" are two different questions that the open-source debate routinely merges. A tool that lets an organization train its own model locally, privately, or inside its own walls gives control without publishing anything — and the risk profile of that is not the risk profile of open release.

Use when:
- Framing a build-versus-buy or open-versus-closed decision for a legal, security, or procurement audience.
- Writing an AI policy that is meant to constrain distribution but is drafted as if it constrains customization.
- Assessing whether a vendor's "own your intelligence" pitch actually removes a dependency.
- Arguing the safety case for or against widening access to model-building capability.

Details:
- The distinction, drawn in answer to a question about frontier labs' safety objection to enabling frontier AI outside the labs: AutoScientist "is about enabling people to customize their models. You can think of that as… a slightly different question from whether those are open source. It's giving people way more control. Whether that's local or private or within that company, it's about… how do they own their own intelligence?" ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 16:02-16:19)
- She does not use the distinction to dismiss the risk: "I definitely am not one of those people who says that open source doesn't carry any risk. So when you make a tool more readily available, there's a profile of risk associated with it." (15:49-16:02)
- The conflation she names, and the cost of it: "the dynamic has often conflated… that real risk of… wider access with [a] slight sense that… it restrains who can actually participate. And I think that's a delicate balance. And I think you have to acknowledge risk by also navigating that and acknowledging that it limits who can participate." Her stated position is that both binary camps "miss a lot." (16:25-16:57)
- Why the distinction is operationally useful and not just rhetorical: the three axes travel separately. *Weight distribution* is who can obtain the parameters. *Customization control* is who can change them and on what data. *Deployment locality* is where inference and training physically run. A hosted fine-tuning API gives customization without weights or locality; an on-prem open model gives all three; a local training tool over a checkpoint you already hold gives control and locality without publication. A policy written against "open source" regulates only the first.
- What this adds to the wiki's sovereignty material: [own open models for sovereignty and permissionless adoption](own-open-models-for-sovereignty-and-permissionless-adoption.md) argues from license and weights, and [decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md) argues from deployment constraints. This page adds the adaptation axis: an organization can be dependency-free on customization while still not distributing anything, which is the configuration most regulated enterprises actually want.
- The connected access argument is that the barrier being lowered is compute shape and tacit know-how rather than weight availability — see [Distributable Compute Lowers the Barrier to Frontier Work](distributable-compute-lowers-the-barrier-to-frontier-work.md) and [Frontier-Training Know-How Is Apprenticeship, Not Literature](frontier-training-know-how-is-apprenticeship-not-literature.md). Under that reading, "who can build" widens even if weight-release policy does not change at all.
- Provenance: this is a founder answering a safety objection to her own product category, and the distinction conveniently places that product outside the open-release debate. It is nonetheless a real distinction, she concedes the risk rather than denying it, and nothing here measures either the risk or the benefit. ([Adaption](../sources/20260812_XEd_SRVHBgU.md), 15:20-16:57)
- **A fourth axis, drawn by someone arguing for release rather than around it: weights versus research.** Rizwan's ask to the American labs separates the two explicitly — "I don't mean we need to open source our research. I think that's what gives us the lead. I think we need to open up our models and start releasing more open weights models, which as we know are not nearly as useful — you can extract the traces and train your copycat models on them more easily, but not in a way that can leapfrog." That is the same move this page makes (unbundle what "open source" is taken to mean) applied to a different pair: *published artifact* versus *published method*. His empirical claim, that distillation from released weights raises a competitor's floor without letting them pass you, is asserted without evidence and is contested; treat it as the position an advocate needs rather than a settled result. It matters here because a policy written against "open source" may be aimed at the research axis while the release being debated is only the weights one. ([Rizwan](../sources/20260807_CoEIs6Xm8m8.md), 15:19-15:45)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Own Open Models for Sovereignty and Permissionless Adoption](own-open-models-for-sovereignty-and-permissionless-adoption.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Distributable Compute Lowers the Barrier to Frontier Work](distributable-compute-lowers-the-barrier-to-frontier-work.md)
- [Frontier-Training Know-How Is Apprenticeship, Not Literature](frontier-training-know-how-is-apprenticeship-not-literature.md)
- [Enterprise Open-Model Adoption Follows Task Pressure](enterprise-open-model-adoption-follows-task-pressure.md)
- [Design Private AI Serving Around Verifiable Remote Compute](design-private-ai-serving-around-verifiable-remote-compute.md)
- [Commoditize the Layer You Do Not Win On](commoditize-the-layer-you-do-not-win-on.md)

Sources:
- [Adaption Labs: Gradient-Free Continual Learning — Sara Hooker, Adaption](../sources/20260812_XEd_SRVHBgU.md), 15:20-16:57
- [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](../sources/20260807_CoEIs6Xm8m8.md), 15:19-15:45
