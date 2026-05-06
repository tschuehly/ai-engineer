# Standardize Development Environments Around Common Model Priors

Summary: Coding agents work better when the repository uses conventional tools, languages, package managers, and workflows that resemble common public examples. Custom or obscure development environments force agents to fight their training-set priors before they can solve the actual task.

Use when:
- Preparing an enterprise codebase for broad coding-agent use.
- Deciding whether a custom package manager, language, linter, or toolchain is worth the agent-readiness cost.

Details:
- Standardized development environments are a no-regrets investment because they help both humans and agents build, test, and reason about code (02:34-02:55).
- Agents are more effective when industry-standard tools are used in familiar ways because those patterns are more likely to appear in model training data; instruction files can help, but they still fight against unusual local conventions (02:55-03:37).
- Teams should be cautious about obscure programming languages, invented package managers, and heavily modified developer tools for production agentic work because they reduce the model's usable prior knowledge (03:37-04:00).
- The source does not claim new tools should never exist; it frames conventionality as a production-readiness constraint, especially for high-scale or enterprise systems where unvetted novelty was already risky (04:00-04:34).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Agent-legible codebases reduce generated-code entropy](agent-legible-codebases-reduce-generated-code-entropy.md)

Sources:
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 02:34-04:34
