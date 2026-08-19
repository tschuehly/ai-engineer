# Realistic Traffic, Not Volume, Is the Hard Part of Load Testing

Summary: Generating synthetic load is easy; generating load that behaves like real client usage is the hard part, and without it a passing load test tells you the system works at the tested number but not whether it can go further. Oxylabs hit a wall at ~20,000 requests per second on the way to 60,000 — the wall was uncertainty, not a failure — and at that volume the telemetry itself became part of the load being measured.

Use when:
- Load-testing an AI serving, retrieval, or data pipeline before a large traffic step.
- A load test passes and you have to decide whether it justifies the next 3x.
- Budgeting observability for a high-volume system, where logs and metrics compete with the workload for capacity.

Details:
- Where the bottleneck actually appeared: "this is where our main bottleneck showed up, not in dramatic outage, in load testing." (13:43-13:55)
- The difficulty is fidelity, not volume: "the hardest part was not generating synthetic traffic. Synthetic traffic is relatively easy comparing to reality… the hardest part, organic data testing" — traffic that behaves enough like real client usage to tell you something useful. (13:55-14:20)
- The wall at ~20,000 requests per second was epistemic: "at that point, there is no question if the system is actually working. It is working. The question becomes, do we actually know that it can go further? And that uncertainty was the real bottleneck." (14:20-14:44)
- Observability becomes self-interfering at scale: "everybody loves observability in theory, but observability at scale becomes a true work because collecting logs is hard, processing logs is harder" — and "when you scale up to that kind of a load, the telemetry itself becomes a part of the load and a part of the complexity." A measurement plan for a 6x traffic step has to budget for the measurement. (14:44-15:20)
- The accepted resolution was gradual scaling plus an explicit admission that the final test is production: "we scaled gradually. And eventually, we had to accept one unavoidable truth that the real testing is going to be with production traffic." In their case that went fine — but the durable point is planning the ramp so production is the last unknown rather than the first. (15:13-15:31)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Define the Unit of Work Behind a Throughput Target](define-the-unit-of-work-behind-a-throughput-target.md)
- [Benchmark Inference With Use-Case-Shaped Token Loads](benchmark-inference-with-use-case-shaped-token-loads.md)
- [Works in Dev, Passes Tests, and Survives Reality Are Three Different Systems](works-in-dev-passes-tests-and-survives-reality-are-three-systems.md)
- [Continuously Reconcile Eval Datasets With User Reality](continuously-reconcile-eval-datasets-with-user-reality.md)

Sources:
- [How Web Data Infrastructure Powers the Next Generation of AI — Patricija Žemaitytė, Oxylabs](../sources/20260814_1UmZHb_E_SM.md), 13:43-15:31
