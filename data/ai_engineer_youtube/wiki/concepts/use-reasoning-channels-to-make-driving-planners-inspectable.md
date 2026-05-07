# Use Reasoning Channels To Make Driving Planners Inspectable

Summary: End-to-end driving models need interpretable intermediate outputs before action waypoints are trusted. EMMA adds a reasoning channel that identifies critical road objects, predicts their behavior, and states a driving meta-decision before emitting a planner output.

Use when:
- Evaluating whether an embodied model's action is explainable enough for safety review.
- Designing intermediate reasoning targets for multimodal action models.

Details:
- The talk names explainability as a clear drawback of end-to-end planning because a waypoint output alone does not reveal what happened inside the model. (09:38-09:54)
- EMMA addresses this by asking the model to explain the driving scenario before outputting the planner result. (09:54-10:07)
- The reasoning channel can identify critical objects such as a cyclist and vehicle, describe expected object behaviors, and choose a meta-decision such as keep speed, yield, or slow down. (10:07-10:35)
- Adding chain-of-thought-style reasoning improved performance on a larger Waymo motion dataset against strong baselines that used oracle perception, road graph, high-definition map, and traffic-light-state inputs. (10:36-11:35)

Related topics:
- [Robotics](../topics/robotics.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Mechanistic Interpretability Turns Model Internals Into Engineering Surfaces](mechanistic-interpretability-turns-model-internals-into-engineering-surfaces.md)
- [Make agent work more trustworthy by making it verifiable](make-agent-work-more-trustworthy-by-making-it-verifiable.md)

Sources:
- [Waymo's EMMA: Teaching Cars to Think - Jyh Jing Hwang, Waymo](../sources/20250726_iS9YFW28XyM.md), 09:38-11:35
