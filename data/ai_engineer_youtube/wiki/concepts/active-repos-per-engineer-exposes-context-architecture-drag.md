# Active Repos Per Engineer Exposes Context Architecture Drag

Summary: Active repositories per engineer is a practical proxy for how distributed a code architecture feels to workers and agents. Highly distributed repo layouts can block AI coding gains when tools cannot access cross-repo context and undocumented system relationships.

Use when:
- Explaining why high AI tool adoption may not produce expected productivity gains.
- Evaluating whether repository architecture and context engineering are limiting coding-agent usefulness.

Details:
- Jellyfish measures architecture shape with active repos per engineer: the number of distinct repositories a typical engineer pushes code to in a week. (12:12-12:25)
- The metric is framed as scale-independent because normalizing by engineer count removes direct company-size correlation and exposes the daily shape of code work. (12:25-12:49)
- Segmenting PR-throughput trends by this metric changed the adoption story: centralized and balanced architectures showed roughly 4x throughput trends, distributed architectures resembled the global 2x trend, and highly distributed architectures showed essentially no positive correlation. (13:23-14:28)
- The proposed mechanism is context: current coding tools usually work best in one repository at a time, while relationships across repositories, systems, and products are often undocumented or locked in senior engineers' heads. (14:44-15:20)
- Highly distributed architectures may become more effective if teams solve cross-repo context engineering and deploy autonomous agents at scale, but the observed current-state data did not show that yet. (15:22-15:52)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Codebase hygiene amplifies AI productivity gains](codebase-hygiene-amplifies-ai-productivity-gains.md)
- [Context engines select task-specific organizational context](context-engines-select-task-specific-organizational-context.md)
- [Enterprise agent failures often expose missing institutional knowledge](enterprise-agent-failures-expose-missing-institutional-knowledge.md)

Sources:
- [What Data from 20m Pull Requests Reveal About AI Transformation - Nick Arcolano, Jellyfish](../sources/20251124_WqZq8L-v9pA.md), 11:39-15:52
