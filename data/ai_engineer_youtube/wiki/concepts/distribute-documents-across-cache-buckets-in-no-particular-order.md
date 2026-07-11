# Distribute Documents Across Cache Buckets in No Particular Order

Summary: When sharding a deeply-interconnected corpus across parallel cached-context buckets, partitioning by domain backfires: a supervisor model skips buckets whose domain looks irrelevant at first glance and misses the cross-domain connections. Distribute documents in no particular order and balance only the count so the fewest documents are needed.

Use when:
- Sharding documents across parallel cache/context buckets (ECAG) or across parallel sub-agents that a router or supervisor will query.
- Documents have dense cross-domain relationships, so relevant evidence hides in buckets that look off-topic.

Details:
- It is tempting to organize documents by domain and hand the supervisor the list of categories so it can route by topic. 04:11-04:20
- In practice, with very dense relationships between documents, the supervisor tends to ignore domains that at first glance seem irrelevant — so a domain label becomes a reason to skip a bucket that actually holds needed connections. 04:20-04:30
- The fix is to distribute all documents in no particular order; the only requirement is to balance the number of documents so that the least amount of documents are needed to answer. 04:30-04:40
- With unordered balanced buckets, the supervisor explores every bucket, progressively builds its internal understanding, and asks specific buckets follow-up questions when it finds something interesting, rather than pre-pruning by topic. 04:40-05:00

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Shard Cache-Augmented Generation Into Parallel Buckets With a Supervisor](shard-cache-augmented-generation-into-parallel-buckets-with-a-supervisor.md)

Sources:
- [When All Context Matters: Extended Cache Augmented Generation - Luis Romero-Sevilla, Orbis](../sources/20260628_XovaGv4f39A.md), 04:11-05:00
