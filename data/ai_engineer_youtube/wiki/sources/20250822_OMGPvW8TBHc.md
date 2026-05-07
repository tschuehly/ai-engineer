# Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

Source: [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](https://www.youtube.com/watch?v=OMGPvW8TBHc)
Uploaded: 2025-08-22
Transcript: `raw/20250822_OMGPvW8TBHc/OMGPvW8TBHc.en-orig.vtt`

## Summary

Leonard Tang frames GenAI evaluation as an AI-specific fuzzing problem: static golden data sets miss brittle local failures, so production readiness needs large-scale simulation of input variants, automated judgment of outputs, and iterative search for cases that break the application. The talk also argues that ordinary LLM-as-judge calls need their own QA, and describes judge-time compute through structured judge agents, rubric fanout, self-verification, debate, ensembles, and RL-tuned small reward models.

## Extracted Concepts

- [Fuzz AI applications for local input brittleness](../concepts/fuzz-ai-applications-for-local-input-brittleness.md) - this source explains why static evals miss brittle behavior under nearby natural-language variants.
- [Search natural-language input space as an optimization problem](../concepts/search-natural-language-input-space-as-an-optimization-problem.md) - this source treats stimuli generation, fuzzing, and adversarial testing as guided search over prompts and modalities.
- [Calibrate LLM judges like binary classifiers](../concepts/calibrate-llm-judges-like-binary-classifiers.md) - this source adds judge failure modes and judge-time compute patterns for making automated scoring more reliable.

## Topic Links

- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

## Notes

- GenAI reliability is described as a last-mile problem: demo-ready systems are easy to build, while production-grade trust, reliability, and risk control remain hard. 01:18-02:09
- The central failure mode is not only nondeterminism; the speaker emphasizes local brittleness where similar inputs with small syntactic, semantic, or appearance changes can produce very different outputs. 02:47-03:56
- Static golden data sets can show perfect scores while nearby perturbations reveal different production behavior, so coverage is a primary weakness of traditional evals. 04:29-05:08
- Quality metrics are difficult because domain experts may have subjective taste and sensitivity that are hard to translate into quantitative measures; exact match, classifiers, semantic similarity, and off-the-shelf LLM judges each have quirks. 05:08-06:10
- "Haizing" simulates large-scale stimuli, scores application responses, and feeds the score back into another round of search until corner cases are found or the search budget is exhausted. 06:10-06:49
- Off-the-shelf LLM judges can hallucinate, be unstable, produce uncalibrated numeric scores, and change under ordering or rubric perturbations, so the judge itself needs QA. 07:10-08:45
- Verdict-style judge agents apply scalable-oversight primitives such as debate, self-verification, and ensembling to subjective expert QA tasks. 08:47-11:47
- The talk presents RL or GRPO-tuned small judges as another judge-time scaling route, including instance-specific criteria generation and critiques inspired by self-principled critique tuning. 11:53-13:56
- For input generation, ordinary fuzzing creates in-distribution variants of happy paths, while adversarial testing emulates prompt injection, jailbreak, and hostile user behavior. 14:06-14:39
- Natural-language fuzzing cannot brute-force the prompt space; the source frames it as discrete optimization using judge loss, gradient methods, tree search, MCTS, embedding-space search, and DSPy-style optimization. 14:39-16:21
- Case studies include a bank loan-calculation app tested against an 18-line code of conduct and a voice-agent debt-collection workflow where input variance included background noise, static, and frequency changes. 16:23-17:47
