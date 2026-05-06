# Browser DevTools MCP turns runtime debugging into agent tools

Summary: A browser DevTools MCP server can let agents inspect and operate a live web application through structured runtime tools instead of relying only on static code or screenshots.

Use when:
- Giving a coding agent browser access for front-end QA, debugging, or performance analysis.
- Deciding whether a web workflow needs Playwright, Chrome DevTools, Lighthouse, network traces, or screenshots as agent-callable tools.

Details:
- Chrome DevTools MCP is presented as a server that exposes browser and DevTools capabilities to an agent through MCP. (08:28-09:18)
- The available tool surface includes clicking, filling forms, console messages, network requests, Lighthouse audit, navigation, screenshots, resizing, and related browser operations. (09:18-09:29)
- In the demo, the agent starts the app, opens Chrome, navigates to the page, takes screenshots, and can test performance under different network conditions. (09:36-11:09)
- DevTools performance tools let the agent gather traces across fast, 3G, and slower network profiles, then report metrics such as LCP, CLS, critical path latency, and render-blocking or image-size recommendations. (10:51-13:44)
- DevTools AI assistance can also analyze console errors, failing network requests, performance traces, selected DOM elements, and live CSS changes, with the option to apply workspace-backed CSS edits instead of losing temporary browser tweaks. (16:05-23:24)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Hackable agent runtimes need tight safety boundaries](hackable-agent-runtimes-need-tight-safety-boundaries.md)
- [Agent tool loops turn model-required actions into executable results](agent-tool-loops-turn-model-required-actions-into-executable-results.md)

Sources:
- [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](../sources/20260410_XZ0boOjtbNo.md), 08:15-13:44, 16:05-23:24
