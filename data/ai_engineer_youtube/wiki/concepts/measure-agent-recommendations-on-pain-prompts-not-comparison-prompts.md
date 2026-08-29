# Measure Agent Recommendations on Pain Prompts, Not Comparison Prompts

Summary: An assistant's willingness to name your product depends heavily on how the question is framed, and the flattering framing is the one you would write by default. Sourcegraph appeared in 65% of answers to comparison-shopping prompts and in zero answers to a prompt describing the pain its product exists to solve — a gap that is invisible unless you deliberately run both conditions.

Use when:
- Setting up a generative-engine-optimization (GEO) measurement and choosing which prompts to run.
- A team concludes from assistant spot-checks that "the models know about us."
- Deciding whether a discoverability problem is a ranking problem or a messaging problem.

Details:
- **The two conditions and the numbers.** Prompts written around someone "actively shopping for this sort of code intelligence sort of tooling and doing a comparative sort of thing" returned the product "like 65% of the time." The prompt written as a symptom — "we keep breaking downstream services when we change shared libraries because we can't see all the consumers" — returned "zero mentions," and the assistant suggested "you could just have your developers make a wiki page." ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), 08:38-09:32)
- **Why the comparison prompt is the easy one.** A comparison prompt already contains the category name, so the assistant only has to enumerate known members of a category it has been handed. A pain prompt requires the model to make the inference from symptom to category to vendor — the same inference your marketing copy is supposed to make for a human — and each hop is a place to lose. The 65% is therefore closer to a recall check on the model's category list than to a measurement of discoverability.
- **The design step that produces the second condition.** The prompts come from asking "what is your ICP actually doing when you would want your product to be surfaced," not from asking what someone comparing tools would type. Jarmak names the pain condition as "arguably the more typical use case and where we'd want to be showing up for people." (08:18-08:57)
- **The diagnosis it licenses is about your content, not the model.** The hypothesis drawn is "maybe the messaging that we're putting out there isn't attributing some of these pains and use cases clearly enough for the agents to be picking it up" — which converts a discoverability metric into a specific editorial task: publish material that names the symptom in the customer's words and connects it to the capability. (09:32-09:50)
- **Make the lift measurable on a campaign timescale by targeting the retrieval path, not the weights.** The planned measurement watches "how the agents that are using those… web search tool calls… are then interpreting the information about your product," explicitly "not necessarily in the form of anything that was baked into the training data." Content that only pays off at the next pretraining run is unmeasurable this quarter; content that a search tool can retrieve today is testable by rerunning the same prompt set. (09:50-10:10)
- **Report both conditions as separate numbers.** Averaging them produces a single mention rate that hides the entire finding. The useful artifact is a prompt set partitioned by intent — comparison, pain, task-in-progress — with a mention rate and a recommendation rate per partition, rerun on each model release. The talk's closing instruction is exactly this: "start developing some of these experiments with the GEO, putting together those prompts, and looking at the mentions versus recommendations." (17:36-17:52)
- **Limit.** This is a self-reported pilot study by a vendor about its own product: no prompt count, no repetition count, no list of which assistants were queried, and single-condition point estimates. Treat 65-versus-zero as an existence proof that the gap can be total, not as a calibrated effect size. ([Jarmak](../sources/20260826_Lrw0jqBNaw0.md), Provenance and Limits)
- **The downstream instrument this one cannot replace.** A prompt harness measures the assistant's behavior; it does not measure whether anyone acted on it. Burns measures the other end with a free-text onboarding question — "how did you hear about this?" — which spiked from a named date and now ranks assistant recommendation as the top inbound source. The two are complementary and neither is sufficient: a mention rate can rise with no installs, and an inbound spike cannot tell you which prompt shape produced it. Running both also operationalizes this page's mentions-versus-recommendations distinction, because only an acted-on recommendation reaches a signup form. See [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md). ([Burns](../sources/20260826_V_5bn4q-vAI.md), 02:17-02:39)

Related topics:
- [Go To Market](../topics/go-to-market.md)
- [Product Strategy](../topics/product-strategy.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Stale Product Content Compounds Through Newer Models](stale-product-content-compounds-through-newer-models.md)
- [Self-Serve Onboarding Is a Precondition for Agent Recommendation](self-serve-onboarding-is-a-precondition-for-agent-recommendation.md)
- [Treat Agent Experience as a Curb Cut](treat-agent-experience-as-a-curb-cut.md)
- [Classify the Assistant Question Log to Find Feature and Content Gaps](classify-the-assistant-question-log-to-find-feature-and-content-gaps.md)
- [Distribution Is the New Bottleneck for Developer Tools](distribution-is-the-new-bottleneck-for-devtools.md)
- [Separate Agent as Product, Agent as Buyer, and Agent as User](separate-agent-as-product-buyer-and-user.md)
- [Agent-readable web surfaces guide browsing agents](agent-readable-web-surfaces-guide-browsing-agents.md)
- [Attribute LLM-Sourced Inbound With a How-Did-You-Hear Field](attribute-llm-sourced-inbound-with-a-how-did-you-hear-field.md)
- [Score Agent-Readiness Against a Moving Baseline](score-agent-readiness-against-a-moving-baseline.md)

Sources:
- [The Death of Developer Advocates — Stephanie Jarmak, Sourcegraph](../sources/20260826_Lrw0jqBNaw0.md), 07:47-10:10, 17:36-17:52
- [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](../sources/20260826_V_5bn4q-vAI.md), 02:17-02:39
