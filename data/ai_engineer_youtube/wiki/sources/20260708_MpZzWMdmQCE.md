# Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com

Source: [Your coding agent doesn't always follow your rules — Talha Sheikh, Checkout.com](https://www.youtube.com/watch?v=MpZzWMdmQCE)
Uploaded: 2026-07-08
Transcript: `raw/20260708_MpZzWMdmQCE/MpZzWMdmQCE.en-orig.vtt`

## Summary

Talha Sheikh (Checkout.com) frames a familiar frustration — Claude Code fans out sub-agents, reports "task completed," but the thing doesn't actually run, so you keep telling it "fix this, fix that" — as a structural problem: *you* are the enforcement layer, because the agent says it's done and nothing else can check it for you. His fix is an **agent harness**: a deterministic verification layer that fires automatically when the agent claims it is finished, checks the output against a config file of test cases, and loops "try again" back into the agent until the checks pass. He built this as a product ("Vector V1" / "Vector Harness", open source) wired through Claude's Stop hook. Two conceptual distinctions carry the talk: capability ≠ reliability (a newer model is more capable but not necessarily more reliable), and instructions ≠ verification (the best spec, MCP servers, sub-agents, and context are still not a check that the work was done the way you wanted). A tighter guardrail layer also lets you downshift to a smaller/cheaper model (Haiku, open source) because failed attempts are caught and retried, trading harness-engineering time for model cost. After an Anthropic engineer told him a smarter future model would make enforcement unnecessary, he re-grounded the idea as a *pattern* everyone reinvents (Anthropic, Meta, his own company), so it should be language-agnostic, shareable, and bring-your-own-enforcement, running at every level (in-conversation, conversation-end, pre-commit, multi-agent, async, plus optional LLM-as-judge). He points to industry convergence — Anthropic's executor/advisor pattern, OpenAI's harness engineering, CodeRabbit-style comprehensive PR review, WorkOS's "enforce, don't instruct," and "slow the hell down" keynote lines — as the same feedback loop. The closing shift: value used to live in the code you create; now it lives in the verification you design — "not can you code, but can you verify?" TLDR: work on the harness, not the code.

## Extracted Concepts

- [Wrap Agent Completion in an Automatic Deterministic Verification Gate](../concepts/wrap-agent-completion-in-an-automatic-deterministic-verification-gate.md) - the human-as-enforcement-layer problem and its fix: a Stop-hook-triggered deterministic check-and-retry gate on the agent's "done."
- [Verification Guardrails Let You Downshift to Cheaper Models](../concepts/verification-guardrails-let-you-downshift-to-cheaper-models.md) - tighter guardrails catch and retry failures, so a smaller/cheaper model reaches the target output, trading harness time for model cost.
- [Harness Engineering Shifts Scarcity From Code Production to Control Surfaces](../concepts/harness-engineering-shifts-scarcity-from-code-production-to-control-surfaces.md) - independent field report that value has shifted from the code you create to the verification you design ("work on the harness, not the code").

## Topic Links

- [Coding Agents](../topics/coding-agents.md)
- [Workflows](../topics/workflows.md)
- [Tools](../topics/tools.md)

## Notes

- The human is the default enforcement layer: the agent "starts putting it out into subtasks," reports "task completed," but "when you actually try to run it… something else failed," so you keep issuing "fix this, fix that" — "I am the enforcement layer… there's nothing else that can check it for you." 00:15-01:36
- The fix is a deterministic completion gate: he built "Vector V1," which "deterministically checks Claude's output… through using Claude hooks. So whenever Claude finishes its session, it automatically the hook calls my vector product," reads a config file of test cases, and on failure "keeps on telling Claude… try again" until the tests pass. 01:57-02:40
- The real object is trust, not capability: "it's not about whether Claude can actually do the task, it's about trust… when I give a task to a coding agent, does it actually complete it?" (and "when I say Claude, I'm just talking in general about LLM agents"). 02:40-02:56
- Capability ≠ reliability: "when a new model comes out… it increases in capability, but that's not necessarily the same thing as reliability. Sure, the model may become a lot more capable, but are they more reliable?" 03:45-04:02
- Instructions ≠ verification: even with the best spec, MCP servers, sub-agents, and context, "giving it instructions is not the same thing as giving it verification… you still will need to verify." 04:12-04:24
- Guardrails enable cheaper models: with guardrails on, "you can use a smaller model like a Haiku or even an open source model… it'll most likely be succinct and get you to the output you want"; frontier Opus alone is most expensive, but "if you put on more guardrails… invest a little bit more time in the harness itself, you can reduce the cost drastically," and async tasks help too. 04:24-05:03
- Enforcement is a reinvented pattern, not a product: "everybody's building their own stuff. Anthropic… my company… Meta… every company," and what one team enforces differs from another, so "it has to be a pattern… language agnostic… shared by everybody, and everybody can bring their own version of enforcement." 05:11-06:03
- It should run at every level: "in conversation… before committing… part of a multi-agent workflow… on asynchronous agents… as well as a check that non-deterministically calls an LLM as a judge," on any language/code "as long as there's a capability to run it deterministically" — a "contract" in the middle that developers and users define. 06:03-06:47
- Industry convergence on the same feedback loop: Anthropic's "executor advisor pattern" (one agent codes, an advisor creates a feedback loop = verify); OpenAI's harness engineering (tools + context so you can verify); CodeRabbit-style "comprehensive PR review" with issues/findings ("do you trust it? No" → feedback loop); WorkOS's "enforce, don't instruct"; and "slow the hell down" keynote lines that are really about the verification layer, not model speed. 06:54-08:22
- The shift: "initially… the value is in the code that we create. But… in reality… it's the verification that we design. So it's not about can you code, but can you verify?" TLDR — "work on the harness, and not on the code." 08:22-08:51
- The tool is public as "Vector Harness"; a Q&A joke ("you're a top token spender at your company" → "I need those tokens to build a verification layer") underlines the harness-investment tradeoff. 09:08-09:43
