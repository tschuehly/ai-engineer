# Make Agent Edits Declarative Tags Instead of Generated Code

Summary: An agent that edits a live world can be restricted to attaching and removing declarative tags on objects, with built-in systems doing all the interpretation, instead of writing code that the runtime then executes. This collapses the agent's action space to a small closed vocabulary, makes every edit reversible and inspectable, and turns unplanned tag combinations into a feature rather than a defect.

Use when:
- Designing what an agent is allowed to *do* to application state, and weighing generated code against structured mutations of a data model.
- An agent's outputs need to be predictable, diffable, or undoable by non-technical users.
- You already have an Entity Component System, feature-flag, or attribute-driven runtime and are deciding where the agent should attach to it.

Details:
- The mechanism is Entity Component System / data-oriented design lifted from game development onto the agent's action surface. In Nereu's "asset tag system" (captioned "asset tax system"), "we just describe objects with components or in this case with tags. And then there are systems that query for all the assets in the world and say… I'm going to move all the objects that have the vehicle, the player, and the drivable tag" (09:29-10:11). The behavior lives in the systems; the agent only decides which objects are in scope for which system.
- The agent's entire action space follows from that: after context assembly, "the agent just performs calls and appends or removes the tags. All these tags and all these systems are built into the engine" (11:35-11:48). There is no generated-code path to review, sandbox, or debug — the failure mode of a bad agent decision is a wrong tag on a wrong object, which the user can see and delete.
- The absence of a scripting layer is deliberate rather than an unfinished feature: "we don't have a scripting system in there. That's on purpose. But it's just JavaScript and runs on the browser. So, whoever wants to extend, they can… But for most users that shouldn't be the case" (11:48-12:05). The escape hatch exists at the platform level, not in the agent's hands.
- The composability payoff is that tag combinations nobody designed still work. A building with no tags does not move, but "nothing prevents you from adding the vehicle and drivable tag to your building and then you have a building that you can put in a Mario Kart style of game" (10:14-10:36). Because systems query by tag rather than by object type, the cross product of tags is reachable without any per-combination code — the opposite of a generated-code system, where each novel combination is a new script that may or may not work.
- Keeping the agent inside a closed vocabulary is also what makes its context tractable: it "knows, understands what are the tools available, what are the tags available, and then it applies them to the asset that I'm talking about" (10:37-10:53), and new tools are handed to the assistant as they are built — "every time we add new tools, the assistant knows the tools that we're adding" (13:37-13:50).
- The cost is expressiveness, and it lands on the platform team. Anything the tag vocabulary cannot say is unreachable until someone decomposes it into tags and systems, which Nunez names as the hardest part of the work (12:09-12:45). A generated-code agent trades reliability for the ability to express things its designers never enumerated.

Related topics:
- [Agents](../topics/agents.md)
- [Tools](../topics/tools.md)

Related concepts:
- [Expose the Domain's Vocabulary to Agents, Not the Platform's Primitives](expose-domain-vocabulary-to-agents-not-platform-primitives.md)
- [Place Agent UI Generation on a Static–Declarative–Generative Spectrum](place-agent-ui-on-the-static-declarative-generative-spectrum.md)
- [Choose agent observation and action spaces explicitly](choose-agent-observation-and-action-spaces-explicitly.md)
- [Encode Agent Intent Into Server-Side Tools](encode-agent-intent-into-server-side-tools.md)
- [Assemble Scene Context by Level of Detail Around the Edit Focus](assemble-scene-context-by-level-of-detail-around-the-edit-focus.md)

Sources:
- [The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu](../sources/20260818_VBCDhRrvlYo.md), 09:29-12:05, 13:37-13:50
