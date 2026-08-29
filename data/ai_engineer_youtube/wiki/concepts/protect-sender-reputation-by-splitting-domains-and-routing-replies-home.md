# Protect Sender Reputation by Splitting Domains and Routing Replies Home

Summary: Agent-generated outreach sent from a real employee address puts the company's whole domain reputation behind the model's output, so volume moves to secondary domains — which then creates two engineering problems the automation must own: routing replies back to the rep, and suppressing every other channel the moment one converts.

Use when:
- Deciding whether an agent sends as a named human, as itself, or from a separate domain.
- Assessing the blast radius of a badly targeted automated campaign.
- Building multi-channel outreach where a response on one channel must stop the others.
- Reviewing an outreach system whose reply handling was designed after its sending.

Details:
- The identity question is posed as a design choice with a shared-resource consequence: "do you email on behalf of the rep, or do you let the agent do the emailing? If you email on behalf of the rep, what that means is like everett@clay.com is actually reaching out directly to customers. But if I do that in the wrong way, or I don't get the replies that I need, that then means that my overall domain reputation is going to suffer for my company." ([Berry](../sources/20260826_UhCY231d0FQ.md), 14:39-15:07)
- **The externality is what makes this an architecture problem rather than a messaging one.** Deliverability is a company-wide asset consumed by every sender; one campaign that lands badly degrades transactional mail, support replies, and every other rep's outbound, none of whom were party to the decision. The blast radius is not the campaign.
- The standard mitigation buys isolation and immediately creates a routing requirement: "a common technique then is to use multiple domains to get in touch with customers. But then if I do that, I actually need to find a way to route responses on that domain back to my main domain so my reps can process it." (15:07-15:26)
- **The second execution problem is cross-channel suppression.** "If you get a call connection and a meeting booked on your call sequence, you then need to suppress your email sequence and maybe [unenroll] someone from a life cycle marketing campaign. So, the coordination of the execution of all of this is also a hard problem and also something that we can use agents to help resolve." A conversion on one channel is a stop event for every other, and each of those channels is usually a different vendor. (15:26-15:48)
- Both modes run concurrently in the described setup rather than one replacing the other: "a rep proxied view where we have a bunch of rep inboxes that are connected to our sequencer and we're actually sending that on behalf of reps. But like I said, we do this for kind of a portion of our accounts. For many of our accounts, we actually use multiple domains." The split is by account tier, so the same system needs both identity paths. (15:48-16:09)
- **Suppression is the orchestration problem from earlier in the same talk, at its highest stakes.** Unenrolling someone from a marketing campaign in a different vendor is exactly the cross-tool write that [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md) says cannot be assumed instantaneous — and here the cost of the lag is a prospect who just booked a meeting receiving a cold email.
- This is the deliverability-side complement to the policy control in [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md). Notion's rule forbids the agent from the channel outright; Berry's practice keeps the agent on it and isolates the reputational damage instead. The two are different bets about where the risk actually lands — content quality versus shared infrastructure — and a system running agents on outbound needs an answer to both.
- **Limit.** No numbers on any of it: no deliverability metric, no threshold at which reputation degrades, no domain count, no reply-routing implementation, and no evidence that the multi-domain split works better than restraint. Whether suppression is implemented in the orchestrator or in the sequencer is not stated. (14:39-16:09)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Workflows](../topics/workflows.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Size Agent Quality Against the Channel's Reply Rate](size-agent-quality-against-the-channel-reply-rate.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)
- [Make Routing and Eligibility a Shared First-Class Primitive](make-routing-and-eligibility-a-shared-first-class-primitive.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Treat Tool-to-Tool Orchestration as a Data Engineering Problem](treat-tool-to-tool-orchestration-as-a-data-engineering-problem.md)
- [AI Does Not Replace Shareable Product Marketing](ai-does-not-replace-shareable-product-marketing.md)

Sources:
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 14:39-16:09
