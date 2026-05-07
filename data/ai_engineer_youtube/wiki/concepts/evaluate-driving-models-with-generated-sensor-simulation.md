# Evaluate Driving Models With Generated Sensor Simulation

Summary: End-to-end driving planners need closed-loop simulation in addition to open-loop log replay. Waymo's Drive&Gen-style research uses generated sensor video to place a planner in controllable virtual conditions such as rain and time of day.

Use when:
- Evaluating an action model whose decisions affect future observations.
- Testing vision-based planners under rare or hard-to-collect environmental conditions.

Details:
- The talk distinguishes open-loop evaluation, which replays video and checks model quality, from simulation and real-world testing; it says open-loop replay is usually less faithful than simulation for this purpose. (14:05-15:01)
- Sensor simulation creates a virtual world where a model can drive, while real-world testing means deploying the model. (14:39-14:53)
- The research uses generated videos as sensor simulation for end-to-end driving evaluation, then evaluates the planner quality inside those generated conditions. (15:04-15:45)
- Generated sensor conditions can vary weather and time of day; the presented results aligned with intuition that rain and nighttime make a camera-only planner perform worse than clearer daytime conditions. (15:45-16:42)

Related topics:
- [Robotics](../topics/robotics.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Evaluate generative media with perceptual metrics](evaluate-generative-media-with-perceptual-metrics.md)

Sources:
- [Waymo's EMMA: Teaching Cars to Think - Jyh Jing Hwang, Waymo](../sources/20250726_iS9YFW28XyM.md), 14:05-16:42
