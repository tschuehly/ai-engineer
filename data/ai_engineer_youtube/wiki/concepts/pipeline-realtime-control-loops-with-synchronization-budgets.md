# Pipeline Realtime Control Loops With Synchronization Budgets

Summary: Realtime robotic control loops need explicit budgets for communication delay, policy runtime, and RX/TX synchronization. Pipelining can reduce cycle time, but it introduces stale-data and queued-command failure modes if thread timing drifts.

Use when:
- Designing control-loop software around sensors, accelerators, bus communication, and actuators.
- Interpreting cycle-time jitter after adding multithreading or pipelining to an embodied AI system.

Details:
- In the toy CAN setup, ten 100-bit messages on a 1 Mbit/s bus consume about 1 ms, so bus transmission time can be on the same order as a 2 ms policy loop. (02:42-03:12)
- One response is to accept the delay; the high-performance response is to separate communication and policy work across threads and stagger RX/TX with policy execution. (03:14-04:28)
- If policy execution runs long or TX/RX threads desynchronize, a missed send can be queued and then emitted with the next command, making the actuator receive two commands at nearly the same time. (06:57-07:41)
- If the RX side is delayed, the policy may compute from stale data and then skip ahead on the next iteration, producing motor jitter that resembles a policy issue. (08:01-08:36)
- Kernel synchronization primitives such as condition variables and semaphores can align the pipeline; when unavailable, padding can provide enough timing cushion to keep RX data matched to the intended policy iteration. (08:38-09:18)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](../sources/20250825_bCGbuyv8PMk.md), 02:42-09:18
