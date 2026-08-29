# Ground agent simulation and evaluation in production logs

Summary: Agent improvement loops should feed production logs and categorized failures back into simulation and evaluation. Aggregate benchmark scores are useful but too coarse to guide hill-climbing when action consequences, state, and counterfactual paths matter.

Use when:
- Building eval or training infrastructure for agentic workflows with side effects.
- Turning production traces into simulation, regression, or RL environments.

Details:
- Hu argues that stateful agents affect both online operation and offline simulation/evaluation because the system must account for the current world, active context, persistent files, and what the agent may interact with. (07:30-08:41)
- Imitation learning and SFT can fall out of distribution when an agent reaches states not represented in demonstrations, such as browser pop-ups; the resulting errors cascade because actions change later state. (08:43-09:35)
- Simulation helps represent messy starting states and play out counterfactual action paths rather than only evaluating one observed trajectory. (10:03-10:24)
- Production logs should ground simulation: after deployment, real-world logs can feed the simulation engine and reveal more than benchmark numbers when broken down by failure category, environment, or error mode. (14:32-15:23)
- Feizi (RELAI) sharpens *why* one log is not enough: a production log plus feedback is a single observation of what happened, not something testable, so continual learning must "infer a distribution from one observation" — lift the log into a replayable learning environment by inferring how tools should behave (real vs mock, and what data feeds the mocking), synthesizing users from the interaction, and inferring the evaluators that define success. The output is executable: you can run different agent candidates against the same pattern and fix issues verifiably. "Production logs are not learning environments." (Feizi 04:14-06:15, 21:52-22:04)
- **The same log read for demand rather than for failure.** Izmit's team classifies its entire question log with LLMs — 1.2 million questions, ~40,000 a week — into a topic taxonomy of categories, subcategories, and example questions, and uses it to see "what people are asking and we are not able to answer" in real time. That is a roadmap instrument, not an eval one: failure-mode breakdown tells you which of your capabilities are broken, while topic distribution tells you which capabilities you do not have. The two readings need the same pipeline and answer different questions, and the second one degrades gracefully — it works from the question alone, without needing the trajectory. Cost at scale is named as the hard part and no figures are given. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 14:11-15:20)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat environments as eval, data, and training substrates](treat-environments-as-eval-data-and-training-substrates.md)
- [Turn real coding sessions into RL environments](turn-real-coding-sessions-into-rl-environments.md)
- [Connect production observability to offline eval loops](connect-production-observability-to-offline-eval-loops.md)
- [Verifiable Continual Learning: Prove Each Agent Fix Helps and Breaks Nothing](verifiable-continual-learning-prove-each-fix-helps-and-breaks-nothing.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)

Sources:
- [Agents are Robots Too: What Self-Driving Taught Me About Building Agents - Jesse Hu, Abundant](../sources/20251124_qqXdLf3wy1E.md), 07:30-15:23
- [Continual Learning for AI Agents: From Failures to Durable Improvements - Soheil Feizi, RELAI](../sources/20260705_2IxD9OB3XuQ.md), 04:14-06:15, 21:52-22:04
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 14:11-15:20
