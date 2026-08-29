# Ask Size Lags Model Capability Because Early Products Boxed the Model In

Summary: Users under-ask not because they misjudge the model but because they learned the size of a reasonable request from a generation of AI products that denied the model tools, execution, and environment access. The constraint is gone; the habit is not. The two responses are to grant apparently excessive degrees of freedom in the product, and to treat teaching larger asks as product work rather than user error.

Use when:
- Diagnosing why an internally capable agent produces small, timid usage.
- Deciding whether to give an agent a general capability (a VM, a shell, network access) that no individual user has asked for.
- Designing onboarding, docs, or in-product prompting for an agent surface.

Details:
- The diagnosis, from someone who shipped the earlier generation: "the first generation of AI products, we put them too much in a box and constrain their access to tools or their degrees of freedom, which means it was much harder to be unreasonable." The user experience that taught the habit — "when you say, do this thing for me, and then it would be like, well, I can't. I can barely — I can write code, but I can't really run it, or I can kind of introspect my environment, but not really." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 03:31-03:53)
- The design corollary is that capability grants look unjustified until you price the failure path. "Does every single knowledge worker need a virtual machine that can write bash? On the face of it, no" — until the built-in PDF parser fails on a file and the model writes its own script instead of returning an apology. The general capability is what converts a dead end into a remediation. ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 03:55-04:16)
- Teaching the ask is a product-team responsibility, not a user competence problem. The trigger was a non-technical colleague asking *him* to change an internal product: "I'm just going to go ask Claude to do this. Like, why don't you ask Claude?... as an industry or even as a product team, we have to teach people to be more unreasonable in their usage." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 03:04-03:27)
- The ask itself changes shape, not just size: from "I have an idea, I'm going to break it down in my head much more how I would do engineering normally, and then iterate through these different steps" to "I'm going to describe the goal, like go off and work on it," with tradeoffs and questions surfaced along the way. He names it "moving from that task delegation to express the end state and then have it go and cook on it." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 01:55-02:39)
- A companion technique for when a bigger ask returns reasoning above your head: ask the model to downshift. The model "will finish work and be like, here's the trade-offs I made. I'm like, can you explain it to me like I'm a little dumber than you are because I need you to break this down for me." ([How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 02:20-02:32)
- Limits: this is an unmeasured interview claim from a lab employee about his own product line. No usage data, no before/after on ask size, and no evidence that granting the VM changed outcomes rather than costs. The "does every knowledge worker need a VM" argument is also the argument for the most expensive possible default, and the talk does not price it.

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Rescope Ambition Down a Tier as Models Improve](rescope-ambition-down-a-tier-as-models-improve.md)
- [Make Delegation Multiplayer So People See Larger Asks](make-delegation-multiplayer-so-people-see-larger-asks.md)
- [Stage Agentic-Engineering Adoption With a Delegation Maturity Model](stage-agentic-engineering-adoption-with-a-delegation-maturity-model.md)
- [Product Surface Fragmentation Makes the User the Integration Layer](product-surface-fragmentation-makes-the-user-the-integration-layer.md)

Sources:
- [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](../sources/20260827_qqrk7CtkuIw.md), 01:55-04:16
