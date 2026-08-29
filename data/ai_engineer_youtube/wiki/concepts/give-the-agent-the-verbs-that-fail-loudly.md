# Give the Agent the Verbs That Fail Loudly

Summary: Classify an agent's operations by what happens when they go wrong, not by how large or destructive they look. Two operations of identical size can have opposite blast radius depending on direction: one turns a dashboard red and gets corrected cheaply, its inverse leaves everything green while a real problem walks past. Give the agent the loud verbs and keep a human on the quiet ones.

Use when:
- Deciding which subset of an API or CLI an agent may call, and the operations come in pairs.
- A risk review is classifying agent actions as "read" and "write" and that split is not separating the cases that matter.
- An agent has an operation that suppresses, disables, silences, filters, or acknowledges something.

Details:
- **The definition.** Verbs are "operations or actions that an agent can take… it could be API calls, it could be CLI commands, it could be really anything," and they are asymmetric because "the same sized action even though it looks same size… can have very different blast radius in actuality depending on which direction it goes." The instruction that follows is the useful part: "stop thinking about resources for a second and think about verbs… think about what happens when one of the verbs goes wrong." ([Malhotra](../sources/20260822_rbjWzZK2LU0.md), 05:47-06:21)
- **The canonical pair, from CI.** Unskip a test wrongly and "the worst that would happen is CI would go red for a bunch of people," which "a human can actually put back very cheaply." Skip a test wrongly and "nothing technically turns red. A real bug can actually walk into production with green checks and nobody would notice it until much later." Same resource, same size, opposite consequence: "the difference is which of the failures would show up on a dashboard and which one wouldn't." (06:21-07:04)
- **Paging is a loud verb, which is counterintuitive.** "If an agent decides to page a human and if it's the wrong call, the worst that's happening is that it's a nuisance for the on call. But there's always a human to correct it." Waking someone up reads as high-impact and is in fact one of the safest verbs to delegate, because its failure mode is self-reporting. (06:31-06:41)
- **The deployed instance.** A test quarantining service holds the list of tests currently skipped "because an on call decided that they had to break glass" during an incident. The agent may re-enable any of them; it may not add to the list. "The skip is a break glass verb itself" — what an on-call reaches for under pressure — so it "needs a human and it will always leave an audit trail." (07:14-08:07)
- **How this differs from the other controls in the same design.** The talk draws the line explicitly against the [undo test](size-agent-controls-with-the-undo-test.md): "the verbs ask whether you would notice the failure and undo asks whether you can recover from it." Detectability and recoverability are independent — a loud verb can still be hard to undo, and a quiet verb can be trivially reversible once someone finally notices — so both questions get asked. (12:33-12:43)
- **Where this sits against the wiki's other action-classification rules.** Amazon AGI Lab trains agents to judge an action on four properties — authorized, irreversible, visible to the user, impactful ([calibrated confidence](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)) — and "visible" is the same axis this page isolates. The difference is where it is enforced and what it means: there it is a learned model-side estimate about visibility *to the user in the moment*, here it is a fixed operator-side scope decision about visibility *to monitoring afterwards*. Neither depends on the model's judgment being right, which is the point of putting it in the scope.
- **A test that transfers past CI.** For any operation, ask what the world looks like ten minutes after the agent gets it wrong. If some existing alarm, dashboard, red build, failed check, or annoyed human is now signaling, it is a loud verb. If the system looks exactly as it did before, it is quiet, and it belongs behind a human regardless of how small it seems. Suppressing an alert, marking an incident resolved, adding an exclusion to a filter, and lowering a threshold are all quiet by this test.
- **Evidence limits.** The classification is presented as a design principle with one worked pair from one domain. Nothing is measured: no count of agent unskips, no false-unskip rate, and no case where the quiet-verb restriction is reported to have prevented a specific bad outcome. The talk also does not address pairs where both directions are quiet, which is where the rule stops giving an answer.

Related topics:
- [Agents](../topics/agents.md)
- [Security](../topics/security.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Replace the Token's Boolean With a Budget on Four Dimensions](replace-the-token-boolean-with-a-budget-on-four-dimensions.md)
- [Size Agent Controls With the Undo Test](size-agent-controls-with-the-undo-test.md)
- [Teach Calibrated Confidence So an Agent Knows When to Hand Off](teach-calibrated-confidence-so-an-agent-knows-when-to-hand-off.md)
- [Route High-Impact Agent Actions Through Explicit Human Approval Gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)
- [Prefer Trip Wires to Allow Lists, Because Only One of Them Learns](prefer-trip-wires-to-allow-lists-because-only-one-of-them-learns.md)
- [Let the Agent Reach a Test Environment, Not Production, When the Domain Carries Money](let-the-agent-reach-a-test-environment-not-production.md)

Sources:
- [Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic](../sources/20260822_rbjWzZK2LU0.md), 05:47-08:07, 12:33-12:43
