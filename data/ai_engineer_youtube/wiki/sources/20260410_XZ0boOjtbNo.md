# AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)

Source: [AI Didn't Kill the Web, It Moved in! - Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](https://www.youtube.com/watch?v=XZ0boOjtbNo)
Uploaded: 2026-04-10
Transcript: `raw/20260410_XZ0boOjtbNo/XZ0boOjtbNo.en-orig.vtt`

## Summary

This talk frames the web as both an agent-built and agent-consumed runtime: coding agents can be steered with repository skills, AGENTS.md instructions, browser automation, and Chrome DevTools MCP; browser-integrated AI can debug console, network, CSS, and performance traces; experimental Web AI APIs can run local browser models for summarization, proofreading, and multimodal prompting; and agent-readable web surfaces such as `llms.txt` and WebMCP can make sites easier for agents to navigate and operate.

## Extracted Concepts

- [Repository skills and AGENTS.md encode repeatable web-agent workflows](../concepts/repository-skills-and-agents-md-encode-repeatable-web-agent-workflows.md) - this source shows skills plus AGENTS.md turning GitHub issue work, Playwright recording, tunnels, and notifications into repeatable coding-agent behavior.
- [Browser DevTools MCP turns runtime debugging into agent tools](../concepts/browser-devtools-mcp-turns-runtime-debugging-into-agent-tools.md) - this source shows Chrome DevTools exposed as MCP tools for navigation, screenshots, console, network, Lighthouse, and performance analysis.
- [Browser-native AI APIs bring local models into web apps](../concepts/browser-native-ai-apis-bring-local-models-into-web-apps.md) - this source demonstrates experimental Web AI APIs for summarization, proofreading, prompt calls, multimodal input, and local model download behavior.
- [Agent-readable web surfaces guide browsing agents](../concepts/agent-readable-web-surfaces-guide-browsing-agents.md) - this source connects `llms.txt`, `llms-full.txt`, and WebMCP to the problem of making sites discoverable and actionable for agents instead of only humans.

## Topic Links

- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Skills are described as lightweight text-format plugins loaded when their description matches the current task, with fuller instructions brought into context only when needed. (02:18-05:42)
- The demo uses repo-local skills for GitHub CLI issue discovery, front-end design, Playwright recording, local tunneling, and Telegram notification, then uses AGENTS.md to require a short video, local tunnel, phone URL, and no issue closure before human confirmation. (03:46-07:29)
- Chrome DevTools MCP is presented as a way for agents to call browser and DevTools capabilities such as clicking, filling forms, console and network inspection, Lighthouse audits, navigation, screenshots, resizing, network throttling, and performance traces. (08:15-13:44)
- The speakers show AI assistance inside DevTools for CORS console errors, failing network requests, performance traces, selected DOM/CSS elements, live CSS changes, and applying changes back to a workspace. (16:05-23:24)
- The Web AI API section shows browser-local summarization, proofreading, writer/rewriter, prompt, image, audio, top-k, temperature, model event logs, token counts, and a one-time local model download around 4 GB, while warning that the APIs are still experimental and can change. (23:31-35:29)
- The agentic-web section frames `llms.txt` as a Markdown map for agents to find documentation and `llms-full.txt` as a single-file content variant, then presents WebMCP as a proposal for web apps to expose agent-callable tools rather than forcing agents to mimic human clicks from screenshots or the DOM. (36:03-42:57)
