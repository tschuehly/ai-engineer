# Simulate Voice Agents With Probabilistic Conversation Evals

Summary: Conversational-agent evals should test distributions of multi-turn outcomes, not only one input against one expected output. Re-running simulated conversations helps estimate failure probability for flexible agents whose responses vary by user behavior and model nondeterminism.

Use when:
- Evaluating an autonomous voice agent that must handle many customer paths.
- Deciding whether a single failed simulated conversation represents a serious release blocker.

Details:
- Hopkins frames deterministic IVR-like control and unconstrained autonomy as a false choice: voice agents need autonomy, but production trust requires systematic evaluation, 01:51-02:32.
- Self-driving-style simulation replaces brittle hand-authored scenario expectations with large-scale checks over event frequency and agent performance across many runs, 03:04-04:01.
- In conversations, each turn changes the next state; simulation should cover possible user responses rather than only one fixed path, 04:16-04:56.
- LLM nondeterminism can be useful for coverage because repeated simulations expose possible user or agent responses and let teams estimate success probability, 05:10-05:32.
- A failed scenario should be re-simulated many times to distinguish rare noise from a consistent failure rate such as 50/100 or 99/100, 11:26-12:18.

Related topics:
- [Voice Agents](../topics/voice-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [From Self-driving to Autonomous Voice Agents - Brooke Hopkins, Coval](../sources/20250731_kDczF4wBh8s.md), 01:51-12:18
