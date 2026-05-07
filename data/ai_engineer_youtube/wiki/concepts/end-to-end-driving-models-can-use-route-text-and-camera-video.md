# End-to-End Driving Models Can Use Route Text and Camera Video

Summary: Autonomous-driving foundation-model prototypes can formulate planning as route-conditioned video-to-waypoint prediction. Waymo's EMMA exploration feeds routing instructions as text plus 360-degree camera video into a Gemini-based model that outputs future vehicle waypoints.

Use when:
- Designing embodied agents that must turn multimodal observations and a goal route into continuous action plans.
- Comparing modular perception-prediction-planning stacks with end-to-end multimodal planning models.

Details:
- The conventional autonomous-driving stack is described as perception to understand the world, prediction to forecast future world states, and planning to choose steering, acceleration, and driving maneuvers. (02:03-02:31)
- EMMA's simple formulation translates route information into text, combines it with eight surrounding camera streams covering 360 degrees, and asks the Gemini-based model to output future waypoints for the next few seconds. (06:30-07:53)
- The formulation is self-supervised because driving logs already contain where the car went next, giving future waypoints as training targets at each time point. (07:58-08:19)
- The prototype is camera-only and high-definition-map-free, using ordinary route text rather than lidar or detailed map priors. (08:19-08:45)

Related topics:
- [Robotics](../topics/robotics.md)
- [Models](../topics/models.md)

Related concepts:
- [Dual-System VLA Architectures Separate Planning From Realtime Control](dual-system-vla-architectures-separate-planning-from-realtime-control.md)
- [Keep visual inputs at native shape for GUI and video agents](keep-visual-inputs-at-native-shape-for-gui-and-video-agents.md)

Sources:
- [Waymo's EMMA: Teaching Cars to Think - Jyh Jing Hwang, Waymo](../sources/20250726_iS9YFW28XyM.md), 02:03-02:31, 06:30-08:45
