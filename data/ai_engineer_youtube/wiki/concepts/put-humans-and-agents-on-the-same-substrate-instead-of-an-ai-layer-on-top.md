# Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top

Summary: An agent added as a layer above the business ends up reading a different representation of the world than the people it works with, and the two representations drift. The alternative is to make the agent another operator inside the system humans already use, which forces the context to be displayed rather than merely queryable.

Use when:
- Deciding whether to build an "AI layer" over existing tools or to put agents inside the system of record people already work in.
- Reviewing an agent design where the model reads a database or API that no human ever looks at.
- Choosing what the human-facing surface of an agentic workflow should be.

Details:
- The rule is stated as a rejection of the default: "instead of building an AI layer on top of our business, we designed our architecture so that the agent can operate as another operator within the same system as humans." ([Liu](../sources/20260826_L4I7WgiEquo.md), 07:09-07:20)
- It arrives as a correction to a finished-looking architecture diagram. After presenting the four layers, Liu says "this architecture is missing something important… the most important part is that humans and agents are operating on the same loop." (06:25-06:38)
- **The concrete requirement is display, not access.** "Concretely, this means that the context needs to be displayed so that humans and agents can read and operate on it together" — a machine-readable API alone does not satisfy it, because the human half of the loop has to see the same object the agent acted on. (06:38-06:45)
- Same system, different roles: agents do "the repetitive work at scale — gathering context, researching, drafting recommendations, and writing artifacts"; humans "provide the judgment, adding nuance, deciding what to do next, and if a recommendation is correct, and owning the customer relationship." (06:49-07:08)
- The closing takeaway states the failure mode directly: "be headless by default and design for agents as operators and not just co-pilots. If humans and agents can't read from the same substrate, you're basically building two systems that will eventually drift apart." (20:13-20:27)
- The substrate property that makes one artifact serve both readers is format: the context layer is "built off of plain markdown, a language that agents are fluent in, and we have databases and hierarchies that they can navigate easily; at the same time this is well designed for humans," which is "what lets our engineers, agents, and GTM work off the same context." (18:18-18:44)
- The human-side payoff is measured in tabs rather than in accuracy: GTM staff "didn't need to jump between many tools anymore," exploring context, investigating accounts, and dispatching to outbound tools from the surface they already used. (10:36-11:03)
- **Limit.** The substrate here is the speaker's own product, and no alternative substrate is compared. The claim that a shared markdown-and-database surface prevents drift is an architectural argument, not a measured result; nothing in the talk reports a drift incident avoided. (11:15-11:17, 18:18-18:44)
- **The shared substrate is necessary and not sufficient, per a vendor who ranks the remaining gap first.** Asked for the hardest problem in GTM engineering, Berry names neither data nor orchestration nor agents but "the interface between the human and the agent," because with the agent acting as "the reasoning and decision layer for a lot of tasks that a sales rep was previously doing," "the rep might think that they should do something different or the rep might not know that the agent did something." A common substrate makes the second knowable; it does not make it known, and it says nothing about the first. See [The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer](the-human-agent-handoff-is-the-hard-part-once-agents-are-the-decision-layer.md). ([Berry](../sources/20260826_UhCY231d0FQ.md), 16:51-17:47)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Own the Context Layer and Rent Every Other Layer](own-the-context-layer-and-rent-every-other-layer.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Personal Knowledge Bases Become Agent Context Substrates](personal-knowledge-bases-become-agent-context-substrates.md)
- [Shared Canvases Expose Multi-Agent State and Coordination](shared-canvases-expose-multi-agent-state-and-coordination.md)
- [Keep Humans Aligned With Proactive Agent Work](keep-humans-aligned-with-proactive-agent-work.md)
- [The Human-Agent Handoff Is the Hard Part Once Agents Are the Decision Layer](the-human-agent-handoff-is-the-hard-part-once-agents-are-the-decision-layer.md)
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 06:25-07:20, 10:36-11:17, 18:18-18:44, 20:13-20:27
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 16:51-17:47
