# Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data

Summary: Robotics foundation models cannot rely on internet-scale action traces the way language models rely on web text. A practical robotics data strategy mixes scarce teleoperated robot trajectories, broad but indirect human videos, synthetic simulation, and methods that multiply high-quality trajectories.

Use when:
- Designing data collection for robot policies or vision-language-action models.
- Explaining why robotics model training needs simulation and teleoperation pipelines in addition to web video.

Details:
- The talk says the desired robot-action data does not exist at internet scale because there is no large scrapeable corpus of robots successfully doing tasks. (04:47-05:15)
- High-quality real-world robot data often comes from human teleoperation, for example using headsets and gloves to operate a real robot through successful tasks; this gives ground-truth trajectories but is small and expensive. (05:17-05:58)
- Internet video supplies abundant human task-solving footage, but it is unstructured and not necessarily robot-relevant, so it is useful only as part of a broader data strategy. (05:58-06:23)
- Synthetic simulation data can in principle be generated repeatedly, but high-quality simulation environments are labor-intensive and require specialized skill. (06:25-06:49)
- GR00T's data strategy also includes multiplying collected human teleoperation trajectories through video/world foundation models such as DreamGen, while combining simulation and real-world data remains an active research problem. (06:56-07:35)

Related topics:
- [Robotics](../topics/robotics.md)
- [Models](../topics/models.md)

Related concepts:
- [Physical AI Has a Three-Stage Compute Lifecycle](physical-ai-has-a-three-stage-compute-lifecycle.md)
- [Ground agent simulation and evaluation in production logs](ground-agent-simulation-and-evaluation-in-production-logs.md)
- [Interactive world models need memory, control, and live prompting](interactive-world-models-need-memory-control-and-live-prompting.md)

Sources:
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md), 04:47-07:35
