# Product-Research Flywheels Expose Model and Harness Gaps

Summary: When model researchers and product engineers use the same agent product internally, real workflows can reveal gaps that offline evals miss. The feedback may point to model training, data distribution, tool design, harness plumbing, latency, artifact handling, or instruction-following problems.

Use when:
- Building AI products close to a model research team.
- Deciding how dogfooding, evals, and product telemetry should feed model and harness improvements.

Details:
- Antigravity was built with early access to Gemini 3 and collaboration with research teams to identify strengths to exploit and gaps to fix for the desired product experience. 06:39-07:05
- Hou argues that product paradigms follow model capability changes, including autocomplete, chat, agents, and newer agent-first surfaces enabled by reasoning, tool use, long-running work, and multimodality. 06:11-08:16
- Internal use by Google engineers and DeepMind researchers exposes the actual experience of using the model, agent manager, and artifacts to the people improving the model. 20:31-21:34
- Product use can show issues that ordinary evals may not capture, such as slow infrastructure, computer-use failure modes, image generation behavior, instruction-following gaps, or a mismatch between model capability and harness tools. 21:34-23:03
- The computer-use example shows bidirectional debugging: product teams can ask whether a capability gap comes from model data distribution while research teams can point out broken or poorly shaped harness tools. 22:27-23:03
- The artifact pattern itself required product/research work because the model initially was not trained around this new review concept; improving it involved creating a hill for the model to climb. 23:04-23:32

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Build AI product iteration tools into the product context](build-ai-product-iteration-tools-into-the-product-context.md)
- [Turn real coding sessions into RL environments](turn-real-coding-sessions-into-rl-environments.md)
- [Use agent readiness flywheels to improve the development environment](use-agent-readiness-flywheels-to-improve-the-development-environment.md)

Sources:
- [Defying Gravity - Kevin Hou, Google DeepMind](../sources/20251202_HN-F-OQe6j0.md), 06:11-08:16, 20:31-23:32
