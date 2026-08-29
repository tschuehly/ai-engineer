# Decide the Agent Buy Boundary With Six Production Questions

Summary: The choice between raw completions, a hand-rolled loop, an agent SDK, and a fully managed runtime is not a preference — it is decided by which of six production concerns you are willing to own: hosting and scaling, session management, filesystem, execution isolation, credentials, and observability. Every rung of the ladder answers some of them and hands you the rest; the checklist is what turns "which surface should we build on" into a list you can actually answer.

Use when:
- Choosing an agent platform, or justifying a build-versus-buy decision to people who are comparing them on model quality.
- A prototype built directly on a completions API is about to go to production and you need the list of what is missing.
- Scoping the real cost of "we'll just write our own agent loop."

Details:
- **The six questions, as posed.** How is the agent hosted and scaled? How are sessions managed? Where is its filesystem? How is execution isolated? Where do credentials live? How is any of it observed? These are presented as unavoidable — every team building an agent for production answers all six, explicitly or by accident. ([Anthropic Applied AI](../sources/20260811_K0X9QDRkIdg.md), 04:30-05:14)
- **The ladder they discriminate between.** *Messages API* — "simply tokens in and tokens out"; you own all six. *Hand-rolled agentic loop* — described as "painstaking"; you own all six plus the loop. *Agent SDK* — "we took the harness that powers Claude Code and we packaged it up," giving "a built-in agentic loop, file system access, tools and sandboxing"; filesystem, isolation, and part of session management move off your plate, while credentials and hosting stay. *Managed agents* — the vendor runs "everything below the product layer," answering all six. (01:41-04:26)
- **What the ladder deliberately does not include.** Anthropic draws the line at the same place on every rung: "you own the product, you own the task, you own your context." Context management and domain expertise are named as the things that do not move — "this is what separates a coding agent from a legal agent or go-to-market agent." That is the useful part of a vendor's framing of its own boundary: it tells you what buying the platform will *not* do for you, which is where the differentiated work has to go. (04:00-04:26, 15:50-16:47)
- **How to use the checklist rather than the ladder.** The ladder is one vendor's product line and will not match another's. The six questions survive the specifics: score any candidate surface on which of the six it answers, which it answers in a way you can live with, and which it answers in a way you would have to undo. A platform that answers "execution isolation" with a shared container may be worse than one that answers it not at all.
- **The two questions most often underestimated.** *Session management* and *observability* are the ones a prototype never has and production always needs — the first because a demo runs to completion in one process (see [keeping the session log separate from the context window](keep-the-session-log-separate-from-the-context-window.md) for what it costs to have skipped it), the second because agent failures are diagnosed from traces rather than stack traces.
- Provenance: an Anthropic vendor talk. Both the ladder and the checklist are Anthropic's, and the ladder terminates at Anthropic's own product, so the framing is structurally favorable to buying. No competing platform is compared, no pricing appears anywhere in the talk, and no cost is given for any rung — which means the checklist can tell you what you would be taking on but not what it would be worth to hand over.

- **A boundary question this list does not ask, and a way to stop the answer from going stale.** Uber's decisive constraint was neither differentiation nor data: it was that their code-review host is Phabricator and "most of the solutions do not provide support for Phabricator." A legacy or unusual substrate can force a build for reasons that have nothing to do with whether the capability is core, which is worth adding to any buy checklist. Their hedge against the resulting lock-in is cheap and portable: keep the vendors wired into the pipeline as alternative generators "so that we can compare ourselves to what's available more broadly," so the decision stays measured on your own traffic rather than being reopened from scratch later. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 01:22-01:46, 03:33-03:43)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Model a Managed Agent as Agent, Environment, and Session](model-a-managed-agent-as-agent-environment-session.md)
- [Build Agent Harnesses Incrementally Up a Capability Ladder](build-agent-harnesses-incrementally-up-a-capability-ladder.md)
- [Do Not Roll Your Own Agent Code Sandbox](do-not-roll-your-own-agent-code-sandbox.md)
- [Decouple the Agent Loop From the Tool Execution Environment](decouple-the-agent-loop-from-the-tool-execution-environment.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)

Sources:
- [Anthropic's Applied AI team on the Evolution of Agentic Surfaces](../sources/20260811_K0X9QDRkIdg.md), 01:41-05:14, 15:50-16:47
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 01:22-01:46, 03:33-03:43
