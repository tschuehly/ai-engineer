# Read-Side Agents Scale First Because the Write Side Needs Approvals

Summary: Internal agent rollouts reach broad adoption on reads — queries, briefs, decks, summaries — long before they touch the systems of record, because writing into a CRM drags in quoting, approvals, and source-of-truth alignment; treat the read/write boundary as the actual sequencing rule rather than as a phase that got skipped.

Use when:
- Sequencing an internal agent program and deciding what to ship in the first year.
- Explaining to stakeholders why an assistant that answers everything still cannot update a record.
- Designing the control structure for an agent's first write path into a system of record.

Details:
- Every deployed use case named in the talk is a read or a generated artifact: forecast briefs, QBR decks, purchase decks, account planning, general data queries, renewal preparation, and the weekly summary. Nothing writes back. ([Joyce](../sources/20260826_Qw_tC68KKes.md), 08:57-14:28)
- **The write path is named as the harder class, and it is still in progress:** "the second thing is harder problems around quoting and approvals and updating the CRM itself. Uh we use Salesforce and we're just in the midst of building the connections and the ability for us to update Salesforce with these agentic systems." (17:51-18:04)
- The intended control is the pipeline that already earned trust on the read side: "I see that being set up in a way that I set up with that automated analysis where you have workflows to just make sure that everything is getting um done right" — reusing the drafter/checker shape from [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md) as the pre-write check. (18:04-18:11)
- **The second blocker is organizational, not technical.** Deeper integration — setting up meetings and embedding generated artifacts into them so reps do not have to pull them, and capturing meeting notes across the board — is blocked on "some information or some security setup" and on system-side work, which is what pushes a plausibly simple feature behind the write-path problem. (17:08-17:50)
- **Reads fail visibly and writes fail silently, which is why the asymmetry holds.** A wrong answer is discovered by the person who asked; a wrong CRM update propagates into forecasts, routing, and compensation before anyone reads it. The wiki's prior treatment of the same boundary places a lightweight operator verification between AI-generated call summaries and CRM sync for exactly this reason ([Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)).
- Quoting and approvals are not CRM writes with a bigger blast radius; they are workflows with existing human authorization structures, which is why they appear in the same sentence. An agent entering them has to be modeled inside the approval chain rather than in front of it.
- The governance concern the speaker raises about proliferating skills — "so that the source of truth in all the systems are aligning" — becomes materially harder once agents write, because divergent definitions stop producing merely divergent answers and start producing divergent records. (18:19-18:49)
- **Limit.** This is a snapshot of one rollout six months in, not a measured claim that reads must precede writes. The talk gives no timeline, design, or risk assessment for the Salesforce write path, and no source here reports an internal deployment that started on the write side to compare against.

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)

Related concepts:
- [Verify AI Call Summaries Before CRM Sync](verify-ai-call-summaries-before-crm-sync.md)
- [Keep Human Review on High-Risk Agent Operations](keep-human-review-on-high-risk-agent-operations.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Split a Generated Narrative Into Drafter, Fact-Checker, and Tone Agents](split-generated-narrative-into-drafter-checker-and-tone-agents.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)
- [Run a Submission-and-Review Alias for Shared Skills](run-a-submission-and-review-alias-for-shared-skills.md)
- [Stage the Internal Agent Roadmap From Answers to Automation to Team-Built Tooling](stage-the-internal-agent-roadmap-from-answers-to-automation-to-team-built-tooling.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 12:36-14:28, 17:08-18:49
