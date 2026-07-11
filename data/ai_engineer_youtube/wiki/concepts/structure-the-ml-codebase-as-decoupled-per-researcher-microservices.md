# Structure the ML Codebase as Decoupled Per-Researcher Microservices

Summary: Keep the AI/ML code in a separate Python mono repo of cleanly isolated, fully decoupled microservices at roughly one microservice per researcher, each a standalone layered FastAPI app behind a shared gateway, so a research prototype can be received and stood up in production quickly and independently — and decompose the prototype into stacked diffs for asynchronous subject-matter-expert review.

Use when:
- You are designing where frontier ML research lands so prototypes can be productionized without fighting old abstractions.
- Multiple researchers each own a distinct initiative (a custom transformer, a diffusion pipeline) that should iterate without coupling to the others or to the core product.
- You need to bring a large monolithic research prototype into a production repo and get the right reviewers on the right slices.

Details:
- Use a **separate repo from the core product repo**, all Python, structured as a mono repo of "cleanly isolated and fully decoupled microservices," at roughly a one-researcher-to-one-microservice ratio (e.g. "data-driven entity prediction" is one researcher's custom transformer), so each initiative grows and iterates independently (06:38-07:41).
- A **gateway guards requests** on one Docker bridge network; web-app clients call the gateway, which routes to the appropriate microservice rather than clients calling a service directly (07:41-08:00, 08:53-09:08).
- Each microservice is a **standalone layered FastAPI application**: core business logic at the services layer (may make external LLM calls to foundation models, or pull the team's own model weights in CI/CD), wrapped by controllers, then API routers exposed as a FastAPI app — API layer / business logic / data layer (08:00-08:53).
- Each microservice root holds metadata, build instructions, a Dockerfile, project dependencies, and poetry/UV lock files; the three production microservices share a consistent "skeletal backbone" that is easy to map out and grow along software-engineering best practices (09:08-09:49).
- Beneath the services sits shared infrastructure: GitHub Actions for build/deploy, automated test suites, linting/formatting/type checks; Jupyter notebooks running on **Modal** for GPU compute; ML studies; and a tooling layer plus a CLI whose only job is to support ML engineers in bundling up the microservices. Specs are "really cleanly documented… so that agents can navigate these repositories and help accelerate our ML researchers" (09:49-10:32, 08:12-08:24).
- Landing a prototype is a **decomposition design problem**: study which axes to slice the monolithic prototype on and its dependency graph, then use **Graphite stacked diffs** to decompose it. Graphite is favored for asynchronous review — "I could be working on a PR up here while a domain specialist is still reviewing a different PR" — letting the team tap subject-matter experts on specific tightly-scoped slices (10:32-12:14).
- Diagnostics for this lever: is it clear where new code goes, with templates/frameworks/patterns to mimic, or have you outgrown the architecture and keep "fighting these old abstractions"? And can you consistently estimate timelines and know which SMEs to tap — if not, the issue points upstream to handoff coordination or the code base itself (13:22-14:35).

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Bridge ML Research to Production With a Taxonomy Handoff Document](bridge-ml-research-to-production-with-a-taxonomy-handoff-document.md)
- [Decompose Large Refactors Into Dependency-Aware Agent Batches](decompose-large-refactors-into-dependency-aware-agent-batches.md)
- [Treat Multi-Agent Systems as Distributed Systems](treat-multi-agent-systems-as-distributed-systems.md)

Sources:
- [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](../sources/20260628_OXMMN-XbxwA.md), 06:38-14:35
