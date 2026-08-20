# Wrap Agent Completion in an Automatic Deterministic Verification Gate

Summary: A coding agent's "task completed" is untrustworthy on its own — by default the human is the enforcement layer who has to run and re-check the work. Replace that manual step with a harness that fires automatically when the agent claims it is done, runs deterministic checks against a config of expected outcomes, and loops corrective "try again" feedback back into the agent until the checks pass.

Use when:
- An agent reports success but the output doesn't actually run, and you keep issuing one-off "fix this, fix that" corrections by hand.
- Deciding whether to trust an agent's self-declared completion or to gate it behind an automated check.
- Standing up an enforcement/verification layer that should run at multiple points in an agent workflow, not just at PR time.

Details:
- The default failure mode: the agent fans out sub-agents, reports "task completed," but "when you actually try to run it… something else failed," so the human becomes the enforcement layer — "I have to tell Claude on what exactly you need to do and how exactly this needs to be enforced… there's nothing else that can check it for you." The object is trust, not capability: "does it actually complete it?" ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 00:15-02:56)
- The mechanism: wire the check to the agent's completion event — Vector V1 uses Claude's Stop hook so "whenever Claude finishes its session, the hook automatically calls my vector product," which reads a config file of test cases, and on failure "keeps on telling Claude… try again" until the tests pass. This is a deterministic completion gate, not a prompt instruction. ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 01:57-02:40)
- Two distinctions justify the gate even as models improve. Capability ≠ reliability: a newer model "increases in capability, but that's not necessarily the same thing as reliability." Instructions ≠ verification: the best spec, MCP servers, sub-agents, and context are still not a check — "you still will need to verify." So the gate is not made obsolete by a smarter model (contra an Anthropic engineer's "you won't need enforcement"). ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 03:45-04:24)
- Enforcement is a *pattern* everyone reinvents (Anthropic, Meta, his own company), and what one team enforces differs from another's, so the durable shape is language-agnostic, shareable, and bring-your-own-enforcement: a "contract" in the middle that developers/users define. It should run at every level — in-conversation, on conversation-end, pre-commit, inside a multi-agent workflow, on async agents — with an optional non-deterministic LLM-as-judge check, on any code "as long as there's a capability to run it deterministically." ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 05:11-06:47)
- Industry convergence on the same feedback loop: Anthropic's executor/advisor pattern (a coding agent plus an advisor that feeds back), OpenAI's harness engineering (tools + context so the work can be verified), CodeRabbit-style comprehensive PR review (issues/findings → feedback loop because "do you trust it? No"), WorkOS's "enforce, don't instruct," and "slow the hell down" keynote lines that are really about the verification layer. The shift: value moved from "the code that we create" to "the verification that we design" — "not can you code, but can you verify?" ([Talha Sheikh](../sources/20260708_MpZzWMdmQCE.md), 06:54-08:51)

- **A vendor instance of the same gate, with the verdict as the agent's exit condition rather than as a post-hoc hook.** In Sonar's demo, Cursor writes, then "on completing the initial write, it's going to call into our verification process to get a list of issues," fixes them, reruns the analysis, "and then it will not proceed until it actually is able to get a passing grade from us on the verification pass." Two differences from the Stop-hook shape above are worth noting. The check is invoked by the agent as a tool rather than fired by the harness on a completion event, which makes it cheaper to run mid-task but leaves the agent able to skip it — the enforcement lives in the prompt/loop rather than outside it. And the same regime is required to run again at the PR gate: "the verification needs to run in both the inner agentic loop and also in the outer loop for CICD," so the in-loop gate is a way to reach the blocking gate clean, not a substitute for it. See [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md). Vendor talk, pre-recorded demo, no measurement. ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 18:58-19:57)

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Use hooks for deterministic agent verification and live context injection](use-hooks-for-deterministic-agent-verification-and-live-context-injection.md)
- [Enforce Agent Rules in Git Hooks and CI, Not the Prompt](enforce-agent-rules-in-git-hooks-and-ci-not-the-prompt.md)
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md)
- [Separate generation and verification prompts or models](separate-generation-and-verification-prompts-or-models.md)
- [Make Agent Work More Trustworthy by Making It Verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)
- [Verification Guardrails Let You Downshift to Cheaper Models](verification-guardrails-let-you-downshift-to-cheaper-models.md)
- [Self-Verifying Agent Loops Hide Review Rather Than Remove It](self-verifying-agent-loops-hide-review-rather-than-remove-it.md)
- [Fix Defects Inside the Agent Loop Before They Become Foundation](fix-defects-inside-the-agent-loop-before-they-become-foundation.md)
- [Choose Verification Layers by Defect-Class Coverage](choose-verification-layers-by-defect-class-coverage.md)

Sources:
- [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](../sources/20260708_MpZzWMdmQCE.md), 00:15-08:51
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 18:58-19:57
