# Calibrate Voice Eval Realism To The Behavior Under Test

Summary: Voice-agent simulations do not always need hyperrealistic audio. Teams should control only the variables relevant to the metric: text may be enough for workflow and tool-call iteration, while accents, background noise, latency, interruptions, and audio quality require voice or end-to-end tests.

Use when:
- Designing a voice-agent eval suite with limited time or compute budget.
- Choosing between text-only, simple voice, and hyperrealistic audio simulations.

Details:
- The necessary realism depends on the behavior under test; like an experiment, the eval should control variables and measure the target behavior, 09:18-09:40.
- Hyperrealistic simulation is not automatically better; useful simulation depends on how well teams can control simulated components and provide the inputs needed for the decision, 10:04-10:29.
- Workflow, tool-call, and instruction-following checks can often run cheaply as text during iteration, with end-to-end voice tests reserved for full-path validation, 10:29-10:46.
- Interruption, latency, and instructed-pause behavior need voice-to-voice tests, but basic synthetic voices may be sufficient unless the target issue involves accent, background noise, or audio quality, 10:47-11:15.
- A practical strategy layers public benchmarks, domain-specific data, task/module evals, and production-shaped end-to-end evals instead of forcing every test through the full stack, 15:16-16:01.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Design voice agents around voice-to-voice latency budgets](design-voice-agents-around-voice-to-voice-latency-budgets.md)

Sources:
- [From Self-driving to Autonomous Voice Agents - Brooke Hopkins, Coval](../sources/20250731_kDczF4wBh8s.md), 09:18-16:01
