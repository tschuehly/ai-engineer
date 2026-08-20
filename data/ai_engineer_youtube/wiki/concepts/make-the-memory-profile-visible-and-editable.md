# Make the Memory Profile Visible and Editable

Summary: The artifact that shapes every conversation should be readable in its exact served form and correctable by the person it describes. Shipped products span the full range — from a profile hidden well enough that a user had to jailbreak the model to read his own, to a raw profile in settings whose user edits trigger a resynthesis — and the hidden end produces uncorrectable errors that persist for months.

Use when:
- Deciding what a personalization or memory settings screen should expose.
- Weighing whether to show users a summary of their profile or the profile itself.
- Designing the correction path for a memory system that will inevitably record something false.

Details:
- ChatGPT v1's fact list was visible in settings and individually deletable — the transparency was a side effect of its user-managed design (02:51-03:00).
- ChatGPT v2 regressed on this axis: settings still showed the old v1 memories, but "chat GPT doesn't let you view this raw profile" (06:29-06:41). The speaker read his own only by jailbreaking the model, noting it "works really well… you might have to attempt a few times, try different thinking modes, but prod enough and you shall receive" (06:41-06:56).
- Claude's v2 shipped the opposite defaults: the raw profile visible in settings; explicit user edit requests, where "that edit would lead to a resynthesis of the profile"; and an interface to manage previous edits and delete things that no longer hold true (08:20-09:16).
- ChatGPT's June 2026 update made the profile visible "somewhat": what the settings screen shows is "an LLM generated summary of your profile, which is weird because your profile is already an LLM generated summary of your conversations" (09:33-09:58). A summary of the served artifact is not the served artifact — the user cannot tell which of the two layers introduced an error.
- Why this matters beyond user control: a hidden profile is also an undebuggable one. The Turkey/Thailand error survived because nothing in the product surface exposes the claim in the form the model actually reads (05:56-06:29).
- Editability changes the correction semantics. Deleting an item from a fact list removes one row; editing a synthesized profile has to re-run the synthesis, which is why Claude's design treats an edit as an input to regeneration rather than a direct write (08:46-09:16).

Related topics:
- [Product Strategy](../topics/product-strategy.md)
- [Context Engineering](../topics/context-engineering.md)
- [Security](../topics/security.md)

Related concepts:
- [Replace User-Managed Memory Lists With a Background-Synthesized Profile](replace-user-managed-memory-lists-with-a-background-profile.md)
- [Explicit Context Attachments Can Outperform Opaque Agent Memory](explicit-context-attachments-can-outperform-opaque-agent-memory.md)
- [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)
- [Aggregated Personal Context Creates Mosaic and Exfiltration Risk](aggregated-personal-context-creates-mosaic-and-exfiltration-risk.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 02:51-03:00, 05:56-06:56, 08:20-09:16, 09:33-09:58
