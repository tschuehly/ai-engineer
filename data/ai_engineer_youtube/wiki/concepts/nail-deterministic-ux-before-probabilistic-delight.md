# Nail Deterministic UX Before Probabilistic Delight

Summary: AI-native apps still need ordinary product reliability before probabilistic model behavior can feel useful. Broken setup, unclear source selection, failed uploads, or weak first actions can destroy trust before users reach the magical parts.

Use when:
- Prioritizing engineering work around an AI feature's onboarding and core flow.
- Deciding whether to invest in model novelty or product basics.

Details:
- The talk states that teams should nail deterministic things before delightful probabilistic bits because a good app is still a good app. 14:55-15:18
- NotebookLM users frequently started by uploading sources and asking for summarization; if that first deterministic-plus-model path failed, the user could leave permanently. 15:20-16:24
- The warning is not anti-delight: it says the product must first earn trust by making the core job work as promised, then use probabilistic behavior to create surprise. 16:34-17:19
- **Where there is no deterministic core path to nail, scope substitutes for it.** An open-input assistant has no equivalent of "upload sources, ask for a summary": each user invents their own first path, so reliability cannot be concentrated on one flow. Izmit's answer is to shrink what the system will attempt until the attempted set is near-certain — "we want to answer 50 questions, but get them 95% right" — and to write the candidate question set from the business process beforehand so the boundary is chosen rather than discovered. Same goal as this page, different lever: not making the core flow deterministic, but making the reachable surface small enough to be reliable. ([Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-05:05)

Related topics:
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Earn AI Product Trust Before Asking for Delight](earn-ai-product-trust-before-asking-for-delight.md)
- [Stage complex AI applications into inspectable deterministic and agentic steps](stage-complex-ai-applications-into-inspectable-deterministic-and-agentic-steps.md)
- [Prefer simple debuggable eval scores](prefer-simple-debuggable-eval-scores.md)
- [Choose Quality Over Coverage Because the First Five Answers Decide Adoption](choose-quality-over-coverage-because-the-first-five-answers-decide-adoption.md)

Sources:
- [Everything is ugly, so go build something that isn't - Raiza Martin, Huxe (ex NotebookLM)](../sources/20250728_yG5d5UaGz1M.md), 14:55-17:19
- [Building GTM AI Agents: Lessons from Deploying to 6,000 Users — Sait Izmit, Snowflake](../sources/20260826_DrTdD-ttjCY.md), 04:08-05:05
