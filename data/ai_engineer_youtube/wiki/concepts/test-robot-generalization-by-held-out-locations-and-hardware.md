# Test Robot Generalization By Held-Out Locations And Hardware

Summary: Robot foundation-model claims should be tested against held-out environments and unfamiliar hardware, not only against trained scenes. Diversity in training locations can improve performance in unseen homes, while cross-hardware demos test whether the software and model generalize beyond one robot body and local team setup.

Use when:
- Evaluating whether a VLA transfers beyond its training locations or robot platform.
- Planning robotics benchmarks for long-horizon household tasks and cross-embodiment deployment.

Details:
- PI05 is presented as a VLA with open-world generalization after PI increased data-collection diversity across static and mobile robot setups, scenes, environments, robot data, web data, object detection data, and language annotations. (08:29-11:54)
- The talk says the model can perform long-horizon tasks up to about ten minutes in entirely unseen homes, including cleaning a kitchen surface and bedroom cleanup from a high-level prompt. (12:50-14:54)
- PI tested generalization by holding out a location, adding increasing numbers of other training locations, and measuring performance in the held-out location; performance increased and eventually matched or slightly surpassed training with that held-out scene included. (13:35-14:20)
- Cross-hardware transfer is treated as a separate hypothesis: PI shows a remote robot they had not seen in person or accessed internally making coffee end to end, using a model checkpoint shared with the partner for inference and low-level technical integration. (15:05-16:54)

Related topics:
- [Robotics](../topics/robotics.md)
- [Evaluation](../topics/evaluation.md)
- [Models](../topics/models.md)

Related concepts:
- [Embodiment-Specific Action Decoders Make Robot Foundation Models Adaptable](embodiment-specific-action-decoders-make-robot-foundation-models-adaptable.md)
- [Robotics Data Pyramids Combine Scarce Real Trajectories With Synthetic Data](robotics-data-pyramids-combine-scarce-real-trajectories-with-synthetic-data.md)

Sources:
- [Robotics: why now? - Quan Vuong and Jost Tobias Springberg, Physical Intelligence](../sources/20250726_cGLa8DsOYdk.md), 08:29-16:54
