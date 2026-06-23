# Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod

Source: [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](https://www.youtube.com/watch?v=ILdE7FaAjVA)
Uploaded: 2026-06-07
Transcript: `raw/20260607_ILdE7FaAjVA/ILdE7FaAjVA.en-orig.vtt`

## Summary

Audry Hsu (RunPod) gives a console-driven intro to RunPod and deploys an open LLM as a serverless inference endpoint in under five minutes. The substance is the serverless GPU deployment flow and its latency/cost profile rather than new architecture: starting from a RunPod Hub listing (a vetted open-source GitHub repo with a preconfigured Dockerfile and defaults), she expands advanced options, sets the max model length (context window) and other knobs — which are passed straight through as flags to `vllm serve` — and clicks deploy. The endpoint defaults to H100s (A100s as backup), is billed a fraction of a cent per second only while a worker is actively handling a request, and is reachable as a plain HTTP API endpoint. The first request to the freshly created endpoint queues for ~41 seconds (cold start: container creation + model download from Hugging Face + first-container init), while every subsequent request executes in ~1.5 seconds; the console telemetry separates delay (queue) time from execution time. Cold start can be eliminated by configuring always-on "active" workers that keep the model pre-downloaded and respond immediately, traded against paying for those workers when idle and giving up scale-to-zero. This is the same speaker as the already-processed RunPod Flash talk (`zDGHt0LB-dA`); the four product modes (pods, serverless, clusters, hub) and per-second billing overlap, so the durable new contribution is the serverless cold-start tax and the hub-to-`vllm serve` deploy mechanic.

## Extracted Concepts

- [Plan Serverless GPU Inference Around the Cold-Start Tax](../concepts/plan-serverless-gpu-inference-around-the-cold-start-tax.md) - measured ~41s first-request cold start vs ~1.5s steady-state, eliminated by always-on active workers at the cost of idle spend.
- [Choose Reserved Pods for Iteration, Serverless for Autoscaling Load](../concepts/choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md) - corroborates per-second request-scoped billing and scale-to-zero, and adds the hub-listing → `vllm serve`-flags deploy mechanic.

## Topic Links

- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

## Notes

- RunPod is an AI cloud infrastructure company: it owns the hardware/GPUs and makes it easy for developers to deploy their own private model or an open-source Hugging Face model — "you bring your code and we'll bring the rest." (00:33-00:53)
- Company glance: 500,000+ developers, 30+ data centers worldwide (including Europe/EU), $120M ARR; bootstrapped in 2022 by founders Zenon and Pardeep from spare basement GPUs after a failed crypto-mining venture, via a Reddit "free GPUs for feedback" post. (02:21-03:46)
- Four ways to build on RunPod: pods (sandbox/virtual-environment container with allocated GPUs, bring your Dockerfile/code), serverless (auto-scaling — workers spin down and you pay nothing when idle, best for bursty/batch workloads and real-time inference), clusters (multi-node high-speed networking for heavy training), and the hub (central repository of pre-configured, pre-vetted AI repos you can fork/watch/star/deploy, both RunPod- and community-listed). (04:19-05:35)
- Serverless config knobs: max workers (scale-up cap), spending caps, and always-on/active workers that "already have your models downloaded" so they respond to requests immediately. (06:02-06:20)
- RunPod also exposes CLI support and "skills ready for your agent" so an agent can work with RunPod without reading the docs; this demo was done via the console for legibility. (06:56-07:16)
- Deploy flow: a hub listing is "literally just a GitHub repo" with an already-preconfigured Dockerfile and defaults; you can pass environment variables, expand advanced options, and set max model length (context window) and max LoRAs — "all of these configuration options get passed as flags to the `vllm serve`." (07:51-09:16)
- Endpoint defaults: deploys on H100s with A100s as backup; pricing is a fraction of a cent per second, charged only while a worker is actually running and handling a request. Max workers shown bumped to 15; active workers can be set so the container never spins down. (09:35-10:16)
- The serverless endpoint is just a provisioned HTTP API endpoint you (or your customers) send requests to; the console can fire test requests and shows them as queued until workers pick them up. (10:22-11:25)
- Telemetry/observability: number of requests, execution time, and delay time are surfaced per endpoint. (11:25-11:40)
- Cold start vs steady state: the first request sat in the queue ~41 seconds because of cold-start work (container init, model download), while execution time was only ~1.5 seconds; total deploy-to-first-response was under five minutes from a hub listing. (11:48-12:19)
- A separate later session was teased covering RunPod's Python SDK done entirely via the terminal — deploying local code as a remote function onto a GPU to make a production-ready endpoint (this is the Flash SDK covered in `zDGHt0LB-dA`). (12:27-12:56)
