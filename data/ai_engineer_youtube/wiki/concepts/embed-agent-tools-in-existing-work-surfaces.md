# Embed Agent Tools in Existing Work Surfaces

Summary: Agent tools get more usage when they appear inside the surfaces where users already perform the work, such as an IDE, ticket, merge request, or support workflow. A separate playground can be useful for discovery but may fail as an adoption surface.

Use when:
- Deciding whether an internal AI tool should be a standalone app, MCP server, IDE integration, ticket action, or merge-request assistant.
- Debugging low usage of a tool that is technically useful but outside the user's normal workflow.

Details:
- Zapier's Autocode playground exposed useful APIs, but asking engineers to visit another web page for context and feedback created low engagement. (05:40-06:25)
- Diagnosis became valuable when support embedded it into the Zap that created Jira tickets from support issues, so the diagnosis appeared in the existing ticket workflow. (06:38-07:22)
- MCP let Zapier expose the same API tools inside engineers' Cursor workflow, reducing IDE context switching. (07:28-07:53)
- Scout moved from loose tools to an embedded agent loop: Zaps start the process, Jira receives diagnosis and routing context, GitLab CI/CD runs plan/execute/validate, and GitLab comments let support request another pass without pulling the merge request into an IDE. (10:09-12:39)
- A high-value tool can still fail when it is synchronous and slow; Zapier's diagnosis tool pushed the workflow toward asynchronous orchestration because users would not wait in the IDE. (07:53-08:15)
- **Tagging an agent into a thread alongside a person doubles as a low-friction demo to a skeptic.** "One of the most powerful thing[s] is being able to tag an agent in the Slack message with somebody and… 'can you just do this for me?' And have the agent[] close the loop in the thread." The adoption use is deliberate: "if you have a new conversation with somebody who's not fully bought in… then you can tag it in a non-passive-aggressive way. You can tag it and say, 'Let's try to see if the agent can get it this time.' And they close the loop and if it's a good experience, that really helps people try it out on their own." The property doing the work is that the demonstration is addressed to a shared task rather than at the skeptic, so a failure costs nothing socially. ([Blum](../sources/20260828_5Bn0xro2ol8.md), 15:28-16:36)
- **The design rule underneath "meet them where they work": every new surface is activation energy charged to an unconvinced user.** Shenoy's phrasing makes the cost explicit — bring "products to their systems so that the energy required for enablement is kept low" — and his list of destinations is the non-engineering equivalent of the IDE and the merge request: "a product that's natively embedded into Excel or into their ERP system, maybe their 3D design software, or maybe even their Microsoft products like Outlook, Gmail." He pairs it with the half this page does not cover: the requirements for such an embedding cannot be gathered remotely, because "you cannot co-design software with the services business over Zoom or over a support ticket." ([Shenoy](../sources/20260828_B0fjR3yaZFU.md), 16:08-16:38, 17:02-17:14)

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent experience prioritizes APIs, CLIs, and MCP over dashboards](agent-experience-prioritizes-apis-clis-and-mcp-over-dashboards.md)
- [Treat agent APIs as asynchronous task lifecycles](treat-agent-apis-as-asynchronous-task-lifecycles.md)
- [Design coding-agent editors as review surfaces](design-coding-agent-editors-as-review-surfaces.md)
- [The Best Engineers Adopt Agents Last, and Their Objections Are the Roadmap](the-best-engineers-adopt-agents-last-and-their-objections-are-the-roadmap.md)
- [Co-Design In Person Because Remote Channels Filter the Requirements](co-design-in-person-because-remote-channels-filter-the-requirements.md)

Sources:
- [Your Support Team Should Ship Code - Lisa Orr, Zapier](../sources/20251216_RmJ4rTLV_x4.md), 05:40-12:39
- [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](../sources/20260828_5Bn0xro2ol8.md), 15:28-16:36
- [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](../sources/20260828_B0fjR3yaZFU.md), 16:08-17:14
