# Court agent emergence with bounded play

Summary: Bounded prototypes can reveal useful agent behaviors that did not fit the original automation plan, such as combining related inputs, generating follow-up reports, or telling the human how to resolve work the agent cannot do.

Use when:
- Exploring whether an AI workflow should do more than automate an existing tedious step.
- Looking for product behaviors that emerge from realistic agent experiments rather than specification alone.

Details:
- The talk warns that new technology can be underused when teams only automate tedious existing steps instead of exploring new behavior enabled by the model. (11:09-11:27)
- In one prototype, dropping a JSON file and a CSV file led the agent to infer that the files should be combined, merge them, report duplicates, and suggest likely next actions. (11:48-13:09)
- A knowledge-base experiment over customer calls and documentation produced an unexpected escalation pattern: the agent decided it could not generate missing employee IDs but could tell the user to ask HR for them. (13:17-14:12)
- The source frames this human-escalation behavior as something the designer discovered through playing with the model and workflow, not something reached from upfront specification alone. (13:56-14:12)
- Teammates adds the product-management version of the same pattern: product teams may need to discover whether an agent can handle customer-invented workflows, such as Google Doc comment tagging, after customers try them. (01:57-02:46)

Related topics:
- [Agents](../topics/agents.md)
- [Workflows](../topics/workflows.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Build AI product iteration tools into the product context](build-ai-product-iteration-tools-into-the-product-context.md)
- [Use decision logs to keep uncertain agents moving](use-decision-logs-to-keep-uncertain-agents-moving.md)
- [Route high-impact agent actions through explicit human approval gates](route-high-impact-agent-actions-through-explicit-human-approval-gates.md)

Sources:
- [Form factors for your new AI coworkers - Craig Wattrus, Flatfile](../sources/20250822_CiMVKnX-CNI.md), 11:09-14:12
- [Shipping Products When You Don't Know What they Can Do - Ben Stein, Teammates](../sources/20250728_PthmdT92qNg.md), 01:57-07:25
