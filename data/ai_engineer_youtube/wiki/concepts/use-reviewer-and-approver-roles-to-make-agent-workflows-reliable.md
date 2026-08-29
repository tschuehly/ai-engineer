# Use Reviewer and Approver Roles To Make Agent Workflows Reliable

Summary: Agent workflows become more reliable when completion routes through explicit reviewer and approver roles instead of relying on one worker agent to remember every validation instruction.

Use when:
- A coding or operational agent often skips requested validation steps.
- Designing multi-agent review loops where quality checks and final acceptance are separate responsibilities.

Details:
- Paperclip's QA example gives a QA agent browser skills for opening sites, filling forms, and clicking buttons, then requires a review when an assignee finishes work.
- The talk separates a reviewer from an approver: a QA agent may iterate with the worker, while a manager or approver decides whether the reviewed work is sufficient for the organization's brand or standards.
- This workflow is positioned as a vendor-neutral alternative to per-agent hooks that behave differently across Claude Code, Codex, and other agents.
- The cited failure mode is prompt-only validation: asking a coding agent to test in the browser before handing work back often fails unless the workflow enforces the review path.
- **A two-stage version where the reviewer also selects among candidates, and a human approver sits behind it.** Notion's cold-outbound workflow runs a research sub-agent doing concurrent research, generates three email drafts that are scored, then "a review agent will pick the highest-scoring one and make any updates if necessary," looping to improve drafts before one lands in a rep's task box for human approval. The scorer is not described, which is the load-bearing omission: selection among candidates is only as good as the score it ranks by. ([Liu](../sources/20260826_L4I7WgiEquo.md), 13:52-14:23, 16:14-16:41)
- **A third role the reviewer/approver pair does not cover: framing.** Cloudflare's weekly go-to-market summary runs "a first pass draft on the data calling our MCPs, and then... a second reviewer agent who checks the veracity of the data, and then... a third agent, which is a tone agent, who using a multi-shot prompt is able to just craft the message and highlight the risks and opportunities equally." A veracity check cannot catch a summary that is accurate and buries the bad news, so the editorial objective is given its own stage and its own specification style — exemplars rather than rules. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 11:03-11:32)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Use independent validation contexts to reduce agent confirmation bias](use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Use reviewer agents and lints to turn review lessons into guardrails](use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)

Sources:
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md), 08:41-11:03
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 13:52-14:23, 16:14-16:41
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 11:03-11:41
