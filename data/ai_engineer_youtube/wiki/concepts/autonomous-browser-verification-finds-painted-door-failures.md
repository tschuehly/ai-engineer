# Autonomous Browser Verification Finds Painted-Door Failures

Summary: Coding agents need autonomous browser-level verification to catch features that look complete but are not wired to real behavior. UI clicks, DOM inspection, logs, API calls, database checks, screenshots, and reusable Playwright tests provide feedback users cannot reliably supply.

Use when:
- Building web-app codegen agents that must validate generated UI without relying on user QA.
- Choosing between unit tests, API tests, browser-use tools, computer use, and reusable end-to-end tests.

Details:
- Replit calls unimplemented-but-visible features "painted doors": buttons without handlers, UI backed by mock data, or components not fully fleshed out. 08:31-09:10
- Internal evaluations found more than 30% of individual generated features broken on the first attempt, making broken features likely across generated apps unless the agent tests them. 09:10-09:24
- Non-technical users cannot be expected to click every button, inspect every field, or provide technical debugging feedback, so the agent must gather feedback from the app environment. 09:24-10:33
- Autonomous testing breaks the human-feedback bottleneck, prevents small errors from compounding, and checks whether model completion claims are real rather than hallucinated. 10:33-11:12
- Unit tests and API tests cover important but partial slices; browser verification is needed to test how a web app functions and looks. 11:12-12:05
- Replit combines browser interaction, database checks, logs, API calls, screenshots, and Playwright scripts; generated Playwright is expressive, LLM-manageable, and reusable as a regression suite. 12:05-14:56
- Antigravity adds a productized browser-verification surface: an agent-controlled Chrome browser can click, scroll, run JavaScript, retrieve DOM state, and produce a screen recording so the human can review what the agent actually tested rather than only a code diff. 03:14-04:24, 09:48-10:27
- Multimodal model understanding makes browser recordings and screenshots reusable feedback: the model can inspect the visual evidence it produced and iterate from there. 10:16-11:05
- The same browser-driving idea works as a *third-party benchmark verifier*, not only as the coding agent's own self-check: SWE-Marathon is "the first benchmark to use a computer use agent or CUA verifier" for full-stack product-clone tasks, because "unit test can pass, but the product is probably still unusable and the front end looks terrible." For a Slack-clone task, deterministic unit tests check the API/back-end, then a CUA "uses the browser like a human" — logging in, creating channels, posting messages, reacting with emotes — and scores the app against a rubric. The durable framing: "full stack evals are hard because correctness is not just an API contract. It's whether the user can actually complete the product's intended workflow." (SWE-Marathon 03:49-05:03)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Browser DevTools MCP turns runtime debugging into agent tools](browser-devtools-mcp-turns-runtime-debugging-into-agent-tools.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Do not report agent autonomy without quality accountability](do-not-report-agent-autonomy-without-quality-accountability.md)
- [Agent managers orchestrate editor, browser, and background agents](agent-managers-orchestrate-editor-browser-and-background-agents.md)

Sources:
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md), 08:31-14:56
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md), 03:14-04:24, 09:48-11:05
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](../sources/20260707_Rx8f05JI_WA.md), 03:49-05:03
