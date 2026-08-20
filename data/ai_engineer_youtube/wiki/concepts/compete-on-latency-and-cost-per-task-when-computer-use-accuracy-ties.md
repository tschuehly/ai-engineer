# Compete on Latency and Cost per Task Once Computer-Use Accuracy Ties

Summary: When a purpose-trained computer-use model reaches accuracy parity with frontier general models, accuracy stops being the interesting number and latency per step and cost per task take over — because a browser task is 20-50 model calls, so per-step differences multiply and decide whether the workload is affordable at all.

Use when:
- Choosing a model for a browser or computer-use agent where the candidates are within noise on task success.
- Justifying a smaller specialized model over a frontier model to someone who only reads the accuracy column.
- Sizing the economics of running many agent instances in parallel.

Details:
- **The measurement.** Against Opus 4.7 and GPT-5.5 on browser-use benchmarks, Batra's own model is "slightly better, but I think that's within statistical noise in terms of accuracy. That improvement I wouldn't beat the drum on. What I would emphasize is latency per step and cost per task." Reporting your own headline win as noise is the part worth copying. ([Dhruv Batra](../sources/20260814_Ki980nV0__0.md), 17:34-17:57)
- **Why per-step matters more here than in chat.** These trajectories run "something like 20, 30 steps of interaction" (elsewhere in the same talk, "about 30 to 50 steps"), so both latency and price are multiplied by the step count before the user sees a result. (16:44-16:56, 17:57-18:24)
- **The numbers, as stated.** "This is a smaller footprint model. That's why it's a lot faster than some of the trillion-parameter-plus models. And there are corresponding cost savings… you're looking at 80 cents per task versus $2.30." Roughly 3x on cost, with the model-size difference given as the mechanism for the latency half. Provenance caveat: these are a vendor's own comparison numbers on unnamed browser-use benchmarks, presented without confidence intervals — see [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md) for why a 4%-apart accuracy comparison in this domain usually cannot support a ranking. (17:57-18:24)
- **What the cost floor unlocks architecturally.** Cheap steps are what make fan-out ordinary: "you can have an orchestrator that is launching multiple navigators in parallel, each with a cloud sandbox instance… so you can accomplish things that would be superhuman because no human would be able to parallelize over that many instances." The same argument the wiki records for [small agentic models making parallel workplace agents economical](small-agentic-models-make-parallel-workplace-agents-economical.md), reached in the computer-use setting where the step count makes it sharper. (15:23-15:51)
- **The trend claim this supports.** Batra's forecast that a browser-backed task endpoint replaces the API that will never be published rests entirely on these two axes continuing to fall: "accuracies are getting higher, benchmarks are falling, latencies are getting smaller, costs are falling," with the target being a structured result for "less than a penny." Whether that holds is the falsifiable part of [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md). (19:38-20:33)
- **He concedes the objection rather than denying it.** Asked whether computer use is slow and expensive: "That claim I think is largely true. There is some truth to it. But I think people forget how much you can optimize these things out." The concept is a claim about the *direction and headroom* of optimization, not a claim that browser agents are currently cheap. (17:13-17:34)
- **Relation to the wiki's general model-selection material.** This is the computer-use instance of [evaluating agent loops with correctness, cost, latency, and step counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md) and of [comparing models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md). What it adds is the step-count multiplier that makes the cost axis dominate earlier here than in single-shot workloads, and a worked case where the specialized small model is the one that wins it.

Related topics:
- [Agents](../topics/agents.md)
- [Inference](../topics/inference.md)
- [Models](../topics/models.md)

Related concepts:
- [Evaluate Agent Loops With Correctness, Cost, Latency, and Step Counts](evaluate-agent-loops-with-correctness-cost-latency-and-step-counts.md)
- [Compare models by task, thinking budget, cost, and latency](compare-models-by-task-thinking-budget-cost-and-latency.md)
- [Small agentic models make parallel workplace agents economical](small-agentic-models-make-parallel-workplace-agents-economical.md)
- [Right-size models with prototype big, deploy small](right-size-models-with-prototype-big-deploy-small.md)
- [The Long Tail of the Web Will Not Ship APIs](the-long-tail-of-the-web-will-not-ship-apis.md)
- [Compute Confidence Intervals Over Both Action and Environment Variance](compute-confidence-intervals-over-both-action-and-environment-variance.md)

Sources:
- [Computer-use models will agentify the web, not APIs — Dhruv Batra, Yutori](../sources/20260814_Ki980nV0__0.md), 15:23-20:33
