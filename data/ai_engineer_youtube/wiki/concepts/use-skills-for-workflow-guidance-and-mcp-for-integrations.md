# Use skills for workflow guidance and MCP for integrations

Summary: Skills and MCP are complementary: MCP is best for service integrations and remote tool execution, while skills describe the workflows, context, and usage guidance that tell an agent how to use tools well.

Use when:
- Choosing between adding an MCP server, a script, or a skill.
- Packaging tool guidance for agents that already have access to integration tools.

Details:
- The talk recommends MCP for integrations, especially when the agent lacks shell access or the action should run server-side instead of depending on a local machine. 07:19-08:12
- Skills provide context and workflow instructions that may not fit into terse MCP tool descriptions. 07:37-07:51
- Script-backed skills run on the local environment, so they inherit OS compatibility, dependency, and credential-management constraints. 07:56-08:36
- In the Supabase example, MCP supplies database operations such as listing tables, executing SQL, applying migrations, and running advisors, while a skill can describe the safe workflow for using those tools. 25:19-26:21, 58:23-01:00:06
- Anthropic's MCP framing makes the same split explicit at the connectivity-stack level: skills capture reusable domain knowledge, while MCP provides richer remote semantics such as resources, tasks, authorization, governance, and MCP applications. (05:28-07:12)
- Anthropic's skills talk applies the split to domain deployment: MCP servers connect the agent to external data and systems, while skills provide expertise and can orchestrate multi-tool workflows across those MCP connections. 08:08-08:33, 09:34-10:31
- Anthropic's Claude API talk gives the platform version of the same boundary: MCP gives an agent access to external tools and context, while skills provide domain expertise about how to use those tools and context well. 10:35-10:47
- **The authorship corollary of the same split.** Touil reaches the boundary from who writes each side rather than what each side does: "tell me like who actually build a lot of MCPs? We just use MCP tools that is actually provided by the tool that we used to use before, right? So we don't really own," whereas skills are where "all of your know-how is actually at the skills level." ([Touil](../sources/20260828_M05vON8i0aI.md), 06:20-06:45) The two framings reinforce each other — integrations are commodities across companies and get shipped by whoever owns the system, while the knowledge of how your company uses them is not a commodity and nobody will ship it to you. The claim is contingent on an org consuming rather than producing MCP servers, and is drawn from a room's reaction rather than a survey.
- **The split as it emerged in a live system, with the capability each half unlocked.** Izmit's assistant carries close to 20 skills and five to six MCP connections, and they arrived for different reasons: skills absorbed business processes that no longer fit in the agent instructions, while MCP connections were what moved users from asking questions to automating work — "the next wave comes with all the MCP connections, all the integrations… now it becomes automate my workflows," with sellers monitoring inboxes and Slack, drafting responses into Gmail for review, and automating outreach. The friction the split introduces is also visible: orchestrating the MCP surface needed enough additional instruction text to hit the agent-instruction limit and force progressive disclosure. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 09:54-10:26, 12:57-13:08)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Evaluate retrieval and MCP layers by task value, not only response availability](evaluate-retrieval-and-mcp-layers-by-task-value.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Ship Skills Over MCP for Server-Authored Tool Guidance](ship-skills-over-mcp-for-server-authored-tool-guidance.md)
- [General agents need skills for domain expertise](general-agents-need-skills-for-domain-expertise.md)
- [Skills Are the Residual Where Organizational Know-How Lands](skills-are-the-residual-where-organizational-know-how-lands.md)
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)
- [Expose the Background Agents' Tool Surface to Employees Over MCP](expose-the-background-agents-tool-surface-to-employees-over-mcp.md)

Sources:
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md), 07:19-08:36, 25:19-26:21, 58:23-01:00:06
- [The Future of MCP - David Soria Parra, Anthropic](../sources/20260419_v3Fr2JR47KA.md), 05:28-07:12, 16:33-17:15
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](../sources/20251208_CEvIs9y1uog.md), 08:08-08:33, 09:34-10:31
- [Katelyn Lesse - Evolving Claude APIs for Agents, Anthropic](../sources/20251204_aqW68Is_Kj4.md), 10:35-10:47
- [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](../sources/20260828_M05vON8i0aI.md), 06:20-06:45
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 05:14-05:31, 09:54-10:26, 12:57-13:08
