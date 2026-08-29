# Stage the MCP Token Tax Down: Direct, Omni, CLI, Then Code Mode

Summary: Uber moved the same catalog of internal tools through four successive interface shapes — direct MCP, a single discovery MCP, a CLI projection, and generated code — each one moving more of the payload out of the agent's context window. The staging is the useful part: the four are not alternatives to choose between but a migration path where each step is cheap because the previous one already normalized the tools behind one gateway.

Use when:
- An MCP catalog has grown past the point where tool definitions and responses fit comfortably in context.
- Deciding whether to adopt code mode, and wanting a sequence rather than a rewrite.
- Estimating what interface work is worth doing before buying more context window.
- Justifying token-efficiency work to someone who wants a number.

Details:
- **The problem is cumulative, not per-tool.** "Once you end up with enough MCPs they'll all add up to and have a massive token tax." The tax has two halves that the four stages attack in order: the *definitions* every tool loads at startup, and the *responses* every call returns. ([Medisetty](../sources/20260821_17-YSUHo6Lk.md), 03:39-04:05)
- **Stage 1 — direct MCP.** The starting point: each server installed and its tools listed in context. This is what the other three stages are measured against, and it is where most organizations are.
- **Stage 2 — Omni MCP, one installed server that finds the rest.** "Earlier this year we created Omni MCP which is one single MCP that you install which can discover and invoke any MCPs within the gateway." This attacks the definition half: one tool definition in context instead of one thousand, with discovery deferred to call time. It only works because a gateway already knows what all the servers are — the registry is the precondition, not a bonus. (04:51-05:06)
- **Stage 3 — project the tools into a CLI.** "Couple of months ago we projected all of these MCPs into CLI pattern so that even the response doesn't eat up in your context." This attacks the response half: a command's output lands in a shell the agent can filter, page, or discard, rather than being pasted whole into the transcript. The generalization is that a CLI is not a different protocol, it is the same tools with a different disposal policy for their output — see [Use Bash as a Composable Code-Mode Tool for Agents](use-bash-as-a-composable-code-mode-tool-for-agents.md). (05:06-05:21)
- **Stage 4 — code mode, targeted at the worst offenders only.** "Of late we also have a code mode skill which is auto-installed which on the fly creates Python scripts to hyper optimize some of the top MCP token consuming use cases." Two design choices worth copying: it is applied to the measured top consumers rather than everywhere, and it ships as an auto-installed skill so the optimization arrives without anyone opting in. (05:06-05:21)
- **The reported result.** "Now we have thousand plus MCP tools and just with these optimization efforts we've saved more than 40% fleetwide savings." (05:21-05:41)
- **Reading the number honestly.** The 40% is a combined figure for stages 2 through 4 with no split between them, no stated baseline or window, and no report of whether task success rates changed. It is worth having as evidence that interface shape is a large lever at fleet scale; it is not a per-stage return you can plan against. The measurement that would make the staging decidable is tokens per *successful outcome* within a task class — see [Measure Agent Interface Efficiency With Tokens per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md) — and it is not reported here.
- **What the staging implies about ordering.** Each stage is a strictly narrower interface than the one before, and each is only affordable because the gateway centralized the tools first. An organization that has not normalized installation and auth cannot jump to stage 4, because there is no place to auto-install the code-mode skill from and no inventory to identify the top consumers in.

Related topics:
- [Tools](../topics/tools.md)
- [Context Engineering](../topics/context-engineering.md)

Related concepts:
- [Expose Large APIs Through Typed Code Mode](expose-large-apis-through-typed-code-mode.md)
- [Use Bash as a Composable Code-Mode Tool for Agents](use-bash-as-a-composable-code-mode-tool-for-agents.md)
- [Measure Agent Interface Efficiency With Tokens per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Crawl Internal APIs Into MCP Servers Instead of Asking Teams to Write Them](crawl-internal-apis-into-mcp-servers-instead-of-asking-teams-to-write-them.md)
- [MCP Gateways Create an Enterprise Root of Trust](mcp-gateways-create-an-enterprise-root-of-trust.md)
- [Cap the Skills List as a Share of the Context Window](cap-the-skills-list-as-a-share-of-the-context-window.md)
- [Agent Connectivity Stack Combines Skills, MCP, CLIs, and Computer Use](agent-connectivity-stack-combines-skills-mcp-clis-and-computer-use.md)
- [Build One Context Graph So Agents Stop Crawling Twenty Systems for Basic Facts](build-one-context-graph-so-agents-stop-crawling-twenty-systems-for-basic-facts.md)

Sources:
- [Agentic SDLC at Uber — Uday Kiran Medisetty & Adam Huda, Uber](../sources/20260821_17-YSUHo6Lk.md), 03:39-05:41
