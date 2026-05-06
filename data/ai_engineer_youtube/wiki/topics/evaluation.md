# Evaluation

## Overview

Evaluation for AI engineering should measure whether models, tools, retrieval layers, skills, context packages, and agent workflows solve the intended task under real constraints. Adoption metrics need the same discipline: raw token volume, AI spend, or leaderboard rank should not be treated as developer productivity because visible usage targets can push engineers toward token generation rather than valuable outcomes. For enterprise context systems, a working connector or non-empty answer is not enough; the retrieved context must close the actual knowledge gap that blocks delivery. For production AI applications, evaluation should connect offline golden data sets, deterministic scores, LLM-as-judge checks, online production scoring, and failure replay so prompt or workflow fixes are measured against both the triggering trace and the broader regression set. Eval platforms also need to mature from ad hoc spreadsheet documentation into experiment systems where technical and domain users can compare configurations, score failure modes, and pull production traces back into offline regression loops. Model evals should include premise-pushback and dissatisfaction signals, because rising benchmark scores can hide models that answer nonsensical requests or produce two "best available" answers users still reject. For coding-agent loops, checks must verify both deterministic correctness and whether an independent reviewer can see failures the producing agent missed. Prompt-coded workspace workflows need an additional negative eval dimension: the agent should do the desired work in its assigned workspace and should not mutate the primary checkout or another forbidden location. Voice-agent evals add realtime and audio-specific concerns: traces, labeled conversations, transcript rubrics, function-call checks, tone and pacing judgments, synthetic conversations, and asynchronous guardrails all contribute different signals. Planning depth is also an evaluation lever: tasks that can be specified and tested should reduce later review churn, while exploratory front-end work may need interactive QA. Agent coding evals should also account for feedback speed: if tests, type checks, and review cannot keep pace with generated code volume, the agent is outrunning its verification loop. Product-quality evaluation has a softer but important layer: some quality debt accumulates as small interaction regressions, missing polish, slow-feeling animations, and customer drift that may not show up in short-term A/B tests. For skills and context files, useful evals compare behavior with and without the context, validate package format and clarity, and use repeated runs or error budgets when results are nondeterministic. Agent runs can also be interrogated directly after completion: asking what would have set the agent up better can reveal missing tools, contradictory instructions, permissions gaps, or wrong-language context before those defects silently repeat. For model training, basic train and validation loss curves are an early diagnostic layer before generated samples or downstream task evals are trusted. Small reasoning models add a generated-output failure mode: repetitive doom loops may survive SFT and need preference-alignment or reinforcement-learning evals that detect non-terminating repetition, missing final answers, and rewardable task completion. LLM judges themselves need evaluation: when a judge is used as a pass/fail classifier, its prompt and examples should be calibrated against domain-expert labels on a development split and validated on a held-out test split with metrics such as F1.

## Key Concepts

- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - side-by-side model comparisons help choose enough reasoning at acceptable speed and cost.
- [Do not use token volume as a developer productivity metric](../concepts/do-not-use-token-volume-as-a-developer-productivity-metric.md) - adoption dashboards should avoid rewarding visible token spend over task impact.
- [Make agent work more trustworthy by making it verifiable](../concepts/make-agent-work-more-trustworthy-by-making-it-verifiable.md) - agent autonomy depends on whether tasks have direct checks, proxy checks, or safe constraints.
- [Evaluate whether models reject impossible or nonsensical premises](../concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - models should be judged on when they stop, clarify, or reject bad premises, not only on how well they solve valid tasks.
- [Track user dissatisfaction alongside pairwise model preference](../concepts/track-user-dissatisfaction-alongside-pairwise-model-preference.md) - "both bad" feedback exposes absolute failure rates that winner-only model comparisons hide.
- [Benchmark narrow slices separately from real expert work](../concepts/benchmark-narrow-slices-separately-from-real-expert-work.md) - benchmark gains should be checked against open-ended expert prompts and shifting user expectations.
- [Sandboxed code execution turns model reasoning into inspectable computation](../concepts/sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md) - executable computation can make some model outputs easier to inspect and verify.
- [Mature eval platforms from spreadsheets into experiment systems](../concepts/mature-eval-platforms-from-spreadsheets-into-experiment-systems.md) - credible eval infrastructure should support comparison, collaboration, and scoring beyond documented output tables.
- [Connect production observability to offline eval loops](../concepts/connect-production-observability-to-offline-eval-loops.md) - real traces expose failure modes and should become replayable offline examples.
- [Agent traces require specialized eval infrastructure](../concepts/agent-traces-require-specialized-eval-infrastructure.md) - agent observability data can be too large, text-heavy, and semi-structured for naive trace storage.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval quality is demonstrated by improved task outcomes, not by connector availability alone.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - agent failures provide concrete test cases for missing context.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - tests, review, and generated critiques should improve later loop runs.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review agents can reduce self-affirming validation.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - task shape determines whether upfront specification or review iteration is the more efficient validation path.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - task scenarios and with/without comparisons reveal whether a skill changes behavior.
- [Evaluate workspace isolation with positive and negative filesystem scorers](../concepts/evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md) - workspace evals should check both intended isolated edits and forbidden primary-checkout edits.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - incorrect assertions or judges can misreport skill impact.
- [Use loss curves to debug local model training](../concepts/use-loss-curves-to-debug-local-model-training.md) - train and validation loss patterns separate non-learning, overfitting, and instability.
- [Mitigate small-model doom loops during preference alignment and RL](../concepts/mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md) - small reasoning models need output-loop checks and post-training reward signals beyond SFT.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - production evaluation of edge agents should account for runtime guardrails, not only raw model output.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - context evals need structural checks, behavioral scenarios, and repeated-run thresholds.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - production and review feedback should become test cases or context improvements.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice evals need observability, transcript checks, audio judgments, simulations, and latency-aware guardrails.
- [Use golden data sets and mixed scoring functions for AI application confidence](../concepts/use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md) - curated edge cases plus deterministic and judge-model scores create a repeatable release gate.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - production monitoring should score live traces while sampling expensive model-based judges deliberately.
- [Replay production failures before promoting prompt fixes](../concepts/replay-production-failures-before-promoting-prompt-fixes.md) - production failures should become replayable regression cases before a prompt patch is trusted.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](../concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - realtime evals may need to inspect streamed audio, visual context, tool events, and latency together.
- [Ask agents after each run what blocked their success](../concepts/ask-agents-after-each-run-what-blocked-their-success.md) - post-run self-reporting can expose setup and context failures.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - agent readiness should be validated through runnable setup, tests, and user-flow checks.
- [Automation loops convert repeated review and triage into factory improvements](../concepts/automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md) - review and triage outputs should feed evals, rules, or process changes.
- [Encode agent intent into server-side tools](../concepts/encode-agent-intent-into-server-side-tools.md) - tool descriptions should be evaluated in relation to competing tools, not only optimized individually.
- [Delegate implementations behind reviewed module interfaces](../concepts/delegate-implementations-behind-reviewed-module-interfaces.md) - module interfaces and tests let reviewers validate agent work without reading every internal line.
- [Limit agent change size by feedback speed](../concepts/limit-agent-change-size-by-feedback-speed.md) - agent diffs should be constrained by how quickly tests, type checks, and review can provide signal.
- [Use deep modules to make agent work testable](../concepts/use-deep-modules-to-make-agent-work-testable.md) - module interface tests can validate agent-written internals without full-line-by-line review.
- [Quality Wednesdays train engineers to notice small regressions](../concepts/quality-wednesdays-train-engineers-to-notice-small-regressions.md) - quality rituals create human detection signals for polish issues that metrics may miss.
- [AI agents still need human taste for interaction quality](../concepts/ai-agents-still-need-human-taste-for-interaction-quality.md) - UI eval needs human judgment when generated interactions are functional but feel wrong.
- [Calibrate LLM judges like binary classifiers](../concepts/calibrate-llm-judges-like-binary-classifiers.md) - judge prompts need dev/test validation before they gate workflow quality.

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
- How reliable is agent self-reporting as an eval signal compared with trace inspection or deterministic failure classifiers?
- How should evaluators score realtime multimodal sessions when the model's answer depends on both live audio and low-frame-rate visual context?
- How should doom-loop metrics be weighted against ordinary task accuracy for small reasoning models?
- Which trace storage model best supports replay, scoring, privacy controls, and query performance for large semi-structured agent traces?
- How should tool-selection evals detect both over-eager tools and tools that are hidden when they should be called?
- Which module-level tests are strong enough to let reviewers delegate internals without losing system control?
- Which premise-rejection evals are reliable enough to run before deploying high-autonomy agents?
- How should dissatisfaction rates be normalized when users ask harder prompts as models improve?
- Which proxy checks are strong enough to stand in for delayed human or legal verification?
- Which AI adoption metrics distinguish useful agent leverage from performative token generation?
- Which product-quality regressions can be detected mechanically, and which still require trained human taste?
- Which LLM judge labels are safe to automate, and which still require domain-expert review before calibration?

## Sources

- [Build & deploy AI-powered apps - Paige Bailey, Google DeepMind](../sources/20260429_G_bHFmEAarM.md)
- [Everything I Learned Training Frontier Small Models - Maxime Labonne, Liquid AI](../sources/20260429_fLUtUkqYHnQ.md)
- [Why building eval platforms is hard - Phil Hetzel, Braintrust](../sources/20260428__fQ7Z_Wfouk.md)
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
- [Building Conversational Agents - Thor Schaeff and Philipp Schmid, Google DeepMind](../sources/20260430_cVzf49yg0D8.md)
- [LLM codegen fails and how to stop 'em - Danilo Campos, PostHog](../sources/20260430_juoNbJiZUi0.md)
- [Building your own software factory — Eric Zakariasson, Cursor](../sources/20260428_rnDm57Py54A.md)
- [Scaling GitHub for your Agents — Sam Morrow, GitHub](../sources/20260427_0n3MKk7r60w.md)
- [Full Walkthrough: Workflow for AI Coding - Matt Pocock](../sources/20260424_-QFHIoCo-Ko.md)
- [What Do Models Still Suck At? - Peter Gostev, Arena.ai, BullshitBench](../sources/20260424_R7A8rX-09Zw.md)
- ["Software Fundamentals Matter More Than Ever" - Matt Pocock](../sources/20260423_v4F1gFy-hqg.md)
- [Agents need more than a chat - Jacob Lauritzen, CTO Legora](../sources/20260422_XNtkiQJ49Ps.md)
- [How AI is changing Software Engineering: A Conversation with Gergely Orosz, @pragmaticengineer](../sources/20260421_CS5Cmz5FssI.md)
- [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer](../sources/20260421_wjk0ulMAkbc.md)
- [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](../sources/20260420_mYSRn6PC1mc.md)
