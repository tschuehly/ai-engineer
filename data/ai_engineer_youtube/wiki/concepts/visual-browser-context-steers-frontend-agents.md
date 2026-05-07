# Visual Browser Context Steers Frontend Agents

Summary: Frontend coding agents need rendered UI feedback, not only source files. Browser previews, selected elements, screenshots, HTML, CSS, and browser-test tools let users point at visible problems and give the agent concrete runtime context.

Use when:
- Steering a coding agent on UI changes whose code location is not obvious from the visual symptom.
- Equipping an IDE or agent workflow with browser evidence and frontend verification tools.

Details:
- In the VS Code demo, the agent can run the app, open the built-in browser preview, and accept selected element context that includes visual evidence plus HTML and CSS for the chosen UI. (22:16-24:07)
- This makes frontend requests more precise: the user can ask for changes to a visible header or progress indicator without first naming the responsible component or stylesheet. (22:16-24:07)
- Playwright MCP is presented as a complementary tool surface for browser testing, screenshots, website execution, and accessibility auditing through VS Code's MCP server configuration. (56:23-58:38)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use multisensory feedback loops for coding-agent validation](use-multisensory-feedback-loops-for-coding-agent-validation.md)
- [Browser DevTools MCP turns runtime debugging into agent tools](browser-devtools-mcp-turns-runtime-debugging-into-agent-tools.md)
- [Autonomous browser verification finds painted-door failures](autonomous-browser-verification-finds-painted-door-failures.md)

Sources:
- [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](../sources/20250803_eOxOzcw70f0.md), 22:16-24:07, 56:23-58:38
