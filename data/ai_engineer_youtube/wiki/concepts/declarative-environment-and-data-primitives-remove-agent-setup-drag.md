# Declarative Environment and Data Primitives Remove Agent Setup Drag

Summary: Agents need runtime primitives that make environment setup and data attachment declarative, reusable, and API-driven, instead of repeatedly rebuilding containers or transferring large datasets.

Use when:
- Designing cloud workspaces where agents repeatedly need custom dependencies, datasets, or shared state.
- Reducing agent time spent on brittle setup work that a human would normally preconfigure.

Details:
- Burazin says an agent can install dependencies in a sandbox, but repeating 20 installs across runs wastes time and resources. 10:35-11:03
- A human-built Docker image and registry push adds human labor, while an agent building and pushing its own image is brittle and slow. 11:05-11:25
- Daytona's declarative image builder lets an agent state the base image, desired installations, and commands, then have the platform build the image and open a sandbox on the fly. 11:28-11:54
- Isolated agent environments lack the implicit local laptop context humans rely on, so large datasets can become expensive to move repeatedly. 11:54-12:28
- Daytona volumes let the agent upload a large dataset once and mount it as a network drive across machines, avoiding repeated S3-style transfer for every environment. 12:31-12:43

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Coding Agents](../topics/coding-agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent-Native Runtimes Provide Fast API-Controlled Sandboxes](agent-native-runtimes-provide-fast-api-controlled-sandboxes.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Branchable Cloud Workspaces Make Agent Actions Reversible](branchable-cloud-workspaces-make-agent-actions-reversible.md)

Sources:
- [AX is the only Experience that Matters - Ivan Burazin, Daytona](../sources/20250724_e9sLVMN76qU.md), 10:35-12:43
