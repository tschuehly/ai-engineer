# Scale Text-Diffusion Quality With More Denoising Steps

Summary: The number of denoising passes is a test-time compute knob for text diffusion: quality rises roughly monotonically with more steps, and the model can be trained to decide for itself when it is done — spending few steps on easy prompts and many on hard ones — all within a step limit that bounds latency.

Use when:
- Tuning test-time compute for a diffusion model.
- Explaining adaptive computation that does not rely on an explicit reasoning chain.
- Planning predictable latency for a diffusion endpoint.

Details:
- More forward passes (a bigger denoising budget) give roughly monotonic quality gains across every eval, because even a nearly-clean solution is re-examined each pass and any mistake fixed — shown across six internal coding evals. (12:00-12:40)
- Adaptive / dynamic computation: the model can be trained to determine itself when it is finished, spending little compute on easy responses and longer on hard ones. Examples: "first 100 digits of pi" = 100 tokens in only 4 steps (memorized/easy); FizzBuzz code = 18 passes; "explain quantum mechanics in a paragraph" = 31 steps; on evals, GPQA Diamond (hard for the model size) takes long while MBPP basic Python finishes fast — entirely decided by the model. (12:40-14:26)
- Throughput contrast: in the 4 steps diffusion used to produce 100 tokens, an autoregressive model would have emitted only 4 tokens. (13:00-13:20)
- Latency is predictable: all responses run with a denoising-step limit but typically finish earlier than the limit, so you can understand the worst-case latency ahead of time. (22:00-23:00)

Related topics:
- [Models](../topics/models.md)
- [Inference](../topics/inference.md)

Related concepts:
- [Generate Text by Iterative Denoising, Not Left-to-Right](generate-text-by-iterative-denoising-not-left-to-right.md)
- [Diffusion Models Self-Correct by Revising Earlier Tokens](diffusion-models-self-correct-by-revising-earlier-tokens.md)
- [Text Diffusion Trades Serving Throughput for Low Latency](text-diffusion-trades-serving-throughput-for-low-latency.md)
- [Scale Reasoning Models With RL and Verifiable Domains](scale-reasoning-models-with-rl-and-verifiable-domains.md)
- [Scale Test-Time Search Through Parallel Verifier-Checked Branches](scale-test-time-search-through-parallel-verifier-checked-branches.md)

Sources:
- [Text Diffusion — Brendan O'Donoghue, Google DeepMind](../sources/20260604_r305-aQTaU0.md), 12:00-14:26, 22:00-23:00
