# Continual Learning and Enablement Are One Loop With a Cold Start

Summary: An agent that learns from production improves only as fast as people use it, so adoption is not a go-to-market concern downstream of the research program — it is the rate limiter on the research program. The two halves are usually owned by different teams, and the loop has no seed: initial usage never simply shows up.

Use when:
- Your continual-learning or trace-mining roadmap is blocked and the actual bottleneck is that nobody is generating traces.
- Deciding who owns adoption when a platform or research team owns the improvement loop.
- Justifying enablement headcount to an organization that treats it as sales overhead.
- Planning a rollout into an organization with long-tenured staff and established processes.

Details:
- The silo, named by function: continual learning — "whether it's in the prompt or in the weights" — is "owned by your research team, your platform engineering team," while "enablement's owned by growth or deployment or customer experience. Usually pretty siloed, not much interaction between the two." ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 13:43-14:29)
- The merge, and the reason: "We think these are part of the exact same loop. The agent only improves if people actually use it. And people only use the agent if it's worth adopting." Drawn as a snowball — more usage drives continual learning, which drives a better agent, which drives more usage. (14:29-14:49)
- **The cold start is the load-bearing part.** "There's still a really big elephant in the room. How do you get the initial usage? A lot of people will use Claude Code or give it to their whole enterprise, expect folks to just start using it. Everyone assumes the usage just shows up. But as we all know, that's simply not the case. It never does. Getting a 100-year-old firm to change its processes is hard." A snowball that never gets pushed does not roll; procurement and provisioning look like the deployment step and are not. (14:49-15:17)
- The failure written as an identity, which is what makes it an engineering constraint rather than a complaint: "You could have the best AI coworker on Earth. And if the person who's closed the books for the last 20 years continues to do things the same way, nothing changes. Nothing happens." Model quality does not appear on the right-hand side. (15:17-15:32)
- How this qualifies the trace-substrate argument. The case that traces are the substrate for improvement is well supported elsewhere in this wiki, but it assumes the traces exist. This page names the upstream dependency: trace volume is a function of adoption, adoption is a function of perceived worth, and perceived worth at time zero cannot come from the loop because the loop has not run. A continual-learning program in a low-adoption deployment is starved by construction, and the fix is enablement work, not more learning machinery.
- Where the seed comes from, on this account: co-design rather than distribution — reduce the activation energy by putting the agent inside the tools people already use, and go find the requirements in person ([Co-Design In Person](co-design-in-person-because-remote-channels-filter-the-requirements.md)). That is an argument for what to do first, not evidence that it works.
- Limits. No adoption rate, usage curve, or improvement measurement is given anywhere in the talk; the snowball is a slide. The speaker's organization owns the businesses it deploys into, which removes the procurement barrier that most teams face and makes his cold-start claim, if anything, an understatement of the problem elsewhere. ([Provenance and Limits](../sources/20260828_B0fjR3yaZFU.md))

Related topics:
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Observability and Continual Learning Are the Same Problem](observability-and-continual-learning-are-the-same-problem.md)
- [Co-Design In Person Because Remote Channels Filter the Requirements](co-design-in-person-because-remote-channels-filter-the-requirements.md)
- [Move enterprise AI adoption beyond spot experiments](move-enterprise-ai-adoption-beyond-spot-experiments.md)
- [AI adoption depends on incentive design as much as tool access](ai-adoption-depends-on-incentive-design-as-much-as-tool-access.md)
- [Embed Agent Tools in Existing Work Surfaces](embed-agent-tools-in-existing-work-surfaces.md)
- [Operational Outcomes Are Eval Labels You Only See If You Own the Operation](operational-outcomes-are-eval-labels-you-only-see-if-you-own-the-operation.md)

Sources:
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 13:43-15:32
