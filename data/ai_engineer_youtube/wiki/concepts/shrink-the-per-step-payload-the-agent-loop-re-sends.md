# Shrink the Per-Step Payload the Agent Loop Re-Sends

Summary: In an agent loop the system prompt, tool results, and conversation history are re-transmitted to the model on every iteration, so token spend compounds with loop length; shrink each re-sent part cheaply — cache the static prefix, offload large tool results out of the message stream, and window the conversation history — rather than changing the prompt or the model.

Use when:
- A production agent's bill is higher than expected even though the model and outputs are fine, and the cost tracks the number of loop iterations or turns.
- Reviewing an agent loop that re-sends its full system prompt, tool outputs, or chat transcript on every model call.
- Looking for cost reductions that are "a few lines of code" and don't require re-prompting or switching models.

Details:
- The compounding mechanism: total tokens ≈ (payload re-sent per step) × (number of steps). Everything the loop puts in the request — system prompt, tool prompts, prior tool results, conversation history — is charged again on each iteration, so shrinking the per-step payload multiplies through every loop. This concept targets the *payload* factor; the step-count factor is bounded separately (see [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md) and the max-iterations cap). ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 00:00-00:18)
- Lever — cache the static prefix: the system prompt (and, if supported, tool prompts and messages) is identical every call, so cache it — in AWS Strands, `cache_prompt = default` sends the full prompt once and a "much reduced" cached reference on every subsequent call. This is the application-code counterpart to the serving layer's [KV-cache hit rate SLO](kv-cache-hit-rate-is-a-production-agent-slo.md): fix the prefix so it stays cacheable. ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 00:18-01:01)
- Lever — offload large tool results: store a big tool result locally or in the cloud and keep only a summary in the message stream, so the full result "isn't added into the context every time the tool loops or every time the agent loops." This is the cost-side version of [clearing stale tool results from the context window](context-window-editing-clears-stale-tool-results.md) and of [offloading long-horizon state outside the window](offload-long-horizon-agent-state-outside-the-context-window.md). ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 01:51-02:47)
- Lever — window the conversation history: a multi-turn agent re-sends the whole transcript each call, which "can eat through hundreds, if not thousands, of tokens"; a sliding window (Strands' `SlidingWindowConversationManager`, e.g. last 10 messages, size configurable) sends only the recent tail. The tradeoff is explicit — "you will lose the message history from the beginning" — so recover the dropped early context by summarizing it into the window. This is the cheap, mechanical cousin of [frequent intentional compaction](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md). ([Erik Hanchett](../sources/20260628_uiP88SpCi1Q.md), 03:37-04:50)
- All three levers are framework-agnostic and require no prompt or model change; the talk demonstrates them with Strands but frames caching, offload, and history trimming as the general moves for reducing what the loop re-transmits.

Related topics:
- [Context Engineering](../topics/context-engineering.md)
- [Agents](../topics/agents.md)

Related concepts:
- [Route Each Request to the Cheapest Sufficient Model by Difficulty](route-each-request-to-the-cheapest-sufficient-model-by-difficulty.md)
- [Contain Retry Amplification Before It Becomes a Compute Incident](contain-retry-amplification-in-agent-loops.md)
- [KV-cache hit rate is a production agent SLO](kv-cache-hit-rate-is-a-production-agent-slo.md)
- [Context window editing clears stale tool results](context-window-editing-clears-stale-tool-results.md)
- [Frequent intentional compaction keeps coding agents in the smart zone](frequent-intentional-compaction-keeps-coding-agents-in-the-smart-zone.md)
- [Cut Coding-Agent Cost by Fixing the Input, Not the Model or Output](cut-coding-agent-cost-by-fixing-the-input-not-the-model-or-output.md)

Sources:
- [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](../sources/20260628_uiP88SpCi1Q.md), 00:00-01:01, 01:51-04:50
