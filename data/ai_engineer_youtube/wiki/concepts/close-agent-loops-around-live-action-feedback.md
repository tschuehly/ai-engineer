# Close agent loops around live action feedback

Summary: Agent actions should expose observable results, completion state, and interruption controls so the agent can recalibrate after acting. Turn-based tool calls are easy to reason about, but they can become open-loop when the external world changes before the agent can observe or respond.

Use when:
- Designing shell, browser, desktop, or long-running-process tools for agents.
- Evaluating whether an agent can recover from action failures instead of only planning correctly.

Details:
- In robotics, closed-loop control means taking an action, measuring what actually happened, and recalibrating because actuators are imperfect; Hu applies the same principle to digital agents. (03:08-03:42)
- A Bash command that starts an open-ended process is open-loop if the agent cannot observe output in real time, know whether the command completed, or exit early. (03:42-04:06)
- Conversation turns and full tool-response waits make agent behavior easier to inspect, but they reduce realtime response to pop-ups and long-running processes. (04:57-05:46)
- Agents move from prediction into action: they predict, act, deal with consequences, and then re-evaluate earlier decisions in a messy world. (09:35-09:59)

Related topics:
- [Agents](../topics/agents.md)
- [Coding Agents](../topics/coding-agents.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Interleave reasoning and tool calls for long-horizon agents](interleave-reasoning-and-tool-calls-for-long-horizon-agents.md)
- [Control long-running workflow agents through run lifecycle operations](control-long-running-workflow-agents-through-run-lifecycle-operations.md)

Sources:
- [Agents are Robots Too: What Self-Driving Taught Me About Building Agents - Jesse Hu, Abundant](../sources/20251124_qqXdLf3wy1E.md), 03:08-05:46
