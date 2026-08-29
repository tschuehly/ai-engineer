# Agent-Legible Codebases Reduce Generated-Code Entropy

Summary: Codebases should be structured so agents can see the intended path, constraints, and source of truth. Modular flow, explicit interfaces, mechanical lint rules, and minimal hidden magic reduce duplicate work, brittle fallbacks, and behavior the team did not mean to support.

Use when:
- Refactoring a product codebase so coding agents can work safely inside it.
- Choosing lint rules, module boundaries, and source-of-truth conventions for agent-heavy development.

Details:
- Agents are optimized to produce runnable progress, so they may add forgiving fallbacks or local recovery behavior that passes immediate checks while creating brittle systems and hidden failure conditions. (07:13-08:40)
- As generated code accumulates, agents can make a codebase too large or complex for themselves to read properly, leading to duplicate implementations, missed files, and more entropy than a human-paced workflow would normally create. (08:40-09:08)
- The speakers distinguish libraries from products: libraries tend to have clearer problems, APIs, and tight constraints, while product code mixes UI, APIs, permissions, feature flags, billing, and other interacting concerns that can exceed an agent's context. (09:16-10:24)
- Agent-legible structure includes modular components and modularized code flow, such as explicit steps from user message to agent loop to output handling, because agents tend to add fuzz between unclear flow boundaries. (10:52-11:50)
- Mechanical enforcement can include no bare catch rules, centralized SQL query interfaces, one UI primitive component library, no dynamic imports, unique function names for search and token efficiency, and TypeScript modes that avoid transpilation confusion. (12:17-14:08)
- Legacy systems that humans cannot reason about also reduce agent capability: if required information is missing from the codebase and structure obscures behavior, the agent falls back to slow trial-and-error instead of direct reasoning (06:47-07:57).
- Long-lived systems need review processes that can reject harmful generated changes; otherwise agentic coding can make the codebase harder for future humans and agents to work with (13:29-14:09).

- One cheap, mechanical way to make the required information present where the agent lands: put the pointer in the comment. Khandelwal treats the codebase as the injection surface — "smartly prompt inject the model with just the right context at just the right time" — and the concrete rule is that a runbook or design doc must be "reflected in the comments so that… if somehow the agent figures its way into like [grepping] into the code base and find that file, it knows I need to go look at this." An agent's entry point is wherever its search matched, so documentation that is only reachable from a docs directory is not reachable. See [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md); note the maintenance cost the source does not price, which is that renaming the referenced file breaks the path with no test failure. ([Khandelwal](../sources/20260811_aeTb5BdmTTc.md), 07:25-08:01, 15:09-15:27)
- **Legibility for reading is now the cheaper half; legibility for running is not.** Denys Linkov reports that cross-repository *navigation* stopped being the constraint — "models are much better at navigating multiple repos. So, if you put it into a higher-level folder, right, they could navigate the file directory" — while "end-to-end testing and verification and deployment… is still much harder to do with multiple repos." As models improve, arguments for repository structure that rest on comprehension weaken every release, and arguments that rest on the agent being able to run and prove its change do not. See [Multi-Repo Cost Has Moved From Navigation to Verification](multi-repo-cost-has-moved-from-navigation-to-verification.md). ([Denys Linkov](../sources/20260808_7vn4WpqNpck.md), 15:15-15:44)
- **Legibility can be an authored index rather than a property of the source.** Figma's Code Connect links design components to codebase components, and that mapping is what lets an external tool emit "use button component" instead of a fresh implementation — entropy falls because the generator was given a name to use, not because the codebase reads better. The limit is coverage: unmapped components get full generated markup with all the divergence that implies, which is why the team wanted a workflow to scan a repository and create mappings in bulk. ([Lumarie](../sources/20260828_ZIYYsAzaLlA.md), 07:17-08:37)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Put Context Pointers Where the Agent Will Land](put-context-pointers-where-the-agent-will-land.md)
- [Use deep modules to make agent work testable](use-deep-modules-to-make-agent-work-testable.md)
- [Agent software factories need runnable, contextual, and verifiable primitives](agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md)
- [Constrain sensitive file access with purpose-built tools](constrain-sensitive-file-access-with-purpose-built-tools.md)
- [Standardize development environments around common model priors](standardize-development-environments-around-common-model-priors.md)
- [Make validation fast, local, deterministic, and actionable](make-validation-fast-local-deterministic-and-actionable.md)
- [Multi-Repo Cost Has Moved From Navigation to Verification](multi-repo-cost-has-moved-from-navigation-to-verification.md)
- [Return a Pointer to the Reader's Own Component Instead of a Faithful Copy](return-a-pointer-to-the-readers-own-component-instead-of-a-copy.md)

Sources:
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md), 07:13-14:08
- [Developer Experience in the Age of AI Coding Agents - Max Kanat-Alexander, Capital One](../sources/20251223_rT2Del5pwg4.md), 06:47-07:57, 13:29-14:09
- [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](../sources/20260811_aeTb5BdmTTc.md), 07:25-08:01, 15:09-15:27
- [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](../sources/20260808_7vn4WpqNpck.md), 15:15-15:44
- [Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma](../sources/20260828_ZIYYsAzaLlA.md), 07:17-08:37
