# Route each change to the proof it needs

Summary: The "read every line" vs. "code is free, don't read" debate is a false binary between people; the durable framing is a per-task routing decision. The same engineer should read every line of some changes and barely inspect others, so replace "should I still read code?" with "what proof does *this specific change* need?" and route each change to the review it requires.

Use when:
- Deciding how much human review an individual agent-generated PR or change deserves.
- Setting team policy that neither mandates line-by-line review of everything nor allows unreviewed merges.
- Explaining why a single engineer can rationally YOLO one change and scrutinize the next.

Details:
- The framing is the Z/L Continuum, an axis between Mario Zechner ("slow down, read every effing line") and OpenAI's Ryan Lopopolo ("code is free, humans no longer need to concern themselves with implementation"). The mea culpa is that the continuum is real but is about *tasks, not people*: "Same engineer could be a Lopopolo on one piece of code and has to be a Zechner on other pieces of code. Different tasks just need different proof." (12:17-12:24)
- The two extremes converge more than the rhetoric suggests. Lopopolo's mechanism is "move attention up the layer" — humans are unreliable at catching repeated same-type mistakes, so when you catch one in review, encode it once as documentation, a linter, or a reviewer; "inspect the system, not every line." Zechner's mechanism is "route by task": non-critical, let it rip; critical, read every line. (13:18)
- How to know what's critical: read the code — or ask the agent. A model is good at scanning a large repository and flagging which lines and primitives are critical, so agents can help route the review, not just produce the code. (13:49)
- The routing table (the "Monday artifact," a slide meant to be screenshotted — "route the change to the proof it needs") (14:35-15:40):
  - Read every line yourself of authentication, money movement, permissions, and irreversible data — inspect the critical path directly.
  - Decompose long PRs into atomic reviewable PRs; agents are good at decomposing, so ask them to, because eyes glaze over a 5,000-line diff exactly when it needs the most thought.
  - Verify with traces, evals, and shadow mode — the software-engineering discipline of verification does not go away.
  - Separate the writer from the reviewer/tester: "if I came up with an exam and then took it and scored myself, it's not productive."
  - Engineer rails, observability, and rollback — "build the system that builds the system, because read spends your attention once."
- Capability drift makes this framing time-dependent: rising model capability pushes everyone toward the Lopopolo end, and the review layer moves — yesterday inspect outputs and read code, today inspect task direction, maybe tomorrow inspect the loops. "Capability drift changes where proof belongs; it doesn't remove the requirement of proof." (17:42-17:57) The Anthropic Fable-5 framing echoes it: "we used to check if Claude is doing the work right; now I check if Claude is doing the right work," and Karpathy: "it's never felt so tempting to stop looking at code at all — but don't do this in production." (16:28)
- The closing rule of thumb: "Not every line in 2026 needs your eyes. Every system still needs your judgment." (21:13)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)

Sources:
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 12:17-21:13
