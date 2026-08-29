# Repository skills and AGENTS.md encode repeatable web-agent workflows

Summary: Repository-local skills and AGENTS.md instructions can turn a vague web-development request into a repeatable workflow with tool selection, browser evidence, preview sharing, and human confirmation rules.

Use when:
- Designing coding-agent workflows for web app feature work.
- Turning repeated local QA or notification rituals into durable agent instructions.

Details:
- The demo asks an agent to implement the first open GitHub issue; the agent uses a GitHub CLI skill to fetch the issue and then starts implementation without the prompt specifying the tool. (03:46-04:35)
- Skills are described as lightweight text-format plugins whose descriptions tell the coding agent when to load deeper instructions into context. (02:18-05:42)
- The repository includes skills for front-end design, Playwright CLI recording, public tunnels, and Telegram sending, so feature completion can include visual proof and a phone-testable URL. (05:45-06:58)
- AGENTS.md is used to make the workflow persistent: after a website change, record a short video with Playwright, run the dev server, create a tunnel, send the URL, and do not close the GitHub issue until human confirmation. (06:58-07:29)
- The notification/tunnel demo initially fails because a token file is not found, showing that workflow skills still need reliable credential and local-state handling. (13:53-14:22)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Treat prompts as distributed harness surfaces](treat-prompts-as-distributed-harness-surfaces.md)
- [Ship Bundled Docs and an AGENTS.md Inside the Published Package](ship-bundled-docs-and-an-agents-md-inside-the-published-package.md)

Sources:
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md), 02:18-07:29
