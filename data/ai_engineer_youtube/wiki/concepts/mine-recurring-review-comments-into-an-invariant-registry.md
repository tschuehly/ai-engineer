# Mine Recurring Review Comments Into an Invariant Registry

Summary: A large share of the comments a team writes in code review are the same comments repeated. Mine the review history in bulk, codify the repeatable ones as invariants, and feed them into the automated check that produces the test plan — so each recurring comment becomes a guardrail rather than a thing a human keeps rediscovering. Jain calls the artifact an "AI slop registry."

Use when:
- Standing up automated review for a team that already has years of review history.
- Deciding what an AI reviewer should check beyond generic bug-finding.
- Looking for a concrete first step that improves review throughput without buying a product.

Details:
- The observation: reviewing manually, "we are essentially possibly identifying the same issues over and over again. Can we actually capture these concepts and codify them so that we don't have to always create those review feedback one by one[?]" (06:53-07:23)
- The homework, which is the operational form of the concept: "Go home and mine your last 1,000 review comments and build out a[n] AI slo[p] register for the things which are repeatable. So, a vast majority of the comments that you're providing in your code review are something that we repeat over and over again." (14:12-14:33)
- The payoff and its shape: "This compounds with every merge[d] PR. Every time you capture something as a register, you don't have to capture that comment again," and "every recurring comment is now a guardrail that you don't have to review again." (07:52-07:57, 14:33-14:41)
- The cost, stated plainly: "It does follow a J curve. So, pain is real. You will have to spend some time to actually make it pay off because initially creating a registry can take some time." Expect the throughput to get worse before it gets better. (14:58-15:08)
- Where the registry is consumed: not only as reviewer prompts but as the *invariant* half of the verification input — "the criteria plus invariant is what makes the test plan," with acceptance criteria coming from the session and invariants from the registry. That is what makes this more than a lint file: the same codified rules end up asserted against a running preview. (08:30-08:39, 10:30-10:35)
- The framing Jain uses for why it improves over time — "think of this as… you're doing more training on top of the standard LLM" — is an analogy for accumulated in-context guidance, not weight training; nothing in the talk describes fine-tuning. (07:23-07:40)
- Difference from the wiki's existing lesson-to-guardrail pattern: Lopopolo's version converts each newly caught incident into a bespoke lint or reviewer prompt going forward. This version is retrospective and bulk — the corpus of past comments already contains the rules, so the first move is mining rather than waiting for the next incident. The two compose: mine the backlog once, then keep appending.
- Boundary worth keeping in view: a registry only absorbs the *repeatable* comments. The talk's own argument is that the non-repeatable ones — architectural feedback, mentorship, what was tried and rejected — are the alignment half that must stay human, so a growing registry should shrink review volume without being expected to reach zero.

- **Independent confirmation that the mining is cheap, and that the cost sits immediately after it.** At Uber "writing the skill was very easy. Like teams just very quickly wrote a skill by asking Claude to write one, go over my previous PR reviews and write me a skill" — the same retrospective corpus this page recommends, harvested by a model in minutes rather than as a project. What replaced the authoring cost was operating cost: "the hard part was how to run these skills at scale with consistent quality and low cost. And that required a lot of iterations not only from the uReview team side, but also like for each team who was trying to write these rules." Read against the J-curve warning above, the pain may be relocating rather than disappearing — from writing the registry to running it — and neither source measures the second half. See [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md). ([Bond and Ketkar](../sources/20260828_EL123UNokkI.md), 09:43-10:12)

- **A flat mine has no tiebreak, and the review graph already contains one.** Unblocked mines the same corpus — "it looks at pull request data… and it generates a series of best practices that help align agents to your codebase" — and then ranks the surfaced results by author: "we use the sort of seniority or expertise as a signal to boost comments that are important." That addresses a gap this page leaves open, since a bulk mine of years of comments contains settled conventions and one-off opinions side by side with no way to order them. The cost is that seniority is a proxy that calcifies, so a boosted corpus needs its own decay pass. See [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md). ([Werry](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:40)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use Reviewer Agents and Lints to Turn Review Lessons Into Guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Make Intent and Evidence the Review Surface](make-intent-and-evidence-the-review-surface.md)
- [Code Review Carries Alignment, Not Just Correctness](code-review-carries-alignment-not-just-correctness.md)
- [AI review gates turn standards into executable feedback](ai-review-gates-turn-standards-into-executable-feedback.md)
- [Automation loops convert repeated review and triage into factory improvements](automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md)
- [Encode non-functional requirements as agent-visible context](encode-non-functional-requirements-as-agent-visible-context.md)
- [Use agent logs and review feedback as context observability signals](use-agent-logs-and-review-feedback-as-context-observability-signals.md)
- [Distributed Rule Authoring Is a Platform Problem, Not an Authoring Problem](distributed-rule-authoring-is-a-platform-problem.md)
- [Weight Mined Review Guidance by the Author's Expertise](weight-mined-review-guidance-by-the-authors-expertise.md)

Sources:
- [How to Kill the Code Review — Ankit Jain, Aviator](../sources/20260817_YgEv7IQzGdM.md), 06:53-07:57, 08:30-08:39, 10:30-10:35, 14:12-15:08
- [Building uReview, Uber's Multi-Agent Code Review Engine — Will Bond & Ameya Ketkar, Uber](../sources/20260828_EL123UNokkI.md), 09:43-10:12
- [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](../sources/20260827_qdAkxLoYNI8.md), 12:44-13:40
