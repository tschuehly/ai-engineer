# Plan AI products for a multimodel market

Summary: AI applications should assume model capability, pricing, and provider share will keep changing. Product and infrastructure design should make model routing, comparison, and replacement normal rather than binding core workflow value to one provider.

Use when:
- Designing model access for an AI application that may need OpenAI, Anthropic, Google, open-source, or specialized models.
- Deciding whether to build workflow value above the model layer instead of relying on one model's temporary lead.

Details:
- Guo frames the model market as increasingly competitive: prior-generation models get much cheaper, Claude and Gemini change usage share, DeepSeek-style releases add competitive open models, and credible new players can enter with different technical approaches. 09:55-11:16
- The practical recommendation is to plan for a multimodel world and use routing or inference platforms such as OpenRouter or Baseten when they help abstract provider choice. 11:16-11:28
- This does not mean model differences are irrelevant; it means the application should preserve enough flexibility to use the right model at the right time while keeping the product's workflow value above the provider choice. 11:16-11:28

Related topics:
- [Inference](../topics/inference.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Abstract LLM inference behind one routing API](abstract-llm-inference-behind-one-routing-api.md)
- [Build domain-specific workflow wrappers around models](build-domain-specific-workflow-wrappers-around-models.md)

Sources:
- [State of Startups and AI 2025 - Sarah Guo, Conviction](../sources/20250802_3MZS5gNElZM.md), 09:55-11:28
