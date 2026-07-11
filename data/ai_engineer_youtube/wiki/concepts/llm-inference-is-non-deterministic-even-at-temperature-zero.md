# LLM Inference Is Non-Deterministic Even at Temperature Zero

Summary: Setting temperature to zero does not make a hosted LLM reproducible; the same prompt can still return dozens of different completions because determinism is lost below the sampler, in floating-point math and server-side batching, not in the token choice.

Use when:
- A team plans to "fix" a non-reproducible agent failure by pinning temperature to zero.
- Deciding whether run-to-run reproducibility can be an assumption in agent debugging or eval design.

Details:
- Temperature zero is a "complete misconception" as a determinism fix: it doesn't repair a broken reasoning path, so the model makes the exact same logical error the exact same way — and worse, the same prompt run a thousand times can still return dozens of completely different responses. Setting temperature to zero is a controllability lever, not a reproducibility guarantee, 02:37-03:29.
- Four first-principles reasons the output drifts run to run, 03:38-04:51:
  - Sampling determinism ≠ system determinism: temperature zero just means always take the argmax, but it does not guarantee the underlying scores stay identical run to run.
  - Floating-point math is not associative: the order you add decimals matters, so a tiny shift in a matrix operation alters the final logits and flips the winning token.
  - It is not a concurrency issue: the same matrix multiplication run alone on a GPU a thousand times returns the exact same bits. The real culprit is batch invariance — a request gets grouped with whatever else hits the server that millisecond.
  - Mixture-of-experts routing has the same bottleneck: experts have strict capacity limits, so if a batch overflows a subnetwork, tokens get rerouted, and whether a token makes the cut depends entirely on the traffic it was batched with.
- Practical consequence for agent teams: chasing identical text output is a losing battle. Don't try to freeze the model; instead record what a run actually did and re-validate it (see record-and-replay). Log the session variables that do move the output — LLM version, build ID, RAG chunks — so you at least know which knobs were live, 04:51-05:33, 13:11-13:28.
- Keeping generation-time variation alive is a feature, not a bug: the randomness/exploration is what makes the model good and "brings the agency into your agent," so pinning temperature to zero is the wrong reflex even when it worked, 05:33-05:57, 13:44-13:52.

Related topics:
- [Inference](../topics/inference.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Record and Replay Agent Runs at Node Boundaries](record-and-replay-agent-runs-at-node-boundaries.md)
- [Turn Recorded Agent Traces Into Free Replay Test Cases](turn-recorded-agent-traces-into-free-replay-test-cases.md)

Sources:
- [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](../sources/20260629_Lc8zRh9muoY.md), 02:37-05:57, 13:11-13:52
