# Evaluation

## Overview

Evaluation for AI engineering should measure whether models, tools, retrieval layers, skills, context packages, and agent workflows solve the intended task under real constraints. Adoption metrics need the same discipline: raw token volume, AI spend, or leaderboard rank should not be treated as developer productivity because visible usage targets can push engineers toward token generation rather than valuable outcomes. Even direct speedup claims need careful measurement: benchmark and time-horizon gains should be checked against field experiments on real developer work, and self-reported task duration should not be treated as reliable elapsed-time data. Benchmark percentages also have a lifecycle problem: once a benchmark moves quickly from first signal to saturation, capability evals need harder task distributions or human-time-horizon measurements, but those still need field validation before they are treated as productivity forecasts. For enterprise context systems, a working connector or non-empty answer is not enough; the retrieved context must close the actual knowledge gap that blocks delivery. For production AI applications, evaluation should connect offline golden data sets, deterministic scores, LLM-as-judge checks, online production scoring, and failure replay so prompt or workflow fixes are measured against both the triggering trace and the broader regression set. Eval platforms also need to mature from ad hoc spreadsheet documentation into experiment systems where technical and domain users can compare configurations, score failure modes, and pull production traces back into offline regression loops. Model evals should include premise-pushback and dissatisfaction signals, because rising benchmark scores can hide models that answer nonsensical requests or produce two "best available" answers users still reject. For coding-agent loops, checks must verify both deterministic correctness and whether an independent reviewer can see failures the producing agent missed. Prompt-coded workspace workflows need an additional negative eval dimension: the agent should do the desired work in its assigned workspace and should not mutate the primary checkout or another forbidden location. Voice-agent evals add realtime and audio-specific concerns: traces, labeled conversations, transcript rubrics, function-call checks, tone and pacing judgments, synthetic conversations, and asynchronous guardrails all contribute different signals. Planning depth is also an evaluation lever: tasks that can be specified and tested should reduce later review churn, while exploratory front-end work may need interactive QA. Agent coding evals should also account for feedback speed and review capacity: if tests, type checks, architecture review, and human inspection cannot keep pace with generated code volume, the agent is outrunning its verification loop and may turn large diffs into rubber-stamped risk. A benchmark pass can still fail a mergeability test when the output requires expensive review, correction, maintainability judgment, or context reconstruction. Product-quality evaluation has a softer but important layer: some quality debt accumulates as small interaction regressions, missing polish, slow-feeling animations, and customer drift that may not show up in short-term A/B tests. For skills and context files, useful evals compare behavior with and without the context, validate package format and clarity, and use repeated runs or error budgets when results are nondeterministic. Agent runs can also be interrogated directly after completion: asking what would have set the agent up better can reveal missing tools, contradictory instructions, permissions gaps, or wrong-language context before those defects silently repeat. For model training, basic train and validation loss curves are an early diagnostic layer before generated samples or downstream task evals are trusted. Small reasoning models add a generated-output failure mode: repetitive doom loops may survive SFT and need preference-alignment or reinforcement-learning evals that detect non-terminating repetition, missing final answers, and rewardable task completion. LLM judges themselves need evaluation: when a judge is used as a pass/fail classifier, its prompt and examples should be calibrated against domain-expert labels on a development split and validated on a held-out test split with metrics such as F1. A judge should usually be decomposed by error type into narrow binary metrics, because broad "success" judges and scalar scores are harder to align with human labels. Prompt optimizers such as GEPA can improve judge rubrics, but only when they receive useful diagnostic feedback such as the judge verdict, human ground truth, reasoning, and relevant domain priors.

Incoming AI-generated work needs evaluation too: automated security reports, issues, pull requests, and fixes can be high-volume and plausible, but maintainers still need to triage them because false reports, low-context fixes, and rushed patches can consume review capacity or break the product. Contribution gates that demand concise human context can be a practical first-pass evaluator before maintainers inspect a generated diff.

