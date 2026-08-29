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
- **A cheaper containment than approval, from a source whose agents already write.** Berry's rule is structural rather than procedural: agents get their own CRM columns, and "I always recommend separating the fields that agents are updating from the fields that deterministic systems are updating or that people are updating." That does not make the write correct, but it stops a wrong agent value from overwriting a right human one, which is the specific mechanism by which a bad write propagates silently into forecasts and routing. It is a third option alongside read-only and human-approved, and it is the one available to a team that cannot afford to gate every field. See [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md). ([Berry](../sources/20260826_UhCY231d0FQ.md), 12:23-12:43)
- **A fourth deployment with the same shape, and the write path described as pre-fill plus a thumbs-up.** Ramp's shipped vertical is a read — the pre-meeting brief — while the CRM write is stated as next: "we want to be able to generate things like post-meeting follow-ups and things like automatic CRM updates, which can pull in the transcript and say, 'Hey, we discussed this potential expansion opportunity. Let me go and pre-fill all the information needed to create that opportunity, get a thumbs up from my rep, and just make it happen.'" Note the specific division of labor: the agent does the extraction and the field mapping, and the human supplies only the decision to commit — which is the cheapest possible gate, and also the one most vulnerable to becoming a reflex. ([Vaziri](../sources/20260826_VjEP0xqTUI0.md), 13:02-13:28)

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
- [Give Agents Their Own Fields in the System of Record](give-agents-their-own-fields-in-the-system-of-record.md)
- [Gate a Generated Multi-Channel Campaign on the Channel Owner](gate-a-generated-multi-channel-campaign-on-the-channel-owner.md)

Sources:
- [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](../sources/20260826_Qw_tC68KKes.md), 12:36-14:28, 17:08-18:49
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 11:07-12:43
- [The Building Blocks of GTM Orchestration — Arman Vaziri, Ramp](../sources/20260826_VjEP0xqTUI0.md), 13:02-13:28
