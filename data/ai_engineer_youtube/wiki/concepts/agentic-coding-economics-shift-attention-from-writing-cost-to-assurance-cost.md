# Agentic coding economics shift attention from writing cost to assurance cost

Summary: When agentic coding makes implementation tokens cheap, the dominant question becomes whether the generated code can be assured cheaply enough to beat ordinary engineering. Adoption is constrained less by raw generation cost than by defect correction, verification, and trust.

Use when:
- Evaluating AI coding ROI beyond token or line-of-code cost.
- Arguing for investment in tests, specifications, formal checks, safety cases, and review automation around generated code.

Details:
- In a sample Codex run, output-token cost was described as only about 15% of total model cost; repeated input, cached input, and reasoning tokens dominated the bill while tests and iterations ran. 30:17-31:13
- The talk compares historical high-assurance software cost with ordinary software and argues that agentic coding can make code generation far cheaper than both, leaving assurance as the practical bottleneck. 31:16-33:29
- The claimed adoption threshold is qualitative: developers avoid agents when fixing generated bugs costs more than writing directly, but adoption can accelerate when agentic coding routinely produces fewer defects than human-written code. 34:12-35:02
- The source cautions implicitly against measuring only generated output volume; useful economics must include verification and correction cost. 30:43-31:13

- An observational datapoint on the same asymmetry, with a time axis this page lacked: a Carnegie Mellon study sorting GitHub projects by whether an AI tool wrote the code found "a temporary spike in productivity… it lasted about 3 months and then it went back down," alongside "a persistent increase in static analysis warnings and code complexity" that "persisted well into the future" ([Chatterjee](../sources/20260809_03l29gJXpCE.md), 01:45-02:34). If it holds, the writing-cost saving is the transient term and the assurance cost is the durable one — which is the economics this page argues from, observed rather than modeled. Carry the caveats with it: the study is cited with no link, sample size, or productivity definition; the causal link between the two findings is the speaker's inference ("the reason for that, we think"); and the instrument was the citing vendor's own analyzer. See [Verification Debt Outlives the Productivity Spike](verification-debt-outlives-the-productivity-spike.md).

Related topics:
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Reliability thresholds determine whether coding agents save time](reliability-thresholds-determine-whether-coding-agents-save-time.md)
- [Measure AI ROI with primary output and guardrails](measure-ai-roi-with-primary-output-and-guardrails.md)
- [AI output speed can overwhelm review capacity](ai-output-speed-can-overwhelm-review-capacity.md)
- [Verification Debt Outlives the Productivity Spike](verification-debt-outlives-the-productivity-spike.md)

Sources:
- [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](../sources/20251124_qLqttdO33UM.md), 30:17-35:02
- [Guide, Verify, Solve — Anirban Chatterjee, Sonar](../sources/20260809_03l29gJXpCE.md), 01:45-02:34

