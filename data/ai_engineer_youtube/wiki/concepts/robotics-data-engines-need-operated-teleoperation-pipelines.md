# Robotics Data Engines Need Operated Teleoperation Pipelines

Summary: Frontier robot policies need an operated data engine, not just a static dataset. Teams must select task families, collect successful teleoperated episodes, track collection metrics, annotate and filter the data, and feed it back into model training.

Use when:
- Designing robotics data collection for dexterous vision-language-action models.
- Explaining why robot model progress depends on operations, annotation, and quality control as much as model architecture.

Details:
- Physical Intelligence frames the robotics data source as an open industry problem because there is no web-scale equivalent of successful robot action traces. (04:13-04:30)
- Their data engine starts from expanding task sets such as clothes folding and grocery bagging, then has human operators teleoperate robots through a custom runtime and leader-arm system to collect intricate successful demonstrations. (05:11-06:35)
- Operationalizing the pipeline is described as more than half the work: getting the right data, making it high quality, scheduling collection sessions, tracking metrics, annotating data in the cloud, filtering by annotations, and using it for training. (05:39-07:17)
- PI reports scaling from the roughly 3,800-hour public Open X-Embodiment dataset baseline to about 10,000 hours of successful episodes across tens of environments and hundreds of tasks after six months of this pipeline. (07:40-08:10)

Related topics:
- [Robotics](../topics/robotics.md)
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data](robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md)
- [Physical AI Has a Three-Stage Compute Lifecycle](physical-ai-has-a-three-stage-compute-lifecycle.md)

Sources:
- [Robotics: why now? - Quan Vuong and Jost Tobias Springberg, Physical Intelligence](../sources/20250726_cGLa8DsOYdk.md), 04:13-08:10
