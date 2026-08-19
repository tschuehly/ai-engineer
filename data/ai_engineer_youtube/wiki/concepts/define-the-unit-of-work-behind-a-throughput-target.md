# Define the Unit of Work Behind a Throughput Target

Summary: A requests-per-second number is meaningless until you say what one request does. Oxylabs' jump from 10,000 to 60,000 requests per second sounds like HTTP throughput but each request is an end-to-end scraping job — routing, rendering, proxy handling, browser execution, parsing, retries, normalization, delivery — which is why adding servers does not close the gap and why an order-of-magnitude jump changes the operating model rather than the capacity plan.

Use when:
- Sizing or quoting throughput for an AI data, retrieval, or inference pipeline where one "request" fans out into a multi-stage job.
- Someone proposes to meet a scale target by adding machines.
- Planning a 10x traffic step and deciding what has to be rebuilt rather than replicated.

Details:
- The unit-of-work caveat, stated directly: 60,000 requests per second "might be also misleading if you are thinking about it as a simple HTTP request. In our world, that means the end-to-end scraping job" — routing, rendering, proxy handling, browser execution, parsing, retries, normalization, and delivery. (12:56-13:32)
- Horizontal capacity is not the lever: "even adding up additional 2,000 servers doesn't solve the problem. You need an architecture. You need central components that actually are reliable. You need observability that still tells you the truth. And you need testing that resembles reality enough to matter." (13:32-13:47)
- Order-of-magnitude growth is an operating-model change, not a growth number: going from 400 million to almost 6 billion daily requests "is not just a change, not just a growth. It's a change in operating model. It changes how you think about costs, observability, and failure domains." (11:24-12:00)
- The moving-target caveat: while scaling to 60,000 rps under the internal name "Project 60," the demand had already moved and it became "Project 150." "Scale is never a finish line… when you reach one target number, the next one will appear," so architecture should be chosen against the next target, not the current one. (15:31-16:10)
- The scaling window was aggressive — roughly 10,000 to 60,000 requests per second in under two months — which is why the constraint surfaced as architecture and measurement rather than procurement. (12:33-12:56)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Realistic Traffic, Not Volume, Is the Hard Part of Load Testing](realistic-traffic-not-volume-is-the-hard-part-of-load-testing.md)
- [Separate Agentic Workflow Design From Scale Infrastructure](separate-agentic-workflow-design-from-scale-infrastructure.md)
- [Benchmark Inference With Use-Case-Shaped Token Loads](benchmark-inference-with-use-case-shaped-token-loads.md)
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)

Sources:
- [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../sources/20260814_1UmZHb_E_SM.md), 11:24-13:47, 15:31-16:10
