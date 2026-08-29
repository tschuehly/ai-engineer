# Self-Hosted Inference Needs a Platform Beyond Runtime and GPUs

Summary: Self-hosted open-model inference is not production-ready just because a team has model weights, vLLM or SGLang, and GPUs. Mission-critical serving needs a platform layer for performance, reliability, scaling, observability, lifecycle management, controls, and audits.

Use when:
- Turning an open-model prototype into enterprise production inference.
- Deciding whether to build or buy the inference platform layer around open-source serving runtimes.

Details:
- The talk explicitly rejects the formula "open model plus runtime plus GPUs equals production inference," saying mission-critical inference inside a company needs much more. (11:17-11:57)
- Performance tuning spans both model and infrastructure layers: speculative decoding strategy, draft models, Medusa heads, Eagle 3, MTP, prefix caching, and disaggregated serving are treated as production choices rather than simple runtime switches. (12:04-13:37)
- Agentic workloads with large, similar prompts make prefix caching and disaggregated serving important for time-to-first-token and P99 reliability. (13:10-13:37)
- Reliability work must handle hardware failures, vLLM crashes, Triton crashes, and recovery paths without letting tail latency spike for users. (13:38-14:24)
- Scaling work includes reducing replica startup time during traffic bursts; the talk cites an enterprise where a new model replica took about eight minutes to come up, which made burst handling unacceptable. (14:30-14:59)
- The platform layer also includes lifecycle management, observability beyond basic logs and metrics, controls, and audits that enterprises care about. (15:00-15:29)
- **What the P99 line on this checklist actually has to mean.** Manuja is blunt that a service-wide latency number over mixed workloads "doesn't make sense. It's a lie," because one platform carries embeddings and classification under a second, chat around three seconds, and reasoning far longer: "you should be tracking your P99 per model per route, not a gateway wide number," and "a reasoning model's normal is actually a chat model's outage." He gives the same granularity to timeouts and calls their absence "the number one root cause of your silent outage. If you don't have a timeout, your gateway thinks your request is being happily served while it is not." Add load shedding to the reliability column too, since "you cannot simply scale out services that is under a retry storm." ([Manuja](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16, 13:49-14:20)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Production Inference Combines Model Support With Cluster Operations](production-inference-combines-model-support-with-cluster-operations.md)
- [SGLang Serves Models Through Configured OpenAI-Compatible Servers](sglang-serves-models-through-configured-openai-compatible-servers.md)
- [Disaggregate prefill and decode workers by workload shape](disaggregate-prefill-and-decode-workers-by-workload-shape.md)
- [Route inference requests by KV locality and worker load](route-inference-requests-by-kv-locality-and-worker-load.md)
- [Track Latency and Timeouts Per Model Class Per Route](track-latency-and-timeouts-per-model-class-per-route.md)

Sources:
- [The Rise of Open Models in the Enterprise — Amir Haghighat, Baseten](../sources/20250724_3WV1vT0B0cg.md), 11:17-15:29
- [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](../sources/20260828_zrZ1amZBSPw.md), 06:54-08:16, 13:49-14:20
