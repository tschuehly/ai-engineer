# Harness Engineering Shifts Scarcity From Code Production to Control Surfaces

Summary: Harness engineering treats coding-agent capacity as abundant and moves the engineering bottleneck to control surfaces: task framing, delegation, review, context, guardrails, and team process. The useful work is not merely producing more code, but making agent-produced code reliably land inside the team's quality bar.

Use when:
- Designing how a team should work when coding agents can run many implementation attempts in parallel.
- Deciding whether to invest in prompts, rules, CI checks, review automation, and repository structure rather than more manual implementation time.

Details:
- Lopopolo argues that implementation is no longer the scarce resource; the scarce resources are human time, human/model attention, and the model context window. (02:09-05:23)
- The new engineering role is to productively deploy agent capacity into codebases and teams through systems thinking, system design, and delegation. (02:47-03:09)
- Lower-priority work can be kicked off in multiple parallel attempts and then selected from, but only if the surrounding harness can route attention, review, and integration responsibly. (05:40-06:05)
- The talk frames every engineer as closer to a staff engineer: responsible for looking days, weeks, and months ahead to build structures that make large amounts of agent output useful. (04:44-05:05)
- Talha Sheikh (Checkout.com) reaches the same conclusion from a coding-agent field report: value used to sit in "the code that we create" but "in reality it's the verification that we design," so "it's not about can you code, but can you verify?" His TLDR — "work on the harness, and not on the code" — restates that engineering leverage has moved to the control surface (here a deterministic verification/enforcement layer), and he notes the same convergence across Anthropic, OpenAI, CodeRabbit, and WorkOS. ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 08:22-08:51)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Coding agents shift engineering work toward planning and review](coding-agents-shift-engineering-work-toward-planning-and-review.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md)

Sources:
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md), 02:09-06:05
- [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../sources/20260708_MpZzWMdmQCE.md), 08:22-08:51
