# Make the Doc the State and the Agent the Action

Summary: In a long-lived chat session, the state of the work is implicit context accumulating inside one agent's window — unshared, and gone when the session ends. Pull that state out into a durable shared document and keep the agent as pure action: agents become "largely stateless," several can start from identical context, the team can read what was decided, and rebuilding your own understanding becomes rereading a file.

Use when:
- Deciding where the durable state of a piece of work should live when agents do the implementation.
- Designing for several agents that need to start from the same understanding.
- Fixing a workflow where killing a session destroys the reasoning that produced it.

Details:
- The diagnosis of chat as a medium: chats "are the relic of building for implementation. So they're… default isolated and ephemeral and… brain off. They're made to build things and get stuff done. And that's not really the same type of work we're doing at the decision layer." ([Dailey](../sources/20260809_Kz4QJmNrVXU.md), 11:11-11:35)
- What that costs: "decisions are being made in that… chat that are not shared with my team, that are going to disappear as… I'm going to result in some code being output where those important decisions are not being made clear and shared with the team." The asymmetry is the point — the code survives the session and the reasoning does not. (10:38-10:55)
- **The split**, called "the big conceptual flip": "when you're living and working in a long-lived session with an agent, there's this implicit context being built up… over that work, and that's great… But… you're also doing actions and it's not shared. What you want is to separate the agent as the action and the doc as the state. And so, you can spawn new agents that have the same context or starting from the same place that are able to collaborate and work on the same piece of context and state." (13:25-13:57)
- The context-engineering framing is explicit: "You're ultimately doing context engineering in this doc, so that every agent is largely stateless and starts from this… same place." The doc is not documentation of the work — it is the agent's constructed context, maintained by hand, with the agent's session treated as disposable. (13:57-14:10)
- **Restartability is the payoff most worth stealing.** "declaring agent bankruptcy is just not a thing because you've made your agent stateless. So, the result of their work is in the do[c]. If you need to rebuild your human context, you just read the doc. Now, you understand the state of this project and you can pick up from there." Note that this repairs the human's context as well as the agent's; both were previously reconstructed by scrolling a transcript. (16:55-17:10)
- **Parallelism follows from shared state, not from tooling.** "when you have this state extracted and you're working from a shared context, you get more parallel agents. It's easier to work with parallel agents." Several agents starting from one written state is a different mechanism from isolating them in worktrees or swim lanes: those separate the *workspace*, this unifies the *premise*. (17:29-17:39)
- **Write decisions down up front rather than mining them afterward.** "a lot of people are thinking about how do we capture all the decisions going into these sessions? A really great solution to that is let's pull out all the decisions up front and agree to them and put them in a place that's durable so that we don't have to have like some LLM summarizing it and maybe picking the wrong things later on." This is a direct alternative to session-transcript extraction — see the tension recorded at [Capture the Coding Session as the Intent Record](capture-the-coding-session-as-the-intent-record.md), which argues the decisions that matter are made *during* implementation and so cannot all be hoisted to the front. (17:41-18:05)
- What the doc is for, in operational terms: "a tool that… helps me understand that system and lay out those key decisions in a… technical sense" — the "portal to the software system," where you say "Show me what matters… Pull out the bits that are relevant" and then "Organize the pieces in the way you want to represent how you want the system to grow." Relevance-finding is the model's job; the arrangement expresses the human's intent for the system. (12:52-13:25)
- The summary form is a substitution of the unit of work: "your core atom of your work is a doc rather than a chat." (14:23-14:30)
- **Unpriced costs.** The talk names no owner for the doc, no versioning against the code it describes, no retirement policy, and no answer for concurrent editing or for a doc that grows to the size of the chat it replaced. The wiki's counterweight is [Retire Completed Planning Docs Before They Become Agent Doc Rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md): a durable planning artifact that outlives its accuracy becomes harmful retrieval context, which is exactly the failure a state document invites. Treat doc lifecycle as the design work this pattern hands you.
- Caveat: vendor talk, and "agent bankruptcy is just not a thing" is the strongest and least supported claim in it — no measurement of restart cost, doc size, or how often a reread actually substitutes for the lost session.
- **A second speaker in the same week reaches the same formulation, and gives it its shortest name.** GitHub Next projects that "more and more of the work that we're doing with AI results in markdown documents in a docs folder that captures sort of the truth," and that editing those documents becomes the development action: "in order to change something about my application, I'm going to edit a document, and I'm going to tell AI, 'Hey, make the document true.'" The independent arrival is the evidence worth recording, since the two sources share no product, method, or framing. It also arrives with the same bill unpaid: neither describes who owns a living state document, how it is versioned against the code it describes, or when it is retired ([retire completed planning docs before they become agent doc rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)). ([Idan Gazit](../sources/20260808_iQ5xldZ9StU.md), 17:45-18:24)

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Separate the Decision Layer From the Implementation Layer](separate-the-decision-layer-from-the-implementation-layer.md)
- [Capture the Coding Session as the Intent Record](capture-the-coding-session-as-the-intent-record.md)
- [Retire Completed Planning Docs Before They Become Agent Doc Rot](retire-completed-planning-docs-before-they-become-agent-doc-rot.md)
- [Collaborate With Complex Agents Through High-Bandwidth Artifacts](collaborate-with-complex-agents-through-high-bandwidth-artifacts.md)
- [Collaborative Plans Become Executable Agent Context](collaborative-plans-become-executable-agent-context.md)
- [Keep the Session Log Separate From the Context Window](keep-the-session-log-separate-from-the-context-window.md)
- [Use Decision Logs to Keep Uncertain Agents Moving](use-decision-logs-to-keep-uncertain-agents-moving.md)
- [Tell the Agent Only What Is Not Recoverable From the Code](tell-the-agent-only-what-is-not-recoverable-from-the-code.md)

Sources:
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster — Matt Dailey, Ref.](../sources/20260809_Kz4QJmNrVXU.md), 10:38-11:35, 12:52-14:30, 16:55-18:05
- [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](../sources/20260808_iQ5xldZ9StU.md), 17:45-18:24
