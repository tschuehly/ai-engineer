# Reduce Every Workflow to Know, Decide, Act, and Learn

Summary: Before designing an agentic business system, reduce each of its workflows to four questions — what do we know, what should happen next, how do we execute that safely, and did it work — and build one layer per question, with the fourth feeding the second. The decomposition is what converts a pile of departmental automations into a single decisioning system.

Use when:
- Starting an internal agent system that spans several teams and tools, and the requirements arrive as a list of automations rather than an architecture.
- Auditing an existing automation stack for which of the four capabilities it silently lacks (usually the fourth).
- Deciding where a proposed feature belongs before arguing about which vendor to use for it.

Details:
- The four questions came out of a cross-functional team — CX, RevOps, product, engineering, sales — that kept finding "the same patterns underneath that complexity": "what do we know about the customer? What should happen next? How do we execute that safely? And did it work? That became our architecture." ([Liu](../sources/20260826_L4I7WgiEquo.md), 05:29-05:57)
- The layers map one-to-one: **know** is "a context layer we can trust about every customer," **decide** is "choose the single next best step for them," **act** is "fire a concrete action" — the named action types are a lifecycle email, an in-app nudge, or a task handed to a rep — and **learn** is "watch what happened and feed it back into the decisioning so that it's a loop." (05:59-06:25)
- **The third question carries the safety requirement inside the decomposition, not beside it.** "How do we execute that safely" is what produces the human-approval default and the untrusted-input stance at Notion, so safety is a layer with an owner rather than a review step bolted on before launch. (05:47-05:53, 07:23-07:58)
- The decomposition is what licenses consolidation. The stated goal is "a single decisioning system that spans self-serve growth and sales assist," replacing marketing, sales, and customer ops each "looking at a customer independently and making decisions separately"; the four common questions are the evidence that one system can serve both motions. (03:02-03:34)
- The system-level properties are named as a triple — "programmable, proactive and continuous" — which maps onto the layers: programmable comes from the shared context and eligibility primitives, proactive comes from non-user-initiated signals in the decide layer, and continuous comes from closing the loop. (03:36-03:41, 11:44-11:59)
- A parallel takeaway gives the vocabulary rather than the layers: "model GTM as primitives — entities, context, triggers, actions, eligibility rules — and the alien world becomes a system you can engineer." Entities and context are the know layer, triggers and eligibility the decide layer, actions the act layer. (20:02-20:12)
- **Limit.** The fourth layer is the least demonstrated. The learn loop is described as "the rebuilt version" of an analyst reading outputs, and no instance of the system pivoting on engagement history is shown; the two reported outcome figures (13 weeks, 63%) measure the system, not the loop. (14:53-15:37, 18:48-19:14)
- **An independently derived four-part decomposition that matches on three of four and orders them by dependency.** Berry's GTM engineering breaks into data, orchestration, agents, and execution — the world model, keeping the systems that hold it in agreement, the reasoning layer, and getting in front of the customer. Know maps to data, decide to agents, act to execution; what Berry adds is orchestration as a first-class layer, which Notion's model absorbs into know and act. What he lacks is learn, and he says why: "the continual learning effort and the next best action suggestions are kind of one of the cutting edge problems… today in GTM, this is not fully solved yet." Two teams converging on nearly the same decomposition from different vantages is evidence for the decomposition; both leaving the fourth layer unbuilt is evidence about the fourth layer. ([Berry](../sources/20260826_UhCY231d0FQ.md), 01:58-02:19, 11:47-12:10)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Put Humans and Agents on the Same Substrate Instead of an AI Layer on Top](put-humans-and-agents-on-the-same-substrate-instead-of-an-ai-layer-on-top.md)
- [Thread Every Outcome Back to the Decision That Caused It](thread-every-outcome-back-to-the-decision-that-caused-it.md)
- [Make Routing and Eligibility a Shared First-Class Primitive](make-routing-and-eligibility-a-shared-first-class-primitive.md)
- [Treat Go-to-Market as a Live Model of Your World That Agents Act On](treat-go-to-market-as-a-live-model-of-your-world.md)
- [Design AI Systems Requirements-First With a Four-Phase Framework](design-ai-systems-requirements-first-with-a-four-phase-framework.md)
- [Close the Eval-to-Action Loop So Signal Survives the Dashboard](close-the-eval-to-action-loop-so-signal-survives-the-dashboard.md)
- [Ship Go-to-Market Changes on an Engineering Release Cadence](ship-go-to-market-changes-on-an-engineering-release-cadence.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 03:02-06:25, 20:02-20:12
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 01:58-02:19, 11:47-12:10
