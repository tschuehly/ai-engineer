# Robotics Policy Failures Can Originate Below The Model

Summary: A robot that stutters, skips, or ignores commands may not have a bad policy; the fault can live in the communication, threading, logging, scheduling, or hardware path around the policy. Diagnose physical AI systems as end-to-end control systems before attributing behavior to model output.

Use when:
- Debugging robotics or embodied-agent behavior where the actuator output does not match the intended policy command.
- Separating model-quality failures from runtime, bus, scheduler, or hardware integration failures.

Details:
- Garg frames the core robotics debugging question as policy versus software system: sensor data must reach the policy, and policy outputs must reach actuators before behavior can be judged as a policy failure. (00:24-01:21)
- The example robot includes actuators, CPU, accelerator, sensors, and a CAN communication path; the communication protocol can shape downstream design decisions. (01:23-01:56)
- Actuator stutter and catch-up behavior can look like a bad policy, but delayed TX messages, stale RX data, and thread desynchronization can produce the same outward symptoms. (04:32-08:36)
- The final recap treats pipeline design, synchronization, logging, and priority inversion as basic ingredients of high-performance robotic systems, not incidental implementation details. (12:03-12:32)

Related topics:
- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)
- [Close agent loops around live action feedback](close-agent-loops-around-live-action-feedback.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](../sources/20250825_bCGbuyv8PMk.md), 00:24-12:32
