# Make Routing and Eligibility a Shared First-Class Primitive

Summary: Eligibility rules — who counts as which segment, what qualifies as a signal, who may receive what — get written independently into each tool that needs them, and the resulting contradictions surface to the customer as duplicate or conflicting messages. Pull them into one rule set that product, sales, and engineering code all consume, and put a single classifier in front of routing.

Use when:
- More than one system can initiate contact with the same customer, user, or account.
- Segment and signal definitions are being re-implemented inside an email tool, a CRM workflow, and application code.
- An agent needs to know whether an action is permitted for a given entity before it plans one.

Details:
- The before state is scatter: "eligibility used to be scattered all over the place. We had one check or rule in an email tool, another in sales." ([Liu](../sources/20260826_L4I7WgiEquo.md), 08:02-08:12)
- The move is consolidation plus shared consumption: "we pulled that all into one place so that these rules can be consumed across our codebase — product, sales, engineering," where the rules are "customer segmentations or signal definitions." The primitive is shared by human-run and agent-run paths alike. (08:12-08:26)
- **Routing is a separate decision from eligibility and gets exactly one owner.** "A single classifier will route what the customer should do," which "will actually prevent double sends from our system and create very cohesive communication." Deduplication is a consequence of centralizing the decision, not a filter applied afterwards. (08:26-08:37)
- Eligibility is elevated to an entity, not a config file: it appears in the warehouse's "small set of modeled, versioned entities" alongside accounts, contacts, workspaces, and facts, so it is versioned and attributed like any other modeled data. (09:22-09:36)
- The closing takeaway lists it as one of the five primitives worth modelling explicitly — "entities, context, triggers, actions, eligibility rules" — which is what makes an unfamiliar business domain "a system you can engineer." (20:02-20:12)
- The rule set is also what makes a single decisioning system possible across two motions: without shared eligibility, self-serve growth and sales-assist necessarily decide separately about the same customer. (03:02-03:34)
- **Limit.** No rule count, conflict rate, or before/after measurement of duplicate sends is given, and the classifier is described only by its job — no model, features, accuracy, or fallback behaviour when it is uncertain. (08:26-08:37)
- **The suppression case, which is the same primitive read at conversion time.** Berry's version of preventing a double send runs after contact rather than before it: "if you get a call connection and a meeting booked on your call sequence, you then need to suppress your email sequence and maybe [unenroll] someone from a life cycle marketing campaign." Notion's single classifier prevents two channels from firing at once; this is the harder residual case where they legitimately both fired and one has now won. It needs the same shared eligibility state, but with a write path from every channel back into it, and each of those channels is usually a different vendor with its own sync lag. ([Berry](../sources/20260826_UhCY231d0FQ.md), 15:26-15:48)

Related topics:
- [Workflows](../topics/workflows.md)
- [Go To Market](../topics/go-to-market.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Reduce Every Workflow to Know, Decide, Act, and Learn](reduce-every-workflow-to-know-decide-act-and-learn.md)
- [Emit Owner-Assigned Tasks From Signals, With a Marketing Default When None Fire](emit-owner-assigned-tasks-from-signals-with-a-marketing-default-when-none-fire.md)
- [Compute Truth in the Warehouse and Serve It as a Denormalized Profile](compute-truth-in-the-warehouse-and-serve-it-as-a-denormalized-profile.md)
- [Tune a Tool Router With K-Sweep and Guard Its Failure Modes](tune-a-tool-router-with-k-sweep-and-guard-its-failure-modes.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Protect Sender Reputation by Splitting Domains and Routing Replies Home](protect-sender-reputation-by-splitting-domains-and-routing-replies-home.md)
- [Wait for the Background Sync Before Acting on a Record You Just Created](wait-for-the-background-sync-before-acting-on-a-record-you-just-created.md)
- [Gate a Generated Multi-Channel Campaign on the Channel Owner](gate-a-generated-multi-channel-campaign-on-the-channel-owner.md)

Sources:
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 03:02-03:34, 07:59-08:37, 09:22-09:36, 20:02-20:12
- [GTM Engineering: The Technical Bits — Everett Berry, Clay](../sources/20260826_UhCY231d0FQ.md), 15:26-15:48
