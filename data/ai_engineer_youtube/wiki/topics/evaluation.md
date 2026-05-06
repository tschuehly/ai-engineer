# Evaluation

## Overview

Evaluation for AI engineering should measure whether models, tools, retrieval layers, skills, context packages, and agent workflows solve the intended task under real constraints. For enterprise context systems, a working connector or non-empty answer is not enough; the retrieved context must close the actual knowledge gap that blocks delivery. For production AI applications, evaluation should connect offline golden data sets, deterministic scores, LLM-as-judge checks, online production scoring, and failure replay so prompt or workflow fixes are measured against both the triggering trace and the broader regression set. For coding-agent loops, checks must verify both deterministic correctness and whether an independent reviewer can see failures the producing agent missed. Prompt-coded workspace workflows need an additional negative eval dimension: the agent should do the desired work in its assigned workspace and should not mutate the primary checkout or another forbidden location. Voice-agent evals add realtime and audio-specific concerns: traces, labeled conversations, transcript rubrics, function-call checks, tone and pacing judgments, synthetic conversations, and asynchronous guardrails all contribute different signals. Planning depth is also an evaluation lever: tasks that can be specified and tested should reduce later review churn, while exploratory front-end work may need interactive QA. For skills and context files, useful evals compare behavior with and without the context, validate package format and clarity, and use repeated runs or error budgets when results are nondeterministic. For model training, basic train and validation loss curves are an early diagnostic layer before generated samples or downstream task evals are trusted.

## Key Concepts

- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval quality is demonstrated by improved task outcomes, not by connector availability alone.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - agent failures provide concrete test cases for missing context.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - tests, review, and generated critiques should improve later loop runs.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review agents can reduce self-affirming validation.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - task shape determines whether upfront specification or review iteration is the more efficient validation path.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - task scenarios and with/without comparisons reveal whether a skill changes behavior.
- [Evaluate workspace isolation with positive and negative filesystem scorers](../concepts/evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md) - workspace evals should check both intended isolated edits and forbidden primary-checkout edits.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - incorrect assertions or judges can misreport skill impact.
- [Use loss curves to debug local model training](../concepts/use-loss-curves-to-debug-local-model-training.md) - train and validation loss patterns separate non-learning, overfitting, and instability.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - production evaluation of edge agents should account for runtime guardrails, not only raw model output.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - context evals need structural checks, behavioral scenarios, and repeated-run thresholds.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - production and review feedback should become test cases or context improvements.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice evals need observability, transcript checks, audio judgments, simulations, and latency-aware guardrails.
- [Use golden data sets and mixed scoring functions for AI application confidence](../concepts/use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md) - curated edge cases plus deterministic and judge-model scores create a repeatable release gate.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - production monitoring should score live traces while sampling expensive model-based judges deliberately.
- [Replay production failures before promoting prompt fixes](../concepts/replay-production-failures-before-promoting-prompt-fixes.md) - production failures should become replayable regression cases before a prompt patch is trusted.

## Open Questions

- Which task-level signals best distinguish a bad retrieval result from an incomplete underlying knowledge base?
- What validation should run outside the producing agent's context for code changes with production risk?
- What mix of deterministic assertions and LLM-as-judge grading is reliable enough for skill evaluation?
- Which generated-sample checks add signal after a tiny model's loss curves look healthy?
- How should CI present nondeterministic context-eval results so teams can act on trend and error-budget changes without chasing noise?
- How should teams measure whether extra planning actually reduces review rounds for a class of coding-agent tasks?
- How long should workspace-isolation eval sessions run before they catch drift that appears only in extended agent work?
- Which audio-specific judgments add enough signal beyond transcript evals to justify their extra cost?
- How much live traffic should receive LLM-as-judge scoring before teams have enough baseline confidence to lower sampling?
- What metadata is necessary to replay a production trace without leaking sensitive user data into eval infrastructure?

## Sources

- [Demand-Driven Context: A Methodology for Coherent Knowledge Bases Through Agent Failure](../sources/20260505__QAVExf_1uw.md)
- [Ralph Loops: Build Dumb AI Loops That Ship - Chris Parsons, Cherrypick](../sources/20260504_2TLXsxkz0zI.md)
- [Skill Issue: How We Used AI to Make Agents Actually Good at Supabase - Pedro Rodrigues, Supabase](../sources/20260504_GmAQKINjv1E.md)
- [Training an LLM from Scratch, Locally - Angelos Perivolaropoulos, ElevenLabs](../sources/20260504_UsB70Tf5zcE.md)
- [TLMs: Tiny LLMs and Agents on Edge Devices with LiteRT-LM - Cormac Brick, Google](../sources/20260503_BKWpYIWvAo4.md)
- [Context Is the New Code - Patrick Debois, Tessl](../sources/20260503_bSG9wUYaHWU.md)
- [Software Engineering Is Becoming Plan and Review - Louis Knight-Webb, Vibe Kanban](../sources/20260502_W76woOYHlvY.md)
- [Building Effective Voice Agents - Toki Sherbakov + Anoop Kotha, OpenAI](../sources/20250720_-OXiljTJxQU.md)
- [Shipping complex AI applications - Braintrust & Trainline](../sources/20260501_ZdheJTfLu-s.md)
- [Replacing 12K LoC with a 200 LoC Skill - David Gomes, Cursor](../sources/20260430_WE_Gnowy3uw.md)
