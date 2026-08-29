# Version-Control and Unit-Test the Agent Permission Policy

Summary: If the agent security boundary is a rule set, that rule set is production code and should be treated like it — written in a real configuration language, checked into git, reviewed change by change, and covered by unit tests that feed fixture requests through the rules and assert that a specific dangerous action stays blocked. It is the answer to "how do you know your guardrails still work after last week's edit?"

Use when:
- Your agent controls are expressed as policy (proxy rules, allow-lists, tool permissions) rather than as code paths, and nothing currently tests them.
- A policy file is growing past the size where a reviewer can hold its interactions in their head.
- You are asked what regression protection exists for a security control that has no failing test when it breaks.

Details:
- **Policy as a reviewed artifact.** Deno's rules "are kind of the key piece of the system," written "in a configuration file using a language called HCL… like the Terraform configuration language. Uh it actually works really well here. So we have a file that we check into git and we manage very carefully that essentially defines the permissions for all of our services." The reviewed-change discipline is stated explicitly: "it's like a thousand lines and… we manage each and every change to that in kind of precise detail." ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 11:02-11:52)
- **The test mechanism, from Q&A.** Asked what testing keeps it honest: "this rule file actually has a test system along with it where you can provide fixtures — like fixture requests — that can flow through the rules, and then you can essentially create unit tests to make sure that… that request, it will always be blocked by your set of rules." The fixture is a captured action, and the assertion is about the *decision*, so the test survives refactors of the rule set that preserve behavior. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 17:26-18:04)
- **Two test surfaces, kept separate.** The rule file's fixtures test the policy an operator wrote; "for the claw patrol software itself we have a large suite of testing" covers the engine that parses protocols and evaluates rules. Confusing the two is how a team ends up with a well-tested engine enforcing an unexamined policy. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 17:56-18:04)
- **Why the scale makes this non-optional.** A thousand lines of allow/deny/escalate rules covering Postgres functions, cloud APIs, and cluster operations has the interaction complexity of a firewall config: any individual rule is readable, and the emergent question "is `DROP TABLE users` still blocked?" is not answerable by reading. A fixture suite converts that question into a build step. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 11:29-11:52, 17:26-18:04)
- **What a fixture should encode.** Because the enforcement unit is an "action" rather than an HTTP request — the rules run against parsed wire-protocol traffic, including traffic tunneled through other systems — a useful fixture is the byte-level action an agent would actually emit, not a summary of intent. The demo's `psql`-issued table deletion is the canonical example of an action worth pinning. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 11:52-13:14)
- **Choosing an existing configuration language over inventing one.** HCL brings variables, blocks, and existing editor and review tooling, and it puts the policy in a dialect infrastructure engineers already read. Dahl offers no comparison against alternatives beyond "it actually works really well here," so treat the specific choice as a report rather than a benchmark; the transferable part is that the policy is authored in something with a grammar and a test harness rather than accumulated in a UI. ([Ryan Dahl](../sources/20260817_MkRYPFIMCSA.md), 11:07-11:29)
- **A second product reaches the version-controlled half and stops short of the tested half, which sharpens what this page is claiming.** GitHub's agentic workflows keep the policy in front matter inside the workflow document — permissions, allowed tools, allowed network destinations, permitted writes, and a capped list of outputs — so it lives in the repository and moves through pull request like any other change, for the same reason Dahl gives: "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse. It's not actually a guardrail." What is missing is everything downstream of storage. There are no fixture tests over the policy, and the executable artifact is machine-generated and explicitly not read: "the markdown is the source code. The YAML is like a compiled artifact… You never look at it." Version control without tests or a reviewed executable form gives you history and blame but not a check that the policy still denies what it used to deny — which is the part this page argues is load-bearing. ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 07:10-07:47, 10:20-10:35)

Related topics:
- [Security](../topics/security.md)
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Make the Instrumentation Boundary Two-Way and Gate It With a Governor](make-the-instrumentation-boundary-two-way-and-gate-it-with-a-governor.md)
- [Enforce Agent Egress Policy at the Wire Protocol, Below HTTP](enforce-agent-egress-policy-below-the-http-layer.md)
- [Composed Access Defeats Per-System Credential Scoping](composed-access-defeats-per-system-credential-scoping.md)
- [Enforce Deterministic Guardrails Around Sensitive Tool Calls](enforce-deterministic-guardrails-around-sensitive-tool-calls.md)
- [Evaluate Workspace Isolation With Positive and Negative Filesystem Scorers](evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md)
- [Spec-Driven Agent Validation Goes Beyond the Test Set](spec-driven-agent-validation-goes-beyond-the-test-set.md)
- [The Markdown Workflow Is the Source; the YAML Is a Compiled Artifact](the-markdown-workflow-is-source-the-yaml-is-a-compiled-artifact.md)

Sources:
- [Security Firewall for Agents — Ryan Dahl, Deno](../sources/20260817_MkRYPFIMCSA.md), 11:02-13:14, 17:26-18:04
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 07:10-07:47, 10:20-10:35
