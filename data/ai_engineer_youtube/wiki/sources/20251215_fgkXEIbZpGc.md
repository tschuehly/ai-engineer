# Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind

Source: [Building in the Gemini Era - Kat Kampf & Ammaar Reshi, Google DeepMind](https://www.youtube.com/watch?v=fgkXEIbZpGc)
Uploaded: 2025-12-15
Transcript: `raw/20251215_fgkXEIbZpGc/fgkXEIbZpGc.en-orig.vtt`

## Summary

Kat Kampf and Ammaar Reshi demonstrate Google AI Studio as a prompt-to-app and multimodal generation environment around Gemini 3 and Nano Banana Pro, emphasizing one-shot UI generation, agentic tool calling, search-grounded image creation, current-context media generation, and forthcoming full-stack runtime support that infers infrastructure needs from user intent.

## Extracted Concepts

- [Ground generated media with current search context](../concepts/ground-generated-media-with-current-search-context.md) - Nano Banana Pro examples use Google Search grounding to bring current facts and public context into generated images.
- [Use one-shot app builders for product ideation](../concepts/use-one-shot-app-builders-for-product-ideation.md) - AI Studio is shown as a way to create, clone, and vary UI concepts quickly enough to explore product interactions.
- [Infer full-stack app infrastructure from user intent](../concepts/infer-full-stack-app-infrastructure-from-user-intent.md) - the full-stack runtime direction is to map requests such as multiplayer, storage, or ecommerce into backend choices without asking users to specify infrastructure.

## Topic Links

- [Generative Media](../topics/generative-media.md)
- [Models](../topics/models.md)
- [Tools](../topics/tools.md)
- [Workflows](../topics/workflows.md)

## Notes

- Gemini 3 is framed around two capabilities for builders: stronger UI and aesthetic generation, including one-shot websites, and stronger agentic tool calling for complex tasks in codebases. 01:23-02:19
- Nano Banana Pro is described as having Google Search-powered world knowledge, improved text rendering, multilingual localization, multi-person consistency, creative controls such as focus changes, and multiple aspect ratios. 02:40-04:16
- AI Studio's build experience exposes feature "chips" for Gemini API capabilities such as Google Search grounding, Google Maps grounding, and the Live API, and shared apps can use visitors' AI Studio free quota rather than the creator's API bill for most models. 04:35-06:10
- The sticker demo uses Google Search grounding to gather current context about a person and generate personalized laptop-sticker imagery, including examples where current news or same-day information avoids relying only on the model's knowledge cutoff. 10:48-11:55
- The AI Studio team uses AI Studio to prototype AI Studio features, including a one-shot UI clone from a screenshot plus an export flow to the Antigravity IDE; repeated runs produced alternate export interactions such as command-line or status interfaces. 11:57-13:39
- A 3D racing game was generated in Three.js, then extended into a multiplayer version through a few prompts; the live demo showed scale and design caveats, including a crowded lobby, collision behavior, and start-state coordination. 13:45-16:08
- The planned full-stack runtime is presented as an abstraction layer that should infer backend support, packages, Express wiring, storage, payments, first-party APIs, and popular third-party API integrations from the user's application intent. 14:13-17:26
