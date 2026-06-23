# A Bigger Model Is Not Automatically a Safer or Better Agent

Summary: For deployed agents there is a real smart-vs-safe tradeoff: a more capable model can be easier to jailbreak, has a wider attack surface when its remit is broad, and costs more and runs slower — so the target is a model good enough to perform the task but not capable of arbitrary harm.

Use when:
- Choosing a model size or capability tier for an automated/agentic deployment, not just a chat demo.
- Reasoning about why a "smarter" model did not make an agent safer or cheaper.
- Scoping an agent's instruction surface and tool/task power as part of risk analysis.

Details:
- Some jailbreaks work *better* on large models: a malicious instruction wrapped in a poem is decoded and executed by a capable model, while a low-end model "doesn't even understand the poem" and so cannot act on it — so bigger is not obviously safer. (02:59-03:24)
- A broad-remit agent that can do many things creates more surface area both to exploit and to test. (03:24-03:39)
- There is also a cost/latency penalty: using a large model for simple work (e.g. basic math) means paying for tokens and running slow rather than something optimized. Hence a smart-vs-safe and smart-vs-capable tradeoff for fully automated use. (03:39-04:05)
- The goal is an agent built on a model "good enough to perform but not capable of doing arbitrary harm." Harm has two surfaces: (1) what instructions/prompts it can receive and how flexibly they can be formulated, and (2) what tools and tasks it can carry out in your infrastructure — wiring millions of dollars is far riskier than answering questions. (04:06-04:36)
- Defining "good" and "harm" is itself hard: harm can mean doing exactly the wrong thing when asked to do something bad, or merely failing the task — different failure modes that a spec should separate. (04:40-05:03)

Related topics:
- [Models](../topics/models.md)
- [Security](../topics/security.md)

Related concepts:
- [Spec-Driven Agent Validation Goes Beyond the Test Set](spec-driven-agent-validation-goes-beyond-the-test-set.md)
- [Fix Tool Discipline Before Reaching for a Bigger Model](fix-tool-discipline-before-reaching-for-a-bigger-model.md)
- [LLM attack surfaces span prompts, context, retrieval, tools, and actions](llm-attack-surfaces-span-prompts-context-retrieval-tools-and-actions.md)
- [Capability-Based Sandboxes Start With No Authority](capability-based-sandboxes-start-with-no-authority.md)

Sources:
- [Spec-Driven Testing for Agents With A Brain the Size of A Planet — Steven Willmott, SafeIntelligence](../sources/20260531_UQKg0td-Bf4.md), 02:59-05:03
