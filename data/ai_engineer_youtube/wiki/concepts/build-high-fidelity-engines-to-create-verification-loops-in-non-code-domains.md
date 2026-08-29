# Build High-Fidelity Engines to Create Verification Loops in Non-Code Domains

Summary: Coding agents work because they can run a compiler, linter, or tests and iterate on the results. To get the same iterate-on-feedback behavior in a domain that has no such tooling off the shelf, build the calculation/rendering engine yourself so the agent can check its own output — and make it high fidelity, because a partial engine produces worse results than none.

Use when:
- Adapting agents to a domain (spreadsheets, CAD, legal, simulation) where code-style compile/lint/test feedback doesn't exist.
- Deciding whether it's worth investing in a "source of truth" engine versus relying on the model's own judgment.
- Reasoning about which parts of an agent system are durable versus transient.

Details:
- Parallel to coding: a coding agent "does a much better job when it can run the compiler for your language or the linter or your tests and then iterate based on those results" — and the same is true of spreadsheets, but the feedback loop had to be built. (HEFSExa0xl0 09:28-10:20)
- Witan Labs built two engines to close the loop: a formula engine (to calculate the formulas) and a render engine (to render a range to an image with formatting and layout). The rendered output is "the source of truth… the verification loop" that makes the agent confirm it did the right thing and go fix the formula or formatting when it didn't. (HEFSExa0xl0 10:20-10:52)
- Rendering the artifact to an image lets the agent *see* what a human sees: an LLM does not perceive spreadsheet structure the way a human "instantly sees" a revenue table, assumptions, and a chart, so a render engine that produces the formatted image gives the agent the visual feedback it otherwise lacks. (HEFSExa0xl0 00:56-01:50, 04:03-04:20)
- High-fidelity requirement — a partial engine backfires: an engine implementing only ~50% of Excel's formulas produces *worse* results, because the agent writes a formula that would work in practice, computes it, and gets a wrong result or an error only because that formula isn't implemented. "That verification loop is really only as good as the engines that power it." (HEFSExa0xl0 10:52-11:19)
- The verification loop is the durable part; the interface is transient: a REPL is the best interface today because coding is what models are best at and may be superseded by computer use, but "what won't change is the need for that verification loop… the more durable part," and across four or five model releases "the more capable the model is, the more they can get out of that verification loop." (HEFSExa0xl0 11:21-12:37)
- Generalization: "if you're in a domain where those feedback loops don't actually exist, I think it's actually really worth spending the time to build that rendering engine or calculation engine or whatever applies to your particular domain." (HEFSExa0xl0 16:41-17:07)

- **What a maximally good oracle buys the loop, seen in the code domain.** Lean's proof search is a tree the agent walks with "tactics which are your moves" toward the theorem, backtracking whenever "for some goals, you're not able to prove it" — a loop that is only viable because rejection is immediate, cheap, and unarguable: "the kernel catches the mistake." That is the property to aim for when building an engine for a domain that has none. A partially faithful engine gives an agent something to fit itself to; an oracle that rejects without negotiation gives it something to search against. ([Pant](../sources/20260828_lRa9sPaMyy4.md), 03:16-04:14)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Give coding agents the same engineering infrastructure humans need](give-coding-agents-the-same-engineering-infrastructure-humans-need.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Pair an LLM Narrator With a Domain Solver Via Tools](pair-an-llm-narrator-with-a-domain-solver-via-tools.md)
- [Give Agents a Persistent-State REPL Instead of Many Tools](give-agents-a-persistent-state-repl-instead-of-many-tools.md)
- [Ship a Proof a Small Kernel Can Recheck, Not a Claim You Must Trust](ship-a-proof-a-small-kernel-can-recheck.md)
- [Curate Tasks by Live Human Demand and a Deterministic Verifier](curate-tasks-by-live-human-demand-and-a-deterministic-verifier.md)
- [Swap the Verifier to Retarget an Agent Arena](swap-the-verifier-to-retarget-an-agent-arena.md)

Sources:
- [Teaching Coding Agents to do Spreadsheets - Nuno Campos, Witan Labs](../sources/20260708_HEFSExa0xl0.md), 09:28-12:37, 16:41-17:07
- [Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers — Varun Pant, AWS](../sources/20260828_lRa9sPaMyy4.md), 03:16-04:14
