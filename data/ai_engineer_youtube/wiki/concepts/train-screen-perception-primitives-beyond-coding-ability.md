# Train Screen-Perception Primitives Beyond Coding Ability

Summary: Coding ability is what made agents able to drive computers through MCP, APIs, and browser automation, but it is not sufficient for computer use. The model itself needs four screen capabilities — grounding, semantic understanding, change detection across an action history, and reconciliation of multiple incomplete observation sources.

Use when:
- Deciding whether a computer-use failure is a harness problem or a model-capability problem.
- Choosing what to train or evaluate in a model intended to operate real UIs.
- Designing the observation channel (screenshots, DOM, accessibility tree) for a browser or desktop agent.

Details:
- Why the transfer was expected: once RL produced good coding agents, they could be pointed at email, chat, docs, and the web, "because all of these tasks can be represented as code, as coding tasks" — chat/email/docs through MCP or API calls, the browser through Playwright/JavaScript/WebMCP, the web through search APIs. "So in theory, coding agents can be really good at computer use." ([From RL to IRL](../sources/20260814_Cc0_nyxROBA.md), 03:23-04:05)
- The bet against that: "one of our biggest bets is that coding abilities are not sufficient to do well on computer use. The model needs to be able to look at the screen the way we humans look at a screen and then make sense from it." (11:04-11:18)
- The four capabilities (11:21-12:20):
  - **Grounding** — "computer screens are very dense," so the agent must resolve layout and locate text and controls.
  - **Semantic understanding** — "what is the purpose of the different things, what to pay attention to for the task that it's trying to do." This is the capability that distinguishes a sponsored button from the real submit button.
  - **Change detection** — after every action a screenshot is appended to the model context, so the model holds a history; it must work out "what are the changes that are happening, are they desirable," and what to do next. Having the screenshots is not the same as reading the delta.
  - **Multi-source observation** — with several incomplete sources, learn "what to expect from each of those" and what to attend to for the task at hand.
- The multi-source problem is concrete, not abstract: the DOM lacks dynamically generated content and did not contain the sponsored ad's text "because it was embedded into the image," while the screenshot contained it but can be truncated by scroll position. The agent is handed both and is not told which to trust for what. (06:37-07:11)
- Placement matters: "all of these capabilities need to be baked into the model," in contrast to the harness features listed later in the same talk. This is the model-side half of the same problem the runtime-side sources attack by [rebuilding what the agent sees](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md) — the two are complements, and a lab that trains the model expects the runtime workaround to become unnecessary over time ([the thinning harness](keep-the-harness-thick-early-and-thin-it-as-the-model-improves.md)).
- Change detection is the model-side counterpart of the runtime pattern of feeding step-by-step deltas and of [verifying an action through a different channel than the one that acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md): both exist because "the click returned" does not mean the screen changed the way the agent intended.

Related topics:
- [Models](../topics/models.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Compose Computer-Use Agents From Reliable Atomic Actions](compose-computer-use-agents-from-reliable-atomic-actions.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Give Browser Agents a Compact Whole-Page Representation](give-browser-agents-a-compact-whole-page-representation.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Map RL Assumptions to Deployment Realities for Computer-Use Agents](map-rl-assumptions-to-deployment-realities-for-computer-use-agents.md)

Sources:
- [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](../sources/20260814_Cc0_nyxROBA.md), 03:23-04:05, 06:37-07:11, 11:04-12:20
