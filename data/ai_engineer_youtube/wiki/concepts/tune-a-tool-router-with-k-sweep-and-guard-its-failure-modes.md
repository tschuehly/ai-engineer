# Tune a Tool Router With a K-Sweep and Guard Its Failure Modes

Summary: Evaluate a semantic tool router on four metrics (tool-selection accuracy, time-to-first-token, input tokens per request, cost per 1,000 calls), sweep the retrieved-tool count K at 3/5/10 and pick the smallest K that hits the accuracy target (K=5 default), then guard the three failure modes — router miss, weak descriptions, and rare tools.

Use when:
- You have built a semantic / just-in-time tool router and need to pick K and prove it beats static loading.
- Diagnosing why a routed agent misses tools it should have selected, or why certain tools never get retrieved.

Details:
- Four eval metrics: tool-selection accuracy, time-to-first-token, input tokens per request, and estimated cost per 1,000 calls. Run identical queries in fat vs. routed mode with the same model, answer key, and tool catalog so the only variable is whether the model saw every tool or only the routed subset. (13:14-14:00)
- Datasets: the Berkeley Function Calling Leaderboard, Skills-bench-style scenarios, and synthetic tool pools that scale the catalog to 10/50/100/200/1041 tools so the accuracy and latency curves can be measured against tool count. (13:20-13:50)
- K trade-off: smaller K is faster and cheaper; larger K recovers more edge cases. K=5 is a strong default; sweep K at 3/5/10 and pick the smallest K that meets your accuracy target. (K = number of tools the router retrieves and gives the model per query.) (14:00-14:20, 21:20-21:40)
- Failure mode 1 — router miss: the router fails to retrieve a tool the model needs. Handle with a fallback: widen K, run a second retrieval pass, or route to a broader tool group. (24:20-24:50)
- Failure mode 2 — weak descriptions: weak tool descriptions produce weak embeddings and poor retrieval. Write descriptions in the words users actually use, encoding intent, action, and key entities. (24:50-25:15)
- Failure mode 3 — rare tools: some tools never score high unless their descriptions include the right language; monitor misses and rewrite those descriptions; re-embed tools when descriptions or schema change. (25:15-25:40)
- Production checklist: lock tools in one place (name, description, schema, owner, version); build the index; write the router (embed query → search → top-K → fetch schema); wire the agent's tool list to the router, not a hard-coded full catalog; evaluate at K=3/5/10; and monitor production by logging selected tools, final tool calls, failures, and fallback usage. "Not a 6-month platform rewrite… for most teams it is a focused sprint." (20:40-22:00)
- **The same component one level up, routing customers instead of tools, and reported without any of these guards.** Notion consolidated scattered eligibility checks into one rule set and put "a single classifier [that] will route what the customer should do" in front of it, credited with preventing double sends across marketing and sales. No model, feature set, accuracy figure, K-equivalent, or uncertainty fallback is given — a useful contrast, since the failure modes this page enumerates (router miss, weak descriptions, rare cases) all have direct analogues in a segment router. ([Liu](../sources/20260826_L4I7WgiEquo.md), 07:59-08:37)

Related topics:
- [Tools](../topics/tools.md)
- [Evaluation](../topics/evaluation.md)

Related concepts:
- [Retrieve tool descriptions before loading large tool catalogs](retrieve-tool-descriptions-before-loading-large-tool-catalogs.md)
- [The Fat-Agent Tool Overload Collapses Accuracy and Inflates Latency](fat-agent-tool-overload-collapses-accuracy-and-latency.md)
- [Use tool names and descriptions as operational prompts](use-tool-names-and-descriptions-as-operational-prompts.md)
- [Evaluate tool definitions and outputs as context](evaluate-tool-definitions-and-outputs-as-context.md)
- [Make Routing and Eligibility a Shared First-Class Primitive](make-routing-and-eligibility-a-shared-first-class-primitive.md)

Sources:
- [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](../sources/20260628_vh2VGuQ3zhY.md), 13:14-14:20, 20:40-25:40
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 07:59-08:37
