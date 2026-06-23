# Plan Serverless GPU Inference Around the Cold-Start Tax

Summary: A scale-to-zero serverless GPU endpoint pays a one-time cold-start tax on the first request after it is created or has gone idle — the worker must create a container, download the model, and initialize before it can serve — so first-request latency is far higher than steady-state, and the fix is to keep always-on "active" workers warm at the cost of paying for idle capacity.

Use when:
- Setting first-request latency expectations or SLOs for a scale-to-zero GPU inference endpoint.
- Deciding whether to pay for always-on/active workers versus accepting cold starts on idle endpoints.
- Debugging why the first request after deploy or after an idle period is dramatically slower than later requests.

Details:
- Measured profile from a fresh RunPod serverless LLM endpoint: the first request sat in the queue ~41 seconds while the container was created, the model was downloaded from Hugging Face, and the first container initialized; every subsequent request executed in ~1.5 seconds. (11:48-12:09)
- Cold start is the direct cost of scale-to-zero: the same idle spin-down that lets you "pay for nothing when idle" forces a cold container plus model download on the next request to a cold endpoint, so the savings and the latency tax are two sides of one knob. (04:48-04:58, 11:54-12:03)
- Mitigation is warm capacity: configure always-on "active" workers that keep the container up and the model pre-downloaded so they "respond to requests immediately," eliminating the cold-start delay — paid for in idle worker cost and by giving up scale-to-zero. (06:02-06:20, 09:56-10:16)
- The latency is observable as a distinct component: the endpoint telemetry separates delay (queue) time from execution time alongside request counts, so cold-start cost can be measured separately from inference cost. (11:25-11:40)
- Practical consequence: "under five minutes to a deployed endpoint" still means the first user request is slow — deploy-from-catalog plus the first cold request takes a couple of minutes, then steady state settles to ~1.5s; capacity planning should budget cold starts for spiky, scale-to-zero traffic rather than assuming steady-state latency from request one. (12:08-12:19)

Related topics:
- [Inference](../topics/inference.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Choose Reserved Pods for Iteration, Serverless for Autoscaling Load](choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md)
- [Voice Agent Infrastructure Needs Realtime Session Deployment](voice-agent-infrastructure-needs-realtime-session-deployment.md)
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)

Sources:
- [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](../sources/20260607_ILdE7FaAjVA.md), 04:48-12:19