Reliable AI app evals should also be reverse-engineered from user-visible outcomes before optimization begins. Generic measures such as groundedness, factuality, or bias can miss whether the product actually resolved the user's task, so teams should define scenario-specific answer criteria, include persona and wording variants, inspect individual failures, and use the benchmark as the baseline for prompt, model, retrieval, logic, and guardrail experiments.

Guardrail evaluation is also part of production AI evaluation. Safety layers should be tested at the same boundaries where attacks enter: direct prompts, external context, RAG chunks, MCP tool descriptions, memory, agent plans, and model responses. For latency-sensitive paths, a fine-tuned encoder discriminator can be evaluated as a binary classifier and compared against slower LLM-as-judge checks, while human approval flows should be tested for whether reviewers see the effective action and hidden parameters they are approving. Multi-agent organizations add another evaluation question: does the workflow actually force review, approval, and role-specific quality checks, or are those still best-effort prompt instructions?

RAG evaluation should treat the pipeline as a set of changeable components, not a solved top-k pattern. Parsing quality, chunk hierarchy, OCR, image descriptions, embedding models, hybrid lexical/vector scoring, metadata filters, and agentic search decisions can each change the answer. Agentic retrieval adds a trace-level evaluation requirement: teams should inspect which searches the model chose, not only whether the final answer sounded plausible.

Enterprise analytics agents add a metadata-specific evaluation layer. GenBI systems should be tested against messy production-like schemas and real user questions, with BI experts reviewing outputs before business users or executives depend on them. Metadata quality can be evaluated directly by running the same question set against better- and worse-documented data sources, then measuring whether the LLM finds the right context, report, or query path more reliably.

Contact-center voice evaluation should inspect each pipeline stage, not only the final summary. Speaker-channel preservation, STT accuracy under accents and poor audio, domain vocabulary, numeric normalization, grounded JSON extraction, hallucination checks, operator edits, and CRM-field mappings each create a failure point that can corrupt business records or analytics.

RL environments add an evaluation shape for interactive model behavior: the same environment can generate rollouts, compute deterministic or weighted rewards, and become the training loop. That makes the environment itself part of the eval artifact. Teams should control environment noise, inspect trajectories, check for hidden opponent or simulator bias, and try the trained model in the real task before trusting reward curves or benchmark scores.

Long-horizon coding demos should be evaluated as workflows, not as one impressive final answer. Poolside's Ada-to-Rust demo includes visible diffs, build output, generated test commands, Bash scripts, manual reruns, and feature-level checks; those surfaces are the evidence that a multi-step coding agent did useful work rather than only producing a convincing summary.

LLM program optimization adds another eval loop: define known inputs and outputs, write metrics that reflect the desired behavior, evaluate the base program, then let an optimizer propose improved prompts or modules. Metric breakdowns should be inspected after optimization because a gain can mean the metric is useful, the data is underspecified, or the program needs decomposition. Prompt-learning loops add a related requirement: labels and scalar scores are weaker than feedback that explains why an output failed and points to violated instructions, missing context, or rule-level noncompliance. The optimizer also inherits evaluator quality, so prompt-improvement systems should test their LLM judges, rule checkers, data splits, and loop budgets before trusting apparent prompt gains. PM-facing eval workflows should also avoid treating prompt playgrounds as isolated demos: traces and spans can carry real inputs, outputs, metadata, and agent actions into datasets and experiments, while LLM judges should emit categorical labels that are deterministically mapped to scores instead of raw numeric ratings.

Coding-agent prompt learning turns that evaluation loop into a system-prompt update path: baseline the agent on tasks such as SWE-bench Lite, run generated patches through tests, ask judges for explanatory diagnoses, synthesize rules from the diagnoses, and rerun the benchmark to check whether agent behavior actually improved without weight changes.

