# Physical AI Has a Three-Stage Compute Lifecycle

Summary: Physical AI systems need a lifecycle that covers data generation, model training, and deployment on the robot or edge device. Each stage has different compute characteristics, so robotics foundation-model work should be planned as a stack rather than as one model artifact.

Use when:
- Planning the infrastructure needed to build or deploy robotics foundation models.
- Separating simulation, training, and edge deployment concerns for embodied AI.

Details:
- GR00T's physical AI lifecycle starts by generating, collecting, or multiplying data; then consumes that data while training a model; then deploys the model onto a robot or edge device. (02:37-03:12)
- NVIDIA frames this as a three-computer problem because simulation, training, and edge deployment have different workload shapes. (03:15-03:22)
- The talk maps simulation to OVX/Omniverse-style machines, training to DGX-style systems that consume large data volumes, and deployment to efficient edge devices such as AGX. (03:22-03:53)
- Project GR00T is presented as a full robotics strategy that spans compute infrastructure, software, research, and the foundation model rather than only a standalone model release. (03:53-04:13)

Related topics:
- [Robotics](../topics/robotics.md)
- [Infrastructure](../topics/infrastructure.md)
- [Edge Inference](../topics/edge-inference.md)

Related concepts:
- [Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data](robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)

Sources:
- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md), 02:37-04:13
