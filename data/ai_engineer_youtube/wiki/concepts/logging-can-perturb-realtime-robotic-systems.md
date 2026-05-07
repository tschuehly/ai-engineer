# Logging Can Perturb Realtime Robotic Systems

Summary: Diagnostic logging in realtime robotics is part of the control system's timing behavior. Logs that flush to disk or slow peripherals can block the loop, create blackout periods, or cascade packet loss while trying to report the original failure.

Use when:
- Adding observability to realtime, embedded, edge, or robotic control software.
- Explaining why debug instrumentation must be budgeted and isolated from critical control paths.

Details:
- Garg warns that ordinary logging can become costly once buffered logs flush to disk; a Raspberry Pi with an SD card froze for roughly 30 ms when the main control loop wrote logs. (09:25-09:55)
- Moving logging to another CPU is one mitigation when the control loop has hard realtime deadlines and logging cannot block the policy/communication path. (09:58-10:13)
- Microcontrollers may log through UART or another peripheral rather than a filesystem, but that peripheral can still take milliseconds depending on log volume. (10:17-10:33)
- A dropped-packet log can become self-amplifying: logging the drop takes enough time to drop the next packet, causing another log and eventually a CAN-bus blackout. (10:35-11:08)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Expose observability as agent-readable feedback](expose-observability-as-agent-readable-feedback.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)

Sources:
- [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](../sources/20250825_bCGbuyv8PMk.md), 09:25-11:08
