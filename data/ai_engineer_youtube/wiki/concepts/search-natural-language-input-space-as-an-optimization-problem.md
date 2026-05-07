# Search natural-language input space as an optimization problem

Summary: Fuzzing and adversarial testing for AI systems should be treated as guided optimization over natural-language, conversation, and modality inputs. The objective is to find stimuli that make the application score poorly under a chosen judge, not to brute-force the prompt space.

Use when:
- Generating eval cases for chatbots, voice agents, RAG systems, or policy-bound AI applications.
- Deciding how to explore more input coverage after a static benchmark stops finding failures.

Details:
- The source separates in-distribution fuzzing from adversarial testing: fuzzing varies plausible happy-path inputs, while adversarial testing emulates prompt injection, jailbreaks, and hostile users. 14:06-14:39
- Natural language has too large an input space for brute-force search, so the search must be pruned and guided. 14:39-15:18
- The target can be the judge score itself: generate inputs that cause the application output to score poorly on the selected quality or safety measure. 15:33-15:50
- Candidate search methods include gradient-guided token changes, tree search, MCTS, embedding-space search mapped back to text, and DSPy-style optimization. 15:50-16:21
- The same frame extends beyond text: voice-agent testing can vary background noise, static, frequency, persistent conversations, and other audio or interaction properties. 17:05-19:06

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Fuzz AI applications for local input brittleness](fuzz-ai-applications-for-local-input-brittleness.md)
- [Evaluate voice agents with traces, transcripts, audio checks, and simulations](evaluate-voice-agents-with-traces-transcripts-audio-checks-and-simulations.md)
- [Build AI app benchmarks before optimization](build-ai-app-benchmarks-before-optimization.md)

Sources:
- [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](../sources/20250822_OMGPvW8TBHc.md), 14:06-16:21, 17:05-19:06
