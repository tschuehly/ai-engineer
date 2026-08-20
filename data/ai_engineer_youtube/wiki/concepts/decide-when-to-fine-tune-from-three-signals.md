# Decide When to Fine-Tune From Three Business Signals

Summary: As an AI product matures and specializes, leaving the frontier API for a fine-tuned model becomes a "when," not an "if" — and three concrete signals say the moment is near: you pay more for the API than your customers pay you, your evals have plateaued, and your latency/throughput needs exceed what a shared endpoint will deliver.

Use when:
- Deciding whether a product has crossed from "wrap a frontier API" into a custom domain worth a fine-tuned model.
- Sequencing the build/own decision against data and eval readiness rather than treating training as a far-future project.
- Explaining to a team why a differentiated product eventually needs model differentiation.

Details:
- The framing thesis: the frontier labs "probably don't have the exact same goal as you" — they want their models to win on everything possible, you want yours to win at your business logic — so it's "just a matter of time until your product steps into being domain-specific," and a differentiated product is by definition custom. (Modal, citing customer Decagon) 04:38-06:12
- Signal 1 — economics inversion: you've already cut tokens (e.g. "caveman mode," telling the LLM to speak tersely) and are still paying more for the API than your customers pay you; the unit economics aren't scaling, which points to a customized inference endpoint. 06:20-06:37
- Signal 2 — eval plateau: when you stop improving on your evals, more prompt engineering won't help and fine-tuning is the lever that might. 06:39-06:50
- Signal 3 — latency/throughput ceiling: enterprise contracts with specific latency or throughput requirements (let alone a custom metric encapsulating your business logic) get little customization on a shared frontier endpoint. 02:36-02:57, 06:39-06:42
- The spectrum being crossed: frontier API (build fast, but no customization past prompt engineering, won't scale at 100×/1000×) ↔ full in-house training (total control but full responsibility for a cluster, infra engineers, and the whole stack). Fine-tuning is the move that escapes the API's ceiling without the legacy "huge jump" to managing your own cluster. 01:55-04:00
- Proof points that the pattern is real, not exceptional: Intercom is beating its frontier API at ~one-fifth the cost (the description says one-tenth); Pinterest claims orders of magnitude. 04:18-04:30
- Prerequisite — garbage in, garbage out: if you haven't been collecting data and lack mature evals, it's not time to train yet; collect the data first. The complement is that if you've built a product you've probably already touched everything you need to train, so the readiness gap is usually smaller than teams assume. 06:51-07:46
- Urgency framing: this is not "train now" — it might be 6 months or a year out — but you prepare for the moment by collecting data and developing evals before you need them. 11:35-12:06
- **A sequencing rule that sits under signal 2, from a vendor that sells fine-tuning.** LangChain picks the next lever by feedback latency rather than by power: "harness engineering gives you feedback in maybe 2 minutes," so you exhaust that ceiling first, fine-tune to break through it, then return to harness engineering — a sandwich rather than a graduation. The eval plateau in signal 2 is the same ceiling seen from the outside, and this explains why reaching it cheaply matters. Two qualifications travel with it: many teams never need the second rung ("we find a lot of teams are happy with harness engineering and it solves their customer use case, so we always sort of recommend it"), and the fine-tuning that does pay targets a narrow vertical because customers "don't really care about the entire variance of tasks" ([Sequence Harness Engineering and Fine-Tuning by Feedback Speed](sequence-harness-engineering-and-finetuning-by-feedback-speed.md)). ([LangChain](../sources/20260812_CvRngaQZQ3Y.md), 09:20-09:48, 15:58-16:51)

Related topics:
- [Models](../topics/models.md)
- [Infrastructure](../topics/infrastructure.md)

Related concepts:
- [Run Elastic Training on Serverless GPU, Not a Reserved Cluster](run-elastic-training-on-serverless-gpu-not-a-reserved-cluster.md)
- [Enterprise Open-Model Adoption Follows Task Pressure](enterprise-open-model-adoption-follows-task-pressure.md)
- [Decide open-model ownership by capability, hardware, latency, and cost thresholds](decide-open-model-ownership-by-capability-hardware-latency-and-cost-thresholds.md)
- [Prefer model-portable agentic prompts before fine-tuning](prefer-model-portable-agentic-prompts-before-fine-tuning.md)
- [Product harnesses can become model customization environments](product-harnesses-can-become-model-customization-environments.md)
- [Sequence Harness Engineering and Fine-Tuning by Feedback Speed](sequence-harness-engineering-and-finetuning-by-feedback-speed.md)

Sources:
- [What Lies Beneath the API — Benjamin Cowen, Modal](../sources/20260602_HvZXAOZ3iv8.md), 01:55-12:06
- [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](../sources/20260812_CvRngaQZQ3Y.md), 09:20-09:48, 15:58-16:51
