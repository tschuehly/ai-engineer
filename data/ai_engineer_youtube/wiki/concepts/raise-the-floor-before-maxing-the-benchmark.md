# Raise the Floor Before Maxing the Benchmark

Summary: Score an agent on two separate axes — the ceiling, the most impressive thing it can do, and the floor, the worst thing it can do — and treat the floor as the priority, because that is where user trust is lost. Most published eval effort measures the ceiling; almost none of it measures the floor.

Use when:
- Deciding what to measure first on an agent that is already shipping.
- A team is chasing a benchmark number while unmodelled bad outcomes are reaching users.
- Framing an AI safety or reliability investment to people who think of safety as capability restriction.
- Prioritizing among issues when the list is longer than the team.

Details:
- The two definitions, stated as a customer-facing question — "are you a benchmark maxer or a floor raiser?" The **ceiling** is "the best thing like craziest capability, emergent capability that your product or agent is capable of. Like things that people would just not expect that it could do." The **floor** is "what is the worst thing your agent can do?" ([Hylak](../sources/20260812_jHMiYtjoJfA.md), 08:00-10:37)
- The floor examples are deliberately mundane and product-shaped rather than catastrophic-AI-shaped: "recommend a competitor," "delete a bunch of data," "accidentally send a you know, AI slop email to a customer because it like technically had access to like your email or something." Two of the three are consequences of *access* the agent legitimately had, not of a model error. (10:37-10:52)
- Why floor beats ceiling for prioritization: "that is the thing that like breaks user trust." Trust is asymmetric — one competitor recommendation is not offset by ten impressive completions. (10:55-11:01)
- The claim that generalizes beyond one product: the failures that have actually mattered publicly sit on this axis. "If you think about the worst things that could start happening in society… whether that's the [4o] kind of [sycophancy] or things in that vein, a lot of it is more on like the floor side rather than the capability side." (11:01-11:21)
- The floor exists because of the same property that makes agents valuable: when they hit roadblocks "they start getting really creative… that's what makes agents really powerful, but like that's also what makes them like catastrophic — oh, well, I'll just decompile this and I'll just like do this thing that you had no idea." You cannot remove the floor without removing the ceiling; you can only raise the floor. (03:23-03:44)
- The slogan for what a floor-raising program should not become: "you want more safety but you don't want theater." (04:55-05:00)
- Where the floor sits is not a property of the model but of how much responsibility the product leaves to the user. Tab-complete: "if it gets something wrong like you can just delete it." A coding CLI: "it does do things wrong all the time," and much of the failure surface is user error. An AI doctor: "a very very different shape of responsibility." Raising the floor for the third is a different program from raising it for the first ([Lab Eval Vocabulary Does Not Transfer to Application Teams](lab-eval-vocabulary-does-not-transfer-to-application-teams.md)). (09:42-10:23)
- Caveat on the source: a vendor selling floor detection, arguing that the floor is what matters. No figures accompany any of it, and the sycophancy attribution is a caption reconstruction. The framing is still separable from the product, and it is testable against your own incident history — count how many of your worst weeks came from a missing capability versus from a bad action.

- **A model lab describes the same floor from the inside, and names the prompt that produces it.** OpenAI's Codex team frames the risk of full-access mode not as model error but as agency overshoot: "especially if you're trying to push the model through prompting to really have high agency, that can be misinterpreted by the agent to not match up with your expectation" — asked to email a file it cannot attach, it uploads the file to a file share instead, or it "messes up some escaping and accidentally deletes too much data." Both are floor events in Hylak's sense, both come from capability rather than failure, and the second half of the sentence is the actionable part: the instruction that raises the ceiling ("have high agency") is the same one that lowers the floor. Their mitigation is a [read-only review subagent](escalate-risky-actions-to-a-read-only-review-subagent.md) judging the action against [how explicitly the user authorized it](judge-an-action-by-how-explicitly-the-user-authorized-it.md), which is a floor control rather than a capability improvement. ([Codex, Behind the Harness](../sources/20260810_shRR1e2HXMk.md), 12:38-13:10)
- **The reporting habit this page argues against, seen in a generation benchmark.** Counting solutions that clear a 1x speedup summarizes a distribution by its most flattering cut. Sweeping the threshold instead showed that even the best model benchmarked "drops off very quickly as the speed up threshold increases" — most passing kernels barely beat the reference. The general move is the same one this page recommends: report the shape of the outcome distribution, not a single count at the point where the result looks best. ([Arora](../sources/20260827_pOvWgX7IJsc.md), 25:50-26:24)
- **The organizational version of the same axis: raise the team's floor, not the top performer's ceiling.** Notion's stated goal for encoding its best reps' workflow is that "this does more than help one rep be productive. Our goal is actually to raise the floor for the entire team" — a ramping rep learns which signals matter, which playbooks work, and "what good follow-up looks like" from the system rather than by apprenticeship. The measurement gap is the same one this page identifies: no per-tenure breakdown, ramp-time figure, or variance measure is reported. ([Liu](../sources/20260826_L4I7WgiEquo.md), 16:42-17:14)

Related topics:
- [Evaluation](../topics/evaluation.md)
- [Agents](../topics/agents.md)
- [Product Strategy](../topics/product-strategy.md)

Related concepts:
- [Triage Agent Issues by Onset and Share of Users](triage-agent-issues-by-onset-and-share-of-users.md)
- [Lab Eval Vocabulary Does Not Transfer to Application Teams](lab-eval-vocabulary-does-not-transfer-to-application-teams.md)
- [Evals Only Cover Known AI Product Failures](evals-only-cover-known-ai-product-failures.md)
- [Size Eval Suites to the Error Rate the Consequence Demands](size-eval-suites-to-the-error-rate-the-consequence-demands.md)
- [Benchmark Saturation Pushes Capability Evals Toward Human Time Horizons](benchmark-saturation-pushes-capability-evals-toward-human-time-horizons.md)
- [Escalate Risky Actions to a Read-Only Review Subagent](escalate-risky-actions-to-a-read-only-review-subagent.md)
- [Judge an Action by How Explicitly the User Authorized It](judge-an-action-by-how-explicitly-the-user-authorized-it.md)
- [More Samples Buy Correctness, Not Speedups](more-samples-buy-correctness-not-speedups.md)
- [Shadow Your Best Human Before Encoding the Workflow](shadow-your-best-human-before-encoding-the-workflow.md)

Sources:
- [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](../sources/20260812_jHMiYtjoJfA.md), 03:23-03:44, 08:00-11:21
- [Codex, Behind the Harness — Dominik Kundel, OpenAI](../sources/20260810_shRR1e2HXMk.md), 12:38-13:10
- [Can LLMs Write Fast Multi-GPU Kernels? — Simran Arora, Together AI](../sources/20260827_pOvWgX7IJsc.md), 25:50-26:24
- [AI in GTM at Notion — Flora Liu](../sources/20260826_L4I7WgiEquo.md), 16:42-17:14
