# Scope a Person-Cloned Agent by Caller, With Drafts as the Shared Capability

Summary: An agent built to act as one high-access person cannot be shared at that person's privilege level, so bind the permission set to the caller rather than to the agent — full read/write and full tools when the owner invokes it, draft-only output and a reduced tool set for everyone else.

Use when:
- Exposing an agent that inherits one person's credentials to a wider audience.
- A useful internal agent is blocked because its access level and its audience cannot both be justified.
- Answering the review question "so there is one security level and everyone can see everything?"

Details:
- The risk is stated plainly by the person asking about it: a clone that "runs with all of your full privileges and then it's available to everybody… suggests that there's one security level and everyone can see everything all the time." ([Wang](../sources/20260826_6pbQgnJ9Voc.md), 15:58-16:19)
- The answer is caller-scoped rather than agent-scoped: "when I use Jeffbot and I call Jeffbot [it] has access to a ton of systems and it can for example do reads and writes. However, when anybody else calls Jeffbot all it can do is draft messages, and also I don't give Jeffbot permissions to all of our MCPs and tools in the case where other people call it." Two things narrow at once — the output capability and the tool set. (16:22-16:52)
- **Drafting is the load-bearing choice.** A draft is a proposal that a human must send, which keeps the agent's authority at zero for delegated callers while preserving most of its usefulness: the shared value here is "create drafts of Slack messages that are basically like answers or decisions that are made," and the GTM team uses it to draft emails. Read access is the part that does not get fixed by drafting — a draft can still contain what the caller was not entitled to see. (09:47-10:00, 16:22-16:52)
- The owner's grant is what makes the asymmetry necessary rather than merely tidy: "I gave it read and write access to all the data that I personally have… I basically have access to every single system at the company… so this thing has access to like everything." An agent cloned from a founder is by construction a maximal-privilege principal. (09:29-09:47)
- This is the caller dimension of agent scoping, complementary to the reachability dimension in [Scope Personal and Team Agents By Reachable Authority](scope-personal-and-team-agents-by-reachable-authority.md): that page says a personal agent should not sit in a shared channel, this one says it can, if identity determines the capability set at invocation time.
- **Limit.** This is a description of configuration and intent, not of enforcement. No mechanism is named for how caller identity is established or how the tool set is swapped, and no injection, exfiltration, or misuse scenario is discussed anywhere in the talk. "It's pretty well defined or we do pay some care to the security" is the strongest assurance offered. (16:52-16:58)
- **The other place authorization can live: below the agent, in the store.** Izmit's deployment binds permissions neither to the agent nor to the caller at the agent layer but to the data platform, where consolidating first-party, third-party, CRM, and call-transcript data means "these agents can basically inherit a lot of the role-based access controls." That answers a different question than caller-scoping — who may read what, rather than what a delegated agent may do on someone's behalf — and the two compose: inherited RBAC bounds reads, drafting bounds writes. Notably, Izmit's automation rung also converges on drafts-plus-review as the write pattern, with sellers having the agent "draft responses, save that in Gmail, review them afterwards, send those things out." ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 09:54-10:26, 19:26-19:55)
- **Drafting as the ceiling generalizes beyond cloned agents.** Notion applies the same bound to every agent in its GTM system regardless of caller: agents draft, humans approve, and no agent speaks to a customer — with the added justification that inbound form text is untrusted input and an agent sits in the middle. Read together, the two sources separate the mechanism (draft-only output) from its two different motivations: privilege containment when the agent is over-permissioned, and trust-boundary integrity when the input is attacker-controlled. ([Liu](../sources/20260826_L4I7WgiEquo.md), 07:23-07:58)

Related topics:
- [Security](../topics/security.md)
- [Agents](../topics/agents.md)
- [Go To Market](../topics/go-to-market.md)

Related concepts:
- [Scope Personal and Team Agents By Reachable Authority](scope-personal-and-team-agents-by-reachable-authority.md)
- [Aggregated personal context creates mosaic and exfiltration risk](aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md)
- [Grow Personal-Agent Permissions Incrementally From Recurring Pain](grow-personal-agent-permissions-incrementally-from-recurring-pain.md)
- [Derive an Agent Persona From a Measured Corpus, Not a Described Tone](derive-an-agent-persona-from-a-measured-corpus-not-a-described-tone.md)
- [Land the Data in One Governed Store So Agents Inherit Access Control](land-the-data-in-one-governed-store-so-agents-inherit-access-control.md)
- [Keep Agents Off the Customer Channel and Treat Inbound Forms as Untrusted Input](keep-agents-off-the-customer-channel-and-treat-inbound-forms-as-untrusted-input.md)

Sources:
- [Knowledge Systems: The New GTM Stack — Jeffrey Wang, Exa](../sources/20260826_6pbQgnJ9Voc.md), 09:29-10:00, 15:58-16:58
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 09:54-10:26, 19:26-19:55
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 07:23-07:58
