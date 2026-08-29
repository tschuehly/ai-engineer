# Choose AI coworker form factors by interaction mode

Summary: AI product interfaces can be split into invisible, ambient, inline, and conversational form factors. The right form depends on whether the agent should work in the background, surface opportunities, act directly inside the user's work, or collaborate through explicit dialogue.

Use when:
- Designing where an AI agent should appear in a product workflow.
- Deciding whether chat is the right surface or whether the agent should be hidden, ambient, or inline.

Details:
- Flatfile's AI stack is described as real-time data context, validation outcomes, agents, tools, runnable jobs, and user-facing surfaces, with four practical interaction buckets: invisible, ambient, inline, and conversational. (01:29-02:14)
- Invisible AI can personalize a demo in the background from a signup email and company lookup without requiring the user to know the agent is working. (02:16-02:44)
- Ambient AI can analyze dirty data in the workspace and mark columns where it sees opportunities to fix issues, while the user is not directly operating the agent. (02:46-03:06)
- Inline AI can sit directly inside the data workflow, generate code, and run that code over large data sets such as many rows and columns. (03:08-03:28)
- Conversational AI remains useful for no-code or low-code build mode, where the user directs an agentic system that writes application code. (03:30-03:52)
- **A second axis for the same choice: the form factor is set by the industry, not only by the interaction mode.** Shenoy runs a parallel taxonomy by autonomy — copilot, synchronous agent, asynchronous agent, long-running agent, AI coworker — and reports that the asynchronous form is the one that does not transfer: "this varies dramatically from industry to industry. Just because you have one way of launching an async agent for code, doesn't mean that same way is going to work for architecture or property management." He also treats form-factor choice and user enablement as one problem rather than two, since a form the user will not adopt returns no signal. ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 05:23-06:47, 09:54-10:13)
- **The modes can be a layering requirement rather than a choice.** Cloudflare runs three concurrently for one substrate: an ambient weekly digest that is pushed, a conversational self-serve workspace reps drive during calls, and a human request queue that never goes away — "that's how they like to interface with the operations team is to be able to ask questions." The selection criterion here is not the nature of the task but the preference distribution of the audience, which is why dropping any one mode strands a population rather than degrading a workflow. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 16:30-16:55)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Collaborate with complex agents through high-bandwidth artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Async Agents Need a Forking Substrate and a User Who Tolerates Out-of-Order Completion](async-agents-need-a-forking-substrate-and-a-tolerant-user.md)
- [Layer Ask, Push, and Self-Serve Because Teams Interface Differently](layer-ask-push-and-self-serve-because-teams-interface-differently.md)

Sources:
- [Form factors for your new AI coworkers - Craig Wattrus, Flatfile](../sources/20250822_CiMVKnX-CNI.md), 01:29-03:52
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 05:23-10:13
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 16:30-16:55
