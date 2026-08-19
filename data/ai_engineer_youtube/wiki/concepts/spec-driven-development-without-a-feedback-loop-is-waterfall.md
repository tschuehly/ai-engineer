# Spec-Driven Development Without a Feedback Loop Is Waterfall

Summary: Write spec → hand to agent → verify is structurally the 1970 waterfall model: requirements, specification, implementation, verification, and no feedback loop. The spec is authored before the unknowns are discovered, the implementer is nondeterministic, and the issues found during implementation rarely make it back into the document — which is why teams keep returning to interactive coding sessions even when they have a spec.

Use when:
- Adopting or evaluating a spec-driven workflow for coding agents.
- Explaining why an approved spec did not prevent mid-implementation renegotiation with the agent.
- Deciding which artifact a team should treat as the record of what was actually decided.

Details:
- The shape of the criticism: "Spec[-driven] development is like, okay, we write a spec… it covers all the details, we pass it to an agent, it generates a code, and then we verify. So, what's wrong here? If you look back in 1970, this is what waterfall model was… But, there's no feedback loop." (04:36-05:00)
- First failure: order of discovery. "The spec is written before we identified everything else… That's why today everyone still wants to use your coding sessions, whether it's [Claude] Code, Codex, Cursor… the reason you're interacting with agents is because there were certain things which were not clear in the spec." (05:00-05:20)
- Second failure: the document goes stale by construction. "As you implement, you identify more issues, and you never go back and update the spec, because… if you're doing the spec[-driven] development, it's already done." (05:20-05:29)
- Third failure: the implementer is not deterministic. "Once the spec is done, you expect… the code will come deterministically. But guess what? LLM is not deterministic. It's going to make decisions itself." A spec that assumes deterministic expansion under-specifies exactly the decisions the model will end up making alone. (05:29-05:38)
- The verdict is a qualification, not a rejection: "spec[-driven] development is a great methodology, but it falls short in day-to-day software development," and the part worth carrying forward is intent rather than the document. (05:38-05:56)
- The wiki's spec-driven pages are consistent with this once read as prescriptions against the failure modes above rather than as an endorsement of up-front specs. Kiro's practice is to keep specs feature-scoped, amend them when current work changes them, and delete them when stale — which is exactly the missing feedback loop, added by hand and by discipline. Treat "does this workflow have a path back from implementation into the spec?" as the test that separates the two readings.
- Corollary for teams that keep the up-front spec anyway: the spec is then a snapshot of pre-implementation belief, not a record of what was decided, so something else has to hold the decisions made after it was written.

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Capture the Coding Session as the Intent Record](capture-the-coding-session-as-the-intent-record.md)
- [Spec-driven development turns prompts into requirements, design, and tasks](spec-driven-development-turns-prompts-into-requirements-design-and-tasks.md)
- [Keep spec artifacts feature-scoped, mutable, and context-backed](keep-spec-artifacts-feature-scoped-mutable-and-context-backed.md)
- [Spec-driven development is a tool-portable pattern, not a single product](spec-driven-development-is-a-tool-portable-pattern.md)
- [Collaborative plans become executable agent context](collaborative-plans-become-executable-agent-context.md)
- [Retire completed planning docs before they become agent doc rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 04:36-05:56
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md), 48:49-55:24
