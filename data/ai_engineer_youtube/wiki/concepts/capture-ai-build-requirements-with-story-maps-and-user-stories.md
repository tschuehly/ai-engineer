# Capture AI-Build Requirements With Story Maps and User Stories

Summary: The business-analyst toolkit — value discovery (VAD + a 4-question value framework), story mapping, and the trained persona/what/need/why user-story structure with acceptance criteria — is the reusable method for deciding and capturing what an AI should build, and it produces better AI output than a generic prompt because models were trained on these familiar structures.

Use when:
- Turning a vague ask ("build us an agent that handles support") into a spec an AI can implement well.
- Running a pre-build discovery/mapping session before prompting a coding agent.
- Writing requirements artifacts to feed as context to an AI (store them in the repo).

Details:
- Start with value discovery, framed as the VAD path — Value → Architecture → Design: understand how value is created and what value the customer wants, then the underlying process/architecture that supports it, then design a system around it (and what process changes are needed). Skipping to a generic prompt "will not get the answer you want." (09:40-10:50)
- Qualify with a 4-question value framework: (1) Whose problem is this? — name a direct persona; (2) What does winning look like for them? — the right outcome, delivered quickly/smoothly/safely; (3) What would make them refuse to use it? — not on their platform, cumbersome, data-security; (4) Would it change a decision, and which one? Answering these elicits better AI responses; track all four "in a good old markdown file in your repository so that AI can access it" for far more context. (08:08-09:40)
- Story mapping captures the process backbone at the right altitude: for a support system, backbone stages contact → triage → resolve → close, with user stories beneath each. Slice "release one" (capture intent, classify urgency, draft a grounded answer, log to a system of record) as the MVP / first user stories; second-row stories (read sentiment, route to a team, suggest next action, check satisfaction) become the backlog. Keep it high-level so you can see the big picture and choose what to build. (04:43-07:00)
- Write each user story in the trained structure — persona / the what / the actual need / the why — plus acceptance criteria "based on which you can derive the test cases." Example: "As a support lead, I need to open cases ranked by urgency so that none of the escalations should slip." AI is strong at pattern recognition and "was actually trained on the user story structure," so a familiar structure gets better results; user stories also double as prompts to elicit stakeholder discussion. (06:30-07:50)
- Daisy-chain the connected user stories into a coherent system → specification → code. The software development life cycle doesn't change much under AI; the toolkit does — the newly scarce skill is the analyst toolkit (story mapping, business model canvas, value canvas, design thinking). (04:24-04:43, 07:20-08:00)

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Elicit Requirements as the Non-Automatable Bottleneck](elicit-requirements-as-the-non-automatable-bottleneck.md)
- [Measure Feature Adoption, Not Shipping Velocity](measure-feature-adoption-not-shipping-velocity.md)

Sources:
- [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](../sources/20260629_6bmM45jkMDY.md), 04:24-10:50
