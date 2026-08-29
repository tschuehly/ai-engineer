# Verify an Action Through a Different Channel Than the One That Acted

Summary: An agent should confirm that an action landed using a sensing channel independent of the one it acted through — check the network, the screen, or the page state rather than the return value of the call it just made — because the acting channel reports that it fired, not that it worked.

Use when:
- Designing the verify step of a sense → act → verify loop for a browser, GUI, or API-driving agent.
- An agent reports success on steps that demonstrably did not happen.
- Choosing which observation channels a runtime must expose, and why more than one is needed.

Details:
- **The rule, stated plainly.** "You sense where you are. You make one move. You confirm that it landed." And the confirmation must come from elsewhere: "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen." ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 05:39-06:38)
- **Why the acting channel cannot verify itself.** A synthetic JavaScript click returns normally even when the page discards it for being untrusted — "there's no failure, there's no error, just nothing happens." Self-reported success is exactly the signal that is missing when the interesting failure occurs. See [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 10:43-11:32)
- **This is what makes multiple senses a requirement, not a luxury.** The usable subset of the Chrome DevTools Protocol organizes into *see* (DOM structure, accessibility-tree semantics, screenshot pixels), *hear* (network traffic, console and logs), and *operate* (clicks, keystrokes, navigation). A runtime that only exposes the operate channel plus one read channel cannot run an independent check. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 04:28-05:39)
- **The failed verification is the control signal.** In a loop-on-a-ladder design, a verify step that keeps failing is what tells the agent to escalate to a more human-like technique rather than retry the same one — so the quality of the verification channel determines whether escalation happens at all. See [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md). ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 06:26-06:47)
- **One action per iteration is part of the discipline.** The loop acts on exactly one thing — one click, one keystroke sequence, one selection — before verifying, so a failed check attributes to a specific action instead of a batch. ([Corey Gallon](../sources/20260814_26RtyAm9y_Q.md), 05:53-06:26)
- **It applies to code the agent writes, not only to clicks.** When a computer-use model executes JavaScript in the page instead of clicking, the screen remains the independent check: "the browser after all is an engine that can execute code, but it has a sort of formal verification system built in. It is seeing the screenshot — that is the source of the truth. So it knows whether it succeeded or not." Batra's operating rule keeps the two coupled — "click buttons when you have to, write code when you have to, and look at the result through pixels because that is the source of truth" — which is what makes a mixed click/code action space safe to expand. See [Pair Clicking With Generated Code and Replayed Network Requests](pair-clicking-with-generated-code-and-replayed-network-requests.md). ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 14:44-15:23)
- **Generalization beyond browsers.** The same independence requirement shows up wherever an agent's self-report is the cheapest available evidence: silent web-fetch failures produce confident hallucination unless the retrieval is checked separately ([Silent Web Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)), and coding agents need an external deterministic gate rather than their own claim of completion ([Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)).

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Climb a Humanness Ladder Only as High as the Page Forces](climb-a-humanness-ladder-only-as-high-as-the-page-forces.md)
- [Chrome Stamps Every Input Trusted or Untrusted](chrome-stamps-every-input-trusted-or-untrusted.md)
- [Silent Web Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Pair Clicking With Generated Code and Replayed Network Requests](pair-clicking-with-generated-code-and-replayed-network-requests.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)

Sources:
- [The Dark Arts of Web Automation — Corey Gallon, Rexmore](../sources/20260814_26RtyAm9y_Q.md), 04:28-06:47, 10:43-11:32
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 14:44-15:23
