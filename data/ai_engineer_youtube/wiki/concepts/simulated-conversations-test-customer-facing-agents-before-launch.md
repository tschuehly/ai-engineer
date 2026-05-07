# Simulated Conversations Test Customer-Facing Agents Before Launch

Summary: Customer-facing agents need simulation-based evaluation because one input/output check cannot validate nondeterministic conversational behavior. Simulated personas, accounts, devices, and troubleshooting states can stress the agent before launch, then live handoffs and mistakes feed a coaching loop.

Use when:
- Designing pre-launch tests for support, care, or voice agents.
- Building a closed-loop improvement process from production conversations.

Details:
- Bavor frames the agent development lifecycle around nondeterministic software and says a single input and expected output is insufficient for testing a company agent. (11:55-12:23)
- Sierra built a user-simulation testing harness with different personas, simulated accounts, and simulated devices or troubleshooting states. (12:23-12:36)
- The harness can run tens or hundreds of thousands of conversations before the agent goes live, revealing missing knowledge and corner cases. (13:21-13:40)
- After launch, tools expose where the agent recognizes it is beyond its ability and hands off to a person; those cases can feed a closed-loop coaching process where the agent learns from past mistakes. (13:42-14:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Contact-center voice evaluation should inspect each pipeline stage](preserve-speaker-channels-before-voice-agent-transcription.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [Rise of the AI Architect - Clay Bavor, Cofounder, Sierra w/ Alessio Fanelli](../sources/20250724_C3geUfBR2js.md), 11:55-14:08
