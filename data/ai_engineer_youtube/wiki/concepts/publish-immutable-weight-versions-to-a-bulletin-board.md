# Publish Immutable Weight Versions to a Bulletin Board

Summary: Replace the trainer's push of weights to a known set of rollout workers with a pull: after each optimizer step the trainer publishes an immutable, numbered rollout-weights version to a shared board, and any engine anywhere fetches and materializes it. Requests then carry which version they target and which versions are acceptable, and responses carry the version they were served by — which is what lets rollout engines run outside the trainer's cluster without the trainer knowing they exist.

Use when:
- Designing weight distribution for an RL fleet that autoscales or spans providers.
- Deciding how a trainer should address rollout workers it did not launch.
- Building an off-policy data contract that survives workers at different versions.
- Choosing a serialization format for weights that unmodified serving engines must load.

Details:
- The shape: "the trainer [sits in] a cluster; after it got updated it publish[es] immutable rollout [weight] version to a shared bulletin board. Rollout engine[s] live outside of the training cluster, which means they don't need to be RDMA connected with the trainer. They can be in different region[s] or different providers." ([Modal](../sources/20260810_maRzp4kImJ4.md), 15:16-15:34)
- **Pull is what makes the fleet elastic.** A push requires the trainer to hold a roster of workers and reach each one; a pull lets an engine that started ten seconds ago join by fetching, and lets one that died be forgotten without a membership change. The trainer's job ends at publication.
- **Immutability is what makes version identity meaningful.** "The trainer writes immutable version[s] to the [board] after [the] optimizer step; [the] engine pull[s the] version and materialize[s] it locally in the checkpoint layout, so they can just serve directly the artifact-defined version. The engine choose[s] how to load and shard it. It does not choose a different serve[d] version." The engine gets latitude over *placement* — tensor parallelism, sharding, attention backend — and none over *content*. That separation is what lets heterogeneous engines produce data attributable to one policy. (16:00-16:23)
- **The request contract carries versions in both directions.** "A request does not just say give me the completion. You will also say which version you will be sending [the] request to and which version you will be accepting, and the response will come back with the version and also like exact same information as if they are in the same cluster as the trainer. They will be returning tokens, log prob[s], like router replay information and many more metadata." An acceptable-version *range* rather than a single pin is what lets a fleet at mixed versions keep serving; the version on the response is what lets the trainer compute staleness per trajectory instead of assuming it. (15:34-16:00)
- Returning log probs and router-replay information alongside tokens is the part that makes remote rollouts usable as training data rather than as text: importance ratios and MoE routing reconstruction both need it, and neither can be recovered after the fact from a completion string.
- **Format choice is a compatibility decision, not a storage one.** "Since it will be [saved] in a Hugging Face safetensors format, which is accepted widely by many rollout engines such as SGLang and vLLM, we can support any compatible backend, attention backend, different parallelism, compatible serving dtype and any compatible GPUs there." Publishing in the format engines already load is what avoids requiring a fork of every engine. (16:23-16:40)
- The board is also the substrate for catch-up: because prior versions remain addressable, an engine that has fallen behind can be walked forward through the missing transitions rather than reloading from scratch — see [Make a Rollout Engine Version-Aware With a Sidecar](make-a-rollout-engine-version-aware-with-a-sidecar.md).
- Modal's implementation is named **Stitch**: "on the trainer side Stitch publishes what defines a rollout weights version… [the] rollout side you will be pulling the latest weights… Stitch itself is very framework agnostic about trainer and engine and also transport. It's very async first and also agentic first." The protocol is presented as general and the implementation as one instance of it; no second implementation is cited. (17:41-18:17)
- **Unaddressed.** Retention policy and storage cost for the version history are never discussed, and neither is trust: publishing weights to a board that engines at arbitrary providers pull from is exactly the point of the design, and the talk offers no threat model, encryption, attestation, or access-control story for it. ([Modal](../sources/20260810_maRzp4kImJ4.md), 15:16-18:17)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Make a Rollout Engine Version-Aware With a Sidecar](make-a-rollout-engine-version-aware-with-a-sidecar.md)
- [Synchronize Rollout Weights With a Bitwise-Lossless Patch, Not a Checkpoint](synchronize-rollout-weights-with-a-bitwise-lossless-patch.md)
- [The Rollout Serving Island Is the Movable Unit of an RL Run](the-rollout-serving-island-is-the-movable-unit-of-an-rl-run.md)
- [Pipeline RL Trades Policy Staleness for GPU Throughput](pipeline-rl-trades-policy-staleness-for-gpu-throughput.md)
- [SGLang Serves Models Through Configured OpenAI-Compatible Servers](sglang-serves-models-through-configured-openai-compatible-servers.md)

Sources:
- [Taking Reinforcement Learning Cross Datacenter — Nan Jiang, Modal](../sources/20260810_maRzp4kImJ4.md), 15:16-16:40, 17:41-18:17
