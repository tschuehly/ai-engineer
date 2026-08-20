# Replace User-Managed Memory Lists With a Background-Synthesized Profile

Summary: A list of extracted facts the user can watch being written makes the user responsible for curating memory mid-conversation; a running profile rewritten by a background pass over recent conversations removes that burden. It does not remove staleness — a profile synthesized from deliberation can record a decision the user never made.

Use when:
- Choosing between an append-only memory list and a periodically re-synthesized user profile.
- Diagnosing why a personalization layer keeps asserting things about a user that stopped being true, or were never true.
- Sizing how much of a memory design is "what we store" versus "how often we rewrite it."

Details:
- ChatGPT's February 2024 v1 stored explicit facts: "remember that I'm vegetarian" became an extracted fact in a list that was added to the context window of every conversation and was visible and deletable in settings (02:20-03:00).
- Its first flaw was interactional rather than technical. Because the user saw each memory being created, "it felt like you were responsible for both creating memories while you were just trying to have a conversation. So the burden of memory management fell to the user" (03:00-03:26).
- Its second flaw was that facts true at write time do not stay true: a memory saying he was going to Bengaluru kept entering his context window long after the trip was irrelevant (03:26-03:53).
- April 2025's v2 replaced the list with a **running profile**: every few days a background pass reads new conversations, extracts what it thinks is important, and rewrites a maintained profile that is then prepended to every new conversation (03:56-04:58). Others call this update pass "dreaming" (04:30-04:47).
- The stored form is a design choice with a stated bet behind it. His profile packs "keywords almost like clues" rather than prose, on the reasoning that frontier models "are so good at inferring context from limited information" that the clues get connected at conversation time; it runs 16 sections and almost 4,000 tokens (04:58-05:47). Claude's equivalent takes the opposite option — complete sentences, ~1,000 tokens (08:20-08:46).
- Background synthesis fixes the burden but not the staleness, and adds a failure mode of its own: **deliberation gets recorded as fact**. A profile entry about his 2025 travel listed Thailand and Turkey with overlapping dates because its source was conversations comparing the two. He went to Thailand and has never been to Turkey, and the profile still says otherwise (05:56-06:29).
- Direction of travel: with the June 2026 update ChatGPT deprecated the v1 fact list entirely, leaving the profile as the only always-on memory artifact (09:33-10:09).

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Pair a Running Profile With On-Demand Conversation Search](pair-a-running-profile-with-on-demand-conversation-search.md)
- [Budget Memory Between Update Cost and Serving Cost](budget-memory-between-update-cost-and-serving-cost.md)
- [Make the Memory Profile Visible and Editable](make-the-memory-profile-visible-and-editable.md)
- [Make Memory Notice Conflicts and Seek the Evidence That Settles Them](make-memory-notice-conflicts-and-seek-the-evidence-that-settles-them.md)
- [Ambient Agents Need Self-Maintenance and Memory Hygiene](ambient-agents-need-self-maintenance-and-memory-hygiene.md)

Sources:
- [Lessons from Studying Every Memory System — Shlok Khemani, Independent](../sources/20260812_5ZGyKWjQDr0.md), 02:20-06:29, 09:33-10:09
