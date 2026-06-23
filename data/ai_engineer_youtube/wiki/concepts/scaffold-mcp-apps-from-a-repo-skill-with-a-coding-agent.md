# Scaffold MCP Apps From a Repo Skill With a Coding Agent

Summary: You do not hand-author an MCP app from scratch — you borrow the official skill from the Model Context Protocol repo, edit it, and run it through a coding-agent CLI (GitHub Copilot CLI, Claude, or similar) so the agent scaffolds the three-part app: a tool, a bundled HTML resource (the UI), and the server-recognized link between the tool's data response and a renderable UI.

Use when:
- Building an MCP app / chat-rendered UI and deciding how to bootstrap it rather than writing the server, resource, and wiring by hand.
- Reasoning about how a published skill turns a coding agent into a repeatable scaffolder for a specific artifact type.

Details:
- The build is a coding-agent workflow, not a framework setup: the speaker took a skill from the Model Context Protocol repository (from Anthropic), edited it a little, and ran it through GitHub Copilot CLI to "spit out a number of different MCP apps" — flame graph, markdown viewer, flight status, and color picker as generic starters. (09:59-10:24)
- The skill carries the build instructions: it tells "Copilot CLI or Claude or whatever AI tooling you're using" how to set the app up and exactly how to run it, with code examples such as handlers and tool visibility — so the skill is the durable, tool-agnostic artifact and the coding agent is interchangeable. (11:03-11:31)
- An MCP app has three main parts (per the repo README the skill follows): (1) the **tool**, called by the LLM and the host; (2) the **resource** — the bundled HTML UI, which can be React, Vue, Svelte, or vanilla JS, "however you want to render your UI"; (3) the **link** between the two, which the server recognizes between the actual data response and a UI being available to render. (10:26-10:57)
- Tool visibility is a scaffolding decision the skill exposes: configure who invokes the tool — the model only, the model and the app, or just the app. (11:10-11:31)
- Concrete shape from the demo: the generated app's MCP server runs on localhost and is written in TypeScript (per the skill), profiles a Go program with `pprof`, returns JSON, and is paired with a React front end ("flame app") using hooks that receives the tool input/results and renders the view. (11:31-13:30)

Related topics:
- [Tools](../topics/tools.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [MCP Applications Ship UI and Tools Together](mcp-applications-ship-ui-and-tools-together.md)
- [Agent skills package progressive-disclosure context for repeatable workflows](agent-skills-package-progressive-disclosure-context-for-repeatable-workflows.md)
- [Ship skills over MCP for server-authored tool guidance](ship-skills-over-mcp-for-server-authored-tool-guidance.md)
- [Render Third-Party Generative UI Through a Double Iframe](render-third-party-generative-ui-through-a-double-iframe.md)

Sources:
- [Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub](../sources/20260606__xIwFcnHqp4.md), 09:59-13:30
