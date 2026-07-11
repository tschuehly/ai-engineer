# Engineer the Interaction, Not the Model, for Discernment

Summary: When a human-in-the-loop step degrades into a rubber stamp, the highest-leverage fix is often the interaction design, not a better model or more oversight. You can't change how a human behaves, but you can engineer the interface to elicit the reasoning you need — reframing the human as an investigator, surfacing assumptions and tradeoffs, and matching friction to the stakes.

Use when:
- A human review step is deferring to AI output instead of judging it independently.
- Designing the review surface for a high-stakes decision, a copilot, or a coding agent.
- Tempted to fix a human-oversight failure by retraining the model or adding reviewers.

Details:
- The cheapest lever can be copy: Duolingo fixed a 50% false-accusation rate among proctors with a single proctoring-guideline change emphasizing two things — (1) the AI signal is only a *preliminary alert* and the human is the *final decision-maker*, and (2) the human must find **independent evidence in the video footage before upholding a flag**. This lifted accurate rejections by **21%** (from 50% to ~71% correctly cleared), matching production, with **no change to the model or the UI**. ([source](../sources/20260707_CDqzWpwkSls.md), 08:22-09:11)
- Principle 1 — engineer the reasoning: decide what reasoning pattern you want from the human and make the interface challenge it. Reframe the human as an **investigator, not a validator**; don't ask "is this looking good?" — force a thoughtful, engaged effort. Surface the model's assumptions early and ask for sign-off to prevent downstream miscommunication; present options and tradeoffs with the reasoning so the user stays in control and can opine early. (18:50-20:18)
- Principle 2 — **match friction to the stakes**: friction is your friend where stakes are high. High-consequence review (visas, admissions) wants deliberately slow reviewers, so add well-structured review gates and speed bumps at exactly the high-stakes checkpoints so review can never become a rubber stamp. Low-oversight delightful surfaces (open chat with an AI) should instead be frictionless and seamless. (20:18-21:31, 25:41-25:51)
- Split conflated decisions so each judgment is honest: a headphone-detection flag that asked one yes/no ("flag it here?") hid two questions — did the model correctly detect headphones, and is this a violation? A hearing-aid wearer is a *true* detection but *not* a violation; answering "no" to avoid a false accusation feeds a wrong signal. Splitting into two questions produces more and better data. (11:56-13:23)
- Surface the same AI output differently to change the interaction: an LLM writing tutor that dumps 400 lines (praise → feedback → unrequested rewrite) is overwhelming and unnatural; a markup UI (green/yellow/red spans, hover for concise actionable feedback, accept inline, every note tied to a text span) mimics human peer review and enables incremental improvement — same model output, better surfacing. The coding-agent version: prefer an agent that behaves like a junior developer (plans, asks good questions, documents decisions, breaks work into reviewable PRs) over one that dumps a giant diff or pings "yes/yes/yes," because both extremes reduce the human to a rubber stamp. (13:23-18:50)
- Concrete interaction primitives: structured inputs/outputs (forms, tables, markup UIs) instead of walls of text; proactively highlighted assumptions the user confirms; deliberate friction and review gates; and explicit feedback collected at the correct touch points with nuance, not just thumbs up/down. The closing frame: "sometimes the fix is not a better model or more oversight, it's engineering the interaction itself." (23:40-25:51)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Automation Bias Turns Human-in-the-Loop Into a Rubber Stamp](automation-bias-turns-human-in-the-loop-into-a-rubber-stamp.md)
- [Treat Every Human-AI Interaction as a Training Label](treat-every-human-ai-interaction-as-a-training-label.md)
- [Choose AI coworker form factors by interaction mode](choose-ai-coworker-form-factors-by-interaction-mode.md)
- [Review Coding Agent Work at Task, Plan, and Code Checkpoints](review-coding-agent-work-at-task-plan-and-code-checkpoints.md)

Sources:
- [Build AI Systems for Discernment, Not Approval - Angel Ortmann Lee, Duolingo](../sources/20260707_CDqzWpwkSls.md), 08:22-25:51
