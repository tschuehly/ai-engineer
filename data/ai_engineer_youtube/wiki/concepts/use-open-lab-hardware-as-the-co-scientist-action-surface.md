# Use Open Lab Hardware as the Co-Scientist Action Surface

Summary: A scientific co-scientist becomes more useful when it is connected to inspectable lab hardware and automation primitives, not only to papers and static data. Open hardware lowers the cost of building feedback loops where agents observe, measure, and eventually help control experiments.

Use when:
- Designing scientific agents that need to observe or manipulate physical experiments.
- Choosing whether to prototype with local sensors, cameras, and open lab automation before a full lab deployment.

Details:
- The demo connected a micro:bit/JackDac sensor board, heat pad, microscope, and camera so the AI assistant could analyze temperature and environmental readings in realtime. (00:59-01:30)
- A mobile object-tracking camera ran a model on the camera itself; Druga notes the same pattern could track crystal growth or other experiment-specific objects. (02:21-03:03)
- The prototype constrained experiment choice by available inputs and outputs, safe at-home execution, travel constraints, and whether the experiment could be measured in realtime. (10:23-11:03)
- Open-source lab hardware ecosystems such as Jubilee motion platform and open bioreactors make pipetting, droplet manipulation, liquid handling, and other scientific automation accessible to builders. (16:09-17:07)

Related topics:
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)
- [Workflows](../topics/workflows.md)

Related concepts:
- [Scientific Agents Should Execute Against Domain Infrastructure](scientific-agents-should-execute-against-domain-infrastructure.md)
- [Treat agents as embodied action systems](treat-agents-as-embodied-action-systems.md)

Sources:
- [Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind](../sources/20250728_wNH3q9pqn0U.md), 00:59-03:13, 10:23-11:03, 16:09-17:07
