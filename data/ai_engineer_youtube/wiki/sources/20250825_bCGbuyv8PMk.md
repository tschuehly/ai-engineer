# Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

Source: [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](https://www.youtube.com/watch?v=bCGbuyv8PMk)
Uploaded: 2025-08-25
Transcript: `raw/20250825_bCGbuyv8PMk/bCGbuyv8PMk.en-orig.vtt`

## Summary

Rishabh Garg explains how high-performance robotics failures that look like bad control policy behavior can come from the software and hardware path between policy output and actuators. The talk uses a CAN-bus toy robot to show how communication bandwidth, pipelining, thread synchronization, logging, and Linux scheduling priorities can create jitter, stale commands, packet drops, and actuator stutter.

## Extracted Concepts

- [Robotics policy failures can originate below the model](../concepts/robotics-policy-failures-can-originate-below-the-model.md) - this source shows why actuator behavior should be debugged across policy, software, communication, and hardware layers.
- [Pipeline realtime control loops with synchronization budgets](../concepts/pipeline-realtime-control-loops-with-synchronization-budgets.md) - this source explains how CAN-bus transmission time, RX/TX pipelining, and synchronization choices affect control-loop cadence.
- [Logging can perturb realtime robotic systems](../concepts/logging-can-perturb-realtime-robotic-systems.md) - this source shows how diagnostic logging can block control loops or trigger cascading packet drops.
- [Priority inversion can starve robot data reception](../concepts/priority-inversion-can-starve-robot-data-reception.md) - this source describes how over-prioritized user processes can block kernel reception paths.

## Topic Links

- [Agents](../topics/agents.md)
- [Evaluation](../topics/evaluation.md)
- [Infrastructure](../topics/infrastructure.md)

## Notes

- The talk frames the main diagnostic question as whether unexpected robot behavior comes from the policy or the software system that moves sensor data to the policy and policy outputs to actuators. (00:24-01:21)
- A CAN-bus example shows that ten 100-bit messages on a 1 Mbit/s bus can consume roughly 1 ms, enough to matter inside a 2 ms control loop. (02:42-03:12)
- Multithreading and pipelining can recover loop cadence, but delayed policy execution or RX/TX desynchronization can queue multiple commands together or feed stale data into the next policy step. (03:21-08:36)
- External CAN transceivers and `candump` provide timestamped bus observations; cycle-time plots make message jitter visible as late messages followed by near-zero intervals. (04:49-06:52)
- Logging can freeze a Raspberry Pi control loop for tens of milliseconds when logs flush to disk, and microcontroller logging can create cascades where logging a dropped packet causes the next packet drop. (09:25-11:08)
- Raising user-process priority too far can block Linux kernel work needed to receive data, creating priority inversion and seconds-scale dropout. (11:10-12:02)
