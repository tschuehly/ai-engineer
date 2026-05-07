# Architecture Copilots

## Overview

Architecture copilots extend AI assistance upstream from code generation into the decisions that determine whether generated code is aimed at the right system shape. Their core substrate is a live architecture model: service inventory, dependencies, cloud and Kubernetes state, logging signals, drift, and business context normalized into a system view that reflects what exists rather than what stale documentation claims.

The useful output is not generic best-practice advice. Architecture copilots should rank recommendations by business impact, explain their evidence, and show tradeoffs across cost, performance, risk, time to value, existing investments, and strategic goals. That makes them a planning and governance tool as much as an agent interface.

The developer-workflow boundary matters. As organizations shift architecture decisions left, periodic architecture-guild reviews do not scale. A copilot can embed policy, standards, and expert guidance into the same workflow where developers and coding agents generate designs or code, turning governance into alignment by design instead of a blocking gate.

## Key Concepts

- [Live architecture digital twins ground architecture copilots](../concepts/live-architecture-digital-twins-ground-architecture-copilots.md) - architecture advice needs a current system model before it can be trusted.
- [Rank architecture recommendations by business impact](../concepts/rank-architecture-recommendations-by-business-impact.md) - recommendations should be explainable, traceable, and tied to business metrics.
- [Embed architecture governance into developer workflows](../concepts/embed-architecture-governance-into-developer-workflows.md) - architecture standards should guide developers at decision time without becoming a bottleneck.

## Open Questions

- Which sources should be mandatory before a live architecture model is trustworthy enough to support recommendations?
- Which recommendation scores can be measured from operational data, and which require explicit business or architecture assumptions?
- How should architecture copilots hand off approved direction to coding agents without losing traceability to the original decision?

## Sources

- [AI Copilots for Tech Architecture: The Highest-ROI Use Case You're Not Building - Boris B., Catio](../sources/20251124_QRWdapxMdSY.md)
