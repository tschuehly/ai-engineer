# Close a Multiples-Wide Latency Gap by Redesign, Not Optimization

Summary: When the target latency is a fraction of the current baseline, tuning the existing path will not get there — the general-purpose system is doing work the new use case does not need. Oxylabs went from a ~4-second general search scraper to a 550 ms average AI-facing search API by cutting the payload down to what AI systems actually read and then hunting seconds across every layer, not by finding one trick.

Use when:
- An agent or RAG loop needs live search inline and the existing retrieval path is seconds slow.
- Deciding whether to optimize a general-purpose collector or build a second, narrower one for the AI path.
- Setting expectations about where a large latency win comes from (many small cuts, not a breakthrough).

Details:
- The gap framing: the traditional search scraper averaged about 4 seconds, and the client asked for sub-second delivery (under 800 ms) with zero data retention in under two weeks. "When your baseline is at 4 seconds, we are not talking about optimization. We are talking about redesign." (07:25-09:24)
- The scope cut is the structural reason a redesign is possible: the general scraper is "built to retrieve as much information as possible" — ads, widgets, rich results, AI-generated results, different layouts — while the fast search API "focuses on the things that actually matters only for AI systems," mostly organic results, top stories, and news, cutting away the heavy layout. (08:00-08:34)
- No single lever produced the win: "there is no magic trick. You just go hunting for a time" — reviewing layouts, parsers, sessions, and proxies for anywhere a second could come off. "This is how systems becomes fast, not by giant breakthroughs as we thought at first, but by small decision that adds up." (10:49-11:12)
- The slow dependency was not removable, only manageable: browsers were required for the second iteration and are "slow, expensive, complex, and deeply incompatible with dreams about low latency," so the hunt had to find its seconds around them. (10:10-10:49)
- Result and framing: 550 ms average today, and "in AI era, speed is not just performance. Speed actually defines what product can exist" — at 4 seconds you have a slow pipeline, at sub-second you have something that "can sit and interact in your AI workflows." Latency is therefore a product boundary for inline agent retrieval, not a quality-of-service metric. (11:12-12:26)
- Timing caveat on demand: a sub-second SERP product built in 2024 for an earlier client was never tested by them and got shelved because "the market wasn't ready"; the same capability shipped in 2025. Being early on latency is not automatically valuable. (07:25-08:00)

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Works in Dev, Passes Tests, and Survives Reality Are Three Different Systems](works-in-dev-passes-tests-and-survives-reality-are-three-systems.md)
- [Separate Engine Latency From Network Latency in Voice Pipelines](separate-engine-latency-from-network-latency-in-voice-pipelines.md)
- [Balance GraphRAG Hop Depth Against Production Latency](balance-graphrag-hop-depth-against-production-latency.md)
- [Latency Shapes Coding Agent Interaction Mode](latency-shapes-coding-agent-interaction-mode.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)

Sources:
- [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../sources/20260814_1UmZHb_E_SM.md), 07:25-12:26
