# Ship a Catalog of Paved Roads, Not One Standard

Summary: Getting two engineering teams to agree on one way of working costs more communication and brokerage than the agreement is worth, so the realistic output of a shared-context program is three or four maintained paved roads teams can pick from, with going your own way allowed on your own budget. The registry that holds them needs an owner, or shared skills fork into near-duplicates nobody can choose between.

Use when:
- A central team is trying to converge the whole organization onto one agent setup and stalling.
- Deciding what a shared skill or context registry should guarantee about the things in it.
- Two teams have forked the same skill and a third team does not know which to adopt.
- Setting the terms on which a team is allowed to opt out of the shared path.

Details:
- **What belongs in the registry, and the argument for it.** "Reusable context across teams. Why are we all inventing how we do the authentication system? This is a shared component. Let's put it in the registry. Why are you building all your harnesses? Well, if we're all using the same linters and the same security tools, that's a reusable component. So, I think that will centralize similar to the paved path for cloud into that platform registry of reuse." ([Debois](../sources/20260822_zCJtYuqwm7E.md), 11:26-11:58) The test is whether the underlying thing is already shared: one auth system, one linter, one security scanner means one context package.
- **The sprawl failure, which is specifically a *choosing* failure.** "If everybody can put stuff like on the internet in a repo, it becomes a sprawl… 'he has a skill, he's maintaining it. That person also has a similar skill and forked it. Now, what do I do? Which one do I pick?'" (11:58-12:26) Note the cost is not storage or duplication effort — it is that a consumer facing two similar skills with unclear maintenance cannot make a decision, so both go unused and a third gets written.
- **What ownership means operationally.** "There's an owner for this area. And they also care about making it testable. They make sure that it's modular, that other people can extend the context, for example, or the harness, that it's security scanned." (12:26-12:44) Four guarantees — tested, modular, extendable, scanned — which is what distinguishes a registry from a shared folder. See [Agent Enablement Falls Between Platform and Developer Experience, So Name an Owner](agent-enablement-falls-between-platform-and-developer-experience-so-name-an-owner.md) for why the owner is hard to find on a standard org chart.
- **Why the answer is a catalog rather than a standard.** "That consensus is hard. I'm not saying this is tabs versus spaces, but at times it feels like that. If you have two developer teams having to have consensus on how they work, that requires a lot of communication and brokerage. So, you probably don't end up with one thing, but a catalog of three, four paved roads where they can pick off." (12:44-13:12) The number is not derived from anything; the mechanism is, and it is coordination cost, which grows with the number of teams that must agree.
- **The escape hatch has a price attached, and that is what makes the catalog work.** "They can still do their own, but that's on their own budget. The centralized pieces will be maintained, and that is supposed to be the easy way of adoption to go there." (13:12-13:26) Nothing is forbidden; the paved road is subsidized and the alternative is not. That is a materially different lever from a mandate, and it is compatible with the wiki's repeated finding that mandates raise usage without raising confidence.
- **Cost visibility is the companion mechanism.** "If they do this blindly, we also want to make sure that they know what it costs. Because if we visualize the cost, they might be eager to do some optimization… If I can reduce the number of iterations the agent has to run through, that is an optimization that I can run. But if I don't visualize that and I just see the end result, then we don't know." (13:26-13:58) And the org-level version: when vendor pricing bites, "you shouldn't say 'let's limit all the spends.' Your reflection should be, let's optimize the spend… pick the right model, educate them on the model, but also giving them better context and harnesses because that will make your cost go down." (18:19-18:46) Better context is being offered as a cost lever, not only a quality lever — the same claim [Cut Coding-Agent Cost by Fixing the Input, Not the Model or Output](cut-coding-agent-cost-by-fixing-the-input-not-the-model-or-output.md) makes from the input side.
- **How this qualifies the wiki's existing paved-path material.** [Build Paved Paths for Enterprise AI Engineering Tools](build-paved-paths-for-enterprise-ai-engineering-tools.md) describes Bloomberg's single paved path — one gateway, one discovery hub, one platform service — as the answer to thousands of engineers duplicating work. Debois agrees about the duplication and disagrees about the cardinality: at the level of *how a team works*, as opposed to which gateway it calls, one path is not reachable. The reconciling variable is whether the shared thing is infrastructure everyone must traverse (one) or a working practice (a few). Blum's finding that centralizing personal workflows hits diminishing returns is the third point on the same line.
- **Caveats.**
  - "Three, four" is a feel, not a finding. No organization is named as having run a catalog of that size, and no criterion is given for when to add a fifth road or retire one.
  - Charging off-road work to the team's own budget assumes a budgeting model where that is even visible. In most engineering orgs it is not, which quietly makes the incentive rhetorical.
  - Nothing is said about versioning, deprecation, or what happens when a paved road changes underneath the teams on it — the hardest part of running a real platform catalog.

Related topics:
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Build Paved Paths for Enterprise AI Engineering Tools](build-paved-paths-for-enterprise-ai-engineering-tools.md)
- [Agent Enablement Falls Between Platform and Developer Experience, So Name an Owner](agent-enablement-falls-between-platform-and-developer-experience-so-name-an-owner.md)
- [Skill Composability Is Decided Before Authoring, Not in the Registry](skill-composability-is-decided-before-authoring-not-in-the-registry.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)
- [Cut Coding-Agent Cost by Fixing the Input, Not the Model or Output](cut-coding-agent-cost-by-fixing-the-input-not-the-model-or-output.md)
- [Measure Enablement by Human Touches and Share of Fixes Reused](measure-enablement-by-human-touches-and-share-of-fixes-reused.md)
- [Make Internal Platforms Self-Service for Agent Users](make-internal-platforms-self-service-for-agent-users.md)

Sources:
- [Coding Agents Don't Scale Themselves. Neither Do Your Teams. — Patrick Debois, Tessl](../sources/20260822_zCJtYuqwm7E.md), 11:26-13:58, 18:19-18:46
