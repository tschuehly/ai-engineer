# Validate Retrieved Content Before Spending Tokens on It

Summary: A blocked page arrives with a 200 status and a plausible body size, so pipelines that gate on status code and length forward CAPTCHA walls to the model as if they were content. The model can tell the difference — that is exactly the problem, because it is billed input tokens to do so, and the agent's choice set silently shrinks to whatever got through. Put a validity check in front of the model, and do it before compression, not after.

Use when:
- An agent fetches many pages in parallel and forwards them to a model, and the fetch layer's only health checks are HTTP status and response size.
- Token spend on a web-reading agent is higher than the useful content justifies, or its answers are drawn from a suspiciously narrow set of sources.
- Choosing between compressing retrieved payloads and filtering them.

Details:
- **The premise.** "HTTP response 200 does not mean that we are good to go" — validating content is one of the two standing rules the talk is built on, alongside using a browser only when you must. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 02:59-03:45)
- **The common implementation and why it looks fine.** "What we see when working with these types of customers is that they often fail to detect the failure. They end up checking only the content size and HTTP response code and then feeding this large HTML to an LLM." A challenge page passes both checks. In the talk's own case the failure was caught only because the builder "did well with observability"; nothing in the fetch path itself would have surfaced it. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-09:22)
- **Why model capability makes this worse, not better.** "A large language model of course can distinguish between valid shop content and a capture. But we need to spend tokens in order to do that." Competence at the detection step is what disguises the cost: nothing errors, the answer is still reasonable, and the waste is invisible in the output. The arithmetic: "when we attempt to open 10 websites, but only three return valid content but feed all of the 10 to the model… we waste 70% of the tokens." ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 09:22-09:44)
- **The second cost, which is not about money.** Blocked fetches do not just burn tokens, they remove options. In the browser-driven version the agent "would be left with very few choices with the majority of popular retailers being left out." An agent that can only choose among the sites that happen not to have blocked it is making a biased decision from a filtered sample, and no amount of reasoning quality repairs that. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 08:39-09:01)
- **Ordering matters: validity before compression.** The instinct to shrink the payload solves the wrong problem. "My initial hunch was to compress the output. But then I thought — wait, the problem is not the compression. The problem is that the content is not valid. We need to make sure that the content is valid before even attempting any compression. This will lead to more options for the agent to choose from and fewer wasted tokens." Compressing a CAPTCHA page produces a cheaper CAPTCHA page. ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 09:44-10:29)
- **Where the check belongs.** In the rebuilt pipeline the validity gate is inside the fetch tool, not in the agent: a blocked request "would fail with an explicit error message. So I know not to include it when sending to a large language model." That placement is the point — a validity signal the agent has to infer costs a model call, while one the tool asserts costs nothing. See [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md). ([Šteimantas](../sources/20260826_XsvUhpnHepE.md), 10:29-10:49)
- **Relation to the correctness-side page.** [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md) reads the same event as an accuracy failure: the block reaches a model that fabricates rather than refusing. This page reads it as a cost and coverage failure, and the two cases are distinguished by whether the block reaches the model at all. Bright Data's case has no valid content in context, so the model falls back on training data; here three of ten pages are real, so the answer is grounded but expensive and drawn from a truncated sample. The mitigation is the same in both readings — do not let the block into the context window — which is why it is worth doing even if your agent never hallucinates.
- **Caveat.** The 70% figure is arithmetic over a hypothetical ten-page fetch with three valid responses, not a measured waste rate, and the talk gives no observed block rate for any real workload. Treat it as an illustration of the shape of the loss.

Related topics:
- [Retrieval](../topics/retrieval.md)
- [Context Engineering](../topics/context-engineering.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Silent Web-Access Failure Produces Confident Hallucination](silent-web-access-failure-produces-confident-hallucination.md)
- [Fail Loudly and Bill Only for Successful Results](fail-loudly-and-bill-only-for-successful-results.md)
- [The Open Web Is Adversarial to Agent Access](the-open-web-is-adversarial-to-agent-access.md)
- [Assign a Web-Access Primitive Per Pipeline Stage](assign-a-web-access-primitive-per-pipeline-stage.md)
- [Measure Agent Interface Efficiency With Tokens Per Successful Outcome](measure-agent-interface-efficiency-with-tokens-per-successful-outcome.md)
- [Ground Agents With Managed Web-Access Infrastructure](ground-agents-with-managed-web-access-infrastructure.md)
- [Harden Third-Party MCP Tools Against Silent Failure and Endpoint Risk](harden-third-party-mcp-tools-against-silent-failure-and-endpoint-risk.md)
- [Verify an Action Through a Different Channel Than the One That Acted](verify-an-action-through-a-different-channel-than-the-one-that-acted.md)
- [Keep Geolocation Consistent Across Pipeline Stages](keep-geolocation-consistent-across-pipeline-stages.md)
- [Fix the Browser-Agent Runtime Interface Before Reaching for a Better Model](fix-the-browser-agent-runtime-interface-before-reaching-for-a-better-model.md)
- [Turn Tool Errors Into Agent Self-Healing Recovery](turn-tool-errors-into-agent-self-healing-recovery.md)
- [Treat CAPTCHA And Proof Of Work As Economic Friction](treat-captcha-and-proof-of-work-as-economic-friction.md)
- [Let an Agent Build and Maintain Self-Healing Scrapers](let-agents-build-and-maintain-self-healing-scrapers.md)

Sources:
- [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](../sources/20260826_XsvUhpnHepE.md), 02:59-03:45, 08:39-10:49
