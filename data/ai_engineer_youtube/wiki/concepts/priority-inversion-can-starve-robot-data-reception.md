# Priority Inversion Can Starve Robot Data Reception

Summary: Raising control-loop process priority can backfire when it starves the kernel or lower-level receiver path that supplies the data the loop needs. Realtime robotic systems need priority design across the whole pipeline, not just maximum priority for user-space policy work.

Use when:
- Tuning Linux, RTOS, or embedded scheduling for robotic data reception and control loops.
- Investigating packet drops or seconds-scale data blackouts after priority changes.

Details:
- In Linux-based robotics, data reception passes through interrupt and kernel handling before it reaches the user process; if user processes block kernel work, the data path itself is starved. (11:10-11:38)
- Garg describes this as priority inversion in action: the system tries to receive data while blocking the component that provides it, which can cause long dropouts. (11:38-11:44)
- The mitigation is to understand the pipeline and set priorities for the whole reception, policy, and transmission path rather than blindly boosting every robotics process. (11:44-12:02)

Related topics:
- [Infrastructure](../topics/infrastructure.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Pipeline realtime control loops with synchronization budgets](pipeline-realtime-control-loops-with-synchronization-budgets.md)
- [Robotics policy failures can originate below the model](robotics-policy-failures-can-originate-below-the-model.md)

Sources:
- [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](../sources/20250825_bCGbuyv8PMk.md), 11:10-12:02
