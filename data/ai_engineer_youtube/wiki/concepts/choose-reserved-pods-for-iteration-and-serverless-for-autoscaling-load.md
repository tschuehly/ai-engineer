# Choose Reserved Pods for Iteration, Serverless for Autoscaling Load

Summary: On a GPU cloud, run experimentation on reserved/persistent pods (or a very low worker count) because you only need one or two GPUs at a time, and switch to autoscaling serverless workers only when production load is variable and needs hundreds of GPUs distributed across data centers — serverless carries a scaling premium but bills only while a request is running and scales back to zero when idle.

Use when:
- Deciding between a reserved GPU pod and serverless workers for a given workload phase.
- Estimating GPU cost across a development-to-production transition or sizing worker counts.
- Explaining why a per-second GPU price does not translate directly into a monthly bill.

Details:
- RunPod's product modes map to workload shapes: pods are a persistent VM with a reserved GPU that stays yours as long as the pod runs, rentable on demand, paid by the second, and torn down when finished; serverless autoscales workers up under load and back down to zero when no requests arrive so you pay no idle time; clusters target multi-node training; and the hub is pre-vetted open-source repos (ComfyUI, Stable Diffusion, vLLM) you can click to deploy. (03:55-05:15)
- The explicit recommendation: while still experimenting, start with pods or a very low worker count because you typically only need one or two GPUs at a time; move to serverless when you need hundreds of workers running on hundreds of GPUs and want them distributed across data centers for better availability. (16:10-16:36, 17:36-18:36)
- Serverless costs a little more than pods because pods give no scaling — there is a premium for the autoscaling behavior. (17:55-18:10)
- Per-second, request-scoped billing is the core economics: an H100 serverless worker is $0.00116/second and you are charged only for how long each request is running. (16:55-17:52)
- Billing tracks live work, not provisioned capacity: requesting three photos lit up three running workers (out of ~five/six provisioned), and the "uptime" of those running workers is exactly what is billed. (16:36-17:30)
- Deploying from the hub is a fast path to a serverless inference endpoint: a hub listing is "literally just a GitHub repo" with a preconfigured Dockerfile and defaults, you pass environment variables and advanced options (max model length / context window, max LoRAs) that "get passed as flags to the `vllm serve`," and clicking deploy on default H100s (A100 backup) gives a provisioned HTTP API endpoint in under five minutes. (ILdE7FaAjVA, 07:51-09:16, 12:08-12:19)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Match GPU Commitments To Workload Lifecycle](match-gpu-commitments-to-workload-lifecycle.md)
- [Autoscale specialized inference workers as traffic mix changes](autoscale-specialized-inference-workers-as-traffic-mix-changes.md)
- [Deploy GPU Functions From the IDE With a Decorator and Hot Reload](deploy-gpu-functions-from-the-ide-with-a-decorator-and-hot-reload.md)
- [Plan Serverless GPU Inference Around the Cold-Start Tax](plan-serverless-gpu-inference-around-the-cold-start-tax.md)

Sources:
- [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](../sources/20260609_zDGHt0LB-dA.md), 03:55-18:36
- [Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod](../sources/20260607_ILdE7FaAjVA.md), 07:51-12:19
