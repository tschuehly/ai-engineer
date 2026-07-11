# Cut Coding-Agent Cost by Fixing the Input, Not the Model or Output

Summary: An AI-coding query's cost is dominated by input context (~90%, or ~70% in a later framing) rather than generated output (~10%) or the model choice, so the highest-leverage cost optimization is shrinking the retrieved context you send, not tuning the model, its settings, or its output length.

Use when:
- An AI-coding bill jumps without a usage change and you need to find where the money actually goes before optimizing.
- Deciding whether to invest in a cheaper/better model, prompt tweaks, output limits, or a retrieval/context layer.
- Justifying context-engineering or code-index work with a cost argument rather than a quality one.

Details:
- Diagnosis: a bill that went from "fine" to "huge" with "same project, same tools, just more of it" traced to context, not "AI thinking" — a typical query sent ~45,000 tokens of context when only ~5,000 mattered, so ~40,000 useless tokens were paid for every query ("like ordering a pizza and paying for extra nine pizzas you don't eat every time").
- The cost breakdown ("the most important slide"): ~90% of AI-coding cost is input (files, search results, context you send in) and ~10% is output (the code the model writes back). So the leverage is asymmetric — cutting output 75% saves only ~8% of the total, while cutting input 94% saves ~61%: "same math, but different result. Fix the input." Restated at the end as models ≈30% of cost, "the other 70% is what you feed it."
- Why the obvious fixes underdeliver: (1) prompt tweaks ("be short, only show relevant code") change nothing because the ~45K tokens are already charged before the model reads the instruction — "cost already happened"; (2) model settings (max tokens, temperature) "change the output, not the input… the money is in the input"; (3) output compression (telling the model to write short answers) genuinely works — it cut output ~75% — but "75% of a small number is still a small number" because output is only ~10% of cost.
- Consequence: "the answer was not a better model. The answer was sending less… fix the input, the model choice matters less than you think." This reframes the Opus-vs-Sonnet debate as second-order and points optimization effort at retrieval/context selection.
- Corroborates the broader "keep context small" thread from the cost side rather than the quality side (context rot, the U-curve, attention limits): here the argument is purely economic — you pay for every irrelevant token on every query.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Coding Agents](../topics/coding-agents.md)

Related concepts:
- [Insert a local code-index retrieval layer between the codebase and the coding agent](insert-a-local-code-index-retrieval-layer-between-codebase-and-agent.md)
- [Treat Embeddings as Cached Compute Decided by Query Volume](treat-embeddings-as-cached-compute-decided-by-query-volume.md)
- [Curate Context Strategically Because Models Drop the Middle](curate-context-strategically-because-models-drop-the-middle.md)
- [Keep agent context small, fresh, and task-specific](keep-agent-context-small-fresh-and-task-specific.md)

Sources:
- [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](../sources/20260628_dRmWYHuIJxM.md), 00:15-03:20, 10:05-10:40
