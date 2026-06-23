# Diffusion Models Self-Correct by Revising Earlier Tokens

Summary: Because text diffusion attends bidirectionally and iterates over the whole output, it can go back and fix an early answer after working through reasoning it has not yet committed to — something an autoregressive model structurally cannot do once it has emitted a token.

Use when:
- Comparing diffusion vs autoregressive reasoning behavior.
- Explaining why a small diffusion model can beat a much larger autoregressive model on a problem that needs revision.
- Reasoning about self-correction as a property of the generation paradigm rather than of a separate "thinking" model.

Details:
- Demo (correct answer 39, "sqrt(81) ... " arithmetic): Gemini Diffusion after one forward pass produced "answer = 60" (wrong) then began reasoning; after two passes it changed 60 → 49; after three passes it finished the reasoning (36 + 3 = 39) and went back to fix the original answer to 39. It guessed wrong twice but corrected itself once the reasoning completed. (08:47-11:00)
- Two much larger autoregressive models failed the same prompt: GPT-4o first emitted 40, reasoned, then corrected ("I made a mistake, it's 39, not 40"); Gemini 2.5 Flash emitted 42 and "stuck to its guns," even writing "36 + 3 is 42" — it incorporated the early error into its later reasoning. Both were far bigger than the Gemini Diffusion model. (11:00-11:55)
- The mechanism: autoregressive models have causal attention and can only attend to the past, so a wrong early token is locked in; a diffusion model attends to the future it will emit and can revise the start after the rest is computed. This is framed as a structural flaw of autoregressive generation, not a model-size issue. (04:18-04:45, 11:30-11:55)
- The autoregressive workaround — modern reasoning / "thinking" models — only "punts the problem into something else" rather than removing the left-to-right commitment. (11:48-12:00)

Related topics:
- [Models](../topics/models.md)

Related concepts:
- [Generate Text by Iterative Denoising, Not Left-to-Right](generate-text-by-iterative-denoising-not-left-to-right.md)
- [Scale Text-Diffusion Quality With More Denoising Steps](scale-text-diffusion-quality-with-more-denoising-steps.md)
- [Scale Reasoning Models With RL and Verifiable Domains](scale-reasoning-models-with-rl-and-verifiable-domains.md)

Sources:
- [Text Diffusion — Brendan O'Donoghue, Google DeepMind](../sources/20260604_r305-aQTaU0.md), 04:18-12:00
