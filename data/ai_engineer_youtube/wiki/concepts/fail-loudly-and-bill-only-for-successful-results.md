# Fail Loudly and Bill Only for Successful Results

Summary: A tool that returns a degraded payload — a challenge page, an empty result, a partial record — instead of an error pushes the detection cost onto the model, which pays in tokens and sometimes gets it wrong. The contract to insist on is an explicit error on the failure path. When the tool is bought, the pricing model is what makes the contract credible: a vendor that charges nothing for failed requests has aligned its incentive with yours to classify them honestly.

Use when:
- Designing the failure path of an agent-facing tool, MCP server, or data API.
- Evaluating a data or web-access vendor, and comparing on price per request without asking what a failure costs.
- An agent's context window is filling with responses that are technically successful and practically useless.

Details:
- **The contract.** In the rebuilt pipeline, a blocked fetch does not return the block: "in case of captures or other blocks the request would fail with an explicit error message. So I know not to include it when sending to a large language model." The value is entirely in *where* the classification happens — the provider already knows the request failed, and asserting it costs nothing, while re-deriving it inside the model costs the full input-token price of the payload. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 10:29-10:49)
- **The billing model as the enforcement mechanism.** "Customers only pay for successful results… No cure or no pay. If the scraper fails, there's no cost and it fails loudly." Presented as a commercial perk, this is really an incentive alignment: a vendor billing per request has a reason to count a returned CAPTCHA page as a delivered response, and a vendor billing per success does not. When comparing web-access, enrichment, or data providers, the question "what does a failed request cost me?" separates them more sharply than the headline unit price. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 11:30-11:54)
- **Why "loud" is the operative word.** The counterpart failure is not an error the agent mishandles; it is the absence of any signal. The default pipeline checked only "content size and HTTP response code," both of which a challenge page satisfies. A loud failure is one that cannot be confused with success by a check the caller can afford to run. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-09:01)
- **Relation to error-message design.** [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md) is about making an error *actionable* once it is raised. This is the step before it: raising one at all rather than returning a plausible body. Both fail in the same direction if skipped, but the costs differ — an unhelpful error wastes a retry, a swallowed error wastes the entire payload and corrupts the result set.
- **Generalization beyond web access.** The shape recurs wherever a dependency can partially succeed: a search returning zero relevant hits as an empty-but-successful list, an enrichment vendor returning nulls rather than a coverage miss, a guardrail timing out and passing traffic through. In each case the caller can construct a check, but the provider already has the answer, and the provider's version is free. The reciprocal design question for anyone building such a tool is which of its degraded outcomes currently look like successes on the wire.
- **The unresolved edge.** Neither the talk nor this page says what to do when the failure is partial rather than binary — a page that returns real content with a section missing, or a record where three of eight fields resolved. "Fails loudly" is well defined for a block and undefined for a truncation, and a hard error on a mostly-good payload is its own waste.
- **Caveat.** This is a vendor describing its own product's contract and pricing. No failure-rate, recovery-rate, or cost-comparison figure is given, and the accompanying "high success rate… even for protected websites" claim carries no number.

Related topics:
- [Tools](../topics/tools.md)
- [Agents](../topics/agents.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Validate Retrieved Content Before Spending Tokens on It](validate-retrieved-content-before-spending-tokens-on-it.md)
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md)
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [Make Recovery a Native Model Action, Not an Infra Reset](make-recovery-a-native-model-action-not-an-infra-reset.md)
- [Treat Guardrails as a Failable Dependency With a Time Budget](treat-guardrails-as-a-failable-dependency-with-a-time-budget.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)
- [Move Mandatory Brittle Tool Steps Outside the Agent Loop](move-mandatory-brittle-tool-steps-outside-the-agent-loop.md)

Sources:
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 08:39-09:01, 10:29-11:54