Anti-slop evaluation should be provenance-neutral. Human and AI outputs can both be low-quality, inauthentic, inaccurate, insecure, or unmaintainable, so the release question is whether the artifact meets the bar. Agent autonomy claims need the same discipline: unattended runtime is only meaningful when paired with tests, review findings, security evidence, maintainability judgment, and human ownership. For generated web apps, browser-level verification is a specific autonomy test because visible UI can hide missing handlers, mock data, or other painted-door failures that non-technical users will not systematically inspect.

## Key Concepts

- [Evaluate agent trajectories with backtests and smell metrics](../concepts/evaluate-agent-trajectories-with-backtests-and-smell-metrics.md) - flexible tool-loop agents need historical and trajectory-level checks.
- [Compare models by task, thinking budget, cost, and latency](../concepts/compare-models-by-task-thinking-budget-cost-and-latency.md) - side-by-side model comparisons help choose enough reasoning at acceptable speed and cost.
- [Do not use token volume as a developer productivity metric](../concepts/do-not-use-token-volume-as-a-developer-productivity-metric.md) - adoption dashboards should avoid rewarding visible token spend over task impact.
- [Measure AI developer productivity with field experiments, not benchmark extrapolation alone](../concepts/measure-ai-developer-productivity-with-field-experiments-not-benchmark-extrapolation-alone.md) - real experienced-developer work can diverge from lab capability curves.
- [Benchmark saturation pushes capability evals toward human time horizons](../concepts/benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md) - benchmark scores become less informative as task sets saturate.
- [Reliability thresholds determine whether coding agents save time](../concepts/reliability-thresholds-determine-whether-coding-agents-save-time.md) - productivity depends on total prompting, review, correction, and handoff cost.
- [Treat slop as a quality failure, not an AI provenance label](../concepts/treat-slop-as-a-quality-failure-not-an-ai-provenance-label.md) - quality gates should inspect the output rather than treating origin as the whole judgment.
- [Do not report agent autonomy without quality accountability](../concepts/do-not-report-agent-autonomy-without-quality-accountability.md) - long autonomous runs need quality evidence before they count as capability.
- [Autonomous browser verification finds painted-door failures](../concepts/autonomous-browser-verification-finds-painted-door-failures.md) - browser checks gather the technical feedback needed to validate generated web-app behavior.
- [Self-reported task duration is a weak productivity signal](../concepts/self-reported-task-duration-is-a-weak-productivity-signal.md) - speedup estimates should not rest on recalled elapsed time.
- [Separate watched and unwatched agent time horizons](../concepts/separate-watched-and-unwatched-agent-time-horizons.md) - autonomy evals should record whether close monitoring is part of the result.
- [Make agent work more trustworthy by making it verifiable](../concepts/make-agent-work-more-trustworthy-by-making-it-verifiable.md) - agent autonomy depends on whether tasks have direct checks, proxy checks, or safe constraints.
- [Evaluate whether models reject impossible or nonsensical premises](../concepts/evaluate-whether-models-reject-impossible-or-nonsensical-premises.md) - models should be judged on when they stop, clarify, or reject bad premises, not only on how well they solve valid tasks.
- [Track user dissatisfaction alongside pairwise model preference](../concepts/track-user-dissatisfaction-alongside-pairwise-model-preference.md) - "both bad" feedback exposes absolute failure rates that winner-only model comparisons hide.
- [Benchmark narrow slices separately from real expert work](../concepts/benchmark-narrow-slices-separately-from-real-expert-work.md) - benchmark gains should be checked against open-ended expert prompts and shifting user expectations.
- [Sandboxed code execution turns model reasoning into inspectable computation](../concepts/sandboxed-code-execution-turns-model-reasoning-into-inspectable-computation.md) - executable computation can make some model outputs easier to inspect and verify.
- [Mature eval platforms from spreadsheets into experiment systems](../concepts/mature-eval-platforms-from-spreadsheets-into-experiment-systems.md) - credible eval infrastructure should support comparison, collaboration, and scoring beyond documented output tables.
- [Evaluate BI agents with real metadata and expert feedback](../concepts/evaluate-bi-agents-with-real-metadata-and-expert-feedback.md) - analytics copilots need production-like data complexity, expert reviewers, and metadata A/B tests.
- [Connect production observability to offline eval loops](../concepts/connect-production-observability-to-offline-eval-loops.md) - real traces expose failure modes and should become replayable offline examples.
- [Agent traces require specialized eval infrastructure](../concepts/agent-traces-require-specialized-eval-infrastructure.md) - agent observability data can be too large, text-heavy, and semi-structured for naive trace storage.
- [Evaluate retrieval and MCP layers by task value, not only response availability](../concepts/evaluate-retrieval-and-mcp-layers-by-task-value.md) - retrieval quality is demonstrated by improved task outcomes, not by connector availability alone.
- [Demand-driven context pulls knowledge from failed work rather than pushing a complete knowledge base upfront](../concepts/demand-driven-context-pulls-knowledge-from-failed-work.md) - agent failures provide concrete test cases for missing context.
- [Feedback turns coding-agent loops into prompt and skill improvement cycles](../concepts/feedback-turns-coding-agent-loops-into-prompt-and-skill-improvement-cycles.md) - tests, review, and generated critiques should improve later loop runs.
- [Use independent validation contexts to reduce agent confirmation bias](../concepts/use-independent-validation-contexts-to-reduce-agent-confirmation-bias.md) - separate review agents can reduce self-affirming validation.
- [Use Reviewer and Approver Roles To Make Agent Workflows Reliable](../concepts/use-reviewer-and-approver-roles-to-make-agent-workflows-reliable.md) - review and approval roles make validation an enforceable workflow stage.
- [Choose plan-heavy or review-heavy agent workflows by task shape](../concepts/choose-plan-heavy-or-review-heavy-agent-workflows-by-task-shape.md) - task shape determines whether upfront specification or review iteration is the more efficient validation path.
- [Use research-plan-implement loops for coding agents](../concepts/use-research-plan-implement-loops-for-coding-agents.md) - research artifacts, plans, and verification commands make implementation-agent output easier to judge.
- [Translate structured requirements into property-based tests](../concepts/translate-structured-requirements-into-property-based-tests.md) - requirements should connect to executable invariants when possible.
- [Evaluate agent skills with task scenarios and comparative conditions](../concepts/evaluate-agent-skills-with-task-scenarios-and-comparative-conditions.md) - task scenarios and with/without comparisons reveal whether a skill changes behavior.
- [Evaluate workspace isolation with positive and negative filesystem scorers](../concepts/evaluate-workspace-isolation-with-positive-and-negative-filesystem-scorers.md) - workspace evals should check both intended isolated edits and forbidden primary-checkout edits.
- [Validate eval harnesses before trusting skill scores](../concepts/validate-eval-harnesses-before-trusting-skill-scores.md) - incorrect assertions or judges can misreport skill impact.
- [Use loss curves to debug local model training](../concepts/use-loss-curves-to-debug-local-model-training.md) - train and validation loss patterns separate non-learning, overfitting, and instability.
- [Build RL environments as software artifacts](../concepts/build-rl-environments-as-software-artifacts.md) - stateful environments can evaluate interactive tasks that static datasets do not capture.
- [Pair next-token prediction with reinforcement learning for long-horizon work](../concepts/pair-next-token-prediction-with-reinforcement-learning-for-long-horizon-work.md) - agentic capability claims should be checked against task completion and rollout behavior.
- [Use verifiable rewards for language-model RL](../concepts/use-verifiable-rewards-for-language-model-rl.md) - deterministic rewards make environment outcomes usable as eval and training signals.
- [Control environment noise for group-based RL](../concepts/control-environment-noise-for-group-based-rl.md) - grouped rollout evals need differences to come from model behavior rather than simulator randomness.
- [Inspect rollouts before trusting RL environment scores](../concepts/inspect-rollouts-before-trusting-rl-environment-scores.md) - strong environment scores can hide biased setup logic or memorized strategies.
- [Make local inference benchmarks reproducible artifacts](../concepts/make-local-inference-benchmarks-reproducible-artifacts.md) - local serving claims should be backed by repeatable run artifacts and hardware metrics.
- [Mitigate small-model doom loops during preference alignment and RL](../concepts/mitigate-small-model-doom-loops-during-preference-alignment-and-rl.md) - small reasoning models need output-loop checks and post-training reward signals beyond SFT.
- [Constrained decoding makes small-model tool calls production-usable](../concepts/constrained-decoding-makes-small-model-tool-calls-production-usable.md) - production evaluation of edge agents should account for runtime guardrails, not only raw model output.
- [Evaluate context changes with lint, task scenarios, and probabilistic budgets](../concepts/evaluate-context-changes-with-lint-task-scenarios-and-probabilistic-budgets.md) - context evals need structural checks, behavioral scenarios, and repeated-run thresholds.
- [Use agent logs and review feedback as context observability signals](../concepts/use-agent-logs-and-review-feedback-as-context-observability-signals.md) - production and review feedback should become test cases or context improvements.
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](../concepts/evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md) - voice evals need observability, transcript checks, audio judgments, simulations, and latency-aware guardrails.
- [Preserve speaker channels before voice-agent transcription](../concepts/preserve-speaker-channels-before-voice-agent-transcription.md) - evaluation should catch speaker-mixing failures before they become wrong summaries.
- [Extract contact-center intelligence as structured JSON](../concepts/extract-contact-center-intelligence-as-structured-json.md) - structured outputs make call-intent, entity, sentiment, and CRM-field checks more explicit than narrative summary review.
- [Verify AI call summaries before CRM sync](../concepts/verify-ai-call-summaries-before-crm-sync.md) - operator edits provide a production signal for extraction accuracy and schema-mapping failures.
- [Use golden data sets and mixed scoring functions for AI application confidence](../concepts/use-golden-data-sets-and-mixed-scoring-functions-for-ai-application-confidence.md) - curated edge cases plus deterministic and judge-model scores create a repeatable release gate.
- [Reverse-engineer AI app evals from user outcomes](../concepts/reverse-engineer-ai-app-evals-from-user-outcomes.md) - product and business outcomes should define the eval criteria before generic AI quality metrics.
- [Build AI app benchmarks before optimization](../concepts/build-ai-app-benchmarks-before-optimization.md) - early benchmarks let teams compare prompts, models, retrieval, logic, and guardrails while catching regressions.
- [Optimize LLM programs with metrics and teacher feedback](../concepts/optimize-llm-programs-with-metrics-and-teacher-feedback.md) - DSPy optimizers turn prompt improvement into a dataset-backed loop with metric and teacher-feedback signals.
- [Use explanatory feedback to optimize prompts](../concepts/use-explanatory-feedback-to-optimize-prompts.md) - prompt optimization should collect reasons for failures, not just labels.
- [System prompt learning updates agent rules from eval explanations](../concepts/system-prompt-learning-updates-agent-rules-from-eval-explanations.md) - coding-agent eval traces can update agent-visible rules.
- [Structure prompt-learning experiments with train/test splits and loop budgets](../concepts/structure-prompt-learning-experiments-with-train-test-splits-and-loop-budgets.md) - prompt-learning runs need explicit sample, split, evaluator, and iteration controls.
- [Evaluator quality is a dependency of prompt optimization](../concepts/evaluator-quality-is-a-dependency-of-prompt-optimization.md) - prompt optimizers amplify evaluator signal, so evaluator prompts and rules need validation.
- [Apply online scoring to production traces with cost-aware sampling](../concepts/apply-online-scoring-to-production-traces-with-cost-aware-sampling.md) - production monitoring should score live traces while sampling expensive model-based judges deliberately.
- [Replay production failures before promoting prompt fixes](../concepts/replay-production-failures-before-promoting-prompt-fixes.md) - production failures should become replayable regression cases before a prompt patch is trusted.
- [Realtime multimodal agents use stateful streams for audio, vision, and tools](../concepts/realtime-multimodal-agents-use-stateful-streams-for-audio-vision-and-tools.md) - realtime evals may need to inspect streamed audio, visual context, tool events, and latency together.
- [Ask agents after each run what blocked their success](../concepts/ask-agents-after-each-run-what-blocked-their-success.md) - post-run self-reporting can expose setup and context failures.
- [Agent software factories need runnable, contextual, and verifiable primitives](../concepts/agent-software-factories-need-runnable-contextual-and-verifiable-primitives.md) - agent readiness should be validated through runnable setup, tests, and user-flow checks.
- [Automation loops convert repeated review and triage into factory improvements](../concepts/automation-loops-convert-repeated-review-and-triage-into-factory-improvements.md) - review and triage outputs should feed evals, rules, or process changes.
- [Encode agent intent into server-side tools](../concepts/encode-agent-intent-into-server-side-tools.md) - tool descriptions should be evaluated in relation to competing tools, not only optimized individually.
- [Delegate implementations behind reviewed module interfaces](../concepts/delegate-implementations-behind-reviewed-module-interfaces.md) - module interfaces and tests let reviewers validate agent work without reading every internal line.
- [Limit agent change size by feedback speed](../concepts/limit-agent-change-size-by-feedback-speed.md) - agent diffs should be constrained by how quickly tests, type checks, and review can provide signal.
- [AI output speed can overwhelm review capacity](../concepts/ai-output-speed-can-overwhelm-review-capacity.md) - generated-code throughput should be evaluated against the team's ability to inspect and own the resulting changes.
- [Keep critical code inside human understanding and review capacity](../concepts/keep-critical-code-inside-human-understanding-and-review-capacity.md) - agent evals should account for whether humans can still read and own critical changes.
- [Agent-legible codebases reduce generated-code entropy](../concepts/agent-legible-codebases-reduce-generated-code-entropy.md) - structural constraints and lint rules make agent output easier to check and less likely to hide accidental behavior.
- [Use AI to scale codebase understanding against code slop](../concepts/use-ai-to-scale-codebase-understanding-against-code-slop.md) - code maps and related AI tools can improve the evidence available for review.
- [Use reviewer agents and lints to turn review lessons into guardrails](../concepts/use-reviewer-agents-and-lints-to-turn-review-lessons-into-guardrails.md) - recurring findings can become automatic reliability, security, and interface-quality checks.
- [AI-generated security reports need maintainer triage](../concepts/ai-generated-security-reports-need-maintainer-triage.md) - automated vulnerability reports and fixes still require human review before action.
- [Gate AI-generated open-source contributions through human-effort filters](../concepts/gate-ai-generated-open-source-contributions-through-human-effort-filters.md) - short human-authored issue requirements can filter low-signal generated submissions.
- [Use human judgment gates for high-risk agent code changes](../concepts/use-human-judgment-gates-for-high-risk-agent-code-changes.md) - high-impact changes need explicit review gates because local test success may not capture production risk.
- [Ratchet agent permissions down in high-consequence code environments](../concepts/ratchet-agent-permissions-down-in-high-consequence-code-environments.md) - high-risk coding-agent evaluation should include permission scope and visible verification surfaces.
- [Use deep modules to make agent work testable](../concepts/use-deep-modules-to-make-agent-work-testable.md) - module interface tests can validate agent-written internals without full-line-by-line review.
- [Quality Wednesdays train engineers to notice small regressions](../concepts/quality-wednesdays-train-engineers-to-notice-small-regressions.md) - quality rituals create human detection signals for polish issues that metrics may miss.
- [AI agents still need human taste for interaction quality](../concepts/ai-agents-still-need-human-taste-for-interaction-quality.md) - UI eval needs human judgment when generated interactions are functional but feel wrong.
- [Calibrate LLM judges like binary classifiers](../concepts/calibrate-llm-judges-like-binary-classifiers.md) - judge prompts need dev/test validation before they gate workflow quality.
- [Label LLM Judge Outputs Before Mapping Them to Scores](../concepts/label-llm-judge-outputs-before-mapping-them-to-scores.md) - categorical judge labels are more reliable than asking the model to invent a raw numeric rating.
- [Split LLM Judges Into Narrow Binary Metrics](../concepts/split-llm-judges-into-narrow-binary-metrics.md) - specific pass/fail metrics are easier to calibrate than one broad success judge.
- [Optimize Judge Prompts With Diagnostic Feedback](../concepts/optimize-judge-prompts-with-diagnostic-feedback.md) - GEPA-style prompt optimization needs verdicts, ground truth, reasoning, and domain priors.
- [Fine-tuned encoder discriminators make low-latency guardrails practical](../concepts/fine-tuned-encoder-discriminators-make-low-latency-guardrails-practical.md) - safety classifiers can provide inline checks when LLM judges are too slow.
- [LLM guardrails need checkpoints at every untrusted boundary](../concepts/llm-guardrails-need-checkpoints-at-every-untrusted-boundary.md) - guardrail evals should cover all context and action surfaces that can carry attack signals.
- [Human approval can hide tool-description and parameter risk](../concepts/human-approval-can-hide-tool-description-and-parameter-risk.md) - approval UX needs evals for whether it exposes enough detail to support real review.
- [Domain Gemma variants package specialized policy and task behavior](../concepts/domain-gemma-variants-package-specialized-policy-and-task-behavior.md) - safety and domain variants still need validation against the policies or specialist tasks they claim to support.
- [Neural weather models can target operational forecast variables directly](../concepts/neural-weather-models-can-target-operational-forecast-variables-directly.md) - domain models should be evaluated against operational targets such as forecast lead time, tail risk, and phenomenon-specific prediction.
- [RAG stacks need modular baselines instead of one fixed recipe](../concepts/rag-stacks-need-modular-baselines-instead-of-one-fixed-recipe.md) - RAG quality depends on tuning shared components to the corpus and user task.
- [Agentic retrieval lets models plan search steps](../concepts/agentic-retrieval-lets-models-plan-search-steps.md) - evals should inspect model-selected search actions and final answers.

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
- Which field-study designs can detect AI coding-tool speedups without washing out effects through task allocation, repository familiarity, or review overhead?
- Which reliability threshold lets expert maintainers accept coding-agent output without spending more time verifying and repairing it than they save?
- How should capability evals combine time-horizon curves, mergeability checks, and real-work RCTs without over-weighting any one source of evidence?
- Which observed timing traces are strong enough to replace self-reported task duration in developer productivity studies?
- Which product-quality regressions can be detected mechanically, and which still require trained human taste?
- Which LLM judge labels are safe to automate, and which still require domain-expert review before calibration?
- Which domain-specific model variants are reliable enough to replace prompting a general model, and which still need expert review or lab validation?
- Which generated-world checks best measure memory, consistency, and controllability under long interactive sessions?
- Which reviewer-agent findings are stable enough to gate CI, and which should remain advisory comments?
- How much human annotation quality and distribution coverage is enough before judge-prompt optimization becomes trustworthy?
- Which local inference metrics beyond time to first token and throughput best predict real user-perceived responsiveness?
- How should retrieval evals isolate whether failures came from parsing, chunking, embedding choice, hybrid scoring, filters, or agent search planning?
- Which metadata fields most improve BI-agent accuracy, and which only make catalog documentation look better without changing task outcomes?
- Which RL environment scores should require manual rollout review before they are allowed to drive training decisions?
- How should contact-center systems measure whether operator edits are correcting model errors, STT errors, schema mapping errors, or policy preferences?
- Which user-outcome metrics are strong enough to replace generic AI quality scores as release gates for each product workflow?
- Which DSPy optimization metrics are stable enough to drive prompt changes automatically, and which should only surface diagnostics for human review?
- Which explanatory feedback fields are stable enough to automate prompt rewriting, and which still require subject-matter-expert review?

