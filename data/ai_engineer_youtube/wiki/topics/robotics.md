# Robotics

## Overview

Robotics turns agent design into a physical control problem. A humanoid or robot foundation model needs language and vision understanding, but it also needs action data, simulation, embodiment-specific control surfaces, edge deployment, and runtime diagnostics across the sensor-policy-actuator path. GR00T N1 adds a reusable model pattern for this domain: collect or synthesize action data, train a vision-language-action model, and deploy it efficiently on the robot while separating slower task planning from fast motor control.

The topic also clarifies why physical AI is not just an LLM with tools. The useful data is not abundant web text but scarce robot trajectories, indirect human videos, simulation rollouts, and multiplied demonstrations. The model's output is not final text but continuous action vectors that must be decoded for a specific body and then delivered through real hardware and software paths. That makes sim-to-real transfer, teleoperation cost, edge latency, and low-level systems failures part of the robotics model's quality envelope.

Physical Intelligence adds a production data-engine view of that problem. A robotics team may need to operate its own collection loop: pick expanding task families, teleoperate robots through custom runtime and leader-arm systems, schedule and measure collection sessions, annotate and filter successful episodes, and feed those episodes back into training. Its PI05 framing also shows a concrete VLA architecture pattern: reuse a pretrained VLM-like backbone for scene understanding and high-level task subdivision, then add an action expert transformer that can attend to the backbone and produce continuous actions at a higher control rate.

Waymo's EMMA adds an autonomous-driving version of physical-agent modeling. Instead of only chaining separate perception, prediction, and planning components, EMMA explores a Gemini-based route-plus-camera formulation: route instructions become text, 360-degree camera video becomes the observation stream, and the model predicts future vehicle waypoints. That makes driving logs a scalable self-supervised training source, but it also makes interpretability and closed-loop evaluation central because a waypoint alone does not explain which road actors and risks shaped the maneuver.

Robotics generalization should be evaluated as transfer, not only as a demo in the training lab. Held-out homes test whether location diversity creates reusable behavior, long-horizon household tasks test whether high-level prompts can be decomposed into minutes of autonomous action, and unfamiliar partner hardware tests whether model intelligence and software integration can move across robot platforms without the model team hand-tuning that robot body.

Driving-model evaluation sharpens the simulation requirement. Open-loop replay can rank a planner on logged data, but simulation lets teams observe how an action model behaves after its own decisions change the virtual world. Generated sensor video can make that test surface more controllable by varying rain, lighting, time of day, and other conditions that are expensive or unsafe to collect exhaustively.

## Key Concepts

- [Physical AI Has a Three-Stage Compute Lifecycle](../concepts/physical-ai-has-a-three-stage-compute-lifecycle.md) - robotics foundation models need distinct simulation, training, and edge deployment infrastructure.
- [Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data](../concepts/robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md) - robot action data needs teleoperation, human videos, simulation, and data multiplication because internet-scale action traces do not exist.
- [Robotics Data Engines Need Operated Teleoperation Pipelines](../concepts/robotics-data-engines-need-operated-teleoperation-pipelines.md) - frontier robot policies need data collection operations, annotation, filtering, and quality control loops.
- [Dual-System VLA Architectures Separate Planning From Realtime Control](../concepts/dual-system-vla-architectures-separate-planning-from-realtime-control.md) - embodied models can pair slow semantic planning with high-frequency motor execution.
- [Action Expert Transformers Adapt VLMs For High-Frequency Robot Control](../concepts/action-expert-transformers-adapt-vlms-for-high-frequency-robot-control.md) - VLM backbones can be adapted with action-generating architecture for continuous control.
- [End-to-End Driving Models Can Use Route Text and Camera Video](../concepts/end-to-end-driving-models-can-use-route-text-and-camera-video.md) - autonomous-driving foundation models can map route-conditioned camera video to future waypoints.
- [Use Reasoning Channels To Make Driving Planners Inspectable](../concepts/use-reasoning-channels-to-make-driving-planners-inspectable.md) - driving planners need intermediate critical-object and meta-decision explanations before waypoint outputs are trusted.
- [Evaluate Driving Models With Generated Sensor Simulation](../concepts/evaluate-driving-models-with-generated-sensor-simulation.md) - generated sensor videos can test planner behavior under controllable weather and lighting conditions.
- [Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable](../concepts/embodiment-specific-action-decoders-make-robot-foundation-models-adaptable.md) - action decoders translate shared model outputs into body-specific continuous motion.
- [Test Robot Generalization By Held-Out Locations And Hardware](../concepts/test-robot-generalization-by-held-out-locations-and-hardware.md) - robotics transfer claims need held-out homes, long-horizon tasks, and unfamiliar hardware checks.
- [Robotics Policy Failures Can Originate Below The Model](../concepts/robotics-policy-failures-can-originate-below-the-model.md) - physical behavior must be debugged through communication, scheduling, logging, and hardware paths before blaming policy quality.
- [Treat agents as embodied action systems](../concepts/treat-agents-as-embodied-action-systems.md) - robotics offers a useful lens for digital agents because action surfaces and feedback loops define what the model can do.

## Open Questions

- Which robot tasks are best learned through teleoperation, synthetic simulation, trajectory multiplication, or reinforcement learning?
- How should teams evaluate whether a cross-embodiment foundation model transfers useful knowledge to a new robot body?
- What runtime diagnostics are sufficient to distinguish model-policy errors from actuator, sensor, bus, scheduler, or edge-compute failures?
- Which parts of cross-hardware robot transfer should live in the model, the embodiment adapter, the inference runtime, or partner-side integration code?
- Which generated sensor conditions are faithful enough to predict real-world driving-planner safety regressions?

## Sources

- [What Is a Humanoid Foundation Model? An Introduction to GR00T N1 - Annika & Aastha](../sources/20250728_mWKYvT9Lc50.md)
- [Rishabh Garg, Tesla Optimus - Challenges in High Performance Robotics Systems](../sources/20250825_bCGbuyv8PMk.md)
- [Agents are Robots Too: What Self-Driving Taught Me About Building Agents - Jesse Hu, Abundant](../sources/20251124_qqXdLf3wy1E.md)
- [Robotics: why now? - Quan Vuong and Jost Tobias Springberg, Physical Intelligence](../sources/20250726_cGLa8DsOYdk.md)
- [Waymo's EMMA: Teaching Cars to Think - Jyh Jing Hwang, Waymo](../sources/20250726_iS9YFW28XyM.md)
