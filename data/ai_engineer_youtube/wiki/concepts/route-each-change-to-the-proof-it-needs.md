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
- Maven Clinic supplies a team-policy implementation of the routing decision and moves the call to the *author*: "we allow engineers to self-identify whether they still need code review. If they think this PR is simple enough, I feel very confident, I don't need anybody to take a look… We let them merge, but we still hold them accountable." Routing without mandatory review only works because accountability does not transfer — the author cannot buy safety by opting out. The rest of the policy constrains what can be routed at all: a 500-line cap per PR and stacked PRs for large features, which is the "decompose long PRs into atomic reviewable PRs" row of the routing table enforced as a limit rather than left to judgment. (Maven Clinic, 11:43-12:32)
- Capability drift makes this framing time-dependent: rising model capability pushes everyone toward the Lopopolo end, and the review layer moves — yesterday inspect outputs and read code, today inspect task direction, maybe tomorrow inspect the loops. "Capability drift changes where proof belongs; it doesn't remove the requirement of proof." (17:42-17:57) The Anthropic Fable-5 framing echoes it: "we used to check if Claude is doing the work right; now I check if Claude is doing the right work," and Karpathy: "it's never felt so tempting to stop looking at code at all — but don't do this in production." (16:28)
- The closing rule of thumb: "Not every line in 2026 needs your eyes. Every system still needs your judgment." (21:13)

- **The same rule applied to review depth at Uber's scale, with the selection layer deliberately kept deterministic.** "We need the ability to take factors like the risk profile and the complexity of a code change and factor that in when deciding how we're going to run a code review. Not all code gets the exact same review." The implementation is "a smart deterministic routing so that we could route which team gets what kind of review with which model, what kind of generators, and so on" — the choice of proof is computed from ownership and risk, and only the proof itself is a model. That split is what keeps cost and latency predictable across hundreds of team configurations, and it is the part a router built as an LLM classifier gives up. ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 02:25-02:43, 09:05-09:16)

- **A literal top rung for this page's metaphor, priced.** "Pick your most critical code, write what correct means, which is the specification… and then you can let your coding agent implement it and your formal verification tool prove it" is the same routing rule stated by someone whose top rung is a machine-checked proof — and Cedar, an authorization policy engine, sits squarely on this page's read-every-line list of authentication, permissions, and irreversible actions. The reason it stays a routing decision rather than a default is cost: converting zlib, one C compression library, took "a week or so" and produced "32,000 lines of proof." ([Pant](../sources/20260828_lRa9sPaMyy4.md), 04:41-05:56, 09:17-09:35)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Keep critical code inside human understanding and review capacity](keep-critical-code-inside-human-understanding-and-review-capacity.md)
- [Choose plan-heavy or review-heavy agent workflows by task shape](choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Self-verifying agent loops hide review rather than remove it](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [Comment Volume Is a Property of the Review Pipeline, Not the Model](comment-volume-is-a-property-of-the-review-pipeline.md)
- [Pick a Verification Route by Which Translation You Can Afford](pick-a-verification-route-by-which-translation-you-can-afford.md)

Sources:
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](../sources/20260710_ZpK5PWX2YRM.md), 12:17-21:13
- [How to build an AI-Native Health Company — Dan Feng, Maven Clinic](../sources/20260819_WJRdLNhrsLQ.md), 11:43-12:32
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 02:25-02:43, 09:05-09:16
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 04:41-05:56, 09:17-09:35
