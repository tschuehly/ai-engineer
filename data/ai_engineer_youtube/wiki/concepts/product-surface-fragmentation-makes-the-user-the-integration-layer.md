# Product Surface Fragmentation Makes the User the Integration Layer

Summary: When an AI product ships several surfaces — a coding CLI, a general workspace, a chat app — that cannot delegate to each other, the user becomes the transport between them, copying output from one into another. Two tests expose the problem: whether the surfaces interoperate, and whether an ordinary person can say why they are different. The fix is deletion and delegation between surfaces, not more surfaces.

Use when:
- Deciding whether to add a new agent surface or fold capability into an existing one.
- Diagnosing why users describe a capable product as confusing.
- Evaluating a roadmap in which surfaces are differentiated by internal architecture rather than by user job.

Details:
- The two-part test, from Anthropic's former chief product officer asked what he would delete: "we're asking people to make code versus co-work versus chat distinctions and one, they don't interoperate well and they can't delegate to each other, and two, I think the average person off the street could not explain to you why those are all different." Interoperability and explicability fail together because both come from the split being an implementation boundary. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 16:33-16:52)
- The symptom to look for is a copy-paste handoff the product asks the user to perform: "there's nothing more frustrating than having a co-work session where you're like, great, I've mapped out exactly what I want you to build and then be like, can you please create a paragraph that I can paste into Claude Code? That is some 2020 kind of workflow that really shouldn't exist anymore." Any manual paste between your own surfaces is a missing delegation edge. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 17:02-17:16)
- The cost is capability, not only polish: "deleting some of the product complexity within our product is a thing that would serve well. Also because then Claude can do what it needs to do and do well." The same constraint is named as the top limit on a specific product — "the things that are holding back Claude Design from being even better is better interaction with our other surfaces... the fact that our surfaces don't talk to each other as well as they could really holds back a lot of interesting ideas around what we could do." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 14:10-14:41, 16:52-17:02)
- Deletion is hard for a measurable reason, and the shape of the difficulty is worth naming before you look at your own usage numbers: the Microsoft Word problem, where "things that had four to five percent usage — you're like, oh, that's really not very many, but then you have like 20 features that each have four to five percent usage" and "everybody uses some disjoint subset of the functionality." Low per-feature usage does not imply low aggregate loss. Anthropic keeps a standing Slack channel named "project unship" to hold the question open. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 15:41-16:06)
- The generational version of the same argument: styles were unshipped in favour of skills because styles were "very prescriptive in the way that it worked," with the rule stated as "you have to be willing to take the primitives of one generation of AI and unship them or at least supplement them or supplant them with the next one." A more general primitive is grounds for retiring the specific one it subsumes. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 16:11-16:32)
- Limits: a candid but unmeasured self-critique. No usage data, no confusion metric, and no proposal for what the merged surface would actually look like — the argument identifies the tax without pricing the merge, and surfaces often exist because of real differences in permissions, latency, and runtime that a single surface still has to model.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Build Product Primitives Before Feature Surfaces](build-product-primitives-before-feature-surfaces.md)
- [Move the Platform's Primary Surface as Its Users Gain Tools](move-the-platforms-primary-surface-as-its-users-gain-tools.md)
- [Ask Size Lags Model Capability Because Early Products Boxed the Model In](ask-size-lags-model-capability-because-early-products-boxed-the-model-in.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 14:10-17:16
