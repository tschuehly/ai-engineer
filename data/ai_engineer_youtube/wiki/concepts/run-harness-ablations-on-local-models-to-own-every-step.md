# Run Harness Ablations on Local Models to Own Every Step

Summary: Running an agent-harness experiment on local models buys the one thing a hosted API cannot give you — control of the data, the full compute and evaluation traces, and every step of the pipeline — which is exactly what an ablation needs. The bill is paid in wall-clock: local models here could only be run serially, with no batch querying, so the evals took days and had to keep running through the conference travel.

Use when:
- Planning a controlled experiment on a harness, memory policy, or context strategy rather than a production deployment.
- Deciding whether an experiment needs local inference or can run against a hosted API.
- Budgeting the time cost of a local eval sweep, or explaining why one is still running.

Details:
- What local control buys, stated as the reason the study was possible: "I got to control everything. I got to control the data I was using, the entire traces of compute and evaluations… I see that as an example of sovereignty," and "it's a very good test for what memory can do when you can control every single step of the pipeline." ([Memory Harnesses for Long-Running Research Agents](../sources/20260812_R3-anFK1YM8.md), 11:30-12:20)
- The tax, named precisely rather than as a general slowness complaint: "these local models I can only run them in serial, like they don't support batch querying for the deep seek 4 flash. So, that's why I am still running evaluations back on my computer in Tokyo, or I was doing it on the flight on my way here because it takes a long time." No batch API means no parallel sweep, and a ladder of recall policies × 68 questions × multiple seeds is exactly the workload that suffers. (11:49-12:11)
- The second, less-discussed tax is thermal. After "running evals non-stop for a couple of days, it started to get hot. So I had my husband put fans around it. Um we're running out of fans, but the machine is still running." A desk-side machine running a multi-day sweep is a sustained-load problem, not a peak-performance one. (02:49-03:13)
- The rig that made it viable: an M3 Ultra with 96 GB unified memory and 28 CPU cores, running two quantized local models, driven remotely from a phone. (02:49-03:29)
- Why local was viable at all *now*: "local models like crossing the line" — GLM "is on everyone's minds," DeepSeek V4 Flash "can now be run on M3 Ultra," RAM is "still a bottleneck… it's tricky," but they "are starting to be useful for agentic tasks and for tool use." The capability threshold for an agentic experiment, not a chat demo, is the relevant one. (02:17-02:43)
- Second-hand cost motivation cited in the talk, and worth keeping labelled as second-hand: a two-day-old tweet from the CEO of Coinbase reporting that the company "managed to reduce their AI spend while actually increasing the AI usage" by moving to many more local models plus "better routing, better caching, keeping the context clean," and better visibility into who used AI for which task. No figures accompany it. (01:44-02:17)
- Practical reading of the tradeoff: choose local when the experiment's value comes from holding things fixed and reading every trace, and accept that the sweep is serial. Choose hosted when throughput is the binding constraint and you can tolerate an opaque middle. The choice is about *what the experiment is for*, not about which is cheaper.
- Provenance: the speaker is a research scientist at Sakana AI, and the closing sovereignty framing is her employer's stated positioning followed by a hiring call. The serial-execution constraint and the thermal observation are independent of that framing.

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Ablate the Recall Policy With a Ladder and an Oracle](ablate-the-recall-policy-with-a-ladder-and-an-oracle.md)
- [Invest in the Harness to Run Weaker and Local Models](invest-in-the-harness-to-run-weaker-and-local-models.md)
- [Use Local AI Workstations When Iteration, Privacy, or Latency Dominate](use-local-ai-workstations-when-iteration-privacy-or-latency-dominate.md)
- [Own Open Models for Sovereignty and Permissionless Adoption](own-open-models-for-sovereignty-and-permissionless-adoption.md)
- [Make Local Inference Benchmarks Reproducible Artifacts](make-local-inference-benchmarks-reproducible-artifacts.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Drive agents remotely and by voice to decouple work from the desk](drive-agents-remotely-and-by-voice-to-decouple-work-from-the-desk.md)

Sources:
- [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](../sources/20260812_R3-anFK1YM8.md), 01:44-03:29, 11:30-12:20
