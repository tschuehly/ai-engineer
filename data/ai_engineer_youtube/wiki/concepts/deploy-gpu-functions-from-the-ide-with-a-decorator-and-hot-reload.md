# Deploy GPU Functions From the IDE With a Decorator and Hot Reload

Summary: A serverless-GPU SDK can collapse the commit → push → Docker-build → registry-pull → server-load → GPU-allocate iteration loop into a single decorator on an async Python function, so only the GPU-needing code runs remotely while orchestration stays local and any file edit hot-reloads onto the cloud.

Use when:
- Iterating on GPU inference code and tired of rebuilding containers to test each change.
- Choosing a serverless GPU SDK or deciding how to shorten the GPU development feedback loop.
- Wiring multi-model orchestration where local glue code fans out to several remote GPU model calls.

Details:
- The pain being removed: normally you make a commit, push to GitHub, build a Docker image, pull it from the container registry, load it onto a server, allocate a GPU, then finally test — and repeat the whole cycle on every change. (05:43-06:24)
- RunPod Flash is a Python SDK whose entire model fits in one paragraph: take a regular async Python function, add the `@flash.endpoint` decorator, and it packages and deploys everything inside that function onto a GPU cloud. (06:25-07:07)
- The boundary is per-function, not per-process: the `main` function and any helper functions keep running in the local development environment, and only the decorated GPU-needing function executes on the cloud. (07:07-07:19)
- Hot file reload closes the loop: changing anything anywhere in the application repackages and pushes it up immediately, so a model swap (Stable Diffusion XL Turbo → DreamShaper, with new inference-step/size params) is a one-line edit rather than a container rebuild. (07:19-07:32, 13:00-14:26)
- `flash run <file>.py` spins up a local FastAPI development server; you POST requests to that local endpoint to test, while the decorated function still runs on the remote GPU. (08:21-09:12)
- The decorator config carries the deployment shape: a name, a GPU family (e.g. "Ada 80 pro" H100 variants), `max_workers` (concurrency ceiling), an always-on `active` worker count, and an idle timeout for how long a worker stays warm. (11:32-12:40)
- The value compounds for orchestration, not single calls: the demo's local pipeline chains three remote/hosted models — Qwen 3 generates image prompts, DreamShaper renders them, and Nano Banana 2 (Google) composes the results into one photo — with all the orchestration code running locally and never leaving the IDE. (14:26-15:45, 16:55-17:00)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Choose Reserved Pods for Iteration, Serverless for Autoscaling Load](choose-reserved-pods-for-iteration-and-serverless-for-autoscaling-load.md)
- [Compile Python inference functions into portable native binaries](compile-python-inference-functions-into-portable-native-binaries.md)
- [Local-First Platform Workflows Shorten Agent Feedback Loops](local-first-platform-workflows-shorten-agent-feedback-loops.md)

Sources:
- [GPU Cloud Deployment Without Leaving Your IDE — Audry Hsu, RunPod](../sources/20260609_zDGHt0LB-dA.md), 05:43-17:00
