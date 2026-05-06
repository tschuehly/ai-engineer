# Evaluation

## Overview

Evaluation for AI engineering should measure whether models, tools, retrieval layers, skills, and agent workflows solve the intended task under real constraints. For enterprise context systems, a working connector or non-empty answer is not enough; the retrieved context must close the actual knowledge gap that blocks delivery. For coding-agent loops, checks must verify both deterministic correctness and whether an independent reviewer can see failures the producing agent missed. For skills, useful evals compare behavior with and without the skill while also validating that the harness is checking the right thing.

## Key Concepts

- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval quality is demonstrated by improved task outcomes, not by connector availability alone.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - agent failures provide concrete test cases for missing context.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - tests, review, and generated critiques should improve later loop runs.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review agents can reduce self-affirming validation.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - task scenarios and with/without comparisons reveal whether a skill changes behavior.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - incorrect assertions or judges can misreport skill impact.

## Open Questions

- Which task-level signals best distinguish a bad retrieval result from an incomplete underlying knowledge base?
- What validation should run outside the producing agent's context for code changes with production risk?
- What mix of deterministic assertions and LLM-as-judge grading is reliable enough for skill evaluation?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
