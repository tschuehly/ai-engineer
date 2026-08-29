# Expose Orchestration Through Both a Prompt and an API

Summary: Multi-agent orchestration is usually shipped one way — a slash command or a phrasing that makes the main agent delegate. Warp ships it twice: the same subagent capability is reachable as a prompt, where an orchestrator agent hides the message-passing and progress-tracking, and as an API, where a subagent is attached to a parent agent by supplied configuration. The two are not redundant, because they answer different questions: the prompt path is for work whose decomposition you cannot specify in advance, and the API path is for work someone wants to wrap in a program you did not write.

Use when:
- Designing the control surface for a multi-agent platform and deciding whether a slash command is sufficient.
- A user asks to script or schedule something your product only exposes conversationally.
- Deciding which platform primitives need API coverage, rather than shipping an API for whichever one was easiest.
- Explaining why an internal team built their own tool on your product instead of asking you to build it.

Details:
- **Why more than one agent at all.** "Real engineering work rarely fits inside one prompt. In a typical workflow, you might need one agent to go research a problem and plan a solution. You might need another agent to implement it, and you might need to bring in a third to validate it. And you might want each of these agents to use different harnesses and different models in order to have a real adversarial and robust approach." The heterogeneity is the argument, not the parallelism — a validator running the same model in the same harness as the implementer is a weaker check. ([Abdalla](../sources/20260822_L173Z8DpaJg.md), 06:24-07:03)
- **The prompt path, and what it absorbs.** "I say `/orchestrate`, or I cue the agent via prompting that I want it to delegate work across multiple sub agents… And this orchestrator agent will do all of the messy complexity of interacting with sub agents, mediating messages between them, and tracking the work that's happening for me behind the scenes with a single prompt." Three things are hidden: spawning, inter-agent messaging, and progress tracking. That matches the wiki's position that [the core agent loop should own decomposition](let-the-core-agent-loop-orchestrate-parallel-subtasks.md) when the user cannot supply it. (07:03-07:41)
- **The API path, stated as a parent-child relation rather than a job submission.** "Everything in our surface area is exposed via an API, and I can fire off a request to say that I want to run a subagent that is attached to a parent agent via configuration that I provide." The distinguishing detail is *attached to a parent* — the API is not a second, flatter way to start an agent; it exposes the same hierarchy the prompt path builds implicitly, which is what lets a program and a conversation participate in one run. (08:04-08:29)
- **The coverage rule.** "We're trying to be intentional about exposing an API for every key component of the stack. So this is APIs for spinning up agents and subagents, for managing the environments and compute that these agents are running in, for working with the artifacts that they produce." The three named primitives correspond to the three things a caller cannot otherwise reach: the run, the place it runs, and its output. (08:50-09:07)
- **The stated payoff is about whose opinion the interface encodes.** "The thing about great APIs and SDKs is people can build on top of them, which means that they're not restricted to your UI or your opinion of how a particular experience should look. This is where composability becomes really powerful." (08:29-08:50)
- **The evidence offered is a use case the vendor did not anticipate and could not have built.** Non-engineering teammates used the SDK to build Slack bots: developer relations "built out tooling to help us manage all of our social mentions. So as tweets and Reddit posts and things are coming in, we have agents that will pick them up, do some sentiment analysis on them, try and understand what the user wants, and then propose a response that folks on our social media team should use." Others built product-question answering and competitive research. Note the shape — an event-triggered pipeline over an external feed, ending in a human-approved draft. None of that is a coding workflow, and none of it fits a `/orchestrate` prompt, which is the argument for the second path rather than a bigger slash command. (09:07-10:06)
- **How this sits against the wiki's API-first pages.** [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md) argues for APIs because the consumer is an agent; [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md) argues for them because a non-engineer with a coding agent will build the screen you would otherwise queue. This adds the case where the thing being exposed *is itself* the agent system, and the resulting demand is not for a screen but for a trigger — the Slack bots exist because something outside the product needed to start work inside it.
- **Unaddressed.** No account of authorization on the API path (who may attach a subagent to whose parent, what a non-engineer's bot is allowed to spend or touch), no versioning or stability commitment for a surface users are being encouraged to build on, and no report of the orchestrator agent failing — no case where prompt-driven delegation decomposed the work badly, and no comparison of prompt-orchestrated against API-orchestrated results. The claim that heterogeneous harnesses and models make the check "adversarial and robust" is asserted, never tested.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Let the Core Agent Loop Orchestrate Parallel Subtasks](let-the-core-agent-loop-orchestrate-parallel-subtasks.md)
- [Customize Subagents by Task, Model, Tools, and Permissions](customize-subagents-by-task-model-tools-and-permissions.md)
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Ship Stable APIs and Let Users Vibe-Code the Interface](ship-stable-apis-and-let-users-vibe-code-the-interface.md)
- [Use coding agents as programmable subagents inside products](use-coding-agents-as-programmable-subagents-inside-products.md)
- [Environment Isolation Is What Lets Non-Engineers Trigger Real Work](environment-isolation-is-what-lets-non-engineers-trigger-real-work.md)
- [Support Many Harnesses by Owning Conversation State and Artifacts](support-many-harnesses-by-owning-conversation-state-and-artifacts.md)

Sources:
- [The Agent Behind the Curtain: Building the Oz Cloud Agent Platform — Safia Abdalla, Warp](../sources/20260822_L173Z8DpaJg.md), 06:24-10:06