## Sources

- [How Claude Code Works - Jared Zoneraich, PromptLayer](../sources/20251226_RFKCzGlAU6Q.md)
- [Why Agent Hype can fall short of reality - Joel Becker, METR](../sources/20251224_RhfqQKe22ZA.md)
- [Agentic Engineering: Working With AI, Not Just Using It - Brendan O'Leary](../sources/20260407_BEKc4P87XKo.md)
- [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality - Al Harris, Amazon Kiro](../sources/20260109_HY_JyxAZsiE.md)
- [How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR](../sources/20260119_k1t2xyWMUdY.md)
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
- [Gemma, DeepMind's Family of Open Models - Omar Sanseviero, Google DeepMind](../sources/20260420__gVFUEdhCyI.md)
- [The Friction is Your Judgment - Armin Ronacher & Cristina Poncela Cubeiro, Earendil](../sources/20260418__Zcw_sVF6hU.md)
- [How Google DeepMind is researching the next Frontier of AI for Gemini - Raia Hadsell, VP of Research](../sources/20260418_zZsTVBXcbow.md)
- [Harness Engineering: How to Build Software When Humans Steer, Agents Execute - Ryan Lopopolo, OpenAI](../sources/20260417_am_oeAoUhew.md)
- [State of the Claw - Peter Steinberger](../sources/20260417_zgNvts_2TUE.md)
- [Building pi in a World of Slop - Mario Zechner](../sources/20260416_RjfbvDXpFls.md)
- [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs - Diego Carpentero](../sources/20260416_YZHPEkfy2kc.md)
- [Paperclip: Open Source Human Control Plane for AI Labor - Dotta Bippa](../sources/20260415_h403btjldDQ.md)
- [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA - Mahmoud Mabrouk, Agenta AI](../sources/20260410_X4dEHRzBLmc.md)
- [Running LLMs locally: Practical LLM Performance on DGX Spark - Mozhgan Kabiri chimeh, NVIDIA](../sources/20260410_c5-kx2bwoCk.md)
- [OpenRAG: An open-source stack for RAG - Phil Nash](../sources/20260408_4TxOBhDRRCM.md)
- [Let LLMs Wander: Engineering RL Environments - Stefano Fiorucci](../sources/20260408_71V3fTaUp2Q.md)
- [Contact Center Voice AI: Low-Latency Intelligence Extraction from Messy Audio Streams - Dippu Singh](../sources/20260408_IEF842ZEU5A.md)
- [Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear](../sources/20250803_-T6uZYYzkWw.md)
- [DSPy: The End of Prompt Engineering - Kevin Madura, AlixPartners](../sources/20260108_-cKUW6n8hBU.md)
- [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](../sources/20260106_SbcQYbrvAfI.md)
- [The Unreasonable Effectiveness of Prompt Learning - Aparna Dhinakaran, Arize](../sources/20251223_pP_dSNz_EdQ.md)
- [AGI: The Path Forward - Jason Warner & Eiso Kant, Poolside](../sources/20251227_OGCG_QkCcZo.md)
- [Shipping AI That Works: An Evaluation Framework for PMs - Aman Khan, Arize](../sources/20251226_2HNSG990Ew8.md)
- [Small Bets, Big Impact Building GenBI at a Fortune 100 - Asaf Bord, Northwestern Mutual](../sources/20251223_LU9KgcZDRfY.md)
- [No More Slop - swyx](../sources/20251222_IoiHI7p12Ao.md)
- [The 3 Pillars of Autonomy - Michele Catasta, Replit](../sources/20251222_MLhAA9yguwM.md)
