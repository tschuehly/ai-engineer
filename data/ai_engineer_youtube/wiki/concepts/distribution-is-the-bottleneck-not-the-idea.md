# Distribution Is the Bottleneck, Not the Idea

Summary: In a go-to-market organization the scarce resource is not good campaign ideas — product, data, engineering, and sales all generate them — but everything downstream of the idea: pulling the audience, producing the enablement material, and persuading the people who own each channel to actually run it. That last step is a coordination cost measured in months, and it is what an orchestration layer exists to remove.

Use when:
- Deciding what an internal go-to-market platform should automate first, and tempted to start with generation quality.
- A team has more approved experiments than it can launch, and the queue is not compute-bound or model-bound.
- Distinguishing the three go-to-market bottlenecks so each gets the fix it needs rather than a single "AI for GTM" initiative.

Details:
- **The diagnosis is stated as a subtraction.** "There's a ton of great ideas… everybody across product and data and engineering and go-to-market have really good ideas for things that they want to do. And the bottleneck is kind of like everything after that, right? How do you go pull an audience to go and target? How do you go and convince a bunch of people to abide by whatever strategy that you've come up with or playbooks or enablement materials." The stated aim is "to reduce that coordination cost." ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 01:00-01:31)
- **Three bottlenecks, and they are not the same problem.** Inconsistent data across systems, where "everybody's operating off of a different source of truth"; reps "buried in busywork" between back-to-back meetings, so "the operational burden of doing everything in between sales was just really high"; and coordination, where writing the proposal and enablement material and then "convincing a bunch of people to go and use all of this… is just a really challenging thing to do on any pace that's not on the order of months." The first is an engineering problem, the second an automation problem, the third a distribution problem. (02:41-03:52)
- **The data problem is subordinate to the distribution problem, not parallel to it.** The reason inconsistency matters is stated causally: disagreeing sources of truth make it "effectively impossible to go and distribute some coordinated action across these different go-to-market teams and channels." A multi-channel action cannot even be *defined* over audiences that four systems compute differently, which is why the substrate has to land before the orchestration does. (02:53-03:04)
- **The target interface is a description, not a workflow.** The goal is "the ability to just describe a motion" — playbook, experiment, or evergreen campaign — and have it distributed "across the channels through which you actually execute your go-to-market, whether it's outbound or ads or web or whatever." One sentence about golfers at East Coast construction companies should produce an audience, an incentive, outbound sequences, ad and web creative, and in-app notifications. (00:29-00:59, 02:00-02:39)
- **Note what is being automated away: persuasion, not typing.** The enablement document and the internal campaign pitch exist because a human has to convince channel owners to change what they do. Generating the artifacts for each channel directly removes the need to persuade anyone to build them, which is a different lever from making any single artifact better.
- **Limit.** The coordination cost is asserted at "on the order of months" with no baseline, and no after-figure is given; the orchestration layer that would compress it is described in the future tense throughout ("what we're building towards"). The verticals underneath it are built; the distribution layer on top is the open frontier of the talk that names it. (00:31, 16:32)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Separate the Context Gap From the Expert Gap](separate-the-context-gap-from-the-expert-gap.md)
- [Gate a Generated Multi-Channel Campaign on the Channel Owner](gate-a-generated-multi-channel-campaign-on-the-channel-owner.md)
- [Solve One Team, Then Mirror the Build Sideways](solve-one-team-then-mirror-the-build-sideways.md)
- [Separate the Did-Not-Try Problem From the Did-Not-Return Problem](separate-the-did-not-try-problem-from-the-did-not-return-problem.md)
- [Distribution Is the New Bottleneck for Developer Tools](distribution-is-the-new-bottleneck-for-devtools.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)

Sources:
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 00:29-03:52, 16:32
